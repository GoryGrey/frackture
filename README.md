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

## 🧪 Development & Testing

Frackture includes a comprehensive test suite with ≥85% code coverage.

### Running Tests

Install development dependencies:
```bash
pip install -e ".[dev]"
# or
pip install pytest pytest-cov
```

Run all tests:
```bash
pytest
```

Run tests with coverage report:
```bash
pytest --cov=. --cov-report=term-missing --cov-report=html
```

Run specific test categories:
```bash
# Unit tests only
pytest -m unit

# Integration tests only
pytest -m integration

# Edge case tests only
pytest -m edge
```

Run tests for a specific module:
```bash
pytest tests/test_preprocessing.py
pytest tests/test_symbolic_fingerprint.py
pytest tests/test_entropy_channel.py
pytest tests/test_integration.py
pytest tests/test_optimizer.py
```

### Test Coverage

The test suite covers:
- ✅ Universal preprocessing for all input types (text, bytes, dicts, NumPy arrays)
- ✅ Deterministic symbolic fingerprinting
- ✅ Encode/decode round-trips
- ✅ Entropy channel behavior
- ✅ Error handling for invalid payloads
- ✅ Optimizer MSE reduction
- ✅ Edge cases (empty inputs, large inputs, malformed data)

View detailed coverage report:
```bash
pytest --cov=. --cov-report=html
open htmlcov/index.html
```

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
