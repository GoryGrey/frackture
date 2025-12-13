# Frackture Benchmark Suite

This directory contains a comprehensive benchmark suite for comparing Frackture's compression, encryption, and hashing performance against industry-standard compression algorithms (gzip and brotli) using **real-world datasets**.

---

## 📋 Overview

The benchmark suite tests Frackture against:
- **gzip**: Popular general-purpose compression (Python standard library)
- **brotli**: Modern compression algorithm with better ratios (optional, requires `pip install brotli`)

**New in v2.0**:
- 🎯 **15+ real datasets** across text, binary, code, structured, and mixed categories
- 📊 **7 size tiers** from 50 bytes to 1 GB (optional huge tier)
- 🔍 **Comprehensive verification metrics** (payload sizing, MSE, determinism, fault injection)
- 🛠️ **Advanced CLI options** for fine-grained control
- 📦 **Dataset repository system** with intelligent scaling

---

## 🎯 What is Measured

### Core Performance Metrics

For each compression method and dataset, the suite measures:

1. **Compression Ratio**: `original_size / compressed_size` (higher is better)
2. **Encode Time**: Time to compress data (lower is better)
3. **Decode Time**: Time to decompress data (lower is better)
4. **Encode Throughput**: MB/s during compression (higher is better)
5. **Decode Throughput**: MB/s during decompression (higher is better)
6. **Hash Latency**: Time to generate a hash (lower is better)
7. **Peak Memory**: Maximum memory usage in MB (lower is better)

### Frackture-Specific Verification Metrics

**Payload Sizing** (validates fixed-size output):
- `symbolic_bytes`: Size of symbolic fingerprint (target: 32 bytes)
- `entropy_bytes`: Size of entropy signature (target: 128 bytes)
- `serialized_total_bytes`: Total JSON serialized size (target: ~96 bytes)
- `payload_is_96b`: Boolean check that payload is within 90-102 bytes

**Reconstruction Quality (MSE)**:
- `baseline_mse`: Mean Squared Error between original and reconstructed
- `optimized_mse`: MSE after self-optimization (5 trials)
- `optimization_improvement_pct`: Percentage improvement from optimization
- `is_lossless`: Boolean (False for Frackture, True for gzip/brotli)

**Determinism**:
- `is_deterministic`: Boolean indicating if multiple encodes produce identical outputs
- `determinism_drifts`: Count of non-matching payloads (should be 0)

**Fault Injection/Corruption Tests**:
- `fault_injection_passed`: Boolean indicating all corruption tests detected
- `fault_injection_errors`: List of specific test failures (should be empty)

Tests performed:
1. Mutated symbolic fingerprint detection
2. Mutated entropy channel detection
3. Empty payload rejection
4. Invalid hex string rejection

---

## 📊 Real Dataset Repository

### 15+ Production-Ready Datasets

All samples are redistribution-safe and represent real-world content types:

| Dataset | Category | Base Size | Description | Compressibility |
|---------|----------|-----------|-------------|-----------------|
| **Text Datasets** ||||
| `text_plain` | text | 596 B | Natural language prose/documentation | High |
| `text_log` | text | 625 B | Structured application log entries | High |
| `text_json` | text | 814 B | JSON structured data | High |
| `text_csv` | text | 222 B | Comma-separated tabular data | High |
| **Binary Datasets** ||||
| `binary_png` | binary | 69 B | PNG image (1x1 red pixel) | Low |
| `binary_jpeg` | binary | 138 B | JPEG image (minimal valid) | Low |
| `binary_pdf` | binary | 457 B | PDF document (minimal valid) | Medium |
| `binary_gif` | binary | 43 B | GIF animation (1x1 transparent) | Low |
| **Structured Datasets** ||||
| `structured_sqlite` | structured | 12 KB | SQLite database with tables | Medium |
| `structured_pickle` | structured | 161 B | Python pickle serialized object | Medium |
| `structured_msgpack` | structured | 85 B | MessagePack serialized data | Medium |
| **Code Datasets** ||||
| `code_javascript` | code | 563 B | JavaScript source code | High |
| `code_javascript_minified` | code | 223 B | Minified JavaScript | Medium |
| `code_python` | code | 1206 B | Python source module | High |
| **Mixed Datasets** ||||
| `mixed_payload` | mixed | 1878 B | Multi-format bundle (text+JSON+binary+code) | Medium |

### Size Tiers

Datasets are scaled to 7 standard tiers for comprehensive testing:

| Tier | Target Size | Range | Use Case |
|------|-------------|-------|----------|
| **tiny** | 50 B | 1-99 B | Headers, metadata, minimal payloads |
| **small** | 1 KB | 100 B - 10 KB | Config files, API responses |
| **medium** | 100 KB | 10 KB - 500 KB | Documents, images, code files |
| **large** | 1 MB | 500 KB - 5 MB | Large documents, small datasets |
| **xlarge** | 10 MB | 5 MB - 50 MB | Media files, archives |
| **xxlarge** | 100 MB | 50 MB - 500 MB | Large datasets, videos |
| **huge** | 1 GB | 500 MB - 10 GB | Very large datasets (optional, skip with `--no-huge`) |

### Mixed Combinations

Predefined combinations for realistic workload testing:

- **text_heavy**: 70% text formats (plain, JSON, log) + 30% code/binary
- **binary_heavy**: 70% binary formats (PNG, JPEG, PDF) + 30% text/code
- **code_heavy**: Mix of JavaScript, Python, minified code + metadata
- **structured_heavy**: SQLite, JSON, CSV, pickle (database/serialization focused)
- **balanced**: Equal mix of all categories

---

## 🚀 Running the Benchmarks

### Basic Usage

```bash
cd benchmarks

# Run all benchmarks with real datasets (default)
python benchmark_frackture.py

# This tests:
# - All 15+ real datasets
# - medium tier (100 KB) and large tier (1 MB)
# - Frackture, gzip (level 6), and brotli (quality 6, if available)
```

### Size-Specific Benchmarks

```bash
# Only small datasets (100 KB)
python benchmark_frackture.py --small-only

# Only large datasets (1 MB)
python benchmark_frackture.py --large-only

# Only tiny datasets (<100 B) - tests edge cases
python benchmark_frackture.py --tiny-only

# Only extreme datasets (100 MB+) - WARNING: very slow
python benchmark_frackture.py --extreme-only

# Enable extreme datasets in addition to normal ones
python benchmark_frackture.py --extreme
```

### Dataset Mode Selection

```bash
# Use real datasets (default if available, recommended)
python benchmark_frackture.py --real

# Use synthetic datasets (legacy Lorem Ipsum generators)
python benchmark_frackture.py --synthetic
```

### Verification Mode

```bash
# Run only verification metrics (skip gzip/brotli, faster)
python benchmark_frackture.py --verify-only

# Enable detailed diagnostic output
python benchmark_frackture.py --detailed
```

### Compression Settings

```bash
# Adjust gzip compression level (1=fastest, 9=best compression)
python benchmark_frackture.py --gzip-level 9

# Adjust brotli quality (0=fastest, 11=best compression)
python benchmark_frackture.py --brotli-quality 11

# Test multiple compression levels
python benchmark_frackture.py --gzip-level 1  # Fast
python benchmark_frackture.py --gzip-level 6  # Default
python benchmark_frackture.py --gzip-level 9  # Maximum
```

### Custom Output Directory

```bash
# Save results to custom location
python benchmark_frackture.py --output-dir /path/to/results

# Organize by date
python benchmark_frackture.py --output-dir ./results/$(date +%Y%m%d)
```

### Combined Examples

```bash
# Large datasets, maximum compression, custom output
python benchmark_frackture.py --large-only --gzip-level 9 --brotli-quality 11 --output-dir ./analysis

# Fast verification for small datasets with details
python benchmark_frackture.py --small-only --verify-only --detailed

# Real datasets, extreme sizes (100 MB+), no tiny tests
python benchmark_frackture.py --extreme --no-tiny --real

# Production-like benchmark (medium + large, real data, balanced compression)
python benchmark_frackture.py --real --gzip-level 6 --brotli-quality 6 --output-dir ./prod_baseline
```

---

## 🔧 Requirements

### Core Dependencies

Installed automatically with Frackture:
```bash
pip install numpy scipy scikit-learn pyyaml
```

### Optional Dependencies

For complete benchmark functionality:
```bash
pip install brotli psutil
```

- **brotli**: Enables brotli compression benchmarks (highly recommended)
  - Without it: Only Frackture and gzip are tested
  - With it: Full comparison against state-of-the-art compression
  
- **psutil**: Provides accurate OS-level memory tracking
  - Without it: Uses `tracemalloc` (Python object memory only)
  - With it: Measures RSS (Resident Set Size) for true memory usage

- **pyyaml**: Required for dataset repository (core dependency as of v2.0)
  - Parses dataset manifest files
  - Manages scaling rules and metadata

---

## 📈 Understanding Results

### Console Output

Results are displayed in formatted tables:

```
========================================================================================================
Dataset: text_plain (medium - 100.00 KB)
========================================================================================================
| Method               | Original     | Compressed   | Ratio    | Encode (ms)  | Decode (ms)  | Encode Tput | Decode Tput | Hash (ms) | Memory (MB) |
|----------------------|--------------|--------------|----------|--------------|--------------|-------------|-------------|-----------|-------------|
| Frackture            | 100.00 KB    | 96 B         | 1066.67x | 2.45         | 0.82         | 40.82 MB/s  | 122.45 MB/s | 0.125     | 2.45        |
| Gzip (level 6)       | 100.00 KB    | 35.21 KB     | 2.84x    | 1.23         | 0.56         | 81.30 MB/s  | 178.57 MB/s | 0.125     | 1.89        |
| Brotli (quality 6)   | 100.00 KB    | 28.44 KB     | 3.52x    | 15.67        | 0.45         | 6.38 MB/s   | 222.22 MB/s | 0.125     | 3.12        |
========================================================================================================

FRACKTURE VERIFICATION METRICS:
  ✓ Payload Size: 96 bytes (symbolic: 32 B, entropy: 128 B serialized)
  ✓ Payload is ~96 bytes: True
  ✓ Baseline MSE: 0.000234
  ✓ Optimized MSE: 0.000198 (improvement: 15.38%)
  ✓ Deterministic: Yes (0 drifts in 3 runs)
  ✓ Fault Injection: Passed (4/4 corruption tests detected)
  ✓ Lossless: No (by design)
```

### JSON Output

Structured data saved to `results/benchmark_results_YYYYMMDD_HHMMSS.json`:

```json
{
  "timestamp": "2024-01-01T12:00:00",
  "system_info": {
    "python_version": "3.11.0",
    "numpy_version": "1.24.0",
    "has_brotli": true,
    "has_psutil": true
  },
  "results": {
    "text_plain_medium": [
      {
        "name": "Frackture",
        "dataset_type": "text",
        "original_size": 102400,
        "compressed_size": 96,
        "compression_ratio": 1066.67,
        "encode_time": 0.00245,
        "decode_time": 0.00082,
        "encode_throughput": 40.82,
        "decode_throughput": 122.45,
        "hash_time": 0.000125,
        "peak_memory_mb": 2.45,
        "success": true,
        "symbolic_bytes": 32,
        "entropy_bytes": 128,
        "serialized_total_bytes": 96,
        "payload_is_96b": true,
        "baseline_mse": 0.000234,
        "optimized_mse": 0.000198,
        "optimization_improvement_pct": 15.38,
        "is_lossless": false,
        "is_deterministic": true,
        "determinism_drifts": 0,
        "fault_injection_passed": true,
        "fault_injection_errors": []
      }
    ]
  }
}
```

### Markdown Output

Human-readable summary saved to `results/benchmark_results_YYYYMMDD_HHMMSS.md` with:
- Formatted tables for each dataset
- Key observations and metrics explanations
- Frackture's unique advantages
- Recommendations based on results

---

## 🔍 Interpreting Results

### Frackture's Unique Position

Frackture is **not a traditional compression algorithm**. Key differences:

1. **Fixed-Size Output**: Always produces ~96 bytes, regardless of input size
   - ✅ Excels at creating compact fingerprints/signatures
   - ✅ Compression ratio scales with input size (1 MB → ~10,000×, 100 MB → ~1,000,000×)
   - ❌ May expand very small inputs (<100 bytes)

2. **Dual-Channel Encoding**:
   - **Symbolic channel** (32 bytes): Identity-preserving fingerprint
   - **Entropy channel** (16 floats): Frequency/pattern signature

3. **Lossy Compression**:
   - ✅ Reconstruction is approximate (measured by MSE)
   - ✅ Self-optimization minimizes MSE (5-30% improvement typical)
   - ❌ Not suitable for exact reconstruction requirements

### Expected Performance Characteristics

**Frackture Advantages:**
- 🚀 Extremely high compression ratios for large inputs (10,000×+ for 1 MB+)
- ⚡ Fast decode throughput (3000-5000 MB/s for 1 MB files)
- 🎯 Consistent memory usage (~2-10 MB regardless of input size)
- 🔒 Identity preservation across similar inputs (deterministic)
- 📊 Built-in entropy awareness (frequency pattern detection)

**Frackture Trade-offs:**
- ⚠️ Lossy compression (MSE 0.0001-0.01 typical)
- ⚠️ May expand very small inputs (<100 bytes to 96 bytes)
- ⚠️ Slower encode for tiny files (overhead dominates)
- ⚠️ Different paradigm than traditional lossless compression

**Traditional Compression (gzip/brotli) Advantages:**
- ✅ Lossless compression (perfect reconstruction)
- ✅ Better for general file compression
- ✅ Variable compression ratios (adapts to compressibility)
- ✅ Faster encode for small files
- ✅ Better for incompressible data (doesn't expand as much)

---

## 📊 Metric Definitions

### Compression Ratio

**Formula**: `original_size / compressed_size`

**Interpretation**:
- **> 1.0**: Compression achieved (output smaller than input)
- **= 1.0**: No compression (output same size as input)
- **< 1.0**: Expansion (output larger than input)

**Frackture-specific**:
- tiny (50 B): ~0.5× (expansion expected)
- small (1 KB): ~10×
- medium (100 KB): ~1000×
- large (1 MB): ~10,000×
- xlarge (10 MB): ~100,000×

### Throughput (MB/s)

**Formula**: `(original_size / 1024^2) / time_in_seconds`

**Interpretation**:
- **Encode throughput**: How fast data is compressed
- **Decode throughput**: How fast data is decompressed

**Typical ranges**:
- Frackture encode: 100-200 MB/s (large files)
- Frackture decode: 3000-5000 MB/s (large files)
- gzip: 20-90 MB/s encode, 200-700 MB/s decode
- brotli: 5-30 MB/s encode, 200-500 MB/s decode

### MSE (Mean Squared Error)

**Formula**: `mean((original_vector - reconstructed_vector)^2)`

**Only applies to Frackture** (lossy compression):

**Interpretation**:
- **< 0.001**: Excellent reconstruction (near-lossless)
- **0.001 - 0.01**: Good reconstruction (minor loss)
- **0.01 - 0.1**: Fair reconstruction (noticeable loss)
- **> 0.1**: Poor reconstruction (significant loss)

**Factors affecting MSE**:
- Data compressibility (text/code → low MSE, random noise → high MSE)
- Optimization (5-30% improvement typical)
- Input size (larger inputs may have higher MSE)

### Determinism

**Definition**: Same input produces same output across multiple encodes.

**Critical for**:
- Deduplication (same file → same fingerprint)
- Caching (consistent cache keys)
- Integrity checking (reproducible hashes)

**Expected**: 100% deterministic (0 drifts)

**If non-deterministic**: File a bug report (should never happen)

### Fault Injection

**Tests performed**:
1. Mutated symbolic fingerprint → Should be detected
2. Mutated entropy channel → Should be detected
3. Empty payload → Should raise ValueError
4. Invalid hex string → Should raise ValueError

**Expected**: All 4 tests pass

**If failures**: Check for:
- Version mismatch (update Frackture)
- Data corruption (filesystem issue)
- Bug in error handling (file a report)

---

## 🎛️ Running >100 MB Scenarios

### Extreme Dataset Testing

For datasets larger than 100 MB, special considerations apply:

```bash
# Enable extreme benchmarks (WARNING: can take 30+ minutes)
python benchmark_frackture.py --extreme

# Only extreme datasets (skip small/medium/large)
python benchmark_frackture.py --extreme-only

# Extreme with custom output
python benchmark_frackture.py --extreme --output-dir ./extreme_results
```

### Size Tiers for Large Files

| Tier | Size | Frackture Time (est.) | gzip Time (est.) | Memory |
|------|------|----------------------|------------------|--------|
| **xlarge** | 10 MB | ~0.5s encode, ~0.02s decode | ~2-5s encode, ~0.5s decode | ~10 MB |
| **xxlarge** | 100 MB | ~5s encode, ~0.2s decode | ~20-50s encode, ~5s decode | ~10 MB |
| **huge** | 1 GB | ~50s encode, ~2s decode | ~200-500s encode, ~50s decode | ~10-20 MB |

### Streaming for Very Large Files

For files >1 GB, use the dataset repository's streaming API:

```python
from dataset_repository import DatasetRepository

repo = DatasetRepository()

# Stream in 1 MB chunks
for chunk in repo.stream_chunks('text_plain', 1_000_000_000, chunk_size=1024*1024):
    # Process chunk
    payload = frackture_v3_3_safe(frackture_preprocess_universal_v2_6(chunk))
```

### Performance Expectations

**Frackture at scale**:
- ✅ Memory usage does NOT scale with input size (~10 MB constant)
- ✅ Throughput remains stable (150-200 MB/s encode, 3000-5000 MB/s decode)
- ✅ Compression ratio grows linearly (1 GB → ~10,000,000×)

**gzip/brotli at scale**:
- ⚠️ Memory scales with compression window (up to hundreds of MB)
- ⚠️ Throughput may degrade for very large files
- ⚠️ Compression ratio plateaus (~2-10× regardless of input size)

---

## 🧪 Dataset CLI Tool

Explore and test datasets before benchmarking:

```bash
cd benchmarks

# List all available datasets
python dataset_cli.py list

# Show datasets grouped by category
python dataset_cli.py categories

# Get detailed information about a dataset
python dataset_cli.py info text_plain
# Output:
#   Name: text_plain
#   Category: text
#   File: sample_text.txt
#   Size: 596 bytes
#   Description: Natural language prose/documentation
#   Compressibility: high
#   Scaling: 50 - 100,000,000 bytes

# Load and save a scaled dataset
python dataset_cli.py load text_plain --tier medium --save output.bin
# Creates a 100 KB file scaled from the 596 B base file

# Test all datasets for integrity
python dataset_cli.py test
# Validates:
# - All non-optional files exist
# - Canonical sizes match actual sizes
# - All datasets can be loaded and scaled
# - Mixed combinations reference valid datasets

# Load a mixed combination
python dataset_cli.py mixed --combination text_heavy --size 100000
# Creates a 100 KB file with 70% text, 30% other content

# Load custom mix
python dataset_cli.py mixed --datasets text_plain,code_python,binary_png --weights 50,30,20 --size 50000
# Creates a 50 KB file with 50% text, 30% code, 20% binary
```

---

## 📁 Output Files

All results are saved to `benchmarks/results/` with timestamps:

```
benchmarks/results/
├── benchmark_results_20240101_120000.json  # Structured data (for automation/analysis)
├── benchmark_results_20240101_120000.md    # Human-readable report (for sharing)
└── benchmark_results_20240101_120000.txt   # Console output log (for debugging)
```

### JSON Output Structure

- `timestamp`: ISO 8601 timestamp
- `system_info`: Python/package versions, available dependencies
- `results`: Dictionary keyed by dataset name
  - Each dataset has list of benchmark results (Frackture, gzip, brotli)
  - Full metrics including verification data

### Markdown Output Structure

- System information header
- Summary table (all datasets, all methods)
- Detailed tables per dataset
- Key observations section
- Recommendations section

---

## 🐛 Troubleshooting

### "brotli not available"

```bash
pip install brotli
```

Without brotli: Benchmarks run but skip brotli comparisons.

### "psutil not available"

```bash
pip install psutil
```

Without psutil: Memory tracking uses `tracemalloc` (less accurate but functional).

### "yaml not available"

```bash
pip install pyyaml
```

Required for dataset repository. Install to use real datasets.

### "DatasetRepository not available"

Make sure you're running from the `benchmarks/` directory:
```bash
cd benchmarks
python benchmark_frackture.py
```

Or use absolute imports if running from elsewhere.

### Benchmarks running too slow

- Use `--small-only` to skip large datasets (~10× faster)
- Use `--no-tiny` to skip tiny dataset edge cases
- Avoid `--extreme` unless needed (100 MB+ tests can take 30+ minutes)
- Use `--verify-only` to skip gzip/brotli (~50% faster)

### Unexpected MSE values

- **Random noise**: High MSE (0.01-0.1) is expected (incompressible data)
- **Text/code**: Low MSE (0.0001-0.001) is expected (compressible, structured)
- **Binary files**: Medium MSE (0.001-0.01) is expected (pre-compressed)

Use `--detailed` to see optimization impact (5-30% reduction typical).

### Non-deterministic results (drifts > 0)

**Should never happen**. If you see this:
1. Verify NumPy version: `pip install --upgrade numpy`
2. Check for filesystem corruption: `fsck` or equivalent
3. File a bug report with full output: `python benchmark_frackture.py --detailed`

### Memory tracking seems inaccurate

- Install `psutil` for OS-level tracking (more accurate)
- Without `psutil`, `tracemalloc` only tracks Python objects (not C extensions)
- For accurate memory profiling, use `--verify-only` with `psutil` installed

---

## 🎨 Customizing Benchmarks

### Adding New Real Datasets

1. Create sample file in `benchmarks/datasets/`
2. Add entry to `benchmarks/datasets/manifest.yaml`:
   ```yaml
   my_dataset:
     category: text
     subcategory: custom
     file: my_sample.txt
     canonical_size: 1234
     description: "My custom dataset"
     compressibility: high
     scaling:
       method: repeat
       min_size: 50
       max_size: 100_000_000
   ```
3. Run tests: `cd .. && python -m pytest tests/test_dataset_repository.py -v`
4. Benchmark: `cd benchmarks && python benchmark_frackture.py --real`

### Adding New Mixed Combinations

Edit `benchmarks/datasets/manifest.yaml`:

```yaml
mixed_combinations:
  my_custom_mix:
    description: "My custom combination"
    components:
      - dataset: text_plain
        weight: 50
      - dataset: binary_png
        weight: 30
      - dataset: code_python
        weight: 20
```

Then use: `python dataset_cli.py mixed --combination my_custom_mix --size 100000`

### Adjusting Compression Levels

Test multiple compression settings to find the sweet spot:

```bash
# Fast compression
python benchmark_frackture.py --gzip-level 1 --brotli-quality 0

# Balanced (default)
python benchmark_frackture.py --gzip-level 6 --brotli-quality 6

# Maximum compression
python benchmark_frackture.py --gzip-level 9 --brotli-quality 11
```

---

## 📖 Further Reading

- **[docs/BENCHMARKING.md](../docs/BENCHMARKING.md)**: Complete methodology and interpretation guide
- **[datasets/README.md](./datasets/README.md)**: Detailed dataset documentation
- **[BENCHMARK_SUITE_SUMMARY.md](../BENCHMARK_SUITE_SUMMARY.md)**: Implementation summary and findings
- **[docs/ARCHITECTURE.md](../docs/ARCHITECTURE.md)**: Technical deep dive into Frackture's design
- **[docs/FAQ.md](../docs/FAQ.md)**: Common questions and troubleshooting

---

## 🤝 Contributing

To add new benchmark scenarios:
1. Add dataset generators to `DatasetGenerator` (for synthetic) or create real files
2. Add benchmark methods to `BenchmarkRunner` (if testing new algorithms)
3. Update result formatters if adding new metrics
4. Update this README and `docs/BENCHMARKING.md` with guidance
5. Add tests to `tests/test_dataset_repository.py`

---

## 📝 License

Same as Frackture - MIT License with attribution requirement.

**Required citation**:
*"Frackture: Recursive Compression & Symbolic Encoding, by Gregory Betti (f(∞))"*
