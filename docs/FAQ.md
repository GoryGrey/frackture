# ❓ Frackture FAQ

Frequently asked questions about Frackture's functionality, use cases, and implementation.

---

## Table of Contents

- [General Questions](#general-questions)
- [Technical Questions](#technical-questions)
- [Use Case Questions](#use-case-questions)
- [Performance Questions](#performance-questions)
- [Security Questions](#security-questions)
- [Troubleshooting](#troubleshooting)
- [Comparison Questions](#comparison-questions)

---

## General Questions

### What is Frackture?

Frackture is a symbolic compression and fingerprinting library that creates fixed-size (~96 byte) representations of any data. It combines:
- **Symbolic fingerprinting** for identity preservation
- **Entropy signatures** for frequency pattern capture
- **HMAC encryption** for integrity protection

Unlike traditional compression (gzip, brotli), Frackture produces fixed-size output ideal for fingerprinting, hashing, and similarity detection.

### Why "Frackture"?

The name reflects the core concept: **fractional capture** of data's essence through recursive **structure breaking** (fracking) and reassembly. The dual-channel architecture fractures data into complementary representations.

### Is Frackture production-ready?

**Yes**, for its intended use cases:
- ✅ Data fingerprinting
- ✅ Integrity checking
- ✅ Similarity detection
- ✅ Embedding compression

**Considerations:**
- Comprehensive test suite (100+ tests)
- Benchmarked against industry standards
- Active development (check GitHub for updates)
- MIT licensed

### How is Frackture different from traditional compression?

| Aspect | Frackture | Traditional (gzip/brotli) |
|--------|-----------|---------------------------|
| **Output Size** | Fixed ~96 bytes | Variable (scales with input) |
| **Type** | Lossy fingerprinting | Lossless compression |
| **Speed** | Very fast (160+ MB/s) | Moderate (25-90 MB/s) |
| **Use Case** | Identity, similarity | Archival, transmission |
| **Reconstruction** | Approximate | Exact |

### What Python versions are supported?

**Python 3.8+** is required.

**Dependencies:**
- numpy (array operations)
- scipy (FFT)
- scikit-learn (statistical processing)

All dependencies install automatically via pip.

---

## Technical Questions

### How does the dual-channel architecture work?

Frackture splits encoding into two parallel channels:

**Symbolic Channel:**
- Recursive XOR operations with masking
- 4-pass transformation with feedback
- Produces 64-character hex fingerprint (32 bytes)
- Preserves data **identity** and structure

**Entropy Channel:**
- FFT-based frequency analysis
- Statistical chunking (mean, std, max, min)
- Produces 16 float features (~128 bytes serialized)
- Captures frequency **patterns**

Both channels are decoded and merged (50/50) for reconstruction.

See [ARCHITECTURE.md](./ARCHITECTURE.md) for detailed explanation.

### Why 768 elements in the preprocessed vector?

**Reasons:**
1. **Compatibility**: Matches common embedding dimensions (BERT-768, GPT-2-768)
2. **Divisibility**: 768 = 2^8 × 3, divisible by many factors (2, 3, 4, 6, 8, 12, 16, 24, 32, ...)
3. **Balance**: Large enough to preserve information, small enough to be efficient
4. **Processing**: Enables clean 16-chunk and 32-chunk divisions

### What's the compression ratio?

**Not applicable in traditional sense!** Frackture produces fixed-size output.

**Better metric: Size reduction**
```
Input: 1 KB    → Output: 96 bytes → 10.6x reduction
Input: 100 KB  → Output: 96 bytes → 1,066x reduction
Input: 1 MB    → Output: 96 bytes → 10,923x reduction
Input: 1 GB    → Output: 96 bytes → 10,923,076x reduction
```

**The larger your input, the more dramatic the "compression"** — but remember, this is lossy fingerprinting, not lossless compression.

### Can I reconstruct the exact original data?

**No.** Frackture is **lossy compression** (fingerprinting).

**What you can reconstruct:**
- Approximate 768-element vector representation
- Similar frequency patterns
- Structural characteristics

**What you cannot reconstruct:**
- Exact original bytes
- Text content
- Specific values

**Use case:** Similarity detection, not archival.

### How accurate is reconstruction?

**Measured by Mean Squared Error (MSE):**
- Typical MSE: **0.01 - 0.15**
- Lower is better
- MSE measures difference between original and reconstructed vectors

**Factors affecting MSE:**
1. Input complexity (random data → higher MSE)
2. Optimization passes (more passes → lower MSE)
3. Data type (repetitive patterns → lower MSE)

**Use `optimize_frackture()`** to minimize MSE through self-optimization.

### What's the overhead of JSON serialization?

**Payload components:**
- Symbolic: 64 characters (32 bytes as hex)
- Entropy: 16 floats (64 bytes as 8-byte floats, or 128 bytes in JSON)
- JSON structure: ~30-50 bytes (keys, brackets, quotes)

**Total serialized size: ~200-250 bytes** depending on entropy float precision.

**Wire format options:**
```python
# JSON (human-readable, ~250 bytes)
import json
json.dumps(payload)

# MessagePack (binary, ~120 bytes)
import msgpack
msgpack.packb(payload)

# Protocol Buffers (most compact, ~100 bytes)
# Requires schema definition
```

### Can I change the output size?

**Currently: No.** The fixed 96-byte payload is core to the design.

**Future possibilities:**
- Variable entropy feature count (8/16/32/64)
- Configurable symbolic passes
- Multi-scale fingerprints

**Workaround for smaller output:**
```python
# Use only symbolic channel (32 bytes)
payload = frackture_v3_3_safe(preprocessed)
compact_fingerprint = payload['symbolic']  # 64-char hex = 32 bytes

# Or hash the full payload (even more compact)
import hashlib
ultra_compact = hashlib.sha256(payload['symbolic'].encode()).hexdigest()[:16]
```

---

## Use Case Questions

### Should I use Frackture for general file compression?

**No.** Use traditional compression (gzip, brotli, zstd) for:
- Archival storage
- File transmission
- Lossless compression needs
- General-purpose compression

**Use Frackture for:**
- Fixed-size fingerprints
- Data deduplication
- Similarity detection
- Identity-preserving hashes

### Can I use Frackture for password hashing?

**NO!** Frackture is **too fast** for password hashing.

**Problem:**
- Attackers can test millions of passwords per second
- No memory-hardness or time-stretch

**Use instead:**
- Argon2 (best, winner of Password Hashing Competition)
- bcrypt (good, widely supported)
- scrypt (good, memory-hard)

### Is Frackture suitable for deduplication?

**Yes!** Frackture excels at deduplication.

**How:**
```python
from frackture import frackture_preprocess_universal_v2_6, frackture_v3_3_safe

def get_fingerprint(data):
    prep = frackture_preprocess_universal_v2_6(data)
    payload = frackture_v3_3_safe(prep)
    return payload['symbolic']

# Store fingerprints in set
fingerprints = set()

for data in data_stream:
    fp = get_fingerprint(data)
    if fp in fingerprints:
        print("Duplicate detected!")
    else:
        fingerprints.add(fp)
        store_data(data)
```

**Benefits:**
- O(1) fingerprint comparison
- Fixed storage per item (32 bytes)
- Fast processing

### Can I use Frackture for similarity search?

**Yes!** Use entropy channels for similarity.

```python
import numpy as np

def similarity(data1, data2):
    prep1 = frackture_preprocess_universal_v2_6(data1)
    prep2 = frackture_preprocess_universal_v2_6(data2)
    
    payload1 = frackture_v3_3_safe(prep1)
    payload2 = frackture_v3_3_safe(prep2)
    
    # Cosine similarity on entropy vectors
    e1 = np.array(payload1['entropy'])
    e2 = np.array(payload2['entropy'])
    
    return np.dot(e1, e2) / (np.linalg.norm(e1) * np.linalg.norm(e2))
```

**Use cases:**
- Document similarity
- Image fingerprint comparison
- Audio pattern matching
- Anomaly detection

### Should I use Frackture for encryption?

**Not as primary encryption!**

**What Frackture provides:**
- HMAC authentication (integrity + authenticity)
- Tamper detection
- Key verification

**What Frackture doesn't provide:**
- Confidentiality (payload data is visible)
- Forward secrecy
- Key exchange

**Best practice: Combine with real encryption**
```python
from cryptography.fernet import Fernet

# 1. Compress with Frackture
payload = frackture_v3_3_safe(preprocessed)

# 2. Encrypt with real encryption
fernet_key = Fernet.generate_key()
fernet = Fernet(fernet_key)
encrypted = fernet.encrypt(json.dumps(payload).encode())

# 3. Authenticate with Frackture
authenticated = frackture_encrypt_payload({'encrypted': encrypted.decode()}, hmac_key)
```

---

## Performance Questions

### How fast is Frackture?

**Benchmarked speeds (1MB input):**
- Encoding: **163 MB/s**
- Decoding: **4,771 MB/s**
- Hashing: **~1-2 µs per hash**

**Comparison:**
- gzip: 24 MB/s encode, 326 MB/s decode
- brotli: 8 MB/s encode, 312 MB/s decode

Frackture is **7x faster encoding**, **15x faster decoding** for large files.

### Does Frackture scale to large inputs?

**Yes**, but with nuances:

**Preprocessing time:** Scales linearly with input size
```
100 KB  → ~5 ms
1 MB    → ~50 ms
10 MB   → ~500 ms
100 MB  → ~5 sec
```

**Encoding time:** Constant (always processes 768-element vector)
```
Any input → ~1-2 ms
```

**Memory:** Constant (~3 KB for 768-float vector)

**Best performance:**
- Large inputs (>1 KB) - extreme compression ratios
- Batch processing - amortize preprocessing cost
- Repeated operations - cache preprocessed vectors

### Can I parallelize Frackture?

**Yes!** Frackture operations are embarrassingly parallel.

```python
from multiprocessing import Pool
from frackture import frackture_preprocess_universal_v2_6, frackture_v3_3_safe

def process_item(data):
    prep = frackture_preprocess_universal_v2_6(data)
    return frackture_v3_3_safe(prep)

# Process in parallel
with Pool(processes=8) as pool:
    results = pool.map(process_item, large_dataset)
```

**Speedup:** Near-linear with CPU cores (8 cores ≈ 8x faster)

### What's the memory footprint?

**Per operation:**
- Input buffer: Variable (depends on input)
- Preprocessed vector: **3 KB** (768 × 4 bytes)
- FFT scratch space: **~6 KB**
- Output payload: **~0.25 KB**

**Total per operation: ~10 KB**

**Batch processing:**
```
1,000 items × 10 KB = ~10 MB
10,000 items × 10 KB = ~100 MB
```

Very memory-efficient compared to traditional compression (which scales with input size).

### How do I optimize for speed?

**Tips:**

1. **Cache preprocessed vectors** if processing same data multiple times
```python
cache = {}
prep = cache.get(data_id) or frackture_preprocess_universal_v2_6(data)
```

2. **Skip optimization** unless quality is critical
```python
# Fast
payload = frackture_v3_3_safe(preprocessed)

# Slower but better quality
payload, mse = optimize_frackture(preprocessed, num_trials=5)
```

3. **Use batch processing** to amortize overhead
```python
payloads = [process(data) for data in batch]
```

4. **Parallelize** for large datasets
```python
with Pool() as pool:
    results = pool.map(process, dataset)
```

---

## Security Questions

### Is Frackture cryptographically secure?

**Partially.**

**Secure aspects:**
- ✅ HMAC-SHA256 authentication (industry standard)
- ✅ Constant-time signature comparison (timing-attack resistant)
- ✅ Collision-resistant fingerprints (256-bit symbolic hash)

**Not secure aspects:**
- ❌ No data encryption (payload visible)
- ❌ Not suitable for password hashing (too fast)
- ❌ No forward secrecy
- ❌ Not quantum-resistant (uses SHA-256)

**Verdict:** Good for integrity and authentication, **not** for confidentiality.

See [SECURITY.md](./SECURITY.md) for detailed analysis.

### Can attackers tamper with encrypted payloads?

**No.** HMAC verification detects any tampering.

```python
encrypted = frackture_encrypt_payload(payload, key)

# Attacker modifies data
encrypted['data']['symbolic'] = "TAMPERED"

# Decryption fails
try:
    frackture_decrypt_payload(encrypted, key)
except ValueError:
    print("Tampering detected!")  # This executes
```

**Protection:** Any modification to `data` invalidates the HMAC signature.

### What happens if I lose my encryption key?

**You cannot decrypt payloads** encrypted with that key.

**There is no key recovery mechanism.**

**Best practices:**
- Store keys securely (KMS, key vault)
- Implement key rotation
- Maintain key backups in secure location
- Document key management procedures

### Are collisions possible?

**Theoretically yes, practically no.**

**Collision probability:**
- Symbolic fingerprint: 32 bytes (256 bits)
- Birthday bound: 2^128 attempts for 50% collision
- Estimated time at 1 billion attempts/second: **10 billion years**

**Verdict:** Collisions are computationally infeasible.

**Additional protection:** Entropy channel provides secondary collision resistance.

### Should I rotate encryption keys?

**Yes!** Regular key rotation is security best practice.

**Recommended interval:** 90 days

**Implementation:**
```python
class KeyManager:
    def rotate_key(self):
        new_key = generate_random_key()
        self.current_key = new_key
        self.keys[new_key_id] = new_key
        return new_key
    
    def re_encrypt_all(self, old_key, new_key):
        for payload_id in self.get_all_payloads():
            encrypted = self.load(payload_id)
            decrypted = frackture_decrypt_payload(encrypted, old_key)
            re_encrypted = frackture_encrypt_payload(decrypted, new_key)
            self.save(payload_id, re_encrypted)
```

---

## Troubleshooting

### ImportError: No module named 'frackture'

**Problem:** Module filename has space: `frackture (2).py`

**Solutions:**

**Option 1:** Rename file
```bash
mv "frackture (2).py" frackture.py
```

**Option 2:** Use importlib
```python
import importlib.util

spec = importlib.util.spec_from_file_location("frackture", "frackture (2).py")
frackture = importlib.util.module_from_spec(spec)
spec.loader.exec_module(frackture)

# Now use it
preprocessed = frackture.frackture_preprocess_universal_v2_6(data)
```

### ValueError: Invalid key or corrupted payload

**Causes:**
1. Wrong encryption key
2. Payload modified/corrupted
3. Key ID mismatch
4. Network transmission error

**Debugging:**
```python
try:
    decrypted = frackture_decrypt_payload(encrypted, key)
except ValueError as e:
    print(f"Error: {e}")
    
    # Check key ID
    provided_key_id = hashlib.sha256(key.encode()).hexdigest()[:8]
    expected_key_id = encrypted['metadata']['key_id']
    
    if provided_key_id != expected_key_id:
        print("Wrong key! Key IDs don't match.")
    else:
        print("Payload may be corrupted.")
```

### MSE too high after reconstruction

**Causes:**
1. Input is very random/complex
2. Using default 4 symbolic passes (not optimized)
3. Input size mismatch with 768 elements

**Solutions:**

**Use optimization:**
```python
payload, mse = optimize_frackture(preprocessed, num_trials=10)
print(f"Optimized MSE: {mse}")
```

**Check input characteristics:**
```python
import numpy as np

# Check entropy
entropy = -np.sum(p * np.log2(p + 1e-10) 
                  for p in np.histogram(data, bins=256, density=True)[0] 
                  if p > 0)
print(f"Input entropy: {entropy:.2f} bits")

# High entropy (>7.5) = harder to compress
```

### Memory Error with large datasets

**Problem:** Processing too many items at once

**Solution: Stream processing**
```python
def process_stream(data_generator, output_file):
    with open(output_file, 'w') as f:
        for data in data_generator:
            payload = frackture_v3_3_safe(
                frackture_preprocess_universal_v2_6(data)
            )
            f.write(json.dumps(payload) + '\n')
            f.flush()  # Write immediately
```

### Slow performance on small inputs

**Expected behavior:** Frackture is optimized for inputs >1 KB.

**For small inputs (<100 bytes):**
- Preprocessing overhead dominates
- Fixed output (~96 bytes) may be larger than input
- Traditional compression may be faster

**Recommendation:** Use traditional compression for small files.

### Tests failing with module import errors

**Problem:** Test imports can't find `frackture (2).py`

**Solution:** Tests already include import helpers

```python
# In test files
import sys
import os
import importlib.util

module_path = os.path.join(os.path.dirname(__file__), '..', 'frackture (2).py')
spec = importlib.util.spec_from_file_location("frackture_2", module_path)
frackture_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(frackture_module)
```

Run tests with:
```bash
python -m pytest tests/ -v
```

---

## Comparison Questions

### Frackture vs. perceptual hashing (pHash)?

| Feature | Frackture | pHash |
|---------|-----------|-------|
| **Input** | Any data type | Images/audio |
| **Output** | 96 bytes | 8-32 bytes |
| **Speed** | Very fast | Fast |
| **Similarity** | Entropy channel | Hamming distance |
| **Use Case** | General fingerprinting | Media deduplication |

**Verdict:** Frackture is more general-purpose; pHash is specialized for multimedia.

### Frackture vs. MinHash?

| Feature | Frackture | MinHash |
|---------|-----------|---------|
| **Method** | Symbolic + entropy | Set similarity |
| **Best For** | Structured data | Text documents |
| **Similarity** | Cosine on entropy | Jaccard estimate |
| **Speed** | Very fast | Fast |

**Verdict:** MinHash for text/set similarity; Frackture for broader data types.

### Frackture vs. Bloom filters?

| Feature | Frackture | Bloom Filter |
|---------|-----------|--------------|
| **Purpose** | Fingerprinting | Membership testing |
| **Output** | 96 bytes | Variable (KB+) |
| **False Positives** | Possible (collisions) | Tunable |
| **Exact Match** | Yes | No (probabilistic) |

**Verdict:** Different use cases. Bloom filters for membership tests; Frackture for identity/similarity.

### Frackture vs. traditional hashing (SHA-256)?

| Feature | Frackture | SHA-256 |
|---------|-----------|---------|
| **Output Size** | 96 bytes (dual channel) | 32 bytes |
| **Speed** | Very fast | Very fast |
| **Collision Resistance** | Very strong | Very strong |
| **Similarity Detection** | Yes (entropy channel) | No |
| **Reconstruction** | Approximate | No |

**Verdict:** SHA-256 for pure identity hashing; Frackture for identity + similarity + reconstruction.

---

## Advanced Questions

### Can I train a neural network on Frackture payloads?

**Yes!** Frackture payloads make excellent ML features.

**Approach:**
```python
# Extract features
features = []
for data in dataset:
    prep = frackture_preprocess_universal_v2_6(data)
    payload = frackture_v3_3_safe(prep)
    
    # Use entropy channel as features
    features.append(payload['entropy'])

X = np.array(features)  # Shape: (n_samples, 16)

# Train model
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(X, y)
```

**Benefits:**
- Fixed-size features (16 floats)
- Captures frequency patterns
- Fast to compute

### Can I customize the symbolic pass count?

**Yes,** but requires modifying the source:

```python
# In frackture (2).py
def frackture_symbolic_fingerprint_f_infinity(input_vector, passes=4):
    # Change passes parameter default value
    ...

# Usage
from frackture import symbolic_channel_encode

# Custom pass count
def custom_encode(input_vector, passes=8):
    from frackture import frackture_symbolic_fingerprint_f_infinity
    return frackture_symbolic_fingerprint_f_infinity(input_vector, passes)
```

**Trade-offs:**
- More passes = better mixing, higher MSE initially
- `optimize_frackture` finds best pass count automatically

### Is there a C/Rust implementation for speed?

**Not yet.** Current implementation is pure Python with NumPy/SciPy.

**Performance is already good** due to NumPy's C-optimized operations.

**Future possibilities:**
- Cython compilation
- Rust rewrite for embedded systems
- CUDA/OpenCL for GPU acceleration

**Contribution welcome!**

### Can I use Frackture in production systems?

**Yes**, with considerations:

✅ **Good for:**
- Fingerprinting services
- Deduplication systems
- Similarity search
- Integrity checking

⚠️ **Consider:**
- Test thoroughly for your use case
- Monitor performance in production
- Implement proper error handling
- Plan key management strategy

❌ **Not for:**
- Primary encryption (use AES/ChaCha20)
- Password hashing (use Argon2/bcrypt)
- Regulatory compliance (FIPS, HIPAA) without additional controls

---

## Getting Help

### Where can I report bugs?

**GitHub Issues:** [Link to repository issues]

**Include:**
- Python version
- Frackture version
- Minimal reproducible example
- Error messages/stack traces

### How do I contribute?

**Contributions welcome!**

**Areas for contribution:**
- Performance improvements
- Additional test cases
- Documentation improvements
- Bug fixes
- Feature requests

**Process:**
1. Fork repository
2. Create feature branch
3. Add tests for new functionality
4. Submit pull request

### Where can I ask questions?

**Options:**
1. GitHub Discussions
2. Stack Overflow (tag: `frackture`)
3. Twitter: [@GoryGrey](https://x.com/GoryGrey)

### Is there a Discord/Slack community?

**Not yet.** As the community grows, we may establish:
- Discord server
- Slack workspace
- Mailing list

**For now:** Use GitHub Discussions for community interaction.

---

## Additional Resources

- **[README.md](../README.md)** - Quick start and overview
- **[ARCHITECTURE.md](./ARCHITECTURE.md)** - Technical deep dive
- **[SECURITY.md](./SECURITY.md)** - Security analysis
- **[EXAMPLES.md](./EXAMPLES.md)** - Copy-paste code examples
- **[TEST_REPORT.md](../TEST_REPORT.md)** - Test coverage
- **[BENCHMARK_SUITE_SUMMARY.md](../BENCHMARK_SUITE_SUMMARY.md)** - Performance data

---

**Didn't find your question?** Open an issue on GitHub or reach out on Twitter!
