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

## 2. Key Questions & Answers

### (1) Is the payload size fixed at 96 bytes?
**No.** The payload size varies between 173 and 408 bytes (Avg: 331.9), contradicting the fixed 96-byte target.

**Details:**
- **Symbolic bytes:** 32 (constant)
- **Entropy bytes:** 128 (constant)
- **Serialization overhead:** Variable (173-408 bytes including encoding/encryption overhead)
- **Variance:** 10586.79
- **Samples:** 20

**Implication:** Serialized payload is NOT fixed at 96B. It ranges wider due to pickle/JSON encoding overhead. This affects bandwidth and storage predictions.

### (2) Is Frackture lossy or lossless in practice?
**Lossy.** Frackture is by design a lossy compression algorithm.

**Evidence:**
- Lossy runs: 19 / 20 (95%)
- Lossless runs: 1 (edge cases)
- Average MSE (optimized): See reconstruction quality metrics below

**Mechanism:** Frackture uses dual-channel design (symbolic + entropy) that sacrifices exact restoration for compression ratio. Reconstruction minimizes MSE rather than guaranteeing bitwise accuracy.

### (3) What compression ratios and throughput does Frackture achieve?
**Compression Ratio:** 47083.35x average

- Best: 606113.29x
- Worst: 0.02x
- Median: 883.51x

**Throughput:** 2146.05 MB/s average

- Best: 19948.52 MB/s
- Worst: 0.00 MB/s
- Median: 57.51 MB/s

### (4) How does Frackture compare to Gzip/Brotli in compression & throughput?
| Method | Compression Ratio | Throughput (MB/s) | Memory (MB) |
|---|---|---|---|
| SHA | 365689.91x | 1023.78 | 195.6 |
| Frackture | 47083.35x | 2146.05 | 237.6 |
| Frackture Encrypted | 30021.84x | 150.88 | 239.9 |
| Brotli | 4420.86x | 247.35 | 135.6 |
| Gzip | 155.14x | 103.73 | 178.4 |
| AES | 0.91x | 1235.50 | 217.6 |

**Summary:** Frackture achieves 47083.35x compression on average. See weaknesses section for competitive gaps.

### (5) What is the latency comparison for hashing/encryption operations?
| Operation | Avg Latency (ms) | Min | Max |
|---|---|---|---|
| Aes Gcm | 150.4581 | 0.0045 | 2304.4148 |
| Frackture Encrypt | 147.1597 | 0.0037 | 2255.0061 |
| Frackture Hash | 118.7313 | 0.0117 | 1682.6615 |
| Sha256 | 7.9182 | 0.0039 | 70.7418 |

**Frackture vs SHA256:** Frackture is 0.1x faster (118.7313ms vs 7.9182ms)

**Frackture Encrypted vs AES-GCM:** Frackture is 1.0x faster (147.1597ms vs 150.4581ms)


### (6) What self-optimization gains are achieved?
**MSE Improvement:** 22.35% average (Max: 53.16%)

The optimization loop successfully reduces reconstruction error by iteratively adjusting decoder parameters. This improves fidelity without sacrificing compression.

### (7) Is determinism validated? Are fault injection tests passing?
**Determinism:** ✓ **PASS** - All 20 runs produced identical outputs for identical inputs.

**Fault Injection:** ✗ **FAIL** - Fault injection failed in 20/20 cases. Mutations not reliably detected in 20 tests.

**Reliability Status:** Determinism is validated, but fault injection detection has gaps.

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

## 4. Detected Weaknesses & Competitive Gaps

### ⚠️ Weakness #1: Low Compression in Tiny (<100B)
**Issue:** Frackture achieves only 0.12x compression in Tiny (<100B) - poor for general-purpose compression
**Frackture Ratio:** 0.12x

### ⚠️ Weakness #2: Fault Injection Detection Gaps
**Issue:** Fault injection detection failed in 20 cases - mutations not properly detected
**Impact:** Payload mutations (bit flips, truncation) not reliably detected in encrypted or optimized modes.
**Recommendation:** Review HMAC authentication and error detection logic.

## 5. Interpretation & Recommendations

### When to Use Frackture
- **Symbolic fingerprinting:** Fast, deterministic hashing for deduplication/change detection
- **Extreme compression:** Specialized datasets with high entropy patterns (achieve 100k+x ratios)
- **Encrypted transmission:** Built-in HMAC-SHA256 authentication with compression
- **Memory-constrained systems:** Small fixed payload (~96B symbolic + 128B entropy core)

### When NOT to Use Frackture
- **Lossless requirement:** Frackture is inherently lossy; use Gzip/Brotli for exact restoration
- **Small payloads (<100B):** Overhead dominates; compression ratios can be <1x
- **General-purpose compression:** Gzip/Brotli offer better compatibility and tuning
- **Fault tolerance critical:** Fault injection detection is not yet reliable

