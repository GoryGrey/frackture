# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial package restructuring with `src/frackture/` layout
- `pyproject.toml` with Hatchling build backend
- Modern CI/CD workflows for testing and publishing
- Comprehensive documentation (README, CONTRIBUTING, CHANGELOG)

## [0.1.0] - 2025-01-01

### Added
- Initial release of Frackture
- Universal data preprocessing supporting strings, bytes, dicts, lists, and numpy arrays
- Symbolic fingerprinting with recursive XOR/masking for identity-preserving hashes
- Entropy channel encoding using FFT and PCA dimensionality reduction
- Self-optimization loop for minimizing reconstruction error
- Core compression/decompression functions (`compress`, `decompress`)
- Advanced API: `frackture_v3_3_safe`, `frackture_v3_3_reconstruct`, `optimize_frackture`
- Fixed-size output payloads (~96 bytes per channel)
- Zero-server architecture with complete local processing

### Features
- 🌀 Universal data preprocessing
- 🧠 Symbolic fingerprinting (identity-preserving logic signatures)
- 📉 Entropy channel encoding with fixed-size output
- ♻️ Self-optimization with decoder feedback loop
- 🔐 Structure-preserving compression across formats
- 🎯 Zero-server architecture (all processing local)

### Documentation
- README with installation, usage examples, and use cases
- Contributing guidelines
- License (MIT with attribution requirement)

---

## Release Process

See [CONTRIBUTING.md](./CONTRIBUTING.md) for detailed release instructions.

Releases are automated via GitHub Actions on tagged commits matching `v*` pattern.
