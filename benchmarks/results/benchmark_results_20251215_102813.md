# Frackture Benchmark Results

**Generated:** 2025-12-15 10:28:13
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
| Overall | 84 | 81 | 96.4% | 6 | 7.1% |

### Win Rates by Tier

| Tier | Total Comparisons | Wins (Ratio) | Win Rate (Ratio) |
|---|---:|---:|---:|
| medium | 84 | 81 | 96.4% |

---

## Dataset: small_text_plain

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 100.00 KB | 65.00 B | 1575.38x | 7.95 | 0.28 | 12.29 MB/s | 353.58 MB/s | 0.0813 | 69.59 | 65 | ❌ | 0.313108 | 0.244711 | ❌ | ✅ |
| SHA256 | 100.00 KB | 64.00 B | 1600.00x | 0.08 | 0.00 | 1268.61 MB/s | 0.00 MB/s | 0.0770 | 69.59 | - | - | - | - | - | - |
| AES-GCM | 100.00 KB | 100.02 KB | 1.00x | 1.37 | 0.45 | 71.27 MB/s | 218.96 MB/s | 0.0805 | 70.24 | - | - | - | - | - | - |
| Frackture Encrypted | 100.00 KB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 100.00 KB | 1.29 KB | 77.40x | 0.27 | 0.15 | 366.14 MB/s | 658.78 MB/s | 0.0828 | 70.19 | - | - | - | - | - | - |
| Gzip L6 | 100.00 KB | 931.00 B | 109.99x | 0.43 | 0.09 | 228.70 MB/s | 1107.83 MB/s | 0.0787 | 70.21 | - | - | - | - | - | - |
| Gzip L9 | 100.00 KB | 931.00 B | 109.99x | 0.33 | 0.07 | 297.10 MB/s | 1330.30 MB/s | 0.0825 | 70.21 | - | - | - | - | - | - |
| Brotli Q4 | 100.00 KB | 353.00 B | 290.08x | 1.58 | 0.14 | 61.76 MB/s | 701.10 MB/s | 0.0808 | 70.71 | - | - | - | - | - | - |
| Brotli Q6 | 100.00 KB | 348.00 B | 294.25x | 1.36 | 0.17 | 71.96 MB/s | 589.75 MB/s | 0.0907 | 72.65 | - | - | - | - | - | - |
| Brotli Q11 | 100.00 KB | 318.00 B | 322.01x | 8.87 | 0.17 | 11.01 MB/s | 575.37 MB/s | 0.0801 | 76.45 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 21.84% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.313108)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: small_text_log

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 100.00 KB | 65.00 B | 1575.38x | 7.71 | 0.34 | 12.66 MB/s | 285.15 MB/s | 0.0815 | 77.26 | 65 | ❌ | 0.199651 | 0.123128 | ❌ | ✅ |
| SHA256 | 100.00 KB | 64.00 B | 1600.00x | 0.09 | 0.00 | 1048.32 MB/s | 0.00 MB/s | 0.0932 | 77.26 | - | - | - | - | - | - |
| AES-GCM | 100.00 KB | 100.02 KB | 1.00x | 0.16 | 0.09 | 595.06 MB/s | 1132.89 MB/s | 0.0805 | 77.26 | - | - | - | - | - | - |
| Frackture Encrypted | 100.00 KB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 100.00 KB | 1.26 KB | 79.56x | 0.24 | 0.11 | 413.49 MB/s | 926.58 MB/s | 0.0790 | 77.34 | - | - | - | - | - | - |
| Gzip L6 | 100.00 KB | 877.00 B | 116.76x | 0.37 | 0.08 | 262.67 MB/s | 1207.24 MB/s | 0.0823 | 77.34 | - | - | - | - | - | - |
| Gzip L9 | 100.00 KB | 768.00 B | 133.33x | 0.43 | 0.14 | 224.94 MB/s | 689.14 MB/s | 0.0799 | 77.34 | - | - | - | - | - | - |
| Brotli Q4 | 100.00 KB | 228.00 B | 449.12x | 0.28 | 0.11 | 349.43 MB/s | 878.18 MB/s | 0.0809 | 77.43 | - | - | - | - | - | - |
| Brotli Q6 | 100.00 KB | 207.00 B | 494.69x | 0.31 | 0.10 | 319.47 MB/s | 951.57 MB/s | 0.0831 | 77.77 | - | - | - | - | - | - |
| Brotli Q11 | 100.00 KB | 192.00 B | 533.33x | 5.99 | 0.11 | 16.29 MB/s | 878.53 MB/s | 0.0831 | 77.86 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 38.33% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.199651)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: small_text_json

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 100.00 KB | 65.00 B | 1575.38x | 6.50 | 0.24 | 15.02 MB/s | 411.05 MB/s | 0.0783 | 77.87 | 65 | ❌ | 0.203007 | 0.142893 | ❌ | ✅ |
| SHA256 | 100.00 KB | 64.00 B | 1600.00x | 0.08 | 0.00 | 1268.21 MB/s | 0.00 MB/s | 0.0770 | 77.87 | - | - | - | - | - | - |
| AES-GCM | 100.00 KB | 100.02 KB | 1.00x | 0.18 | 0.08 | 541.51 MB/s | 1153.80 MB/s | 0.0786 | 77.87 | - | - | - | - | - | - |
| Frackture Encrypted | 100.00 KB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 100.00 KB | 1.93 KB | 51.90x | 0.32 | 0.12 | 308.33 MB/s | 837.20 MB/s | 0.0793 | 77.91 | - | - | - | - | - | - |
| Gzip L6 | 100.00 KB | 1004.00 B | 101.99x | 0.42 | 0.09 | 231.50 MB/s | 1078.87 MB/s | 0.0804 | 77.91 | - | - | - | - | - | - |
| Gzip L9 | 100.00 KB | 892.00 B | 114.80x | 0.58 | 0.11 | 169.29 MB/s | 862.38 MB/s | 0.0814 | 77.91 | - | - | - | - | - | - |
| Brotli Q4 | 100.00 KB | 338.00 B | 302.96x | 0.23 | 0.11 | 427.16 MB/s | 875.47 MB/s | 0.0830 | 77.96 | - | - | - | - | - | - |
| Brotli Q6 | 100.00 KB | 317.00 B | 323.03x | 0.35 | 0.10 | 277.95 MB/s | 942.97 MB/s | 0.0794 | 78.26 | - | - | - | - | - | - |
| Brotli Q11 | 100.00 KB | 293.00 B | 349.49x | 6.27 | 0.13 | 15.58 MB/s | 762.21 MB/s | 0.0793 | 78.31 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 29.61% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.203007)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: small_text_csv

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 100.00 KB | 65.00 B | 1575.38x | 7.12 | 0.33 | 13.71 MB/s | 292.33 MB/s | 0.0819 | 78.31 | 65 | ❌ | 0.199575 | 0.188218 | ❌ | ✅ |
| SHA256 | 100.00 KB | 64.00 B | 1600.00x | 0.08 | 0.00 | 1264.50 MB/s | 0.00 MB/s | 0.0772 | 78.31 | - | - | - | - | - | - |
| AES-GCM | 100.00 KB | 100.02 KB | 1.00x | 0.15 | 0.08 | 647.58 MB/s | 1184.06 MB/s | 0.0814 | 78.31 | - | - | - | - | - | - |
| Frackture Encrypted | 100.00 KB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 100.00 KB | 966.00 B | 106.00x | 0.21 | 0.09 | 468.61 MB/s | 1043.80 MB/s | 0.0800 | 78.31 | - | - | - | - | - | - |
| Gzip L6 | 100.00 KB | 607.00 B | 168.70x | 0.34 | 0.07 | 286.94 MB/s | 1425.49 MB/s | 0.0812 | 78.31 | - | - | - | - | - | - |
| Gzip L9 | 100.00 KB | 607.00 B | 168.70x | 0.38 | 0.07 | 260.20 MB/s | 1461.09 MB/s | 0.0793 | 78.31 | - | - | - | - | - | - |
| Brotli Q4 | 100.00 KB | 164.00 B | 624.39x | 0.22 | 0.11 | 446.71 MB/s | 906.88 MB/s | 0.0798 | 78.38 | - | - | - | - | - | - |
| Brotli Q6 | 100.00 KB | 158.00 B | 648.10x | 0.17 | 0.12 | 584.76 MB/s | 789.00 MB/s | 0.0801 | 78.49 | - | - | - | - | - | - |
| Brotli Q11 | 100.00 KB | 151.00 B | 678.15x | 4.64 | 0.17 | 21.03 MB/s | 588.22 MB/s | 0.0814 | 78.54 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 5.69% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.199575)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: small_binary_png

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 100.00 KB | 65.00 B | 1575.38x | 5.97 | 0.22 | 16.37 MB/s | 447.30 MB/s | 0.0812 | 78.54 | 65 | ❌ | 0.126382 | 0.120252 | ❌ | ✅ |
| SHA256 | 100.00 KB | 64.00 B | 1600.00x | 0.08 | 0.00 | 1215.99 MB/s | 0.00 MB/s | 0.0803 | 78.54 | - | - | - | - | - | - |
| AES-GCM | 100.00 KB | 100.02 KB | 1.00x | 0.21 | 0.09 | 475.30 MB/s | 1090.10 MB/s | 0.0855 | 78.54 | - | - | - | - | - | - |
| Frackture Encrypted | 100.00 KB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 100.00 KB | 857.00 B | 119.49x | 0.33 | 0.14 | 297.46 MB/s | 681.85 MB/s | 0.0852 | 78.54 | - | - | - | - | - | - |
| Gzip L6 | 100.00 KB | 464.00 B | 220.69x | 0.47 | 0.13 | 209.70 MB/s | 773.23 MB/s | 0.0860 | 78.54 | - | - | - | - | - | - |
| Gzip L9 | 100.00 KB | 464.00 B | 220.69x | 0.50 | 0.13 | 195.46 MB/s | 773.34 MB/s | 0.0864 | 78.54 | - | - | - | - | - | - |
| Brotli Q4 | 100.00 KB | 82.00 B | 1248.78x | 0.25 | 0.11 | 384.78 MB/s | 923.76 MB/s | 0.0808 | 78.59 | - | - | - | - | - | - |
| Brotli Q6 | 100.00 KB | 90.00 B | 1137.78x | 0.19 | 0.14 | 525.25 MB/s | 700.31 MB/s | 0.0877 | 78.64 | - | - | - | - | - | - |
| Brotli Q11 | 100.00 KB | 84.00 B | 1219.05x | 6.15 | 0.14 | 15.88 MB/s | 700.15 MB/s | 0.0873 | 78.70 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 4.85% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.126382)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: small_binary_jpeg

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 100.00 KB | 65.00 B | 1575.38x | 9.59 | 0.32 | 10.18 MB/s | 302.67 MB/s | 0.0787 | 78.70 | 65 | ❌ | 0.129295 | 0.122793 | ❌ | ✅ |
| SHA256 | 100.00 KB | 64.00 B | 1600.00x | 0.08 | 0.00 | 1287.09 MB/s | 0.00 MB/s | 0.0759 | 78.70 | - | - | - | - | - | - |
| AES-GCM | 100.00 KB | 100.02 KB | 1.00x | 0.16 | 0.13 | 615.06 MB/s | 779.93 MB/s | 0.0811 | 78.70 | - | - | - | - | - | - |
| Frackture Encrypted | 100.00 KB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 100.00 KB | 957.00 B | 107.00x | 0.23 | 0.09 | 431.11 MB/s | 1076.20 MB/s | 0.0810 | 78.70 | - | - | - | - | - | - |
| Gzip L6 | 100.00 KB | 565.00 B | 181.24x | 0.34 | 0.08 | 290.02 MB/s | 1228.10 MB/s | 0.0826 | 78.70 | - | - | - | - | - | - |
| Gzip L9 | 100.00 KB | 565.00 B | 181.24x | 0.31 | 0.07 | 314.69 MB/s | 1438.96 MB/s | 0.0808 | 78.70 | - | - | - | - | - | - |
| Brotli Q4 | 100.00 KB | 117.00 B | 875.21x | 0.18 | 0.11 | 540.91 MB/s | 882.95 MB/s | 0.0808 | 78.76 | - | - | - | - | - | - |
| Brotli Q6 | 100.00 KB | 129.00 B | 793.80x | 0.15 | 0.10 | 632.52 MB/s | 972.49 MB/s | 0.0817 | 78.84 | - | - | - | - | - | - |
| Brotli Q11 | 100.00 KB | 132.00 B | 775.76x | 4.50 | 0.11 | 21.69 MB/s | 878.74 MB/s | 0.0855 | 78.89 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 5.03% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.129295)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: small_binary_pdf

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 100.00 KB | 65.00 B | 1575.38x | 6.24 | 0.23 | 15.66 MB/s | 429.49 MB/s | 0.0818 | 78.89 | 65 | ❌ | 0.159119 | 0.149942 | ❌ | ✅ |
| SHA256 | 100.00 KB | 64.00 B | 1600.00x | 0.08 | 0.00 | 1179.12 MB/s | 0.00 MB/s | 0.0828 | 78.89 | - | - | - | - | - | - |
| AES-GCM | 100.00 KB | 100.02 KB | 1.00x | 0.20 | 0.12 | 481.82 MB/s | 848.03 MB/s | 0.0833 | 78.89 | - | - | - | - | - | - |
| Frackture Encrypted | 100.00 KB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 100.00 KB | 1.46 KB | 68.59x | 0.21 | 0.10 | 459.78 MB/s | 987.15 MB/s | 0.0814 | 78.89 | - | - | - | - | - | - |
| Gzip L6 | 100.00 KB | 762.00 B | 134.38x | 0.44 | 0.08 | 222.63 MB/s | 1272.53 MB/s | 0.0823 | 78.89 | - | - | - | - | - | - |
| Gzip L9 | 100.00 KB | 762.00 B | 134.38x | 0.70 | 0.09 | 138.89 MB/s | 1089.51 MB/s | 0.0799 | 78.89 | - | - | - | - | - | - |
| Brotli Q4 | 100.00 KB | 269.00 B | 380.67x | 0.23 | 0.11 | 430.96 MB/s | 906.24 MB/s | 0.0785 | 78.96 | - | - | - | - | - | - |
| Brotli Q6 | 100.00 KB | 253.00 B | 404.74x | 0.20 | 0.10 | 500.54 MB/s | 989.78 MB/s | 0.0804 | 79.05 | - | - | - | - | - | - |
| Brotli Q11 | 100.00 KB | 232.00 B | 441.38x | 5.68 | 0.11 | 17.20 MB/s | 858.09 MB/s | 0.0803 | 79.11 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 5.77% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.159119)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: small_binary_gif

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 100.00 KB | 65.00 B | 1575.38x | 5.83 | 0.25 | 16.76 MB/s | 393.72 MB/s | 0.0839 | 79.11 | 65 | ❌ | 0.136235 | 0.136235 | ❌ | ✅ |
| SHA256 | 100.00 KB | 64.00 B | 1600.00x | 0.08 | 0.00 | 1254.87 MB/s | 0.00 MB/s | 0.0778 | 79.11 | - | - | - | - | - | - |
| AES-GCM | 100.00 KB | 100.02 KB | 1.00x | 0.15 | 0.11 | 658.19 MB/s | 854.37 MB/s | 0.0912 | 79.11 | - | - | - | - | - | - |
| Frackture Encrypted | 100.00 KB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 100.00 KB | 522.00 B | 196.17x | 0.23 | 0.13 | 416.45 MB/s | 780.29 MB/s | 0.0882 | 79.11 | - | - | - | - | - | - |
| Gzip L6 | 100.00 KB | 372.00 B | 275.27x | 0.52 | 0.17 | 186.93 MB/s | 577.95 MB/s | 0.0881 | 79.11 | - | - | - | - | - | - |
| Gzip L9 | 100.00 KB | 372.00 B | 275.27x | 0.52 | 0.20 | 188.37 MB/s | 493.63 MB/s | 0.0851 | 79.11 | - | - | - | - | - | - |
| Brotli Q4 | 100.00 KB | 51.00 B | 2007.84x | 0.20 | 0.15 | 486.76 MB/s | 667.51 MB/s | 0.0869 | 79.16 | - | - | - | - | - | - |
| Brotli Q6 | 100.00 KB | 60.00 B | 1706.67x | 0.20 | 0.17 | 498.94 MB/s | 561.07 MB/s | 0.0872 | 79.21 | - | - | - | - | - | - |
| Brotli Q11 | 100.00 KB | 51.00 B | 2007.84x | 6.00 | 0.11 | 16.27 MB/s | 912.13 MB/s | 0.0857 | 79.25 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 0.00% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.136235)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: small_structured_sqlite

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 100.00 KB | 65.00 B | 1575.38x | 7.97 | 0.35 | 12.25 MB/s | 278.47 MB/s | 0.0790 | 79.25 | 65 | ❌ | 0.043278 | 0.043278 | ❌ | ✅ |
| SHA256 | 100.00 KB | 64.00 B | 1600.00x | 0.08 | 0.00 | 1249.27 MB/s | 0.00 MB/s | 0.0782 | 79.25 | - | - | - | - | - | - |
| AES-GCM | 100.00 KB | 100.02 KB | 1.00x | 0.15 | 0.14 | 652.75 MB/s | 706.76 MB/s | 0.0783 | 79.25 | - | - | - | - | - | - |
| Frackture Encrypted | 100.00 KB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 100.00 KB | 1.13 KB | 88.66x | 0.22 | 0.10 | 450.56 MB/s | 1014.21 MB/s | 0.0797 | 79.25 | - | - | - | - | - | - |
| Gzip L6 | 100.00 KB | 741.00 B | 138.19x | 0.47 | 0.11 | 209.99 MB/s | 871.58 MB/s | 0.0811 | 79.25 | - | - | - | - | - | - |
| Gzip L9 | 100.00 KB | 741.00 B | 138.19x | 0.72 | 0.12 | 135.55 MB/s | 794.08 MB/s | 0.0787 | 79.25 | - | - | - | - | - | - |
| Brotli Q4 | 100.00 KB | 486.00 B | 210.70x | 0.32 | 0.12 | 308.64 MB/s | 789.26 MB/s | 0.0784 | 79.31 | - | - | - | - | - | - |
| Brotli Q6 | 100.00 KB | 468.00 B | 218.80x | 0.40 | 0.11 | 242.98 MB/s | 915.83 MB/s | 0.0829 | 79.43 | - | - | - | - | - | - |
| Brotli Q11 | 100.00 KB | 392.00 B | 261.22x | 6.39 | 0.12 | 15.29 MB/s | 807.00 MB/s | 0.0807 | 79.48 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 0.00% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.043278)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: small_structured_pickle

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 100.00 KB | 65.00 B | 1575.38x | 5.88 | 0.21 | 16.60 MB/s | 455.20 MB/s | 0.0785 | 79.48 | 65 | ❌ | 0.212640 | 0.180567 | ❌ | ✅ |
| SHA256 | 100.00 KB | 64.00 B | 1600.00x | 0.08 | 0.00 | 1270.00 MB/s | 0.00 MB/s | 0.0769 | 79.48 | - | - | - | - | - | - |
| AES-GCM | 100.00 KB | 100.02 KB | 1.00x | 0.18 | 0.08 | 549.45 MB/s | 1194.10 MB/s | 0.0783 | 79.48 | - | - | - | - | - | - |
| Frackture Encrypted | 100.00 KB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 100.00 KB | 1.00 KB | 99.61x | 0.20 | 0.09 | 487.93 MB/s | 1118.40 MB/s | 0.0804 | 79.48 | - | - | - | - | - | - |
| Gzip L6 | 100.00 KB | 583.00 B | 175.64x | 0.42 | 0.07 | 234.99 MB/s | 1329.87 MB/s | 0.0785 | 79.48 | - | - | - | - | - | - |
| Gzip L9 | 100.00 KB | 583.00 B | 175.64x | 0.44 | 0.07 | 220.74 MB/s | 1445.28 MB/s | 0.0816 | 79.48 | - | - | - | - | - | - |
| Brotli Q4 | 100.00 KB | 145.00 B | 706.21x | 0.23 | 0.11 | 417.57 MB/s | 913.74 MB/s | 0.0803 | 79.54 | - | - | - | - | - | - |
| Brotli Q6 | 100.00 KB | 142.00 B | 721.13x | 0.14 | 0.10 | 695.00 MB/s | 996.82 MB/s | 0.0812 | 79.59 | - | - | - | - | - | - |
| Brotli Q11 | 100.00 KB | 139.00 B | 736.69x | 4.88 | 0.11 | 20.01 MB/s | 884.46 MB/s | 0.0814 | 79.63 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 15.08% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.212640)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: small_code_javascript

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 100.00 KB | 65.00 B | 1575.38x | 5.80 | 0.22 | 16.84 MB/s | 447.73 MB/s | 0.0791 | 79.63 | 65 | ❌ | 0.210678 | 0.176264 | ❌ | ✅ |
| SHA256 | 100.00 KB | 64.00 B | 1600.00x | 0.08 | 0.00 | 1239.29 MB/s | 0.00 MB/s | 0.0788 | 79.63 | - | - | - | - | - | - |
| AES-GCM | 100.00 KB | 100.02 KB | 1.00x | 0.15 | 0.11 | 631.66 MB/s | 915.11 MB/s | 0.0799 | 79.63 | - | - | - | - | - | - |
| Frackture Encrypted | 100.00 KB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 100.00 KB | 1.54 KB | 64.85x | 0.23 | 0.10 | 428.79 MB/s | 969.51 MB/s | 0.0898 | 79.63 | - | - | - | - | - | - |
| Gzip L6 | 100.00 KB | 831.00 B | 123.23x | 0.44 | 0.08 | 221.14 MB/s | 1201.27 MB/s | 0.0796 | 79.63 | - | - | - | - | - | - |
| Gzip L9 | 100.00 KB | 831.00 B | 123.23x | 0.35 | 0.07 | 277.00 MB/s | 1377.17 MB/s | 0.0823 | 79.63 | - | - | - | - | - | - |
| Brotli Q4 | 100.00 KB | 275.00 B | 372.36x | 0.20 | 0.11 | 479.77 MB/s | 884.79 MB/s | 0.0800 | 79.68 | - | - | - | - | - | - |
| Brotli Q6 | 100.00 KB | 254.00 B | 403.15x | 0.17 | 0.10 | 583.61 MB/s | 994.21 MB/s | 0.0822 | 79.74 | - | - | - | - | - | - |
| Brotli Q11 | 100.00 KB | 236.00 B | 433.90x | 5.94 | 0.14 | 16.43 MB/s | 693.93 MB/s | 0.0819 | 79.79 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 16.33% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.210678)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: small_code_javascript_minified

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 100.00 KB | 65.00 B | 1575.38x | 5.63 | 0.25 | 17.34 MB/s | 397.07 MB/s | 0.0795 | 79.79 | 65 | ❌ | 0.248601 | 0.216233 | ❌ | ✅ |
| SHA256 | 100.00 KB | 64.00 B | 1600.00x | 0.08 | 0.00 | 1272.59 MB/s | 0.00 MB/s | 0.0767 | 79.79 | - | - | - | - | - | - |
| AES-GCM | 100.00 KB | 100.02 KB | 1.00x | 0.17 | 0.08 | 564.46 MB/s | 1162.13 MB/s | 0.0791 | 79.79 | - | - | - | - | - | - |
| Frackture Encrypted | 100.00 KB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 100.00 KB | 1.03 KB | 97.34x | 0.19 | 0.09 | 502.47 MB/s | 1075.15 MB/s | 0.0785 | 79.79 | - | - | - | - | - | - |
| Gzip L6 | 100.00 KB | 607.00 B | 168.70x | 0.40 | 0.07 | 246.33 MB/s | 1372.62 MB/s | 0.0786 | 79.79 | - | - | - | - | - | - |
| Gzip L9 | 100.00 KB | 607.00 B | 168.70x | 0.32 | 0.07 | 302.83 MB/s | 1407.52 MB/s | 0.0818 | 79.79 | - | - | - | - | - | - |
| Brotli Q4 | 100.00 KB | 169.00 B | 605.92x | 0.19 | 0.11 | 522.76 MB/s | 920.59 MB/s | 0.0801 | 79.85 | - | - | - | - | - | - |
| Brotli Q6 | 100.00 KB | 157.00 B | 652.23x | 0.16 | 0.10 | 610.82 MB/s | 1013.75 MB/s | 0.0817 | 79.89 | - | - | - | - | - | - |
| Brotli Q11 | 100.00 KB | 165.00 B | 620.61x | 5.20 | 0.11 | 18.79 MB/s | 858.18 MB/s | 0.0793 | 79.94 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 13.02% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.248601)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: small_code_python

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 100.00 KB | 65.00 B | 1575.38x | 5.75 | 0.22 | 17.00 MB/s | 442.82 MB/s | 0.0796 | 79.95 | 65 | ❌ | 0.201540 | 0.173739 | ❌ | ✅ |
| SHA256 | 100.00 KB | 64.00 B | 1600.00x | 0.08 | 0.00 | 1296.21 MB/s | 0.00 MB/s | 0.0753 | 79.95 | - | - | - | - | - | - |
| AES-GCM | 100.00 KB | 100.02 KB | 1.00x | 0.17 | 0.10 | 578.88 MB/s | 973.34 MB/s | 0.0813 | 79.95 | - | - | - | - | - | - |
| Frackture Encrypted | 100.00 KB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 100.00 KB | 2.50 KB | 39.95x | 0.25 | 0.11 | 383.38 MB/s | 869.05 MB/s | 0.0792 | 79.95 | - | - | - | - | - | - |
| Gzip L6 | 100.00 KB | 1.35 KB | 73.83x | 0.39 | 0.08 | 249.49 MB/s | 1219.42 MB/s | 0.0815 | 79.95 | - | - | - | - | - | - |
| Gzip L9 | 100.00 KB | 1.13 KB | 88.43x | 0.43 | 0.08 | 227.58 MB/s | 1186.70 MB/s | 0.0784 | 79.95 | - | - | - | - | - | - |
| Brotli Q4 | 100.00 KB | 534.00 B | 191.76x | 0.24 | 0.11 | 401.62 MB/s | 859.13 MB/s | 0.0796 | 80.00 | - | - | - | - | - | - |
| Brotli Q6 | 100.00 KB | 506.00 B | 202.37x | 0.23 | 0.10 | 418.89 MB/s | 957.19 MB/s | 0.0810 | 80.08 | - | - | - | - | - | - |
| Brotli Q11 | 100.00 KB | 491.00 B | 208.55x | 6.69 | 0.13 | 14.61 MB/s | 780.79 MB/s | 0.0809 | 80.14 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 13.79% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.201540)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: small_mixed_payload

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 100.00 KB | 65.00 B | 1575.38x | 6.06 | 0.29 | 16.10 MB/s | 341.76 MB/s | 0.0795 | 80.14 | 65 | ❌ | 0.067139 | 0.050524 | ❌ | ✅ |
| SHA256 | 100.00 KB | 64.00 B | 1600.00x | 0.08 | 0.00 | 1292.12 MB/s | 0.00 MB/s | 0.0756 | 80.14 | - | - | - | - | - | - |
| AES-GCM | 100.00 KB | 100.02 KB | 1.00x | 0.15 | 0.11 | 655.92 MB/s | 861.03 MB/s | 0.0799 | 80.14 | - | - | - | - | - | - |
| Frackture Encrypted | 100.00 KB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 100.00 KB | 2.76 KB | 36.20x | 0.26 | 0.18 | 370.81 MB/s | 537.72 MB/s | 0.0783 | 80.14 | - | - | - | - | - | - |
| Gzip L6 | 100.00 KB | 1.68 KB | 59.60x | 0.47 | 0.09 | 207.47 MB/s | 1091.46 MB/s | 0.0868 | 80.14 | - | - | - | - | - | - |
| Gzip L9 | 100.00 KB | 1.68 KB | 59.60x | 0.42 | 0.09 | 234.86 MB/s | 1101.66 MB/s | 0.0788 | 80.14 | - | - | - | - | - | - |
| Brotli Q4 | 100.00 KB | 1.04 KB | 96.51x | 0.30 | 0.12 | 326.62 MB/s | 804.15 MB/s | 0.0800 | 80.19 | - | - | - | - | - | - |
| Brotli Q6 | 100.00 KB | 995.00 B | 102.91x | 0.33 | 0.11 | 293.28 MB/s | 893.79 MB/s | 0.0799 | 80.27 | - | - | - | - | - | - |
| Brotli Q11 | 100.00 KB | 900.00 B | 113.78x | 7.86 | 0.13 | 12.43 MB/s | 763.46 MB/s | 0.0814 | 80.32 | - | - | - | - | - | - |

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
