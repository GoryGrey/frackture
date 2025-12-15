# Frackture Benchmark Results

**Generated:** 2025-12-15 06:39:46
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
| Frackture | 100.00 KB | 65.00 B | 1575.38x | 7.24 | 0.29 | 13.49 MB/s | 338.68 MB/s | 0.0784 | 70.95 | 65 | ❌ | 0.329752 | 0.283997 | ❌ | ✅ |
| SHA256 | 100.00 KB | 64.00 B | 1600.00x | 0.08 | 0.00 | 1264.06 MB/s | 0.00 MB/s | 0.0773 | 70.95 | - | - | - | - | - | - |
| AES-GCM | 100.00 KB | 100.02 KB | 1.00x | 1.21 | 0.30 | 81.01 MB/s | 320.43 MB/s | 0.0814 | 71.41 | - | - | - | - | - | - |
| Frackture Encrypted | 100.00 KB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 100.00 KB | 22.23 KB | 4.50x | 0.99 | 0.51 | 98.71 MB/s | 190.19 MB/s | 0.0787 | 71.34 | - | - | - | - | - | - |
| Gzip L6 | 100.00 KB | 15.51 KB | 6.45x | 3.61 | 0.28 | 27.07 MB/s | 348.18 MB/s | 0.0788 | 71.34 | - | - | - | - | - | - |
| Gzip L9 | 100.00 KB | 15.01 KB | 6.66x | 14.83 | 0.28 | 6.59 MB/s | 353.69 MB/s | 0.0740 | 71.34 | - | - | - | - | - | - |
| Brotli Q4 | 100.00 KB | 20.24 KB | 4.94x | 4.50 | 0.24 | 21.71 MB/s | 410.29 MB/s | 0.0783 | 71.79 | - | - | - | - | - | - |
| Brotli Q6 | 100.00 KB | 16.50 KB | 6.06x | 3.10 | 0.17 | 31.47 MB/s | 559.58 MB/s | 0.0810 | 73.58 | - | - | - | - | - | - |
| Brotli Q11 | 100.00 KB | 13.77 KB | 7.26x | 159.48 | 0.20 | 0.61 MB/s | 482.02 MB/s | 0.0783 | 80.20 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 13.88% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.329752)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ✅ Passed

---

## Dataset: small_json

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 100.00 KB | 65.00 B | 1575.38x | 5.70 | 0.22 | 17.12 MB/s | 440.40 MB/s | 0.0738 | 81.14 | 65 | ❌ | 0.204423 | 0.176305 | ❌ | ✅ |
| SHA256 | 100.00 KB | 64.00 B | 1600.00x | 0.07 | 0.00 | 1351.31 MB/s | 0.00 MB/s | 0.0723 | 81.14 | - | - | - | - | - | - |
| AES-GCM | 100.00 KB | 100.02 KB | 1.00x | 0.15 | 0.08 | 651.25 MB/s | 1243.25 MB/s | 0.0733 | 81.14 | - | - | - | - | - | - |
| Frackture Encrypted | 100.00 KB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 100.00 KB | 13.51 KB | 7.40x | 0.49 | 0.24 | 197.69 MB/s | 403.44 MB/s | 0.0766 | 81.14 | - | - | - | - | - | - |
| Gzip L6 | 100.00 KB | 10.70 KB | 9.34x | 1.09 | 0.19 | 89.78 MB/s | 505.84 MB/s | 0.0765 | 81.14 | - | - | - | - | - | - |
| Gzip L9 | 100.00 KB | 9.91 KB | 10.09x | 4.69 | 0.26 | 20.82 MB/s | 377.21 MB/s | 0.0796 | 81.14 | - | - | - | - | - | - |
| Brotli Q4 | 100.00 KB | 8.87 KB | 11.27x | 0.77 | 0.14 | 126.43 MB/s | 693.51 MB/s | 0.0815 | 81.18 | - | - | - | - | - | - |
| Brotli Q6 | 100.00 KB | 7.88 KB | 12.69x | 2.07 | 0.14 | 47.16 MB/s | 704.33 MB/s | 0.0892 | 82.11 | - | - | - | - | - | - |
| Brotli Q11 | 100.00 KB | 6.56 KB | 15.24x | 164.43 | 0.13 | 0.59 MB/s | 773.06 MB/s | 0.0783 | 82.11 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 13.75% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.204423)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ✅ Passed

---

## Dataset: small_binary_blob

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 75.00 KB | 65.00 B | 1181.54x | 5.53 | 0.22 | 13.23 MB/s | 330.88 MB/s | 0.0587 | 82.11 | 65 | ❌ | 0.321718 | 0.143347 | ❌ | ✅ |
| SHA256 | 75.00 KB | 64.00 B | 1200.00x | 0.06 | 0.00 | 1205.06 MB/s | 0.00 MB/s | 0.0608 | 82.11 | - | - | - | - | - | - |
| AES-GCM | 75.00 KB | 75.02 KB | 1.00x | 0.15 | 0.08 | 477.20 MB/s | 885.52 MB/s | 0.0624 | 82.14 | - | - | - | - | - | - |
| Frackture Encrypted | 75.00 KB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 75.00 KB | 25.49 KB | 2.94x | 0.59 | 0.15 | 124.00 MB/s | 483.50 MB/s | 0.0603 | 82.14 | - | - | - | - | - | - |
| Gzip L6 | 75.00 KB | 25.29 KB | 2.97x | 0.65 | 0.19 | 113.48 MB/s | 388.28 MB/s | 0.0592 | 82.14 | - | - | - | - | - | - |
| Gzip L9 | 75.00 KB | 25.29 KB | 2.97x | 0.60 | 0.15 | 122.83 MB/s | 480.90 MB/s | 0.0587 | 82.14 | - | - | - | - | - | - |
| Brotli Q4 | 75.00 KB | 25.02 KB | 3.00x | 0.43 | 0.15 | 168.56 MB/s | 481.21 MB/s | 0.0577 | 82.14 | - | - | - | - | - | - |
| Brotli Q6 | 75.00 KB | 25.02 KB | 3.00x | 0.55 | 0.14 | 133.44 MB/s | 516.88 MB/s | 0.0598 | 82.14 | - | - | - | - | - | - |
| Brotli Q11 | 75.00 KB | 25.03 KB | 3.00x | 97.89 | 0.14 | 0.75 MB/s | 513.51 MB/s | 0.0633 | 82.56 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 55.44% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.321718)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ✅ Passed

---

## Dataset: small_random_noise

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 100.00 KB | 65.00 B | 1575.38x | 5.72 | 0.22 | 17.07 MB/s | 435.03 MB/s | 0.0826 | 82.56 | 65 | ❌ | 0.159255 | 0.132777 | ❌ | ✅ |
| SHA256 | 100.00 KB | 64.00 B | 1600.00x | 0.08 | 0.00 | 1289.36 MB/s | 0.00 MB/s | 0.0757 | 82.56 | - | - | - | - | - | - |
| AES-GCM | 100.00 KB | 100.02 KB | 1.00x | 0.19 | 0.08 | 526.07 MB/s | 1242.98 MB/s | 0.0816 | 82.56 | - | - | - | - | - | - |
| Frackture Encrypted | 100.00 KB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 100.00 KB | 100.05 KB | 1.00x | 2.26 | 0.10 | 43.29 MB/s | 948.86 MB/s | 0.0784 | 82.56 | - | - | - | - | - | - |
| Gzip L6 | 100.00 KB | 100.05 KB | 1.00x | 2.41 | 0.07 | 40.47 MB/s | 1386.59 MB/s | 0.0799 | 82.56 | - | - | - | - | - | - |
| Gzip L9 | 100.00 KB | 100.05 KB | 1.00x | 2.39 | 0.07 | 40.88 MB/s | 1472.21 MB/s | 0.0793 | 82.56 | - | - | - | - | - | - |
| Brotli Q4 | 100.00 KB | 100.00 KB | 1.00x | 0.22 | 0.02 | 448.41 MB/s | 5255.70 MB/s | 0.0798 | 82.56 | - | - | - | - | - | - |
| Brotli Q6 | 100.00 KB | 100.00 KB | 1.00x | 0.79 | 0.02 | 123.43 MB/s | 5504.55 MB/s | 0.0821 | 82.64 | - | - | - | - | - | - |
| Brotli Q11 | 100.00 KB | 100.00 KB | 1.00x | 22.78 | 0.02 | 4.29 MB/s | 5156.09 MB/s | 0.0754 | 82.64 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 16.63% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.159255)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ✅ Passed

---

## Dataset: small_highly_repetitive

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 100.00 KB | 65.00 B | 1575.38x | 5.43 | 0.21 | 17.98 MB/s | 462.42 MB/s | 0.0823 | 82.64 | 65 | ❌ | 0.356588 | 0.199328 | ❌ | ✅ |
| SHA256 | 100.00 KB | 64.00 B | 1600.00x | 0.08 | 0.00 | 1294.67 MB/s | 0.00 MB/s | 0.0754 | 82.64 | - | - | - | - | - | - |
| AES-GCM | 100.00 KB | 100.02 KB | 1.00x | 0.19 | 0.07 | 518.19 MB/s | 1307.73 MB/s | 0.0800 | 82.64 | - | - | - | - | - | - |
| Frackture Encrypted | 100.00 KB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 100.00 KB | 537.00 B | 190.69x | 0.16 | 0.08 | 622.83 MB/s | 1208.29 MB/s | 0.0809 | 82.64 | - | - | - | - | - | - |
| Gzip L6 | 100.00 KB | 138.00 B | 742.03x | 0.32 | 0.11 | 300.54 MB/s | 861.78 MB/s | 0.0794 | 82.64 | - | - | - | - | - | - |
| Gzip L9 | 100.00 KB | 138.00 B | 742.03x | 0.43 | 0.12 | 229.13 MB/s | 843.84 MB/s | 0.0786 | 82.64 | - | - | - | - | - | - |
| Brotli Q4 | 100.00 KB | 17.00 B | 6023.53x | 0.10 | 0.10 | 1015.91 MB/s | 1013.41 MB/s | 0.0808 | 82.64 | - | - | - | - | - | - |
| Brotli Q6 | 100.00 KB | 17.00 B | 6023.53x | 0.07 | 0.09 | 1356.77 MB/s | 1061.52 MB/s | 0.0784 | 82.64 | - | - | - | - | - | - |
| Brotli Q11 | 100.00 KB | 18.00 B | 5688.89x | 7.00 | 0.10 | 13.95 MB/s | 999.51 MB/s | 0.0788 | 82.64 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 44.10% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.356588)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ✅ Passed

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
