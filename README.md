# 🧠 Frackture

[![PyPI version](https://img.shields.io/pypi/v/frackture.svg)](https://pypi.org/project/frackture/)
[![Downloads](https://img.shields.io/pypi/dm/frackture.svg)](https://pypi.org/project/frackture/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

Frackture is a **symbolic compression engine** using recursive logic and entropy signatures to compress data while preserving identity and structure.

> Built to push boundaries in compression, data fingerprinting, and self-optimizing logic.

---

## 🚀 Installation

Install from PyPI:

```bash
pip install frackture
```

Or install from source with development dependencies:

```bash
git clone https://github.com/GoryGrey/frackture.git
cd frackture
pip install -e ".[dev]"
```

---

## 🧪 Basic Usage

```python
from frackture import compress, decompress

data = b"Hello world. This is a test of the emergency broadcast system."
compressed = compress(data)
original = decompress(compressed)

print(original)  # Reconstructed approximation
```

### Core Functions

```python
from frackture import (
    frackture_v3_3_safe,
    frackture_v3_3_reconstruct,
    optimize_frackture,
    frackture_preprocess_universal_v2_6,
)

# Preprocess and compress
data = "your input here"
preprocessed = frackture_preprocess_universal_v2_6(data)
payload = frackture_v3_3_safe(preprocessed)

# Reconstruct
reconstructed = frackture_v3_3_reconstruct(payload)

# Optimize with multiple trials
optimized_payload, mse = optimize_frackture(preprocessed, num_trials=5)
```

---

## 🧬 Features

- 🌀 Universal data preprocessing (handles strings, bytes, dicts, lists, arrays)
- 🧠 Symbolic fingerprinting (identity-preserving logic signatures)
- 📉 Entropy channel encoding with fixed-size output (~96 bytes per channel)
- ♻️ Self-optimization with decoder feedback loop
- 🔐 Structure-preserving compression across formats (text, binary, etc)
- 🎯 Zero-server architecture (all processing local)

---

## 📚 Use Cases

- Secure identity-preserving hashes
- Embedding compression for LLMs or AI pipelines
- Data integrity checking with entropy-aware patterns
- Experimental symbolic computing
- Content fingerprinting

---

## 🛠 Requirements

- Python 3.9+
- Dependencies: `numpy`, `scipy`, `scikit-learn`

(Handled automatically during install)

---

## 📦 Packaging & Distribution

This package is built with modern Python packaging standards:

- **Build backend**: Hatchling
- **Package format**: `src/` layout
- **Supported platforms**: Linux, macOS, Windows
- **Distribution**: PyPI (stable releases) and TestPyPI (development)

### Building from source

```bash
# Install build tools
pip install build twine

# Build wheels and source distribution
python -m build

# Validate distribution
twine check dist/*

# Install locally (editable)
pip install -e .
```

### Development setup

```bash
# Clone and setup
git clone https://github.com/GoryGrey/frackture.git
cd frackture

# Install with dev tools
pip install -e ".[dev]"

# Run tests
pytest

# Run linting
black src/ tests/
isort src/ tests/
flake8 src/ tests/
```

---

## 🔄 Zero-Server Architecture

Frackture runs entirely on your local machine:
- **No cloud services**: All compression/decompression happens locally
- **No telemetry**: Complete privacy by design
- **No dependencies**: Just NumPy, SciPy, and scikit-learn
- **Fully offline**: Works without internet connection

---

## 📄 License

MIT — do what you want, just don't sue me.

All usage must clearly cite the origin: **"Frackture: Recursive Compression & Symbolic Encoding, by Gregory Betti (f(∞))"**

---

## 🤖 Author

Built by [@GoryGrey](https://x.com/GoryGrey) — degen dev with a compression disorder.
Feel free to fork, remix, or break reality with it.

---

## 🔗 Links

- [PyPI Package](https://pypi.org/project/frackture/)
- [GitHub Repository](https://github.com/GoryGrey/frackture)
- [Contributing Guide](./CONTRIBUTING.md)
- [Changelog](./CHANGELOG.md)
