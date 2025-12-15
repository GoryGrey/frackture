# Frackture Benchmark Results

**Generated:** 2025-12-15 10:07:04
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
| Frackture | 100.00 KB | 65.00 B | 1575.38x | 7.22 | 0.23 | 13.52 MB/s | 429.93 MB/s | 0.0763 | 69.72 | 65 | ❌ | 0.337858 | 0.288574 | ❌ | ✅ |
| SHA256 | 100.00 KB | 64.00 B | 1600.00x | 0.07 | 0.00 | 1361.20 MB/s | 0.00 MB/s | 0.0717 | 69.72 | - | - | - | - | - | - |
| AES-GCM | 100.00 KB | 100.02 KB | 1.00x | 1.16 | 0.35 | 84.22 MB/s | 278.01 MB/s | 0.0733 | 70.28 | - | - | - | - | - | - |
| Frackture Encrypted | 100.00 KB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 100.00 KB | 22.38 KB | 4.47x | 0.85 | 0.41 | 114.43 MB/s | 238.04 MB/s | 0.0696 | 70.30 | - | - | - | - | - | - |
| Gzip L6 | 100.00 KB | 15.57 KB | 6.42x | 3.22 | 0.25 | 30.37 MB/s | 388.37 MB/s | 0.0712 | 70.30 | - | - | - | - | - | - |
| Gzip L9 | 100.00 KB | 15.08 KB | 6.63x | 14.12 | 0.26 | 6.92 MB/s | 374.13 MB/s | 0.0742 | 70.30 | - | - | - | - | - | - |
| Brotli Q4 | 100.00 KB | 20.32 KB | 4.92x | 2.04 | 0.23 | 47.93 MB/s | 427.66 MB/s | 0.0893 | 70.75 | - | - | - | - | - | - |
| Brotli Q6 | 100.00 KB | 16.63 KB | 6.01x | 3.15 | 0.17 | 31.01 MB/s | 562.27 MB/s | 0.0785 | 72.55 | - | - | - | - | - | - |
| Brotli Q11 | 100.00 KB | 13.90 KB | 7.20x | 148.87 | 0.19 | 0.66 MB/s | 505.78 MB/s | 0.0712 | 79.17 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 14.59% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.337858)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ✅ Passed

---

## Dataset: small_json

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 100.00 KB | 65.00 B | 1575.38x | 5.87 | 0.20 | 16.63 MB/s | 486.47 MB/s | 0.0683 | 80.11 | 65 | ❌ | 0.267007 | 0.171706 | ❌ | ✅ |
| SHA256 | 100.00 KB | 64.00 B | 1600.00x | 0.07 | 0.00 | 1394.85 MB/s | 0.00 MB/s | 0.0700 | 80.11 | - | - | - | - | - | - |
| AES-GCM | 100.00 KB | 100.02 KB | 1.00x | 0.14 | 0.08 | 676.26 MB/s | 1190.42 MB/s | 0.0738 | 80.11 | - | - | - | - | - | - |
| Frackture Encrypted | 100.00 KB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 100.00 KB | 13.57 KB | 7.37x | 0.47 | 0.24 | 206.95 MB/s | 402.02 MB/s | 0.0802 | 80.11 | - | - | - | - | - | - |
| Gzip L6 | 100.00 KB | 10.64 KB | 9.40x | 1.00 | 0.23 | 98.10 MB/s | 431.52 MB/s | 0.0734 | 80.11 | - | - | - | - | - | - |
| Gzip L9 | 100.00 KB | 9.92 KB | 10.08x | 4.08 | 0.20 | 23.96 MB/s | 496.68 MB/s | 0.0706 | 80.11 | - | - | - | - | - | - |
| Brotli Q4 | 100.00 KB | 8.82 KB | 11.34x | 0.73 | 0.13 | 133.70 MB/s | 765.96 MB/s | 0.0757 | 80.13 | - | - | - | - | - | - |
| Brotli Q6 | 100.00 KB | 7.85 KB | 12.74x | 1.92 | 0.12 | 50.76 MB/s | 817.58 MB/s | 0.0731 | 81.07 | - | - | - | - | - | - |
| Brotli Q11 | 100.00 KB | 6.49 KB | 15.41x | 151.41 | 0.11 | 0.64 MB/s | 878.85 MB/s | 0.0706 | 81.07 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 35.69% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.267007)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ✅ Passed

---

## Dataset: small_binary_blob

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 75.00 KB | 65.00 B | 1181.54x | 5.89 | 0.20 | 12.44 MB/s | 366.90 MB/s | 0.0610 | 81.07 | 65 | ❌ | 0.281424 | 0.156773 | ❌ | ✅ |
| SHA256 | 75.00 KB | 64.00 B | 1200.00x | 0.06 | 0.00 | 1272.70 MB/s | 0.00 MB/s | 0.0575 | 81.07 | - | - | - | - | - | - |
| AES-GCM | 75.00 KB | 75.02 KB | 1.00x | 0.14 | 0.08 | 525.34 MB/s | 942.72 MB/s | 0.0614 | 81.10 | - | - | - | - | - | - |
| Frackture Encrypted | 75.00 KB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 75.00 KB | 25.49 KB | 2.94x | 0.46 | 0.13 | 158.84 MB/s | 554.41 MB/s | 0.0543 | 81.10 | - | - | - | - | - | - |
| Gzip L6 | 75.00 KB | 25.29 KB | 2.97x | 0.59 | 0.15 | 124.09 MB/s | 495.32 MB/s | 0.0522 | 81.10 | - | - | - | - | - | - |
| Gzip L9 | 75.00 KB | 25.29 KB | 2.97x | 0.67 | 0.14 | 110.03 MB/s | 509.53 MB/s | 0.0527 | 81.10 | - | - | - | - | - | - |
| Brotli Q4 | 75.00 KB | 25.02 KB | 3.00x | 0.33 | 0.12 | 223.68 MB/s | 603.05 MB/s | 0.0559 | 81.10 | - | - | - | - | - | - |
| Brotli Q6 | 75.00 KB | 25.02 KB | 3.00x | 0.82 | 0.14 | 89.54 MB/s | 536.35 MB/s | 0.0527 | 81.11 | - | - | - | - | - | - |
| Brotli Q11 | 75.00 KB | 25.03 KB | 3.00x | 60.52 | 0.13 | 1.21 MB/s | 585.25 MB/s | 0.0530 | 81.53 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 44.29% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.281424)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ✅ Passed

---

## Dataset: small_random_noise

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 100.00 KB | 65.00 B | 1575.38x | 5.66 | 0.19 | 17.26 MB/s | 518.66 MB/s | 0.0711 | 81.53 | 65 | ❌ | 0.207524 | 0.132820 | ❌ | ✅ |
| SHA256 | 100.00 KB | 64.00 B | 1600.00x | 0.07 | 0.00 | 1384.39 MB/s | 0.00 MB/s | 0.0705 | 81.53 | - | - | - | - | - | - |
| AES-GCM | 100.00 KB | 100.02 KB | 1.00x | 0.13 | 0.07 | 766.33 MB/s | 1422.79 MB/s | 0.0749 | 81.53 | - | - | - | - | - | - |
| Frackture Encrypted | 100.00 KB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 100.00 KB | 100.05 KB | 1.00x | 2.12 | 0.07 | 46.05 MB/s | 1351.57 MB/s | 0.0743 | 81.53 | - | - | - | - | - | - |
| Gzip L6 | 100.00 KB | 100.05 KB | 1.00x | 2.10 | 0.06 | 46.43 MB/s | 1692.45 MB/s | 0.0686 | 81.53 | - | - | - | - | - | - |
| Gzip L9 | 100.00 KB | 100.05 KB | 1.00x | 2.02 | 0.06 | 48.23 MB/s | 1725.83 MB/s | 0.0687 | 81.53 | - | - | - | - | - | - |
| Brotli Q4 | 100.00 KB | 100.00 KB | 1.00x | 0.16 | 0.01 | 594.20 MB/s | 7359.17 MB/s | 0.0716 | 81.53 | - | - | - | - | - | - |
| Brotli Q6 | 100.00 KB | 100.00 KB | 1.00x | 0.83 | 0.02 | 117.69 MB/s | 6276.11 MB/s | 0.0731 | 81.71 | - | - | - | - | - | - |
| Brotli Q11 | 100.00 KB | 100.00 KB | 1.00x | 20.86 | 0.02 | 4.68 MB/s | 5429.27 MB/s | 0.0709 | 81.71 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 36.00% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.207524)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ✅ Passed

---

## Dataset: small_highly_repetitive

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 100.00 KB | 65.00 B | 1575.38x | 5.88 | 0.25 | 16.60 MB/s | 393.05 MB/s | 0.0740 | 81.71 | 65 | ❌ | 0.144186 | 0.138058 | ❌ | ✅ |
| SHA256 | 100.00 KB | 64.00 B | 1600.00x | 0.07 | 0.00 | 1347.33 MB/s | 0.00 MB/s | 0.0725 | 81.71 | - | - | - | - | - | - |
| AES-GCM | 100.00 KB | 100.02 KB | 1.00x | 0.23 | 0.10 | 426.62 MB/s | 959.67 MB/s | 0.0764 | 81.71 | - | - | - | - | - | - |
| Frackture Encrypted | 100.00 KB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 100.00 KB | 537.00 B | 190.69x | 0.15 | 0.07 | 641.58 MB/s | 1308.01 MB/s | 0.0729 | 81.71 | - | - | - | - | - | - |
| Gzip L6 | 100.00 KB | 138.00 B | 742.03x | 0.29 | 0.10 | 338.38 MB/s | 935.92 MB/s | 0.0764 | 81.71 | - | - | - | - | - | - |
| Gzip L9 | 100.00 KB | 138.00 B | 742.03x | 0.39 | 0.11 | 248.48 MB/s | 922.07 MB/s | 0.0767 | 81.71 | - | - | - | - | - | - |
| Brotli Q4 | 100.00 KB | 17.00 B | 6023.53x | 0.09 | 0.09 | 1033.59 MB/s | 1048.06 MB/s | 0.0787 | 81.71 | - | - | - | - | - | - |
| Brotli Q6 | 100.00 KB | 17.00 B | 6023.53x | 0.07 | 0.09 | 1443.76 MB/s | 1102.76 MB/s | 0.0769 | 81.71 | - | - | - | - | - | - |
| Brotli Q11 | 100.00 KB | 18.00 B | 5688.89x | 6.79 | 0.10 | 14.39 MB/s | 986.58 MB/s | 0.0752 | 81.71 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 4.25% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.144186)
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
