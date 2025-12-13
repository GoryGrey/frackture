# 🧠 Frackture

[![PyPI version](https://img.shields.io/pypi/v/frackture.svg)](https://pypi.org/project/frackture/)
[![Downloads](https://img.shields.io/pypi/dm/frackture.svg)](https://pypi.org/project/frackture/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE)

**Frackture is a unified symbolic compression, encryption, and hashing library** that combines recursive logic with entropy signatures to create fixed-size (~96-byte) identity-preserving fingerprints.

> Built to push boundaries in compression, data fingerprinting, secure hashing, and self-optimizing logic.

---

## 🌟 What Makes Frackture Unique?

Frackture is **not traditional compression**—it's a symbolic encoding system that:

- 🎯 **Fixed-Size Output**: Always produces ~96 bytes regardless of input size (1KB or 1TB)
- 🧬 **Dual-Channel Architecture**: Combines symbolic fingerprinting with entropy signatures
- 🔐 **Built-in Security**: HMAC-based encryption with tamper detection
- ♻️ **Self-Optimizing**: Decoder feedback loop minimizes reconstruction error
- 🌍 **Universal Input**: Handles text, JSON, binary, arrays, and Python objects
- 🎨 **Identity-Preserving**: Similar inputs produce similar fingerprints

---

## 📊 Quick Comparison

| Feature | Frackture | Traditional Compression (gzip/brotli) |
|---------|-----------|--------------------------------------|
| Output Size | Fixed ~96 bytes | Variable (scales with input) |
| Compression Type | Lossy (fingerprinting) | Lossless (exact) |
| Best For | Identity hashing, fingerprints | General file compression |
| Compression Ratio (1MB) | ~10,000x | 2-10x |
| Speed | 160+ MB/s encode, 4700+ MB/s decode | 25-90 MB/s encode, 300-700 MB/s decode |
| Security | Built-in HMAC encryption | Requires separate encryption |

See [BENCHMARK_SUITE_SUMMARY.md](./BENCHMARK_SUITE_SUMMARY.md) for detailed performance comparisons.

---

## 🚀 Installation

```bash
pip install frackture
```

**Requirements:**
- Python 3.8+
- numpy, scipy, scikit-learn (installed automatically)
- cryptography (optional, for benchmark comparisons)

---

## 💡 Three Primary Use Cases

### 1. 📦 Compression & Fingerprinting

Create fixed-size fingerprints for data integrity, deduplication, or similarity detection:

```python
from frackture import (
    frackture_preprocess_universal_v2_6,
    frackture_v3_3_safe,
    frackture_v3_3_reconstruct
)

# Any input type: str, bytes, dict, list, numpy arrays
data = b"Hello world. This is a test of the emergency broadcast system."

# Preprocess to normalized 768-length vector
preprocessed = frackture_preprocess_universal_v2_6(data)

# Encode to fixed ~96-byte payload
payload = frackture_v3_3_safe(preprocessed)
print(f"Compressed size: {len(payload['symbolic']) + len(payload['entropy']) * 8} bytes")

# Reconstruct approximate representation
reconstructed = frackture_v3_3_reconstruct(payload)

# payload contains:
# - 'symbolic': 64-char hex string (32 bytes) - identity fingerprint
# - 'entropy': 16 floats (128 bytes serialized) - frequency signature
```

**Output structure:**
```python
{
    "symbolic": "a3f5c8e2d9b1f7a4...",  # 64-char hex fingerprint
    "entropy": [0.234, 0.891, ...]      # 16-element frequency signature
}
```

### 2. 🔐 Encryption Mode

Secure payloads with HMAC authentication and tamper detection:

```python
from frackture import (
    frackture_preprocess_universal_v2_6,
    frackture_v3_3_safe,
    frackture_encrypt_payload,
    frackture_decrypt_payload
)

# Create payload
data = "Sensitive information"
preprocessed = frackture_preprocess_universal_v2_6(data)
payload = frackture_v3_3_safe(preprocessed)

# Encrypt with key
encryption_key = "my-secret-key-2024"
encrypted = frackture_encrypt_payload(payload, encryption_key)

# Encrypted structure includes:
# - data: original payload
# - signature: HMAC-SHA256 signature
# - metadata: key_id for verification

# Decrypt with correct key
try:
    decrypted = frackture_decrypt_payload(encrypted, encryption_key)
    print("Decryption successful!")
except ValueError as e:
    print(f"Decryption failed: {e}")  # Wrong key or tampered data
```

**Security features:**
- HMAC-SHA256 authentication
- Constant-time signature comparison (timing-attack resistant)
- Key ID metadata for key management
- Automatic tamper detection

### 3. 🔍 Identity-Preserving Hashing

Generate deterministic hashes for collision testing and data integrity:

```python
from frackture import frackture_deterministic_hash

# Deterministic hashing
data1 = "Hello World"
hash1 = frackture_deterministic_hash(data1)
hash2 = frackture_deterministic_hash(data1)
assert hash1 == hash2  # Always the same for same input

# With salt for namespacing
hash_salted = frackture_deterministic_hash(data1, salt="user_123")

# Different data = different hashes
data2 = "Hello World!"
hash3 = frackture_deterministic_hash(data2)
assert hash1 != hash3  # Different inputs produce different hashes

# Output: 64-character SHA256 hex string
print(f"Hash: {hash1}")  # SHA256 hex digest
```

---

## 🏗️ Architecture Overview

Frackture uses a **dual-channel architecture** for maximum information preservation:

```
Input (any type)
      ↓
┌─────────────────────────────┐
│  Universal Preprocessor     │
│  - Converts any input       │
│  - Normalizes to [0,1]      │
│  - Pads/wraps to 768 floats │
└─────────────────────────────┘
      ↓
      ├──────────────────┬─────────────────┐
      ↓                  ↓                 ↓
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│  Symbolic    │  │   Entropy    │  │  Optimizer   │
│  Channel     │  │   Channel    │  │  (optional)  │
│              │  │              │  │              │
│ Recursive    │  │ FFT →        │  │ MSE feedback │
│ XOR masking  │  │ Statistical  │  │ loop for     │
│ 4-pass       │  │ chunking     │  │ best passes  │
│ folding      │  │ 16 features  │  │              │
│              │  │              │  │              │
│ Output:      │  │ Output:      │  │ Improves:    │
│ 64-char hex  │  │ 16 floats    │  │ Both channels│
└──────────────┘  └──────────────┘  └──────────────┘
      │                  │                 │
      └──────────┬───────┘                 │
                 ↓                         │
        ┌─────────────────┐                │
        │ Combined Payload│◄───────────────┘
        │ ~96 bytes total │
        └─────────────────┘
                 ↓
        ┌─────────────────┐
        │  Reconstruction │
        │  - Decode both  │
        │  - Merge 50/50  │
        │  - Return 768   │
        └─────────────────┘
```

### Channel Details

**Symbolic Channel (32 bytes compressed):**
- Recursive XOR with pseudo-random mask
- 4-pass folding with bit rotation
- Entropy mixing per pass
- 32-chunk XOR reduction
- Output: 64-character hex string

**Entropy Channel (16 floats):**
- FFT-based frequency analysis
- Statistical chunking (mean, std, max, min)
- 16 compressed features
- Preserves frequency patterns

**Decoder:**
- Expands symbolic fingerprint via tiling
- Expands entropy features via repetition
- Merges both channels with 50/50 weighting
- Returns 768-element normalized vector

---

## 🧪 Self-Optimization

Frackture includes a **decoder feedback optimization** that automatically tunes compression:

```python
from frackture import (
    frackture_preprocess_universal_v2_6,
    optimize_frackture,
    frackture_v3_3_reconstruct
)

# Standard encoding
data = "Important data to compress optimally"
preprocessed = frackture_preprocess_universal_v2_6(data)

# Self-optimizing compression
optimized_payload, mse = optimize_frackture(preprocessed, num_trials=5)

# The optimizer:
# - Tries different symbolic pass counts (2-6)
# - Measures reconstruction MSE for each
# - Returns payload with lowest reconstruction error
# - Never worse than baseline

print(f"Optimized MSE: {mse:.6f}")
reconstructed = frackture_v3_3_reconstruct(optimized_payload)
```

**How it works:**
1. Generates multiple payload candidates with varying symbolic passes
2. Reconstructs each and measures Mean Squared Error (MSE)
3. Returns the payload with minimum MSE
4. **Guarantee**: Never degrades below single-pass baseline

See [TEST_REPORT.md](./TEST_REPORT.md) for optimization verification.

---

## 📚 API Reference

### Core Functions

#### `frackture_preprocess_universal_v2_6(data)`
Converts any input to normalized 768-element vector.

**Parameters:**
- `data`: Any type (str, bytes, dict, list, numpy array, or Python object)

**Returns:**
- `numpy.ndarray`: 768-element float32 array normalized to [0, 1]

**Examples:**
```python
vec1 = frackture_preprocess_universal_v2_6("text")
vec2 = frackture_preprocess_universal_v2_6(b"bytes")
vec3 = frackture_preprocess_universal_v2_6({"key": "value"})
vec4 = frackture_preprocess_universal_v2_6([1, 2, 3, 4])
```

---

#### `frackture_v3_3_safe(input_vector)`
Encodes preprocessed vector into dual-channel payload.

**Parameters:**
- `input_vector`: 768-element numpy array (from preprocessor)

**Returns:**
- `dict`: Contains `symbolic` (str) and `entropy` (list of 16 floats)

**Example:**
```python
payload = frackture_v3_3_safe(preprocessed)
# payload = {
#     "symbolic": "a3f5c8e2...",  # 64-char hex
#     "entropy": [0.234, 0.891, ...]  # 16 floats
# }
```

---

#### `frackture_v3_3_reconstruct(payload)`
Reconstructs approximate vector from payload.

**Parameters:**
- `payload`: Dict with `symbolic` and `entropy` keys

**Returns:**
- `numpy.ndarray`: 768-element reconstructed vector

**Example:**
```python
reconstructed = frackture_v3_3_reconstruct(payload)
# Returns normalized 768-element vector
```

---

#### `optimize_frackture(input_vector, num_trials=5)`
Self-optimizing compression with MSE minimization.

**Parameters:**
- `input_vector`: 768-element numpy array
- `num_trials`: Number of optimization trials (default: 5)

**Returns:**
- `tuple`: (best_payload, best_mse)
  - `best_payload`: Optimized dual-channel payload
  - `best_mse`: Mean squared error of reconstruction

**Example:**
```python
payload, mse = optimize_frackture(preprocessed, num_trials=5)
print(f"Optimization achieved MSE: {mse:.6f}")
```

---

### Encryption Functions

#### `frackture_encrypt_payload(payload, key)`
Encrypts payload with HMAC authentication.

**Parameters:**
- `payload`: Dict (typically from `frackture_v3_3_safe`)
- `key`: String encryption key

**Returns:**
- `dict`: Encrypted payload with signature and metadata

**Example:**
```python
encrypted = frackture_encrypt_payload(payload, "my-secret-key")
# Returns: {
#     "data": {...},
#     "signature": "abc123...",
#     "metadata": {"key_id": "12345678"}
# }
```

---

#### `frackture_decrypt_payload(encrypted_payload, key)`
Decrypts and verifies payload.

**Parameters:**
- `encrypted_payload`: Dict from `frackture_encrypt_payload`
- `key`: String decryption key

**Returns:**
- `dict`: Original payload

**Raises:**
- `ValueError`: If key is wrong or payload is tampered

**Example:**
```python
try:
    decrypted = frackture_decrypt_payload(encrypted, "my-secret-key")
except ValueError as e:
    print(f"Decryption failed: {e}")
```

---

### Hashing Functions

#### `frackture_deterministic_hash(data, salt="")`
Generates deterministic SHA256 hash.

**Parameters:**
- `data`: Any data (converted to string)
- `salt`: Optional salt string (default: "")

**Returns:**
- `str`: 64-character hex SHA256 hash

**Example:**
```python
hash1 = frackture_deterministic_hash("data")
hash2 = frackture_deterministic_hash("data", salt="namespace")
```

---

## 🔒 Security Properties

### Threat Model

Frackture is designed for:
- ✅ **Data fingerprinting** with collision resistance
- ✅ **Integrity checking** with entropy awareness
- ✅ **Authenticated encryption** via HMAC
- ✅ **Tamper detection** through signature verification
- ✅ **Key management** with key ID metadata

Frackture is **NOT designed for:**
- ❌ Cryptographic security (use AES, ChaCha20 instead)
- ❌ Long-term secret storage (use proper encryption)
- ❌ Password hashing (use Argon2, bcrypt instead)

### Security Features

**HMAC Authentication:**
- Uses HMAC-SHA256 for payload authentication
- Constant-time comparison prevents timing attacks
- Key ID metadata enables key rotation

**Tamper Detection:**
```python
encrypted = frackture_encrypt_payload(payload, "key")

# Tamper with data
encrypted["data"]["symbolic"] = "tampered"

# Verification fails
try:
    frackture_decrypt_payload(encrypted, "key")
except ValueError:
    print("Tampering detected!")  # This will execute
```

**Collision Resistance:**
- Symbolic fingerprints use 64-character hex (32 bytes)
- Entropy signatures add 16 independent features
- Combined ~96 bytes provide strong uniqueness

See [docs/SECURITY.md](./docs/SECURITY.md) for detailed security analysis.

---

## 🏃 Running Tests

Comprehensive test suite with 100+ tests covering all functionality:

```bash
# Run all tests
python -m pytest tests/ -v

# Run specific test categories
python -m pytest tests/test_encryption.py -v
python -m pytest tests/test_hashing.py -v
python -m pytest tests/test_optimization.py -v

# Run with coverage
python -m pytest tests/ --cov="frackture (2)" --cov-report=term-missing

# Quick smoke test
python run_tests.py
```

**Test coverage:**
- ✅ Preprocessing edge cases (empty, None, unicode, special types)
- ✅ Round-trip compression/decompression
- ✅ Encryption security (wrong keys, tampering, metadata)
- ✅ Hashing determinism and collision sampling
- ✅ Failure path handling
- ✅ Optimization properties (MSE improvement guarantee)
- ✅ Large payload handling (100KB-1MB+)
- ✅ Adversarial inputs

See [TEST_REPORT.md](./TEST_REPORT.md) for detailed test results.

---

## 📊 Benchmarks

Compare Frackture against gzip and brotli using **15+ real-world datasets** across 7 size tiers:

```bash
cd benchmarks

# Run comprehensive benchmarks (default: real datasets)
python benchmark_frackture.py

# Size-specific testing
python benchmark_frackture.py --small-only   # 100KB datasets
python benchmark_frackture.py --large-only   # 1MB datasets
python benchmark_frackture.py --extreme      # 100MB+ datasets (slow)

# Advanced options
python benchmark_frackture.py --verify-only  # Skip gzip/brotli, focus on verification
python benchmark_frackture.py --detailed     # Enable diagnostic output
python benchmark_frackture.py --gzip-level 9 --brotli-quality 11  # Max compression
```

### Real Dataset Repository

**15+ production-ready datasets** covering all major content types:

| Category | Datasets | Example Use Cases |
|----------|----------|-------------------|
| 📄 **Text** | plain text, logs, JSON, CSV | Documents, API responses, structured data |
| 🖼️ **Binary** | PNG, JPEG, PDF, GIF | Images, documents, animations |
| 💾 **Structured** | SQLite, pickle, MessagePack | Databases, serialized objects |
| 🔧 **Code** | JavaScript, Python, minified | Source code, scripts, bundles |
| 🔀 **Mixed** | multi-format payloads | Real-world combined data |

**Size tiers**: tiny (50 B) → small (1 KB) → medium (100 KB) → large (1 MB) → xlarge (10 MB) → xxlarge (100 MB) → huge (1 GB, optional)

Explore datasets:
```bash
cd benchmarks
python dataset_cli.py list         # List all 15+ datasets
python dataset_cli.py categories   # Group by category
python dataset_cli.py info text_plain  # Detailed dataset info
python dataset_cli.py test         # Validate all datasets
```

### Sample Results

**1MB Text File:**

| Method | Compressed Size | Ratio | Encode | Decode | Memory |
|--------|----------------|-------|--------|--------|--------|
| **Frackture** | **96 bytes** | **10,923×** | 163 MB/s | 4,771 MB/s | 2.5 MB |
| Gzip (level 6) | 151 KB | 6.9× | 24 MB/s | 326 MB/s | 3.2 MB |
| Brotli (quality 6) | 125 KB | 8.4× | 8 MB/s | 312 MB/s | 4.1 MB |

**100MB Mixed Payload:**

| Method | Compressed Size | Ratio | Encode Time | Decode Time |
|--------|----------------|-------|-------------|-------------|
| **Frackture** | **96 bytes** | **~1,000,000×** | ~5s | ~0.2s |
| Gzip | ~35 MB | ~2.8× | ~50s | ~5s |
| Brotli | ~28 MB | ~3.5× | ~180s | ~4s |

### Comprehensive Metrics

Beyond compression ratios, the suite measures:

- **Payload Sizing**: Validates fixed 96-byte output (symbolic 32B + entropy 128B serialized)
- **MSE (Reconstruction Quality)**: Tracks lossy compression quality (typical: 0.0001-0.01)
- **Optimization Impact**: Self-optimization improves MSE by 5-30%
- **Determinism**: Ensures same input → same fingerprint (critical for deduplication)
- **Fault Injection**: Tests corruption detection (4 robustness tests)

### Key Findings

**Frackture excels at:**
- ✅ **Large file fingerprinting** (1 MB+): Extreme compression ratios (10,000×+)
- ✅ **Fixed-size signatures**: Predictable storage (always ~96 bytes)
- ✅ **Fast decode**: 3-10× faster than gzip/brotli for read-heavy workloads
- ✅ **Consistent performance**: Works equally well on text, binary, random noise
- ✅ **ML embedding compression**: Perfect for 768-dim vectors (97% size reduction)

**Use traditional compression for:**
- ❌ Small files (<1 KB): Frackture may expand to 96 bytes
- ❌ Lossless requirements: Frackture is lossy by design
- ❌ Network transmission: Protocols expect lossless compression
- ❌ Archival storage: Legal/compliance may require exact reconstruction

### Documentation

- **[docs/BENCHMARKING.md](./docs/BENCHMARKING.md)** - Complete methodology, metrics, and interpretation guide
- **[benchmarks/README.md](./benchmarks/README.md)** - Running benchmarks, CLI options, troubleshooting
- **[benchmarks/datasets/README.md](./benchmarks/datasets/README.md)** - Dataset details and scaling
- **[BENCHMARK_SUITE_SUMMARY.md](./BENCHMARK_SUITE_SUMMARY.md)** - Implementation summary and key findings

---

## 📖 Additional Documentation

Explore detailed guides in the `docs/` directory:

- **[docs/ARCHITECTURE.md](./docs/ARCHITECTURE.md)** - Deep dive into dual-channel design
- **[docs/BENCHMARKING.md](./docs/BENCHMARKING.md)** - Complete benchmarking methodology and interpretation guide
- **[docs/SECURITY.md](./docs/SECURITY.md)** - Security properties and threat model
- **[docs/EXAMPLES.md](./docs/EXAMPLES.md)** - Copy-paste examples for all workflows
- **[docs/FAQ.md](./docs/FAQ.md)** - Common questions and troubleshooting

---

## 🎯 Use Cases

### ✅ Ideal For:

1. **Identity-Preserving Hashes**
   - Fixed-size fingerprints for any data size
   - Collision-resistant signatures
   - Fast integrity checking

2. **Data Deduplication**
   - Compare fingerprints instead of full data
   - O(1) size comparisons
   - Similarity detection via entropy channel

3. **Embedding Compression**
   - Compress ML model embeddings
   - Fixed-size representations for databases
   - Fast similarity search

4. **Secure Data Transmission**
   - Encrypt payloads with HMAC authentication
   - Tamper detection included
   - Lightweight secure transport

5. **AI/ML Pipelines**
   - Compact data representations
   - Fast encode/decode for real-time inference
   - Consistent vector lengths

### ❌ Not Ideal For:

1. **Lossless Compression** - Use gzip, brotli, or zstd
2. **Password Hashing** - Use Argon2 or bcrypt
3. **Long-Term Archival** - Use lossless compression
4. **General File Compression** - Use traditional algorithms

---

## 🧬 Advanced Usage

### Custom Optimization Trials

```python
# More trials = better optimization (but slower)
payload, mse = optimize_frackture(preprocessed, num_trials=10)
```

### Batch Processing

```python
# Process multiple inputs efficiently
import numpy as np

inputs = ["data1", "data2", "data3"]
payloads = []

for data in inputs:
    preprocessed = frackture_preprocess_universal_v2_6(data)
    payload = frackture_v3_3_safe(preprocessed)
    payloads.append(payload)

# Store or transmit payloads (~96 bytes each)
```

### Similarity Detection

```python
# Compare entropy channels for similarity
data1 = "The quick brown fox"
data2 = "The quick brown dog"

prep1 = frackture_preprocess_universal_v2_6(data1)
prep2 = frackture_preprocess_universal_v2_6(data2)

payload1 = frackture_v3_3_safe(prep1)
payload2 = frackture_v3_3_safe(prep2)

# Compare entropy signatures
import numpy as np
entropy_similarity = np.dot(payload1['entropy'], payload2['entropy'])
print(f"Similarity: {entropy_similarity}")
```

---

## 🤖 Author

**Built by [@GoryGrey](https://x.com/GoryGrey)** — degen dev with a compression disorder.

**Attribution:**  
*"Frackture: Recursive Compression & Symbolic Encoding, by Gregory Betti (f(∞))"*

Feel free to fork, remix, or break reality with it.

---

## 📄 License

MIT License with attribution requirement — see [LICENSE](./LICENSE) for details.

**TL;DR:** Do what you want, just cite the origin and don't sue me.

---

## 🔗 Links

- **PyPI Package:** [https://pypi.org/project/frackture/](https://pypi.org/project/frackture/)
- **GitHub:** [Link to repository]
- **Twitter:** [@GoryGrey](https://x.com/GoryGrey)

---

## 🚀 Quick Start Examples

### 1. Fingerprint Generation

```python
from frackture import frackture_preprocess_universal_v2_6, frackture_v3_3_safe

data = "Your important data"
preprocessed = frackture_preprocess_universal_v2_6(data)
fingerprint = frackture_v3_3_safe(preprocessed)

print(f"Fingerprint (symbolic): {fingerprint['symbolic'][:32]}...")
print(f"Fingerprint size: ~96 bytes")
```

### 2. Secure Storage

```python
from frackture import *

# Prepare data
data = {"user": "alice", "balance": 1000}
preprocessed = frackture_preprocess_universal_v2_6(data)
payload = frackture_v3_3_safe(preprocessed)

# Encrypt for storage
key = "storage-key-2024"
encrypted = frackture_encrypt_payload(payload, key)

# Later: retrieve and decrypt
decrypted = frackture_decrypt_payload(encrypted, key)
reconstructed = frackture_v3_3_reconstruct(decrypted)
```

### 3. Hash-Based Integrity

```python
from frackture import frackture_deterministic_hash

# Original data
data = "Critical system configuration"
original_hash = frackture_deterministic_hash(data)

# Later: verify integrity
current_hash = frackture_deterministic_hash(data)
if original_hash == current_hash:
    print("Data integrity verified!")
else:
    print("Data has been modified!")
```

---

## 🎓 Learn More

Ready to dive deeper? Check out:

1. **[docs/ARCHITECTURE.md](./docs/ARCHITECTURE.md)** - Understand the dual-channel design
2. **[docs/EXAMPLES.md](./docs/EXAMPLES.md)** - More copy-paste examples
3. **[TEST_REPORT.md](./TEST_REPORT.md)** - Verification results
4. **[BENCHMARK_SUITE_SUMMARY.md](./BENCHMARK_SUITE_SUMMARY.md)** - Performance data

**Questions?** See [docs/FAQ.md](./docs/FAQ.md) or open an issue!

---

<div align="center">

**🧠 Frackture: Compress. Encrypt. Hash. Optimize. 🚀**

*Built with recursive logic and entropy signatures*

</div>
