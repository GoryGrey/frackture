# Frackture Benchmark Results

**Generated:** 2025-12-15 10:30:06
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
- **Real datasets:** True
- **All tiers:** False

## Competition Summary (Frackture vs Gzip/Brotli)

| Scope | Total Comparisons | Wins (Ratio) | Win Rate (Ratio) | Wins (Throughput) | Win Rate (Throughput) |
|---|---:|---:|---:|---:|---:|
| Overall | 84 | 82 | 97.6% | 16 | 19.0% |

### Win Rates by Tier

| Tier | Total Comparisons | Wins (Ratio) | Win Rate (Ratio) |
|---|---:|---:|---:|
| large | 84 | 82 | 97.6% |

---

## Dataset: large_text_plain

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 1.00 MB | 65.00 B | 16131.94x | 7.84 | 0.28 | 127.50 MB/s | 3593.68 MB/s | 0.7921 | 87.11 | 65 | ❌ | 0.313108 | 0.244711 | ❌ | ✅ |
| SHA256 | 1.00 MB | 64.00 B | 16384.00x | 0.80 | 0.00 | 1257.51 MB/s | 0.00 MB/s | 0.7952 | 87.11 | - | - | - | - | - | - |
| AES-GCM | 1.00 MB | 1.00 MB | 1.00x | 1.74 | 0.79 | 574.01 MB/s | 1260.98 MB/s | 0.8103 | 87.54 | - | - | - | - | - | - |
| Frackture Encrypted | 1.00 MB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 1.00 MB | 11.11 KB | 92.13x | 1.84 | 1.23 | 542.21 MB/s | 812.75 MB/s | 0.7869 | 85.20 | - | - | - | - | - | - |
| Gzip L6 | 1.00 MB | 5.38 KB | 190.17x | 3.67 | 0.51 | 272.51 MB/s | 1953.17 MB/s | 0.7842 | 85.20 | - | - | - | - | - | - |
| Gzip L9 | 1.00 MB | 5.38 KB | 190.17x | 3.47 | 0.44 | 288.41 MB/s | 2274.57 MB/s | 0.7818 | 85.20 | - | - | - | - | - | - |
| Brotli Q4 | 1.00 MB | 367.00 B | 2857.16x | 3.52 | 1.10 | 283.71 MB/s | 905.46 MB/s | 0.8477 | 87.95 | - | - | - | - | - | - |
| Brotli Q6 | 1.00 MB | 395.00 B | 2654.62x | 2.28 | 1.09 | 437.90 MB/s | 916.63 MB/s | 0.7834 | 90.59 | - | - | - | - | - | - |
| Brotli Q11 | 1.00 MB | 318.00 B | 3297.41x | 17.04 | 0.97 | 58.70 MB/s | 1031.57 MB/s | 0.7617 | 88.59 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 21.84% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.313108)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: large_text_log

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 1.00 MB | 65.00 B | 16131.94x | 6.05 | 0.27 | 165.31 MB/s | 3704.65 MB/s | 0.7780 | 96.23 | 65 | ❌ | 0.199651 | 0.123128 | ❌ | ✅ |
| SHA256 | 1.00 MB | 64.00 B | 16384.00x | 0.78 | 0.00 | 1286.07 MB/s | 0.00 MB/s | 0.7776 | 96.23 | - | - | - | - | - | - |
| AES-GCM | 1.00 MB | 1.00 MB | 1.00x | 0.46 | 0.40 | 2153.67 MB/s | 2478.95 MB/s | 0.7778 | 96.23 | - | - | - | - | - | - |
| Frackture Encrypted | 1.00 MB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 1.00 MB | 9.86 KB | 103.87x | 1.78 | 0.55 | 560.36 MB/s | 1822.37 MB/s | 0.7826 | 96.23 | - | - | - | - | - | - |
| Gzip L6 | 1.00 MB | 6.03 KB | 169.78x | 3.93 | 0.76 | 254.53 MB/s | 1307.55 MB/s | 0.7879 | 96.23 | - | - | - | - | - | - |
| Gzip L9 | 1.00 MB | 5.23 KB | 195.92x | 4.34 | 0.45 | 230.17 MB/s | 2199.46 MB/s | 0.7828 | 96.23 | - | - | - | - | - | - |
| Brotli Q4 | 1.00 MB | 232.00 B | 4519.72x | 1.55 | 1.09 | 646.83 MB/s | 918.94 MB/s | 0.7730 | 96.30 | - | - | - | - | - | - |
| Brotli Q6 | 1.00 MB | 267.00 B | 3927.25x | 1.15 | 1.04 | 868.91 MB/s | 957.97 MB/s | 0.7915 | 96.54 | - | - | - | - | - | - |
| Brotli Q11 | 1.00 MB | 192.00 B | 5461.33x | 19.93 | 0.97 | 50.18 MB/s | 1027.74 MB/s | 0.7878 | 92.61 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 38.33% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.199651)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: large_text_json

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 1.00 MB | 65.00 B | 16131.94x | 6.10 | 0.24 | 163.81 MB/s | 4084.08 MB/s | 0.7750 | 96.24 | 65 | ❌ | 0.203007 | 0.142893 | ❌ | ✅ |
| SHA256 | 1.00 MB | 64.00 B | 16384.00x | 0.78 | 0.00 | 1284.25 MB/s | 0.00 MB/s | 0.7787 | 96.24 | - | - | - | - | - | - |
| AES-GCM | 1.00 MB | 1.00 MB | 1.00x | 0.57 | 0.55 | 1751.63 MB/s | 1815.89 MB/s | 0.7700 | 96.24 | - | - | - | - | - | - |
| Frackture Encrypted | 1.00 MB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 1.00 MB | 16.19 KB | 63.26x | 2.77 | 0.86 | 360.85 MB/s | 1166.16 MB/s | 1.0914 | 94.71 | - | - | - | - | - | - |
| Gzip L6 | 1.00 MB | 6.29 KB | 162.70x | 6.29 | 1.21 | 158.88 MB/s | 826.46 MB/s | 0.7849 | 94.75 | - | - | - | - | - | - |
| Gzip L9 | 1.00 MB | 5.35 KB | 191.49x | 4.01 | 0.58 | 249.51 MB/s | 1737.13 MB/s | 0.7830 | 94.75 | - | - | - | - | - | - |
| Brotli Q4 | 1.00 MB | 351.00 B | 2987.40x | 1.39 | 1.04 | 719.37 MB/s | 958.11 MB/s | 0.7854 | 94.81 | - | - | - | - | - | - |
| Brotli Q6 | 1.00 MB | 372.00 B | 2818.75x | 1.22 | 1.16 | 818.25 MB/s | 860.18 MB/s | 0.7851 | 95.18 | - | - | - | - | - | - |
| Brotli Q11 | 1.00 MB | 293.00 B | 3578.76x | 18.85 | 1.05 | 53.05 MB/s | 955.81 MB/s | 0.7786 | 91.13 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 29.61% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.203007)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: large_text_csv

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 1.00 MB | 65.00 B | 16131.94x | 6.42 | 0.32 | 155.68 MB/s | 3124.47 MB/s | 0.7760 | 95.19 | 65 | ❌ | 0.199575 | 0.188218 | ❌ | ✅ |
| SHA256 | 1.00 MB | 64.00 B | 16384.00x | 0.78 | 0.00 | 1287.56 MB/s | 0.00 MB/s | 0.7767 | 95.19 | - | - | - | - | - | - |
| AES-GCM | 1.00 MB | 1.00 MB | 1.00x | 0.48 | 0.42 | 2094.31 MB/s | 2387.08 MB/s | 0.8487 | 95.25 | - | - | - | - | - | - |
| Frackture Encrypted | 1.00 MB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 1.00 MB | 7.08 KB | 144.65x | 1.74 | 0.47 | 574.89 MB/s | 2133.02 MB/s | 0.7734 | 95.25 | - | - | - | - | - | - |
| Gzip L6 | 1.00 MB | 4.17 KB | 245.28x | 3.55 | 0.55 | 281.90 MB/s | 1832.73 MB/s | 0.8082 | 95.25 | - | - | - | - | - | - |
| Gzip L9 | 1.00 MB | 4.17 KB | 245.28x | 5.40 | 0.62 | 185.22 MB/s | 1625.62 MB/s | 0.8013 | 95.25 | - | - | - | - | - | - |
| Brotli Q4 | 1.00 MB | 171.00 B | 6132.02x | 1.62 | 1.80 | 617.83 MB/s | 554.32 MB/s | 0.8362 | 95.33 | - | - | - | - | - | - |
| Brotli Q6 | 1.00 MB | 195.00 B | 5377.31x | 1.64 | 1.29 | 608.71 MB/s | 774.98 MB/s | 0.8042 | 95.55 | - | - | - | - | - | - |
| Brotli Q11 | 1.00 MB | 151.00 B | 6944.21x | 22.07 | 1.61 | 45.31 MB/s | 620.89 MB/s | 0.8015 | 91.62 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 5.69% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.199575)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: large_binary_png

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 1.00 MB | 65.00 B | 16131.94x | 8.83 | 0.32 | 113.27 MB/s | 3107.07 MB/s | 0.7837 | 95.25 | 65 | ❌ | 0.126382 | 0.120252 | ❌ | ✅ |
| SHA256 | 1.00 MB | 64.00 B | 16384.00x | 0.77 | 0.00 | 1295.92 MB/s | 0.00 MB/s | 0.7717 | 95.25 | - | - | - | - | - | - |
| AES-GCM | 1.00 MB | 1.00 MB | 1.00x | 0.48 | 0.47 | 2091.49 MB/s | 2141.85 MB/s | 0.7757 | 95.25 | - | - | - | - | - | - |
| Frackture Encrypted | 1.00 MB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 1.00 MB | 7.30 KB | 140.18x | 1.78 | 0.48 | 562.22 MB/s | 2071.80 MB/s | 0.7791 | 95.25 | - | - | - | - | - | - |
| Gzip L6 | 1.00 MB | 3.59 KB | 285.56x | 3.51 | 0.52 | 284.71 MB/s | 1936.48 MB/s | 0.7788 | 95.25 | - | - | - | - | - | - |
| Gzip L9 | 1.00 MB | 3.59 KB | 285.56x | 3.61 | 0.51 | 277.26 MB/s | 1969.23 MB/s | 0.8433 | 95.25 | - | - | - | - | - | - |
| Brotli Q4 | 1.00 MB | 81.00 B | 12945.38x | 1.85 | 1.22 | 540.86 MB/s | 822.10 MB/s | 0.7964 | 96.07 | - | - | - | - | - | - |
| Brotli Q6 | 1.00 MB | 136.00 B | 7710.12x | 1.01 | 1.07 | 992.41 MB/s | 938.43 MB/s | 0.7848 | 96.13 | - | - | - | - | - | - |
| Brotli Q11 | 1.00 MB | 84.00 B | 12483.05x | 20.14 | 0.99 | 49.66 MB/s | 1012.71 MB/s | 0.7940 | 91.62 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 4.85% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.126382)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: large_binary_jpeg

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 1.00 MB | 65.00 B | 16131.94x | 6.13 | 0.24 | 163.23 MB/s | 4084.33 MB/s | 0.7956 | 95.25 | 65 | ❌ | 0.129295 | 0.122793 | ❌ | ✅ |
| SHA256 | 1.00 MB | 64.00 B | 16384.00x | 0.78 | 0.00 | 1275.57 MB/s | 0.00 MB/s | 0.7840 | 95.25 | - | - | - | - | - | - |
| AES-GCM | 1.00 MB | 1.00 MB | 1.00x | 0.55 | 0.49 | 1833.75 MB/s | 2054.67 MB/s | 0.7746 | 95.25 | - | - | - | - | - | - |
| Frackture Encrypted | 1.00 MB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 1.00 MB | 7.83 KB | 130.83x | 1.76 | 0.52 | 568.91 MB/s | 1941.03 MB/s | 0.8278 | 95.25 | - | - | - | - | - | - |
| Gzip L6 | 1.00 MB | 4.13 KB | 247.77x | 3.49 | 0.65 | 286.94 MB/s | 1526.91 MB/s | 0.7742 | 95.25 | - | - | - | - | - | - |
| Gzip L9 | 1.00 MB | 4.13 KB | 247.77x | 3.70 | 0.46 | 270.53 MB/s | 2191.03 MB/s | 0.7798 | 95.25 | - | - | - | - | - | - |
| Brotli Q4 | 1.00 MB | 121.00 B | 8665.92x | 1.69 | 1.04 | 593.43 MB/s | 965.84 MB/s | 0.7793 | 96.07 | - | - | - | - | - | - |
| Brotli Q6 | 1.00 MB | 171.00 B | 6132.02x | 1.05 | 1.04 | 950.09 MB/s | 964.50 MB/s | 0.7845 | 96.18 | - | - | - | - | - | - |
| Brotli Q11 | 1.00 MB | 132.00 B | 7943.76x | 19.69 | 1.51 | 50.79 MB/s | 664.19 MB/s | 0.8030 | 91.62 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 5.03% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.129295)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: large_binary_pdf

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 1.00 MB | 65.00 B | 16131.94x | 6.06 | 0.25 | 165.09 MB/s | 4008.19 MB/s | 0.7816 | 95.25 | 65 | ❌ | 0.159119 | 0.149942 | ❌ | ✅ |
| SHA256 | 1.00 MB | 64.00 B | 16384.00x | 0.77 | 0.00 | 1298.55 MB/s | 0.00 MB/s | 0.7701 | 95.25 | - | - | - | - | - | - |
| AES-GCM | 1.00 MB | 1.00 MB | 1.00x | 0.58 | 0.54 | 1731.91 MB/s | 1847.60 MB/s | 0.7970 | 95.25 | - | - | - | - | - | - |
| Frackture Encrypted | 1.00 MB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 1.00 MB | 12.81 KB | 79.96x | 1.88 | 0.56 | 531.16 MB/s | 1771.32 MB/s | 0.8295 | 95.25 | - | - | - | - | - | - |
| Gzip L6 | 1.00 MB | 4.77 KB | 214.56x | 4.21 | 0.46 | 237.26 MB/s | 2155.31 MB/s | 0.8357 | 95.25 | - | - | - | - | - | - |
| Gzip L9 | 1.00 MB | 4.77 KB | 214.56x | 3.52 | 0.45 | 283.70 MB/s | 2229.74 MB/s | 0.8182 | 95.25 | - | - | - | - | - | - |
| Brotli Q4 | 1.00 MB | 270.00 B | 3883.61x | 2.56 | 1.84 | 391.22 MB/s | 542.26 MB/s | 0.8228 | 96.07 | - | - | - | - | - | - |
| Brotli Q6 | 1.00 MB | 308.00 B | 3404.47x | 1.82 | 1.87 | 550.71 MB/s | 535.40 MB/s | 0.8395 | 96.36 | - | - | - | - | - | - |
| Brotli Q11 | 1.00 MB | 232.00 B | 4519.72x | 19.60 | 1.03 | 51.02 MB/s | 971.09 MB/s | 0.7995 | 91.62 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 5.77% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.159119)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: large_binary_gif

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 1.00 MB | 65.00 B | 16131.94x | 8.96 | 0.25 | 111.56 MB/s | 4044.39 MB/s | 0.7881 | 95.25 | 65 | ❌ | 0.136235 | 0.136235 | ❌ | ✅ |
| SHA256 | 1.00 MB | 64.00 B | 16384.00x | 0.78 | 0.00 | 1274.37 MB/s | 0.00 MB/s | 0.7847 | 95.25 | - | - | - | - | - | - |
| AES-GCM | 1.00 MB | 1.00 MB | 1.00x | 0.59 | 0.43 | 1695.37 MB/s | 2299.87 MB/s | 0.7824 | 95.25 | - | - | - | - | - | - |
| Frackture Encrypted | 1.00 MB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 1.00 MB | 4.54 KB | 225.60x | 1.68 | 0.46 | 596.50 MB/s | 2170.71 MB/s | 0.7784 | 95.25 | - | - | - | - | - | - |
| Gzip L6 | 1.00 MB | 3.05 KB | 335.76x | 3.43 | 0.70 | 291.18 MB/s | 1437.57 MB/s | 0.7785 | 95.25 | - | - | - | - | - | - |
| Gzip L9 | 1.00 MB | 3.05 KB | 335.76x | 3.67 | 0.69 | 272.83 MB/s | 1452.93 MB/s | 0.7757 | 95.25 | - | - | - | - | - | - |
| Brotli Q4 | 1.00 MB | 47.00 B | 22310.13x | 1.70 | 1.10 | 586.68 MB/s | 910.40 MB/s | 0.7793 | 96.07 | - | - | - | - | - | - |
| Brotli Q6 | 1.00 MB | 99.00 B | 10591.68x | 0.99 | 1.01 | 1005.90 MB/s | 988.37 MB/s | 0.7787 | 96.11 | - | - | - | - | - | - |
| Brotli Q11 | 1.00 MB | 51.00 B | 20560.31x | 19.03 | 1.02 | 52.54 MB/s | 978.24 MB/s | 0.7736 | 91.62 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 0.00% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.136235)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: large_structured_sqlite

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 1.00 MB | 65.00 B | 16131.94x | 6.06 | 0.24 | 165.14 MB/s | 4227.40 MB/s | 0.7839 | 95.25 | 65 | ❌ | 0.043278 | 0.043278 | ❌ | ✅ |
| SHA256 | 1.00 MB | 64.00 B | 16384.00x | 0.77 | 0.00 | 1294.30 MB/s | 0.00 MB/s | 0.7726 | 95.25 | - | - | - | - | - | - |
| AES-GCM | 1.00 MB | 1.00 MB | 1.00x | 0.51 | 0.40 | 1953.80 MB/s | 2524.39 MB/s | 0.7774 | 95.25 | - | - | - | - | - | - |
| Frackture Encrypted | 1.00 MB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 1.00 MB | 6.34 KB | 161.57x | 1.70 | 0.70 | 588.11 MB/s | 1429.62 MB/s | 0.7788 | 95.25 | - | - | - | - | - | - |
| Gzip L6 | 1.00 MB | 2.47 KB | 414.95x | 3.55 | 0.75 | 281.98 MB/s | 1341.32 MB/s | 0.7745 | 95.25 | - | - | - | - | - | - |
| Gzip L9 | 1.00 MB | 2.47 KB | 414.95x | 6.53 | 1.09 | 153.24 MB/s | 919.12 MB/s | 0.7742 | 95.25 | - | - | - | - | - | - |
| Brotli Q4 | 1.00 MB | 522.00 B | 2008.77x | 1.91 | 1.06 | 522.99 MB/s | 943.02 MB/s | 0.7741 | 96.07 | - | - | - | - | - | - |
| Brotli Q6 | 1.00 MB | 530.00 B | 1978.45x | 1.40 | 1.03 | 715.26 MB/s | 973.09 MB/s | 0.7830 | 96.49 | - | - | - | - | - | - |
| Brotli Q11 | 1.00 MB | 392.00 B | 2674.94x | 21.90 | 2.08 | 45.65 MB/s | 481.86 MB/s | 0.7833 | 85.79 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 0.00% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.043278)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: large_structured_pickle

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 1.00 MB | 65.00 B | 16131.94x | 6.01 | 0.23 | 166.50 MB/s | 4270.37 MB/s | 0.7842 | 95.25 | 65 | ❌ | 0.212640 | 0.180567 | ❌ | ✅ |
| SHA256 | 1.00 MB | 64.00 B | 16384.00x | 0.78 | 0.00 | 1289.23 MB/s | 0.00 MB/s | 0.7757 | 95.25 | - | - | - | - | - | - |
| AES-GCM | 1.00 MB | 1.00 MB | 1.00x | 0.47 | 0.54 | 2129.69 MB/s | 1846.05 MB/s | 0.7812 | 95.25 | - | - | - | - | - | - |
| Frackture Encrypted | 1.00 MB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 1.00 MB | 8.90 KB | 115.08x | 1.85 | 0.47 | 540.29 MB/s | 2132.46 MB/s | 0.7797 | 95.25 | - | - | - | - | - | - |
| Gzip L6 | 1.00 MB | 4.15 KB | 246.72x | 3.47 | 0.45 | 288.54 MB/s | 2233.90 MB/s | 0.7820 | 95.25 | - | - | - | - | - | - |
| Gzip L9 | 1.00 MB | 4.15 KB | 246.72x | 3.47 | 0.45 | 288.12 MB/s | 2198.15 MB/s | 0.7729 | 95.25 | - | - | - | - | - | - |
| Brotli Q4 | 1.00 MB | 149.00 B | 7037.42x | 1.59 | 0.98 | 629.00 MB/s | 1022.47 MB/s | 0.7972 | 96.07 | - | - | - | - | - | - |
| Brotli Q6 | 1.00 MB | 195.00 B | 5377.31x | 1.10 | 1.01 | 912.00 MB/s | 987.89 MB/s | 0.7814 | 96.23 | - | - | - | - | - | - |
| Brotli Q11 | 1.00 MB | 139.00 B | 7543.71x | 18.28 | 2.19 | 54.72 MB/s | 456.03 MB/s | 0.7730 | 86.04 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 15.08% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.212640)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: large_code_javascript

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 1.00 MB | 65.00 B | 16131.94x | 5.98 | 0.24 | 167.36 MB/s | 4224.85 MB/s | 0.7825 | 95.25 | 65 | ❌ | 0.210678 | 0.176264 | ❌ | ✅ |
| SHA256 | 1.00 MB | 64.00 B | 16384.00x | 0.78 | 0.00 | 1286.08 MB/s | 0.00 MB/s | 0.7776 | 95.25 | - | - | - | - | - | - |
| AES-GCM | 1.00 MB | 1.00 MB | 1.00x | 0.50 | 0.38 | 2000.63 MB/s | 2654.75 MB/s | 0.7770 | 95.25 | - | - | - | - | - | - |
| Frackture Encrypted | 1.00 MB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 1.00 MB | 9.47 KB | 108.09x | 1.74 | 0.55 | 574.76 MB/s | 1810.82 MB/s | 0.7778 | 95.25 | - | - | - | - | - | - |
| Gzip L6 | 1.00 MB | 5.29 KB | 193.68x | 4.16 | 0.47 | 240.46 MB/s | 2120.10 MB/s | 0.7798 | 95.25 | - | - | - | - | - | - |
| Gzip L9 | 1.00 MB | 5.29 KB | 193.68x | 4.74 | 0.51 | 210.86 MB/s | 1958.35 MB/s | 0.7830 | 95.25 | - | - | - | - | - | - |
| Brotli Q4 | 1.00 MB | 304.00 B | 3449.26x | 1.66 | 0.99 | 601.58 MB/s | 1008.89 MB/s | 0.7709 | 96.07 | - | - | - | - | - | - |
| Brotli Q6 | 1.00 MB | 309.00 B | 3393.45x | 1.19 | 0.99 | 843.75 MB/s | 1013.83 MB/s | 0.7769 | 96.37 | - | - | - | - | - | - |
| Brotli Q11 | 1.00 MB | 236.00 B | 4443.12x | 18.28 | 2.30 | 54.69 MB/s | 434.34 MB/s | 0.7781 | 86.04 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 16.33% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.210678)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: large_code_javascript_minified

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 1.00 MB | 65.00 B | 16131.94x | 6.18 | 0.23 | 161.73 MB/s | 4343.33 MB/s | 0.7748 | 95.25 | 65 | ❌ | 0.248601 | 0.216233 | ❌ | ✅ |
| SHA256 | 1.00 MB | 64.00 B | 16384.00x | 0.77 | 0.00 | 1303.19 MB/s | 0.00 MB/s | 0.7673 | 95.25 | - | - | - | - | - | - |
| AES-GCM | 1.00 MB | 1.00 MB | 1.00x | 0.53 | 0.40 | 1895.90 MB/s | 2474.08 MB/s | 0.7779 | 95.25 | - | - | - | - | - | - |
| Frackture Encrypted | 1.00 MB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 1.00 MB | 8.02 KB | 127.69x | 1.79 | 0.46 | 559.42 MB/s | 2152.52 MB/s | 0.7782 | 95.25 | - | - | - | - | - | - |
| Gzip L6 | 1.00 MB | 4.18 KB | 245.22x | 3.49 | 0.44 | 286.75 MB/s | 2262.97 MB/s | 0.7793 | 95.25 | - | - | - | - | - | - |
| Gzip L9 | 1.00 MB | 4.18 KB | 245.22x | 3.50 | 0.54 | 285.98 MB/s | 1841.59 MB/s | 0.8091 | 95.25 | - | - | - | - | - | - |
| Brotli Q4 | 1.00 MB | 180.00 B | 5825.42x | 1.66 | 1.28 | 600.91 MB/s | 781.89 MB/s | 0.7949 | 96.07 | - | - | - | - | - | - |
| Brotli Q6 | 1.00 MB | 224.00 B | 4681.14x | 1.10 | 1.02 | 911.49 MB/s | 984.45 MB/s | 0.7826 | 96.27 | - | - | - | - | - | - |
| Brotli Q11 | 1.00 MB | 165.00 B | 6355.01x | 17.17 | 2.14 | 58.23 MB/s | 467.52 MB/s | 0.7854 | 86.04 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 13.02% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.248601)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: large_code_python

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 1.00 MB | 65.00 B | 16131.94x | 6.35 | 0.24 | 157.58 MB/s | 4169.50 MB/s | 0.7870 | 95.26 | 65 | ❌ | 0.201540 | 0.173739 | ❌ | ✅ |
| SHA256 | 1.00 MB | 64.00 B | 16384.00x | 0.77 | 0.00 | 1304.20 MB/s | 0.00 MB/s | 0.7668 | 95.26 | - | - | - | - | - | - |
| AES-GCM | 1.00 MB | 1.00 MB | 1.00x | 0.49 | 0.59 | 2043.52 MB/s | 1700.24 MB/s | 0.7760 | 95.26 | - | - | - | - | - | - |
| Frackture Encrypted | 1.00 MB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 1.00 MB | 21.20 KB | 48.31x | 2.19 | 0.70 | 457.31 MB/s | 1438.42 MB/s | 0.7789 | 95.26 | - | - | - | - | - | - |
| Gzip L6 | 1.00 MB | 8.10 KB | 126.47x | 4.02 | 0.54 | 248.50 MB/s | 1863.17 MB/s | 0.7832 | 95.26 | - | - | - | - | - | - |
| Gzip L9 | 1.00 MB | 6.06 KB | 169.10x | 4.47 | 0.44 | 223.83 MB/s | 2259.21 MB/s | 0.7781 | 95.26 | - | - | - | - | - | - |
| Brotli Q4 | 1.00 MB | 574.00 B | 1826.79x | 1.71 | 1.08 | 583.94 MB/s | 926.46 MB/s | 0.7739 | 96.07 | - | - | - | - | - | - |
| Brotli Q6 | 1.00 MB | 575.00 B | 1823.61x | 1.33 | 1.04 | 752.34 MB/s | 958.31 MB/s | 0.7744 | 96.57 | - | - | - | - | - | - |
| Brotli Q11 | 1.00 MB | 491.00 B | 2135.59x | 19.34 | 2.08 | 51.69 MB/s | 480.38 MB/s | 0.7823 | 86.04 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 13.79% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.201540)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: large_mixed_payload

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 1.00 MB | 65.00 B | 16131.94x | 5.97 | 0.24 | 167.44 MB/s | 4234.96 MB/s | 0.7983 | 95.26 | 65 | ❌ | 0.067139 | 0.050524 | ❌ | ✅ |
| SHA256 | 1.00 MB | 64.00 B | 16384.00x | 0.78 | 0.00 | 1289.61 MB/s | 0.00 MB/s | 0.7754 | 95.26 | - | - | - | - | - | - |
| AES-GCM | 1.00 MB | 1.00 MB | 1.00x | 0.47 | 0.55 | 2112.95 MB/s | 1802.31 MB/s | 0.7813 | 95.26 | - | - | - | - | - | - |
| Frackture Encrypted | 1.00 MB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 1.00 MB | 26.07 KB | 39.28x | 2.25 | 0.77 | 444.23 MB/s | 1300.51 MB/s | 0.7750 | 95.26 | - | - | - | - | - | - |
| Gzip L6 | 1.00 MB | 6.63 KB | 154.52x | 3.66 | 0.54 | 273.29 MB/s | 1843.53 MB/s | 0.7884 | 95.26 | - | - | - | - | - | - |
| Gzip L9 | 1.00 MB | 6.63 KB | 154.52x | 3.66 | 0.56 | 273.41 MB/s | 1772.00 MB/s | 0.7730 | 95.26 | - | - | - | - | - | - |
| Brotli Q4 | 1.00 MB | 1.13 KB | 904.72x | 1.73 | 1.02 | 578.15 MB/s | 975.81 MB/s | 0.7722 | 96.07 | - | - | - | - | - | - |
| Brotli Q6 | 1.00 MB | 1.01 KB | 1009.22x | 1.60 | 1.06 | 623.57 MB/s | 942.06 MB/s | 0.7786 | 96.84 | - | - | - | - | - | - |
| Brotli Q11 | 1.00 MB | 900.00 B | 1165.08x | 20.63 | 2.28 | 48.47 MB/s | 439.53 MB/s | 0.8039 | 86.04 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 24.75% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.067139)
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
