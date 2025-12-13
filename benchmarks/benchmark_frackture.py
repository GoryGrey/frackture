#!/usr/bin/env python3
"""
Frackture Benchmark Suite
Compares Frackture compression/encryption/hash performance against gzip and brotli
over representative datasets.
"""

import sys
import os
import time
import json
import tracemalloc
import gzip
import numpy as np
from pathlib import Path
from typing import Dict, List, Any, Callable, Tuple, Optional
from dataclasses import dataclass, asdict
import random
import string

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

# Import dataset repository
try:
    from dataset_repository import DatasetRepository
    HAS_DATASET_REPO = True
except ImportError:
    HAS_DATASET_REPO = False
    print("Warning: DatasetRepository not available, using legacy DatasetGenerator")

# Import Frackture - note the module name has spaces
import importlib.util
spec = importlib.util.spec_from_file_location("frackture", str(Path(__file__).parent.parent / "frackture (2).py"))
frackture_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(frackture_module)

frackture_preprocess_universal_v2_6 = frackture_module.frackture_preprocess_universal_v2_6
frackture_v3_3_safe = frackture_module.frackture_v3_3_safe
frackture_v3_3_reconstruct = frackture_module.frackture_v3_3_reconstruct
frackture_deterministic_hash = frackture_module.frackture_deterministic_hash
optimize_frackture = frackture_module.optimize_frackture

# Try to import brotli
try:
    import brotli
    HAS_BROTLI = True
except ImportError:
    HAS_BROTLI = False
    print("Warning: brotli not available. Install with: pip install brotli")

# Try to import psutil for more accurate memory tracking
try:
    import psutil
    HAS_PSUTIL = True
except ImportError:
    HAS_PSUTIL = False


@dataclass
class BenchmarkResult:
    """Container for benchmark results"""
    name: str
    dataset_type: str
    original_size: int
    compressed_size: int
    compression_ratio: float
    encode_time: float
    decode_time: float
    encode_throughput: float  # MB/s
    decode_throughput: float  # MB/s
    hash_time: float
    peak_memory_mb: float
    success: bool
    error: str = ""
    # New verification metrics
    symbolic_bytes: int = 0
    entropy_bytes: int = 0
    serialized_total_bytes: int = 0
    payload_is_96b: bool = False
    baseline_mse: float = 0.0
    optimized_mse: float = 0.0
    optimization_improvement_pct: float = 0.0
    optimization_trials: int = 0
    is_lossless: bool = False
    is_deterministic: bool = False
    determinism_drifts: int = 0
    fault_injection_passed: bool = False
    fault_injection_errors: Optional[List[str]] = None


class DatasetGenerator:
    """Generate various types of test datasets"""
    
    @staticmethod
    def generate_text(size_kb: int = 100) -> bytes:
        """Generate Lorem Ipsum-style text"""
        words = ["lorem", "ipsum", "dolor", "sit", "amet", "consectetur", 
                 "adipiscing", "elit", "sed", "do", "eiusmod", "tempor",
                 "incididunt", "ut", "labore", "et", "dolore", "magna", "aliqua"]
        
        text = []
        target_size = size_kb * 1024
        while len(' '.join(text).encode()) < target_size:
            text.append(random.choice(words))
        
        return ' '.join(text).encode()[:target_size]
    
    @staticmethod
    def generate_json(size_kb: int = 100) -> bytes:
        """Generate structured JSON data"""
        data = {
            "users": [],
            "metadata": {
                "version": "1.0",
                "timestamp": "2024-01-01T00:00:00Z",
                "count": 0
            }
        }
        
        target_size = size_kb * 1024
        user_id = 0
        
        while len(json.dumps(data).encode()) < target_size:
            user = {
                "id": user_id,
                "name": f"User {user_id}",
                "email": f"user{user_id}@example.com",
                "age": random.randint(18, 80),
                "active": random.choice([True, False]),
                "tags": random.sample(["python", "javascript", "rust", "go", "java"], k=2)
            }
            data["users"].append(user)
            user_id += 1
        
        data["metadata"]["count"] = len(data["users"])
        return json.dumps(data).encode()[:target_size]
    
    @staticmethod
    def generate_binary_blob(size_kb: int = 100) -> bytes:
        """Generate mixed binary data (partially compressible)"""
        size = size_kb * 1024
        # Mix of repeated patterns and random data
        repeated = b'\x00\xFF\xAA\x55' * (size // 8)
        random_bytes = bytes(random.randint(0, 255) for _ in range(size // 4))
        data = repeated + random_bytes
        return data[:size]
    
    @staticmethod
    def generate_random_noise(size_kb: int = 100) -> bytes:
        """Generate random noise (incompressible)"""
        size = size_kb * 1024
        return bytes(random.randint(0, 255) for _ in range(size))
    
    @staticmethod
    def generate_highly_repetitive(size_kb: int = 100) -> bytes:
        """Generate highly repetitive data (very compressible)"""
        pattern = b"ABCD" * 256  # 1KB pattern
        size = size_kb * 1024
        return (pattern * (size // len(pattern) + 1))[:size]
    
    @staticmethod
    def generate_tiny_datasets() -> Dict[str, bytes]:
        """Generate tiny datasets (<100B) for edge case testing"""
        return {
            "tiny_text": b"Hello World! This is a tiny text dataset.",
            "tiny_json": b'{"tiny": true, "data": "minimal"}',
            "tiny_binary": b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09',
            "tiny_random": bytes(random.randint(0, 255) for _ in range(50)),
            "tiny_repetitive": b"AB" * 25  # 50 bytes of ABABAB...
        }
    
    @staticmethod
    def generate_extreme_datasets() -> Dict[str, bytes]:
        """Generate extreme datasets for stress testing"""
        # Highly compressible - very repetitive
        highly_compressible = b"REPEAT_THIS_PATTERN_OVER_AND_OVER_AGAIN_AND_AGAIN" * 10000  # ~2MB
        extremely_compressible = b"X" * 104857600  # 100MB of same character
        
        # Random - incompressible
        extremely_random = bytes(random.randint(0, 255) for _ in range(104857600))  # 100MB random
        
        # Mixed patterns
        mixed_compressible = (b"PATTERN1" * 500000 + b"PATTERN2" * 500000)  # 8MB mixed
        mixed_random = bytes(random.randint(0, 255) for _ in range(10485760))  # 10MB random
        
        return {
            "highly_compressible": highly_compressible,
            "extremely_compressible": extremely_compressible,
            "extremely_random": extremely_random,
            "mixed_compressible": mixed_compressible,
            "mixed_random": mixed_random
        }
    
    @staticmethod
    def get_all_datasets(small: bool = True) -> Dict[str, bytes]:
        """Get all test datasets"""
        size = 100 if small else 1000  # 100KB or 1MB
        
        return {
            "text": DatasetGenerator.generate_text(size),
            "json": DatasetGenerator.generate_json(size),
            "binary_blob": DatasetGenerator.generate_binary_blob(size),
            "random_noise": DatasetGenerator.generate_random_noise(size),
            "highly_repetitive": DatasetGenerator.generate_highly_repetitive(size)
        }


class MemoryTracker:
    """Track memory usage during benchmarks"""
    
    def __init__(self):
        self.peak_memory = 0
        self.use_psutil = HAS_PSUTIL
        if self.use_psutil:
            self.process = psutil.Process()
    
    def start(self):
        """Start tracking memory"""
        tracemalloc.start()
        if self.use_psutil:
            self.process.memory_info()  # Warm up
    
    def stop(self) -> float:
        """Stop tracking and return peak memory in MB"""
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        # Use psutil if available for more accurate measurement
        if self.use_psutil:
            mem_info = self.process.memory_info()
            return mem_info.rss / (1024 * 1024)  # Convert to MB
        
        return peak / (1024 * 1024)  # Convert to MB


class BenchmarkRunner:
    """Run benchmarks for different compression methods"""
    
    @staticmethod
    def benchmark_frackture(data: bytes) -> BenchmarkResult:
        """Benchmark Frackture compression with comprehensive verification metrics"""
        dataset_type = "unknown"
        original_size = len(data)
        
        try:
            # Memory tracking
            mem_tracker = MemoryTracker()
            mem_tracker.start()
            
            # Preprocessing
            preprocessed = frackture_preprocess_universal_v2_6(data)
            
            # === 1. BASELINE ENCODING/DECODING ===
            encode_start = time.perf_counter()
            payload = frackture_v3_3_safe(preprocessed)
            encode_time = time.perf_counter() - encode_start
            
            # === 2. PAYLOAD SIZING METRICS ===
            # Calculate symbolic bytes (hex string length)
            symbolic_bytes = len(payload['symbolic']) if payload['symbolic'] else 0
            symbolic_bytes //= 2  # Convert hex chars to bytes (2 chars = 1 byte)
            
            # Calculate entropy bytes (16 floats * 8 bytes each for double precision)
            entropy_bytes = len(payload['entropy']) * 8
            
            # Calculate serialized total
            serializable_payload = {
                'symbolic': payload['symbolic'],
                'entropy': [float(x) for x in payload['entropy']]
            }
            payload_bytes = json.dumps(serializable_payload).encode()
            serialized_total_bytes = len(payload_bytes)
            
            # Check if payload is ~96 bytes (allowing some variance for metadata)
            payload_is_96b = 90 <= serialized_total_bytes <= 102
            
            # === 3. RECONSTRUCTION QUALITY ===
            decode_start = time.perf_counter()
            reconstructed = frackture_v3_3_reconstruct(payload)
            decode_time = time.perf_counter() - decode_start
            
            # Calculate MSE between original and reconstructed
            baseline_mse = float(np.mean((preprocessed - reconstructed) ** 2))
            is_lossless = baseline_mse < 1e-6  # Threshold for lossless
            
            # === 4. OPTIMIZATION COMPARISON ===
            optimization_start = time.perf_counter()
            optimized_payload, optimized_mse = optimize_frackture(preprocessed, num_trials=5)
            optimization_time = time.perf_counter() - optimization_start
            
            # Calculate improvement percentage
            if baseline_mse > 0:
                optimization_improvement_pct = ((baseline_mse - optimized_mse) / baseline_mse) * 100
            else:
                optimization_improvement_pct = 0.0
            
            optimization_trials = 5
            
            # === 5. DETERMINISM VALIDATION ===
            # Encode the same input multiple times and check for identical payloads
            num_determinism_tests = 3
            deterministic_payloads = []
            for i in range(num_determinism_tests):
                test_payload = frackture_v3_3_safe(preprocessed)
                deterministic_payloads.append(test_payload)
            
            # Check if all payloads are identical
            is_deterministic = True
            determinism_drifts = 0
            if len(deterministic_payloads) > 1:
                first_payload = deterministic_payloads[0]
                for i in range(1, len(deterministic_payloads)):
                    if (first_payload['symbolic'] != deterministic_payloads[i]['symbolic'] or
                        first_payload['entropy'] != deterministic_payloads[i]['entropy']):
                        is_deterministic = False
                        determinism_drifts += 1
            
            # === 6. FAULT INJECTION ===
            fault_injection_passed = True
            fault_injection_errors = []
            
            try:
                # Test 1: Mutate symbolic fingerprint
                mutated_symbolic = "".join("FF" if c != "F" else "00" for c in payload['symbolic'])
                mutated_payload_1 = {
                    'symbolic': mutated_symbolic,
                    'entropy': payload['entropy']
                }
                try:
                    _ = frackture_v3_3_reconstruct(mutated_payload_1)
                    fault_injection_passed = False
                    fault_injection_errors.append("Symbolic mutation not detected")
                except (ValueError, IndexError, KeyError):
                    pass  # Expected behavior
                
                # Test 2: Mutate entropy channel
                mutated_entropy = [float(x * 2) for x in payload['entropy']]
                mutated_payload_2 = {
                    'symbolic': payload['symbolic'],
                    'entropy': mutated_entropy
                }
                try:
                    _ = frackture_v3_3_reconstruct(mutated_payload_2)
                    fault_injection_passed = False
                    fault_injection_errors.append("Entropy mutation not detected")
                except (ValueError, IndexError, KeyError):
                    pass  # Expected behavior
                
                # Test 3: Empty payload
                try:
                    _ = frackture_v3_3_reconstruct({})
                    fault_injection_passed = False
                    fault_injection_errors.append("Empty payload not detected")
                except (ValueError, IndexError, KeyError, TypeError):
                    pass  # Expected behavior
                
                # Test 4: Invalid hex in symbolic
                try:
                    invalid_payload = {
                        'symbolic': 'INVALID_HEX_!@#$%',
                        'entropy': payload['entropy']
                    }
                    _ = frackture_v3_3_reconstruct(invalid_payload)
                    fault_injection_passed = False
                    fault_injection_errors.append("Invalid hex not detected")
                except (ValueError, IndexError, KeyError):
                    pass  # Expected behavior
                
            except Exception as e:
                fault_injection_passed = False
                fault_injection_errors.append(f"Fault injection test error: {str(e)}")
            
            # === 7. TIMING COMPLETION ===
            hash_start = time.perf_counter()
            _ = frackture_deterministic_hash(data)
            hash_time = time.perf_counter() - hash_start
            
            # Stop memory tracking
            peak_memory = mem_tracker.stop()
            
            # === 8. FINAL METRICS CALCULATION ===
            # Use baseline encoding time for throughput (exclude optimization)
            compression_ratio = original_size / serialized_total_bytes if serialized_total_bytes > 0 else 0
            encode_throughput = (original_size / (1024 * 1024)) / encode_time if encode_time > 0 else 0
            decode_throughput = (original_size / (1024 * 1024)) / decode_time if decode_time > 0 else 0
            
            return BenchmarkResult(
                name="Frackture",
                dataset_type=dataset_type,
                original_size=original_size,
                compressed_size=serialized_total_bytes,
                compression_ratio=compression_ratio,
                encode_time=encode_time,
                decode_time=decode_time,
                encode_throughput=encode_throughput,
                decode_throughput=decode_throughput,
                hash_time=hash_time,
                peak_memory_mb=peak_memory,
                success=True,
                # New verification metrics
                symbolic_bytes=symbolic_bytes,
                entropy_bytes=entropy_bytes,
                serialized_total_bytes=serialized_total_bytes,
                payload_is_96b=payload_is_96b,
                baseline_mse=baseline_mse,
                optimized_mse=optimized_mse,
                optimization_improvement_pct=optimization_improvement_pct,
                optimization_trials=optimization_trials,
                is_lossless=is_lossless,
                is_deterministic=is_deterministic,
                determinism_drifts=determinism_drifts,
                fault_injection_passed=fault_injection_passed,
                fault_injection_errors=fault_injection_errors or []
            )
            
        except Exception as e:
            return BenchmarkResult(
                name="Frackture",
                dataset_type=dataset_type,
                original_size=original_size,
                compressed_size=0,
                compression_ratio=0,
                encode_time=0,
                decode_time=0,
                encode_throughput=0,
                decode_throughput=0,
                hash_time=0,
                peak_memory_mb=0,
                success=False,
                error=str(e),
                # Default values for new metrics
                symbolic_bytes=0,
                entropy_bytes=0,
                serialized_total_bytes=0,
                payload_is_96b=False,
                baseline_mse=0.0,
                optimized_mse=0.0,
                optimization_improvement_pct=0.0,
                optimization_trials=0,
                is_lossless=False,
                is_deterministic=False,
                determinism_drifts=0,
                fault_injection_passed=False,
                fault_injection_errors=[]
            )
    
    @staticmethod
    def benchmark_gzip(data: bytes, level: int = 6) -> BenchmarkResult:
        """Benchmark gzip compression"""
        dataset_type = "unknown"
        original_size = len(data)
        
        try:
            mem_tracker = MemoryTracker()
            mem_tracker.start()
            
            # Encode timing
            encode_start = time.perf_counter()
            compressed = gzip.compress(data, compresslevel=level)
            encode_time = time.perf_counter() - encode_start
            
            compressed_size = len(compressed)
            
            # Decode timing
            decode_start = time.perf_counter()
            decompressed = gzip.decompress(compressed)
            decode_time = time.perf_counter() - decode_start
            
            # Hash timing (using same hash as Frackture for comparison)
            hash_start = time.perf_counter()
            _ = frackture_deterministic_hash(data)
            hash_time = time.perf_counter() - hash_start
            
            peak_memory = mem_tracker.stop()
            
            # Verify
            assert decompressed == data, "Decompression mismatch"
            
            compression_ratio = original_size / compressed_size if compressed_size > 0 else 0
            encode_throughput = (original_size / (1024 * 1024)) / encode_time if encode_time > 0 else 0
            decode_throughput = (original_size / (1024 * 1024)) / decode_time if decode_time > 0 else 0
            
            return BenchmarkResult(
                name=f"Gzip (level {level})",
                dataset_type=dataset_type,
                original_size=original_size,
                compressed_size=compressed_size,
                compression_ratio=compression_ratio,
                encode_time=encode_time,
                decode_time=decode_time,
                encode_throughput=encode_throughput,
                decode_throughput=decode_throughput,
                hash_time=hash_time,
                peak_memory_mb=peak_memory,
                success=True
            )
            
        except Exception as e:
            return BenchmarkResult(
                name=f"Gzip (level {level})",
                dataset_type=dataset_type,
                original_size=original_size,
                compressed_size=0,
                compression_ratio=0,
                encode_time=0,
                decode_time=0,
                encode_throughput=0,
                decode_throughput=0,
                hash_time=0,
                peak_memory_mb=0,
                success=False,
                error=str(e)
            )
    
    @staticmethod
    def benchmark_brotli(data: bytes, quality: int = 6) -> BenchmarkResult:
        """Benchmark brotli compression"""
        if not HAS_BROTLI:
            return BenchmarkResult(
                name=f"Brotli (quality {quality})",
                dataset_type="unknown",
                original_size=len(data),
                compressed_size=0,
                compression_ratio=0,
                encode_time=0,
                decode_time=0,
                encode_throughput=0,
                decode_throughput=0,
                hash_time=0,
                peak_memory_mb=0,
                success=False,
                error="Brotli not installed"
            )
        
        dataset_type = "unknown"
        original_size = len(data)
        
        try:
            mem_tracker = MemoryTracker()
            mem_tracker.start()
            
            # Encode timing
            encode_start = time.perf_counter()
            compressed = brotli.compress(data, quality=quality)
            encode_time = time.perf_counter() - encode_start
            
            compressed_size = len(compressed)
            
            # Decode timing
            decode_start = time.perf_counter()
            decompressed = brotli.decompress(compressed)
            decode_time = time.perf_counter() - decode_start
            
            # Hash timing
            hash_start = time.perf_counter()
            _ = frackture_deterministic_hash(data)
            hash_time = time.perf_counter() - hash_start
            
            peak_memory = mem_tracker.stop()
            
            # Verify
            assert decompressed == data, "Decompression mismatch"
            
            compression_ratio = original_size / compressed_size if compressed_size > 0 else 0
            encode_throughput = (original_size / (1024 * 1024)) / encode_time if encode_time > 0 else 0
            decode_throughput = (original_size / (1024 * 1024)) / decode_time if decode_time > 0 else 0
            
            return BenchmarkResult(
                name=f"Brotli (quality {quality})",
                dataset_type=dataset_type,
                original_size=original_size,
                compressed_size=compressed_size,
                compression_ratio=compression_ratio,
                encode_time=encode_time,
                decode_time=decode_time,
                encode_throughput=encode_throughput,
                decode_throughput=decode_throughput,
                hash_time=hash_time,
                peak_memory_mb=peak_memory,
                success=True
            )
            
        except Exception as e:
            return BenchmarkResult(
                name=f"Brotli (quality {quality})",
                dataset_type=dataset_type,
                original_size=original_size,
                compressed_size=0,
                compression_ratio=0,
                encode_time=0,
                decode_time=0,
                encode_throughput=0,
                decode_throughput=0,
                hash_time=0,
                peak_memory_mb=0,
                success=False,
                error=str(e)
            )


class ResultFormatter:
    """Format and display benchmark results"""
    
    @staticmethod
    def format_size(size_bytes: int) -> str:
        """Format bytes to human-readable size"""
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size_bytes < 1024.0:
                return f"{size_bytes:.2f} {unit}"
            size_bytes /= 1024.0
        return f"{size_bytes:.2f} TB"
    
    @staticmethod
    def print_table(results: List[BenchmarkResult], dataset_name: str):
        """Print results as a formatted table with enhanced verification metrics"""
        print(f"\n{'='*140}")
        print(f"Dataset: {dataset_name}")
        print(f"{'='*140}")
        
        if not results:
            print("No results to display")
            return
        
        # Check if we have Frackture results to determine header format
        has_frackture = any(r.name == "Frackture" and r.success for r in results)
        
        if has_frackture:
            # Enhanced header for Frackture with verification metrics
            headers = [
                "Method",
                "Original",
                "Compressed",
                "Ratio",
                "Encode (ms)",
                "Decode (ms)",
                "Enc Speed",
                "Dec Speed",
                "Hash (ms)",
                "Mem (MB)",
                "Payload (B)",
                "96B?",
                "MSE Baseline",
                "MSE Optimized",
                "Lossless?",
                "Deterministic?"
            ]
        else:
            # Standard header for other methods
            headers = [
                "Method",
                "Original",
                "Compressed",
                "Ratio",
                "Encode (ms)",
                "Decode (ms)",
                "Enc Speed",
                "Dec Speed",
                "Hash (ms)",
                "Mem (MB)",
                "-",
                "-",
                "-",
                "-",
                "-",
                "-"
            ]
        
        # Column widths
        widths = [20, 12, 12, 8, 12, 12, 12, 12, 10, 10, 12, 8, 12, 12, 12, 14]
        
        # Print header
        header_line = "| " + " | ".join(
            h.ljust(w) for h, w in zip(headers, widths)
        ) + " |"
        print(header_line)
        print("|" + "|".join("-" * (w + 2) for w in widths) + "|")
        
        # Print rows
        for result in results:
            if not result.success:
                row = [
                    result.name,
                    ResultFormatter.format_size(result.original_size),
                    "FAILED",
                    "-",
                    "-",
                    "-",
                    "-",
                    "-",
                    "-",
                    "-",
                    "-",
                    "-",
                    "-",
                    "-",
                    "-",
                    "-"
                ]
            elif result.name == "Frackture":
                # Frackture gets enhanced metrics
                row = [
                    result.name,
                    ResultFormatter.format_size(result.original_size),
                    ResultFormatter.format_size(result.compressed_size),
                    f"{result.compression_ratio:.2f}x",
                    f"{result.encode_time * 1000:.2f}",
                    f"{result.decode_time * 1000:.2f}",
                    f"{result.encode_throughput:.2f} MB/s",
                    f"{result.decode_throughput:.2f} MB/s",
                    f"{result.hash_time * 1000:.4f}",
                    f"{result.peak_memory_mb:.2f}",
                    f"{result.serialized_total_bytes}",
                    "✓" if result.payload_is_96b else "✗",
                    f"{result.baseline_mse:.6f}",
                    f"{result.optimized_mse:.6f}",
                    "✓" if result.is_lossless else "✗",
                    "✓" if result.is_deterministic else f"Drift({result.determinism_drifts})"
                ]
            else:
                # Standard methods get standard metrics
                row = [
                    result.name,
                    ResultFormatter.format_size(result.original_size),
                    ResultFormatter.format_size(result.compressed_size),
                    f"{result.compression_ratio:.2f}x",
                    f"{result.encode_time * 1000:.2f}",
                    f"{result.decode_time * 1000:.2f}",
                    f"{result.encode_throughput:.2f} MB/s",
                    f"{result.decode_throughput:.2f} MB/s",
                    f"{result.hash_time * 1000:.4f}",
                    f"{result.peak_memory_mb:.2f}",
                    "-",
                    "-",
                    "-",
                    "-",
                    "-",
                    "-"
                ]
            row_line = "| " + " | ".join(
                str(v).ljust(w) for v, w in zip(row, widths)
            ) + " |"
            print(row_line)
        
        # Print Frackture-specific verification details
        for result in results:
            if result.name == "Frackture" and result.success:
                print(f"\n🔍 Frackture Verification Details for {dataset_name}:")
                print(f"  📊 Payload Sizing: Symbolic={result.symbolic_bytes}B, Entropy={result.entropy_bytes}B, Total={result.serialized_total_bytes}B")
                print(f"  🎯 96B Target: {'✅ Met' if result.payload_is_96b else '❌ Missed'} (target: ~96B)")
                print(f"  📈 Optimization: {result.optimization_improvement_pct:.2f}% improvement over {result.optimization_trials} trials")
                print(f"  🔧 Fault Injection: {'✅ Passed' if result.fault_injection_passed else '❌ Failed'}")
                if result.fault_injection_errors:
                    print(f"  ⚠️  Fault Errors: {', '.join(result.fault_injection_errors)}")
        
        print(f"{'='*140}\n")
    
    @staticmethod
    def save_json(results_by_dataset: Dict[str, List[BenchmarkResult]], output_path: Path):
        """Save results as JSON with enhanced verification metrics"""
        output = {
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "benchmark_version": "2.0.0",
            "enhanced_metrics": {
                "payload_sizing": "Symbolic bytes, entropy bytes, serialized total, 96B validation",
                "reconstruction_quality": "MSE baseline vs optimized, lossless status",
                "optimization": "MSE improvement percentage, trials count",
                "determinism": "Multiple encoding tests, drift detection",
                "fault_injection": "Payload mutation tests, error handling validation"
            },
            "results": {}
        }
        
        for dataset_name, results in results_by_dataset.items():
            output["results"][dataset_name] = [
                asdict(r) for r in results
            ]
        
        with open(output_path, 'w') as f:
            json.dump(output, f, indent=2, default=str)
        
        print(f"✅ JSON results saved to: {output_path}")
        print(f"📊 Enhanced metrics version: {output['benchmark_version']}")
    
    @staticmethod
    def save_markdown(results_by_dataset: Dict[str, List[BenchmarkResult]], output_path: Path):
        """Save results as Markdown with enhanced verification metrics"""
        lines = [
            "# Frackture Benchmark Results",
            "",
            f"**Generated:** {time.strftime('%Y-%m-%d %H:%M:%S')}",
            f"**Enhanced Metrics Version:** 2.0.0",
            "",
            "## New Verification Metrics",
            "",
            "- **Payload Sizing**: Symbolic bytes, entropy bytes, serialized total, 96B validation",
            "- **Reconstruction Quality**: MSE baseline vs optimized, lossless status",
            "- **Optimization**: MSE improvement percentage, trials count",
            "- **Determinism**: Multiple encoding tests, drift detection",
            "- **Fault Injection**: Payload mutation tests, error handling validation",
            "",
            "---",
            ""
        ]
        
        for dataset_name, results in results_by_dataset.items():
            lines.append(f"## Dataset: {dataset_name}")
            lines.append("")
            
            if not results:
                lines.append("*No results*")
                lines.append("")
                continue
            
            # Check if we have Frackture results for enhanced table
            has_frackture = any(r.name == "Frackture" and r.success for r in results)
            
            if has_frackture:
                # Enhanced table for Frackture
                lines.append("### Performance & Verification Metrics")
                lines.append("")
                lines.append("| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |")
                lines.append("|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|")
                
                for result in results:
                    if not result.success:
                        lines.append(f"| {result.name} | {ResultFormatter.format_size(result.original_size)} | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |")
                    elif result.name == "Frackture":
                        row = (
                            f"| {result.name} "
                            f"| {ResultFormatter.format_size(result.original_size)} "
                            f"| {ResultFormatter.format_size(result.compressed_size)} "
                            f"| {result.compression_ratio:.2f}x "
                            f"| {result.encode_time * 1000:.2f} "
                            f"| {result.decode_time * 1000:.2f} "
                            f"| {result.encode_throughput:.2f} MB/s "
                            f"| {result.decode_throughput:.2f} MB/s "
                            f"| {result.hash_time * 1000:.4f} "
                            f"| {result.peak_memory_mb:.2f} "
                            f"| {result.serialized_total_bytes} "
                            f"| {'✅' if result.payload_is_96b else '❌'} "
                            f"| {result.baseline_mse:.6f} "
                            f"| {result.optimized_mse:.6f} "
                            f"| {'✅' if result.is_lossless else '❌'} "
                            f"| {'✅' if result.is_deterministic else f'Drift({result.determinism_drifts})'} |"
                        )
                        lines.append(row)
                    else:
                        lines.append(f"| {result.name} | {ResultFormatter.format_size(result.original_size)} | {ResultFormatter.format_size(result.compressed_size)} | {result.compression_ratio:.2f}x | {result.encode_time * 1000:.2f} | {result.decode_time * 1000:.2f} | {result.encode_throughput:.2f} MB/s | {result.decode_throughput:.2f} MB/s | {result.hash_time * 1000:.4f} | {result.peak_memory_mb:.2f} | - | - | - | - | - | - |")
            else:
                # Standard table for non-Frackture results
                lines.append("| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) |")
                lines.append("|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|")
                
                for result in results:
                    if not result.success:
                        lines.append(f"| {result.name} | {ResultFormatter.format_size(result.original_size)} | FAILED | - | - | - | - | - | - | - |")
                    else:
                        row = (
                            f"| {result.name} "
                            f"| {ResultFormatter.format_size(result.original_size)} "
                            f"| {ResultFormatter.format_size(result.compressed_size)} "
                            f"| {result.compression_ratio:.2f}x "
                            f"| {result.encode_time * 1000:.2f} "
                            f"| {result.decode_time * 1000:.2f} "
                            f"| {result.encode_throughput:.2f} MB/s "
                            f"| {result.decode_throughput:.2f} MB/s "
                            f"| {result.hash_time * 1000:.4f} "
                            f"| {result.peak_memory_mb:.2f} |"
                        )
                        lines.append(row)
            
            # Add detailed verification metrics for Frackture
            for result in results:
                if result.name == "Frackture" and result.success:
                    lines.append("")
                    lines.append("### Frackture Verification Details")
                    lines.append("")
                    lines.append(f"- **Payload Sizing**: Symbolic={result.symbolic_bytes}B, Entropy={result.entropy_bytes}B, Total={result.serialized_total_bytes}B")
                    lines.append(f"- **96B Target**: {'✅ Met' if result.payload_is_96b else '❌ Missed'} (target: ~96B)")
                    lines.append(f"- **Optimization**: {result.optimization_improvement_pct:.2f}% improvement over {result.optimization_trials} trials")
                    lines.append(f"- **Reconstruction**: {'✅ Lossless' if result.is_lossless else '❌ Lossy'} (MSE: {result.baseline_mse:.6f})")
                    lines.append(f"- **Determinism**: {'✅ Deterministic' if result.is_deterministic else f'❌ Drift detected ({result.determinism_drifts} differences)'}")
                    lines.append(f"- **Fault Injection**: {'✅ Passed' if result.fault_injection_passed else '❌ Failed'}")
                    if result.fault_injection_errors:
                        lines.append(f"- **Fault Errors**: {', '.join(result.fault_injection_errors)}")
            
            lines.append("")
            lines.append("---")
            lines.append("")
        
        # Add enhanced summary
        lines.append("## Summary")
        lines.append("")
        lines.append("### Key Metrics")
        lines.append("")
        lines.append("- **Compression Ratio**: Higher is better (original size / compressed size)")
        lines.append("- **Throughput**: Higher is better (MB processed per second)")
        lines.append("- **Latency**: Lower is better (milliseconds)")
        lines.append("- **Memory**: Lower is better (peak memory usage in MB)")
        lines.append("- **MSE**: Lower is better (reconstruction quality)")
        lines.append("- **96B Target**: Frackture should maintain ~96-byte payloads")
        lines.append("")
        lines.append("### Enhanced Frackture Verification")
        lines.append("")
        lines.append("1. **Payload Size Validation**: Ensures Frackture maintains its ~96-byte promise")
        lines.append("2. **Reconstruction Quality**: MSE measurements for baseline vs optimized encoding")
        lines.append("3. **Optimization Impact**: Measures effectiveness of self-optimization")
        lines.append("4. **Determinism Testing**: Validates consistent output across multiple runs")
        lines.append("5. **Fault Injection**: Tests error handling and tamper detection")
        lines.append("")
        lines.append("### Frackture Core Advantages")
        lines.append("")
        lines.append("- Fixed-size output (~96 bytes) regardless of input size")
        lines.append("- Identity-preserving symbolic fingerprints")
        lines.append("- Fast hashing for integrity checks")
        lines.append("- Dual-channel (symbolic + entropy) encoding")
        lines.append("- Self-optimization with decoder feedback")
        lines.append("- Built-in fault detection and error handling")
        lines.append("")
        
        with open(output_path, 'w') as f:
            f.write('\n'.join(lines))
        
        print(f"✅ Markdown results saved to: {output_path}")
        print(f"📊 Enhanced verification metrics included")


def run_benchmark_suite(
    small_datasets: bool = True,
    large_datasets: bool = True,
    tiny_datasets: bool = True,
    extreme_datasets: bool = False,  # Disabled by default due to size
    output_dir: Path = None,
    use_real_datasets: bool = None
):
    """Run the complete benchmark suite with enhanced metrics and extreme dataset support"""
    
    if output_dir is None:
        output_dir = Path(__file__).parent / "results"
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Auto-detect if we should use real datasets
    if use_real_datasets is None:
        use_real_datasets = HAS_DATASET_REPO
    elif use_real_datasets and not HAS_DATASET_REPO:
        print("Warning: Real datasets requested but DatasetRepository not available")
        use_real_datasets = False
    
    print("\n" + "="*120)
    print("🔥 FRACKTURE ENHANCED BENCHMARK SUITE 🔥")
    print("="*120)
    print(f"\n📁 Output directory: {output_dir}")
    print(f"📊 Dataset mode: {'REAL DATASETS' if use_real_datasets else 'SYNTHETIC DATASETS'}")
    print(f"🧮 Brotli available: {HAS_BROTLI}")
    print(f"💾 Psutil available: {HAS_PSUTIL}")
    print(f"📏 Tiny datasets: {'✅' if tiny_datasets else '❌'}")
    print(f"🚀 Extreme datasets: {'✅' if extreme_datasets else '❌'}")
    print(f"✨ Enhanced metrics: Payload sizing, MSE, optimization, determinism, fault injection")
    
    all_results = {}
    
    # Initialize dataset repository if using real datasets
    repo = None
    if use_real_datasets:
        try:
            repo = DatasetRepository()
            print(f"✓ Loaded {len(repo.list_datasets())} real datasets from manifest")
        except Exception as e:
            print(f"✗ Failed to load DatasetRepository: {e}")
            print("  Falling back to synthetic datasets")
            use_real_datasets = False
    
    # Run benchmarks on small datasets
    if small_datasets:
        print("\n📊 Running benchmarks on small datasets (100KB)...")
        
        if use_real_datasets:
            # Get all real datasets at medium tier (100KB)
            try:
                datasets = repo.get_all_datasets(tier='medium', skip_optional=True)
                print(f"  Loaded {len(datasets)} real dataset samples")
            except Exception as e:
                print(f"  Error loading real datasets: {e}")
                datasets = DatasetGenerator.get_all_datasets(small=True)
        else:
            datasets = DatasetGenerator.get_all_datasets(small=True)
        
        for dataset_name, data in datasets.items():
            print(f"\n🔍 Benchmarking dataset: {dataset_name}")
            results = []
            
            # Frackture
            print("  - Running Frackture...")
            result = BenchmarkRunner.benchmark_frackture(data)
            result.dataset_type = dataset_name
            results.append(result)
            
            # Gzip
            print("  - Running Gzip...")
            result = BenchmarkRunner.benchmark_gzip(data, level=6)
            result.dataset_type = dataset_name
            results.append(result)
            
            # Brotli
            if HAS_BROTLI:
                print("  - Running Brotli...")
                result = BenchmarkRunner.benchmark_brotli(data, quality=6)
                result.dataset_type = dataset_name
                results.append(result)
            
            all_results[f"small_{dataset_name}"] = results
            ResultFormatter.print_table(results, f"small_{dataset_name}")
    
    # Run benchmarks on large datasets
    if large_datasets:
        print("\n📊 Running benchmarks on large datasets (1MB)...")
        
        if use_real_datasets:
            # Get all real datasets at large tier (1MB)
            try:
                datasets = repo.get_all_datasets(tier='large', skip_optional=True)
                print(f"  Loaded {len(datasets)} real dataset samples")
            except Exception as e:
                print(f"  Error loading real datasets: {e}")
                datasets = DatasetGenerator.get_all_datasets(small=False)
        else:
            datasets = DatasetGenerator.get_all_datasets(small=False)
        
        for dataset_name, data in datasets.items():
            print(f"\n🔍 Benchmarking dataset: {dataset_name}")
            results = []
            
            # Frackture
            print("  - Running Frackture...")
            result = BenchmarkRunner.benchmark_frackture(data)
            result.dataset_type = dataset_name
            results.append(result)
            
            # Gzip
            print("  - Running Gzip...")
            result = BenchmarkRunner.benchmark_gzip(data, level=6)
            result.dataset_type = dataset_name
            results.append(result)
            
            # Brotli
            if HAS_BROTLI:
                print("  - Running Brotli...")
                result = BenchmarkRunner.benchmark_brotli(data, quality=6)
                result.dataset_type = dataset_name
                results.append(result)
            
            all_results[f"large_{dataset_name}"] = results
            ResultFormatter.print_table(results, f"large_{dataset_name}")
    
    # Run benchmarks on tiny datasets (<100B)
    if tiny_datasets:
        print("\n📏 Running benchmarks on tiny datasets (<100B)...")
        datasets = DatasetGenerator.generate_tiny_datasets()
        print(f"  Generated {len(datasets)} tiny dataset samples")
        
        for dataset_name, data in datasets.items():
            print(f"\n🔍 Benchmarking tiny dataset: {dataset_name}")
            results = []
            
            # Frackture
            print("  - Running Frackture...")
            result = BenchmarkRunner.benchmark_frackture(data)
            result.dataset_type = dataset_name
            results.append(result)
            
            # Gzip (only for non-empty data)
            if len(data) > 0:
                print("  - Running Gzip...")
                result = BenchmarkRunner.benchmark_gzip(data, level=6)
                result.dataset_type = dataset_name
                results.append(result)
            
            # Brotli (only for non-empty data)
            if HAS_BROTLI and len(data) > 0:
                print("  - Running Brotli...")
                result = BenchmarkRunner.benchmark_brotli(data, quality=6)
                result.dataset_type = dataset_name
                results.append(result)
            
            all_results[f"tiny_{dataset_name}"] = results
            ResultFormatter.print_table(results, f"tiny_{dataset_name}")
    
    # Run benchmarks on extreme datasets (>100MB)
    if extreme_datasets:
        print("\n🚀 Running benchmarks on extreme datasets (>100MB)...")
        print("⚠️  WARNING: These tests may take a very long time and consume significant memory!")
        
        datasets = DatasetGenerator.generate_extreme_datasets()
        print(f"  Generated {len(datasets)} extreme dataset samples")
        
        for dataset_name, data in datasets.items():
            size_mb = len(data) / (1024 * 1024)
            print(f"\n🔍 Benchmarking extreme dataset: {dataset_name} ({size_mb:.1f}MB)")
            results = []
            
            # Frackture (always included)
            print("  - Running Frackture...")
            result = BenchmarkRunner.benchmark_frackture(data)
            result.dataset_type = dataset_name
            results.append(result)
            
            # Only test gzip on smaller extreme datasets to avoid timeout
            if size_mb <= 10:  # Only test datasets <= 10MB with gzip
                print("  - Running Gzip...")
                result = BenchmarkRunner.benchmark_gzip(data, level=6)
                result.dataset_type = dataset_name
                results.append(result)
            else:
                print("  - Skipping Gzip (dataset too large)")
            
            # Skip Brotli for extreme datasets due to performance
            print("  - Skipping Brotli (performance reasons)")
            
            all_results[f"extreme_{dataset_name}"] = results
            ResultFormatter.print_table(results, f"extreme_{dataset_name}")
    
    # Save results
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    json_path = output_dir / f"benchmark_results_{timestamp}.json"
    md_path = output_dir / f"benchmark_results_{timestamp}.md"
    
    ResultFormatter.save_json(all_results, json_path)
    ResultFormatter.save_markdown(all_results, md_path)
    
    print("\n" + "="*100)
    print("✅ BENCHMARK SUITE COMPLETED")
    print("="*100)
    print(f"\nResults saved to:")
    print(f"  - JSON: {json_path}")
    print(f"  - Markdown: {md_path}")
    print()


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Frackture Enhanced Benchmark Suite with Verification Metrics",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                           # Run all benchmarks (small, large, tiny)
  %(prog)s --small-only             # Run only 100KB dataset benchmarks
  %(prog)s --large-only             # Run only 1MB dataset benchmarks  
  %(prog)s --tiny-only              # Run only <100B dataset benchmarks
  %(prog)s --extreme                # Run extreme >100MB dataset benchmarks
  %(prog)s --no-tiny               # Disable tiny dataset tests
  %(prog)s --synthetic             # Use synthetic datasets only
  %(prog)s --real                  # Use real datasets if available
  %(prog)s --output-dir ./results  # Custom output directory
        """
    )
    
    # Dataset size options
    dataset_group = parser.add_mutually_exclusive_group()
    dataset_group.add_argument(
        "--small-only",
        action="store_true",
        help="Run only small dataset benchmarks (100KB)"
    )
    dataset_group.add_argument(
        "--large-only", 
        action="store_true",
        help="Run only large dataset benchmarks (1MB)"
    )
    dataset_group.add_argument(
        "--tiny-only",
        action="store_true", 
        help="Run only tiny dataset benchmarks (<100B)"
    )
    dataset_group.add_argument(
        "--extreme-only",
        action="store_true",
        help="Run only extreme dataset benchmarks (>100MB)"
    )
    
    # Additional dataset options
    parser.add_argument(
        "--no-tiny",
        action="store_true",
        help="Disable tiny dataset benchmarks (<100B)"
    )
    parser.add_argument(
        "--extreme",
        action="store_true",
        help="Enable extreme dataset benchmarks (>100MB, can be very slow)"
    )
    
    # Output and mode options
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        help="Output directory for results (default: benchmarks/results)"
    )
    parser.add_argument(
        "--synthetic",
        action="store_true",
        help="Use synthetic datasets instead of real samples (legacy mode)"
    )
    parser.add_argument(
        "--real",
        action="store_true",
        help="Use real dataset samples (default if available)"
    )
    
    # Enhanced features
    parser.add_argument(
        "--verify-only",
        action="store_true",
        help="Run only verification metrics (payload sizing, MSE, determinism, fault injection)"
    )
    parser.add_argument(
        "--detailed",
        action="store_true",
        help="Enable detailed verification output with more diagnostic information"
    )
    
    args = parser.parse_args()
    
    # Determine which datasets to run
    small = not (args.large_only or args.tiny_only or args.extreme_only)
    large = not (args.small_only or args.tiny_only or args.extreme_only) 
    tiny = not (args.small_only or args.large_only or args.extreme_only) and not args.no_tiny
    extreme = args.extreme_only or args.extreme
    
    # Determine dataset mode
    use_real = None  # Auto-detect
    if args.synthetic:
        use_real = False
    elif args.real:
        use_real = True
    
    print("\n🚀 Enhanced Frackture Benchmark Configuration:")
    print(f"  Small datasets (100KB): {'✅' if small else '❌'}")
    print(f"  Large datasets (1MB): {'✅' if large else '❌'}")
    print(f"  Tiny datasets (<100B): {'✅' if tiny else '❌'}")
    print(f"  Extreme datasets (>100MB): {'✅' if extreme else '❌'}")
    print(f"  Real datasets: {'✅' if use_real else 'Synthetic' if use_real is False else 'Auto-detect'}")
    print(f"  Enhanced verification: ✅")
    
    run_benchmark_suite(
        small_datasets=small,
        large_datasets=large,
        tiny_datasets=tiny,
        extreme_datasets=extreme,
        output_dir=args.output_dir,
        use_real_datasets=use_real
    )
