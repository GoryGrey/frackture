# Frackture Benchmark Results

**Generated:** 2025-12-15 08:20:49
**Enhanced Metrics Version:** 2.1.0

## New Verification Metrics

- **Payload Sizing**: Symbolic bytes, entropy bytes, serialized total, 96B validation
- **Reconstruction Quality**: MSE baseline vs optimized, lossless status
- **Optimization**: MSE improvement percentage, trials count
- **Determinism**: Multiple encoding tests, drift detection
- **Fault Injection**: Payload mutation tests, error handling validation
- **Competition Summary**: Frackture vs Gzip/Brotli wins by tier and by configuration

## Benchmark Configuration

- **Gzip levels:** [1, 6, 9]
- **Brotli qualities:** [4, 6, 11]
- **Real datasets:** False
- **All tiers:** False

## Competition Summary (Frackture vs Gzip/Brotli)

| Scope | Total Comparisons | Wins (Ratio) | Win Rate (Ratio) | Wins (Throughput) | Win Rate (Throughput) |
|---|---:|---:|---:|---:|---:|
| Overall | 30 | 9 | 30.0% | 0 | 0.0% |

### Win Rates by Tier

| Tier | Total Comparisons | Wins (Ratio) | Win Rate (Ratio) |
|---|---:|---:|---:|
| tiny | 30 | 9 | 30.0% |

---

## Dataset: tiny_tiny_text

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 41.00 B | 49.00 B | 0.84x | 7.79 | 0.29 | 0.01 MB/s | 0.13 MB/s | 0.0033 | 67.93 | 49 | ❌ | 0.278337 | 0.215631 | ❌ | ✅ |
| SHA256 | 41.00 B | 64.00 B | 0.64x | 0.00 | 0.00 | 33.07 MB/s | 0.00 MB/s | 0.0012 | 67.93 | - | - | - | - | - | - |
| AES-GCM | 41.00 B | 57.00 B | 0.72x | 1.33 | 0.44 | 0.03 MB/s | 0.09 MB/s | 0.0029 | 68.28 | - | - | - | - | - | - |
| Frackture Encrypted | 41.00 B | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 41.00 B | 59.00 B | 0.69x | 0.11 | 0.06 | 0.34 MB/s | 0.69 MB/s | 0.0029 | 68.36 | - | - | - | - | - | - |
| Gzip L6 | 41.00 B | 59.00 B | 0.69x | 0.03 | 0.02 | 1.52 MB/s | 1.58 MB/s | 0.0040 | 68.36 | - | - | - | - | - | - |
| Gzip L9 | 41.00 B | 59.00 B | 0.69x | 0.03 | 0.03 | 1.17 MB/s | 1.48 MB/s | 0.0029 | 68.36 | - | - | - | - | - | - |
| Brotli Q4 | 41.00 B | 43.00 B | 0.95x | 1.22 | 0.02 | 0.03 MB/s | 2.07 MB/s | 0.0029 | 68.73 | - | - | - | - | - | - |
| Brotli Q6 | 41.00 B | 45.00 B | 0.91x | 0.29 | 0.01 | 0.13 MB/s | 3.96 MB/s | 0.0032 | 69.00 | - | - | - | - | - | - |
| Brotli Q11 | 41.00 B | 43.00 B | 0.95x | 0.82 | 0.02 | 0.05 MB/s | 2.14 MB/s | 0.0030 | 69.60 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=49B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 22.53% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.278337)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: tiny_tiny_json

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 33.00 B | 49.00 B | 0.67x | 5.20 | 0.26 | 0.01 MB/s | 0.12 MB/s | 0.0030 | 69.61 | 49 | ❌ | 0.259878 | 0.219127 | ❌ | ✅ |
| SHA256 | 33.00 B | 64.00 B | 0.52x | 0.00 | 0.00 | 27.82 MB/s | 0.00 MB/s | 0.0011 | 69.61 | - | - | - | - | - | - |
| AES-GCM | 33.00 B | 49.00 B | 0.67x | 0.14 | 0.07 | 0.22 MB/s | 0.45 MB/s | 0.0034 | 69.61 | - | - | - | - | - | - |
| Frackture Encrypted | 33.00 B | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 33.00 B | 51.00 B | 0.65x | 0.05 | 0.03 | 0.68 MB/s | 0.95 MB/s | 0.0029 | 69.61 | - | - | - | - | - | - |
| Gzip L6 | 33.00 B | 51.00 B | 0.65x | 0.02 | 0.02 | 1.39 MB/s | 1.46 MB/s | 0.0032 | 69.61 | - | - | - | - | - | - |
| Gzip L9 | 33.00 B | 51.00 B | 0.65x | 0.02 | 0.02 | 1.30 MB/s | 1.46 MB/s | 0.0027 | 69.61 | - | - | - | - | - | - |
| Brotli Q4 | 33.00 B | 37.00 B | 0.89x | 0.04 | 0.01 | 0.82 MB/s | 4.55 MB/s | 0.0027 | 69.61 | - | - | - | - | - | - |
| Brotli Q6 | 33.00 B | 36.00 B | 0.92x | 0.09 | 0.01 | 0.34 MB/s | 2.18 MB/s | 0.0029 | 69.72 | - | - | - | - | - | - |
| Brotli Q11 | 33.00 B | 37.00 B | 0.89x | 0.54 | 0.01 | 0.06 MB/s | 3.79 MB/s | 0.0029 | 69.79 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=49B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 15.68% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.259878)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: tiny_tiny_binary

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 10.00 B | 49.00 B | 0.20x | 4.76 | 0.24 | 0.00 MB/s | 0.04 MB/s | 0.0029 | 69.79 | 49 | ❌ | 0.162775 | 0.170095 | ❌ | ✅ |
| SHA256 | 10.00 B | 64.00 B | 0.16x | 0.00 | 0.00 | 8.31 MB/s | 0.00 MB/s | 0.0011 | 69.79 | - | - | - | - | - | - |
| AES-GCM | 10.00 B | 26.00 B | 0.38x | 0.13 | 0.05 | 0.08 MB/s | 0.20 MB/s | 0.0031 | 69.79 | - | - | - | - | - | - |
| Frackture Encrypted | 10.00 B | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 10.00 B | 30.00 B | 0.33x | 0.05 | 0.04 | 0.20 MB/s | 0.22 MB/s | 0.0029 | 69.79 | - | - | - | - | - | - |
| Gzip L6 | 10.00 B | 30.00 B | 0.33x | 0.02 | 0.04 | 0.45 MB/s | 0.24 MB/s | 0.0027 | 69.79 | - | - | - | - | - | - |
| Gzip L9 | 10.00 B | 30.00 B | 0.33x | 0.02 | 0.02 | 0.52 MB/s | 0.50 MB/s | 0.0028 | 69.79 | - | - | - | - | - | - |
| Brotli Q4 | 10.00 B | 14.00 B | 0.71x | 0.03 | 0.01 | 0.27 MB/s | 1.21 MB/s | 0.0029 | 69.79 | - | - | - | - | - | - |
| Brotli Q6 | 10.00 B | 14.00 B | 0.71x | 0.04 | 0.00 | 0.22 MB/s | 2.47 MB/s | 0.0028 | 69.83 | - | - | - | - | - | - |
| Brotli Q11 | 10.00 B | 13.00 B | 0.77x | 0.33 | 0.01 | 0.03 MB/s | 0.98 MB/s | 0.0027 | 69.88 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=49B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: -4.50% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.162775)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: tiny_tiny_random

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 50.00 B | 65.00 B | 0.77x | 4.75 | 0.26 | 0.01 MB/s | 0.18 MB/s | 0.0029 | 69.88 | 65 | ❌ | 0.084609 | 0.084609 | ❌ | ✅ |
| SHA256 | 50.00 B | 64.00 B | 0.78x | 0.00 | 0.00 | 41.94 MB/s | 0.00 MB/s | 0.0011 | 69.88 | - | - | - | - | - | - |
| AES-GCM | 50.00 B | 66.00 B | 0.76x | 0.12 | 0.05 | 0.38 MB/s | 1.03 MB/s | 0.0028 | 69.88 | - | - | - | - | - | - |
| Frackture Encrypted | 50.00 B | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 50.00 B | 73.00 B | 0.68x | 0.05 | 0.03 | 0.94 MB/s | 1.48 MB/s | 0.0030 | 69.88 | - | - | - | - | - | - |
| Gzip L6 | 50.00 B | 73.00 B | 0.68x | 0.03 | 0.02 | 1.54 MB/s | 2.11 MB/s | 0.0027 | 69.88 | - | - | - | - | - | - |
| Gzip L9 | 50.00 B | 73.00 B | 0.68x | 0.02 | 0.02 | 2.05 MB/s | 2.42 MB/s | 0.0029 | 69.88 | - | - | - | - | - | - |
| Brotli Q4 | 50.00 B | 54.00 B | 0.93x | 0.05 | 0.01 | 0.88 MB/s | 6.65 MB/s | 0.0034 | 69.88 | - | - | - | - | - | - |
| Brotli Q6 | 50.00 B | 54.00 B | 0.93x | 0.12 | 0.01 | 0.40 MB/s | 9.47 MB/s | 0.0030 | 70.04 | - | - | - | - | - | - |
| Brotli Q11 | 50.00 B | 54.00 B | 0.93x | 0.92 | 0.01 | 0.05 MB/s | 6.40 MB/s | 0.0029 | 70.09 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 0.00% improvement over 2 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.084609)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: tiny_tiny_repetitive

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 50.00 B | 65.00 B | 0.77x | 4.69 | 0.25 | 0.01 MB/s | 0.19 MB/s | 0.0030 | 70.09 | 65 | ❌ | 0.162195 | 0.162195 | ❌ | ✅ |
| SHA256 | 50.00 B | 64.00 B | 0.78x | 0.00 | 0.00 | 34.44 MB/s | 0.00 MB/s | 0.0014 | 70.09 | - | - | - | - | - | - |
| AES-GCM | 50.00 B | 66.00 B | 0.76x | 0.12 | 0.05 | 0.39 MB/s | 1.02 MB/s | 0.0027 | 70.09 | - | - | - | - | - | - |
| Frackture Encrypted | 50.00 B | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 50.00 B | 25.00 B | 2.00x | 0.04 | 0.03 | 1.06 MB/s | 1.37 MB/s | 0.0029 | 70.09 | - | - | - | - | - | - |
| Gzip L6 | 50.00 B | 25.00 B | 2.00x | 0.02 | 0.02 | 2.38 MB/s | 2.22 MB/s | 0.0031 | 70.09 | - | - | - | - | - | - |
| Gzip L9 | 50.00 B | 25.00 B | 2.00x | 0.02 | 0.02 | 2.28 MB/s | 2.31 MB/s | 0.0027 | 70.09 | - | - | - | - | - | - |
| Brotli Q4 | 50.00 B | 11.00 B | 4.55x | 0.03 | 0.01 | 1.44 MB/s | 4.19 MB/s | 0.0027 | 70.09 | - | - | - | - | - | - |
| Brotli Q6 | 50.00 B | 11.00 B | 4.55x | 0.04 | 0.00 | 1.35 MB/s | 9.96 MB/s | 0.0030 | 70.11 | - | - | - | - | - | - |
| Brotli Q11 | 50.00 B | 12.00 B | 4.17x | 0.38 | 0.01 | 0.13 MB/s | 5.79 MB/s | 0.0027 | 70.15 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 0.00% improvement over 2 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.162195)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Summary

### Key Metrics

- **Compression Ratio**: Higher is better (original size / compressed size)
- **Throughput**: Higher is better (MB processed per second)
- **Latency**: Lower is better (milliseconds)
- **Memory**: Lower is better (peak memory usage in MB)
- **MSE**: Lower is better (reconstruction quality)
- **96B Target**: Frackture should maintain ~96-byte payloads

### Enhanced Frackture Verification

1. **Payload Size Validation**: Ensures Frackture maintains its ~96-byte promise
2. **Reconstruction Quality**: MSE measurements for baseline vs optimized encoding
3. **Optimization Impact**: Measures effectiveness of self-optimization
4. **Determinism Testing**: Validates consistent output across multiple runs
5. **Fault Injection**: Tests error handling and tamper detection

### Frackture Core Advantages

- Fixed-size output (~96 bytes) regardless of input size
- Identity-preserving symbolic fingerprints
- Fast hashing for integrity checks
- Dual-channel (symbolic + entropy) encoding
- Self-optimization with decoder feedback
- Built-in fault detection and error handling
