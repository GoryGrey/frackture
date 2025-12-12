# 🧠 Frackture

[![PyPI version](https://img.shields.io/pypi/v/frackture.svg)](https://pypi.org/project/frackture/)
[![Downloads](https://img.shields.io/pypi/dm/frackture.svg)](https://pypi.org/project/frackture/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE)

Frackture is a **symbolic compression engine** using recursive logic and entropy signatures to compress data while preserving identity and structure.

> Built to push boundaries in compression, data fingerprinting, and self-optimizing logic.

---

## 🚀 Installation

```bash
pip install frackture
```

### Development Installation

```bash
# Clone the repository
git clone https://github.com/GoryGrey/frackture.git
cd frackture

# Install in editable mode with dev dependencies
pip install -e ".[dev]"

# Or using make
make install-dev
```

---

## 🧪 Basic Usage

```python
from frackture import (
    frackture_preprocess_universal_v2_6,
    frackture_v3_3_safe,
    frackture_v3_3_reconstruct
)

# Compress data
data = b"Hello world. This is a test of the emergency broadcast system."
preprocessed = frackture_preprocess_universal_v2_6(data)
payload = frackture_v3_3_safe(preprocessed)

# Decompress
reconstructed = frackture_v3_3_reconstruct(payload)
```

### CLI Usage

```bash
# Compress data
echo "hello world" | frackture compress > compressed.json

# Generate hash
frackture hash -i myfile.txt

# Optimize compression
frackture optimize -i data.bin --trials 10
```

---

## 🧬 Features

- 🌀 Universal data preprocessing  
- 🧠 Symbolic fingerprinting (identity-preserving logic signatures)  
- 📉 Entropy channel encoding with fixed-size output (~96 bytes)  
- ♻️ Self-optimization with decoder feedback  
- 🔐 Structure-preserving compression across formats (text, binary, etc)

---

## 📚 Use Cases

- Secure identity-preserving hashes  
- Embedding compression for LLMs or AI pipelines  
- Data integrity checking with entropy-aware patterns  
- Experimental symbolic computing

---

## 🛠 Requirements

- Python 3.8+
- Dependencies: `numpy`, `scipy`, `scikit-learn`

(Handled automatically during install)

---

## 📊 Benchmarks

Want to see how Frackture compares to gzip and brotli? Check out the comprehensive benchmark suite:

```bash
cd benchmarks
python benchmark_frackture.py
```

The benchmark suite tests compression ratio, throughput, hashing latency, and memory usage across various datasets (text, JSON, binary, random noise, etc.).

See [benchmarks/README.md](benchmarks/README.md) for detailed instructions and how to interpret results.

**Key highlights:**
- Fixed ~96-byte output regardless of input size
- 250-500x compression ratios for fingerprinting use cases
- Fast hashing for integrity checks
- Consistent memory footprint

---

## 🤖 Author

Built by [@GoryGrey](https://x.com/GoryGrey) — degen dev with a compression disorder.  
Feel free to fork, remix, or break reality with it.

---

## 📄 License

MIT — do what you want, just don’t sue me.

---

## 🔗 PyPI

[https://pypi.org/project/frackture/](https://pypi.org/project/frackture/)

## 🛠 Development

### Running Tests

```bash
# Run all tests
make test

# Run with coverage
make test-cov

# Run linting
make lint

# Format code
make format
```

### Building and Publishing

See [RELEASE.md](RELEASE.md) for detailed instructions on creating tagged releases and publishing to PyPI.

---

## 🔗 Links

- **GitHub**: [https://github.com/GoryGrey/frackture](https://github.com/GoryGrey/frackture)
- **Issues**: [https://github.com/GoryGrey/frackture/issues](https://github.com/GoryGrey/frackture/issues)
