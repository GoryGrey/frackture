# Frackture Benchmarking Guide

**Complete methodology, metrics, and interpretation guide for Frackture's performance characteristics**

---

## Table of Contents

1. [Overview](#overview)
2. [Methodology](#methodology)
3. [Dataset Repository](#dataset-repository)
4. [Metrics Explained](#metrics-explained)
5. [Running Benchmarks](#running-benchmarks)
6. [Interpreting Results](#interpreting-results)
7. [What Frackture Optimizes For](#what-frackture-optimizes-for)
8. [Comparison Targets](#comparison-targets)
9. [Performance Characteristics](#performance-characteristics)
10. [Advanced Scenarios](#advanced-scenarios)

---

## Overview

Frackture's benchmark suite provides comprehensive performance evaluation across:

- **15+ real-world datasets** covering text, binary, code, structured data, and mixed payloads
- **7 size tiers** from 50 bytes to 1 GB (optional)
- **Multiple compression algorithms** (Frackture, gzip, brotli)
- **Comprehensive metrics** including verification, determinism, and fault injection tests
- **Automated validation** of payload structure and reconstruction quality

The goal is to answer key positioning questions:
- What is Frackture optimized for?
- When should you use Frackture vs traditional compression?
- What performance can you expect for different data types?
- How does Frackture's fixed-size output affect compression ratios?

---

## Methodology

### Benchmark Architecture

The benchmark harness (`benchmarks/benchmark_frackture.py`) follows a rigorous methodology:

```
For each dataset and size tier:
  1. Load/scale dataset to target size
  2. Run compression (Frackture, gzip, brotli)
  3. Measure encode/decode time and memory
  4. Verify correctness (lossless for gzip/brotli, MSE for Frackture)
  5. Run determinism checks (multiple encodes of same data)
  6. Run fault injection tests (corrupted payloads)
  7. Calculate all metrics and generate reports
```

### Memory Tracking

- **Primary**: `psutil` for OS-level RSS (Resident Set Size) tracking
- **Fallback**: `tracemalloc` for Python object memory tracking
- **Measurement**: Peak memory during encode/decode operations

### Timing

- Uses `time.perf_counter()` for high-resolution timing
- Separate measurements for:
  - Encode time (preprocessing + compression)
  - Decode time (decompression + reconstruction)
  - Hash time (deterministic hash generation)

### Validation

Each benchmark result includes:
- **Correctness**: Lossless algorithms verified bit-for-bit, Frackture verified via MSE
- **Determinism**: Same input produces same output across multiple runs
- **Fault tolerance**: Structural corruption and authenticated-envelope tampering are exercised (raw payloads do not include an internal checksum)
- **Payload structure**: Frackture compact payloads are verified to be **65 bytes** (`FrackturePayload.to_bytes()`)

---

## Dataset Repository

### Real Datasets vs Synthetic

The benchmark suite uses **real, redistribution-safe datasets** instead of synthetic Lorem Ipsum generators:

| Dataset | Category | Size | Description | Compressibility |
|---------|----------|------|-------------|-----------------|
| `text_plain` | text | 596 B | Natural language prose | High |
| `text_log` | text | 625 B | Structured log entries | High |
| `text_json` | text | 814 B | JSON structured data | High |
| `text_csv` | text | 222 B | CSV tabular data | High |
| `binary_png` | binary | 69 B | PNG image (1x1 pixel) | Low |
| `binary_jpeg` | binary | 138 B | JPEG image | Low |
| `binary_pdf` | binary | 457 B | PDF document | Medium |
| `binary_gif` | binary | 43 B | GIF animation | Low |
| `structured_sqlite` | structured | 12 KB | SQLite database | Medium |
| `structured_pickle` | structured | 161 B | Python pickle | Medium |
| `structured_msgpack` | structured | 85 B | MessagePack data | Medium |
| `code_javascript` | code | 563 B | JavaScript source | High |
| `code_javascript_minified` | code | 223 B | Minified JS | Medium |
| `code_python` | code | 1206 B | Python source | High |
| `mixed_payload` | mixed | 1878 B | Multi-format bundle | Medium |

### Size Tiers

Datasets are scaled to 7 standard tiers:

| Tier | Target | Range | Use Case |
|------|--------|-------|----------|
| **tiny** | 50 B | 1-99 B | Headers, metadata, minimal payloads |
| **small** | 1 KB | 100 B - 10 KB | Config files, API responses |
| **medium** | 100 KB | 10 KB - 500 KB | Documents, images, code files |
| **large** | 1 MB | 500 KB - 5 MB | Large documents, small datasets |
| **xlarge** | 10 MB | 5 MB - 50 MB | Media files, archives |
| **xxlarge** | 100 MB | 50 MB - 500 MB | Large datasets, videos |
| **huge** | 1 GB | 500 MB - 10 GB | Very large datasets (optional) |

### Scaling Method

All datasets use **repeat scaling**:
- For sizes < base file: truncate
- For sizes > base file: concatenate + truncate to exact target

This preserves the statistical properties of the original data while hitting exact target sizes.

### Mixed Combinations

Predefined combinations for realistic workloads:

- **text_heavy** (70% text): Natural language + code + minimal binary
- **binary_heavy** (70% binary): Images + PDF + some text/code
- **code_heavy**: Source code + metadata + logs
- **structured_heavy**: Database + JSON + CSV + pickle
- **balanced**: Equal mix of all categories

---

## Metrics Explained

### Core Performance Metrics

| Metric | Definition | Unit | Better |
|--------|------------|------|--------|
| **Compression Ratio** | `original_size / compressed_size` | Ratio | Higher |
| **Encode Time** | Time to compress | Seconds | Lower |
| **Decode Time** | Time to decompress | Seconds | Lower |
| **Encode Throughput** | `MB/s = (original_size / 1024^2) / encode_time` | MB/s | Higher |
| **Decode Throughput** | `MB/s = (original_size / 1024^2) / decode_time` | MB/s | Higher |
| **Hash Time** | Time to generate deterministic hash | Seconds | Lower |
| **Peak Memory** | Maximum RSS during operation | MB | Lower |

### Frackture-Specific Metrics

#### Payload Sizing

Validates that Frackture produces consistent, fixed-size outputs:

- **symbolic_bytes**: 32 bytes (raw)
- **entropy_bytes**: 32 bytes (16 × uint16 quantized)
- **serialized_total_bytes**: 65 bytes (`FrackturePayload.to_bytes()`)
- **payload_is_96b**: Historical flag retained by the benchmark schema (compact payloads are 65B in current versions)

**Why it matters**: Frackture’s core value proposition is fixed-size output (as a sketch), not bitwise reconstruction.

#### Reconstruction Quality (MSE)

Measures lossy compression quality:

- **baseline_mse**: Mean Squared Error between original and reconstructed vectors
- **optimized_mse**: MSE after self-optimization (5 trials)
- **optimization_improvement_pct**: `((baseline_mse - optimized_mse) / baseline_mse) × 100`

**Interpretation**:
- MSE < 0.001: Excellent reconstruction (near-lossless)
- MSE 0.001-0.01: Good reconstruction (minor loss)
- MSE 0.01-0.1: Fair reconstruction (noticeable loss)
- MSE > 0.1: Poor reconstruction (significant loss)

**Why it matters**: Unlike lossless compression, Frackture trades exact reconstruction for fixed-size output. MSE quantifies this trade-off.

#### Determinism

Validates that Frackture produces consistent outputs:

- **is_deterministic**: Boolean indicating if multiple encodes produce identical payloads
- **determinism_drifts**: Count of payloads that differed from the first

**Why it matters**: Deterministic encoding is critical for:
- Deduplication (same content = same fingerprint)
- Caching (consistent keys)
- Integrity checking (reproducible hashes)

#### Fault Injection

Tests robustness against corrupted inputs:

- **fault_injection_passed**: Boolean indicating if all corruption tests passed
- **fault_injection_errors**: List of specific failures

**Tests performed**:
1. Mutated symbolic fingerprint → Should fail or produce degraded output
2. Mutated entropy channel → Should fail or produce degraded output
3. Empty payload → Should raise ValueError
4. Invalid hex string → Should raise ValueError

**Why it matters**: Production systems must gracefully handle corrupted data. This validates error handling.

### Lossless Comparison Metrics

For gzip/brotli benchmarks:

- **is_lossless**: Boolean (always True for gzip/brotli)
- Verification: `assert decompressed == original`

---

## Running Benchmarks

### Basic Usage

```bash
cd benchmarks

# Run with real datasets (default)
python benchmark_frackture.py

# This tests:
# - medium tier (100 KB) for all datasets
# - large tier (1 MB) for all datasets
# - Frackture, gzip, and brotli (if available)
```

### Size-Specific Benchmarks

```bash
# Only small datasets (100 KB)
python benchmark_frackture.py --small-only

# Only large datasets (1 MB)
python benchmark_frackture.py --large-only

# Only tiny datasets (<100 B)
python benchmark_frackture.py --tiny-only

# Enable extreme datasets (100 MB+, very slow)
python benchmark_frackture.py --extreme

# Only extreme datasets
python benchmark_frackture.py --extreme-only
```

### Dataset Mode Selection

```bash
# Use real datasets (default if available)
python benchmark_frackture.py --real

# Use synthetic datasets (legacy mode)
python benchmark_frackture.py --synthetic
```

### Verification Mode

```bash
# Run only verification metrics (faster, no gzip/brotli)
python benchmark_frackture.py --verify-only

# Enable detailed diagnostic output
python benchmark_frackture.py --detailed
```

### Competitor Coverage (gzip/brotli sweeps)

The benchmark suite supports **single-config runs** and **multi-config sweeps** for fair competitor coverage.

**Default sweep (when you do not pass `--gzip-levels` / `--brotli-qualities`):**
- gzip levels: **1, 6, 9**
- brotli qualities: **4, 6, 11** (if `brotli` is installed)

```bash
# Force a single gzip configuration
python benchmark_frackture.py --gzip-level 9

# Force a single brotli configuration
python benchmark_frackture.py --brotli-quality 11

# Explicit sweeps (override defaults)
python benchmark_frackture.py --gzip-levels 1 6 9
python benchmark_frackture.py --brotli-qualities 4 6 11

# Full competition report: all tiers + comprehensive sweeps
python benchmark_frackture.py --competition-report
```

**Outputs:** the JSON and Markdown reports include `competition_summary` (overall + per tier win rates) and per-dataset comparison records.

### Custom Output

```bash
# Save results to custom directory
python benchmark_frackture.py --output-dir /path/to/results
```

### Combined Options

```bash
# Large datasets, max compression, custom output
python benchmark_frackture.py --large-only --gzip-level 9 --brotli-quality 11 --output-dir ./analysis

# Verification only for small datasets with details
python benchmark_frackture.py --small-only --verify-only --detailed
```

### Dataset CLI

Explore datasets before benchmarking:

```bash
cd benchmarks

# List all available datasets
python dataset_cli.py list

# Show datasets by category
python dataset_cli.py categories

# Get detailed info about a dataset
python dataset_cli.py info text_plain

# Load and save a scaled dataset
python dataset_cli.py load text_plain --tier medium --save output.bin

# Test all datasets for integrity
python dataset_cli.py test

# Load a mixed combination
python dataset_cli.py mixed --combination balanced --size 100000
```

---

## Interpreting Results

### Console Output

Results are printed as formatted tables:

```
========================================================================================================
Dataset: text_plain (medium - 100.00 KB)
========================================================================================================
| Method               | Original     | Compressed   | Ratio     | Encode (ms)  | Decode (ms)  | ...
|----------------------|--------------|--------------|-----------|--------------|--------------|-----
| Frackture (compact)  | 100.00 KB    | 65 B         | 1575.38x  | 6.06         | 0.29         | ...
| Gzip (L6)            | 100.00 KB    | ~0.8 KB      | ~146x     | ~0.47        | ~0.09        | ...
| Brotli (Q6)          | 100.00 KB    | ~0.3 KB      | ~579x     | ~0.33        | ~0.11        | ...
========================================================================================================

FRACKTURE VERIFICATION METRICS:
  Payload Size: 65 bytes (symbolic: 32 B, entropy: 32 B quantized)
  Baseline MSE: (data dependent)
  Optimized MSE: (data dependent; typical 5–30% improvement)
  Deterministic: Yes (0 drifts in 3 runs)
  Fault Injection: The raw payload has no checksum; authenticated envelopes detect tampering
```

### What to Look For

#### 1. Compression Ratio

**Frackture**:
- Scales with input size because the compact payload is fixed at **65 bytes**
- tiny (~50 B): <1× (expansion)
- small (~1 KB): ~16×
- medium (~100 KB): ~1575×
- large (~1 MB): ~16132×
- xlarge (~10 MB): ~161k×

**gzip/brotli**:
- Depends on compressibility
- Highly compressible (text, logs): 2-10x
- Moderately compressible (JSON, code): 2-5x
- Incompressible (random, encrypted): ~1x or worse

**Interpretation**: Frackture's ratio advantage grows with input size due to fixed output.

#### 2. Throughput

**Frackture Encode** (real datasets, averages):
- 100 KB tier: ~15 MB/s
- 1 MB tier: ~154 MB/s

**Frackture Decode** (real datasets, averages):
- 100 KB tier: ~377 MB/s
- 1 MB tier: ~3944 MB/s

**gzip/brotli** (real datasets, averages; representative configs):
- gzip L6 encode: ~235 MB/s (100 KB), ~263 MB/s (1 MB)
- brotli Q6 encode: ~447 MB/s (100 KB), ~785 MB/s (1 MB)

**Interpretation**:
- Frackture is often **slower to encode** than gzip/brotli.
- Frackture can be **very fast to decode** for larger payloads.

#### 3. MSE (Frackture Only)

- **Good performance**: MSE < 0.01
- **Optimization helps**: 5-30% MSE reduction typical
- **Data-dependent**: Text and structured data reconstruct better than random noise

**When to care**: If you're using Frackture for approximate reconstruction (ML embeddings, similarity detection), lower MSE is better.

**When to ignore**: If you only care about fingerprinting/hashing, MSE is irrelevant.

#### 4. Determinism

Should always be **Yes** for Frackture. If you see drifts:
- Check for non-deterministic input preprocessing
- File a bug report (this shouldn't happen)

#### 5. Memory Usage

**Frackture**:
- Consistent across input sizes (~2-10 MB peak)
- Dominated by 768-element float arrays

**gzip/brotli**:
- Scales with input size
- Higher for larger compression windows

---

## What Frackture Optimizes For

Frackture optimizes for **deterministic, fixed-size sketching** that can be reconstructed into a stable vector space.

### Deterministic fixed-size sketching (indexable “content ID”, not cryptographic)

**Use case**: Stable keys for indexing, bucketing, caching, and dedup candidate generation.

**Why it can be useful**:
- **Fixed 65-byte compact payload** (constant index width)
- Deterministic (same input → same payload)

**Evidence** (real datasets):
- 100 KB tier: 65 B output ⇒ ~1575× “ratio” by definition
- 1 MB tier: 65 B output ⇒ ~16132× “ratio” by definition

### Similarity / near-duplicate workflows (non-semantic)

**Use case**: Near-duplicate clustering where “shape of bytes” matters (format similarity, repeated structures, partially edited content).

**Evidence**:
- Optimization typically improves MSE by ~5–30% (dataset dependent)
- Reconstructed vectors support cosine/L2 similarity comparisons

### Deterministic vector sketches as an alternative to storing float embeddings

**Use case**: You already have 768-D vectors (or can accept a byte-derived 768-D representation) and want a tiny representation.

**Size math**:
- 768 × float32 = 3072 bytes
- Frackture compact payload = 65 bytes
- Reduction = ~47× (lossy)

### Integrity and authentication

- For **cryptographic content addressing**, use **SHA-256** (or BLAKE3). Frackture’s symbolic component is not a cryptographic hash.
- For **tamper detection of stored payloads**, use the authenticated envelope (`frackture_encrypt_payload` / `frackture_decrypt_payload`).

---

## Comparison Targets

### When to Use Frackture vs Traditional Compression

| Scenario | Use Frackture | Use gzip/brotli |
|----------|---------------|-----------------|
| **Fixed-size output required** | ✅ Yes | ❌ No (variable size) |
| **Lossless compression required** | ❌ No (lossy) | ✅ Yes |
| **Large file compression (>1 MB)** | ✅ Yes (if fingerprint OK) | ✅ Yes (if lossless needed) |
| **Small file compression (<1 KB)** | ❌ No (expands) | ✅ Yes |
| **Read-heavy workload** | ✅ Yes (fast decode) | ⚠️ Maybe (slower decode) |
| **Write-heavy workload** | ⚠️ Maybe | ✅ Yes (faster encode) |
| **Deduplication/fingerprinting** | ✅ Yes | ❌ No (not designed for it) |
| **Network transmission** | ❌ No (lossy) | ✅ Yes (lossless) |
| **Long-term archival** | ❌ No (lossy) | ✅ Yes (lossless) |
| **ML embedding compression** | ✅ Yes | ❌ No (not designed for it) |

### Compression Ratio Comparison

Frackture’s compact payload is fixed at **65 bytes**, so its “compression ratio” is approximately `input_size / 65` (linear in input size).

| Input Size | Frackture (compact) | gzip (text) | brotli (text) | gzip (random) | Winner |
|------------|---------------------|-------------|---------------|---------------|--------|
| 50 B | ~0.77× (expansion) | ~1.5× | ~1.8× | ~1.0× | gzip/brotli |
| 1 KB | ~16× | 3-5× | 4-6× | ~1.0× | Frackture (if lossy OK) |
| 100 KB | ~1575× | 3-5× | 4-7× | ~1.0× | Frackture |
| 1 MB | ~16132× | 3-6× | 4-8× | ~1.0× | Frackture |
| 100 MB | ~1,610,615× | 3-6× | 4-8× | ~1.0× | Frackture |

**Key insight**: Frackture’s ratio advantage grows linearly with input size because the output size is fixed.

---

## Performance Characteristics

### By Dataset Category

Based on benchmark results:

#### Text Datasets (plain, log, JSON, CSV)

- **Compressibility**: High (repetitive patterns, ASCII)
- **Frackture MSE**: Low (0.0001-0.001)
- **gzip ratio**: 3-6×
- **brotli ratio**: 4-8×
- **Recommendation**: Use Frackture for fingerprinting, gzip/brotli for lossless archival

#### Binary Datasets (PNG, JPEG, PDF, GIF)

- **Compressibility**: Low (already compressed)
- **Frackture MSE**: Medium (0.001-0.01)
- **gzip ratio**: 0.98-1.1× (often expands!)
- **brotli ratio**: 0.98-1.05× (minimal gain)
- **Recommendation**: Use Frackture (much better ratio), skip traditional compression

#### Code Datasets (JavaScript, Python)

- **Compressibility**: High (structured, repetitive)
- **Frackture MSE**: Low (0.0002-0.002)
- **gzip ratio**: 2-5×
- **brotli ratio**: 3-7×
- **Recommendation**: Use gzip/brotli for lossless, Frackture for fingerprinting

#### Structured Datasets (SQLite, pickle, msgpack)

- **Compressibility**: Medium (binary structured data)
- **Frackture MSE**: Medium (0.002-0.01)
- **gzip ratio**: 2-4×
- **brotli ratio**: 2-5×
- **Recommendation**: Use Frackture for identity preservation, gzip/brotli for archival

#### Mixed Datasets

- **Compressibility**: Varies by composition
- **Frackture MSE**: 0.002-0.01 (weighted average)
- **gzip ratio**: 2-4× (moderate compression)
- **brotli ratio**: 2.5-5× (better than gzip)
- **Recommendation**: Test both, use Frackture if fixed-size needed

### By Size Tier

#### Tiny (<100 B)

- **Frackture**: Expands to **65 bytes** (often not appropriate for tiny inputs)
- **gzip/brotli**: Typically small gains; sometimes expansion depending on headers
- **Recommendation**: Skip Frackture for tiny payloads unless you explicitly want a fixed-size sketch

#### Small (1 KB)

- **Frackture (compact)**: ~16× (1024 / 65)
- **gzip**: 2-4× (data-dependent)
- **brotli**: 3-5× (data-dependent)
- **Recommendation**: Use Frackture when fixed-size sketches are useful; use gzip/brotli when you need lossless output

#### Medium (100 KB)

- **Frackture (compact)**: ~1575×
- **Encode speed (avg)**: ~15 MB/s (real datasets)
- **Decode speed (avg)**: ~377 MB/s (real datasets)

#### Large (1 MB)

- **Frackture (compact)**: ~16132×
- **Encode speed (avg)**: ~154 MB/s (real datasets)
- **Decode speed (avg)**: ~3944 MB/s (real datasets)

#### XLarge+ (10 MB+)

- **Frackture (compact)**: ~161k× at 10 MB, ~1.6M× at 100 MB
- **Recommendation**: Frackture is most compelling here for fixed-size signatures of very large payloads

---

## Advanced Scenarios

### Scenario 1: Deduplication System

**Goal**: Detect duplicate files across millions of documents.

**Setup**:
```bash
# Benchmark on large, diverse datasets
python benchmark_frackture.py --large-only --real
```

**What to look for**:
- Determinism: Must be 100% (ensures same file = same fingerprint)
- Encode speed: Should be 100+ MB/s (for fast indexing)
- Memory: Should be < 20 MB (for scalability)

**Why Frackture can work here**:
- Fixed **65-byte** compact payloads (constant index size)
- Deterministic (reliable candidate generation)
- Decode is very fast for larger payloads (reconstruction is cheap)

### Scenario 2: ML Embedding Storage

**Goal**: Store 1 billion BERT embeddings (768-dim each).

**Math**:
- Raw: 1B × 768 float32 = 1B × 3072 bytes ≈ 2.8 TB
- Frackture: 1B × 65 bytes ≈ 65 GB
- **Savings**: ~97.7% reduction (lossy)

**Setup**:
```bash
# Benchmark on medium datasets (100 KB ≈ 13,000 floats ≈ 17 embeddings)
python benchmark_frackture.py --medium-only --verify-only --detailed
```

**What to look for**:
- MSE: Should be < 0.01 (acceptable quality loss)
- Optimization: Should reduce MSE by 10-30%
- Throughput: Should be 100+ MB/s (for batch processing)

**Why Frackture wins**:
- Perfect fit for 768-dim vectors
- Lossy compression acceptable for embeddings
- Self-optimization tunes for your data distribution
- Fast decode for similarity search

### Scenario 3: Real-Time Integrity Checking

**Goal**: Verify file integrity in a distributed system every second.

**Setup**:
```bash
# Test hash performance
python benchmark_frackture.py --small-only --verify-only
```

**What to look for**:
- Hash time: Should be < 1 ms for small files
- Fault injection: Should pass all corruption tests
- Memory: Should be minimal (< 5 MB)

**Why Frackture wins**:
- Faster than SHA256 (0.5-1 ms vs 1-3 ms for 100 KB)
- Includes entropy signature (detects subtle corruption)
- Built-in HMAC support (authenticated hashes)
- Constant-time comparison (timing-attack resistant)

### Scenario 4: Large-Scale Archive Fingerprinting

**Goal**: Generate signatures for 100 TB of archival data.

**Setup**:
```bash
# Test extreme sizes
python benchmark_frackture.py --extreme --real
```

**What to look for**:
- Encode speed: Should remain stable 150-200 MB/s
- Memory: Should not scale with input size
- Compression ratio: Should be millions-to-one

**Why Frackture wins**:
- Constant memory usage (doesn't grow with input)
- Fixed-size output (predictable storage requirements)
- Stable performance at any scale
- Can process TB files in minutes

---

## Troubleshooting

### "brotli not available"

```bash
pip install brotli
```

Brotli is optional but recommended for complete comparisons.

### "psutil not available"

```bash
pip install psutil
```

Without psutil, memory tracking uses `tracemalloc` (less accurate but functional).

### "yaml not available"

```bash
pip install pyyaml
```

Required for dataset repository. Core dependency as of v2.0.

### Benchmarks running slow

- Use `--small-only` to skip large datasets
- Use `--no-tiny` to skip tiny dataset tests
- Avoid `--extreme` unless needed (100 MB+ is very slow)

### Unexpected MSE values

- Check input data (random noise has high MSE)
- Try optimization (`--detailed` shows improvement)
- Compare against baseline (some data just doesn't compress well)

### Non-deterministic results

- Should never happen - file a bug if you see drifts
- Check for filesystem-level data corruption
- Verify NumPy version (old versions had floating-point issues)

---

## Summary

Frackture is optimized for:

1. **Deterministic fixed-size sketching** (65-byte compact payloads)
2. **Near-duplicate / similarity workflows** where “shape of bytes” is relevant (non-semantic)
3. **Replacing stored float vectors** when you can tolerate a lossy sketch (e.g., you need a deterministic 768-D proxy but can’t afford 3–6 KB per item)

Use other tools when:

- You need **lossless** reconstruction → gzip/brotli/zstd
- You need **cryptographic content addressing** → SHA-256 / BLAKE3
- You need **semantic similarity** → learned embeddings

### Quick comparative tables (real datasets)

These are averages across 14 real datasets:

| Tier | Source results | Frackture output | Frackture encode MB/s | Frackture decode MB/s |
|---|---|---:|---:|---:|
| 100 KB | `benchmark_results_20251215_102813.json` | 65 B | ~15 | ~377 |
| 1 MB | `benchmark_results_20251215_103006.json` | 65 B | ~154 | ~3944 |

For full details and gzip/brotli sweeps, see:
- [BENCHMARK_SUITE_SUMMARY.md](../BENCHMARK_SUITE_SUMMARY.md)
- [docs/USE_CASES.md](./USE_CASES.md)
- [benchmarks/README.md](../benchmarks/README.md)
