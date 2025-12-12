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

---

## 🧪 Basic Usage

```python
from frackture import compress, decompress

data = b"Hello world. This is a test of the emergency broadcast system."
compressed = compress(data)
original = decompress(compressed)

print(original)  # should match original input
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
