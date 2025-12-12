# Contributing to Frackture

Thank you for your interest in contributing to Frackture! This document provides guidelines and instructions for development, testing, and releasing.

## Table of Contents

- [Development Setup](#development-setup)
- [Code Style](#code-style)
- [Testing](#testing)
- [Release Instructions](#release-instructions)

---

## Development Setup

### Prerequisites

- Python 3.9+
- Git
- pip/venv

### Setup Steps

1. **Clone the repository**

```bash
git clone https://github.com/GoryGrey/frackture.git
cd frackture
```

2. **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install in editable mode with dev dependencies**

```bash
pip install -e ".[dev]"
```

This installs:
- Core dependencies: `numpy`, `scipy`, `scikit-learn`
- Dev tools: `black`, `isort`, `flake8`, `mypy`
- Test tools: `pytest`, `pytest-cov`

---

## Code Style

We follow PEP 8 with some stricter standards enforced by our tooling.

### Formatting

**Black** (line length: 100 characters):
```bash
black src/ tests/
```

**isort** (import sorting):
```bash
isort src/ tests/
```

### Linting

**Flake8**:
```bash
flake8 src/ tests/
```

**Mypy** (type checking, optional enforcement):
```bash
mypy src/
```

### Pre-commit Hooks

Before committing, ensure code passes all checks:

```bash
black src/ tests/ && isort src/ tests/ && flake8 src/ tests/
```

---

## Testing

### Running Tests

```bash
pytest
```

With coverage:
```bash
pytest --cov=src/frackture --cov-report=html
```

### Test Structure

Tests should be placed in the `tests/` directory with the naming convention:
- Test files: `test_*.py` or `*_test.py`
- Test functions: `test_*`

Example:
```python
# tests/test_core.py
import pytest
from frackture import compress, decompress

def test_compress_decompress():
    data = b"test"
    compressed = compress(data)
    result = decompress(compressed)
    assert result is not None
```

---

## Release Instructions

### Prerequisites

Before releasing, ensure:
1. All tests pass: `pytest`
2. Code is formatted: `black src/ tests/ && isort src/ tests/`
3. No linting errors: `flake8 src/ tests/`
4. CHANGELOG.md is updated with new changes

### Manual Release Process

1. **Update version**

Edit `src/frackture/version.py`:
```python
__version__ = "X.Y.Z"  # Use semantic versioning
```

2. **Update CHANGELOG**

Add a new section in `CHANGELOG.md` under `## [X.Y.Z] - YYYY-MM-DD`

3. **Create a git tag**

```bash
git add -A
git commit -m "chore: release v0.2.0"
git tag -a v0.2.0 -m "Release version 0.2.0"
git push origin main --tags
```

### Automated Release (GitHub Actions)

When a tag matching `v*` is pushed, the GitHub Actions workflow automatically:
1. Runs tests on Python 3.9-3.12
2. Builds wheels and source distributions
3. Publishes to TestPyPI (for validation)
4. Upon workflow approval, publishes to PyPI

**Tag format**: `vX.Y.Z` (e.g., `v0.1.0`, `v1.2.3`)

### Verification

After release, verify the package on PyPI:

```bash
pip install --upgrade frackture
python -c "import frackture; print(frackture.__version__)"
```

Test from TestPyPI before production:
```bash
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ frackture
```

---

## Building Locally

### Build wheels and source distribution

```bash
pip install build
python -m build
```

### Validate distribution

```bash
pip install twine
twine check dist/*
```

### Install locally

```bash
pip install -e .
```

---

## Package Structure

```
frackture/
├── src/frackture/          # Main package
│   ├── __init__.py         # Public API
│   ├── core.py             # Core functionality
│   └── version.py          # Version info
├── tests/                  # Test suite
├── pyproject.toml          # Project metadata & build config
├── MANIFEST.in             # Package manifest
├── README.md               # User documentation
├── CHANGELOG.md            # Release notes
├── CONTRIBUTING.md         # This file
└── LICENSE                 # MIT License
```

---

## CI/CD Workflows

### Test Workflow

Triggered on every push/PR:
- Runs tests on Python 3.9, 3.10, 3.11, 3.12
- Runs linting and type checks
- Generates coverage reports

### Publish Workflow

Triggered on tagged releases (`v*`):
- Builds wheels and source distribution
- Publishes to TestPyPI
- Requires manual approval for PyPI publication

---

## Licensing

All contributions must adhere to the MIT license with attribution requirement:

> All usage must clearly cite the origin: **"Frackture: Recursive Compression & Symbolic Encoding, by Gregory Betti (f(∞))"**

---

## Questions?

Feel free to open an issue or discussion on GitHub. We welcome all feedback and contributions!

---

**Author**: [@GoryGrey](https://x.com/GoryGrey)
