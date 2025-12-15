# Frackture Benchmark Results

**Generated:** 2025-12-15 10:00:40
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
| Overall | 30 | 27 | 90.0% | 6 | 20.0% |

### Win Rates by Tier

| Tier | Total Comparisons | Wins (Ratio) | Win Rate (Ratio) |
|---|---:|---:|---:|
| medium | 30 | 27 | 90.0% |

---

## Dataset: small_text

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 100.00 KB | 65.00 B | 1575.38x | 6.83 | 0.23 | 14.31 MB/s | 424.85 MB/s | 0.0749 | 70.00 | 65 | ❌ | 0.357602 | 0.277555 | ❌ | ✅ |
| SHA256 | 100.00 KB | 64.00 B | 1600.00x | 0.07 | 0.00 | 1322.72 MB/s | 0.00 MB/s | 0.0738 | 70.00 | - | - | - | - | - | - |
| AES-GCM | 100.00 KB | 100.02 KB | 1.00x | 1.18 | 0.36 | 83.07 MB/s | 272.14 MB/s | 0.0732 | 70.46 | - | - | - | - | - | - |
| Frackture Encrypted | 100.00 KB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 100.00 KB | 22.25 KB | 4.49x | 0.93 | 0.44 | 105.27 MB/s | 223.19 MB/s | 0.0732 | 70.55 | - | - | - | - | - | - |
| Gzip L6 | 100.00 KB | 15.59 KB | 6.41x | 3.55 | 0.35 | 27.48 MB/s | 278.56 MB/s | 0.0765 | 70.55 | - | - | - | - | - | - |
| Gzip L9 | 100.00 KB | 15.09 KB | 6.63x | 14.64 | 0.28 | 6.67 MB/s | 348.25 MB/s | 0.0747 | 70.55 | - | - | - | - | - | - |
| Brotli Q4 | 100.00 KB | 20.27 KB | 4.93x | 2.64 | 0.23 | 37.03 MB/s | 421.28 MB/s | 0.0750 | 70.99 | - | - | - | - | - | - |
| Brotli Q6 | 100.00 KB | 16.61 KB | 6.02x | 3.26 | 0.17 | 29.99 MB/s | 580.59 MB/s | 0.0726 | 72.79 | - | - | - | - | - | - |
| Brotli Q11 | 100.00 KB | 13.79 KB | 7.25x | 154.56 | 0.20 | 0.63 MB/s | 484.81 MB/s | 0.0717 | 79.40 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 22.38% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.357602)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: small_json

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 100.00 KB | 65.00 B | 1575.38x | 5.21 | 0.21 | 18.74 MB/s | 468.12 MB/s | 0.0727 | 80.35 | 65 | ❌ | 0.191871 | 0.183644 | ❌ | ✅ |
| SHA256 | 100.00 KB | 64.00 B | 1600.00x | 0.07 | 0.00 | 1380.22 MB/s | 0.00 MB/s | 0.0708 | 80.35 | - | - | - | - | - | - |
| AES-GCM | 100.00 KB | 100.02 KB | 1.00x | 0.14 | 0.10 | 703.15 MB/s | 1019.73 MB/s | 0.0731 | 80.35 | - | - | - | - | - | - |
| Frackture Encrypted | 100.00 KB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 100.00 KB | 13.46 KB | 7.43x | 0.46 | 0.23 | 211.72 MB/s | 423.02 MB/s | 0.0776 | 80.35 | - | - | - | - | - | - |
| Gzip L6 | 100.00 KB | 10.71 KB | 9.34x | 0.95 | 0.18 | 102.89 MB/s | 534.89 MB/s | 0.0741 | 80.35 | - | - | - | - | - | - |
| Gzip L9 | 100.00 KB | 9.94 KB | 10.06x | 4.24 | 0.18 | 23.05 MB/s | 534.53 MB/s | 0.0822 | 80.35 | - | - | - | - | - | - |
| Brotli Q4 | 100.00 KB | 8.80 KB | 11.36x | 0.74 | 0.12 | 131.44 MB/s | 842.30 MB/s | 0.0694 | 80.38 | - | - | - | - | - | - |
| Brotli Q6 | 100.00 KB | 7.87 KB | 12.71x | 1.92 | 0.13 | 50.88 MB/s | 758.26 MB/s | 0.0693 | 81.32 | - | - | - | - | - | - |
| Brotli Q11 | 100.00 KB | 6.55 KB | 15.27x | 162.76 | 0.12 | 0.60 MB/s | 841.68 MB/s | 0.0751 | 81.32 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 4.29% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.191871)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: small_binary_blob

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 75.00 KB | 65.00 B | 1181.54x | 5.57 | 0.21 | 13.16 MB/s | 351.69 MB/s | 0.0547 | 81.32 | 65 | ❌ | 0.321718 | 0.143347 | ❌ | ✅ |
| SHA256 | 75.00 KB | 64.00 B | 1200.00x | 0.05 | 0.00 | 1472.00 MB/s | 0.00 MB/s | 0.0498 | 81.32 | - | - | - | - | - | - |
| AES-GCM | 75.00 KB | 75.02 KB | 1.00x | 0.13 | 0.07 | 558.53 MB/s | 1025.74 MB/s | 0.0534 | 81.36 | - | - | - | - | - | - |
| Frackture Encrypted | 75.00 KB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 75.00 KB | 25.49 KB | 2.94x | 0.49 | 0.13 | 148.55 MB/s | 547.43 MB/s | 0.0534 | 81.36 | - | - | - | - | - | - |
| Gzip L6 | 75.00 KB | 25.29 KB | 2.97x | 0.59 | 0.15 | 123.96 MB/s | 502.82 MB/s | 0.0532 | 81.36 | - | - | - | - | - | - |
| Gzip L9 | 75.00 KB | 25.29 KB | 2.97x | 0.59 | 0.14 | 123.37 MB/s | 518.55 MB/s | 0.0556 | 81.36 | - | - | - | - | - | - |
| Brotli Q4 | 75.00 KB | 25.02 KB | 3.00x | 0.32 | 0.15 | 230.96 MB/s | 488.29 MB/s | 0.0524 | 81.36 | - | - | - | - | - | - |
| Brotli Q6 | 75.00 KB | 25.03 KB | 3.00x | 0.65 | 0.12 | 112.80 MB/s | 596.73 MB/s | 0.0523 | 81.36 | - | - | - | - | - | - |
| Brotli Q11 | 75.00 KB | 25.03 KB | 3.00x | 80.24 | 0.13 | 0.91 MB/s | 547.00 MB/s | 0.0563 | 81.78 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 55.44% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.321718)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: small_random_noise

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 100.00 KB | 65.00 B | 1575.38x | 5.27 | 0.21 | 18.53 MB/s | 458.09 MB/s | 0.0755 | 81.78 | 65 | ❌ | 0.176390 | 0.150367 | ❌ | ✅ |
| SHA256 | 100.00 KB | 64.00 B | 1600.00x | 0.07 | 0.00 | 1360.89 MB/s | 0.00 MB/s | 0.0718 | 81.78 | - | - | - | - | - | - |
| AES-GCM | 100.00 KB | 100.02 KB | 1.00x | 0.13 | 0.07 | 758.90 MB/s | 1426.10 MB/s | 0.0737 | 81.78 | - | - | - | - | - | - |
| Frackture Encrypted | 100.00 KB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 100.00 KB | 100.05 KB | 1.00x | 2.19 | 0.07 | 44.65 MB/s | 1377.34 MB/s | 0.0765 | 81.78 | - | - | - | - | - | - |
| Gzip L6 | 100.00 KB | 100.05 KB | 1.00x | 2.25 | 0.06 | 43.45 MB/s | 1551.50 MB/s | 0.0766 | 81.78 | - | - | - | - | - | - |
| Gzip L9 | 100.00 KB | 100.05 KB | 1.00x | 2.21 | 0.06 | 44.24 MB/s | 1609.95 MB/s | 0.0773 | 81.78 | - | - | - | - | - | - |
| Brotli Q4 | 100.00 KB | 100.00 KB | 1.00x | 0.17 | 0.02 | 591.10 MB/s | 6086.40 MB/s | 0.0689 | 81.78 | - | - | - | - | - | - |
| Brotli Q6 | 100.00 KB | 100.00 KB | 1.00x | 0.77 | 0.02 | 127.28 MB/s | 5841.73 MB/s | 0.0732 | 81.86 | - | - | - | - | - | - |
| Brotli Q11 | 100.00 KB | 100.00 KB | 1.00x | 21.31 | 0.02 | 4.58 MB/s | 5805.62 MB/s | 0.0702 | 81.86 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 14.75% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.176390)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: small_highly_repetitive

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 100.00 KB | 65.00 B | 1575.38x | 5.17 | 0.20 | 18.88 MB/s | 490.47 MB/s | 0.0706 | 81.86 | 65 | ❌ | 0.356588 | 0.199328 | ❌ | ✅ |
| SHA256 | 100.00 KB | 64.00 B | 1600.00x | 0.07 | 0.00 | 1457.92 MB/s | 0.00 MB/s | 0.0670 | 81.86 | - | - | - | - | - | - |
| AES-GCM | 100.00 KB | 100.02 KB | 1.00x | 0.11 | 0.06 | 893.19 MB/s | 1564.40 MB/s | 0.0698 | 81.86 | - | - | - | - | - | - |
| Frackture Encrypted | 100.00 KB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 100.00 KB | 537.00 B | 190.69x | 0.14 | 0.07 | 694.82 MB/s | 1388.82 MB/s | 0.0722 | 81.86 | - | - | - | - | - | - |
| Gzip L6 | 100.00 KB | 138.00 B | 742.03x | 0.35 | 0.13 | 277.49 MB/s | 758.69 MB/s | 0.0729 | 81.86 | - | - | - | - | - | - |
| Gzip L9 | 100.00 KB | 138.00 B | 742.03x | 0.39 | 0.10 | 253.47 MB/s | 957.81 MB/s | 0.0743 | 81.86 | - | - | - | - | - | - |
| Brotli Q4 | 100.00 KB | 17.00 B | 6023.53x | 0.08 | 0.11 | 1176.20 MB/s | 905.26 MB/s | 0.0735 | 81.86 | - | - | - | - | - | - |
| Brotli Q6 | 100.00 KB | 17.00 B | 6023.53x | 0.07 | 0.09 | 1453.67 MB/s | 1128.39 MB/s | 0.0789 | 81.86 | - | - | - | - | - | - |
| Brotli Q11 | 100.00 KB | 18.00 B | 5688.89x | 6.28 | 0.11 | 15.55 MB/s | 853.95 MB/s | 0.0742 | 81.86 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 44.10% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.356588)
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
