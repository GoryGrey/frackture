# Frackture Benchmark Runbook (Phase 1)

This runbook provides step-by-step instructions for executing the comprehensive Frackture benchmark suite. It covers environment setup, dataset management, CLI usage, metric collection, and artifact generation.

## Table of Contents

- [Environment Setup](#environment-setup)
- [Dataset Repository](#dataset-repository)
- [Benchmark Execution](#benchmark-execution)
- [Compression Sweeps](#compression-sweeps)
- [Edge Cases](#edge-cases)
- [Analysis Pipeline](#analysis-pipeline)
- [Metric Requirements](#metric-requirements)
- [Artifact Management](#artifact-management)
- [Troubleshooting](#troubleshooting)

## Environment Setup

### System Requirements

- Python 3.8+
- 4GB+ RAM (8GB+ recommended for extreme tiers)
- 1GB+ disk space for datasets and results

### Dependencies Installation

```bash
# Navigate to project root
cd /path/to/frackture

# Install required dependencies
pip install numpy scipy scikit-learn pytest pytest-cov

# Optional but recommended for full functionality
pip install brotli cryptography psutil pyyaml

# Verify installation
python -c "import brotli, cryptography; print('All dependencies available')"
```

### Project Structure Validation

Ensure the following directory structure exists:

```
frackture/
├── frackture (2).py                 # Core module
├── benchmarks/
│   ├── benchmark_frackture.py       # Main benchmark harness
│   ├── analyze_results.py           # Analysis pipeline
│   ├── dataset_repository.py        # Real dataset management
│   ├── dataset_cli.py               # Dataset exploration CLI
│   ├── datasets/                    # Real dataset samples
│   │   ├── manifest.yaml            # Dataset metadata
│   │   ├── sample_text.txt          # Text samples
│   │   ├── sample_image.png         # Binary samples
│   │   └── ...                      # Other dataset files
│   └── results/                     # Benchmark output directory
└── docs/
    └── benchmark_runbook.md         # This document
```

### Dataset Verification

```bash
# Navigate to benchmarks directory
cd benchmarks

# Validate all datasets are present
python dataset_cli.py test

# List available datasets
python dataset_cli.py list

# Explore dataset categories
python dataset_cli.py categories
```

Expected output: All 15 datasets should be found and validated.

## Dataset Repository

### Understanding Dataset Structure

The benchmark suite uses a real dataset repository with 15 carefully curated samples:

#### Categories
- **text**: Plain text, logs, JSON, CSV files
- **binary**: Images, PDF documents, animations  
- **structured**: Database files, serialized objects
- **code**: JavaScript, Python source files
- **mixed**: Combined payloads from multiple categories

#### Size Tiers
- **tiny**: < 100 bytes (target: 50B)
- **small**: 100B - 10KB (target: 1KB)
- **medium**: 10KB - 500KB (target: 100KB)
- **large**: 500KB - 5MB (target: 1MB)
- **xlarge**: 5MB - 50MB (target: 10MB)
- **xxlarge**: 50MB - 500MB (target: 100MB)
- **huge**: 500MB - 10GB (target: 1GB, optional)

### Dataset Manifest

The `benchmarks/datasets/manifest.yaml` defines:
- Each dataset's properties and scaling rules
- Size tier configurations
- Mixed payload combinations
- Canonical sizes and scaling methods

### Loading Specific Datasets

```python
# Interactive dataset exploration
cd benchmarks
python dataset_cli.py

# Load specific dataset at tier
python -c "
from dataset_repository import DatasetRepository
repo = DatasetRepository()
data = repo.load_dataset('text_plain', 'small')  # 1KB text
print(f'Loaded {len(data)} bytes')
"
```

## Benchmark Execution

### Basic Usage Patterns

#### Standard Benchmarks (Recommended for Most Users)

```bash
# Default: Run small (100KB) and large (1MB) dataset benchmarks
cd benchmarks
python benchmark_frackture.py

# Use real datasets explicitly
python benchmark_frackture.py --real
```

#### Tier-Specific Execution

```bash
# Only small datasets (100KB) - fastest
python benchmark_frackture.py --small-only

# Only large datasets (1MB) - moderate runtime
python benchmark_frackture.py --large-only

# Only tiny datasets (<100B) - quick verification
python benchmark_frackture.py --tiny-only

# Extreme datasets (>100MB) - very slow, use sparingly
python benchmark_frackture.py --extreme

# Full tier sweep (tiny → huge) - comprehensive but slow
python benchmark_frackture.py --all-tiers

# Include 1GB+ tier in full sweep (extremely slow)
python benchmark_frackture.py --all-tiers --include-huge
```

#### Category-Specific Execution

```bash
# Text datasets only
python benchmark_frackture.py --categories text

# Binary and structured datasets
python benchmark_frackture.py --categories binary,structured

# Code datasets only  
python benchmark_frackture.py --categories code

# Mixed payloads
python benchmark_frackture.py --categories mixed

# Multiple categories
python benchmark_frackture.py --categories text,binary,code
```

#### Custom Tier Sets

```bash
# Specific tier subset
python benchmark_frackture.py --tiers tiny,small,medium

# Exclude tiny datasets
python benchmark_frackture.py --no-tiny

# Custom output directory
python benchmark_frackture.py --output-dir ./my_results
```

### Verification-Only Mode

For rapid validation without compression comparisons:

```bash
# Run only verification metrics (payload sizing, MSE, determinism, fault injection)
python benchmark_frackture.py --verify-only

# With detailed diagnostic output
python benchmark_frackture.py --verify-only --detailed
```

### Synthetic vs Real Datasets

```bash
# Use synthetic datasets (legacy mode, faster)
python benchmark_frackture.py --synthetic

# Use real datasets (recommended)
python benchmark_frackture.py --real

# Auto-detect (default behavior)
python benchmark_frackture.py  # Uses real if available
```

## Compression Sweeps

### Gzip Compression Level Sweeps

#### Single Level (Default Behavior)

```bash
# Default level 6
python benchmark_frackture.py

# Explicit level
python benchmark_frackture.py --gzip-level 9
```

#### Multi-Level Sweeps

```bash
# Sweep specific levels
python benchmark_frackture.py --gzip-levels 1 6 9

# Sweep all levels (comprehensive)
python benchmark_frackture.py --gzip-levels 1 2 3 4 5 6 7 8 9

# Combined with tier selection
python benchmark_frackture.py --small-only --gzip-levels 1 9
```

### Brotli Quality Sweeps

#### Single Quality

```bash
# Default quality
python benchmark_frackture.py

# Explicit quality
python benchmark_frackture.py --brotli-quality 11
```

#### Multi-Quality Sweeps

```bash
# Sweep specific qualities
python benchmark_frackture.py --brotli-qualities 4 6 11

# Sweep full range (comprehensive)
python benchmark_frackture.py --brotli-qualities 0 1 2 3 4 5 6 7 8 9 10 11

# Combined with gzip sweep
python benchmark_frackture.py --gzip-levels 1 6 9 --brotli-qualities 4 6 11
```

### Comprehensive Comparison

```bash
# Full compression sweep on small datasets
python benchmark_frackture.py \
  --small-only \
  --gzip-levels 1 3 6 9 \
  --brotli-qualities 1 4 8 11

# Generate competitive matrix for all tiers
python benchmark_frackture.py \
  --all-tiers \
  --gzip-levels 1 6 9 \
  --brotli-qualities 4 6 11 \
  --include-huge
```

## Edge Cases

### Testing <100 Byte Payloads

```bash
# Explicit tiny payload testing
python benchmark_frackture.py --tiny-only

# Include tiny in comprehensive test
python benchmark_frackture.py --all-tiers

# Verify payload sizing for tiny inputs
python benchmark_frackture.py --tiny-only --verify-only --detailed
```

**What this tests:**
- Payload overhead impact on small data
- MSE optimization effectiveness
- Determinism with tiny inputs
- Fault injection detection

### Testing >100MB Payloads

```bash
# Enable extreme testing (>100MB)
python benchmark_frackture.py --extreme

# Full tier sweep including 1GB+ data
python benchmark_frackture.py --all-tiers --include-huge

# Verify memory efficiency and streaming
python benchmark_frackture.py --extreme --verify-only --detailed
```

**What this tests:**
- Memory usage patterns
- Streaming scalability
- Large payload compression ratios
- System resource management

### Stress Testing Combinations

```bash
# Maximum comprehensive test (will take hours)
python benchmark_frackture.py \
  --all-tiers \
  --include-huge \
  --categories text,binary,structured,code,mixed \
  --gzip-levels 1 6 9 \
  --brotli-qualities 4 6 11 \
  --detailed
```

## Analysis Pipeline

### Automatic Analysis

After running benchmarks, the analysis pipeline processes results:

```bash
# Auto-detect latest results and analyze
python analyze_results.py

# Specify results file explicitly
python analyze_results.py results/benchmark_results_20241213_143022.json

# Custom output directory
python analyze_results.py --output-dir custom_analysis
```

### Analysis Outputs

The pipeline generates two files:

1. **`analysis/report.md`**: Human-readable analysis with:
   - Performance comparisons
   - Key findings and insights
   - Trend analysis
   - Competitive positioning

2. **`analysis/insights.json`**: Machine-readable structured data with:
   - Detailed metrics
   - Statistical analysis
   - Weakness detection results
   - Latency comparisons

### Manual Analysis Integration

```bash
# Run benchmark and analysis in sequence
python benchmark_frackture.py --small-only
python analyze_results.py

# Or chain with shell script
./run_benchmark_and_analyze.sh --tiers small,medium
```

## Metric Requirements

### Core Performance Metrics

#### Compression Metrics
- **compression_ratio**: Original size / compressed size
- **encode_time**: Time to create fingerprint (seconds)
- **decode_time**: Time to reconstruct data (seconds)
- **encode_throughput**: MB/s processing speed (encode)
- **decode_throughput**: MB/s processing speed (decode)

#### Resource Metrics
- **peak_memory_mb**: Maximum memory usage
- **hash_time**: SHA256 hashing latency
- **success**: Boolean indicating successful operation
- **error**: Error message if operation failed

### Frackture-Specific Verification Metrics

#### Payload Sizing
- **symbolic_bytes**: Size of symbolic channel (should be 32)
- **entropy_bytes**: Size of entropy channel (should be 128)
- **serialized_total_bytes**: Total serialized payload (should be ~96)
- **payload_is_96b**: Boolean verification of expected size

#### Reconstruction Quality
- **baseline_mse**: Mean squared error before optimization
- **optimized_mse**: Mean squared error after optimization  
- **optimization_improvement_pct**: Percentage improvement (5-30% typical)
- **is_lossless**: Boolean (should be False - Frackture is lossy by design)

#### Reliability Testing
- **is_deterministic**: Boolean - same input produces same output
- **determinism_drifts**: Number of times deterministic behavior failed
- **fault_injection_passed**: Boolean - detected intentional mutations
- **fault_injection_errors**: List of faults that should have been detected

### Competitor Comparison Metrics

#### Gzip Metrics
- **gzip_level**: Compression level used (1-9)
- **gzip_compression_ratio**: Gzip-only compression ratio
- **gzip_throughput**: Gzip encode/decode speed

#### Brotli Metrics  
- **brotli_quality**: Quality parameter used (0-11)
- **brotli_compression_ratio**: Brotli-only compression ratio
- **brotli_throughput**: Brotli encode/decode speed

### Expected Metric Ranges

| Metric | Expected Range | Notes |
|--------|----------------|-------|
| compression_ratio | 1.0 - 50.0+ | Varies by data type and size |
| encode_throughput | 50 - 500 MB/s | Hardware dependent |
| decode_throughput | 1000 - 10000 MB/s | Decode is faster |
| optimization_improvement_pct | 5 - 30% | Typical MSE improvement |
| payload_is_96b | True | Fixed-size output requirement |
| is_deterministic | True | Should always pass |
| fault_injection_passed | True | Should detect all mutations |

## Artifact Management

### Result File Locations

```bash
# Default results directory
benchmarks/results/

# Custom output directory
--output-dir ./custom_results/
```

### Result File Naming

Results are automatically named with timestamp:
```
benchmark_results_YYYYMMDD_HHMMSS.json
```

Example: `benchmark_results_20241213_143022.json`

### Result File Structure

```json
{
  "benchmark_info": {
    "timestamp": "2024-12-13T14:30:22",
    "version": "frackture-benchmark-v2.0",
    "config": {...}
  },
  "results": [
    {
      "name": "text_plain_small",
      "dataset_type": "real",
      "original_size": 1024,
      "compressed_size": 96,
      "compression_ratio": 10.67,
      "symbolic_bytes": 32,
      "entropy_bytes": 128,
      "serialized_total_bytes": 96,
      "payload_is_96b": true,
      "baseline_mse": 0.234,
      "optimized_mse": 0.187,
      "optimization_improvement_pct": 20.1,
      "is_deterministic": true,
      "determinism_drifts": 0,
      "fault_injection_passed": true,
      "fault_injection_errors": [],
      "gzip_level": 6,
      "brotli_quality": 6,
      "success": true
    }
  ]
}
```

### Analysis Output Structure

```bash
# Markdown report
analysis/report.md

# JSON insights
analysis/insights.json

# Custom output directory
custom_analysis/
├── report.md
└── insights.json
```

### Backup and Archiving

```bash
# Archive results with timestamp
tar -czf benchmark_results_$(date +%Y%m%d_%H%M%S).tar.gz benchmarks/results/

# Organize by benchmark type
mkdir -p archive/{small,large,extreme,verification}
cp benchmarks/results/benchmark_results_*.json archive/small/
```

## Troubleshooting

### Common Issues

#### Dataset Repository Not Available
```
Warning: DatasetRepository not available, using legacy DatasetGenerator
```
**Solution**: 
```bash
cd benchmarks
pip install pyyaml
python dataset_cli.py test
```

#### Missing Dependencies
```
Warning: brotli not available. Install with: pip install brotli
Warning: cryptography not available. Install with: pip install cryptography
```
**Solution**:
```bash
pip install brotli cryptography psutil
```

#### Out of Memory on Extreme Tests
```
MemoryError or system becomes unresponsive
```
**Solutions**:
1. Use `--extreme-only` instead of `--all-tiers`
2. Close other applications
3. Add more RAM or use smaller tiers
4. Use synthetic datasets: `--synthetic`

#### Benchmark Takes Too Long
**Solutions**:
1. Start with `--small-only` for quick results
2. Use fewer compression levels: `--gzip-levels 6`
3. Use verification-only mode: `--verify-only`
4. Skip tiny datasets: `--no-tiny`

#### Results File Not Found for Analysis
```
FileNotFoundError: Results file not found
```
**Solutions**:
```bash
# List available results
ls benchmarks/results/

# Use specific file
python analyze_results.py benchmarks/results/benchmark_results_20241213_143022.json

# Verify file exists
python -c "import json; print(json.load(open('benchmarks/results/latest.json'))['benchmark_info']['timestamp'])"
```

### Performance Optimization

#### Faster Execution
```bash
# Use synthetic datasets for development
python benchmark_frackture.py --synthetic --small-only

# Single compression level comparisons
python benchmark_frackture.py --gzip-level 6 --brotli-quality 6

# Verification-only for testing
python benchmark_frackture.py --verify-only
```

#### Memory Efficiency
```bash
# Process smaller tiers only
python benchmark_frackture.py --small-only --medium-only

# Skip memory-intensive tests
python benchmark_frackture.py --no-tiny --large-only
```

### Validation Commands

#### Verify Installation
```bash
# Test core functionality
python -c "
import sys; sys.path.insert(0, '.')
import importlib.util
spec = importlib.util.spec_from_file_location('frackture', 'frackture (2).py')
frackture = importlib.util.module_from_spec(spec)
spec.loader.exec_module(frackture)
print('✅ Frackture module loads successfully')
"

# Test benchmark system
python benchmark_frackture.py --verify-only --tiny-only

# Test analysis pipeline
python analyze_results.py benchmarks/results/latest.json 2>/dev/null && echo "✅ Analysis pipeline working"
```

#### Dataset Validation
```bash
cd benchmarks
python dataset_cli.py test  # Should show all datasets found
python dataset_cli.py list  # Should list 15 datasets
```

### Getting Help

#### Built-in Help
```bash
python benchmark_frackture.py --help
python analyze_results.py --help
python dataset_cli.py --help
```

#### Logging and Debugging
```bash
# Enable verbose output
python benchmark_frackture.py --detailed --verify-only

# Check specific dataset loading
python -c "
from dataset_repository import DatasetRepository
repo = DatasetRepository()
try:
    data = repo.load_dataset('text_plain', 'tiny')
    print(f'✅ Loaded {len(data)} bytes')
except Exception as e:
    print(f'❌ Error: {e}')
"
```

## Quick Reference

### Common Command Sequences

#### Development Workflow
```bash
# 1. Quick validation
python benchmark_frackture.py --verify-only --small-only

# 2. Check results
python analyze_results.py

# 3. Review report
cat analysis/report.md
```

#### Comprehensive Benchmark
```bash
# Full tier analysis
python benchmark_frackture.py --all-tiers --detailed

# Analyze results
python analyze_results.py

# Archive results
tar -czf comprehensive_$(date +%Y%m%d).tar.gz benchmarks/results/ analysis/
```

#### Competitive Analysis
```bash
# Compare against gzip/brotli
python benchmark_frackture.py \
  --small-only \
  --gzip-levels 1 6 9 \
  --brotli-qualities 4 6 11

# Analyze competitive positioning
python analyze_results.py
```

### Success Criteria Checklist

For a successful benchmark run:

- [ ] All datasets load successfully (`python dataset_cli.py test`)
- [ ] Benchmark completes without errors
- [ ] All Frackture runs show `payload_is_96b: true`
- [ ] Determinism tests pass (`is_deterministic: true`)
- [ ] Fault injection tests pass (`fault_injection_passed: true`)
- [ ] Analysis completes successfully
- [ ] Report generated in `analysis/report.md`
- [ ] JSON insights saved to `analysis/insights.json`

This runbook provides complete coverage for executing Frackture's Phase 1 benchmark suite. Engineers can follow these instructions to reproduce comprehensive benchmark results without examining the underlying code.