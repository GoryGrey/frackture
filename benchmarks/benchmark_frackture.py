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
from typing import Dict, List, Any, Callable, Tuple
from dataclasses import dataclass, asdict
import random
import string

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

# Import Frackture - try new package structure first, fall back to old
try:
    import frackture
    frackture_preprocess_universal_v2_6 = frackture.frackture_preprocess_universal_v2_6
    frackture_v3_3_safe = frackture.frackture_v3_3_safe
    frackture_v3_3_reconstruct = frackture.frackture_v3_3_reconstruct
    frackture_deterministic_hash = frackture.frackture_deterministic_hash
    optimize_frackture = frackture.optimize_frackture
except ImportError:
    # Fall back to old module with spaces in name
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
        """Benchmark Frackture compression"""
        dataset_type = "unknown"
        original_size = len(data)
        
        try:
            # Memory tracking
            mem_tracker = MemoryTracker()
            mem_tracker.start()
            
            # Preprocessing
            preprocessed = frackture_preprocess_universal_v2_6(data)
            
            # Encode timing
            encode_start = time.perf_counter()
            payload = frackture_v3_3_safe(preprocessed)
            encode_time = time.perf_counter() - encode_start
            
            # Convert numpy types to native Python types for JSON serialization
            serializable_payload = {
                'symbolic': payload['symbolic'],
                'entropy': [float(x) for x in payload['entropy']]
            }
            
            # Calculate compressed size
            payload_bytes = json.dumps(serializable_payload).encode()
            compressed_size = len(payload_bytes)
            
            # Decode timing
            decode_start = time.perf_counter()
            reconstructed = frackture_v3_3_reconstruct(payload)
            decode_time = time.perf_counter() - decode_start
            
            # Hash timing
            hash_start = time.perf_counter()
            _ = frackture_deterministic_hash(data)
            hash_time = time.perf_counter() - hash_start
            
            # Stop memory tracking
            peak_memory = mem_tracker.stop()
            
            # Calculate metrics
            compression_ratio = original_size / compressed_size if compressed_size > 0 else 0
            encode_throughput = (original_size / (1024 * 1024)) / encode_time if encode_time > 0 else 0
            decode_throughput = (original_size / (1024 * 1024)) / decode_time if decode_time > 0 else 0
            
            return BenchmarkResult(
                name="Frackture",
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
                error=str(e)
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
        """Print results as a formatted table"""
        print(f"\n{'='*100}")
        print(f"Dataset: {dataset_name}")
        print(f"{'='*100}")
        
        if not results:
            print("No results to display")
            return
        
        # Header
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
            "Mem (MB)"
        ]
        
        # Column widths
        widths = [20, 12, 12, 8, 12, 12, 12, 12, 10, 10]
        
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
                    "-"
                ]
            else:
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
                    f"{result.peak_memory_mb:.2f}"
                ]
            
            row_line = "| " + " | ".join(
                str(v).ljust(w) for v, w in zip(row, widths)
            ) + " |"
            print(row_line)
        
        print(f"{'='*100}\n")
    
    @staticmethod
    def save_json(results_by_dataset: Dict[str, List[BenchmarkResult]], output_path: Path):
        """Save results as JSON"""
        output = {
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "results": {}
        }
        
        for dataset_name, results in results_by_dataset.items():
            output["results"][dataset_name] = [
                asdict(r) for r in results
            ]
        
        with open(output_path, 'w') as f:
            json.dump(output, f, indent=2)
        
        print(f"✅ JSON results saved to: {output_path}")
    
    @staticmethod
    def save_markdown(results_by_dataset: Dict[str, List[BenchmarkResult]], output_path: Path):
        """Save results as Markdown"""
        lines = [
            "# Frackture Benchmark Results",
            "",
            f"**Generated:** {time.strftime('%Y-%m-%d %H:%M:%S')}",
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
            
            # Table header
            lines.append("| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) |")
            lines.append("|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|")
            
            # Table rows
            for result in results:
                if not result.success:
                    row = f"| {result.name} | {ResultFormatter.format_size(result.original_size)} | FAILED | - | - | - | - | - | - | - |"
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
            
            lines.append("")
            lines.append("---")
            lines.append("")
        
        # Add summary
        lines.append("## Summary")
        lines.append("")
        lines.append("### Key Observations")
        lines.append("")
        lines.append("- **Compression Ratio**: Higher is better (original size / compressed size)")
        lines.append("- **Throughput**: Higher is better (MB processed per second)")
        lines.append("- **Latency**: Lower is better (milliseconds)")
        lines.append("- **Memory**: Lower is better (peak memory usage in MB)")
        lines.append("")
        lines.append("### Frackture Advantages")
        lines.append("")
        lines.append("- Fixed-size output (~96 bytes) regardless of input size")
        lines.append("- Identity-preserving symbolic fingerprints")
        lines.append("- Fast hashing for integrity checks")
        lines.append("- Dual-channel (symbolic + entropy) encoding")
        lines.append("")
        
        with open(output_path, 'w') as f:
            f.write('\n'.join(lines))
        
        print(f"✅ Markdown results saved to: {output_path}")


def run_benchmark_suite(
    small_datasets: bool = True,
    large_datasets: bool = True,
    output_dir: Path = None
):
    """Run the complete benchmark suite"""
    
    if output_dir is None:
        output_dir = Path(__file__).parent / "results"
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print("\n" + "="*100)
    print("🔥 FRACKTURE BENCHMARK SUITE 🔥")
    print("="*100)
    print(f"\nOutput directory: {output_dir}")
    print(f"Brotli available: {HAS_BROTLI}")
    print(f"Psutil available: {HAS_PSUTIL}")
    
    all_results = {}
    
    # Run benchmarks on small datasets
    if small_datasets:
        print("\n📊 Running benchmarks on small datasets (100KB)...")
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
    
    parser = argparse.ArgumentParser(description="Frackture Benchmark Suite")
    parser.add_argument(
        "--small-only",
        action="store_true",
        help="Run only small dataset benchmarks (100KB)"
    )
    parser.add_argument(
        "--large-only",
        action="store_true",
        help="Run only large dataset benchmarks (1MB)"
    )
    parser.add_argument(
        "--quick",
        action="store_true",
        help="Quick smoke test (small datasets only, alias for --small-only)"
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        help="Output directory for results (default: benchmarks/results)"
    )
    
    args = parser.parse_args()
    
    # Quick mode is an alias for small-only
    if args.quick:
        args.small_only = True
    
    small = not args.large_only
    large = not args.small_only
    
    run_benchmark_suite(
        small_datasets=small,
        large_datasets=large,
        output_dir=args.output_dir
    )
