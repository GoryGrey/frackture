# Frackture Analysis Dashboard (Benchmark-Backed)

**Sources (committed JSON outputs):**

- 100 KB tier (real datasets): `benchmarks/results/benchmark_results_20251215_102813.json`
- 1 MB tier (real datasets): `benchmarks/results/benchmark_results_20251215_103006.json`
- Full competitor sweeps across tiers: `benchmarks/results/benchmark_results_20251215_102604.json`

This report is intended to be **honest and decision-oriented**. Frackture is best interpreted as deterministic **lossy content sketching**, not a drop-in replacement for gzip/brotli and not a semantic embedding model.

## 1) Executive Summary

- **Compact output size:** 65 bytes (`FrackturePayload.to_bytes()`)
- **Determinism:** Verified across repeated encodes in the benchmark suite
- **Losslessness:** No (reconstruction is approximate)
- **Ratio vs gzip/brotli:** Usually wins for non-tiny tiers because output is fixed-size
- **Encode throughput:** Often slower than gzip/brotli
- **Decode throughput:** Can be very fast for larger payloads (≥ 1 MB)

## 2) Headline comparison tables (averages across 14 real datasets)

### 100 KB tier

| Method | Output (avg) | Ratio (avg) | Encode (avg MB/s) | Decode (avg MB/s) | Notes |
|---|---:|---:|---:|---:|---|
| **Frackture (compact)** | **65 B** | **1575×** | 14.9 | 377.0 | Fixed-size, lossy sketch |
| gzip (L6) | 818 B | 146× | 234.9 | 1125.5 | Lossless |
| brotli (Q6) | 292 B | 579× | 446.9 | 876.3 | Lossless |
| SHA-256 (hex) | 64 B | 1600× | 1243.3 | — | Integrity/content id only |

### 1 MB tier

| Method | Output (avg) | Ratio (avg) | Encode (avg MB/s) | Decode (avg MB/s) | Notes |
|---|---:|---:|---:|---:|---|
| **Frackture (compact)** | **65 B** | **16132×** | 153.7 | **3944.4** | Decode is very fast |
| gzip (L6) | 4991 B | 231× | 263.4 | 1760.1 | Lossless |
| brotli (Q6) | 344 B | 4349× | 785.1 | 914.0 | Lossless |
| SHA-256 (hex) | 64 B | 16384× | 1287.6 | — | Integrity/content id only |

## 3) gzip/brotli sweep win rates (ratio vs encode throughput)

From `benchmark_results_20251215_102604.json` (gzip levels 1–9, brotli qualities 0–11):

| Tier | Frackture win-rate (compression ratio) | Frackture win-rate (encode throughput) |
|---|---:|---:|
| tiny | 25.0% | 0.0% |
| small | 93.5% | 0.0% |
| medium | 96.9% | 1.0% |
| large | 98.6% | 10.5% |
| xlarge | 100.0% | 100.0% |

**Interpretation:** if you measure “compression ratio” as `input_size / output_size`, Frackture will naturally dominate once inputs are non-trivial. If you care about CPU time at encode, gzip/brotli are typically faster for compressible data.

## 4) Notes / limitations surfaced by the suite

- The benchmark schema still includes a `payload_is_96b` flag. Current Frackture compact payloads are **65 bytes**, so that legacy flag should not be used as a correctness criterion.
- “Fault injection” outcomes depend on what you mean by detection:
  - The **raw compact payload** has no checksum; bit flips may still deserialize and reconstruct.
  - The authenticated envelope (`frackture_encrypt_payload` / `frackture_decrypt_payload`) detects tampering via HMAC.

## 5) Recommendation shortcut

Use:

- **gzip/brotli/zstd** when you need lossless compression.
- **SHA-256 / BLAKE3** when you need cryptographic content addressing.
- **learned embeddings** when you need semantic similarity.
- **Frackture** when you want a deterministic, fixed-size, similarity-friendly sketch.

See **[docs/USE_CASES.md](../docs/USE_CASES.md)** for a decision tree and end-to-end pipelines.
