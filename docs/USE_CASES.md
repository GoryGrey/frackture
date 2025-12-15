# Frackture Use Cases (Decision-Driven)

Frackture is best understood as **deterministic lossy content sketching**:

- Input: any Python data (bytes/text/JSON/arrays)
- Output: a **fixed-size 65-byte compact payload** (`FrackturePayload.to_bytes()`)
- Reconstruction: a deterministic **768-float vector** (useful as a similarity surrogate)

It is **not** a replacement for lossless compression or semantic embeddings. It is useful when you want a small, deterministic, content-derived representation that can be compared and reconstructed into a stable vector space.

Benchmarks referenced below are from the repo’s benchmark suite on real datasets:

- 100 KB tier: `benchmarks/results/benchmark_results_20251215_102813.json`
- 1 MB tier: `benchmarks/results/benchmark_results_20251215_103006.json`
- Full gzip/brotli sweep + win-rate summary: `benchmarks/results/benchmark_results_20251215_102604.json`

## Decision tree

```
Need exact bytes back?
  └─ yes → gzip / brotli / zstd
  └─ no
      Need cryptographic integrity / content addressing?
        └─ yes → SHA-256 (or BLAKE3)
        └─ no
            Need semantic similarity ("meaning" of text)?
              └─ yes → learned embeddings + vector DB
              └─ no
                  Need deterministic, fixed-size, similarity-friendly sketch?
                    └─ yes → Frackture (store payload, compare reconstructed vectors)
                    └─ no → pick simpler hashes / heuristics
```

## Trade-offs (from benchmark data)

| Property | Frackture | gzip/brotli | SHA-256 | Learned embeddings |
|---|---:|---:|---:|---:|
| Output size | **65 B fixed** (compact) | Variable | 32 B (raw) / 64 B (hex) fixed | Typically 384–3072 dims (1.5–12 KB @ float32) |
| Determinism | Yes | Yes | Yes | Usually yes for a fixed model + deterministic kernels (often not enforced in practice) |
| Losslessness | **No** | Yes | N/A | N/A |
| Semantic signal | No (byte/statistics derived) | No | No | **Yes** |
| Encode throughput @ 100 KB (avg) | **~14.9 MB/s** | gzip L6 ~234.9 MB/s, brotli Q6 ~446.9 MB/s | ~1243 MB/s (hashing) | typically slower than hashing; model-dependent |
| Decode throughput @ 1 MB (avg) | **~3944 MB/s** | gzip L6 ~1760 MB/s, brotli Q6 ~914 MB/s | N/A | N/A |

Numbers above are averages across 14 real datasets.

## 1) Deterministic ML embeddings (vector-DB alternative for non-semantic similarity)

### What you get

- A deterministic way to map *content bytes* → fixed-size payload → stable 768-D vector.
- Useful for **content similarity and clustering** when you do *not* require semantic understanding.

### When to use (vs embeddings/gzip/SHA-256)

Use Frackture when:
- You need a **small, deterministic** representation of content.
- You want **similarity search** on “content shape” (byte distribution/frequency patterns), not meaning.
- You want to store *something vector-like* but **cannot afford storing float vectors**.

Prefer learned embeddings when:
- You need **semantic** similarity (natural language meaning, intent, paraphrases).

Prefer gzip/brotli when:
- You must keep the original bytes and want bandwidth/storage reduction.

Prefer SHA-256 when:
- You need cryptographic content addressing / integrity (and no similarity).

### Example: sketch + similarity search (pipeline + reconstruction)

This snippet is self-contained for this repo (note the filename contains a space).

```python
import importlib.util
import numpy as np

spec = importlib.util.spec_from_file_location("frackture", "frackture (2).py")
frackture = importlib.util.module_from_spec(spec)
spec.loader.exec_module(frackture)


def frackture_vector(text: str) -> np.ndarray:
    payload_bytes = frackture.compress_simple(
        text,
        tier=frackture.CompressionTier.DEFAULT,  # keep comparisons consistent
        optimize=True,  # better reconstruction fidelity
        return_format="compact",
    )
    return frackture.decompress_simple(payload_bytes)


def cosine(a: np.ndarray, b: np.ndarray) -> float:
    a = a.astype(np.float32)
    b = b.astype(np.float32)
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b) + 1e-12))


docs = {
    "doc_a": "Error: connection timeout while calling service A",
    "doc_b": "Error: connection timed out while calling service A",
    "doc_c": "A completely unrelated paragraph about biology.",
}

vectors = {k: frackture_vector(v) for k, v in docs.items()}

query = "Error: timeout calling service A"
qv = frackture_vector(query)

scores = sorted(((k, cosine(qv, v)) for k, v in vectors.items()), key=lambda x: x[1], reverse=True)
print(scores)
```

### Configuration knobs

- **Tier** (`CompressionTier.TINY|DEFAULT|LARGE`):
  - Auto-selected by input size, but for “embedding-like” comparisons you typically want to **force `DEFAULT`** so all items are encoded with the same reconstruction weighting.
- **Optimization trials** (`optimize=True` or `optimize_frackture(..., num_trials=...)`):
  - More trials → lower MSE → better vector fidelity, at a compute cost.

## 2) Lossy deduplication and lossy storage

### What you get

- A fixed-size content sketch suitable for **bucketing**, **dedup candidates**, and “store-the-sketch” workflows.
- Optional reconstruction into a vector to compute distances for near-duplicate detection.

### When to use (vs gzip/SHA-256/embeddings)

Use Frackture when:
- You want to **store only a sketch**, not the original.
- You want to identify **near duplicates** (not only byte-identical duplicates).

Prefer SHA-256 when:
- You only care about exact duplicates and you need strong collision resistance.

Prefer gzip/brotli when:
- You want to **store the original bytes** but smaller.

Prefer embeddings when:
- You want “duplicate meaning” (semantic dedup), e.g. paraphrases.

### Example: two-stage dedup (fast key + near-duplicate check)

```python
import importlib.util
import numpy as np

spec = importlib.util.spec_from_file_location("frackture", "frackture (2).py")
frackture = importlib.util.module_from_spec(spec)
spec.loader.exec_module(frackture)


def frackture_payload_and_vec(data: bytes):
    payload = frackture.compress_simple(data, optimize=True, return_format="compact")
    vec = frackture.decompress_simple(payload)
    return payload, vec


def l2(a: np.ndarray, b: np.ndarray) -> float:
    d = a.astype(np.float32) - b.astype(np.float32)
    return float(np.sqrt(np.dot(d, d)))

store = {}  # id -> (payload_bytes, vector)

items = {
    "a": b"hello world\n" * 1000,
    "b": b"hello world\n" * 1000 + b"!",  # near-duplicate
    "c": b"completely different" * 200,
}

for k, v in items.items():
    payload, vec = frackture_payload_and_vec(v)

    # Stage 1: exact match on payload bytes (very strict)
    for existing_id, (existing_payload, existing_vec) in store.items():
        if payload == existing_payload:
            print(f"exact duplicate: {k} == {existing_id}")
            break

        # Stage 2: near-duplicate by distance in reconstructed space
        if l2(vec, existing_vec) < 2.0:
            print(f"near duplicate candidate: {k} ~ {existing_id}")

    store[k] = (payload, vec)
```

### Configuration knobs

- If your inputs are mostly >100 B, `DEFAULT` tier is usually fine.
- For very small payloads, Frackture’s fixed output can be larger than the input; see the benchmark sweep win rates (tiny tier).

## 3) Deterministic content addressing (exact + similarity-friendly)

### What you get

A practical pattern is to store **two keys**:

1. **SHA-256** (exact content addressing, cryptographic)
2. **Frackture** payload/symbolic component (similarity-friendly sketch)

This lets you keep the standard “content hash” property while enabling similarity search and approximate grouping.

### When to use

Use SHA-256 alone when:
- You need a strong, conventional content identifier.

Add Frackture when:
- You also want to find “nearby” content without computing embeddings.

### Example: dual-key content store

```python
import importlib.util
import hashlib

spec = importlib.util.spec_from_file_location("frackture", "frackture (2).py")
frackture = importlib.util.module_from_spec(spec)
spec.loader.exec_module(frackture)


def content_address(data: bytes):
    sha256_hex = hashlib.sha256(data).hexdigest()
    fr_bytes = frackture.compress_simple(data, optimize=False, return_format="compact")

    # You can also key on the symbolic 32 bytes (not cryptographic, but stable):
    fr_payload = frackture.deserialize_frackture_payload(fr_bytes)
    symbolic_hex = fr_payload.symbolic.hex()

    return sha256_hex, symbolic_hex, fr_bytes

blob = b"example payload" * 1000
sha256_hex, symbolic_hex, fr_bytes = content_address(blob)
print("sha256:", sha256_hex)
print("frackture symbolic:", symbolic_hex)
print("frackture bytes:", len(fr_bytes))
```

### Notes and limitations

- Frackture’s symbolic component is **not a cryptographic hash**.
- If you need tamper detection for a stored payload, use the authenticated envelope (`frackture_encrypt_payload(...)`) and verify with `frackture_decrypt_payload(...)`. (This authenticates; it does not hide content.)

## Benchmarks (quick reference tables)

### Average performance @ 100 KB (14 real datasets)

From `benchmarks/results/benchmark_results_20251215_102813.json`:

| Method | Output (avg) | Ratio (avg) | Encode (avg MB/s) | Decode (avg MB/s) | Notes |
|---|---:|---:|---:|---:|---|
| Frackture | 65 B | 1575× | 14.9 | 377 | Fixed-size, lossy, deterministic |
| gzip (L6) | 818 B | 146× | 234.9 | 1125.5 | Lossless; tuned via level |
| brotli (Q6) | 292 B | 579× | 446.9 | 876.3 | Lossless; better ratio than gzip |
| SHA-256 (hex) | 64 B | 1600× | 1243.3 | — | Integrity/content id only |

### Average performance @ 1 MB (14 real datasets)

From `benchmarks/results/benchmark_results_20251215_103006.json`:

| Method | Output (avg) | Ratio (avg) | Encode (avg MB/s) | Decode (avg MB/s) | Notes |
|---|---:|---:|---:|---:|---|
| Frackture | 65 B | 16132× | 153.7 | 3944.4 | Fixed-size, lossy, deterministic |
| gzip (L6) | 4991 B | 231× | 263.4 | 1760.1 | Lossless |
| brotli (Q6) | 344 B | 4349× | 785.1 | 914.0 | Lossless |
| SHA-256 (hex) | 64 B | 16384× | 1287.6 | — | Integrity/content id only |

### Win rates vs gzip/brotli across tiers (full sweep)

From `benchmarks/results/benchmark_results_20251215_102604.json` (gzip levels 1–9, brotli qualities 0–11):

| Tier | Frackture win-rate (compression ratio) | Frackture win-rate (encode throughput) |
|---|---:|---:|
| tiny | 25.0% | 0.0% |
| small | 93.5% | 0.0% |
| medium | 96.9% | 1.0% |
| large | 98.6% | 10.5% |
| xlarge | 100.0% | 100.0% |

Interpretation: Frackture usually wins on “ratio” once the payload is not tiny, but it is often slower to encode than gzip/brotli on typical CPU workloads.
