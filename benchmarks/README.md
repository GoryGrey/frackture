# Frackture Benchmark Suite

This directory contains a comprehensive benchmark suite for comparing Frackture's compression, encryption, and hashing performance against industry-standard compression algorithms (gzip and brotli).

## 📋 Overview

The benchmark suite tests Frackture against:
- **gzip**: Popular general-purpose compression (part of Python standard library)
- **brotli**: Modern compression algorithm with better ratios (optional, requires `pip install brotli`)

## 🎯 What is Measured

For each compression method and dataset, the suite measures:

1. **Compression Ratio**: `original_size / compressed_size` (higher is better)
2. **Encode Time**: Time to compress data (lower is better)
3. **Decode Time**: Time to decompress data (lower is better)
4. **Encode Throughput**: MB/s during compression (higher is better)
5. **Decode Throughput**: MB/s during decompression (higher is better)
6. **Hash Latency**: Time to generate a hash (lower is better)
7. **Peak Memory**: Maximum memory usage in MB (lower is better)

## 📊 Test Datasets

The suite tests against various data types to show performance across different scenarios:

### Small Datasets (100 KB each)
- **text**: Lorem Ipsum-style plain text
- **json**: Structured JSON data with users and metadata
- **binary_blob**: Mixed binary data (partially compressible)
- **random_noise**: Random bytes (incompressible)
- **highly_repetitive**: Highly repetitive patterns (very compressible)

### Large Datasets (1 MB each)
Same types as above, but 10x larger to test performance at scale.

## 🚀 Running the Benchmarks

### Basic Usage

Run all benchmarks:
```bash
cd benchmarks
python benchmark_frackture.py
```

### Advanced Options

Run only small dataset benchmarks (100KB):
```bash
python benchmark_frackture.py --small-only
```

Run only large dataset benchmarks (1MB):
```bash
python benchmark_frackture.py --large-only
```

Specify custom output directory:
```bash
python benchmark_frackture.py --output-dir /path/to/results
```

### Requirements

Install optional dependencies for complete benchmarks:
```bash
pip install brotli psutil
```

- `brotli`: For brotli compression benchmarks (optional but recommended)
- `psutil`: For more accurate memory tracking (optional)

## 📈 Understanding Results

### Console Output

Results are displayed in formatted tables showing all metrics for easy comparison:

```
========================================================================================================
Dataset: small_text
========================================================================================================
| Method               | Original     | Compressed   | Ratio    | Encode (ms)  | Decode (ms)  | ...
|----------------------|--------------|--------------|----------|--------------|--------------|-----
| Frackture            | 100.00 KB    | 96 B         | 1065.33x | 2.45         | 0.82         | ...
| Gzip (level 6)       | 100.00 KB    | 35.21 KB     | 2.84x    | 1.23         | 0.56         | ...
| Brotli (quality 6)   | 100.00 KB    | 28.44 KB     | 3.52x    | 15.67        | 0.45         | ...
========================================================================================================
```

### JSON Output

Structured data saved to `results/benchmark_results_TIMESTAMP.json`:
```json
{
  "timestamp": "2024-01-01 12:00:00",
  "results": {
    "small_text": [
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
        "success": true
      }
    ]
  }
}
```

### Markdown Output

Human-readable summary saved to `results/benchmark_results_TIMESTAMP.md` with:
- Formatted tables for each dataset
- Key observations and metrics explanations
- Frackture's unique advantages

## 🔍 Interpreting Results

### Frackture's Unique Position

Frackture is **not a traditional compression algorithm**. Key differences:

1. **Fixed-Size Output**: Frackture always produces ~96 bytes, regardless of input size
   - This means it excels at creating compact fingerprints/signatures
   - Traditional compression algorithms scale with input size

2. **Dual-Channel Encoding**: 
   - Symbolic channel: Identity-preserving fingerprint
   - Entropy channel: Frequency/pattern signature

3. **Use Cases**:
   - ✅ **Identity-preserving hashes**: Fixed-size unique signatures
   - ✅ **Data fingerprinting**: Detect similarity and patterns
   - ✅ **Embedding compression**: Compact representations for ML/AI
   - ✅ **Integrity checking**: Fast verification with entropy awareness
   - ❌ **General-purpose compression**: Not designed to replace gzip/brotli

### Expected Performance Characteristics

**Frackture Advantages:**
- Extremely high compression ratios for large inputs (fixed 96-byte output)
- Fast hashing and fingerprinting
- Consistent memory usage
- Identity preservation across similar inputs

**Frackture Trade-offs:**
- Lossy compression (reconstruction is approximate)
- May not compress small inputs (<100 bytes)
- Different paradigm than traditional lossless compression

**Traditional Compression (gzip/brotli) Advantages:**
- Lossless compression (perfect reconstruction)
- Better for general file compression
- Variable compression ratios based on content

## 🎛️ Customizing Benchmarks

### Adding New Datasets

Edit `benchmark_frackture.py` and add to `DatasetGenerator`:

```python
@staticmethod
def generate_custom(size_kb: int = 100) -> bytes:
    # Your custom data generation logic
    return data

# Then add to get_all_datasets():
datasets = {
    # ... existing datasets ...
    "custom": DatasetGenerator.generate_custom(size)
}
```

### Adjusting Compression Levels

Modify the calls in `run_benchmark_suite()`:

```python
# Gzip: levels 1-9 (1=fastest, 9=best compression)
result = BenchmarkRunner.benchmark_gzip(data, level=9)

# Brotli: quality 0-11 (0=fastest, 11=best compression)
result = BenchmarkRunner.benchmark_brotli(data, quality=11)
```

## 📁 Output Files

All results are saved to `benchmarks/results/` with timestamps:
- `benchmark_results_YYYYMMDD_HHMMSS.json`: Structured data for analysis
- `benchmark_results_YYYYMMDD_HHMMSS.md`: Human-readable report

## 🐛 Troubleshooting

**Error: "brotli not available"**
```bash
pip install brotli
```

**Error: "No module named 'psutil'"**
```bash
pip install psutil
```
(psutil is optional - benchmarks will use tracemalloc instead)

**Memory tracking seems inaccurate**
- Install psutil for more accurate OS-level memory tracking
- Without psutil, tracemalloc only tracks Python object memory

## 📊 Example Results

Here's what to expect from a typical run:

**Small Text (100KB)**:
- Frackture: ~96 bytes (1000x+ compression ratio)
- Gzip: ~35KB (2-3x compression ratio)
- Brotli: ~28KB (3-4x compression ratio)

**Random Noise (100KB)**:
- Frackture: ~96 bytes (1000x+ compression ratio)
- Gzip: ~102KB (0.98x - slightly larger!)
- Brotli: ~102KB (0.98x - slightly larger!)

This shows Frackture's fixed-size advantage for fingerprinting, while traditional algorithms struggle with incompressible data.

## 🤝 Contributing

To add new benchmark scenarios:
1. Add dataset generators to `DatasetGenerator`
2. Add benchmark methods to `BenchmarkRunner`
3. Update result formatters if adding new metrics
4. Update this README with guidance

## 📝 License

Same as Frackture - MIT License
