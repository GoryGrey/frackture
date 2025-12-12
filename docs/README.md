# 📚 Frackture Documentation

Welcome to the comprehensive documentation for Frackture, the unified symbolic compression, encryption, and hashing library.

---

## 📖 Documentation Structure

### Getting Started
- **[Main README](../README.md)** - Installation, quick start, and overview
- **[Examples](./EXAMPLES.md)** - Copy-paste code examples for all workflows
- **[FAQ](./FAQ.md)** - Frequently asked questions and troubleshooting

### Technical Documentation
- **[Architecture](./ARCHITECTURE.md)** - Deep dive into dual-channel design, algorithms, and implementation
- **[Security](./SECURITY.md)** - Security properties, threat model, and best practices

### Verification & Performance
- **[Test Report](../TEST_REPORT.md)** - Comprehensive test coverage and results
- **[Benchmark Summary](../BENCHMARK_SUITE_SUMMARY.md)** - Performance comparisons vs gzip/brotli
- **[Benchmark Suite](../benchmarks/README.md)** - How to run and interpret benchmarks

---

## 🚀 Quick Navigation

### I want to...

**...get started quickly**
→ Read the [Main README](../README.md) and check [Examples](./EXAMPLES.md)

**...understand how Frackture works**
→ Read [Architecture](./ARCHITECTURE.md)

**...implement secure encryption**
→ Read [Security](./SECURITY.md) and [Examples - Encryption section](./EXAMPLES.md#encryption--decryption)

**...see performance data**
→ Check [Benchmark Summary](../BENCHMARK_SUITE_SUMMARY.md)

**...troubleshoot issues**
→ Check [FAQ - Troubleshooting](./FAQ.md#troubleshooting)

**...understand use cases**
→ Read [FAQ - Use Case Questions](./FAQ.md#use-case-questions)

**...contribute**
→ Read [FAQ - Getting Help](./FAQ.md#getting-help)

---

## 📋 Documentation Overview

### [ARCHITECTURE.md](./ARCHITECTURE.md)
Deep technical dive into Frackture's design:
- Universal preprocessor implementation
- Symbolic channel algorithm (recursive XOR + masking)
- Entropy channel algorithm (FFT + statistical features)
- Reconstruction and merging
- Self-optimization mechanism
- Security layer design
- Performance characteristics

**Read if:** You want to understand implementation details or contribute.

### [SECURITY.md](./SECURITY.md)
Comprehensive security analysis:
- Threat model and attack scenarios
- HMAC authentication properties
- Collision and timing attack resistance
- Security limitations and best practices
- Key management guidelines
- Compliance considerations (FIPS, GDPR, HIPAA, PCI DSS)

**Read if:** You need to deploy Frackture in production or security-sensitive contexts.

### [EXAMPLES.md](./EXAMPLES.md)
Copy-paste code examples:
- Basic usage patterns
- Compression & fingerprinting workflows
- Encryption & decryption examples
- Hashing & integrity checking
- Self-optimization usage
- Advanced patterns (pipelines, caching, streaming)
- Integration examples (Flask API, database storage)
- Error handling strategies

**Read if:** You want practical code to adapt for your use case.

### [FAQ.md](./FAQ.md)
Frequently asked questions:
- General concepts and terminology
- Technical implementation questions
- Use case recommendations
- Performance optimization tips
- Security considerations
- Troubleshooting common issues
- Comparisons to other technologies

**Read if:** You have specific questions or need quick answers.

---

## 🎯 Use Case Documentation

### Data Fingerprinting
- **[Examples - Fingerprinting](./EXAMPLES.md#compression--fingerprinting)**
- **[FAQ - Deduplication](./FAQ.md#is-frackture-suitable-for-deduplication)**
- **[Architecture - Symbolic Channel](./ARCHITECTURE.md#symbolic-channel)**

### Secure Encryption
- **[Examples - Encryption](./EXAMPLES.md#encryption--decryption)**
- **[Security - HMAC Authentication](./SECURITY.md#security-features)**
- **[FAQ - Encryption](./FAQ.md#should-i-use-frackture-for-encryption)**

### Identity-Preserving Hashing
- **[Examples - Hashing](./EXAMPLES.md#hashing--integrity)**
- **[Security - Collision Resistance](./SECURITY.md#attack-resistance)**
- **[FAQ - Hashing](./FAQ.md#are-collisions-possible)**

### Similarity Detection
- **[Examples - Similarity Detection](./EXAMPLES.md#similarity-detection)**
- **[Architecture - Entropy Channel](./ARCHITECTURE.md#entropy-channel)**
- **[FAQ - Similarity Search](./FAQ.md#can-i-use-frackture-for-similarity-search)**

### Self-Optimization
- **[Examples - Optimization](./EXAMPLES.md#self-optimization)**
- **[Architecture - Self-Optimization](./ARCHITECTURE.md#self-optimization)**
- **[FAQ - MSE Too High](./FAQ.md#mse-too-high-after-reconstruction)**

---

## 🔬 Research & Analysis

### Algorithm Analysis
- **[Architecture - Channel Details](./ARCHITECTURE.md#channel-details)**
- **[Architecture - Design Philosophy](./ARCHITECTURE.md#design-philosophy)**

### Security Analysis
- **[Security - Cryptographic Properties](./SECURITY.md#cryptographic-properties)**
- **[Security - Attack Resistance](./SECURITY.md#attack-resistance)**
- **[Security - Threat Model](./SECURITY.md#threat-model)**

### Performance Analysis
- **[Benchmark Suite Summary](../BENCHMARK_SUITE_SUMMARY.md)**
- **[Architecture - Performance Characteristics](./ARCHITECTURE.md#performance-characteristics)**
- **[FAQ - Performance Questions](./FAQ.md#performance-questions)**

---

## 📊 Benchmark & Test Data

### Running Tests
```bash
# All tests
python -m pytest tests/ -v

# Specific categories
python -m pytest tests/test_encryption.py -v
python -m pytest tests/test_optimization.py -v

# With coverage
python -m pytest tests/ --cov="frackture (2)" --cov-report=term-missing
```

### Running Benchmarks
```bash
cd benchmarks
python benchmark_frackture.py

# Specific sizes
python benchmark_frackture.py --small-only
python benchmark_frackture.py --large-only
```

See **[Test Report](../TEST_REPORT.md)** and **[Benchmark Suite](../benchmarks/README.md)** for details.

---

## 🛠️ API Reference

### Core Functions

| Function | Purpose | Documentation |
|----------|---------|---------------|
| `frackture_preprocess_universal_v2_6()` | Convert any input to 768-element vector | [README](../README.md#frackture_preprocess_universal_v2_6data) |
| `frackture_v3_3_safe()` | Encode to dual-channel payload | [README](../README.md#frackture_v3_3_safeinput_vector) |
| `frackture_v3_3_reconstruct()` | Reconstruct from payload | [README](../README.md#frackture_v3_3_reconstructpayload) |
| `optimize_frackture()` | Self-optimizing compression | [README](../README.md#optimize_fractureinput_vector-num_trials5) |

### Encryption Functions

| Function | Purpose | Documentation |
|----------|---------|---------------|
| `frackture_encrypt_payload()` | Encrypt with HMAC auth | [README](../README.md#frackture_encrypt_payloadpayload-key) |
| `frackture_decrypt_payload()` | Decrypt and verify | [README](../README.md#frackture_decrypt_payloadencrypted_payload-key) |

### Hashing Functions

| Function | Purpose | Documentation |
|----------|---------|---------------|
| `frackture_deterministic_hash()` | Generate SHA256 hash | [README](../README.md#frackture_deterministic_hashdata-salt) |

---

## 🤝 Contributing

We welcome contributions! Areas where you can help:

### Documentation
- Fix typos or unclear explanations
- Add more examples
- Translate documentation
- Improve diagrams

### Code
- Performance improvements
- Bug fixes
- New features
- Additional tests

### Community
- Answer questions in GitHub Discussions
- Share use cases and success stories
- Create tutorials or blog posts

**See [FAQ - Contributing](./FAQ.md#how-do-i-contribute) for details.**

---

## 📞 Getting Help

### Documentation Not Clear?
Open an issue on GitHub with:
- Which document is unclear
- What you're trying to understand
- Suggestions for improvement

### Found a Bug?
Report on GitHub Issues with:
- Minimal reproducible example
- Expected vs actual behavior
- Environment details (Python version, OS)

### Have Questions?
Check **[FAQ](./FAQ.md)** first, then:
- GitHub Discussions for general questions
- Twitter [@GoryGrey](https://x.com/GoryGrey)
- Stack Overflow (tag: `frackture`)

---

## 📄 License

MIT License with attribution requirement.

**Attribution:**  
*"Frackture: Recursive Compression & Symbolic Encoding, by Gregory Betti (f(∞))"*

See [LICENSE](../LICENSE) for full details.

---

## 🔗 External Resources

### Related Technologies
- **Perceptual Hashing:** [pHash](http://www.phash.org/)
- **MinHash:** [Wikipedia](https://en.wikipedia.org/wiki/MinHash)
- **Locality-Sensitive Hashing:** [Wikipedia](https://en.wikipedia.org/wiki/Locality-sensitive_hashing)

### Cryptography
- **HMAC:** [RFC 2104](https://tools.ietf.org/html/rfc2104)
- **SHA-256:** [FIPS 180-4](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf)
- **Argon2:** [Password Hashing](https://github.com/P-H-C/phc-winner-argon2)

### Compression
- **gzip:** [RFC 1952](https://tools.ietf.org/html/rfc1952)
- **brotli:** [RFC 7932](https://tools.ietf.org/html/rfc7932)
- **zstd:** [Facebook Research](https://facebook.github.io/zstd/)

---

<div align="center">

**🧠 Frackture Documentation**

*Comprehensive guides for compression, encryption, and hashing*

[GitHub](#) | [PyPI](https://pypi.org/project/frackture/) | [Twitter](https://x.com/GoryGrey)

</div>
