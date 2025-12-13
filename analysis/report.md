# Frackture Analysis Dashboard

**Source:** `benchmark_results_20251213_171939.json`
**Timestamp:** 2025-12-13 17:19:39

## 1. Executive Summary

| Metric | Value |
|---|---|
| **Avg Compression Ratio** | 47083.35x |
| **Avg Throughput** | 2146.05 MB/s |
| **Avg Optimization Gain** | 22.35% |
| **Payload Fixed?** | No (Range: 173-408 bytes) |
| **Lossless?** | No (Lossy runs: 19/20) |
| **Deterministic?** | Yes |

## 2. Key Questions

### Is the payload size fixed at 96 bytes?
**No.** The payload size varies between 173 and 408 bytes (Avg: 331.9). This contradicts the 96-byte target in some cases.

### Is Frackture lossy or lossless?
**Lossy.** Frackture is primarily a lossy compression algorithm. 19 out of 20 runs were lossy. Reconstruction relies on minimizing MSE rather than exact bitwise restoration.

### What compression gains does Frackture achieve?
On average, Frackture achieves **47083.35x** compression.
- **Best case:** 606113.29x
- **Worst case:** 0.02x

### How does it compare to Gzip/Brotli/AES/SHA?
| Method | Ratio | Speed (MB/s) | Memory (MB) |
|---|---|---|---|
| SHA | 365689.91x | 1023.78 | 195.6 |
| Frackture | 47083.35x | 2146.05 | 237.6 |
| Frackture Encrypted | 30021.84x | 150.88 | 239.9 |
| Brotli | 4420.86x | 247.35 | 135.6 |
| Gzip | 155.14x | 103.73 | 178.4 |
| AES | 0.91x | 1235.50 | 217.6 |

### Is determinism validated?
**Yes.** All 20 runs produced identical outputs for identical inputs.

## 3. Performance Highlights

### Performance by Size Tier
| Tier | Avg Ratio | Avg Speed (MB/s) | Count |
|---|---|---|---|
| Small/Medium (100KB+) | 1808.75x | 100.53 | 11 |
| Tiny (<100B) | 0.12x | 0.01 | 5 |
| Extreme (>100MB) | 432191.62x | 19612.63 | 2 |
| Large (1MB+) | 28693.41x | 1294.96 | 2 |

### Random vs Repetitive Data
| Data Type | Avg Ratio | Avg MSE |
|---|---|---|
| Mixed/Other | 54067.90x | 0.2055 |
| Random | 57384.70x | 0.1547 |
| Repetitive | 1976.23x | 0.2270 |

### Optimization Gains
The optimization loop improved reconstruction MSE by an average of **22.35%** (Max: 53.16%).
Trend: `▄▂█▂▇▃▂█ ▇▃▃ ▂▆▃ ▃▄▂`

### Reliability & Fault Injection
- **Fault Injection:** Failed
- **Passed Runs:** 0
- **Failed Runs:** 20

### Throughput Distribution
Encoding Speed (MB/s): `                █▇  `
Range: 0.00 - 19948.52 MB/s
