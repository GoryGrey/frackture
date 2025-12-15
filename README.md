# Frackture

[![PyPI version](https://img.shields.io/pypi/v/frackture.svg)](https://pypi.org/project/frackture/)
[![Downloads](https://img.shields.io/pypi/dm/frackture.svg)](https://pypi.org/project/frackture/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE)

Frackture is a **deterministic, lossy content sketching** library.

- Input: arbitrary Python data (bytes/text/JSON/arrays)
- Output: a **fixed-size 65-byte compact payload**
- Reconstruction: a deterministic **768-float vector** suitable for similarity-style comparisons

Frackture is **not** a general-purpose lossless compressor (gzip/brotli) and **not** a semantic embedding model.

## Decision tree (when to use Frackture)

```
Need exact bytes back?
  └─ yes → gzip / brotli / zstd
  └─ no
      Need cryptographic content addressing / integrity?
        └─ yes → SHA-256 / BLAKE3
        └─ no
            Need semantic similarity (meaning of text)?
              └─ yes → learned embeddings + vector DB
              └─ no → Frackture (fixed-size deterministic sketch)
```

For deeper guidance (with pipelines and limitations), see **[docs/USE_CASES.md](./docs/USE_CASES.md)**.

## What the 65-byte payload is

The compact format is:

- 1-byte header (version + tier flags)
- 32 bytes symbolic channel
- 32 bytes quantized entropy channel

In code, this is `FrackturePayload.to_bytes()`.

## Quick start (repo-local import)

The core module file in this repo is named **`frackture (2).py`** (note the space). The snippets below use a safe import that works from the repo root.

```python
import importlib.util

spec = importlib.util.spec_from_file_location("frackture", "frackture (2).py")
frackture = importlib.util.module_from_spec(spec)
spec.loader.exec_module(frackture)

payload = frackture.compress_simple(
    "Error: timeout calling service A",
    tier=frackture.CompressionTier.DEFAULT,
    optimize=True,
    return_format="compact",
)

print(len(payload))  # 65

vec = frackture.decompress_simple(payload)
print(vec.shape)  # (768,)
```

More examples: **[docs/EXAMPLES.md](./docs/EXAMPLES.md)**.

## Benchmarks (scientific, reproducible)

Benchmark sources committed in this repo:

- 100 KB tier (real datasets): `benchmarks/results/benchmark_results_20251215_102813.json`
- 1 MB tier (real datasets): `benchmarks/results/benchmark_results_20251215_103006.json`
- Full gzip/brotli sweep + win rates: `benchmarks/results/benchmark_results_20251215_102604.json`

### Average performance @ 100 KB (14 real datasets)

| Method | Output (avg) | Ratio (avg) | Encode (avg MB/s) | Decode (avg MB/s) |
|---|---:|---:|---:|---:|
| **Frackture (compact)** | **65 B** | **1575×** | 14.9 | 377.0 |
| gzip (L6) | 818 B | 146× | 234.9 | 1125.5 |
| brotli (Q6) | 292 B | 579× | 446.9 | 876.3 |
| SHA-256 (hex) | 64 B | 1600× | 1243.3 | — |

### Average performance @ 1 MB (14 real datasets)

| Method | Output (avg) | Ratio (avg) | Encode (avg MB/s) | Decode (avg MB/s) |
|---|---:|---:|---:|---:|
| **Frackture (compact)** | **65 B** | **16132×** | 153.7 | **3944.4** |
| gzip (L6) | 4991 B | 231× | 263.4 | 1760.1 |
| brotli (Q6) | 344 B | 4349× | 785.1 | 914.0 |
| SHA-256 (hex) | 64 B | 16384× | 1287.6 | — |

### Win rates vs gzip/brotli across tiers (full sweep)

| Tier | Frackture win-rate (compression ratio) | Frackture win-rate (encode throughput) |
|---|---:|---:|
| tiny | 25.0% | 0.0% |
| small | 93.5% | 0.0% |
| medium | 96.9% | 1.0% |
| large | 98.6% | 10.5% |
| xlarge | 100.0% | 100.0% |

Interpretation:

- If you measure “compression ratio” as `input_size / output_size`, Frackture naturally dominates once inputs are not tiny.
- For typical CPU workloads, gzip/brotli are often faster to encode.
- Frackture decode can be very fast for larger inputs.

Full methodology: **[docs/BENCHMARKING.md](./docs/BENCHMARKING.md)**.

## Trade-offs / limitations

- **Lossy**: reconstruction is approximate and should be treated as a similarity surrogate, not content recovery.
- **Not semantic**: Frackture does not model meaning like learned embeddings.
- **Not cryptographic**: the symbolic channel is deterministic but is not a cryptographic hash; use SHA-256/BLAKE3 for integrity.
- **Tiny inputs**: if your input is smaller than 65 bytes, the sketch is larger than the original.

## Documentation

- **[docs/USE_CASES.md](./docs/USE_CASES.md)**: decision tree + deep use-case guidance
- **[docs/EXAMPLES.md](./docs/EXAMPLES.md)**: copy/paste code
- **[docs/BENCHMARKING.md](./docs/BENCHMARKING.md)**: methodology + interpretation
- **[docs/ARCHITECTURE.md](./docs/ARCHITECTURE.md)**: algorithms and design
- **[analysis/report.md](./analysis/report.md)**: benchmark-backed narrative summary

## Attribution

Per the MIT license, please cite:

*"Frackture: Recursive Compression & Symbolic Encoding, by Gregory Betti (f(∞))"*

Author: [@GoryGrey](https://x.com/GoryGrey)
