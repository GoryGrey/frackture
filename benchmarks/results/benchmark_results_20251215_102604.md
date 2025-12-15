# Frackture Benchmark Results

**Generated:** 2025-12-15 10:26:04
**Enhanced Metrics Version:** 2.1.0

## New Verification Metrics

- **Payload Sizing**: Symbolic bytes, entropy bytes, serialized total, 96B validation
- **Reconstruction Quality**: MSE baseline vs optimized, lossless status
- **Optimization**: MSE improvement percentage, trials count
- **Determinism**: Multiple encoding tests, drift detection
- **Fault Injection**: Payload mutation tests, error handling validation
- **Competition Summary**: Frackture vs Gzip/Brotli wins by tier and by configuration

## Benchmark Configuration

- **Gzip levels:** [1, 2, 3, 4, 5, 6, 7, 8, 9]
- **Brotli qualities:** [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
- **Real datasets:** True
- **All tiers:** True

## Competition Summary (Frackture vs Gzip/Brotli)

| Scope | Total Comparisons | Wins (Ratio) | Win Rate (Ratio) | Wins (Throughput) | Win Rate (Throughput) |
|---|---:|---:|---:|---:|---:|
| Overall | 1215 | 994 | 81.8% | 115 | 9.5% |

### Win Rates by Tier

| Tier | Total Comparisons | Wins (Ratio) | Win Rate (Ratio) |
|---|---:|---:|---:|
| large | 294 | 290 | 98.6% |
| medium | 294 | 285 | 96.9% |
| small | 294 | 275 | 93.5% |
| tiny | 252 | 63 | 25.0% |
| xlarge | 81 | 81 | 100.0% |

---

## Dataset: binary_png_tiny

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 50.00 B | 65.00 B | 0.77x | 6.20 | 0.27 | 0.01 MB/s | 0.18 MB/s | 0.0027 | 67.82 | 65 | ❌ | 0.163385 | 0.163385 | ❌ | ✅ |
| SHA256 | 50.00 B | 64.00 B | 0.78x | 0.00 | 0.00 | 41.79 MB/s | 0.00 MB/s | 0.0011 | 67.82 | - | - | - | - | - | - |
| AES-GCM | 50.00 B | 66.00 B | 0.76x | 1.34 | 0.26 | 0.04 MB/s | 0.18 MB/s | 0.0029 | 68.12 | - | - | - | - | - | - |
| Frackture Encrypted | 50.00 B | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 50.00 B | 63.00 B | 0.79x | 0.11 | 0.05 | 0.45 MB/s | 0.99 MB/s | 0.0030 | 68.21 | - | - | - | - | - | - |
| Gzip L2 | 50.00 B | 63.00 B | 0.79x | 0.04 | 0.03 | 1.33 MB/s | 1.82 MB/s | 0.0028 | 68.23 | - | - | - | - | - | - |
| Gzip L3 | 50.00 B | 63.00 B | 0.79x | 0.02 | 0.02 | 2.12 MB/s | 2.39 MB/s | 0.0027 | 68.23 | - | - | - | - | - | - |
| Gzip L4 | 50.00 B | 63.00 B | 0.79x | 0.02 | 0.02 | 2.43 MB/s | 2.70 MB/s | 0.0033 | 68.23 | - | - | - | - | - | - |
| Gzip L5 | 50.00 B | 63.00 B | 0.79x | 0.02 | 0.02 | 2.01 MB/s | 2.39 MB/s | 0.0029 | 68.23 | - | - | - | - | - | - |
| Gzip L6 | 50.00 B | 63.00 B | 0.79x | 0.02 | 0.02 | 2.54 MB/s | 2.51 MB/s | 0.0030 | 68.23 | - | - | - | - | - | - |
| Gzip L7 | 50.00 B | 63.00 B | 0.79x | 0.03 | 0.02 | 1.87 MB/s | 2.37 MB/s | 0.0027 | 68.23 | - | - | - | - | - | - |
| Gzip L8 | 50.00 B | 63.00 B | 0.79x | 0.02 | 0.02 | 2.47 MB/s | 2.67 MB/s | 0.0028 | 68.23 | - | - | - | - | - | - |
| Gzip L9 | 50.00 B | 63.00 B | 0.79x | 0.02 | 0.02 | 2.67 MB/s | 2.69 MB/s | 0.0030 | 68.23 | - | - | - | - | - | - |
| Brotli Q0 | 50.00 B | 54.00 B | 0.93x | 0.66 | 0.01 | 0.07 MB/s | 3.57 MB/s | 0.0028 | 68.59 | - | - | - | - | - | - |
| Brotli Q1 | 50.00 B | 54.00 B | 0.93x | 0.02 | 0.00 | 2.53 MB/s | 13.59 MB/s | 0.0029 | 68.59 | - | - | - | - | - | - |
| Brotli Q2 | 50.00 B | 54.00 B | 0.93x | 0.08 | 0.00 | 0.62 MB/s | 15.46 MB/s | 0.0027 | 68.73 | - | - | - | - | - | - |
| Brotli Q3 | 50.00 B | 54.00 B | 0.93x | 0.04 | 0.00 | 1.32 MB/s | 16.76 MB/s | 0.0028 | 68.77 | - | - | - | - | - | - |
| Brotli Q4 | 50.00 B | 54.00 B | 0.93x | 0.15 | 0.01 | 0.33 MB/s | 6.14 MB/s | 0.0034 | 68.77 | - | - | - | - | - | - |
| Brotli Q5 | 50.00 B | 54.00 B | 0.93x | 0.14 | 0.00 | 0.34 MB/s | 11.22 MB/s | 0.0028 | 68.89 | - | - | - | - | - | - |
| Brotli Q6 | 50.00 B | 54.00 B | 0.93x | 0.15 | 0.00 | 0.33 MB/s | 12.38 MB/s | 0.0033 | 68.98 | - | - | - | - | - | - |
| Brotli Q7 | 50.00 B | 54.00 B | 0.93x | 0.12 | 0.00 | 0.39 MB/s | 10.62 MB/s | 0.0029 | 68.98 | - | - | - | - | - | - |
| Brotli Q8 | 50.00 B | 54.00 B | 0.93x | 0.08 | 0.00 | 0.57 MB/s | 13.37 MB/s | 0.0027 | 68.98 | - | - | - | - | - | - |
| Brotli Q9 | 50.00 B | 54.00 B | 0.93x | 0.17 | 0.01 | 0.28 MB/s | 7.31 MB/s | 0.0038 | 68.98 | - | - | - | - | - | - |
| Brotli Q10 | 50.00 B | 54.00 B | 0.93x | 1.16 | 0.01 | 0.04 MB/s | 6.72 MB/s | 0.0030 | 69.49 | - | - | - | - | - | - |
| Brotli Q11 | 50.00 B | 54.00 B | 0.93x | 0.63 | 0.01 | 0.08 MB/s | 7.94 MB/s | 0.0031 | 69.50 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 0.00% improvement over 2 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.163385)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: binary_jpeg_tiny

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 50.00 B | 65.00 B | 0.77x | 5.06 | 0.24 | 0.01 MB/s | 0.20 MB/s | 0.0029 | 69.52 | 65 | ❌ | 0.148596 | 0.148596 | ❌ | ✅ |
| SHA256 | 50.00 B | 64.00 B | 0.78x | 0.00 | 0.00 | 41.82 MB/s | 0.00 MB/s | 0.0011 | 69.52 | - | - | - | - | - | - |
| AES-GCM | 50.00 B | 66.00 B | 0.76x | 0.14 | 0.06 | 0.35 MB/s | 0.77 MB/s | 0.0034 | 69.52 | - | - | - | - | - | - |
| Frackture Encrypted | 50.00 B | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 50.00 B | 69.00 B | 0.72x | 0.05 | 0.04 | 0.88 MB/s | 1.07 MB/s | 0.0046 | 69.52 | - | - | - | - | - | - |
| Gzip L2 | 50.00 B | 69.00 B | 0.72x | 0.04 | 0.12 | 1.07 MB/s | 0.39 MB/s | 0.0030 | 69.52 | - | - | - | - | - | - |
| Gzip L3 | 50.00 B | 69.00 B | 0.72x | 0.03 | 0.03 | 1.81 MB/s | 1.90 MB/s | 0.0030 | 69.52 | - | - | - | - | - | - |
| Gzip L4 | 50.00 B | 69.00 B | 0.72x | 0.02 | 0.02 | 2.05 MB/s | 2.26 MB/s | 0.0031 | 69.52 | - | - | - | - | - | - |
| Gzip L5 | 50.00 B | 69.00 B | 0.72x | 0.02 | 0.02 | 2.07 MB/s | 2.25 MB/s | 0.0029 | 69.52 | - | - | - | - | - | - |
| Gzip L6 | 50.00 B | 69.00 B | 0.72x | 0.02 | 0.02 | 2.07 MB/s | 2.27 MB/s | 0.0027 | 69.52 | - | - | - | - | - | - |
| Gzip L7 | 50.00 B | 69.00 B | 0.72x | 0.02 | 0.02 | 2.64 MB/s | 2.60 MB/s | 0.0031 | 69.52 | - | - | - | - | - | - |
| Gzip L8 | 50.00 B | 69.00 B | 0.72x | 0.02 | 0.02 | 2.53 MB/s | 2.49 MB/s | 0.0028 | 69.52 | - | - | - | - | - | - |
| Gzip L9 | 50.00 B | 69.00 B | 0.72x | 0.02 | 0.02 | 2.74 MB/s | 2.68 MB/s | 0.0026 | 69.52 | - | - | - | - | - | - |
| Brotli Q0 | 50.00 B | 54.00 B | 0.93x | 0.03 | 0.01 | 1.45 MB/s | 7.55 MB/s | 0.0028 | 69.52 | - | - | - | - | - | - |
| Brotli Q1 | 50.00 B | 54.00 B | 0.93x | 0.02 | 0.00 | 2.89 MB/s | 14.45 MB/s | 0.0028 | 69.52 | - | - | - | - | - | - |
| Brotli Q2 | 50.00 B | 54.00 B | 0.93x | 0.01 | 0.00 | 3.28 MB/s | 15.78 MB/s | 0.0031 | 69.52 | - | - | - | - | - | - |
| Brotli Q3 | 50.00 B | 54.00 B | 0.93x | 0.02 | 0.00 | 2.56 MB/s | 11.15 MB/s | 0.0026 | 69.52 | - | - | - | - | - | - |
| Brotli Q4 | 50.00 B | 54.00 B | 0.93x | 0.03 | 0.00 | 1.83 MB/s | 16.45 MB/s | 0.0028 | 69.52 | - | - | - | - | - | - |
| Brotli Q5 | 50.00 B | 54.00 B | 0.93x | 0.11 | 0.00 | 0.44 MB/s | 14.95 MB/s | 0.0035 | 69.67 | - | - | - | - | - | - |
| Brotli Q6 | 50.00 B | 54.00 B | 0.93x | 0.10 | 0.00 | 0.45 MB/s | 12.22 MB/s | 0.0028 | 69.83 | - | - | - | - | - | - |
| Brotli Q7 | 50.00 B | 54.00 B | 0.93x | 0.10 | 0.00 | 0.47 MB/s | 14.70 MB/s | 0.0030 | 70.00 | - | - | - | - | - | - |
| Brotli Q8 | 50.00 B | 54.00 B | 0.93x | 0.11 | 0.00 | 0.43 MB/s | 11.59 MB/s | 0.0027 | 70.18 | - | - | - | - | - | - |
| Brotli Q9 | 50.00 B | 54.00 B | 0.93x | 0.14 | 0.00 | 0.34 MB/s | 10.34 MB/s | 0.0028 | 70.18 | - | - | - | - | - | - |
| Brotli Q10 | 50.00 B | 54.00 B | 0.93x | 0.60 | 0.00 | 0.08 MB/s | 10.03 MB/s | 0.0032 | 70.28 | - | - | - | - | - | - |
| Brotli Q11 | 50.00 B | 54.00 B | 0.93x | 0.56 | 0.01 | 0.09 MB/s | 7.91 MB/s | 0.0035 | 70.28 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 0.00% improvement over 2 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.148596)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: binary_pdf_tiny

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 50.00 B | 65.00 B | 0.77x | 5.08 | 0.27 | 0.01 MB/s | 0.18 MB/s | 0.0031 | 70.28 | 65 | ❌ | 0.139894 | 0.139894 | ❌ | ✅ |
| SHA256 | 50.00 B | 64.00 B | 0.78x | 0.00 | 0.00 | 41.67 MB/s | 0.00 MB/s | 0.0011 | 70.28 | - | - | - | - | - | - |
| AES-GCM | 50.00 B | 66.00 B | 0.76x | 0.13 | 0.06 | 0.36 MB/s | 0.84 MB/s | 0.0027 | 70.28 | - | - | - | - | - | - |
| Frackture Encrypted | 50.00 B | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 50.00 B | 69.00 B | 0.72x | 0.05 | 0.04 | 0.97 MB/s | 1.19 MB/s | 0.0029 | 70.28 | - | - | - | - | - | - |
| Gzip L2 | 50.00 B | 69.00 B | 0.72x | 0.03 | 0.02 | 1.88 MB/s | 2.19 MB/s | 0.0031 | 70.28 | - | - | - | - | - | - |
| Gzip L3 | 50.00 B | 69.00 B | 0.72x | 0.02 | 0.02 | 2.22 MB/s | 2.35 MB/s | 0.0027 | 70.28 | - | - | - | - | - | - |
| Gzip L4 | 50.00 B | 69.00 B | 0.72x | 0.03 | 0.03 | 1.78 MB/s | 1.87 MB/s | 0.0030 | 70.28 | - | - | - | - | - | - |
| Gzip L5 | 50.00 B | 69.00 B | 0.72x | 0.02 | 0.02 | 2.40 MB/s | 2.51 MB/s | 0.0031 | 70.28 | - | - | - | - | - | - |
| Gzip L6 | 50.00 B | 69.00 B | 0.72x | 0.02 | 0.02 | 2.55 MB/s | 2.61 MB/s | 0.0030 | 70.28 | - | - | - | - | - | - |
| Gzip L7 | 50.00 B | 69.00 B | 0.72x | 0.02 | 0.02 | 2.43 MB/s | 2.49 MB/s | 0.0027 | 70.28 | - | - | - | - | - | - |
| Gzip L8 | 50.00 B | 69.00 B | 0.72x | 0.02 | 0.02 | 2.66 MB/s | 1.91 MB/s | 0.0029 | 70.28 | - | - | - | - | - | - |
| Gzip L9 | 50.00 B | 69.00 B | 0.72x | 0.02 | 0.02 | 2.55 MB/s | 2.54 MB/s | 0.0028 | 70.28 | - | - | - | - | - | - |
| Brotli Q0 | 50.00 B | 54.00 B | 0.93x | 0.03 | 0.01 | 1.46 MB/s | 8.16 MB/s | 0.0027 | 70.28 | - | - | - | - | - | - |
| Brotli Q1 | 50.00 B | 54.00 B | 0.93x | 0.02 | 0.00 | 2.96 MB/s | 15.14 MB/s | 0.0030 | 70.28 | - | - | - | - | - | - |
| Brotli Q2 | 50.00 B | 54.00 B | 0.93x | 0.01 | 0.00 | 3.35 MB/s | 15.18 MB/s | 0.0028 | 70.28 | - | - | - | - | - | - |
| Brotli Q3 | 50.00 B | 54.00 B | 0.93x | 0.02 | 0.00 | 2.88 MB/s | 17.73 MB/s | 0.0027 | 70.28 | - | - | - | - | - | - |
| Brotli Q4 | 50.00 B | 54.00 B | 0.93x | 0.08 | 0.00 | 0.60 MB/s | 14.38 MB/s | 0.0027 | 70.36 | - | - | - | - | - | - |
| Brotli Q5 | 50.00 B | 52.00 B | 0.96x | 0.06 | 0.01 | 0.73 MB/s | 4.93 MB/s | 0.0028 | 70.46 | - | - | - | - | - | - |
| Brotli Q6 | 50.00 B | 52.00 B | 0.96x | 0.13 | 0.01 | 0.38 MB/s | 7.27 MB/s | 0.0038 | 70.64 | - | - | - | - | - | - |
| Brotli Q7 | 50.00 B | 52.00 B | 0.96x | 0.10 | 0.01 | 0.50 MB/s | 5.15 MB/s | 0.0030 | 70.80 | - | - | - | - | - | - |
| Brotli Q8 | 50.00 B | 52.00 B | 0.96x | 0.10 | 0.01 | 0.46 MB/s | 6.48 MB/s | 0.0027 | 70.97 | - | - | - | - | - | - |
| Brotli Q9 | 50.00 B | 52.00 B | 0.96x | 0.16 | 0.01 | 0.30 MB/s | 6.01 MB/s | 0.0027 | 70.97 | - | - | - | - | - | - |
| Brotli Q10 | 50.00 B | 54.00 B | 0.93x | 0.75 | 0.01 | 0.06 MB/s | 6.29 MB/s | 0.0032 | 71.09 | - | - | - | - | - | - |
| Brotli Q11 | 50.00 B | 54.00 B | 0.93x | 0.64 | 0.01 | 0.07 MB/s | 4.01 MB/s | 0.0027 | 71.09 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 0.00% improvement over 2 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.139894)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: binary_gif_tiny

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 50.00 B | 65.00 B | 0.77x | 5.09 | 0.24 | 0.01 MB/s | 0.20 MB/s | 0.0029 | 71.09 | 65 | ❌ | 0.138092 | 0.138092 | ❌ | ✅ |
| SHA256 | 50.00 B | 64.00 B | 0.78x | 0.00 | 0.00 | 41.64 MB/s | 0.00 MB/s | 0.0011 | 71.09 | - | - | - | - | - | - |
| AES-GCM | 50.00 B | 66.00 B | 0.76x | 0.12 | 0.05 | 0.39 MB/s | 1.00 MB/s | 0.0029 | 71.09 | - | - | - | - | - | - |
| Frackture Encrypted | 50.00 B | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 50.00 B | 57.00 B | 0.88x | 0.04 | 0.03 | 1.12 MB/s | 1.52 MB/s | 0.0027 | 71.09 | - | - | - | - | - | - |
| Gzip L2 | 50.00 B | 57.00 B | 0.88x | 0.02 | 0.02 | 2.07 MB/s | 2.28 MB/s | 0.0028 | 71.09 | - | - | - | - | - | - |
| Gzip L3 | 50.00 B | 57.00 B | 0.88x | 0.02 | 0.02 | 2.31 MB/s | 2.37 MB/s | 0.0030 | 71.09 | - | - | - | - | - | - |
| Gzip L4 | 50.00 B | 57.00 B | 0.88x | 0.02 | 0.02 | 2.38 MB/s | 2.59 MB/s | 0.0033 | 71.09 | - | - | - | - | - | - |
| Gzip L5 | 50.00 B | 57.00 B | 0.88x | 0.02 | 0.02 | 2.09 MB/s | 2.37 MB/s | 0.0028 | 71.09 | - | - | - | - | - | - |
| Gzip L6 | 50.00 B | 57.00 B | 0.88x | 0.02 | 0.02 | 2.71 MB/s | 2.76 MB/s | 0.0029 | 71.09 | - | - | - | - | - | - |
| Gzip L7 | 50.00 B | 57.00 B | 0.88x | 0.02 | 0.02 | 2.82 MB/s | 2.75 MB/s | 0.0028 | 71.09 | - | - | - | - | - | - |
| Gzip L8 | 50.00 B | 57.00 B | 0.88x | 0.02 | 0.02 | 2.88 MB/s | 2.70 MB/s | 0.0026 | 71.09 | - | - | - | - | - | - |
| Gzip L9 | 50.00 B | 57.00 B | 0.88x | 0.03 | 0.02 | 1.42 MB/s | 2.58 MB/s | 0.0027 | 71.09 | - | - | - | - | - | - |
| Brotli Q0 | 50.00 B | 54.00 B | 0.93x | 0.03 | 0.01 | 1.44 MB/s | 7.33 MB/s | 0.0028 | 71.09 | - | - | - | - | - | - |
| Brotli Q1 | 50.00 B | 54.00 B | 0.93x | 0.02 | 0.00 | 2.66 MB/s | 14.17 MB/s | 0.0028 | 71.09 | - | - | - | - | - | - |
| Brotli Q2 | 50.00 B | 54.00 B | 0.93x | 0.02 | 0.00 | 3.00 MB/s | 14.16 MB/s | 0.0028 | 71.09 | - | - | - | - | - | - |
| Brotli Q3 | 50.00 B | 47.00 B | 1.06x | 0.02 | 0.01 | 3.05 MB/s | 5.04 MB/s | 0.0029 | 71.09 | - | - | - | - | - | - |
| Brotli Q4 | 50.00 B | 51.00 B | 0.98x | 0.03 | 0.01 | 1.71 MB/s | 7.44 MB/s | 0.0030 | 71.09 | - | - | - | - | - | - |
| Brotli Q5 | 50.00 B | 54.00 B | 0.93x | 0.04 | 0.00 | 1.06 MB/s | 14.90 MB/s | 0.0027 | 71.12 | - | - | - | - | - | - |
| Brotli Q6 | 50.00 B | 54.00 B | 0.93x | 0.07 | 0.00 | 0.65 MB/s | 18.35 MB/s | 0.0029 | 71.23 | - | - | - | - | - | - |
| Brotli Q7 | 50.00 B | 54.00 B | 0.93x | 0.07 | 0.00 | 0.65 MB/s | 16.82 MB/s | 0.0030 | 71.35 | - | - | - | - | - | - |
| Brotli Q8 | 50.00 B | 54.00 B | 0.93x | 0.08 | 0.00 | 0.59 MB/s | 15.31 MB/s | 0.0029 | 71.47 | - | - | - | - | - | - |
| Brotli Q9 | 50.00 B | 54.00 B | 0.93x | 0.14 | 0.00 | 0.34 MB/s | 11.11 MB/s | 0.0026 | 71.47 | - | - | - | - | - | - |
| Brotli Q10 | 50.00 B | 54.00 B | 0.93x | 0.67 | 0.01 | 0.07 MB/s | 3.94 MB/s | 0.0029 | 71.47 | - | - | - | - | - | - |
| Brotli Q11 | 50.00 B | 48.00 B | 1.04x | 0.68 | 0.01 | 0.07 MB/s | 4.07 MB/s | 0.0026 | 71.47 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 0.00% improvement over 2 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.138092)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: code_javascript_tiny

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 50.00 B | 65.00 B | 0.77x | 4.98 | 0.24 | 0.01 MB/s | 0.20 MB/s | 0.0056 | 71.47 | 65 | ❌ | 0.141407 | 0.141407 | ❌ | ✅ |
| SHA256 | 50.00 B | 64.00 B | 0.78x | 0.00 | 0.00 | 41.74 MB/s | 0.00 MB/s | 0.0011 | 71.47 | - | - | - | - | - | - |
| AES-GCM | 50.00 B | 66.00 B | 0.76x | 0.12 | 0.10 | 0.39 MB/s | 0.50 MB/s | 0.0045 | 71.47 | - | - | - | - | - | - |
| Frackture Encrypted | 50.00 B | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 50.00 B | 70.00 B | 0.71x | 0.06 | 0.05 | 0.80 MB/s | 1.00 MB/s | 0.0083 | 71.47 | - | - | - | - | - | - |
| Gzip L2 | 50.00 B | 70.00 B | 0.71x | 0.05 | 0.04 | 1.02 MB/s | 1.31 MB/s | 0.0047 | 71.47 | - | - | - | - | - | - |
| Gzip L3 | 50.00 B | 70.00 B | 0.71x | 0.04 | 0.03 | 1.09 MB/s | 1.40 MB/s | 0.0046 | 71.47 | - | - | - | - | - | - |
| Gzip L4 | 50.00 B | 70.00 B | 0.71x | 0.03 | 0.03 | 1.49 MB/s | 1.70 MB/s | 0.0044 | 71.47 | - | - | - | - | - | - |
| Gzip L5 | 50.00 B | 70.00 B | 0.71x | 0.04 | 0.03 | 1.30 MB/s | 1.46 MB/s | 0.0047 | 71.47 | - | - | - | - | - | - |
| Gzip L6 | 50.00 B | 70.00 B | 0.71x | 0.04 | 0.03 | 1.20 MB/s | 1.42 MB/s | 0.0048 | 71.47 | - | - | - | - | - | - |
| Gzip L7 | 50.00 B | 70.00 B | 0.71x | 0.04 | 0.03 | 1.26 MB/s | 1.45 MB/s | 0.0045 | 71.47 | - | - | - | - | - | - |
| Gzip L8 | 50.00 B | 70.00 B | 0.71x | 0.03 | 0.03 | 1.49 MB/s | 1.65 MB/s | 0.0039 | 71.47 | - | - | - | - | - | - |
| Gzip L9 | 50.00 B | 70.00 B | 0.71x | 0.03 | 0.03 | 1.68 MB/s | 1.75 MB/s | 0.0044 | 71.47 | - | - | - | - | - | - |
| Brotli Q0 | 50.00 B | 54.00 B | 0.93x | 0.04 | 0.01 | 1.10 MB/s | 5.15 MB/s | 0.0040 | 71.47 | - | - | - | - | - | - |
| Brotli Q1 | 50.00 B | 54.00 B | 0.93x | 0.02 | 0.00 | 2.29 MB/s | 11.05 MB/s | 0.0043 | 71.47 | - | - | - | - | - | - |
| Brotli Q2 | 50.00 B | 54.00 B | 0.93x | 0.02 | 0.00 | 2.45 MB/s | 11.42 MB/s | 0.0040 | 71.47 | - | - | - | - | - | - |
| Brotli Q3 | 50.00 B | 52.00 B | 0.96x | 0.02 | 0.01 | 2.26 MB/s | 4.10 MB/s | 0.0043 | 71.47 | - | - | - | - | - | - |
| Brotli Q4 | 50.00 B | 44.00 B | 1.14x | 0.04 | 0.01 | 1.09 MB/s | 3.65 MB/s | 0.0040 | 71.47 | - | - | - | - | - | - |
| Brotli Q5 | 50.00 B | 42.00 B | 1.19x | 0.06 | 0.01 | 0.75 MB/s | 5.49 MB/s | 0.0037 | 71.53 | - | - | - | - | - | - |
| Brotli Q6 | 50.00 B | 42.00 B | 1.19x | 0.08 | 0.01 | 0.63 MB/s | 7.27 MB/s | 0.0037 | 71.64 | - | - | - | - | - | - |
| Brotli Q7 | 50.00 B | 42.00 B | 1.19x | 0.10 | 0.01 | 0.50 MB/s | 7.84 MB/s | 0.0039 | 71.78 | - | - | - | - | - | - |
| Brotli Q8 | 50.00 B | 42.00 B | 1.19x | 0.11 | 0.01 | 0.44 MB/s | 6.67 MB/s | 0.0046 | 71.94 | - | - | - | - | - | - |
| Brotli Q9 | 50.00 B | 42.00 B | 1.19x | 0.21 | 0.01 | 0.23 MB/s | 3.84 MB/s | 0.0036 | 71.94 | - | - | - | - | - | - |
| Brotli Q10 | 50.00 B | 50.00 B | 1.00x | 0.49 | 0.01 | 0.10 MB/s | 3.41 MB/s | 0.0028 | 71.94 | - | - | - | - | - | - |
| Brotli Q11 | 50.00 B | 50.00 B | 1.00x | 0.39 | 0.01 | 0.12 MB/s | 4.49 MB/s | 0.0038 | 71.94 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 0.00% improvement over 2 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.141407)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: code_javascript_minified_tiny

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 50.00 B | 65.00 B | 0.77x | 5.27 | 0.24 | 0.01 MB/s | 0.20 MB/s | 0.0027 | 71.95 | 65 | ❌ | 0.143860 | 0.143860 | ❌ | ✅ |
| SHA256 | 50.00 B | 64.00 B | 0.78x | 0.00 | 0.00 | 36.38 MB/s | 0.00 MB/s | 0.0013 | 71.95 | - | - | - | - | - | - |
| AES-GCM | 50.00 B | 66.00 B | 0.76x | 0.11 | 0.05 | 0.43 MB/s | 1.01 MB/s | 0.0029 | 71.95 | - | - | - | - | - | - |
| Frackture Encrypted | 50.00 B | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 50.00 B | 66.00 B | 0.76x | 0.07 | 0.04 | 0.66 MB/s | 1.34 MB/s | 0.0030 | 71.95 | - | - | - | - | - | - |
| Gzip L2 | 50.00 B | 66.00 B | 0.76x | 0.03 | 0.02 | 1.47 MB/s | 2.16 MB/s | 0.0029 | 71.95 | - | - | - | - | - | - |
| Gzip L3 | 50.00 B | 66.00 B | 0.76x | 0.02 | 0.02 | 2.27 MB/s | 1.92 MB/s | 0.0031 | 71.95 | - | - | - | - | - | - |
| Gzip L4 | 50.00 B | 66.00 B | 0.76x | 0.02 | 0.02 | 2.32 MB/s | 2.59 MB/s | 0.0033 | 71.95 | - | - | - | - | - | - |
| Gzip L5 | 50.00 B | 66.00 B | 0.76x | 0.02 | 0.02 | 2.23 MB/s | 2.33 MB/s | 0.0026 | 71.95 | - | - | - | - | - | - |
| Gzip L6 | 50.00 B | 66.00 B | 0.76x | 0.02 | 0.02 | 2.72 MB/s | 2.83 MB/s | 0.0031 | 71.95 | - | - | - | - | - | - |
| Gzip L7 | 50.00 B | 66.00 B | 0.76x | 0.02 | 0.02 | 2.20 MB/s | 2.34 MB/s | 0.0028 | 71.95 | - | - | - | - | - | - |
| Gzip L8 | 50.00 B | 66.00 B | 0.76x | 0.02 | 0.02 | 2.49 MB/s | 2.53 MB/s | 0.0026 | 71.95 | - | - | - | - | - | - |
| Gzip L9 | 50.00 B | 66.00 B | 0.76x | 0.02 | 0.08 | 2.76 MB/s | 0.58 MB/s | 0.0036 | 71.95 | - | - | - | - | - | - |
| Brotli Q0 | 50.00 B | 54.00 B | 0.93x | 0.03 | 0.01 | 1.39 MB/s | 7.52 MB/s | 0.0029 | 71.95 | - | - | - | - | - | - |
| Brotli Q1 | 50.00 B | 54.00 B | 0.93x | 0.02 | 0.00 | 2.93 MB/s | 15.01 MB/s | 0.0028 | 71.95 | - | - | - | - | - | - |
| Brotli Q2 | 50.00 B | 54.00 B | 0.93x | 0.01 | 0.00 | 3.39 MB/s | 16.35 MB/s | 0.0026 | 71.95 | - | - | - | - | - | - |
| Brotli Q3 | 50.00 B | 54.00 B | 0.93x | 0.02 | 0.00 | 3.03 MB/s | 20.90 MB/s | 0.0028 | 71.95 | - | - | - | - | - | - |
| Brotli Q4 | 50.00 B | 48.00 B | 1.04x | 0.03 | 0.01 | 1.56 MB/s | 5.43 MB/s | 0.0043 | 71.95 | - | - | - | - | - | - |
| Brotli Q5 | 50.00 B | 49.00 B | 1.02x | 0.06 | 0.01 | 0.79 MB/s | 5.19 MB/s | 0.0031 | 72.00 | - | - | - | - | - | - |
| Brotli Q6 | 50.00 B | 49.00 B | 1.02x | 0.05 | 0.01 | 0.91 MB/s | 6.71 MB/s | 0.0029 | 72.06 | - | - | - | - | - | - |
| Brotli Q7 | 50.00 B | 49.00 B | 1.02x | 0.07 | 0.01 | 0.66 MB/s | 8.23 MB/s | 0.0034 | 72.15 | - | - | - | - | - | - |
| Brotli Q8 | 50.00 B | 49.00 B | 1.02x | 0.07 | 0.01 | 0.64 MB/s | 7.26 MB/s | 0.0028 | 72.25 | - | - | - | - | - | - |
| Brotli Q9 | 50.00 B | 49.00 B | 1.02x | 0.22 | 0.01 | 0.21 MB/s | 4.72 MB/s | 0.0027 | 72.25 | - | - | - | - | - | - |
| Brotli Q10 | 50.00 B | 54.00 B | 0.93x | 0.55 | 0.01 | 0.09 MB/s | 8.52 MB/s | 0.0028 | 72.27 | - | - | - | - | - | - |
| Brotli Q11 | 50.00 B | 54.00 B | 0.93x | 0.49 | 0.01 | 0.10 MB/s | 9.01 MB/s | 0.0026 | 72.27 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 0.00% improvement over 2 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.143860)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: code_python_tiny

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 50.00 B | 65.00 B | 0.77x | 4.91 | 0.24 | 0.01 MB/s | 0.20 MB/s | 0.0031 | 72.28 | 65 | ❌ | 0.180405 | 0.180405 | ❌ | ✅ |
| SHA256 | 50.00 B | 64.00 B | 0.78x | 0.00 | 0.00 | 42.31 MB/s | 0.00 MB/s | 0.0011 | 72.28 | - | - | - | - | - | - |
| AES-GCM | 50.00 B | 66.00 B | 0.76x | 0.11 | 0.05 | 0.42 MB/s | 1.04 MB/s | 0.0029 | 72.28 | - | - | - | - | - | - |
| Frackture Encrypted | 50.00 B | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 50.00 B | 68.00 B | 0.74x | 0.04 | 0.03 | 1.15 MB/s | 1.51 MB/s | 0.0029 | 72.28 | - | - | - | - | - | - |
| Gzip L2 | 50.00 B | 68.00 B | 0.74x | 0.02 | 0.02 | 2.09 MB/s | 2.24 MB/s | 0.0029 | 72.28 | - | - | - | - | - | - |
| Gzip L3 | 50.00 B | 68.00 B | 0.74x | 0.02 | 0.02 | 2.37 MB/s | 2.48 MB/s | 0.0027 | 72.28 | - | - | - | - | - | - |
| Gzip L4 | 50.00 B | 68.00 B | 0.74x | 0.02 | 0.02 | 2.51 MB/s | 2.58 MB/s | 0.0028 | 72.28 | - | - | - | - | - | - |
| Gzip L5 | 50.00 B | 68.00 B | 0.74x | 0.02 | 0.02 | 2.69 MB/s | 2.71 MB/s | 0.0030 | 72.28 | - | - | - | - | - | - |
| Gzip L6 | 50.00 B | 68.00 B | 0.74x | 0.02 | 0.02 | 2.76 MB/s | 2.77 MB/s | 0.0027 | 72.28 | - | - | - | - | - | - |
| Gzip L7 | 50.00 B | 68.00 B | 0.74x | 0.02 | 0.02 | 2.92 MB/s | 2.83 MB/s | 0.0031 | 72.28 | - | - | - | - | - | - |
| Gzip L8 | 50.00 B | 68.00 B | 0.74x | 0.02 | 0.02 | 2.87 MB/s | 2.15 MB/s | 0.0029 | 72.28 | - | - | - | - | - | - |
| Gzip L9 | 50.00 B | 68.00 B | 0.74x | 0.02 | 0.02 | 2.34 MB/s | 2.67 MB/s | 0.0028 | 72.28 | - | - | - | - | - | - |
| Brotli Q0 | 50.00 B | 54.00 B | 0.93x | 0.03 | 0.01 | 1.54 MB/s | 7.34 MB/s | 0.0026 | 72.28 | - | - | - | - | - | - |
| Brotli Q1 | 50.00 B | 54.00 B | 0.93x | 0.02 | 0.00 | 3.12 MB/s | 15.58 MB/s | 0.0031 | 72.28 | - | - | - | - | - | - |
| Brotli Q2 | 50.00 B | 54.00 B | 0.93x | 0.02 | 0.00 | 3.06 MB/s | 13.61 MB/s | 0.0036 | 72.28 | - | - | - | - | - | - |
| Brotli Q3 | 50.00 B | 53.00 B | 0.94x | 0.02 | 0.01 | 2.96 MB/s | 5.68 MB/s | 0.0027 | 72.28 | - | - | - | - | - | - |
| Brotli Q4 | 50.00 B | 53.00 B | 0.94x | 0.03 | 0.01 | 1.73 MB/s | 8.08 MB/s | 0.0027 | 72.28 | - | - | - | - | - | - |
| Brotli Q5 | 50.00 B | 51.00 B | 0.98x | 0.05 | 0.01 | 1.03 MB/s | 7.11 MB/s | 0.0029 | 72.32 | - | - | - | - | - | - |
| Brotli Q6 | 50.00 B | 51.00 B | 0.98x | 0.04 | 0.01 | 1.12 MB/s | 9.46 MB/s | 0.0030 | 72.38 | - | - | - | - | - | - |
| Brotli Q7 | 50.00 B | 51.00 B | 0.98x | 0.07 | 0.01 | 0.67 MB/s | 8.94 MB/s | 0.0026 | 72.49 | - | - | - | - | - | - |
| Brotli Q8 | 50.00 B | 51.00 B | 0.98x | 0.08 | 0.00 | 0.62 MB/s | 10.98 MB/s | 0.0028 | 72.62 | - | - | - | - | - | - |
| Brotli Q9 | 50.00 B | 51.00 B | 0.98x | 0.15 | 0.01 | 0.33 MB/s | 6.74 MB/s | 0.0028 | 72.62 | - | - | - | - | - | - |
| Brotli Q10 | 50.00 B | 43.00 B | 1.16x | 0.43 | 0.01 | 0.11 MB/s | 6.20 MB/s | 0.0029 | 72.62 | - | - | - | - | - | - |
| Brotli Q11 | 50.00 B | 43.00 B | 1.16x | 0.43 | 0.01 | 0.11 MB/s | 5.99 MB/s | 0.0027 | 72.62 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 0.00% improvement over 2 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.180405)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: structured_pickle_tiny

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 50.00 B | 65.00 B | 0.77x | 4.77 | 0.25 | 0.01 MB/s | 0.19 MB/s | 0.0028 | 72.62 | 65 | ❌ | 0.118727 | 0.118727 | ❌ | ✅ |
| SHA256 | 50.00 B | 64.00 B | 0.78x | 0.00 | 0.00 | 39.17 MB/s | 0.00 MB/s | 0.0012 | 72.62 | - | - | - | - | - | - |
| AES-GCM | 50.00 B | 66.00 B | 0.76x | 0.11 | 0.04 | 0.42 MB/s | 1.07 MB/s | 0.0028 | 72.62 | - | - | - | - | - | - |
| Frackture Encrypted | 50.00 B | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 50.00 B | 64.00 B | 0.78x | 0.04 | 0.03 | 1.10 MB/s | 1.47 MB/s | 0.0029 | 72.62 | - | - | - | - | - | - |
| Gzip L2 | 50.00 B | 64.00 B | 0.78x | 0.02 | 0.02 | 2.11 MB/s | 2.25 MB/s | 0.0029 | 72.62 | - | - | - | - | - | - |
| Gzip L3 | 50.00 B | 64.00 B | 0.78x | 0.02 | 0.02 | 1.96 MB/s | 2.34 MB/s | 0.0028 | 72.62 | - | - | - | - | - | - |
| Gzip L4 | 50.00 B | 64.00 B | 0.78x | 0.02 | 0.02 | 2.21 MB/s | 2.59 MB/s | 0.0027 | 72.62 | - | - | - | - | - | - |
| Gzip L5 | 50.00 B | 64.00 B | 0.78x | 0.02 | 0.02 | 2.15 MB/s | 2.04 MB/s | 0.0026 | 72.62 | - | - | - | - | - | - |
| Gzip L6 | 50.00 B | 64.00 B | 0.78x | 0.02 | 0.02 | 2.78 MB/s | 2.93 MB/s | 0.0028 | 72.62 | - | - | - | - | - | - |
| Gzip L7 | 50.00 B | 64.00 B | 0.78x | 0.02 | 0.02 | 2.79 MB/s | 2.86 MB/s | 0.0027 | 72.62 | - | - | - | - | - | - |
| Gzip L8 | 50.00 B | 64.00 B | 0.78x | 0.02 | 0.02 | 2.67 MB/s | 2.65 MB/s | 0.0028 | 72.62 | - | - | - | - | - | - |
| Gzip L9 | 50.00 B | 64.00 B | 0.78x | 0.02 | 0.02 | 2.21 MB/s | 2.58 MB/s | 0.0043 | 72.62 | - | - | - | - | - | - |
| Brotli Q0 | 50.00 B | 54.00 B | 0.93x | 0.03 | 0.01 | 1.45 MB/s | 7.11 MB/s | 0.0030 | 72.62 | - | - | - | - | - | - |
| Brotli Q1 | 50.00 B | 54.00 B | 0.93x | 0.02 | 0.00 | 2.73 MB/s | 13.15 MB/s | 0.0029 | 72.62 | - | - | - | - | - | - |
| Brotli Q2 | 50.00 B | 54.00 B | 0.93x | 0.01 | 0.00 | 3.38 MB/s | 16.15 MB/s | 0.0027 | 72.62 | - | - | - | - | - | - |
| Brotli Q3 | 50.00 B | 52.00 B | 0.96x | 0.02 | 0.01 | 2.49 MB/s | 5.62 MB/s | 0.0027 | 72.62 | - | - | - | - | - | - |
| Brotli Q4 | 50.00 B | 54.00 B | 0.93x | 0.03 | 0.01 | 1.71 MB/s | 6.09 MB/s | 0.0038 | 72.62 | - | - | - | - | - | - |
| Brotli Q5 | 50.00 B | 53.00 B | 0.94x | 0.05 | 0.01 | 0.97 MB/s | 5.71 MB/s | 0.0031 | 72.65 | - | - | - | - | - | - |
| Brotli Q6 | 50.00 B | 53.00 B | 0.94x | 0.04 | 0.01 | 1.20 MB/s | 7.91 MB/s | 0.0027 | 72.69 | - | - | - | - | - | - |
| Brotli Q7 | 50.00 B | 53.00 B | 0.94x | 0.07 | 0.01 | 0.69 MB/s | 9.02 MB/s | 0.0027 | 72.80 | - | - | - | - | - | - |
| Brotli Q8 | 50.00 B | 53.00 B | 0.94x | 0.07 | 0.00 | 0.64 MB/s | 11.96 MB/s | 0.0028 | 72.93 | - | - | - | - | - | - |
| Brotli Q9 | 50.00 B | 53.00 B | 0.94x | 0.14 | 0.01 | 0.34 MB/s | 7.09 MB/s | 0.0028 | 72.93 | - | - | - | - | - | - |
| Brotli Q10 | 50.00 B | 54.00 B | 0.93x | 0.54 | 0.00 | 0.09 MB/s | 10.09 MB/s | 0.0031 | 72.95 | - | - | - | - | - | - |
| Brotli Q11 | 50.00 B | 54.00 B | 0.93x | 0.50 | 0.01 | 0.10 MB/s | 9.50 MB/s | 0.0026 | 72.95 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 0.00% improvement over 2 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.118727)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: text_plain_tiny

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 50.00 B | 65.00 B | 0.77x | 4.75 | 0.24 | 0.01 MB/s | 0.20 MB/s | 0.0027 | 72.95 | 65 | ❌ | 0.142766 | 0.142766 | ❌ | ✅ |
| SHA256 | 50.00 B | 64.00 B | 0.78x | 0.00 | 0.00 | 42.14 MB/s | 0.00 MB/s | 0.0011 | 72.95 | - | - | - | - | - | - |
| AES-GCM | 50.00 B | 66.00 B | 0.76x | 0.11 | 0.05 | 0.44 MB/s | 1.05 MB/s | 0.0028 | 72.95 | - | - | - | - | - | - |
| Frackture Encrypted | 50.00 B | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 50.00 B | 69.00 B | 0.72x | 0.04 | 0.03 | 1.12 MB/s | 1.55 MB/s | 0.0027 | 72.95 | - | - | - | - | - | - |
| Gzip L2 | 50.00 B | 69.00 B | 0.72x | 0.02 | 0.04 | 2.30 MB/s | 1.29 MB/s | 0.0028 | 72.95 | - | - | - | - | - | - |
| Gzip L3 | 50.00 B | 69.00 B | 0.72x | 0.02 | 0.02 | 2.47 MB/s | 2.46 MB/s | 0.0028 | 72.95 | - | - | - | - | - | - |
| Gzip L4 | 50.00 B | 69.00 B | 0.72x | 0.02 | 0.02 | 2.58 MB/s | 2.66 MB/s | 0.0031 | 72.95 | - | - | - | - | - | - |
| Gzip L5 | 50.00 B | 69.00 B | 0.72x | 0.02 | 0.02 | 2.72 MB/s | 2.80 MB/s | 0.0027 | 72.95 | - | - | - | - | - | - |
| Gzip L6 | 50.00 B | 69.00 B | 0.72x | 0.02 | 0.02 | 3.01 MB/s | 2.99 MB/s | 0.0028 | 72.95 | - | - | - | - | - | - |
| Gzip L7 | 50.00 B | 69.00 B | 0.72x | 0.02 | 0.02 | 2.82 MB/s | 2.81 MB/s | 0.0028 | 72.95 | - | - | - | - | - | - |
| Gzip L8 | 50.00 B | 69.00 B | 0.72x | 0.02 | 0.02 | 2.91 MB/s | 2.70 MB/s | 0.0026 | 72.95 | - | - | - | - | - | - |
| Gzip L9 | 50.00 B | 69.00 B | 0.72x | 0.02 | 0.02 | 2.73 MB/s | 2.92 MB/s | 0.0029 | 72.95 | - | - | - | - | - | - |
| Brotli Q0 | 50.00 B | 54.00 B | 0.93x | 0.03 | 0.01 | 1.53 MB/s | 7.88 MB/s | 0.0032 | 72.95 | - | - | - | - | - | - |
| Brotli Q1 | 50.00 B | 54.00 B | 0.93x | 0.02 | 0.00 | 2.79 MB/s | 13.34 MB/s | 0.0027 | 72.95 | - | - | - | - | - | - |
| Brotli Q2 | 50.00 B | 54.00 B | 0.93x | 0.01 | 0.00 | 3.71 MB/s | 17.41 MB/s | 0.0028 | 72.95 | - | - | - | - | - | - |
| Brotli Q3 | 50.00 B | 52.00 B | 0.96x | 0.02 | 0.01 | 2.88 MB/s | 6.50 MB/s | 0.0028 | 72.95 | - | - | - | - | - | - |
| Brotli Q4 | 50.00 B | 53.00 B | 0.94x | 0.03 | 0.01 | 1.65 MB/s | 8.49 MB/s | 0.0028 | 72.95 | - | - | - | - | - | - |
| Brotli Q5 | 50.00 B | 51.00 B | 0.98x | 0.07 | 0.01 | 0.71 MB/s | 7.98 MB/s | 0.0027 | 73.00 | - | - | - | - | - | - |
| Brotli Q6 | 50.00 B | 51.00 B | 0.98x | 0.04 | 0.00 | 1.11 MB/s | 11.08 MB/s | 0.0030 | 73.05 | - | - | - | - | - | - |
| Brotli Q7 | 50.00 B | 51.00 B | 0.98x | 0.48 | 0.01 | 0.10 MB/s | 4.99 MB/s | 0.0038 | 73.20 | - | - | - | - | - | - |
| Brotli Q8 | 50.00 B | 51.00 B | 0.98x | 0.32 | 0.01 | 0.15 MB/s | 6.01 MB/s | 0.0027 | 73.36 | - | - | - | - | - | - |
| Brotli Q9 | 50.00 B | 51.00 B | 0.98x | 0.17 | 0.01 | 0.28 MB/s | 5.46 MB/s | 0.0027 | 73.36 | - | - | - | - | - | - |
| Brotli Q10 | 50.00 B | 54.00 B | 0.93x | 0.49 | 0.01 | 0.10 MB/s | 9.47 MB/s | 0.0028 | 73.36 | - | - | - | - | - | - |
| Brotli Q11 | 50.00 B | 54.00 B | 0.93x | 0.43 | 0.00 | 0.11 MB/s | 10.22 MB/s | 0.0027 | 73.36 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 0.00% improvement over 2 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.142766)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: text_log_tiny

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 50.00 B | 65.00 B | 0.77x | 4.89 | 0.22 | 0.01 MB/s | 0.21 MB/s | 0.0027 | 73.37 | 65 | ❌ | 0.168634 | 0.168634 | ❌ | ✅ |
| SHA256 | 50.00 B | 64.00 B | 0.78x | 0.00 | 0.00 | 41.95 MB/s | 0.00 MB/s | 0.0011 | 73.37 | - | - | - | - | - | - |
| AES-GCM | 50.00 B | 66.00 B | 0.76x | 0.11 | 0.05 | 0.44 MB/s | 1.03 MB/s | 0.0028 | 73.37 | - | - | - | - | - | - |
| Frackture Encrypted | 50.00 B | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 50.00 B | 65.00 B | 0.77x | 0.04 | 0.06 | 1.15 MB/s | 0.79 MB/s | 0.0028 | 73.37 | - | - | - | - | - | - |
| Gzip L2 | 50.00 B | 65.00 B | 0.77x | 0.02 | 0.02 | 2.13 MB/s | 2.32 MB/s | 0.0029 | 73.37 | - | - | - | - | - | - |
| Gzip L3 | 50.00 B | 65.00 B | 0.77x | 0.02 | 0.02 | 2.42 MB/s | 2.54 MB/s | 0.0030 | 73.37 | - | - | - | - | - | - |
| Gzip L4 | 50.00 B | 65.00 B | 0.77x | 0.02 | 0.02 | 2.15 MB/s | 2.43 MB/s | 0.0027 | 73.37 | - | - | - | - | - | - |
| Gzip L5 | 50.00 B | 65.00 B | 0.77x | 0.02 | 0.02 | 2.78 MB/s | 2.86 MB/s | 0.0032 | 73.37 | - | - | - | - | - | - |
| Gzip L6 | 50.00 B | 65.00 B | 0.77x | 0.02 | 0.02 | 2.51 MB/s | 2.54 MB/s | 0.0028 | 73.37 | - | - | - | - | - | - |
| Gzip L7 | 50.00 B | 65.00 B | 0.77x | 0.02 | 0.02 | 2.72 MB/s | 2.71 MB/s | 0.0026 | 73.37 | - | - | - | - | - | - |
| Gzip L8 | 50.00 B | 65.00 B | 0.77x | 0.02 | 0.02 | 2.59 MB/s | 2.55 MB/s | 0.0027 | 73.37 | - | - | - | - | - | - |
| Gzip L9 | 50.00 B | 65.00 B | 0.77x | 0.02 | 0.02 | 2.53 MB/s | 2.65 MB/s | 0.0030 | 73.37 | - | - | - | - | - | - |
| Brotli Q0 | 50.00 B | 54.00 B | 0.93x | 0.03 | 0.01 | 1.50 MB/s | 7.63 MB/s | 0.0028 | 73.37 | - | - | - | - | - | - |
| Brotli Q1 | 50.00 B | 54.00 B | 0.93x | 0.02 | 0.00 | 2.88 MB/s | 15.94 MB/s | 0.0026 | 73.37 | - | - | - | - | - | - |
| Brotli Q2 | 50.00 B | 54.00 B | 0.93x | 0.01 | 0.00 | 3.64 MB/s | 21.50 MB/s | 0.0028 | 73.37 | - | - | - | - | - | - |
| Brotli Q3 | 50.00 B | 54.00 B | 0.93x | 0.02 | 0.00 | 2.41 MB/s | 19.13 MB/s | 0.0029 | 73.37 | - | - | - | - | - | - |
| Brotli Q4 | 50.00 B | 54.00 B | 0.93x | 0.03 | 0.01 | 1.71 MB/s | 5.86 MB/s | 0.0027 | 73.37 | - | - | - | - | - | - |
| Brotli Q5 | 50.00 B | 54.00 B | 0.93x | 0.04 | 0.00 | 1.20 MB/s | 15.65 MB/s | 0.0031 | 73.38 | - | - | - | - | - | - |
| Brotli Q6 | 50.00 B | 54.00 B | 0.93x | 0.06 | 0.00 | 0.82 MB/s | 16.51 MB/s | 0.0028 | 73.47 | - | - | - | - | - | - |
| Brotli Q7 | 50.00 B | 54.00 B | 0.93x | 0.08 | 0.00 | 0.61 MB/s | 18.30 MB/s | 0.0026 | 73.60 | - | - | - | - | - | - |
| Brotli Q8 | 50.00 B | 54.00 B | 0.93x | 0.10 | 0.00 | 0.49 MB/s | 17.12 MB/s | 0.0027 | 73.75 | - | - | - | - | - | - |
| Brotli Q9 | 50.00 B | 54.00 B | 0.93x | 0.15 | 0.00 | 0.32 MB/s | 12.95 MB/s | 0.0040 | 73.75 | - | - | - | - | - | - |
| Brotli Q10 | 50.00 B | 54.00 B | 0.93x | 0.53 | 0.01 | 0.09 MB/s | 8.48 MB/s | 0.0027 | 73.76 | - | - | - | - | - | - |
| Brotli Q11 | 50.00 B | 54.00 B | 0.93x | 0.40 | 0.00 | 0.12 MB/s | 11.94 MB/s | 0.0028 | 73.76 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 0.00% improvement over 2 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.168634)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: text_json_tiny

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 50.00 B | 65.00 B | 0.77x | 4.76 | 0.22 | 0.01 MB/s | 0.22 MB/s | 0.0027 | 73.76 | 65 | ❌ | 0.126942 | 0.126942 | ❌ | ✅ |
| SHA256 | 50.00 B | 64.00 B | 0.78x | 0.00 | 0.00 | 36.98 MB/s | 0.00 MB/s | 0.0013 | 73.76 | - | - | - | - | - | - |
| AES-GCM | 50.00 B | 66.00 B | 0.76x | 0.12 | 0.05 | 0.41 MB/s | 1.03 MB/s | 0.0028 | 73.76 | - | - | - | - | - | - |
| Frackture Encrypted | 50.00 B | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 50.00 B | 55.00 B | 0.91x | 0.04 | 0.03 | 1.19 MB/s | 1.53 MB/s | 0.0029 | 73.76 | - | - | - | - | - | - |
| Gzip L2 | 50.00 B | 55.00 B | 0.91x | 0.02 | 0.02 | 2.14 MB/s | 2.27 MB/s | 0.0029 | 73.76 | - | - | - | - | - | - |
| Gzip L3 | 50.00 B | 55.00 B | 0.91x | 0.02 | 0.02 | 2.09 MB/s | 2.44 MB/s | 0.0026 | 73.76 | - | - | - | - | - | - |
| Gzip L4 | 50.00 B | 55.00 B | 0.91x | 0.03 | 0.02 | 1.89 MB/s | 2.50 MB/s | 0.0027 | 73.76 | - | - | - | - | - | - |
| Gzip L5 | 50.00 B | 55.00 B | 0.91x | 0.02 | 0.02 | 2.82 MB/s | 2.91 MB/s | 0.0028 | 73.76 | - | - | - | - | - | - |
| Gzip L6 | 50.00 B | 55.00 B | 0.91x | 0.02 | 0.02 | 2.96 MB/s | 2.86 MB/s | 0.0028 | 73.76 | - | - | - | - | - | - |
| Gzip L7 | 50.00 B | 55.00 B | 0.91x | 0.02 | 0.02 | 2.90 MB/s | 2.78 MB/s | 0.0027 | 73.76 | - | - | - | - | - | - |
| Gzip L8 | 50.00 B | 55.00 B | 0.91x | 0.02 | 0.02 | 2.98 MB/s | 2.89 MB/s | 0.0030 | 73.76 | - | - | - | - | - | - |
| Gzip L9 | 50.00 B | 55.00 B | 0.91x | 0.02 | 0.02 | 2.89 MB/s | 2.73 MB/s | 0.0030 | 73.76 | - | - | - | - | - | - |
| Brotli Q0 | 50.00 B | 54.00 B | 0.93x | 0.03 | 0.01 | 1.48 MB/s | 8.51 MB/s | 0.0027 | 73.76 | - | - | - | - | - | - |
| Brotli Q1 | 50.00 B | 54.00 B | 0.93x | 0.02 | 0.00 | 2.96 MB/s | 15.87 MB/s | 0.0029 | 73.76 | - | - | - | - | - | - |
| Brotli Q2 | 50.00 B | 54.00 B | 0.93x | 0.01 | 0.00 | 3.34 MB/s | 16.96 MB/s | 0.0028 | 73.76 | - | - | - | - | - | - |
| Brotli Q3 | 50.00 B | 46.00 B | 1.09x | 0.02 | 0.01 | 2.38 MB/s | 5.60 MB/s | 0.0028 | 73.76 | - | - | - | - | - | - |
| Brotli Q4 | 50.00 B | 46.00 B | 1.09x | 0.03 | 0.01 | 1.87 MB/s | 9.01 MB/s | 0.0027 | 73.76 | - | - | - | - | - | - |
| Brotli Q5 | 50.00 B | 50.00 B | 1.00x | 0.03 | 0.01 | 1.38 MB/s | 7.23 MB/s | 0.0030 | 73.77 | - | - | - | - | - | - |
| Brotli Q6 | 50.00 B | 50.00 B | 1.00x | 0.04 | 0.01 | 1.07 MB/s | 8.24 MB/s | 0.0028 | 73.81 | - | - | - | - | - | - |
| Brotli Q7 | 50.00 B | 52.00 B | 0.96x | 0.06 | 0.01 | 0.74 MB/s | 7.64 MB/s | 0.0027 | 73.91 | - | - | - | - | - | - |
| Brotli Q8 | 50.00 B | 52.00 B | 0.96x | 0.09 | 0.01 | 0.51 MB/s | 9.15 MB/s | 0.0028 | 74.05 | - | - | - | - | - | - |
| Brotli Q9 | 50.00 B | 46.00 B | 1.09x | 0.13 | 0.01 | 0.35 MB/s | 6.15 MB/s | 0.0028 | 74.05 | - | - | - | - | - | - |
| Brotli Q10 | 50.00 B | 48.00 B | 1.04x | 0.45 | 0.01 | 0.11 MB/s | 5.18 MB/s | 0.0034 | 74.05 | - | - | - | - | - | - |
| Brotli Q11 | 50.00 B | 48.00 B | 1.04x | 0.47 | 0.01 | 0.10 MB/s | 4.52 MB/s | 0.0026 | 74.05 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 0.00% improvement over 2 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.126942)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: text_csv_tiny

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 50.00 B | 65.00 B | 0.77x | 4.67 | 0.31 | 0.01 MB/s | 0.15 MB/s | 0.0027 | 74.07 | 65 | ❌ | 0.128671 | 0.128671 | ❌ | ✅ |
| SHA256 | 50.00 B | 64.00 B | 0.78x | 0.00 | 0.00 | 41.39 MB/s | 0.00 MB/s | 0.0012 | 74.07 | - | - | - | - | - | - |
| AES-GCM | 50.00 B | 66.00 B | 0.76x | 0.11 | 0.06 | 0.43 MB/s | 0.81 MB/s | 0.0029 | 74.07 | - | - | - | - | - | - |
| Frackture Encrypted | 50.00 B | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 50.00 B | 69.00 B | 0.72x | 0.07 | 0.04 | 0.73 MB/s | 1.23 MB/s | 0.0027 | 74.07 | - | - | - | - | - | - |
| Gzip L2 | 50.00 B | 69.00 B | 0.72x | 0.02 | 0.02 | 2.17 MB/s | 2.28 MB/s | 0.0028 | 74.07 | - | - | - | - | - | - |
| Gzip L3 | 50.00 B | 69.00 B | 0.72x | 0.02 | 0.02 | 2.38 MB/s | 2.41 MB/s | 0.0030 | 74.07 | - | - | - | - | - | - |
| Gzip L4 | 50.00 B | 69.00 B | 0.72x | 0.02 | 0.02 | 2.50 MB/s | 2.12 MB/s | 0.0026 | 74.07 | - | - | - | - | - | - |
| Gzip L5 | 50.00 B | 69.00 B | 0.72x | 0.02 | 0.02 | 2.65 MB/s | 2.72 MB/s | 0.0028 | 74.07 | - | - | - | - | - | - |
| Gzip L6 | 50.00 B | 69.00 B | 0.72x | 0.02 | 0.02 | 2.73 MB/s | 2.76 MB/s | 0.0029 | 74.07 | - | - | - | - | - | - |
| Gzip L7 | 50.00 B | 69.00 B | 0.72x | 0.02 | 0.02 | 2.82 MB/s | 2.72 MB/s | 0.0027 | 74.07 | - | - | - | - | - | - |
| Gzip L8 | 50.00 B | 69.00 B | 0.72x | 0.02 | 0.03 | 2.87 MB/s | 1.38 MB/s | 0.0027 | 74.07 | - | - | - | - | - | - |
| Gzip L9 | 50.00 B | 69.00 B | 0.72x | 0.02 | 0.02 | 2.95 MB/s | 2.79 MB/s | 0.0030 | 74.07 | - | - | - | - | - | - |
| Brotli Q0 | 50.00 B | 54.00 B | 0.93x | 0.03 | 0.01 | 1.48 MB/s | 7.55 MB/s | 0.0027 | 74.07 | - | - | - | - | - | - |
| Brotli Q1 | 50.00 B | 54.00 B | 0.93x | 0.02 | 0.00 | 3.03 MB/s | 15.17 MB/s | 0.0027 | 74.07 | - | - | - | - | - | - |
| Brotli Q2 | 50.00 B | 54.00 B | 0.93x | 0.01 | 0.00 | 3.61 MB/s | 21.25 MB/s | 0.0029 | 74.07 | - | - | - | - | - | - |
| Brotli Q3 | 50.00 B | 52.00 B | 0.96x | 0.02 | 0.01 | 3.04 MB/s | 6.33 MB/s | 0.0029 | 74.07 | - | - | - | - | - | - |
| Brotli Q4 | 50.00 B | 48.00 B | 1.04x | 0.03 | 0.01 | 1.62 MB/s | 7.45 MB/s | 0.0027 | 74.07 | - | - | - | - | - | - |
| Brotli Q5 | 50.00 B | 49.00 B | 1.02x | 0.04 | 0.01 | 1.18 MB/s | 8.19 MB/s | 0.0030 | 74.09 | - | - | - | - | - | - |
| Brotli Q6 | 50.00 B | 49.00 B | 1.02x | 0.05 | 0.00 | 0.94 MB/s | 9.88 MB/s | 0.0028 | 74.17 | - | - | - | - | - | - |
| Brotli Q7 | 50.00 B | 49.00 B | 1.02x | 0.08 | 0.00 | 0.62 MB/s | 10.10 MB/s | 0.0027 | 74.29 | - | - | - | - | - | - |
| Brotli Q8 | 50.00 B | 49.00 B | 1.02x | 0.12 | 0.01 | 0.41 MB/s | 9.22 MB/s | 0.0027 | 74.45 | - | - | - | - | - | - |
| Brotli Q9 | 50.00 B | 49.00 B | 1.02x | 0.15 | 0.01 | 0.32 MB/s | 6.72 MB/s | 0.0028 | 74.45 | - | - | - | - | - | - |
| Brotli Q10 | 50.00 B | 51.00 B | 0.98x | 0.51 | 0.01 | 0.09 MB/s | 4.72 MB/s | 0.0028 | 74.45 | - | - | - | - | - | - |
| Brotli Q11 | 50.00 B | 51.00 B | 0.98x | 0.43 | 0.01 | 0.11 MB/s | 5.18 MB/s | 0.0029 | 74.45 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 0.00% improvement over 2 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.128671)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: binary_png_small

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 1.00 KB | 65.00 B | 15.75x | 6.10 | 0.24 | 0.16 MB/s | 4.14 MB/s | 0.0040 | 74.46 | 65 | ❌ | 0.126382 | 0.120252 | ❌ | ✅ |
| SHA256 | 1.00 KB | 64.00 B | 16.00x | 0.00 | 0.00 | 492.80 MB/s | 0.00 MB/s | 0.0020 | 74.46 | - | - | - | - | - | - |
| AES-GCM | 1.00 KB | 1.02 KB | 0.98x | 0.14 | 0.11 | 7.16 MB/s | 8.66 MB/s | 0.0040 | 74.56 | - | - | - | - | - | - |
| Frackture Encrypted | 1.00 KB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 1.00 KB | 95.00 B | 10.78x | 0.05 | 0.04 | 19.09 MB/s | 27.53 MB/s | 0.0040 | 74.56 | - | - | - | - | - | - |
| Gzip L2 | 1.00 KB | 92.00 B | 11.13x | 0.03 | 0.02 | 34.09 MB/s | 39.91 MB/s | 0.0044 | 74.56 | - | - | - | - | - | - |
| Gzip L3 | 1.00 KB | 92.00 B | 11.13x | 0.03 | 0.02 | 32.12 MB/s | 39.32 MB/s | 0.0040 | 74.56 | - | - | - | - | - | - |
| Gzip L4 | 1.00 KB | 91.00 B | 11.25x | 0.03 | 0.02 | 32.79 MB/s | 45.13 MB/s | 0.0039 | 74.56 | - | - | - | - | - | - |
| Gzip L5 | 1.00 KB | 91.00 B | 11.25x | 0.02 | 0.02 | 39.61 MB/s | 47.63 MB/s | 0.0039 | 74.56 | - | - | - | - | - | - |
| Gzip L6 | 1.00 KB | 91.00 B | 11.25x | 0.02 | 0.02 | 42.14 MB/s | 48.42 MB/s | 0.0041 | 74.56 | - | - | - | - | - | - |
| Gzip L7 | 1.00 KB | 91.00 B | 11.25x | 0.02 | 0.02 | 43.60 MB/s | 45.40 MB/s | 0.0039 | 74.56 | - | - | - | - | - | - |
| Gzip L8 | 1.00 KB | 91.00 B | 11.25x | 0.02 | 0.02 | 44.79 MB/s | 48.98 MB/s | 0.0040 | 74.56 | - | - | - | - | - | - |
| Gzip L9 | 1.00 KB | 91.00 B | 11.25x | 0.02 | 0.02 | 43.11 MB/s | 45.77 MB/s | 0.0040 | 74.56 | - | - | - | - | - | - |
| Brotli Q0 | 1.00 KB | 155.00 B | 6.61x | 0.04 | 0.02 | 25.94 MB/s | 55.63 MB/s | 0.0041 | 74.56 | - | - | - | - | - | - |
| Brotli Q1 | 1.00 KB | 111.00 B | 9.23x | 0.02 | 0.01 | 47.73 MB/s | 100.06 MB/s | 0.0040 | 74.56 | - | - | - | - | - | - |
| Brotli Q2 | 1.00 KB | 108.00 B | 9.48x | 0.02 | 0.01 | 53.74 MB/s | 96.21 MB/s | 0.0040 | 74.56 | - | - | - | - | - | - |
| Brotli Q3 | 1.00 KB | 80.00 B | 12.80x | 0.02 | 0.01 | 39.78 MB/s | 138.50 MB/s | 0.0037 | 74.56 | - | - | - | - | - | - |
| Brotli Q4 | 1.00 KB | 79.00 B | 12.96x | 0.04 | 0.01 | 24.40 MB/s | 84.42 MB/s | 0.0037 | 74.56 | - | - | - | - | - | - |
| Brotli Q5 | 1.00 KB | 87.00 B | 11.77x | 0.11 | 0.01 | 9.24 MB/s | 114.73 MB/s | 0.0037 | 74.61 | - | - | - | - | - | - |
| Brotli Q6 | 1.00 KB | 87.00 B | 11.77x | 0.07 | 0.01 | 13.75 MB/s | 147.65 MB/s | 0.0039 | 74.70 | - | - | - | - | - | - |
| Brotli Q7 | 1.00 KB | 91.00 B | 11.25x | 0.12 | 0.01 | 8.42 MB/s | 123.83 MB/s | 0.0039 | 74.88 | - | - | - | - | - | - |
| Brotli Q8 | 1.00 KB | 91.00 B | 11.25x | 0.13 | 0.02 | 7.65 MB/s | 41.50 MB/s | 0.0039 | 75.07 | - | - | - | - | - | - |
| Brotli Q9 | 1.00 KB | 90.00 B | 11.38x | 0.28 | 0.01 | 3.49 MB/s | 75.54 MB/s | 0.0038 | 75.07 | - | - | - | - | - | - |
| Brotli Q10 | 1.00 KB | 81.00 B | 12.64x | 0.76 | 0.01 | 1.28 MB/s | 80.35 MB/s | 0.0040 | 75.07 | - | - | - | - | - | - |
| Brotli Q11 | 1.00 KB | 81.00 B | 12.64x | 0.72 | 0.01 | 1.36 MB/s | 85.45 MB/s | 0.0042 | 75.07 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 4.85% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.126382)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: binary_jpeg_small

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 1.00 KB | 65.00 B | 15.75x | 5.71 | 0.22 | 0.17 MB/s | 4.41 MB/s | 0.0041 | 75.09 | 65 | ❌ | 0.129295 | 0.122793 | ❌ | ✅ |
| SHA256 | 1.00 KB | 64.00 B | 16.00x | 0.00 | 0.00 | 496.67 MB/s | 0.00 MB/s | 0.0020 | 75.09 | - | - | - | - | - | - |
| AES-GCM | 1.00 KB | 1.02 KB | 0.98x | 0.12 | 0.05 | 7.85 MB/s | 18.77 MB/s | 0.0040 | 75.09 | - | - | - | - | - | - |
| Frackture Encrypted | 1.00 KB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 1.00 KB | 154.00 B | 6.65x | 0.06 | 0.04 | 16.90 MB/s | 26.15 MB/s | 0.0041 | 75.09 | - | - | - | - | - | - |
| Gzip L2 | 1.00 KB | 154.00 B | 6.65x | 0.03 | 0.03 | 30.33 MB/s | 34.75 MB/s | 0.0041 | 75.09 | - | - | - | - | - | - |
| Gzip L3 | 1.00 KB | 154.00 B | 6.65x | 0.03 | 0.02 | 33.92 MB/s | 41.97 MB/s | 0.0039 | 75.09 | - | - | - | - | - | - |
| Gzip L4 | 1.00 KB | 151.00 B | 6.78x | 0.05 | 0.03 | 20.77 MB/s | 30.66 MB/s | 0.0041 | 75.09 | - | - | - | - | - | - |
| Gzip L5 | 1.00 KB | 151.00 B | 6.78x | 0.03 | 0.02 | 31.07 MB/s | 44.39 MB/s | 0.0039 | 75.09 | - | - | - | - | - | - |
| Gzip L6 | 1.00 KB | 151.00 B | 6.78x | 0.03 | 0.02 | 37.27 MB/s | 46.32 MB/s | 0.0042 | 75.09 | - | - | - | - | - | - |
| Gzip L7 | 1.00 KB | 151.00 B | 6.78x | 0.02 | 0.02 | 39.80 MB/s | 46.76 MB/s | 0.0039 | 75.09 | - | - | - | - | - | - |
| Gzip L8 | 1.00 KB | 151.00 B | 6.78x | 0.02 | 0.02 | 39.79 MB/s | 47.40 MB/s | 0.0038 | 75.09 | - | - | - | - | - | - |
| Gzip L9 | 1.00 KB | 151.00 B | 6.78x | 0.02 | 0.02 | 39.98 MB/s | 45.38 MB/s | 0.0040 | 75.09 | - | - | - | - | - | - |
| Brotli Q0 | 1.00 KB | 204.00 B | 5.02x | 0.06 | 0.02 | 15.56 MB/s | 53.99 MB/s | 0.0038 | 75.09 | - | - | - | - | - | - |
| Brotli Q1 | 1.00 KB | 159.00 B | 6.44x | 0.02 | 0.01 | 46.24 MB/s | 83.00 MB/s | 0.0038 | 75.09 | - | - | - | - | - | - |
| Brotli Q2 | 1.00 KB | 156.00 B | 6.56x | 0.02 | 0.01 | 43.94 MB/s | 88.72 MB/s | 0.0039 | 75.09 | - | - | - | - | - | - |
| Brotli Q3 | 1.00 KB | 129.00 B | 7.94x | 0.03 | 0.01 | 34.81 MB/s | 126.74 MB/s | 0.0040 | 75.09 | - | - | - | - | - | - |
| Brotli Q4 | 1.00 KB | 115.00 B | 8.90x | 0.04 | 0.01 | 23.08 MB/s | 138.11 MB/s | 0.0039 | 75.09 | - | - | - | - | - | - |
| Brotli Q5 | 1.00 KB | 126.00 B | 8.13x | 0.06 | 0.01 | 15.46 MB/s | 122.79 MB/s | 0.0042 | 75.12 | - | - | - | - | - | - |
| Brotli Q6 | 1.00 KB | 126.00 B | 8.13x | 0.11 | 0.01 | 9.22 MB/s | 93.50 MB/s | 0.0039 | 75.26 | - | - | - | - | - | - |
| Brotli Q7 | 1.00 KB | 128.00 B | 8.00x | 0.16 | 0.01 | 6.18 MB/s | 109.46 MB/s | 0.0039 | 75.52 | - | - | - | - | - | - |
| Brotli Q8 | 1.00 KB | 128.00 B | 8.00x | 0.21 | 0.01 | 4.73 MB/s | 112.75 MB/s | 0.0041 | 75.88 | - | - | - | - | - | - |
| Brotli Q9 | 1.00 KB | 128.00 B | 8.00x | 0.39 | 0.01 | 2.49 MB/s | 83.54 MB/s | 0.0038 | 75.88 | - | - | - | - | - | - |
| Brotli Q10 | 1.00 KB | 130.00 B | 7.88x | 0.70 | 0.01 | 1.40 MB/s | 65.60 MB/s | 0.0041 | 75.89 | - | - | - | - | - | - |
| Brotli Q11 | 1.00 KB | 130.00 B | 7.88x | 0.75 | 0.02 | 1.31 MB/s | 57.59 MB/s | 0.0041 | 75.89 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 5.03% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.129295)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: binary_pdf_small

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 1.00 KB | 65.00 B | 15.75x | 5.75 | 0.22 | 0.17 MB/s | 4.43 MB/s | 0.0071 | 75.90 | 65 | ❌ | 0.159119 | 0.149942 | ❌ | ✅ |
| SHA256 | 1.00 KB | 64.00 B | 16.00x | 0.00 | 0.00 | 360.67 MB/s | 0.00 MB/s | 0.0027 | 75.90 | - | - | - | - | - | - |
| AES-GCM | 1.00 KB | 1.02 KB | 0.98x | 0.16 | 0.08 | 5.96 MB/s | 12.01 MB/s | 0.0062 | 75.90 | - | - | - | - | - | - |
| Frackture Encrypted | 1.00 KB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 1.00 KB | 298.00 B | 3.44x | 0.08 | 0.06 | 11.80 MB/s | 17.00 MB/s | 0.0051 | 75.90 | - | - | - | - | - | - |
| Gzip L2 | 1.00 KB | 293.00 B | 3.49x | 0.06 | 0.04 | 16.03 MB/s | 25.14 MB/s | 0.0040 | 75.90 | - | - | - | - | - | - |
| Gzip L3 | 1.00 KB | 290.00 B | 3.53x | 0.04 | 0.03 | 24.43 MB/s | 32.86 MB/s | 0.0040 | 75.90 | - | - | - | - | - | - |
| Gzip L4 | 1.00 KB | 289.00 B | 3.54x | 0.04 | 0.03 | 22.95 MB/s | 34.39 MB/s | 0.0041 | 75.90 | - | - | - | - | - | - |
| Gzip L5 | 1.00 KB | 284.00 B | 3.61x | 0.05 | 0.03 | 20.79 MB/s | 32.25 MB/s | 0.0039 | 75.90 | - | - | - | - | - | - |
| Gzip L6 | 1.00 KB | 284.00 B | 3.61x | 0.04 | 0.03 | 25.96 MB/s | 35.56 MB/s | 0.0039 | 75.90 | - | - | - | - | - | - |
| Gzip L7 | 1.00 KB | 284.00 B | 3.61x | 0.03 | 0.03 | 29.69 MB/s | 37.31 MB/s | 0.0041 | 75.90 | - | - | - | - | - | - |
| Gzip L8 | 1.00 KB | 284.00 B | 3.61x | 0.04 | 0.03 | 27.12 MB/s | 34.52 MB/s | 0.0042 | 75.90 | - | - | - | - | - | - |
| Gzip L9 | 1.00 KB | 284.00 B | 3.61x | 0.03 | 0.03 | 31.63 MB/s | 37.09 MB/s | 0.0039 | 75.90 | - | - | - | - | - | - |
| Brotli Q0 | 1.00 KB | 340.00 B | 3.01x | 0.04 | 0.02 | 21.89 MB/s | 49.25 MB/s | 0.0039 | 75.90 | - | - | - | - | - | - |
| Brotli Q1 | 1.00 KB | 301.00 B | 3.40x | 0.03 | 0.01 | 36.08 MB/s | 84.34 MB/s | 0.0040 | 75.90 | - | - | - | - | - | - |
| Brotli Q2 | 1.00 KB | 278.00 B | 3.68x | 0.03 | 0.01 | 34.63 MB/s | 75.02 MB/s | 0.0041 | 75.90 | - | - | - | - | - | - |
| Brotli Q3 | 1.00 KB | 269.00 B | 3.81x | 0.04 | 0.01 | 24.29 MB/s | 93.61 MB/s | 0.0040 | 75.90 | - | - | - | - | - | - |
| Brotli Q4 | 1.00 KB | 267.00 B | 3.84x | 0.07 | 0.01 | 13.73 MB/s | 95.11 MB/s | 0.0041 | 75.90 | - | - | - | - | - | - |
| Brotli Q5 | 1.00 KB | 250.00 B | 4.10x | 0.10 | 0.01 | 9.45 MB/s | 91.20 MB/s | 0.0039 | 75.94 | - | - | - | - | - | - |
| Brotli Q6 | 1.00 KB | 250.00 B | 4.10x | 0.12 | 0.01 | 8.12 MB/s | 102.70 MB/s | 0.0041 | 76.08 | - | - | - | - | - | - |
| Brotli Q7 | 1.00 KB | 250.00 B | 4.10x | 0.27 | 0.01 | 3.67 MB/s | 102.52 MB/s | 0.0039 | 76.58 | - | - | - | - | - | - |
| Brotli Q8 | 1.00 KB | 250.00 B | 4.10x | 0.39 | 0.01 | 2.48 MB/s | 106.16 MB/s | 0.0039 | 77.33 | - | - | - | - | - | - |
| Brotli Q9 | 1.00 KB | 250.00 B | 4.10x | 0.65 | 0.01 | 1.49 MB/s | 75.15 MB/s | 0.0043 | 77.33 | - | - | - | - | - | - |
| Brotli Q10 | 1.00 KB | 227.00 B | 4.51x | 1.13 | 0.02 | 0.86 MB/s | 60.55 MB/s | 0.0040 | 77.33 | - | - | - | - | - | - |
| Brotli Q11 | 1.00 KB | 229.00 B | 4.47x | 1.45 | 0.02 | 0.67 MB/s | 63.56 MB/s | 0.0037 | 77.33 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 5.77% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.159119)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: binary_gif_small

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 1.00 KB | 65.00 B | 15.75x | 5.74 | 0.30 | 0.17 MB/s | 3.28 MB/s | 0.0040 | 77.34 | 65 | ❌ | 0.136235 | 0.136235 | ❌ | ✅ |
| SHA256 | 1.00 KB | 64.00 B | 16.00x | 0.00 | 0.00 | 533.03 MB/s | 0.00 MB/s | 0.0018 | 77.34 | - | - | - | - | - | - |
| AES-GCM | 1.00 KB | 1.02 KB | 0.98x | 0.12 | 0.05 | 8.20 MB/s | 19.01 MB/s | 0.0044 | 77.34 | - | - | - | - | - | - |
| Frackture Encrypted | 1.00 KB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 1.00 KB | 65.00 B | 15.75x | 0.05 | 0.04 | 21.69 MB/s | 27.51 MB/s | 0.0040 | 77.34 | - | - | - | - | - | - |
| Gzip L2 | 1.00 KB | 65.00 B | 15.75x | 0.02 | 0.02 | 42.31 MB/s | 42.16 MB/s | 0.0041 | 77.34 | - | - | - | - | - | - |
| Gzip L3 | 1.00 KB | 65.00 B | 15.75x | 0.02 | 0.02 | 46.64 MB/s | 45.32 MB/s | 0.0041 | 77.34 | - | - | - | - | - | - |
| Gzip L4 | 1.00 KB | 64.00 B | 16.00x | 0.02 | 0.02 | 42.24 MB/s | 47.57 MB/s | 0.0040 | 77.34 | - | - | - | - | - | - |
| Gzip L5 | 1.00 KB | 64.00 B | 16.00x | 0.02 | 0.02 | 44.55 MB/s | 49.15 MB/s | 0.0043 | 77.34 | - | - | - | - | - | - |
| Gzip L6 | 1.00 KB | 64.00 B | 16.00x | 0.02 | 0.02 | 40.31 MB/s | 45.95 MB/s | 0.0039 | 77.34 | - | - | - | - | - | - |
| Gzip L7 | 1.00 KB | 64.00 B | 16.00x | 0.02 | 0.03 | 45.85 MB/s | 38.78 MB/s | 0.0041 | 77.34 | - | - | - | - | - | - |
| Gzip L8 | 1.00 KB | 64.00 B | 16.00x | 0.02 | 0.02 | 48.96 MB/s | 44.44 MB/s | 0.0039 | 77.34 | - | - | - | - | - | - |
| Gzip L9 | 1.00 KB | 64.00 B | 16.00x | 0.03 | 0.02 | 37.30 MB/s | 39.73 MB/s | 0.0039 | 77.34 | - | - | - | - | - | - |
| Brotli Q0 | 1.00 KB | 112.00 B | 9.14x | 0.04 | 0.02 | 27.59 MB/s | 49.81 MB/s | 0.0040 | 77.34 | - | - | - | - | - | - |
| Brotli Q1 | 1.00 KB | 70.00 B | 14.63x | 0.02 | 0.01 | 55.09 MB/s | 110.47 MB/s | 0.0041 | 77.34 | - | - | - | - | - | - |
| Brotli Q2 | 1.00 KB | 64.00 B | 16.00x | 0.02 | 0.01 | 57.72 MB/s | 91.45 MB/s | 0.0038 | 77.34 | - | - | - | - | - | - |
| Brotli Q3 | 1.00 KB | 45.00 B | 22.76x | 0.02 | 0.01 | 55.05 MB/s | 141.49 MB/s | 0.0037 | 77.34 | - | - | - | - | - | - |
| Brotli Q4 | 1.00 KB | 49.00 B | 20.90x | 0.03 | 0.03 | 31.70 MB/s | 38.47 MB/s | 0.0038 | 77.34 | - | - | - | - | - | - |
| Brotli Q5 | 1.00 KB | 57.00 B | 17.96x | 0.04 | 0.01 | 25.50 MB/s | 124.50 MB/s | 0.0041 | 77.34 | - | - | - | - | - | - |
| Brotli Q6 | 1.00 KB | 57.00 B | 17.96x | 0.04 | 0.01 | 27.35 MB/s | 158.53 MB/s | 0.0044 | 77.36 | - | - | - | - | - | - |
| Brotli Q7 | 1.00 KB | 57.00 B | 17.96x | 0.06 | 0.01 | 17.00 MB/s | 122.01 MB/s | 0.0039 | 77.42 | - | - | - | - | - | - |
| Brotli Q8 | 1.00 KB | 57.00 B | 17.96x | 0.07 | 0.01 | 13.74 MB/s | 161.04 MB/s | 0.0040 | 77.53 | - | - | - | - | - | - |
| Brotli Q9 | 1.00 KB | 57.00 B | 17.96x | 0.13 | 0.01 | 7.25 MB/s | 124.10 MB/s | 0.0039 | 77.53 | - | - | - | - | - | - |
| Brotli Q10 | 1.00 KB | 49.00 B | 20.90x | 0.78 | 0.01 | 1.25 MB/s | 85.92 MB/s | 0.0039 | 77.53 | - | - | - | - | - | - |
| Brotli Q11 | 1.00 KB | 49.00 B | 20.90x | 0.69 | 0.01 | 1.41 MB/s | 97.37 MB/s | 0.0043 | 77.53 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 0.00% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.136235)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: code_javascript_small

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 1.00 KB | 65.00 B | 15.75x | 5.65 | 0.23 | 0.17 MB/s | 4.34 MB/s | 0.0045 | 77.54 | 65 | ❌ | 0.210678 | 0.176264 | ❌ | ✅ |
| SHA256 | 1.00 KB | 64.00 B | 16.00x | 0.00 | 0.00 | 354.81 MB/s | 0.00 MB/s | 0.0028 | 77.54 | - | - | - | - | - | - |
| AES-GCM | 1.00 KB | 1.02 KB | 0.98x | 0.16 | 0.08 | 6.25 MB/s | 12.33 MB/s | 0.0061 | 77.54 | - | - | - | - | - | - |
| Frackture Encrypted | 1.00 KB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 1.00 KB | 314.00 B | 3.26x | 0.07 | 0.05 | 14.79 MB/s | 21.51 MB/s | 0.0051 | 77.54 | - | - | - | - | - | - |
| Gzip L2 | 1.00 KB | 312.00 B | 3.28x | 0.07 | 0.05 | 14.27 MB/s | 18.76 MB/s | 0.0059 | 77.54 | - | - | - | - | - | - |
| Gzip L3 | 1.00 KB | 307.00 B | 3.34x | 0.05 | 0.04 | 18.51 MB/s | 26.15 MB/s | 0.0040 | 77.54 | - | - | - | - | - | - |
| Gzip L4 | 1.00 KB | 303.00 B | 3.38x | 0.04 | 0.03 | 21.90 MB/s | 31.29 MB/s | 0.0041 | 77.54 | - | - | - | - | - | - |
| Gzip L5 | 1.00 KB | 303.00 B | 3.38x | 0.05 | 0.03 | 21.63 MB/s | 31.45 MB/s | 0.0039 | 77.54 | - | - | - | - | - | - |
| Gzip L6 | 1.00 KB | 301.00 B | 3.40x | 0.04 | 0.03 | 22.92 MB/s | 32.80 MB/s | 0.0039 | 77.54 | - | - | - | - | - | - |
| Gzip L7 | 1.00 KB | 301.00 B | 3.40x | 0.04 | 0.03 | 26.56 MB/s | 34.45 MB/s | 0.0040 | 77.54 | - | - | - | - | - | - |
| Gzip L8 | 1.00 KB | 301.00 B | 3.40x | 0.03 | 0.03 | 29.25 MB/s | 35.54 MB/s | 0.0046 | 77.54 | - | - | - | - | - | - |
| Gzip L9 | 1.00 KB | 301.00 B | 3.40x | 0.06 | 0.04 | 17.30 MB/s | 22.68 MB/s | 0.0045 | 77.54 | - | - | - | - | - | - |
| Brotli Q0 | 1.00 KB | 360.00 B | 2.84x | 0.04 | 0.02 | 21.99 MB/s | 47.81 MB/s | 0.0040 | 77.54 | - | - | - | - | - | - |
| Brotli Q1 | 1.00 KB | 317.00 B | 3.23x | 0.03 | 0.01 | 35.04 MB/s | 80.38 MB/s | 0.0039 | 77.54 | - | - | - | - | - | - |
| Brotli Q2 | 1.00 KB | 307.00 B | 3.34x | 0.03 | 0.01 | 32.86 MB/s | 71.66 MB/s | 0.0037 | 77.54 | - | - | - | - | - | - |
| Brotli Q3 | 1.00 KB | 293.00 B | 3.49x | 0.04 | 0.01 | 21.85 MB/s | 65.98 MB/s | 0.0037 | 77.54 | - | - | - | - | - | - |
| Brotli Q4 | 1.00 KB | 272.00 B | 3.76x | 0.10 | 0.01 | 10.07 MB/s | 80.06 MB/s | 0.0038 | 77.54 | - | - | - | - | - | - |
| Brotli Q5 | 1.00 KB | 252.00 B | 4.06x | 0.09 | 0.03 | 11.03 MB/s | 30.33 MB/s | 0.0038 | 77.55 | - | - | - | - | - | - |
| Brotli Q6 | 1.00 KB | 252.00 B | 4.06x | 0.15 | 0.01 | 6.69 MB/s | 88.61 MB/s | 0.0037 | 77.63 | - | - | - | - | - | - |
| Brotli Q7 | 1.00 KB | 254.00 B | 4.03x | 0.25 | 0.01 | 3.90 MB/s | 82.73 MB/s | 0.0038 | 78.02 | - | - | - | - | - | - |
| Brotli Q8 | 1.00 KB | 254.00 B | 4.03x | 0.36 | 0.01 | 2.73 MB/s | 83.09 MB/s | 0.0040 | 78.74 | - | - | - | - | - | - |
| Brotli Q9 | 1.00 KB | 254.00 B | 4.03x | 0.77 | 0.02 | 1.27 MB/s | 59.24 MB/s | 0.0039 | 78.74 | - | - | - | - | - | - |
| Brotli Q10 | 1.00 KB | 241.00 B | 4.25x | 1.00 | 0.02 | 0.97 MB/s | 52.75 MB/s | 0.0038 | 78.74 | - | - | - | - | - | - |
| Brotli Q11 | 1.00 KB | 233.00 B | 4.39x | 1.39 | 0.02 | 0.70 MB/s | 58.93 MB/s | 0.0039 | 78.74 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 16.33% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.210678)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: code_javascript_minified_small

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 1.00 KB | 65.00 B | 15.75x | 5.73 | 0.22 | 0.17 MB/s | 4.41 MB/s | 0.0040 | 78.75 | 65 | ❌ | 0.248601 | 0.216233 | ❌ | ✅ |
| SHA256 | 1.00 KB | 64.00 B | 16.00x | 0.00 | 0.00 | 499.46 MB/s | 0.00 MB/s | 0.0020 | 78.75 | - | - | - | - | - | - |
| AES-GCM | 1.00 KB | 1.02 KB | 0.98x | 0.12 | 0.05 | 8.12 MB/s | 19.10 MB/s | 0.0039 | 78.75 | - | - | - | - | - | - |
| Frackture Encrypted | 1.00 KB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 1.00 KB | 199.00 B | 5.15x | 0.06 | 0.04 | 17.32 MB/s | 23.74 MB/s | 0.0040 | 78.75 | - | - | - | - | - | - |
| Gzip L2 | 1.00 KB | 198.00 B | 5.17x | 0.05 | 0.03 | 21.08 MB/s | 32.98 MB/s | 0.0040 | 78.75 | - | - | - | - | - | - |
| Gzip L3 | 1.00 KB | 197.00 B | 5.20x | 0.03 | 0.03 | 30.15 MB/s | 36.87 MB/s | 0.0041 | 78.75 | - | - | - | - | - | - |
| Gzip L4 | 1.00 KB | 194.00 B | 5.28x | 0.03 | 0.03 | 32.00 MB/s | 37.93 MB/s | 0.0040 | 78.75 | - | - | - | - | - | - |
| Gzip L5 | 1.00 KB | 194.00 B | 5.28x | 0.03 | 0.02 | 36.67 MB/s | 42.37 MB/s | 0.0039 | 78.75 | - | - | - | - | - | - |
| Gzip L6 | 1.00 KB | 194.00 B | 5.28x | 0.03 | 0.02 | 38.64 MB/s | 43.39 MB/s | 0.0039 | 78.75 | - | - | - | - | - | - |
| Gzip L7 | 1.00 KB | 194.00 B | 5.28x | 0.02 | 0.02 | 39.36 MB/s | 43.48 MB/s | 0.0042 | 78.75 | - | - | - | - | - | - |
| Gzip L8 | 1.00 KB | 194.00 B | 5.28x | 0.02 | 0.02 | 39.90 MB/s | 41.84 MB/s | 0.0040 | 78.75 | - | - | - | - | - | - |
| Gzip L9 | 1.00 KB | 194.00 B | 5.28x | 0.03 | 0.02 | 38.81 MB/s | 41.13 MB/s | 0.0040 | 78.75 | - | - | - | - | - | - |
| Brotli Q0 | 1.00 KB | 237.00 B | 4.32x | 0.04 | 0.02 | 25.55 MB/s | 52.18 MB/s | 0.0040 | 78.75 | - | - | - | - | - | - |
| Brotli Q1 | 1.00 KB | 192.00 B | 5.33x | 0.02 | 0.01 | 42.08 MB/s | 91.90 MB/s | 0.0043 | 78.75 | - | - | - | - | - | - |
| Brotli Q2 | 1.00 KB | 187.00 B | 5.48x | 0.02 | 0.01 | 40.33 MB/s | 82.20 MB/s | 0.0040 | 78.75 | - | - | - | - | - | - |
| Brotli Q3 | 1.00 KB | 175.00 B | 5.85x | 0.03 | 0.01 | 32.31 MB/s | 118.63 MB/s | 0.0038 | 78.75 | - | - | - | - | - | - |
| Brotli Q4 | 1.00 KB | 167.00 B | 6.13x | 0.06 | 0.01 | 17.57 MB/s | 105.34 MB/s | 0.0038 | 78.75 | - | - | - | - | - | - |
| Brotli Q5 | 1.00 KB | 155.00 B | 6.61x | 0.06 | 0.01 | 16.05 MB/s | 80.85 MB/s | 0.0045 | 78.75 | - | - | - | - | - | - |
| Brotli Q6 | 1.00 KB | 155.00 B | 6.61x | 0.08 | 0.01 | 12.74 MB/s | 99.27 MB/s | 0.0040 | 78.78 | - | - | - | - | - | - |
| Brotli Q7 | 1.00 KB | 155.00 B | 6.61x | 0.14 | 0.01 | 6.80 MB/s | 111.47 MB/s | 0.0040 | 79.01 | - | - | - | - | - | - |
| Brotli Q8 | 1.00 KB | 155.00 B | 6.61x | 0.18 | 0.01 | 5.38 MB/s | 124.37 MB/s | 0.0039 | 79.38 | - | - | - | - | - | - |
| Brotli Q9 | 1.00 KB | 155.00 B | 6.61x | 0.45 | 0.01 | 2.16 MB/s | 71.20 MB/s | 0.0044 | 79.38 | - | - | - | - | - | - |
| Brotli Q10 | 1.00 KB | 166.00 B | 6.17x | 0.79 | 0.02 | 1.24 MB/s | 55.35 MB/s | 0.0040 | 79.38 | - | - | - | - | - | - |
| Brotli Q11 | 1.00 KB | 162.00 B | 6.32x | 0.92 | 0.02 | 1.06 MB/s | 63.36 MB/s | 0.0041 | 79.38 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 13.02% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.248601)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: code_python_small

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 1.00 KB | 65.00 B | 15.75x | 5.60 | 0.22 | 0.17 MB/s | 4.46 MB/s | 0.0039 | 79.39 | 65 | ❌ | 0.201540 | 0.173739 | ❌ | ✅ |
| SHA256 | 1.00 KB | 64.00 B | 16.00x | 0.00 | 0.00 | 534.90 MB/s | 0.00 MB/s | 0.0018 | 79.39 | - | - | - | - | - | - |
| AES-GCM | 1.00 KB | 1.02 KB | 0.98x | 0.18 | 0.06 | 5.36 MB/s | 15.38 MB/s | 0.0037 | 79.39 | - | - | - | - | - | - |
| Frackture Encrypted | 1.00 KB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 1.00 KB | 522.00 B | 1.96x | 0.08 | 0.05 | 12.18 MB/s | 20.23 MB/s | 0.0042 | 79.39 | - | - | - | - | - | - |
| Gzip L2 | 1.00 KB | 518.00 B | 1.98x | 0.05 | 0.03 | 20.29 MB/s | 28.27 MB/s | 0.0039 | 79.39 | - | - | - | - | - | - |
| Gzip L3 | 1.00 KB | 510.00 B | 2.01x | 0.05 | 0.03 | 21.44 MB/s | 30.36 MB/s | 0.0039 | 79.39 | - | - | - | - | - | - |
| Gzip L4 | 1.00 KB | 502.00 B | 2.04x | 0.05 | 0.03 | 19.19 MB/s | 30.52 MB/s | 0.0039 | 79.39 | - | - | - | - | - | - |
| Gzip L5 | 1.00 KB | 497.00 B | 2.06x | 0.05 | 0.03 | 18.58 MB/s | 29.74 MB/s | 0.0041 | 79.39 | - | - | - | - | - | - |
| Gzip L6 | 1.00 KB | 496.00 B | 2.06x | 0.05 | 0.03 | 18.99 MB/s | 31.36 MB/s | 0.0039 | 79.39 | - | - | - | - | - | - |
| Gzip L7 | 1.00 KB | 496.00 B | 2.06x | 0.05 | 0.03 | 21.65 MB/s | 32.96 MB/s | 0.0039 | 79.39 | - | - | - | - | - | - |
| Gzip L8 | 1.00 KB | 496.00 B | 2.06x | 0.04 | 0.03 | 23.05 MB/s | 34.11 MB/s | 0.0040 | 79.39 | - | - | - | - | - | - |
| Gzip L9 | 1.00 KB | 496.00 B | 2.06x | 0.04 | 0.03 | 24.53 MB/s | 34.84 MB/s | 0.0041 | 79.39 | - | - | - | - | - | - |
| Brotli Q0 | 1.00 KB | 600.00 B | 1.71x | 0.05 | 0.02 | 20.73 MB/s | 42.41 MB/s | 0.0039 | 79.39 | - | - | - | - | - | - |
| Brotli Q1 | 1.00 KB | 547.00 B | 1.87x | 0.03 | 0.01 | 30.18 MB/s | 65.70 MB/s | 0.0038 | 79.39 | - | - | - | - | - | - |
| Brotli Q2 | 1.00 KB | 543.00 B | 1.89x | 0.04 | 0.02 | 24.08 MB/s | 59.99 MB/s | 0.0043 | 79.39 | - | - | - | - | - | - |
| Brotli Q3 | 1.00 KB | 515.00 B | 1.99x | 0.07 | 0.02 | 13.74 MB/s | 57.94 MB/s | 0.0053 | 79.39 | - | - | - | - | - | - |
| Brotli Q4 | 1.00 KB | 485.00 B | 2.11x | 0.12 | 0.02 | 8.11 MB/s | 59.40 MB/s | 0.0041 | 79.39 | - | - | - | - | - | - |
| Brotli Q5 | 1.00 KB | 464.00 B | 2.21x | 0.11 | 0.02 | 8.80 MB/s | 60.24 MB/s | 0.0039 | 79.39 | - | - | - | - | - | - |
| Brotli Q6 | 1.00 KB | 465.00 B | 2.20x | 0.13 | 0.01 | 7.46 MB/s | 69.99 MB/s | 0.0039 | 79.44 | - | - | - | - | - | - |
| Brotli Q7 | 1.00 KB | 464.00 B | 2.21x | 0.36 | 0.01 | 2.73 MB/s | 66.35 MB/s | 0.0038 | 79.93 | - | - | - | - | - | - |
| Brotli Q8 | 1.00 KB | 464.00 B | 2.21x | 0.54 | 0.02 | 1.81 MB/s | 59.21 MB/s | 0.0040 | 80.84 | - | - | - | - | - | - |
| Brotli Q9 | 1.00 KB | 463.00 B | 2.21x | 1.29 | 0.02 | 0.76 MB/s | 46.79 MB/s | 0.0042 | 80.84 | - | - | - | - | - | - |
| Brotli Q10 | 1.00 KB | 447.00 B | 2.29x | 1.37 | 0.02 | 0.71 MB/s | 44.54 MB/s | 0.0038 | 80.84 | - | - | - | - | - | - |
| Brotli Q11 | 1.00 KB | 455.00 B | 2.25x | 2.36 | 0.02 | 0.41 MB/s | 41.95 MB/s | 0.0040 | 80.84 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 13.79% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.201540)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: mixed_payload_small

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 1.00 KB | 65.00 B | 15.75x | 5.66 | 0.22 | 0.17 MB/s | 4.46 MB/s | 0.0039 | 80.84 | 65 | ❌ | 0.238798 | 0.223683 | ❌ | ✅ |
| SHA256 | 1.00 KB | 64.00 B | 16.00x | 0.00 | 0.00 | 524.97 MB/s | 0.00 MB/s | 0.0019 | 80.84 | - | - | - | - | - | - |
| AES-GCM | 1.00 KB | 1.02 KB | 0.98x | 0.12 | 0.05 | 7.98 MB/s | 18.94 MB/s | 0.0039 | 80.84 | - | - | - | - | - | - |
| Frackture Encrypted | 1.00 KB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 1.00 KB | 602.00 B | 1.70x | 0.08 | 0.05 | 12.57 MB/s | 19.64 MB/s | 0.0038 | 80.84 | - | - | - | - | - | - |
| Gzip L2 | 1.00 KB | 602.00 B | 1.70x | 0.05 | 0.06 | 19.40 MB/s | 16.99 MB/s | 0.0039 | 80.84 | - | - | - | - | - | - |
| Gzip L3 | 1.00 KB | 600.00 B | 1.71x | 0.09 | 0.04 | 10.36 MB/s | 25.45 MB/s | 0.0038 | 80.84 | - | - | - | - | - | - |
| Gzip L4 | 1.00 KB | 596.00 B | 1.72x | 0.05 | 0.04 | 19.46 MB/s | 27.30 MB/s | 0.0039 | 80.84 | - | - | - | - | - | - |
| Gzip L5 | 1.00 KB | 593.00 B | 1.73x | 0.05 | 0.05 | 19.60 MB/s | 20.34 MB/s | 0.0039 | 80.84 | - | - | - | - | - | - |
| Gzip L6 | 1.00 KB | 593.00 B | 1.73x | 0.04 | 0.03 | 22.65 MB/s | 33.00 MB/s | 0.0039 | 80.84 | - | - | - | - | - | - |
| Gzip L7 | 1.00 KB | 593.00 B | 1.73x | 0.04 | 0.03 | 24.59 MB/s | 33.52 MB/s | 0.0040 | 80.84 | - | - | - | - | - | - |
| Gzip L8 | 1.00 KB | 593.00 B | 1.73x | 0.04 | 0.03 | 23.83 MB/s | 31.02 MB/s | 0.0039 | 80.84 | - | - | - | - | - | - |
| Gzip L9 | 1.00 KB | 593.00 B | 1.73x | 0.04 | 0.03 | 24.98 MB/s | 32.37 MB/s | 0.0039 | 80.84 | - | - | - | - | - | - |
| Brotli Q0 | 1.00 KB | 688.00 B | 1.49x | 0.05 | 0.02 | 21.08 MB/s | 43.54 MB/s | 0.0040 | 80.84 | - | - | - | - | - | - |
| Brotli Q1 | 1.00 KB | 628.00 B | 1.63x | 0.03 | 0.01 | 29.57 MB/s | 69.34 MB/s | 0.0079 | 80.84 | - | - | - | - | - | - |
| Brotli Q2 | 1.00 KB | 616.00 B | 1.66x | 0.05 | 0.02 | 19.42 MB/s | 42.29 MB/s | 0.0059 | 80.84 | - | - | - | - | - | - |
| Brotli Q3 | 1.00 KB | 604.00 B | 1.70x | 0.08 | 0.02 | 12.70 MB/s | 40.59 MB/s | 0.0061 | 80.84 | - | - | - | - | - | - |
| Brotli Q4 | 1.00 KB | 577.00 B | 1.77x | 0.16 | 0.02 | 6.20 MB/s | 47.35 MB/s | 0.0059 | 80.84 | - | - | - | - | - | - |
| Brotli Q5 | 1.00 KB | 552.00 B | 1.86x | 0.19 | 0.02 | 5.01 MB/s | 41.76 MB/s | 0.0062 | 80.85 | - | - | - | - | - | - |
| Brotli Q6 | 1.00 KB | 552.00 B | 1.86x | 0.32 | 0.02 | 3.05 MB/s | 40.49 MB/s | 0.0050 | 80.87 | - | - | - | - | - | - |
| Brotli Q7 | 1.00 KB | 552.00 B | 1.86x | 0.31 | 0.02 | 3.13 MB/s | 50.63 MB/s | 0.0039 | 81.29 | - | - | - | - | - | - |
| Brotli Q8 | 1.00 KB | 552.00 B | 1.86x | 0.52 | 0.02 | 1.89 MB/s | 51.14 MB/s | 0.0078 | 82.29 | - | - | - | - | - | - |
| Brotli Q9 | 1.00 KB | 556.00 B | 1.84x | 2.36 | 0.03 | 0.41 MB/s | 35.62 MB/s | 0.0059 | 82.29 | - | - | - | - | - | - |
| Brotli Q10 | 1.00 KB | 502.00 B | 2.04x | 1.98 | 0.03 | 0.49 MB/s | 36.63 MB/s | 0.0043 | 82.29 | - | - | - | - | - | - |
| Brotli Q11 | 1.00 KB | 506.00 B | 2.02x | 2.27 | 0.02 | 0.43 MB/s | 41.48 MB/s | 0.0037 | 82.29 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 6.33% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.238798)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: structured_sqlite_small

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 1.00 KB | 65.00 B | 15.75x | 5.64 | 0.25 | 0.17 MB/s | 3.89 MB/s | 0.0038 | 82.30 | 65 | ❌ | 0.042963 | 0.042963 | ❌ | ✅ |
| SHA256 | 1.00 KB | 64.00 B | 16.00x | 0.00 | 0.00 | 530.42 MB/s | 0.00 MB/s | 0.0018 | 82.30 | - | - | - | - | - | - |
| AES-GCM | 1.00 KB | 1.02 KB | 0.98x | 0.12 | 0.05 | 8.27 MB/s | 18.87 MB/s | 0.0039 | 82.30 | - | - | - | - | - | - |
| Frackture Encrypted | 1.00 KB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 1.00 KB | 89.00 B | 11.51x | 0.05 | 0.04 | 18.44 MB/s | 26.31 MB/s | 0.0040 | 82.30 | - | - | - | - | - | - |
| Gzip L2 | 1.00 KB | 88.00 B | 11.64x | 0.03 | 0.02 | 34.81 MB/s | 40.64 MB/s | 0.0039 | 82.30 | - | - | - | - | - | - |
| Gzip L3 | 1.00 KB | 88.00 B | 11.64x | 0.03 | 0.04 | 37.40 MB/s | 27.79 MB/s | 0.0041 | 82.30 | - | - | - | - | - | - |
| Gzip L4 | 1.00 KB | 83.00 B | 12.34x | 0.03 | 0.02 | 31.36 MB/s | 41.95 MB/s | 0.0040 | 82.30 | - | - | - | - | - | - |
| Gzip L5 | 1.00 KB | 82.00 B | 12.49x | 0.03 | 0.02 | 35.95 MB/s | 44.03 MB/s | 0.0051 | 82.30 | - | - | - | - | - | - |
| Gzip L6 | 1.00 KB | 82.00 B | 12.49x | 0.05 | 0.04 | 19.52 MB/s | 26.32 MB/s | 0.0061 | 82.30 | - | - | - | - | - | - |
| Gzip L7 | 1.00 KB | 82.00 B | 12.49x | 0.15 | 0.04 | 6.48 MB/s | 22.24 MB/s | 0.0052 | 82.30 | - | - | - | - | - | - |
| Gzip L8 | 1.00 KB | 82.00 B | 12.49x | 0.04 | 0.03 | 23.24 MB/s | 30.76 MB/s | 0.0041 | 82.30 | - | - | - | - | - | - |
| Gzip L9 | 1.00 KB | 82.00 B | 12.49x | 0.03 | 0.03 | 33.47 MB/s | 37.70 MB/s | 0.0052 | 82.30 | - | - | - | - | - | - |
| Brotli Q0 | 1.00 KB | 144.00 B | 7.11x | 0.05 | 0.02 | 18.33 MB/s | 42.80 MB/s | 0.0068 | 82.30 | - | - | - | - | - | - |
| Brotli Q1 | 1.00 KB | 101.00 B | 10.14x | 0.03 | 0.02 | 28.68 MB/s | 53.92 MB/s | 0.0060 | 82.30 | - | - | - | - | - | - |
| Brotli Q2 | 1.00 KB | 91.00 B | 11.25x | 0.03 | 0.02 | 30.18 MB/s | 51.84 MB/s | 0.0057 | 82.30 | - | - | - | - | - | - |
| Brotli Q3 | 1.00 KB | 73.00 B | 14.03x | 0.03 | 0.01 | 30.10 MB/s | 69.87 MB/s | 0.0040 | 82.30 | - | - | - | - | - | - |
| Brotli Q4 | 1.00 KB | 72.00 B | 14.22x | 0.04 | 0.01 | 23.81 MB/s | 96.57 MB/s | 0.0058 | 82.30 | - | - | - | - | - | - |
| Brotli Q5 | 1.00 KB | 78.00 B | 13.13x | 0.08 | 0.02 | 13.01 MB/s | 58.54 MB/s | 0.0055 | 82.30 | - | - | - | - | - | - |
| Brotli Q6 | 1.00 KB | 78.00 B | 13.13x | 0.05 | 0.01 | 17.78 MB/s | 70.89 MB/s | 0.0037 | 82.31 | - | - | - | - | - | - |
| Brotli Q7 | 1.00 KB | 79.00 B | 12.96x | 0.06 | 0.01 | 17.61 MB/s | 100.24 MB/s | 0.0038 | 82.34 | - | - | - | - | - | - |
| Brotli Q8 | 1.00 KB | 79.00 B | 12.96x | 0.08 | 0.01 | 11.65 MB/s | 111.37 MB/s | 0.0038 | 82.43 | - | - | - | - | - | - |
| Brotli Q9 | 1.00 KB | 79.00 B | 12.96x | 0.17 | 0.01 | 5.66 MB/s | 94.88 MB/s | 0.0042 | 82.43 | - | - | - | - | - | - |
| Brotli Q10 | 1.00 KB | 72.00 B | 14.22x | 0.86 | 0.02 | 1.14 MB/s | 45.95 MB/s | 0.0040 | 82.43 | - | - | - | - | - | - |
| Brotli Q11 | 1.00 KB | 72.00 B | 14.22x | 0.77 | 0.02 | 1.27 MB/s | 63.77 MB/s | 0.0040 | 82.43 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 0.00% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.042963)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: structured_pickle_small

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 1.00 KB | 65.00 B | 15.75x | 5.71 | 0.24 | 0.17 MB/s | 4.02 MB/s | 0.0042 | 82.43 | 65 | ❌ | 0.212640 | 0.180567 | ❌ | ✅ |
| SHA256 | 1.00 KB | 64.00 B | 16.00x | 0.00 | 0.00 | 532.12 MB/s | 0.00 MB/s | 0.0018 | 82.43 | - | - | - | - | - | - |
| AES-GCM | 1.00 KB | 1.02 KB | 0.98x | 0.13 | 0.05 | 7.41 MB/s | 18.82 MB/s | 0.0041 | 82.43 | - | - | - | - | - | - |
| Frackture Encrypted | 1.00 KB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 1.00 KB | 175.00 B | 5.85x | 0.06 | 0.04 | 17.44 MB/s | 27.10 MB/s | 0.0040 | 82.44 | - | - | - | - | - | - |
| Gzip L2 | 1.00 KB | 174.00 B | 5.89x | 0.03 | 0.02 | 31.59 MB/s | 41.03 MB/s | 0.0039 | 82.44 | - | - | - | - | - | - |
| Gzip L3 | 1.00 KB | 174.00 B | 5.89x | 0.03 | 0.02 | 37.34 MB/s | 44.78 MB/s | 0.0039 | 82.44 | - | - | - | - | - | - |
| Gzip L4 | 1.00 KB | 173.00 B | 5.92x | 0.03 | 0.02 | 34.00 MB/s | 46.83 MB/s | 0.0041 | 82.44 | - | - | - | - | - | - |
| Gzip L5 | 1.00 KB | 173.00 B | 5.92x | 0.03 | 0.02 | 37.45 MB/s | 46.84 MB/s | 0.0039 | 82.44 | - | - | - | - | - | - |
| Gzip L6 | 1.00 KB | 173.00 B | 5.92x | 0.02 | 0.02 | 41.09 MB/s | 47.51 MB/s | 0.0038 | 82.44 | - | - | - | - | - | - |
| Gzip L7 | 1.00 KB | 173.00 B | 5.92x | 0.03 | 0.02 | 35.43 MB/s | 46.75 MB/s | 0.0040 | 82.44 | - | - | - | - | - | - |
| Gzip L8 | 1.00 KB | 173.00 B | 5.92x | 0.02 | 0.02 | 41.03 MB/s | 47.15 MB/s | 0.0040 | 82.44 | - | - | - | - | - | - |
| Gzip L9 | 1.00 KB | 173.00 B | 5.92x | 0.03 | 0.02 | 30.64 MB/s | 42.16 MB/s | 0.0038 | 82.44 | - | - | - | - | - | - |
| Brotli Q0 | 1.00 KB | 217.00 B | 4.72x | 0.04 | 0.02 | 24.61 MB/s | 41.57 MB/s | 0.0037 | 82.44 | - | - | - | - | - | - |
| Brotli Q1 | 1.00 KB | 174.00 B | 5.89x | 0.02 | 0.01 | 47.38 MB/s | 104.83 MB/s | 0.0039 | 82.44 | - | - | - | - | - | - |
| Brotli Q2 | 1.00 KB | 173.00 B | 5.92x | 0.02 | 0.01 | 45.12 MB/s | 87.68 MB/s | 0.0039 | 82.44 | - | - | - | - | - | - |
| Brotli Q3 | 1.00 KB | 148.00 B | 6.92x | 0.03 | 0.01 | 32.98 MB/s | 130.09 MB/s | 0.0041 | 82.44 | - | - | - | - | - | - |
| Brotli Q4 | 1.00 KB | 142.00 B | 7.21x | 0.05 | 0.01 | 19.22 MB/s | 117.97 MB/s | 0.0039 | 82.44 | - | - | - | - | - | - |
| Brotli Q5 | 1.00 KB | 140.00 B | 7.31x | 0.05 | 0.01 | 18.93 MB/s | 96.61 MB/s | 0.0040 | 82.44 | - | - | - | - | - | - |
| Brotli Q6 | 1.00 KB | 140.00 B | 7.31x | 0.07 | 0.01 | 13.28 MB/s | 106.09 MB/s | 0.0043 | 82.45 | - | - | - | - | - | - |
| Brotli Q7 | 1.00 KB | 140.00 B | 7.31x | 0.08 | 0.01 | 12.15 MB/s | 118.76 MB/s | 0.0042 | 82.52 | - | - | - | - | - | - |
| Brotli Q8 | 1.00 KB | 140.00 B | 7.31x | 0.12 | 0.01 | 7.99 MB/s | 122.19 MB/s | 0.0039 | 82.70 | - | - | - | - | - | - |
| Brotli Q9 | 1.00 KB | 140.00 B | 7.31x | 0.41 | 0.02 | 2.38 MB/s | 54.12 MB/s | 0.0040 | 82.70 | - | - | - | - | - | - |
| Brotli Q10 | 1.00 KB | 139.00 B | 7.37x | 0.66 | 0.02 | 1.47 MB/s | 63.84 MB/s | 0.0051 | 82.70 | - | - | - | - | - | - |
| Brotli Q11 | 1.00 KB | 145.00 B | 7.06x | 0.65 | 0.01 | 1.50 MB/s | 66.07 MB/s | 0.0040 | 82.70 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 15.08% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.212640)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: text_plain_small

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 1.00 KB | 65.00 B | 15.75x | 5.72 | 0.28 | 0.17 MB/s | 3.44 MB/s | 0.0041 | 82.71 | 65 | ❌ | 0.313108 | 0.244711 | ❌ | ✅ |
| SHA256 | 1.00 KB | 64.00 B | 16.00x | 0.00 | 0.00 | 537.70 MB/s | 0.00 MB/s | 0.0018 | 82.71 | - | - | - | - | - | - |
| AES-GCM | 1.00 KB | 1.02 KB | 0.98x | 0.12 | 0.05 | 8.05 MB/s | 18.99 MB/s | 0.0039 | 82.71 | - | - | - | - | - | - |
| Frackture Encrypted | 1.00 KB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 1.00 KB | 386.00 B | 2.65x | 0.07 | 0.04 | 14.72 MB/s | 21.99 MB/s | 0.0040 | 82.71 | - | - | - | - | - | - |
| Gzip L2 | 1.00 KB | 386.00 B | 2.65x | 0.04 | 0.03 | 26.20 MB/s | 30.64 MB/s | 0.0041 | 82.71 | - | - | - | - | - | - |
| Gzip L3 | 1.00 KB | 385.00 B | 2.66x | 0.04 | 0.03 | 25.74 MB/s | 31.00 MB/s | 0.0040 | 82.71 | - | - | - | - | - | - |
| Gzip L4 | 1.00 KB | 383.00 B | 2.67x | 0.04 | 0.03 | 23.59 MB/s | 32.63 MB/s | 0.0043 | 82.71 | - | - | - | - | - | - |
| Gzip L5 | 1.00 KB | 381.00 B | 2.69x | 0.04 | 0.03 | 22.56 MB/s | 31.79 MB/s | 0.0042 | 82.71 | - | - | - | - | - | - |
| Gzip L6 | 1.00 KB | 381.00 B | 2.69x | 0.04 | 0.03 | 27.73 MB/s | 34.07 MB/s | 0.0040 | 82.71 | - | - | - | - | - | - |
| Gzip L7 | 1.00 KB | 381.00 B | 2.69x | 0.04 | 0.03 | 25.78 MB/s | 28.16 MB/s | 0.0041 | 82.71 | - | - | - | - | - | - |
| Gzip L8 | 1.00 KB | 381.00 B | 2.69x | 0.03 | 0.03 | 30.73 MB/s | 33.73 MB/s | 0.0044 | 82.71 | - | - | - | - | - | - |
| Gzip L9 | 1.00 KB | 381.00 B | 2.69x | 0.04 | 0.03 | 26.14 MB/s | 33.76 MB/s | 0.0039 | 82.71 | - | - | - | - | - | - |
| Brotli Q0 | 1.00 KB | 428.00 B | 2.39x | 0.04 | 0.02 | 22.75 MB/s | 49.39 MB/s | 0.0039 | 82.71 | - | - | - | - | - | - |
| Brotli Q1 | 1.00 KB | 388.00 B | 2.64x | 0.03 | 0.01 | 37.79 MB/s | 83.01 MB/s | 0.0039 | 82.71 | - | - | - | - | - | - |
| Brotli Q2 | 1.00 KB | 377.00 B | 2.72x | 0.03 | 0.01 | 32.52 MB/s | 75.22 MB/s | 0.0041 | 82.71 | - | - | - | - | - | - |
| Brotli Q3 | 1.00 KB | 364.00 B | 2.81x | 0.04 | 0.01 | 27.84 MB/s | 100.82 MB/s | 0.0040 | 82.71 | - | - | - | - | - | - |
| Brotli Q4 | 1.00 KB | 350.00 B | 2.93x | 0.09 | 0.01 | 10.90 MB/s | 73.89 MB/s | 0.0044 | 82.71 | - | - | - | - | - | - |
| Brotli Q5 | 1.00 KB | 346.00 B | 2.96x | 0.09 | 0.01 | 10.48 MB/s | 69.97 MB/s | 0.0039 | 82.71 | - | - | - | - | - | - |
| Brotli Q6 | 1.00 KB | 346.00 B | 2.96x | 0.09 | 0.01 | 10.67 MB/s | 87.36 MB/s | 0.0041 | 82.71 | - | - | - | - | - | - |
| Brotli Q7 | 1.00 KB | 346.00 B | 2.96x | 0.15 | 0.01 | 6.53 MB/s | 86.33 MB/s | 0.0039 | 82.86 | - | - | - | - | - | - |
| Brotli Q8 | 1.00 KB | 346.00 B | 2.96x | 0.30 | 0.01 | 3.28 MB/s | 77.22 MB/s | 0.0040 | 83.39 | - | - | - | - | - | - |
| Brotli Q9 | 1.00 KB | 350.00 B | 2.93x | 0.97 | 0.02 | 1.01 MB/s | 49.51 MB/s | 0.0043 | 83.39 | - | - | - | - | - | - |
| Brotli Q10 | 1.00 KB | 318.00 B | 3.22x | 0.89 | 0.02 | 1.10 MB/s | 48.64 MB/s | 0.0039 | 83.39 | - | - | - | - | - | - |
| Brotli Q11 | 1.00 KB | 315.00 B | 3.25x | 1.27 | 0.02 | 0.77 MB/s | 58.04 MB/s | 0.0038 | 83.39 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 21.84% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.313108)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: text_log_small

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 1.00 KB | 65.00 B | 15.75x | 5.75 | 0.30 | 0.17 MB/s | 3.24 MB/s | 0.0044 | 83.41 | 65 | ❌ | 0.199651 | 0.123128 | ❌ | ✅ |
| SHA256 | 1.00 KB | 64.00 B | 16.00x | 0.00 | 0.00 | 529.97 MB/s | 0.00 MB/s | 0.0018 | 83.41 | - | - | - | - | - | - |
| AES-GCM | 1.00 KB | 1.02 KB | 0.98x | 0.12 | 0.05 | 8.06 MB/s | 19.11 MB/s | 0.0041 | 83.41 | - | - | - | - | - | - |
| Frackture Encrypted | 1.00 KB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 1.00 KB | 258.00 B | 3.97x | 0.06 | 0.04 | 15.51 MB/s | 21.82 MB/s | 0.0040 | 83.41 | - | - | - | - | - | - |
| Gzip L2 | 1.00 KB | 252.00 B | 4.06x | 0.04 | 0.03 | 26.39 MB/s | 31.94 MB/s | 0.0041 | 83.41 | - | - | - | - | - | - |
| Gzip L3 | 1.00 KB | 252.00 B | 4.06x | 0.03 | 0.03 | 29.93 MB/s | 34.89 MB/s | 0.0039 | 83.41 | - | - | - | - | - | - |
| Gzip L4 | 1.00 KB | 250.00 B | 4.10x | 0.03 | 0.03 | 28.29 MB/s | 36.23 MB/s | 0.0041 | 83.41 | - | - | - | - | - | - |
| Gzip L5 | 1.00 KB | 250.00 B | 4.10x | 0.03 | 0.03 | 28.09 MB/s | 35.51 MB/s | 0.0041 | 83.41 | - | - | - | - | - | - |
| Gzip L6 | 1.00 KB | 250.00 B | 4.10x | 0.03 | 0.03 | 33.03 MB/s | 37.89 MB/s | 0.0041 | 83.41 | - | - | - | - | - | - |
| Gzip L7 | 1.00 KB | 248.00 B | 4.13x | 0.03 | 0.03 | 28.80 MB/s | 35.23 MB/s | 0.0041 | 83.41 | - | - | - | - | - | - |
| Gzip L8 | 1.00 KB | 248.00 B | 4.13x | 0.04 | 0.03 | 23.50 MB/s | 33.53 MB/s | 0.0040 | 83.41 | - | - | - | - | - | - |
| Gzip L9 | 1.00 KB | 248.00 B | 4.13x | 0.04 | 0.03 | 27.16 MB/s | 36.72 MB/s | 0.0040 | 83.41 | - | - | - | - | - | - |
| Brotli Q0 | 1.00 KB | 302.00 B | 3.39x | 0.05 | 0.02 | 21.22 MB/s | 47.79 MB/s | 0.0041 | 83.41 | - | - | - | - | - | - |
| Brotli Q1 | 1.00 KB | 253.00 B | 4.05x | 0.03 | 0.01 | 38.15 MB/s | 83.31 MB/s | 0.0039 | 83.41 | - | - | - | - | - | - |
| Brotli Q2 | 1.00 KB | 243.00 B | 4.21x | 0.03 | 0.02 | 36.78 MB/s | 58.45 MB/s | 0.0047 | 83.41 | - | - | - | - | - | - |
| Brotli Q3 | 1.00 KB | 230.00 B | 4.45x | 0.04 | 0.01 | 22.69 MB/s | 73.02 MB/s | 0.0043 | 83.41 | - | - | - | - | - | - |
| Brotli Q4 | 1.00 KB | 225.00 B | 4.55x | 0.07 | 0.01 | 13.83 MB/s | 76.20 MB/s | 0.0044 | 83.41 | - | - | - | - | - | - |
| Brotli Q5 | 1.00 KB | 205.00 B | 5.00x | 0.08 | 0.01 | 12.48 MB/s | 73.58 MB/s | 0.0039 | 83.41 | - | - | - | - | - | - |
| Brotli Q6 | 1.00 KB | 205.00 B | 5.00x | 0.07 | 0.01 | 13.91 MB/s | 93.33 MB/s | 0.0042 | 83.42 | - | - | - | - | - | - |
| Brotli Q7 | 1.00 KB | 207.00 B | 4.95x | 0.11 | 0.01 | 8.90 MB/s | 74.62 MB/s | 0.0045 | 83.50 | - | - | - | - | - | - |
| Brotli Q8 | 1.00 KB | 207.00 B | 4.95x | 0.27 | 0.01 | 3.56 MB/s | 65.86 MB/s | 0.0042 | 83.73 | - | - | - | - | - | - |
| Brotli Q9 | 1.00 KB | 207.00 B | 4.95x | 0.54 | 0.02 | 1.82 MB/s | 54.98 MB/s | 0.0043 | 83.73 | - | - | - | - | - | - |
| Brotli Q10 | 1.00 KB | 191.00 B | 5.36x | 0.91 | 0.02 | 1.07 MB/s | 52.44 MB/s | 0.0043 | 83.73 | - | - | - | - | - | - |
| Brotli Q11 | 1.00 KB | 191.00 B | 5.36x | 1.36 | 0.04 | 0.72 MB/s | 22.03 MB/s | 0.0041 | 83.73 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 38.33% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.199651)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: text_json_small

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 1.00 KB | 65.00 B | 15.75x | 6.02 | 0.23 | 0.16 MB/s | 4.29 MB/s | 0.0038 | 83.75 | 65 | ❌ | 0.203007 | 0.142893 | ❌ | ✅ |
| SHA256 | 1.00 KB | 64.00 B | 16.00x | 0.00 | 0.00 | 395.52 MB/s | 0.00 MB/s | 0.0025 | 83.75 | - | - | - | - | - | - |
| AES-GCM | 1.00 KB | 1.02 KB | 0.98x | 0.16 | 0.06 | 5.97 MB/s | 16.49 MB/s | 0.0039 | 83.75 | - | - | - | - | - | - |
| Frackture Encrypted | 1.00 KB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 1.00 KB | 375.00 B | 2.73x | 0.07 | 0.05 | 14.27 MB/s | 21.07 MB/s | 0.0041 | 83.75 | - | - | - | - | - | - |
| Gzip L2 | 1.00 KB | 364.00 B | 2.81x | 0.04 | 0.03 | 22.36 MB/s | 30.17 MB/s | 0.0039 | 83.75 | - | - | - | - | - | - |
| Gzip L3 | 1.00 KB | 364.00 B | 2.81x | 0.04 | 0.03 | 26.60 MB/s | 33.80 MB/s | 0.0041 | 83.75 | - | - | - | - | - | - |
| Gzip L4 | 1.00 KB | 355.00 B | 2.88x | 0.04 | 0.03 | 22.29 MB/s | 33.85 MB/s | 0.0039 | 83.75 | - | - | - | - | - | - |
| Gzip L5 | 1.00 KB | 355.00 B | 2.88x | 0.04 | 0.03 | 22.00 MB/s | 35.45 MB/s | 0.0041 | 83.75 | - | - | - | - | - | - |
| Gzip L6 | 1.00 KB | 353.00 B | 2.90x | 0.05 | 0.04 | 20.97 MB/s | 23.68 MB/s | 0.0039 | 83.75 | - | - | - | - | - | - |
| Gzip L7 | 1.00 KB | 353.00 B | 2.90x | 0.04 | 0.03 | 24.87 MB/s | 35.34 MB/s | 0.0041 | 83.75 | - | - | - | - | - | - |
| Gzip L8 | 1.00 KB | 353.00 B | 2.90x | 0.04 | 0.03 | 23.91 MB/s | 32.71 MB/s | 0.0040 | 83.75 | - | - | - | - | - | - |
| Gzip L9 | 1.00 KB | 353.00 B | 2.90x | 0.04 | 0.03 | 24.33 MB/s | 32.91 MB/s | 0.0039 | 83.75 | - | - | - | - | - | - |
| Brotli Q0 | 1.00 KB | 438.00 B | 2.34x | 0.05 | 0.02 | 21.63 MB/s | 48.15 MB/s | 0.0040 | 83.75 | - | - | - | - | - | - |
| Brotli Q1 | 1.00 KB | 398.00 B | 2.57x | 0.04 | 0.02 | 25.80 MB/s | 60.38 MB/s | 0.0042 | 83.75 | - | - | - | - | - | - |
| Brotli Q2 | 1.00 KB | 365.00 B | 2.81x | 0.03 | 0.01 | 30.96 MB/s | 66.19 MB/s | 0.0040 | 83.75 | - | - | - | - | - | - |
| Brotli Q3 | 1.00 KB | 356.00 B | 2.88x | 0.05 | 0.01 | 18.99 MB/s | 75.20 MB/s | 0.0039 | 83.75 | - | - | - | - | - | - |
| Brotli Q4 | 1.00 KB | 335.00 B | 3.06x | 0.09 | 0.01 | 10.48 MB/s | 76.65 MB/s | 0.0041 | 83.75 | - | - | - | - | - | - |
| Brotli Q5 | 1.00 KB | 314.00 B | 3.26x | 0.09 | 0.01 | 10.96 MB/s | 78.26 MB/s | 0.0041 | 83.75 | - | - | - | - | - | - |
| Brotli Q6 | 1.00 KB | 314.00 B | 3.26x | 0.09 | 0.01 | 10.95 MB/s | 89.86 MB/s | 0.0043 | 83.76 | - | - | - | - | - | - |
| Brotli Q7 | 1.00 KB | 318.00 B | 3.22x | 0.14 | 0.01 | 6.90 MB/s | 69.19 MB/s | 0.0041 | 83.86 | - | - | - | - | - | - |
| Brotli Q8 | 1.00 KB | 318.00 B | 3.22x | 0.24 | 0.01 | 4.09 MB/s | 71.30 MB/s | 0.0040 | 84.21 | - | - | - | - | - | - |
| Brotli Q9 | 1.00 KB | 313.00 B | 3.27x | 0.82 | 0.02 | 1.19 MB/s | 53.67 MB/s | 0.0043 | 84.21 | - | - | - | - | - | - |
| Brotli Q10 | 1.00 KB | 297.00 B | 3.45x | 1.27 | 0.02 | 0.77 MB/s | 42.48 MB/s | 0.0040 | 84.21 | - | - | - | - | - | - |
| Brotli Q11 | 1.00 KB | 291.00 B | 3.52x | 2.14 | 0.02 | 0.46 MB/s | 44.71 MB/s | 0.0040 | 84.21 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 29.61% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.203007)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: text_csv_small

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 1.00 KB | 65.00 B | 15.75x | 5.67 | 0.25 | 0.17 MB/s | 3.95 MB/s | 0.0042 | 84.22 | 65 | ❌ | 0.199575 | 0.188218 | ❌ | ✅ |
| SHA256 | 1.00 KB | 64.00 B | 16.00x | 0.00 | 0.00 | 528.69 MB/s | 0.00 MB/s | 0.0018 | 84.22 | - | - | - | - | - | - |
| AES-GCM | 1.00 KB | 1.02 KB | 0.98x | 0.16 | 0.06 | 6.27 MB/s | 17.71 MB/s | 0.0039 | 84.22 | - | - | - | - | - | - |
| Frackture Encrypted | 1.00 KB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 1.00 KB | 197.00 B | 5.20x | 0.06 | 0.04 | 16.07 MB/s | 22.58 MB/s | 0.0040 | 84.22 | - | - | - | - | - | - |
| Gzip L2 | 1.00 KB | 197.00 B | 5.20x | 0.03 | 0.03 | 29.94 MB/s | 33.62 MB/s | 0.0040 | 84.22 | - | - | - | - | - | - |
| Gzip L3 | 1.00 KB | 197.00 B | 5.20x | 0.03 | 0.03 | 34.91 MB/s | 35.87 MB/s | 0.0040 | 84.22 | - | - | - | - | - | - |
| Gzip L4 | 1.00 KB | 193.00 B | 5.31x | 0.03 | 0.02 | 32.84 MB/s | 39.64 MB/s | 0.0041 | 84.22 | - | - | - | - | - | - |
| Gzip L5 | 1.00 KB | 193.00 B | 5.31x | 0.03 | 0.02 | 35.63 MB/s | 41.30 MB/s | 0.0039 | 84.22 | - | - | - | - | - | - |
| Gzip L6 | 1.00 KB | 193.00 B | 5.31x | 0.02 | 0.02 | 40.92 MB/s | 41.64 MB/s | 0.0039 | 84.22 | - | - | - | - | - | - |
| Gzip L7 | 1.00 KB | 193.00 B | 5.31x | 0.02 | 0.02 | 41.75 MB/s | 42.45 MB/s | 0.0041 | 84.22 | - | - | - | - | - | - |
| Gzip L8 | 1.00 KB | 193.00 B | 5.31x | 0.03 | 0.03 | 29.90 MB/s | 34.43 MB/s | 0.0042 | 84.22 | - | - | - | - | - | - |
| Gzip L9 | 1.00 KB | 193.00 B | 5.31x | 0.03 | 0.03 | 34.50 MB/s | 37.92 MB/s | 0.0039 | 84.22 | - | - | - | - | - | - |
| Brotli Q0 | 1.00 KB | 234.00 B | 4.38x | 0.04 | 0.02 | 24.39 MB/s | 53.38 MB/s | 0.0037 | 84.22 | - | - | - | - | - | - |
| Brotli Q1 | 1.00 KB | 190.00 B | 5.39x | 0.02 | 0.01 | 44.90 MB/s | 96.55 MB/s | 0.0039 | 84.22 | - | - | - | - | - | - |
| Brotli Q2 | 1.00 KB | 185.00 B | 5.54x | 0.02 | 0.01 | 42.02 MB/s | 83.78 MB/s | 0.0037 | 84.22 | - | - | - | - | - | - |
| Brotli Q3 | 1.00 KB | 168.00 B | 6.10x | 0.03 | 0.01 | 32.09 MB/s | 107.90 MB/s | 0.0039 | 84.22 | - | - | - | - | - | - |
| Brotli Q4 | 1.00 KB | 162.00 B | 6.32x | 0.06 | 0.01 | 17.12 MB/s | 99.70 MB/s | 0.0043 | 84.22 | - | - | - | - | - | - |
| Brotli Q5 | 1.00 KB | 156.00 B | 6.56x | 0.06 | 0.01 | 16.10 MB/s | 94.78 MB/s | 0.0042 | 84.22 | - | - | - | - | - | - |
| Brotli Q6 | 1.00 KB | 156.00 B | 6.56x | 0.07 | 0.01 | 13.81 MB/s | 101.91 MB/s | 0.0038 | 84.22 | - | - | - | - | - | - |
| Brotli Q7 | 1.00 KB | 158.00 B | 6.48x | 0.12 | 0.01 | 7.82 MB/s | 99.43 MB/s | 0.0038 | 84.27 | - | - | - | - | - | - |
| Brotli Q8 | 1.00 KB | 158.00 B | 6.48x | 0.14 | 0.01 | 7.04 MB/s | 110.73 MB/s | 0.0039 | 84.43 | - | - | - | - | - | - |
| Brotli Q9 | 1.00 KB | 158.00 B | 6.48x | 0.42 | 0.01 | 2.34 MB/s | 65.50 MB/s | 0.0039 | 84.43 | - | - | - | - | - | - |
| Brotli Q10 | 1.00 KB | 148.00 B | 6.92x | 0.73 | 0.02 | 1.34 MB/s | 44.22 MB/s | 0.0038 | 84.43 | - | - | - | - | - | - |
| Brotli Q11 | 1.00 KB | 148.00 B | 6.92x | 0.86 | 0.02 | 1.14 MB/s | 52.74 MB/s | 0.0040 | 84.43 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 5.69% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.199575)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: binary_png_medium

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 100.00 KB | 65.00 B | 1575.38x | 5.91 | 0.23 | 16.52 MB/s | 433.02 MB/s | 0.0798 | 84.87 | 65 | ❌ | 0.126382 | 0.120252 | ❌ | ✅ |
| SHA256 | 100.00 KB | 64.00 B | 1600.00x | 0.07 | 0.00 | 1302.79 MB/s | 0.00 MB/s | 0.0750 | 84.87 | - | - | - | - | - | - |
| AES-GCM | 100.00 KB | 100.02 KB | 1.00x | 0.15 | 0.11 | 644.28 MB/s | 904.14 MB/s | 0.0800 | 84.87 | - | - | - | - | - | - |
| Frackture Encrypted | 100.00 KB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 100.00 KB | 857.00 B | 119.49x | 0.20 | 0.18 | 500.52 MB/s | 538.36 MB/s | 0.0783 | 84.87 | - | - | - | - | - | - |
| Gzip L2 | 100.00 KB | 769.00 B | 133.16x | 0.18 | 0.08 | 534.97 MB/s | 1217.67 MB/s | 0.0793 | 84.87 | - | - | - | - | - | - |
| Gzip L3 | 100.00 KB | 769.00 B | 133.16x | 0.15 | 0.07 | 644.83 MB/s | 1319.55 MB/s | 0.0780 | 84.87 | - | - | - | - | - | - |
| Gzip L4 | 100.00 KB | 464.00 B | 220.69x | 0.35 | 0.08 | 280.84 MB/s | 1266.95 MB/s | 0.0823 | 84.87 | - | - | - | - | - | - |
| Gzip L5 | 100.00 KB | 464.00 B | 220.69x | 0.31 | 0.07 | 319.94 MB/s | 1389.41 MB/s | 0.0801 | 84.87 | - | - | - | - | - | - |
| Gzip L6 | 100.00 KB | 464.00 B | 220.69x | 0.30 | 0.07 | 326.43 MB/s | 1418.02 MB/s | 0.0806 | 84.87 | - | - | - | - | - | - |
| Gzip L7 | 100.00 KB | 464.00 B | 220.69x | 0.33 | 0.07 | 292.17 MB/s | 1363.08 MB/s | 0.0787 | 84.87 | - | - | - | - | - | - |
| Gzip L8 | 100.00 KB | 464.00 B | 220.69x | 0.35 | 0.08 | 280.04 MB/s | 1249.95 MB/s | 0.0809 | 84.87 | - | - | - | - | - | - |
| Gzip L9 | 100.00 KB | 464.00 B | 220.69x | 0.31 | 0.07 | 311.19 MB/s | 1345.74 MB/s | 0.0816 | 84.87 | - | - | - | - | - | - |
| Brotli Q0 | 100.00 KB | 181.00 B | 565.75x | 0.06 | 0.10 | 1519.21 MB/s | 945.54 MB/s | 0.0816 | 84.87 | - | - | - | - | - | - |
| Brotli Q1 | 100.00 KB | 111.00 B | 922.52x | 0.07 | 0.10 | 1344.37 MB/s | 1007.19 MB/s | 0.0795 | 84.87 | - | - | - | - | - | - |
| Brotli Q2 | 100.00 KB | 110.00 B | 930.91x | 0.16 | 0.10 | 627.16 MB/s | 1021.24 MB/s | 0.0809 | 84.97 | - | - | - | - | - | - |
| Brotli Q3 | 100.00 KB | 82.00 B | 1248.78x | 0.10 | 0.09 | 986.16 MB/s | 1062.83 MB/s | 0.0810 | 84.97 | - | - | - | - | - | - |
| Brotli Q4 | 100.00 KB | 82.00 B | 1248.78x | 0.22 | 0.09 | 454.17 MB/s | 1028.68 MB/s | 0.0833 | 85.20 | - | - | - | - | - | - |
| Brotli Q5 | 100.00 KB | 90.00 B | 1137.78x | 0.13 | 0.09 | 755.57 MB/s | 1028.55 MB/s | 0.0805 | 85.26 | - | - | - | - | - | - |
| Brotli Q6 | 100.00 KB | 90.00 B | 1137.78x | 0.12 | 0.09 | 784.60 MB/s | 1038.56 MB/s | 0.0815 | 85.34 | - | - | - | - | - | - |
| Brotli Q7 | 100.00 KB | 93.00 B | 1101.08x | 0.16 | 0.12 | 604.81 MB/s | 838.09 MB/s | 0.0786 | 85.45 | - | - | - | - | - | - |
| Brotli Q8 | 100.00 KB | 93.00 B | 1101.08x | 0.21 | 0.10 | 458.15 MB/s | 981.50 MB/s | 0.0787 | 85.61 | - | - | - | - | - | - |
| Brotli Q9 | 100.00 KB | 92.00 B | 1113.04x | 0.27 | 0.10 | 362.74 MB/s | 973.19 MB/s | 0.0876 | 85.61 | - | - | - | - | - | - |
| Brotli Q10 | 100.00 KB | 84.00 B | 1219.05x | 3.68 | 0.18 | 26.54 MB/s | 552.40 MB/s | 0.0782 | 85.71 | - | - | - | - | - | - |
| Brotli Q11 | 100.00 KB | 84.00 B | 1219.05x | 4.30 | 0.13 | 22.73 MB/s | 753.51 MB/s | 0.0823 | 85.87 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 4.85% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.126382)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: binary_jpeg_medium

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 100.00 KB | 65.00 B | 1575.38x | 5.96 | 0.30 | 16.40 MB/s | 330.21 MB/s | 0.0797 | 85.88 | 65 | ❌ | 0.129295 | 0.122793 | ❌ | ✅ |
| SHA256 | 100.00 KB | 64.00 B | 1600.00x | 0.08 | 0.00 | 1238.76 MB/s | 0.00 MB/s | 0.0788 | 85.88 | - | - | - | - | - | - |
| AES-GCM | 100.00 KB | 100.02 KB | 1.00x | 0.15 | 0.08 | 668.04 MB/s | 1248.96 MB/s | 0.0794 | 85.88 | - | - | - | - | - | - |
| Frackture Encrypted | 100.00 KB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 100.00 KB | 957.00 B | 107.00x | 0.22 | 0.10 | 440.95 MB/s | 1019.57 MB/s | 0.0810 | 85.88 | - | - | - | - | - | - |
| Gzip L2 | 100.00 KB | 834.00 B | 122.78x | 0.16 | 0.07 | 622.93 MB/s | 1410.73 MB/s | 0.0799 | 85.88 | - | - | - | - | - | - |
| Gzip L3 | 100.00 KB | 834.00 B | 122.78x | 0.20 | 0.09 | 486.10 MB/s | 1060.75 MB/s | 0.0824 | 85.88 | - | - | - | - | - | - |
| Gzip L4 | 100.00 KB | 565.00 B | 181.24x | 0.31 | 0.07 | 310.68 MB/s | 1350.78 MB/s | 0.0795 | 85.88 | - | - | - | - | - | - |
| Gzip L5 | 100.00 KB | 565.00 B | 181.24x | 0.40 | 0.08 | 241.35 MB/s | 1199.93 MB/s | 0.0799 | 85.88 | - | - | - | - | - | - |
| Gzip L6 | 100.00 KB | 565.00 B | 181.24x | 0.37 | 0.07 | 261.43 MB/s | 1440.02 MB/s | 0.0849 | 85.88 | - | - | - | - | - | - |
| Gzip L7 | 100.00 KB | 565.00 B | 181.24x | 0.32 | 0.07 | 300.76 MB/s | 1315.01 MB/s | 0.0834 | 85.88 | - | - | - | - | - | - |
| Gzip L8 | 100.00 KB | 565.00 B | 181.24x | 0.33 | 0.08 | 297.33 MB/s | 1195.83 MB/s | 0.0811 | 85.88 | - | - | - | - | - | - |
| Gzip L9 | 100.00 KB | 565.00 B | 181.24x | 0.43 | 0.08 | 225.30 MB/s | 1298.83 MB/s | 0.0792 | 85.88 | - | - | - | - | - | - |
| Brotli Q0 | 100.00 KB | 233.00 B | 439.48x | 0.06 | 0.11 | 1659.27 MB/s | 928.83 MB/s | 0.0807 | 85.88 | - | - | - | - | - | - |
| Brotli Q1 | 100.00 KB | 160.00 B | 640.00x | 0.07 | 0.12 | 1389.67 MB/s | 795.97 MB/s | 0.0791 | 85.88 | - | - | - | - | - | - |
| Brotli Q2 | 100.00 KB | 158.00 B | 648.10x | 0.16 | 0.10 | 598.97 MB/s | 970.21 MB/s | 0.0806 | 85.95 | - | - | - | - | - | - |
| Brotli Q3 | 100.00 KB | 132.00 B | 775.76x | 0.10 | 0.10 | 931.15 MB/s | 998.47 MB/s | 0.0791 | 85.95 | - | - | - | - | - | - |
| Brotli Q4 | 100.00 KB | 117.00 B | 875.21x | 0.14 | 0.10 | 681.32 MB/s | 1002.27 MB/s | 0.0804 | 85.99 | - | - | - | - | - | - |
| Brotli Q5 | 100.00 KB | 129.00 B | 793.80x | 0.12 | 0.10 | 824.75 MB/s | 1000.55 MB/s | 0.0787 | 86.04 | - | - | - | - | - | - |
| Brotli Q6 | 100.00 KB | 129.00 B | 793.80x | 0.14 | 0.09 | 719.86 MB/s | 1028.76 MB/s | 0.0808 | 86.15 | - | - | - | - | - | - |
| Brotli Q7 | 100.00 KB | 130.00 B | 787.69x | 0.17 | 0.10 | 571.03 MB/s | 1000.51 MB/s | 0.0783 | 86.34 | - | - | - | - | - | - |
| Brotli Q8 | 100.00 KB | 130.00 B | 787.69x | 0.24 | 0.11 | 409.14 MB/s | 881.53 MB/s | 0.0792 | 86.67 | - | - | - | - | - | - |
| Brotli Q9 | 100.00 KB | 130.00 B | 787.69x | 0.35 | 0.12 | 277.49 MB/s | 783.59 MB/s | 0.0784 | 86.67 | - | - | - | - | - | - |
| Brotli Q10 | 100.00 KB | 132.00 B | 775.76x | 3.26 | 0.11 | 29.94 MB/s | 913.02 MB/s | 0.0817 | 86.67 | - | - | - | - | - | - |
| Brotli Q11 | 100.00 KB | 132.00 B | 775.76x | 4.11 | 0.10 | 23.75 MB/s | 951.22 MB/s | 0.0800 | 86.70 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 5.03% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.129295)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: binary_pdf_medium

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 100.00 KB | 65.00 B | 1575.38x | 5.76 | 0.23 | 16.95 MB/s | 428.46 MB/s | 0.0791 | 86.72 | 65 | ❌ | 0.159119 | 0.149942 | ❌ | ✅ |
| SHA256 | 100.00 KB | 64.00 B | 1600.00x | 0.08 | 0.00 | 1217.51 MB/s | 0.00 MB/s | 0.0802 | 86.72 | - | - | - | - | - | - |
| AES-GCM | 100.00 KB | 100.02 KB | 1.00x | 0.15 | 0.08 | 648.56 MB/s | 1186.60 MB/s | 0.0799 | 86.72 | - | - | - | - | - | - |
| Frackture Encrypted | 100.00 KB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 100.00 KB | 1.46 KB | 68.59x | 0.21 | 0.10 | 468.87 MB/s | 981.13 MB/s | 0.0835 | 86.72 | - | - | - | - | - | - |
| Gzip L2 | 100.00 KB | 1.27 KB | 78.47x | 0.17 | 0.08 | 563.92 MB/s | 1248.85 MB/s | 0.0803 | 86.72 | - | - | - | - | - | - |
| Gzip L3 | 100.00 KB | 1.26 KB | 79.07x | 0.17 | 0.07 | 559.08 MB/s | 1314.69 MB/s | 0.0838 | 86.72 | - | - | - | - | - | - |
| Gzip L4 | 100.00 KB | 919.00 B | 111.43x | 0.34 | 0.08 | 287.33 MB/s | 1263.59 MB/s | 0.0780 | 86.72 | - | - | - | - | - | - |
| Gzip L5 | 100.00 KB | 802.00 B | 127.68x | 0.36 | 0.07 | 271.85 MB/s | 1351.76 MB/s | 0.0795 | 86.72 | - | - | - | - | - | - |
| Gzip L6 | 100.00 KB | 762.00 B | 134.38x | 0.45 | 0.07 | 214.65 MB/s | 1412.05 MB/s | 0.0792 | 86.72 | - | - | - | - | - | - |
| Gzip L7 | 100.00 KB | 762.00 B | 134.38x | 0.32 | 0.07 | 300.64 MB/s | 1427.26 MB/s | 0.0815 | 86.72 | - | - | - | - | - | - |
| Gzip L8 | 100.00 KB | 762.00 B | 134.38x | 0.32 | 0.07 | 303.00 MB/s | 1381.86 MB/s | 0.0791 | 86.72 | - | - | - | - | - | - |
| Gzip L9 | 100.00 KB | 762.00 B | 134.38x | 0.38 | 0.09 | 255.50 MB/s | 1141.28 MB/s | 0.0779 | 86.72 | - | - | - | - | - | - |
| Brotli Q0 | 100.00 KB | 371.00 B | 276.01x | 0.07 | 0.10 | 1451.68 MB/s | 949.28 MB/s | 0.0782 | 86.72 | - | - | - | - | - | - |
| Brotli Q1 | 100.00 KB | 297.00 B | 344.78x | 0.07 | 0.17 | 1329.62 MB/s | 560.60 MB/s | 0.0804 | 86.72 | - | - | - | - | - | - |
| Brotli Q2 | 100.00 KB | 281.00 B | 364.41x | 0.16 | 0.10 | 618.12 MB/s | 980.91 MB/s | 0.0791 | 86.75 | - | - | - | - | - | - |
| Brotli Q3 | 100.00 KB | 272.00 B | 376.47x | 0.13 | 0.10 | 771.51 MB/s | 1025.90 MB/s | 0.0780 | 86.75 | - | - | - | - | - | - |
| Brotli Q4 | 100.00 KB | 269.00 B | 380.67x | 0.17 | 0.10 | 591.77 MB/s | 1018.70 MB/s | 0.0783 | 86.76 | - | - | - | - | - | - |
| Brotli Q5 | 100.00 KB | 253.00 B | 404.74x | 0.15 | 0.10 | 658.76 MB/s | 1002.31 MB/s | 0.0802 | 86.80 | - | - | - | - | - | - |
| Brotli Q6 | 100.00 KB | 253.00 B | 404.74x | 0.18 | 0.10 | 551.00 MB/s | 1019.50 MB/s | 0.0827 | 86.94 | - | - | - | - | - | - |
| Brotli Q7 | 100.00 KB | 253.00 B | 404.74x | 0.28 | 0.10 | 350.68 MB/s | 978.98 MB/s | 0.0795 | 87.31 | - | - | - | - | - | - |
| Brotli Q8 | 100.00 KB | 253.00 B | 404.74x | 0.43 | 0.10 | 227.82 MB/s | 974.97 MB/s | 0.0801 | 88.00 | - | - | - | - | - | - |
| Brotli Q9 | 100.00 KB | 253.00 B | 404.74x | 0.71 | 0.10 | 137.83 MB/s | 950.53 MB/s | 0.0799 | 88.01 | - | - | - | - | - | - |
| Brotli Q10 | 100.00 KB | 229.00 B | 447.16x | 3.99 | 0.11 | 24.48 MB/s | 916.65 MB/s | 0.0812 | 88.01 | - | - | - | - | - | - |
| Brotli Q11 | 100.00 KB | 232.00 B | 441.38x | 5.21 | 0.11 | 18.76 MB/s | 923.00 MB/s | 0.0812 | 88.01 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 5.77% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.159119)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: binary_gif_medium

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 100.00 KB | 65.00 B | 1575.38x | 5.69 | 0.29 | 17.16 MB/s | 334.28 MB/s | 0.0803 | 88.02 | 65 | ❌ | 0.136235 | 0.136235 | ❌ | ✅ |
| SHA256 | 100.00 KB | 64.00 B | 1600.00x | 0.08 | 0.00 | 1276.62 MB/s | 0.00 MB/s | 0.0765 | 88.02 | - | - | - | - | - | - |
| AES-GCM | 100.00 KB | 100.02 KB | 1.00x | 0.15 | 0.08 | 657.72 MB/s | 1235.61 MB/s | 0.0785 | 88.02 | - | - | - | - | - | - |
| Frackture Encrypted | 100.00 KB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 100.00 KB | 522.00 B | 196.17x | 0.18 | 0.08 | 546.71 MB/s | 1170.17 MB/s | 0.0785 | 88.02 | - | - | - | - | - | - |
| Gzip L2 | 100.00 KB | 522.00 B | 196.17x | 0.15 | 0.12 | 667.72 MB/s | 800.68 MB/s | 0.0796 | 88.02 | - | - | - | - | - | - |
| Gzip L3 | 100.00 KB | 522.00 B | 196.17x | 0.14 | 0.08 | 676.82 MB/s | 1199.46 MB/s | 0.0799 | 88.02 | - | - | - | - | - | - |
| Gzip L4 | 100.00 KB | 372.00 B | 275.27x | 0.37 | 0.09 | 266.92 MB/s | 1103.60 MB/s | 0.0821 | 88.02 | - | - | - | - | - | - |
| Gzip L5 | 100.00 KB | 372.00 B | 275.27x | 0.42 | 0.09 | 233.42 MB/s | 1096.89 MB/s | 0.0795 | 88.02 | - | - | - | - | - | - |
| Gzip L6 | 100.00 KB | 372.00 B | 275.27x | 0.42 | 0.09 | 234.30 MB/s | 1048.85 MB/s | 0.0782 | 88.02 | - | - | - | - | - | - |
| Gzip L7 | 100.00 KB | 372.00 B | 275.27x | 0.36 | 0.08 | 274.70 MB/s | 1163.89 MB/s | 0.0779 | 88.02 | - | - | - | - | - | - |
| Gzip L8 | 100.00 KB | 372.00 B | 275.27x | 0.34 | 0.08 | 283.82 MB/s | 1170.80 MB/s | 0.0783 | 88.02 | - | - | - | - | - | - |
| Gzip L9 | 100.00 KB | 372.00 B | 275.27x | 0.42 | 0.09 | 234.64 MB/s | 1123.85 MB/s | 0.0804 | 88.02 | - | - | - | - | - | - |
| Brotli Q0 | 100.00 KB | 202.00 B | 506.93x | 0.07 | 0.14 | 1374.32 MB/s | 718.84 MB/s | 0.0794 | 88.02 | - | - | - | - | - | - |
| Brotli Q1 | 100.00 KB | 67.00 B | 1528.36x | 0.07 | 0.09 | 1499.41 MB/s | 1039.45 MB/s | 0.0840 | 88.02 | - | - | - | - | - | - |
| Brotli Q2 | 100.00 KB | 66.00 B | 1551.52x | 0.13 | 0.10 | 777.02 MB/s | 1025.75 MB/s | 0.0844 | 88.05 | - | - | - | - | - | - |
| Brotli Q3 | 100.00 KB | 47.00 B | 2178.72x | 0.10 | 0.09 | 979.45 MB/s | 1058.26 MB/s | 0.0874 | 88.05 | - | - | - | - | - | - |
| Brotli Q4 | 100.00 KB | 51.00 B | 2007.84x | 0.12 | 0.10 | 815.33 MB/s | 969.47 MB/s | 0.0811 | 88.05 | - | - | - | - | - | - |
| Brotli Q5 | 100.00 KB | 60.00 B | 1706.67x | 0.08 | 0.10 | 1206.12 MB/s | 997.18 MB/s | 0.0809 | 88.05 | - | - | - | - | - | - |
| Brotli Q6 | 100.00 KB | 60.00 B | 1706.67x | 0.08 | 0.10 | 1196.08 MB/s | 971.26 MB/s | 0.0823 | 88.07 | - | - | - | - | - | - |
| Brotli Q7 | 100.00 KB | 60.00 B | 1706.67x | 0.10 | 0.10 | 931.94 MB/s | 1023.65 MB/s | 0.0819 | 88.13 | - | - | - | - | - | - |
| Brotli Q8 | 100.00 KB | 60.00 B | 1706.67x | 0.11 | 0.10 | 900.02 MB/s | 1017.77 MB/s | 0.0782 | 88.22 | - | - | - | - | - | - |
| Brotli Q9 | 100.00 KB | 60.00 B | 1706.67x | 0.21 | 0.10 | 460.47 MB/s | 1020.87 MB/s | 0.0796 | 88.22 | - | - | - | - | - | - |
| Brotli Q10 | 100.00 KB | 51.00 B | 2007.84x | 3.45 | 0.11 | 28.28 MB/s | 916.58 MB/s | 0.0792 | 88.23 | - | - | - | - | - | - |
| Brotli Q11 | 100.00 KB | 51.00 B | 2007.84x | 4.26 | 0.10 | 22.95 MB/s | 973.06 MB/s | 0.0815 | 88.23 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 0.00% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.136235)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: code_javascript_medium

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 100.00 KB | 65.00 B | 1575.38x | 5.68 | 0.23 | 17.19 MB/s | 431.51 MB/s | 0.0780 | 88.24 | 65 | ❌ | 0.210678 | 0.176264 | ❌ | ✅ |
| SHA256 | 100.00 KB | 64.00 B | 1600.00x | 0.08 | 0.00 | 1299.99 MB/s | 0.00 MB/s | 0.0751 | 88.24 | - | - | - | - | - | - |
| AES-GCM | 100.00 KB | 100.02 KB | 1.00x | 0.20 | 0.08 | 487.43 MB/s | 1216.16 MB/s | 0.0818 | 88.24 | - | - | - | - | - | - |
| Frackture Encrypted | 100.00 KB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 100.00 KB | 1.54 KB | 64.85x | 0.22 | 0.12 | 451.62 MB/s | 794.90 MB/s | 0.0783 | 88.24 | - | - | - | - | - | - |
| Gzip L2 | 100.00 KB | 1.57 KB | 63.60x | 0.20 | 0.08 | 480.43 MB/s | 1160.45 MB/s | 0.0797 | 88.24 | - | - | - | - | - | - |
| Gzip L3 | 100.00 KB | 1.47 KB | 67.81x | 0.20 | 0.08 | 492.00 MB/s | 1221.37 MB/s | 0.0782 | 88.24 | - | - | - | - | - | - |
| Gzip L4 | 100.00 KB | 939.00 B | 109.05x | 0.36 | 0.07 | 274.02 MB/s | 1308.89 MB/s | 0.0812 | 88.24 | - | - | - | - | - | - |
| Gzip L5 | 100.00 KB | 931.00 B | 109.99x | 0.36 | 0.07 | 268.02 MB/s | 1399.79 MB/s | 0.0797 | 88.24 | - | - | - | - | - | - |
| Gzip L6 | 100.00 KB | 831.00 B | 123.23x | 0.34 | 0.07 | 290.18 MB/s | 1431.43 MB/s | 0.0812 | 88.24 | - | - | - | - | - | - |
| Gzip L7 | 100.00 KB | 831.00 B | 123.23x | 0.41 | 0.07 | 236.31 MB/s | 1415.68 MB/s | 0.0778 | 88.24 | - | - | - | - | - | - |
| Gzip L8 | 100.00 KB | 831.00 B | 123.23x | 0.38 | 0.07 | 257.61 MB/s | 1436.46 MB/s | 0.0784 | 88.24 | - | - | - | - | - | - |
| Gzip L9 | 100.00 KB | 831.00 B | 123.23x | 0.34 | 0.07 | 288.98 MB/s | 1470.62 MB/s | 0.0804 | 88.24 | - | - | - | - | - | - |
| Brotli Q0 | 100.00 KB | 380.00 B | 269.47x | 0.06 | 0.10 | 1611.17 MB/s | 938.34 MB/s | 0.0797 | 88.24 | - | - | - | - | - | - |
| Brotli Q1 | 100.00 KB | 314.00 B | 326.11x | 0.07 | 0.10 | 1347.97 MB/s | 998.29 MB/s | 0.0816 | 88.24 | - | - | - | - | - | - |
| Brotli Q2 | 100.00 KB | 310.00 B | 330.32x | 0.12 | 0.10 | 812.06 MB/s | 991.63 MB/s | 0.0797 | 88.24 | - | - | - | - | - | - |
| Brotli Q3 | 100.00 KB | 296.00 B | 345.95x | 0.11 | 0.10 | 871.84 MB/s | 1021.02 MB/s | 0.0805 | 88.24 | - | - | - | - | - | - |
| Brotli Q4 | 100.00 KB | 275.00 B | 372.36x | 0.15 | 0.10 | 656.34 MB/s | 1009.77 MB/s | 0.0793 | 88.24 | - | - | - | - | - | - |
| Brotli Q5 | 100.00 KB | 255.00 B | 401.57x | 0.15 | 0.10 | 636.96 MB/s | 986.85 MB/s | 0.0810 | 88.27 | - | - | - | - | - | - |
| Brotli Q6 | 100.00 KB | 254.00 B | 403.15x | 0.15 | 0.10 | 639.88 MB/s | 965.14 MB/s | 0.0792 | 88.32 | - | - | - | - | - | - |
| Brotli Q7 | 100.00 KB | 257.00 B | 398.44x | 0.23 | 0.10 | 428.35 MB/s | 1009.78 MB/s | 0.0814 | 88.57 | - | - | - | - | - | - |
| Brotli Q8 | 100.00 KB | 257.00 B | 398.44x | 0.38 | 0.10 | 255.74 MB/s | 1012.06 MB/s | 0.0783 | 89.22 | - | - | - | - | - | - |
| Brotli Q9 | 100.00 KB | 256.00 B | 400.00x | 0.74 | 0.10 | 131.13 MB/s | 946.17 MB/s | 0.0822 | 89.22 | - | - | - | - | - | - |
| Brotli Q10 | 100.00 KB | 243.00 B | 421.40x | 4.15 | 0.11 | 23.55 MB/s | 902.23 MB/s | 0.0795 | 89.22 | - | - | - | - | - | - |
| Brotli Q11 | 100.00 KB | 236.00 B | 433.90x | 5.53 | 0.11 | 17.65 MB/s | 901.54 MB/s | 0.0783 | 89.22 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 16.33% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.210678)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: code_javascript_minified_medium

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 100.00 KB | 65.00 B | 1575.38x | 5.71 | 0.23 | 17.10 MB/s | 420.88 MB/s | 0.0807 | 89.23 | 65 | ❌ | 0.248601 | 0.216233 | ❌ | ✅ |
| SHA256 | 100.00 KB | 64.00 B | 1600.00x | 0.08 | 0.00 | 1290.23 MB/s | 0.00 MB/s | 0.0757 | 89.23 | - | - | - | - | - | - |
| AES-GCM | 100.00 KB | 100.02 KB | 1.00x | 0.15 | 0.08 | 657.34 MB/s | 1233.22 MB/s | 0.0808 | 89.23 | - | - | - | - | - | - |
| Frackture Encrypted | 100.00 KB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 100.00 KB | 1.03 KB | 97.34x | 0.20 | 0.12 | 495.12 MB/s | 837.41 MB/s | 0.0836 | 89.23 | - | - | - | - | - | - |
| Gzip L2 | 100.00 KB | 1013.00 B | 101.09x | 0.18 | 0.07 | 550.75 MB/s | 1312.18 MB/s | 0.0789 | 89.23 | - | - | - | - | - | - |
| Gzip L3 | 100.00 KB | 1.01 KB | 99.22x | 0.16 | 0.07 | 619.47 MB/s | 1394.47 MB/s | 0.0814 | 89.23 | - | - | - | - | - | - |
| Gzip L4 | 100.00 KB | 607.00 B | 168.70x | 0.31 | 0.07 | 314.84 MB/s | 1496.62 MB/s | 0.0799 | 89.23 | - | - | - | - | - | - |
| Gzip L5 | 100.00 KB | 607.00 B | 168.70x | 0.33 | 0.07 | 299.35 MB/s | 1499.93 MB/s | 0.0818 | 89.23 | - | - | - | - | - | - |
| Gzip L6 | 100.00 KB | 607.00 B | 168.70x | 0.31 | 0.07 | 314.82 MB/s | 1464.73 MB/s | 0.0790 | 89.23 | - | - | - | - | - | - |
| Gzip L7 | 100.00 KB | 607.00 B | 168.70x | 0.35 | 0.11 | 281.05 MB/s | 895.54 MB/s | 0.0780 | 89.23 | - | - | - | - | - | - |
| Gzip L8 | 100.00 KB | 607.00 B | 168.70x | 0.32 | 0.07 | 302.06 MB/s | 1457.90 MB/s | 0.0803 | 89.23 | - | - | - | - | - | - |
| Gzip L9 | 100.00 KB | 607.00 B | 168.70x | 0.31 | 0.07 | 315.37 MB/s | 1497.63 MB/s | 0.0809 | 89.23 | - | - | - | - | - | - |
| Brotli Q0 | 100.00 KB | 265.00 B | 386.42x | 0.06 | 0.10 | 1678.35 MB/s | 943.68 MB/s | 0.0814 | 89.23 | - | - | - | - | - | - |
| Brotli Q1 | 100.00 KB | 198.00 B | 517.17x | 0.07 | 0.10 | 1411.30 MB/s | 1012.71 MB/s | 0.0791 | 89.23 | - | - | - | - | - | - |
| Brotli Q2 | 100.00 KB | 190.00 B | 538.95x | 0.11 | 0.10 | 865.72 MB/s | 1022.94 MB/s | 0.0837 | 89.23 | - | - | - | - | - | - |
| Brotli Q3 | 100.00 KB | 177.00 B | 578.53x | 0.11 | 0.09 | 915.64 MB/s | 1040.25 MB/s | 0.0791 | 89.23 | - | - | - | - | - | - |
| Brotli Q4 | 100.00 KB | 169.00 B | 605.92x | 0.13 | 0.09 | 748.56 MB/s | 1035.10 MB/s | 0.0812 | 89.23 | - | - | - | - | - | - |
| Brotli Q5 | 100.00 KB | 157.00 B | 652.23x | 0.11 | 0.09 | 927.04 MB/s | 1038.03 MB/s | 0.0794 | 89.23 | - | - | - | - | - | - |
| Brotli Q6 | 100.00 KB | 157.00 B | 652.23x | 0.11 | 0.12 | 877.56 MB/s | 814.29 MB/s | 0.0807 | 89.27 | - | - | - | - | - | - |
| Brotli Q7 | 100.00 KB | 157.00 B | 652.23x | 0.17 | 0.09 | 580.41 MB/s | 1056.86 MB/s | 0.0796 | 89.43 | - | - | - | - | - | - |
| Brotli Q8 | 100.00 KB | 157.00 B | 652.23x | 0.24 | 0.09 | 405.90 MB/s | 1050.80 MB/s | 0.0837 | 89.83 | - | - | - | - | - | - |
| Brotli Q9 | 100.00 KB | 157.00 B | 652.23x | 0.45 | 0.17 | 219.31 MB/s | 586.97 MB/s | 0.0789 | 89.83 | - | - | - | - | - | - |
| Brotli Q10 | 100.00 KB | 168.00 B | 609.52x | 3.47 | 0.11 | 28.13 MB/s | 898.57 MB/s | 0.0835 | 89.84 | - | - | - | - | - | - |
| Brotli Q11 | 100.00 KB | 165.00 B | 620.61x | 4.62 | 0.11 | 21.15 MB/s | 916.86 MB/s | 0.0778 | 89.84 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 13.02% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.248601)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: code_python_medium

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 100.00 KB | 65.00 B | 1575.38x | 5.71 | 0.23 | 17.10 MB/s | 431.10 MB/s | 0.0812 | 89.85 | 65 | ❌ | 0.201540 | 0.173739 | ❌ | ✅ |
| SHA256 | 100.00 KB | 64.00 B | 1600.00x | 0.08 | 0.00 | 1283.02 MB/s | 0.00 MB/s | 0.0761 | 89.85 | - | - | - | - | - | - |
| AES-GCM | 100.00 KB | 100.02 KB | 1.00x | 0.15 | 0.08 | 659.38 MB/s | 1204.59 MB/s | 0.0808 | 89.85 | - | - | - | - | - | - |
| Frackture Encrypted | 100.00 KB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 100.00 KB | 2.50 KB | 39.95x | 0.26 | 0.12 | 368.71 MB/s | 805.02 MB/s | 0.0811 | 89.85 | - | - | - | - | - | - |
| Gzip L2 | 100.00 KB | 2.22 KB | 45.07x | 0.21 | 0.09 | 474.48 MB/s | 1069.34 MB/s | 0.0804 | 89.85 | - | - | - | - | - | - |
| Gzip L3 | 100.00 KB | 1.71 KB | 58.65x | 0.19 | 0.08 | 519.79 MB/s | 1183.98 MB/s | 0.0818 | 89.85 | - | - | - | - | - | - |
| Gzip L4 | 100.00 KB | 1.48 KB | 67.77x | 0.37 | 0.08 | 265.66 MB/s | 1230.81 MB/s | 0.0791 | 89.85 | - | - | - | - | - | - |
| Gzip L5 | 100.00 KB | 1.39 KB | 72.06x | 0.42 | 0.08 | 233.74 MB/s | 1270.08 MB/s | 0.0782 | 89.85 | - | - | - | - | - | - |
| Gzip L6 | 100.00 KB | 1.35 KB | 73.83x | 0.42 | 0.08 | 231.42 MB/s | 1217.77 MB/s | 0.0802 | 89.85 | - | - | - | - | - | - |
| Gzip L7 | 100.00 KB | 1.13 KB | 88.43x | 0.36 | 0.08 | 269.09 MB/s | 1281.41 MB/s | 0.0798 | 89.85 | - | - | - | - | - | - |
| Gzip L8 | 100.00 KB | 1.13 KB | 88.43x | 0.36 | 0.07 | 272.69 MB/s | 1365.40 MB/s | 0.0808 | 89.85 | - | - | - | - | - | - |
| Gzip L9 | 100.00 KB | 1.13 KB | 88.43x | 0.36 | 0.09 | 272.09 MB/s | 1084.27 MB/s | 0.0791 | 89.85 | - | - | - | - | - | - |
| Brotli Q0 | 100.00 KB | 671.00 B | 152.61x | 0.07 | 0.13 | 1379.66 MB/s | 766.73 MB/s | 0.0793 | 89.85 | - | - | - | - | - | - |
| Brotli Q1 | 100.00 KB | 604.00 B | 169.54x | 0.08 | 0.12 | 1177.19 MB/s | 827.19 MB/s | 0.0778 | 89.85 | - | - | - | - | - | - |
| Brotli Q2 | 100.00 KB | 589.00 B | 173.85x | 0.14 | 0.12 | 693.13 MB/s | 797.60 MB/s | 0.0791 | 89.85 | - | - | - | - | - | - |
| Brotli Q3 | 100.00 KB | 560.00 B | 182.86x | 0.13 | 0.11 | 760.31 MB/s | 853.91 MB/s | 0.0779 | 89.85 | - | - | - | - | - | - |
| Brotli Q4 | 100.00 KB | 534.00 B | 191.76x | 0.20 | 0.10 | 494.79 MB/s | 958.46 MB/s | 0.0800 | 89.85 | - | - | - | - | - | - |
| Brotli Q5 | 100.00 KB | 505.00 B | 202.77x | 0.19 | 0.10 | 523.09 MB/s | 956.20 MB/s | 0.0783 | 89.85 | - | - | - | - | - | - |
| Brotli Q6 | 100.00 KB | 506.00 B | 202.37x | 0.18 | 0.10 | 528.76 MB/s | 990.41 MB/s | 0.0797 | 89.87 | - | - | - | - | - | - |
| Brotli Q7 | 100.00 KB | 505.00 B | 202.77x | 0.33 | 0.10 | 296.90 MB/s | 969.44 MB/s | 0.0834 | 90.23 | - | - | - | - | - | - |
| Brotli Q8 | 100.00 KB | 505.00 B | 202.77x | 0.73 | 0.10 | 134.31 MB/s | 943.10 MB/s | 0.0784 | 91.36 | - | - | - | - | - | - |
| Brotli Q9 | 100.00 KB | 505.00 B | 202.77x | 1.42 | 0.11 | 68.72 MB/s | 882.99 MB/s | 0.0826 | 91.36 | - | - | - | - | - | - |
| Brotli Q10 | 100.00 KB | 484.00 B | 211.57x | 4.59 | 0.12 | 21.27 MB/s | 844.86 MB/s | 0.0784 | 91.36 | - | - | - | - | - | - |
| Brotli Q11 | 100.00 KB | 491.00 B | 208.55x | 6.41 | 0.12 | 15.22 MB/s | 844.58 MB/s | 0.0820 | 91.36 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 13.79% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.201540)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: mixed_payload_medium

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 100.00 KB | 65.00 B | 1575.38x | 7.75 | 0.72 | 12.60 MB/s | 135.57 MB/s | 0.0834 | 89.86 | 65 | ❌ | 0.067139 | 0.050524 | ❌ | ✅ |
| SHA256 | 100.00 KB | 64.00 B | 1600.00x | 0.08 | 0.00 | 1282.64 MB/s | 0.00 MB/s | 0.0761 | 89.98 | - | - | - | - | - | - |
| AES-GCM | 100.00 KB | 100.02 KB | 1.00x | 0.15 | 0.08 | 646.66 MB/s | 1280.10 MB/s | 0.0818 | 90.04 | - | - | - | - | - | - |
| Frackture Encrypted | 100.00 KB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 100.00 KB | 2.76 KB | 36.20x | 0.25 | 0.12 | 385.28 MB/s | 834.55 MB/s | 0.0811 | 90.39 | - | - | - | - | - | - |
| Gzip L2 | 100.00 KB | 2.90 KB | 34.48x | 0.23 | 0.10 | 428.55 MB/s | 999.85 MB/s | 0.0783 | 90.39 | - | - | - | - | - | - |
| Gzip L3 | 100.00 KB | 2.27 KB | 44.01x | 0.20 | 0.13 | 477.57 MB/s | 725.92 MB/s | 0.0782 | 90.39 | - | - | - | - | - | - |
| Gzip L4 | 100.00 KB | 1.77 KB | 56.36x | 0.39 | 0.08 | 249.07 MB/s | 1150.40 MB/s | 0.0813 | 90.39 | - | - | - | - | - | - |
| Gzip L5 | 100.00 KB | 1.72 KB | 58.12x | 0.38 | 0.08 | 258.94 MB/s | 1208.81 MB/s | 0.0794 | 90.39 | - | - | - | - | - | - |
| Gzip L6 | 100.00 KB | 1.68 KB | 59.60x | 0.38 | 0.09 | 256.91 MB/s | 1140.54 MB/s | 0.0808 | 90.39 | - | - | - | - | - | - |
| Gzip L7 | 100.00 KB | 1.68 KB | 59.60x | 0.39 | 0.08 | 250.13 MB/s | 1188.12 MB/s | 0.0779 | 90.39 | - | - | - | - | - | - |
| Gzip L8 | 100.00 KB | 1.68 KB | 59.60x | 0.38 | 0.08 | 255.74 MB/s | 1202.12 MB/s | 0.0807 | 90.39 | - | - | - | - | - | - |
| Gzip L9 | 100.00 KB | 1.68 KB | 59.60x | 0.37 | 0.08 | 265.02 MB/s | 1264.55 MB/s | 0.0795 | 90.39 | - | - | - | - | - | - |
| Brotli Q0 | 100.00 KB | 1.20 KB | 83.12x | 0.07 | 0.11 | 1385.39 MB/s | 901.15 MB/s | 0.0807 | 90.39 | - | - | - | - | - | - |
| Brotli Q1 | 100.00 KB | 1.12 KB | 89.28x | 0.09 | 0.11 | 1060.51 MB/s | 925.43 MB/s | 0.0796 | 90.39 | - | - | - | - | - | - |
| Brotli Q2 | 100.00 KB | 1.11 KB | 90.14x | 0.14 | 0.11 | 692.33 MB/s | 910.69 MB/s | 0.0810 | 90.39 | - | - | - | - | - | - |
| Brotli Q3 | 100.00 KB | 1.09 KB | 91.76x | 0.14 | 0.10 | 681.35 MB/s | 961.78 MB/s | 0.0806 | 90.39 | - | - | - | - | - | - |
| Brotli Q4 | 100.00 KB | 1.04 KB | 96.51x | 0.22 | 0.11 | 450.24 MB/s | 920.70 MB/s | 0.0812 | 90.39 | - | - | - | - | - | - |
| Brotli Q5 | 100.00 KB | 996.00 B | 102.81x | 0.26 | 0.12 | 381.10 MB/s | 784.14 MB/s | 0.0782 | 90.39 | - | - | - | - | - | - |
| Brotli Q6 | 100.00 KB | 995.00 B | 102.91x | 0.31 | 0.11 | 316.16 MB/s | 903.99 MB/s | 0.0785 | 90.41 | - | - | - | - | - | - |
| Brotli Q7 | 100.00 KB | 993.00 B | 103.12x | 0.43 | 0.11 | 229.25 MB/s | 895.67 MB/s | 0.0815 | 90.81 | - | - | - | - | - | - |
| Brotli Q8 | 100.00 KB | 993.00 B | 103.12x | 0.97 | 0.11 | 100.47 MB/s | 850.26 MB/s | 0.0855 | 92.40 | - | - | - | - | - | - |
| Brotli Q9 | 100.00 KB | 998.00 B | 102.61x | 2.72 | 0.12 | 35.84 MB/s | 847.41 MB/s | 0.0838 | 92.40 | - | - | - | - | - | - |
| Brotli Q10 | 100.00 KB | 912.00 B | 112.28x | 5.80 | 0.12 | 16.84 MB/s | 806.34 MB/s | 0.0809 | 92.40 | - | - | - | - | - | - |
| Brotli Q11 | 100.00 KB | 900.00 B | 113.78x | 7.47 | 0.12 | 13.08 MB/s | 821.10 MB/s | 0.0817 | 92.40 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 24.75% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.067139)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: structured_sqlite_medium

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 100.00 KB | 65.00 B | 1575.38x | 5.89 | 0.25 | 16.59 MB/s | 384.25 MB/s | 0.0782 | 92.42 | 65 | ❌ | 0.043278 | 0.043278 | ❌ | ✅ |
| SHA256 | 100.00 KB | 64.00 B | 1600.00x | 0.08 | 0.00 | 1269.20 MB/s | 0.00 MB/s | 0.0769 | 92.42 | - | - | - | - | - | - |
| AES-GCM | 100.00 KB | 100.02 KB | 1.00x | 0.15 | 0.08 | 668.28 MB/s | 1272.64 MB/s | 0.0787 | 92.42 | - | - | - | - | - | - |
| Frackture Encrypted | 100.00 KB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 100.00 KB | 1.13 KB | 88.66x | 0.21 | 0.13 | 454.94 MB/s | 747.93 MB/s | 0.0797 | 92.42 | - | - | - | - | - | - |
| Gzip L2 | 100.00 KB | 1.12 KB | 89.12x | 0.20 | 0.08 | 496.22 MB/s | 1175.29 MB/s | 0.0785 | 92.42 | - | - | - | - | - | - |
| Gzip L3 | 100.00 KB | 1.09 KB | 91.59x | 0.17 | 0.08 | 562.42 MB/s | 1269.90 MB/s | 0.0798 | 92.42 | - | - | - | - | - | - |
| Gzip L4 | 100.00 KB | 765.00 B | 133.86x | 0.42 | 0.15 | 232.62 MB/s | 645.49 MB/s | 0.0792 | 92.42 | - | - | - | - | - | - |
| Gzip L5 | 100.00 KB | 763.00 B | 134.21x | 0.45 | 0.16 | 214.81 MB/s | 604.13 MB/s | 0.0811 | 92.42 | - | - | - | - | - | - |
| Gzip L6 | 100.00 KB | 741.00 B | 138.19x | 0.37 | 0.14 | 261.70 MB/s | 673.84 MB/s | 0.0796 | 92.42 | - | - | - | - | - | - |
| Gzip L7 | 100.00 KB | 741.00 B | 138.19x | 0.45 | 0.14 | 215.57 MB/s | 683.61 MB/s | 0.0819 | 92.42 | - | - | - | - | - | - |
| Gzip L8 | 100.00 KB | 741.00 B | 138.19x | 0.47 | 0.12 | 209.20 MB/s | 819.44 MB/s | 0.0804 | 92.42 | - | - | - | - | - | - |
| Gzip L9 | 100.00 KB | 741.00 B | 138.19x | 0.63 | 0.12 | 154.16 MB/s | 783.27 MB/s | 0.0823 | 92.42 | - | - | - | - | - | - |
| Brotli Q0 | 100.00 KB | 653.00 B | 156.81x | 0.07 | 0.10 | 1466.60 MB/s | 941.90 MB/s | 0.0833 | 92.42 | - | - | - | - | - | - |
| Brotli Q1 | 100.00 KB | 556.00 B | 184.17x | 0.09 | 0.10 | 1136.60 MB/s | 942.42 MB/s | 0.0790 | 92.42 | - | - | - | - | - | - |
| Brotli Q2 | 100.00 KB | 513.00 B | 199.61x | 0.13 | 0.11 | 747.88 MB/s | 874.58 MB/s | 0.0826 | 92.42 | - | - | - | - | - | - |
| Brotli Q3 | 100.00 KB | 500.00 B | 204.80x | 0.14 | 0.10 | 718.44 MB/s | 947.91 MB/s | 0.0780 | 92.42 | - | - | - | - | - | - |
| Brotli Q4 | 100.00 KB | 486.00 B | 210.70x | 0.22 | 0.12 | 440.24 MB/s | 795.71 MB/s | 0.0812 | 92.42 | - | - | - | - | - | - |
| Brotli Q5 | 100.00 KB | 468.00 B | 218.80x | 0.30 | 0.10 | 320.91 MB/s | 942.90 MB/s | 0.0782 | 92.42 | - | - | - | - | - | - |
| Brotli Q6 | 100.00 KB | 468.00 B | 218.80x | 0.29 | 0.10 | 340.26 MB/s | 958.98 MB/s | 0.0814 | 92.42 | - | - | - | - | - | - |
| Brotli Q7 | 100.00 KB | 465.00 B | 220.22x | 0.35 | 0.10 | 283.04 MB/s | 930.26 MB/s | 0.0800 | 92.52 | - | - | - | - | - | - |
| Brotli Q8 | 100.00 KB | 465.00 B | 220.22x | 0.56 | 0.11 | 174.65 MB/s | 928.02 MB/s | 0.0784 | 93.10 | - | - | - | - | - | - |
| Brotli Q9 | 100.00 KB | 465.00 B | 220.22x | 1.15 | 0.11 | 84.70 MB/s | 873.58 MB/s | 0.0847 | 93.10 | - | - | - | - | - | - |
| Brotli Q10 | 100.00 KB | 401.00 B | 255.36x | 4.49 | 0.12 | 21.75 MB/s | 784.60 MB/s | 0.0781 | 93.10 | - | - | - | - | - | - |
| Brotli Q11 | 100.00 KB | 392.00 B | 261.22x | 6.41 | 0.11 | 15.24 MB/s | 868.19 MB/s | 0.0853 | 93.10 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 0.00% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.043278)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: structured_pickle_medium

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 100.00 KB | 65.00 B | 1575.38x | 5.78 | 0.23 | 16.91 MB/s | 424.02 MB/s | 0.0808 | 93.12 | 65 | ❌ | 0.212640 | 0.180567 | ❌ | ✅ |
| SHA256 | 100.00 KB | 64.00 B | 1600.00x | 0.08 | 0.00 | 1279.86 MB/s | 0.00 MB/s | 0.0763 | 93.12 | - | - | - | - | - | - |
| AES-GCM | 100.00 KB | 100.02 KB | 1.00x | 0.15 | 0.14 | 631.72 MB/s | 712.06 MB/s | 0.0807 | 93.12 | - | - | - | - | - | - |
| Frackture Encrypted | 100.00 KB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 100.00 KB | 1.00 KB | 99.61x | 0.20 | 0.09 | 495.29 MB/s | 1052.56 MB/s | 0.0820 | 93.12 | - | - | - | - | - | - |
| Gzip L2 | 100.00 KB | 970.00 B | 105.57x | 0.20 | 0.07 | 486.50 MB/s | 1320.86 MB/s | 0.0812 | 93.12 | - | - | - | - | - | - |
| Gzip L3 | 100.00 KB | 963.00 B | 106.33x | 0.16 | 0.09 | 616.09 MB/s | 1100.20 MB/s | 0.0779 | 93.12 | - | - | - | - | - | - |
| Gzip L4 | 100.00 KB | 583.00 B | 175.64x | 0.34 | 0.07 | 288.95 MB/s | 1411.95 MB/s | 0.0813 | 93.12 | - | - | - | - | - | - |
| Gzip L5 | 100.00 KB | 583.00 B | 175.64x | 0.31 | 0.06 | 315.61 MB/s | 1565.81 MB/s | 0.0803 | 93.12 | - | - | - | - | - | - |
| Gzip L6 | 100.00 KB | 583.00 B | 175.64x | 0.43 | 0.06 | 228.13 MB/s | 1586.93 MB/s | 0.0802 | 93.12 | - | - | - | - | - | - |
| Gzip L7 | 100.00 KB | 583.00 B | 175.64x | 0.41 | 0.06 | 237.20 MB/s | 1542.39 MB/s | 0.0780 | 93.12 | - | - | - | - | - | - |
| Gzip L8 | 100.00 KB | 583.00 B | 175.64x | 0.38 | 0.06 | 258.82 MB/s | 1533.98 MB/s | 0.0779 | 93.12 | - | - | - | - | - | - |
| Gzip L9 | 100.00 KB | 583.00 B | 175.64x | 0.34 | 0.06 | 285.09 MB/s | 1531.60 MB/s | 0.0795 | 93.12 | - | - | - | - | - | - |
| Brotli Q0 | 100.00 KB | 251.00 B | 407.97x | 0.06 | 0.10 | 1692.92 MB/s | 962.79 MB/s | 0.0787 | 93.12 | - | - | - | - | - | - |
| Brotli Q1 | 100.00 KB | 173.00 B | 591.91x | 0.07 | 0.10 | 1365.04 MB/s | 1019.60 MB/s | 0.0783 | 93.12 | - | - | - | - | - | - |
| Brotli Q2 | 100.00 KB | 176.00 B | 581.82x | 0.12 | 0.10 | 827.24 MB/s | 1005.16 MB/s | 0.0782 | 93.12 | - | - | - | - | - | - |
| Brotli Q3 | 100.00 KB | 150.00 B | 682.67x | 0.12 | 0.09 | 824.25 MB/s | 1049.67 MB/s | 0.0779 | 93.12 | - | - | - | - | - | - |
| Brotli Q4 | 100.00 KB | 145.00 B | 706.21x | 0.19 | 0.10 | 522.28 MB/s | 997.47 MB/s | 0.0782 | 93.12 | - | - | - | - | - | - |
| Brotli Q5 | 100.00 KB | 142.00 B | 721.13x | 0.12 | 0.10 | 832.40 MB/s | 1016.83 MB/s | 0.0791 | 93.12 | - | - | - | - | - | - |
| Brotli Q6 | 100.00 KB | 142.00 B | 721.13x | 0.10 | 0.10 | 935.86 MB/s | 1022.21 MB/s | 0.0781 | 93.12 | - | - | - | - | - | - |
| Brotli Q7 | 100.00 KB | 142.00 B | 721.13x | 0.12 | 0.09 | 795.45 MB/s | 1044.89 MB/s | 0.0778 | 93.14 | - | - | - | - | - | - |
| Brotli Q8 | 100.00 KB | 142.00 B | 721.13x | 0.23 | 0.09 | 418.77 MB/s | 1046.42 MB/s | 0.0782 | 93.28 | - | - | - | - | - | - |
| Brotli Q9 | 100.00 KB | 143.00 B | 716.08x | 0.36 | 0.10 | 273.46 MB/s | 988.20 MB/s | 0.0821 | 93.28 | - | - | - | - | - | - |
| Brotli Q10 | 100.00 KB | 141.00 B | 726.24x | 3.71 | 0.11 | 26.29 MB/s | 929.63 MB/s | 0.0780 | 93.28 | - | - | - | - | - | - |
| Brotli Q11 | 100.00 KB | 139.00 B | 736.69x | 4.82 | 0.11 | 20.25 MB/s | 918.87 MB/s | 0.0798 | 93.28 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 15.08% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.212640)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: text_plain_medium

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 100.00 KB | 65.00 B | 1575.38x | 5.77 | 0.23 | 16.94 MB/s | 422.02 MB/s | 0.0780 | 93.63 | 65 | ❌ | 0.313108 | 0.244711 | ❌ | ✅ |
| SHA256 | 100.00 KB | 64.00 B | 1600.00x | 0.08 | 0.00 | 1283.95 MB/s | 0.00 MB/s | 0.0761 | 93.63 | - | - | - | - | - | - |
| AES-GCM | 100.00 KB | 100.02 KB | 1.00x | 0.15 | 0.14 | 631.27 MB/s | 711.18 MB/s | 0.0781 | 93.63 | - | - | - | - | - | - |
| Frackture Encrypted | 100.00 KB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 100.00 KB | 1.29 KB | 77.40x | 0.21 | 0.09 | 470.83 MB/s | 1054.64 MB/s | 0.0799 | 93.63 | - | - | - | - | - | - |
| Gzip L2 | 100.00 KB | 1.27 KB | 78.71x | 0.17 | 0.08 | 587.35 MB/s | 1291.37 MB/s | 0.0808 | 93.63 | - | - | - | - | - | - |
| Gzip L3 | 100.00 KB | 1.24 KB | 80.95x | 0.16 | 0.08 | 609.59 MB/s | 1279.75 MB/s | 0.0811 | 93.63 | - | - | - | - | - | - |
| Gzip L4 | 100.00 KB | 933.00 B | 109.75x | 0.33 | 0.09 | 296.14 MB/s | 1130.59 MB/s | 0.0798 | 93.63 | - | - | - | - | - | - |
| Gzip L5 | 100.00 KB | 931.00 B | 109.99x | 0.35 | 0.07 | 280.09 MB/s | 1363.08 MB/s | 0.0795 | 93.63 | - | - | - | - | - | - |
| Gzip L6 | 100.00 KB | 931.00 B | 109.99x | 0.32 | 0.07 | 304.07 MB/s | 1409.22 MB/s | 0.0811 | 93.63 | - | - | - | - | - | - |
| Gzip L7 | 100.00 KB | 931.00 B | 109.99x | 0.32 | 0.07 | 308.15 MB/s | 1460.63 MB/s | 0.0796 | 93.63 | - | - | - | - | - | - |
| Gzip L8 | 100.00 KB | 931.00 B | 109.99x | 0.31 | 0.07 | 313.78 MB/s | 1387.02 MB/s | 0.0831 | 93.63 | - | - | - | - | - | - |
| Gzip L9 | 100.00 KB | 931.00 B | 109.99x | 0.33 | 0.07 | 294.08 MB/s | 1392.07 MB/s | 0.0781 | 93.63 | - | - | - | - | - | - |
| Brotli Q0 | 100.00 KB | 455.00 B | 225.05x | 0.06 | 0.18 | 1626.06 MB/s | 545.57 MB/s | 0.0791 | 93.63 | - | - | - | - | - | - |
| Brotli Q1 | 100.00 KB | 387.00 B | 264.60x | 0.07 | 0.11 | 1362.79 MB/s | 860.67 MB/s | 0.0780 | 93.63 | - | - | - | - | - | - |
| Brotli Q2 | 100.00 KB | 379.00 B | 270.18x | 0.18 | 0.10 | 543.62 MB/s | 971.19 MB/s | 0.0784 | 93.63 | - | - | - | - | - | - |
| Brotli Q3 | 100.00 KB | 366.00 B | 279.78x | 0.12 | 0.10 | 795.06 MB/s | 1006.01 MB/s | 0.0783 | 93.63 | - | - | - | - | - | - |
| Brotli Q4 | 100.00 KB | 353.00 B | 290.08x | 0.21 | 0.10 | 474.49 MB/s | 989.00 MB/s | 0.0782 | 93.63 | - | - | - | - | - | - |
| Brotli Q5 | 100.00 KB | 348.00 B | 294.25x | 0.16 | 0.10 | 609.89 MB/s | 1000.67 MB/s | 0.0797 | 93.63 | - | - | - | - | - | - |
| Brotli Q6 | 100.00 KB | 348.00 B | 294.25x | 0.14 | 0.10 | 701.92 MB/s | 1015.06 MB/s | 0.0784 | 93.63 | - | - | - | - | - | - |
| Brotli Q7 | 100.00 KB | 348.00 B | 294.25x | 0.19 | 0.10 | 516.71 MB/s | 988.00 MB/s | 0.0806 | 93.71 | - | - | - | - | - | - |
| Brotli Q8 | 100.00 KB | 348.00 B | 294.25x | 0.33 | 0.10 | 292.42 MB/s | 1017.63 MB/s | 0.0801 | 94.17 | - | - | - | - | - | - |
| Brotli Q9 | 100.00 KB | 352.00 B | 290.91x | 1.00 | 0.11 | 97.41 MB/s | 908.24 MB/s | 0.0828 | 94.17 | - | - | - | - | - | - |
| Brotli Q10 | 100.00 KB | 321.00 B | 319.00x | 4.29 | 0.19 | 22.76 MB/s | 508.50 MB/s | 0.0829 | 94.17 | - | - | - | - | - | - |
| Brotli Q11 | 100.00 KB | 318.00 B | 322.01x | 5.75 | 0.11 | 16.99 MB/s | 895.63 MB/s | 0.0812 | 94.17 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 21.84% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.313108)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: text_log_medium

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 100.00 KB | 65.00 B | 1575.38x | 6.38 | 0.36 | 15.32 MB/s | 270.88 MB/s | 0.0833 | 94.19 | 65 | ❌ | 0.199651 | 0.123128 | ❌ | ✅ |
| SHA256 | 100.00 KB | 64.00 B | 1600.00x | 0.08 | 0.00 | 1203.42 MB/s | 0.00 MB/s | 0.0811 | 94.19 | - | - | - | - | - | - |
| AES-GCM | 100.00 KB | 100.02 KB | 1.00x | 0.25 | 0.13 | 387.45 MB/s | 773.97 MB/s | 0.0789 | 94.19 | - | - | - | - | - | - |
| Frackture Encrypted | 100.00 KB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 100.00 KB | 1.26 KB | 79.56x | 0.26 | 0.12 | 373.43 MB/s | 794.58 MB/s | 0.0805 | 94.19 | - | - | - | - | - | - |
| Gzip L2 | 100.00 KB | 1.22 KB | 81.79x | 0.28 | 0.12 | 346.57 MB/s | 782.38 MB/s | 0.0871 | 94.19 | - | - | - | - | - | - |
| Gzip L3 | 100.00 KB | 1.25 KB | 79.69x | 0.26 | 0.12 | 382.96 MB/s | 812.85 MB/s | 0.0845 | 94.19 | - | - | - | - | - | - |
| Gzip L4 | 100.00 KB | 1.15 KB | 86.85x | 0.52 | 0.11 | 186.64 MB/s | 915.86 MB/s | 0.0874 | 94.19 | - | - | - | - | - | - |
| Gzip L5 | 100.00 KB | 877.00 B | 116.76x | 0.37 | 0.09 | 267.25 MB/s | 1060.18 MB/s | 0.0821 | 94.19 | - | - | - | - | - | - |
| Gzip L6 | 100.00 KB | 877.00 B | 116.76x | 0.43 | 0.08 | 228.47 MB/s | 1190.25 MB/s | 0.0782 | 94.19 | - | - | - | - | - | - |
| Gzip L7 | 100.00 KB | 794.00 B | 128.97x | 0.49 | 0.07 | 200.65 MB/s | 1331.21 MB/s | 0.0812 | 94.19 | - | - | - | - | - | - |
| Gzip L8 | 100.00 KB | 768.00 B | 133.33x | 0.38 | 0.08 | 259.52 MB/s | 1174.39 MB/s | 0.0812 | 94.19 | - | - | - | - | - | - |
| Gzip L9 | 100.00 KB | 768.00 B | 133.33x | 0.42 | 0.11 | 234.94 MB/s | 890.15 MB/s | 0.0875 | 94.19 | - | - | - | - | - | - |
| Brotli Q0 | 100.00 KB | 333.00 B | 307.51x | 0.08 | 0.17 | 1232.64 MB/s | 589.22 MB/s | 0.0859 | 94.19 | - | - | - | - | - | - |
| Brotli Q1 | 100.00 KB | 261.00 B | 392.34x | 0.10 | 0.23 | 1005.90 MB/s | 420.27 MB/s | 0.0823 | 94.19 | - | - | - | - | - | - |
| Brotli Q2 | 100.00 KB | 246.00 B | 416.26x | 0.22 | 0.10 | 439.06 MB/s | 945.16 MB/s | 0.0845 | 94.19 | - | - | - | - | - | - |
| Brotli Q3 | 100.00 KB | 233.00 B | 439.48x | 0.13 | 0.10 | 729.94 MB/s | 973.52 MB/s | 0.0835 | 94.19 | - | - | - | - | - | - |
| Brotli Q4 | 100.00 KB | 228.00 B | 449.12x | 0.19 | 0.15 | 510.82 MB/s | 636.88 MB/s | 0.0846 | 94.19 | - | - | - | - | - | - |
| Brotli Q5 | 100.00 KB | 207.00 B | 494.69x | 0.17 | 0.21 | 575.02 MB/s | 475.90 MB/s | 0.0809 | 94.19 | - | - | - | - | - | - |
| Brotli Q6 | 100.00 KB | 207.00 B | 494.69x | 0.14 | 0.10 | 711.12 MB/s | 974.76 MB/s | 0.0842 | 94.19 | - | - | - | - | - | - |
| Brotli Q7 | 100.00 KB | 209.00 B | 489.95x | 0.20 | 0.16 | 481.88 MB/s | 621.64 MB/s | 0.0854 | 94.20 | - | - | - | - | - | - |
| Brotli Q8 | 100.00 KB | 209.00 B | 489.95x | 0.40 | 0.16 | 246.73 MB/s | 629.78 MB/s | 0.0800 | 94.41 | - | - | - | - | - | - |
| Brotli Q9 | 100.00 KB | 209.00 B | 489.95x | 0.57 | 0.16 | 172.61 MB/s | 603.98 MB/s | 0.0818 | 94.41 | - | - | - | - | - | - |
| Brotli Q10 | 100.00 KB | 193.00 B | 530.57x | 5.60 | 0.16 | 17.42 MB/s | 606.44 MB/s | 0.0875 | 94.41 | - | - | - | - | - | - |
| Brotli Q11 | 100.00 KB | 192.00 B | 533.33x | 6.14 | 0.16 | 15.91 MB/s | 602.35 MB/s | 0.0860 | 94.41 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 38.33% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.199651)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: text_json_medium

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 100.00 KB | 65.00 B | 1575.38x | 6.23 | 0.23 | 15.67 MB/s | 418.12 MB/s | 0.0810 | 94.42 | 65 | ❌ | 0.203007 | 0.142893 | ❌ | ✅ |
| SHA256 | 100.00 KB | 64.00 B | 1600.00x | 0.08 | 0.00 | 1252.66 MB/s | 0.00 MB/s | 0.0780 | 94.42 | - | - | - | - | - | - |
| AES-GCM | 100.00 KB | 100.02 KB | 1.00x | 0.18 | 0.09 | 552.70 MB/s | 1138.17 MB/s | 0.0793 | 94.42 | - | - | - | - | - | - |
| Frackture Encrypted | 100.00 KB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 100.00 KB | 1.93 KB | 51.90x | 0.23 | 0.11 | 424.43 MB/s | 908.19 MB/s | 0.0802 | 94.42 | - | - | - | - | - | - |
| Gzip L2 | 100.00 KB | 1.78 KB | 56.26x | 0.19 | 0.08 | 518.87 MB/s | 1150.11 MB/s | 0.0816 | 94.42 | - | - | - | - | - | - |
| Gzip L3 | 100.00 KB | 1.68 KB | 59.43x | 0.19 | 0.08 | 521.50 MB/s | 1224.81 MB/s | 0.0806 | 94.42 | - | - | - | - | - | - |
| Gzip L4 | 100.00 KB | 1.10 KB | 90.70x | 0.35 | 0.07 | 279.04 MB/s | 1323.22 MB/s | 0.0787 | 94.42 | - | - | - | - | - | - |
| Gzip L5 | 100.00 KB | 1.23 KB | 81.27x | 0.40 | 0.08 | 241.39 MB/s | 1210.98 MB/s | 0.0818 | 94.42 | - | - | - | - | - | - |
| Gzip L6 | 100.00 KB | 1004.00 B | 101.99x | 0.36 | 0.08 | 270.69 MB/s | 1277.57 MB/s | 0.0824 | 94.42 | - | - | - | - | - | - |
| Gzip L7 | 100.00 KB | 892.00 B | 114.80x | 0.48 | 0.07 | 202.11 MB/s | 1380.53 MB/s | 0.0802 | 94.42 | - | - | - | - | - | - |
| Gzip L8 | 100.00 KB | 892.00 B | 114.80x | 0.39 | 0.07 | 253.51 MB/s | 1389.87 MB/s | 0.0790 | 94.42 | - | - | - | - | - | - |
| Gzip L9 | 100.00 KB | 892.00 B | 114.80x | 0.49 | 0.07 | 200.07 MB/s | 1405.02 MB/s | 0.0835 | 94.42 | - | - | - | - | - | - |
| Brotli Q0 | 100.00 KB | 470.00 B | 217.87x | 0.06 | 0.11 | 1514.05 MB/s | 899.98 MB/s | 0.0887 | 94.42 | - | - | - | - | - | - |
| Brotli Q1 | 100.00 KB | 385.00 B | 265.97x | 0.09 | 0.10 | 1115.28 MB/s | 958.34 MB/s | 0.0786 | 94.42 | - | - | - | - | - | - |
| Brotli Q2 | 100.00 KB | 368.00 B | 278.26x | 0.20 | 0.13 | 486.28 MB/s | 743.00 MB/s | 0.0790 | 94.42 | - | - | - | - | - | - |
| Brotli Q3 | 100.00 KB | 359.00 B | 285.24x | 0.13 | 0.10 | 732.52 MB/s | 987.51 MB/s | 0.0789 | 94.42 | - | - | - | - | - | - |
| Brotli Q4 | 100.00 KB | 338.00 B | 302.96x | 0.16 | 0.10 | 602.88 MB/s | 989.40 MB/s | 0.0827 | 94.42 | - | - | - | - | - | - |
| Brotli Q5 | 100.00 KB | 317.00 B | 323.03x | 0.15 | 0.10 | 631.78 MB/s | 984.85 MB/s | 0.0809 | 94.42 | - | - | - | - | - | - |
| Brotli Q6 | 100.00 KB | 317.00 B | 323.03x | 0.14 | 0.10 | 700.91 MB/s | 1010.11 MB/s | 0.0821 | 94.42 | - | - | - | - | - | - |
| Brotli Q7 | 100.00 KB | 320.00 B | 320.00x | 0.17 | 0.10 | 564.46 MB/s | 1003.32 MB/s | 0.0818 | 94.48 | - | - | - | - | - | - |
| Brotli Q8 | 100.00 KB | 320.00 B | 320.00x | 0.26 | 0.13 | 375.91 MB/s | 751.43 MB/s | 0.0810 | 94.71 | - | - | - | - | - | - |
| Brotli Q9 | 100.00 KB | 315.00 B | 325.08x | 0.80 | 0.11 | 121.88 MB/s | 891.95 MB/s | 0.0817 | 94.71 | - | - | - | - | - | - |
| Brotli Q10 | 100.00 KB | 300.00 B | 341.33x | 5.96 | 0.18 | 16.37 MB/s | 534.72 MB/s | 0.0851 | 94.71 | - | - | - | - | - | - |
| Brotli Q11 | 100.00 KB | 293.00 B | 349.49x | 6.79 | 0.17 | 14.39 MB/s | 581.60 MB/s | 0.0928 | 94.71 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 29.61% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.203007)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: text_csv_medium

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 100.00 KB | 65.00 B | 1575.38x | 9.69 | 0.38 | 10.07 MB/s | 258.04 MB/s | 0.0819 | 94.72 | 65 | ❌ | 0.199575 | 0.188218 | ❌ | ✅ |
| SHA256 | 100.00 KB | 64.00 B | 1600.00x | 0.08 | 0.00 | 1287.56 MB/s | 0.00 MB/s | 0.0758 | 94.72 | - | - | - | - | - | - |
| AES-GCM | 100.00 KB | 100.02 KB | 1.00x | 0.17 | 0.08 | 579.71 MB/s | 1171.16 MB/s | 0.0814 | 94.72 | - | - | - | - | - | - |
| Frackture Encrypted | 100.00 KB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 100.00 KB | 966.00 B | 106.00x | 0.25 | 0.10 | 384.89 MB/s | 999.54 MB/s | 0.0795 | 94.72 | - | - | - | - | - | - |
| Gzip L2 | 100.00 KB | 958.00 B | 106.89x | 0.16 | 0.07 | 620.26 MB/s | 1378.68 MB/s | 0.0859 | 94.72 | - | - | - | - | - | - |
| Gzip L3 | 100.00 KB | 938.00 B | 109.17x | 0.21 | 0.11 | 454.36 MB/s | 895.11 MB/s | 0.0827 | 94.72 | - | - | - | - | - | - |
| Gzip L4 | 100.00 KB | 607.00 B | 168.70x | 0.33 | 0.07 | 293.23 MB/s | 1373.16 MB/s | 0.0805 | 94.72 | - | - | - | - | - | - |
| Gzip L5 | 100.00 KB | 607.00 B | 168.70x | 0.34 | 0.07 | 285.27 MB/s | 1390.34 MB/s | 0.0788 | 94.72 | - | - | - | - | - | - |
| Gzip L6 | 100.00 KB | 607.00 B | 168.70x | 0.33 | 0.07 | 293.08 MB/s | 1473.68 MB/s | 0.0815 | 94.72 | - | - | - | - | - | - |
| Gzip L7 | 100.00 KB | 607.00 B | 168.70x | 0.31 | 0.07 | 311.21 MB/s | 1479.30 MB/s | 0.0800 | 94.72 | - | - | - | - | - | - |
| Gzip L8 | 100.00 KB | 607.00 B | 168.70x | 0.42 | 0.10 | 234.43 MB/s | 966.18 MB/s | 0.0831 | 94.72 | - | - | - | - | - | - |
| Gzip L9 | 100.00 KB | 607.00 B | 168.70x | 0.74 | 0.11 | 132.64 MB/s | 857.18 MB/s | 0.0872 | 94.72 | - | - | - | - | - | - |
| Brotli Q0 | 100.00 KB | 257.00 B | 398.44x | 0.08 | 0.18 | 1238.73 MB/s | 537.07 MB/s | 0.0837 | 94.72 | - | - | - | - | - | - |
| Brotli Q1 | 100.00 KB | 192.00 B | 533.33x | 0.10 | 0.16 | 1006.02 MB/s | 627.89 MB/s | 0.0866 | 94.72 | - | - | - | - | - | - |
| Brotli Q2 | 100.00 KB | 188.00 B | 544.68x | 0.17 | 0.15 | 576.08 MB/s | 639.97 MB/s | 0.0847 | 94.72 | - | - | - | - | - | - |
| Brotli Q3 | 100.00 KB | 171.00 B | 598.83x | 0.12 | 0.17 | 783.70 MB/s | 564.45 MB/s | 0.0832 | 94.72 | - | - | - | - | - | - |
| Brotli Q4 | 100.00 KB | 164.00 B | 624.39x | 0.18 | 0.16 | 529.44 MB/s | 622.65 MB/s | 0.0870 | 94.72 | - | - | - | - | - | - |
| Brotli Q5 | 100.00 KB | 158.00 B | 648.10x | 0.17 | 0.15 | 581.97 MB/s | 634.79 MB/s | 0.0840 | 94.72 | - | - | - | - | - | - |
| Brotli Q6 | 100.00 KB | 158.00 B | 648.10x | 0.15 | 0.19 | 634.15 MB/s | 509.08 MB/s | 0.0867 | 94.72 | - | - | - | - | - | - |
| Brotli Q7 | 100.00 KB | 160.00 B | 640.00x | 0.20 | 0.18 | 487.72 MB/s | 539.13 MB/s | 0.0856 | 94.73 | - | - | - | - | - | - |
| Brotli Q8 | 100.00 KB | 160.00 B | 640.00x | 0.16 | 0.10 | 593.24 MB/s | 961.13 MB/s | 0.0826 | 94.83 | - | - | - | - | - | - |
| Brotli Q9 | 100.00 KB | 160.00 B | 640.00x | 0.45 | 0.10 | 217.96 MB/s | 966.52 MB/s | 0.0805 | 94.83 | - | - | - | - | - | - |
| Brotli Q10 | 100.00 KB | 150.00 B | 682.67x | 3.83 | 0.11 | 25.46 MB/s | 912.20 MB/s | 0.0784 | 94.84 | - | - | - | - | - | - |
| Brotli Q11 | 100.00 KB | 151.00 B | 678.15x | 4.86 | 0.11 | 20.11 MB/s | 901.54 MB/s | 0.0815 | 94.84 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 5.69% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.199575)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: binary_png_large

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 1.00 MB | 65.00 B | 16131.94x | 6.12 | 0.24 | 163.30 MB/s | 4198.82 MB/s | 0.7816 | 94.88 | 65 | ❌ | 0.126382 | 0.120252 | ❌ | ✅ |
| SHA256 | 1.00 MB | 64.00 B | 16384.00x | 0.79 | 0.00 | 1269.80 MB/s | 0.00 MB/s | 0.7875 | 94.88 | - | - | - | - | - | - |
| AES-GCM | 1.00 MB | 1.00 MB | 1.00x | 0.46 | 0.47 | 2170.81 MB/s | 2137.46 MB/s | 0.7814 | 94.88 | - | - | - | - | - | - |
| Frackture Encrypted | 1.00 MB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 1.00 MB | 7.30 KB | 140.18x | 1.74 | 0.47 | 574.99 MB/s | 2135.96 MB/s | 0.7968 | 94.88 | - | - | - | - | - | - |
| Gzip L2 | 1.00 MB | 6.57 KB | 155.85x | 1.76 | 0.48 | 567.89 MB/s | 2100.61 MB/s | 0.7876 | 94.88 | - | - | - | - | - | - |
| Gzip L3 | 1.00 MB | 6.57 KB | 155.85x | 1.94 | 0.43 | 515.34 MB/s | 2304.59 MB/s | 0.8204 | 94.88 | - | - | - | - | - | - |
| Gzip L4 | 1.00 MB | 3.59 KB | 285.56x | 3.69 | 0.50 | 270.90 MB/s | 1981.36 MB/s | 0.8251 | 94.88 | - | - | - | - | - | - |
| Gzip L5 | 1.00 MB | 3.59 KB | 285.56x | 3.84 | 0.90 | 260.48 MB/s | 1116.60 MB/s | 0.7971 | 94.88 | - | - | - | - | - | - |
| Gzip L6 | 1.00 MB | 3.59 KB | 285.56x | 3.60 | 0.54 | 278.08 MB/s | 1859.15 MB/s | 0.7773 | 94.88 | - | - | - | - | - | - |
| Gzip L7 | 1.00 MB | 3.59 KB | 285.56x | 3.43 | 0.55 | 291.41 MB/s | 1814.17 MB/s | 0.7803 | 94.88 | - | - | - | - | - | - |
| Gzip L8 | 1.00 MB | 3.59 KB | 285.56x | 3.64 | 0.60 | 274.63 MB/s | 1660.80 MB/s | 0.7939 | 94.88 | - | - | - | - | - | - |
| Gzip L9 | 1.00 MB | 3.59 KB | 285.56x | 3.58 | 0.56 | 279.44 MB/s | 1786.17 MB/s | 0.7717 | 94.88 | - | - | - | - | - | - |
| Brotli Q0 | 1.00 MB | 404.00 B | 2595.49x | 0.17 | 0.36 | 6054.73 MB/s | 2764.55 MB/s | 0.8320 | 94.88 | - | - | - | - | - | - |
| Brotli Q1 | 1.00 MB | 540.00 B | 1941.81x | 0.19 | 0.83 | 5365.61 MB/s | 1201.94 MB/s | 0.8203 | 94.88 | - | - | - | - | - | - |
| Brotli Q2 | 1.00 MB | 110.00 B | 9532.51x | 1.17 | 1.11 | 852.91 MB/s | 901.72 MB/s | 0.8252 | 94.88 | - | - | - | - | - | - |
| Brotli Q3 | 1.00 MB | 82.00 B | 12787.51x | 0.96 | 1.01 | 1040.66 MB/s | 994.46 MB/s | 0.7966 | 94.88 | - | - | - | - | - | - |
| Brotli Q4 | 1.00 MB | 81.00 B | 12945.38x | 1.29 | 1.00 | 776.08 MB/s | 996.13 MB/s | 0.7853 | 94.88 | - | - | - | - | - | - |
| Brotli Q5 | 1.00 MB | 136.00 B | 7710.12x | 0.99 | 0.97 | 1008.25 MB/s | 1032.20 MB/s | 0.8016 | 94.88 | - | - | - | - | - | - |
| Brotli Q6 | 1.00 MB | 136.00 B | 7710.12x | 0.98 | 1.01 | 1015.40 MB/s | 990.84 MB/s | 0.7843 | 94.89 | - | - | - | - | - | - |
| Brotli Q7 | 1.00 MB | 141.00 B | 7436.71x | 1.55 | 1.95 | 644.82 MB/s | 513.24 MB/s | 0.7938 | 94.95 | - | - | - | - | - | - |
| Brotli Q8 | 1.00 MB | 141.00 B | 7436.71x | 1.21 | 1.09 | 826.78 MB/s | 914.49 MB/s | 0.8036 | 95.02 | - | - | - | - | - | - |
| Brotli Q9 | 1.00 MB | 140.00 B | 7489.83x | 1.07 | 1.06 | 936.63 MB/s | 943.95 MB/s | 0.7913 | 95.02 | - | - | - | - | - | - |
| Brotli Q10 | 1.00 MB | 84.00 B | 12483.05x | 15.06 | 1.16 | 66.38 MB/s | 862.80 MB/s | 0.8242 | 95.58 | - | - | - | - | - | - |
| Brotli Q11 | 1.00 MB | 84.00 B | 12483.05x | 19.34 | 0.96 | 51.70 MB/s | 1044.34 MB/s | 0.7782 | 98.95 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 4.85% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.126382)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: binary_jpeg_large

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 1.00 MB | 65.00 B | 16131.94x | 5.86 | 0.23 | 170.58 MB/s | 4313.21 MB/s | 0.7753 | 98.95 | 65 | ❌ | 0.129295 | 0.122793 | ❌ | ✅ |
| SHA256 | 1.00 MB | 64.00 B | 16384.00x | 0.77 | 0.00 | 1301.34 MB/s | 0.00 MB/s | 0.7684 | 98.95 | - | - | - | - | - | - |
| AES-GCM | 1.00 MB | 1.00 MB | 1.00x | 0.48 | 0.48 | 2080.68 MB/s | 2063.34 MB/s | 0.7766 | 98.95 | - | - | - | - | - | - |
| Frackture Encrypted | 1.00 MB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 1.00 MB | 7.83 KB | 130.83x | 1.78 | 0.47 | 560.33 MB/s | 2125.10 MB/s | 0.7738 | 98.95 | - | - | - | - | - | - |
| Gzip L2 | 1.00 MB | 6.63 KB | 154.36x | 1.66 | 0.44 | 601.63 MB/s | 2294.43 MB/s | 0.7752 | 98.95 | - | - | - | - | - | - |
| Gzip L3 | 1.00 MB | 6.63 KB | 154.36x | 1.66 | 0.43 | 603.08 MB/s | 2326.59 MB/s | 0.7806 | 98.95 | - | - | - | - | - | - |
| Gzip L4 | 1.00 MB | 4.13 KB | 247.77x | 3.53 | 0.44 | 283.26 MB/s | 2295.50 MB/s | 0.7904 | 98.95 | - | - | - | - | - | - |
| Gzip L5 | 1.00 MB | 4.13 KB | 247.77x | 3.40 | 0.49 | 294.18 MB/s | 2031.01 MB/s | 0.7979 | 98.95 | - | - | - | - | - | - |
| Gzip L6 | 1.00 MB | 4.13 KB | 247.77x | 4.03 | 0.50 | 247.98 MB/s | 2017.04 MB/s | 0.7789 | 98.95 | - | - | - | - | - | - |
| Gzip L7 | 1.00 MB | 4.13 KB | 247.77x | 3.68 | 0.47 | 271.73 MB/s | 2126.39 MB/s | 0.7913 | 98.95 | - | - | - | - | - | - |
| Gzip L8 | 1.00 MB | 4.13 KB | 247.77x | 3.44 | 0.64 | 290.69 MB/s | 1560.38 MB/s | 0.7704 | 98.95 | - | - | - | - | - | - |
| Gzip L9 | 1.00 MB | 4.13 KB | 247.77x | 3.43 | 0.47 | 291.35 MB/s | 2123.90 MB/s | 0.7711 | 98.95 | - | - | - | - | - | - |
| Brotli Q0 | 1.00 MB | 466.00 B | 2250.16x | 0.20 | 0.48 | 4893.21 MB/s | 2088.84 MB/s | 0.7726 | 98.95 | - | - | - | - | - | - |
| Brotli Q1 | 1.00 MB | 505.00 B | 2076.39x | 0.18 | 0.74 | 5414.68 MB/s | 1355.40 MB/s | 0.7750 | 98.95 | - | - | - | - | - | - |
| Brotli Q2 | 1.00 MB | 158.00 B | 6636.56x | 0.97 | 1.02 | 1029.00 MB/s | 977.97 MB/s | 0.7813 | 98.95 | - | - | - | - | - | - |
| Brotli Q3 | 1.00 MB | 132.00 B | 7943.76x | 0.91 | 1.03 | 1101.72 MB/s | 973.69 MB/s | 0.7726 | 98.95 | - | - | - | - | - | - |
| Brotli Q4 | 1.00 MB | 121.00 B | 8665.92x | 1.32 | 1.03 | 757.36 MB/s | 974.08 MB/s | 0.7735 | 98.95 | - | - | - | - | - | - |
| Brotli Q5 | 1.00 MB | 171.00 B | 6132.02x | 0.96 | 1.00 | 1039.65 MB/s | 997.81 MB/s | 0.7738 | 98.95 | - | - | - | - | - | - |
| Brotli Q6 | 1.00 MB | 171.00 B | 6132.02x | 0.95 | 0.99 | 1048.52 MB/s | 1011.78 MB/s | 0.7741 | 98.95 | - | - | - | - | - | - |
| Brotli Q7 | 1.00 MB | 178.00 B | 5890.88x | 0.98 | 1.00 | 1024.72 MB/s | 997.91 MB/s | 0.7782 | 98.96 | - | - | - | - | - | - |
| Brotli Q8 | 1.00 MB | 178.00 B | 5890.88x | 1.03 | 0.96 | 970.02 MB/s | 1038.57 MB/s | 0.7733 | 99.01 | - | - | - | - | - | - |
| Brotli Q9 | 1.00 MB | 178.00 B | 5890.88x | 1.17 | 1.12 | 854.04 MB/s | 895.08 MB/s | 0.7785 | 99.01 | - | - | - | - | - | - |
| Brotli Q10 | 1.00 MB | 132.00 B | 7943.76x | 13.64 | 1.11 | 73.30 MB/s | 901.39 MB/s | 0.7811 | 99.01 | - | - | - | - | - | - |
| Brotli Q11 | 1.00 MB | 132.00 B | 7943.76x | 15.93 | 0.95 | 62.78 MB/s | 1047.60 MB/s | 0.7885 | 99.14 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 5.03% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.129295)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: binary_pdf_large

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 1.00 MB | 65.00 B | 16131.94x | 6.30 | 0.36 | 158.74 MB/s | 2790.00 MB/s | 0.7734 | 99.15 | 65 | ❌ | 0.159119 | 0.149942 | ❌ | ✅ |
| SHA256 | 1.00 MB | 64.00 B | 16384.00x | 0.76 | 0.00 | 1311.09 MB/s | 0.00 MB/s | 0.7627 | 99.15 | - | - | - | - | - | - |
| AES-GCM | 1.00 MB | 1.00 MB | 1.00x | 0.50 | 0.40 | 1988.80 MB/s | 2518.81 MB/s | 0.7768 | 99.15 | - | - | - | - | - | - |
| Frackture Encrypted | 1.00 MB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 1.00 MB | 12.81 KB | 79.96x | 1.90 | 0.57 | 527.23 MB/s | 1746.95 MB/s | 0.7701 | 99.15 | - | - | - | - | - | - |
| Gzip L2 | 1.00 MB | 12.50 KB | 81.89x | 1.94 | 0.53 | 516.42 MB/s | 1896.56 MB/s | 0.7795 | 99.15 | - | - | - | - | - | - |
| Gzip L3 | 1.00 MB | 9.77 KB | 104.82x | 1.84 | 0.49 | 544.05 MB/s | 2035.91 MB/s | 0.7738 | 99.15 | - | - | - | - | - | - |
| Gzip L4 | 1.00 MB | 6.04 KB | 169.40x | 3.49 | 0.45 | 286.46 MB/s | 2207.35 MB/s | 0.7765 | 99.15 | - | - | - | - | - | - |
| Gzip L5 | 1.00 MB | 5.02 KB | 204.04x | 3.61 | 0.44 | 276.80 MB/s | 2274.61 MB/s | 0.7767 | 99.15 | - | - | - | - | - | - |
| Gzip L6 | 1.00 MB | 4.77 KB | 214.56x | 3.62 | 0.44 | 276.03 MB/s | 2278.28 MB/s | 0.7752 | 99.15 | - | - | - | - | - | - |
| Gzip L7 | 1.00 MB | 4.77 KB | 214.56x | 3.58 | 0.49 | 279.47 MB/s | 2039.80 MB/s | 0.7737 | 99.15 | - | - | - | - | - | - |
| Gzip L8 | 1.00 MB | 4.77 KB | 214.56x | 3.72 | 0.49 | 269.08 MB/s | 2022.13 MB/s | 0.7930 | 99.15 | - | - | - | - | - | - |
| Gzip L9 | 1.00 MB | 4.77 KB | 214.56x | 3.50 | 0.46 | 285.42 MB/s | 2186.95 MB/s | 0.7892 | 99.15 | - | - | - | - | - | - |
| Brotli Q0 | 1.00 MB | 1.01 KB | 1009.22x | 0.54 | 0.38 | 1845.11 MB/s | 2617.54 MB/s | 0.7731 | 99.15 | - | - | - | - | - | - |
| Brotli Q1 | 1.00 MB | 1021.00 B | 1027.01x | 0.18 | 0.91 | 5506.24 MB/s | 1102.26 MB/s | 0.7765 | 99.15 | - | - | - | - | - | - |
| Brotli Q2 | 1.00 MB | 281.00 B | 3731.59x | 0.92 | 1.02 | 1081.76 MB/s | 983.50 MB/s | 0.7718 | 99.15 | - | - | - | - | - | - |
| Brotli Q3 | 1.00 MB | 272.00 B | 3855.06x | 0.91 | 1.00 | 1099.43 MB/s | 1004.87 MB/s | 0.7762 | 99.15 | - | - | - | - | - | - |
| Brotli Q4 | 1.00 MB | 270.00 B | 3883.61x | 1.30 | 0.97 | 769.65 MB/s | 1026.23 MB/s | 0.7728 | 99.16 | - | - | - | - | - | - |
| Brotli Q5 | 1.00 MB | 308.00 B | 3404.47x | 1.03 | 1.01 | 969.97 MB/s | 989.14 MB/s | 0.7732 | 99.16 | - | - | - | - | - | - |
| Brotli Q6 | 1.00 MB | 308.00 B | 3404.47x | 1.12 | 0.97 | 892.77 MB/s | 1029.90 MB/s | 0.7747 | 99.16 | - | - | - | - | - | - |
| Brotli Q7 | 1.00 MB | 309.00 B | 3393.45x | 1.03 | 1.01 | 967.77 MB/s | 992.66 MB/s | 0.7747 | 99.18 | - | - | - | - | - | - |
| Brotli Q8 | 1.00 MB | 309.00 B | 3393.45x | 1.04 | 0.97 | 964.69 MB/s | 1030.42 MB/s | 0.7759 | 99.22 | - | - | - | - | - | - |
| Brotli Q9 | 1.00 MB | 309.00 B | 3393.45x | 1.66 | 0.98 | 602.19 MB/s | 1015.63 MB/s | 0.7857 | 99.22 | - | - | - | - | - | - |
| Brotli Q10 | 1.00 MB | 229.00 B | 4578.93x | 12.63 | 0.99 | 79.17 MB/s | 1013.27 MB/s | 0.7789 | 99.23 | - | - | - | - | - | - |
| Brotli Q11 | 1.00 MB | 232.00 B | 4519.72x | 16.42 | 1.08 | 60.91 MB/s | 924.51 MB/s | 0.7746 | 99.23 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 5.77% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.159119)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: binary_gif_large

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 1.00 MB | 65.00 B | 16131.94x | 6.12 | 0.25 | 163.28 MB/s | 4005.86 MB/s | 0.7903 | 99.24 | 65 | ❌ | 0.136235 | 0.136235 | ❌ | ✅ |
| SHA256 | 1.00 MB | 64.00 B | 16384.00x | 0.77 | 0.00 | 1294.19 MB/s | 0.00 MB/s | 0.7727 | 99.24 | - | - | - | - | - | - |
| AES-GCM | 1.00 MB | 1.00 MB | 1.00x | 0.50 | 0.41 | 1988.04 MB/s | 2430.04 MB/s | 0.7773 | 99.24 | - | - | - | - | - | - |
| Frackture Encrypted | 1.00 MB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 1.00 MB | 4.54 KB | 225.60x | 1.72 | 0.58 | 580.96 MB/s | 1714.94 MB/s | 0.7855 | 99.24 | - | - | - | - | - | - |
| Gzip L2 | 1.00 MB | 4.54 KB | 225.60x | 1.63 | 0.54 | 612.66 MB/s | 1850.30 MB/s | 0.7878 | 99.24 | - | - | - | - | - | - |
| Gzip L3 | 1.00 MB | 4.54 KB | 225.60x | 1.74 | 0.43 | 573.52 MB/s | 2334.64 MB/s | 0.7757 | 99.24 | - | - | - | - | - | - |
| Gzip L4 | 1.00 MB | 3.05 KB | 335.76x | 3.36 | 0.72 | 297.23 MB/s | 1389.41 MB/s | 0.7913 | 99.24 | - | - | - | - | - | - |
| Gzip L5 | 1.00 MB | 3.05 KB | 335.76x | 4.08 | 0.85 | 245.16 MB/s | 1177.52 MB/s | 0.7765 | 99.24 | - | - | - | - | - | - |
| Gzip L6 | 1.00 MB | 3.05 KB | 335.76x | 3.81 | 0.82 | 262.52 MB/s | 1214.06 MB/s | 0.7712 | 99.24 | - | - | - | - | - | - |
| Gzip L7 | 1.00 MB | 3.05 KB | 335.76x | 3.44 | 0.76 | 291.11 MB/s | 1323.77 MB/s | 0.7759 | 99.24 | - | - | - | - | - | - |
| Gzip L8 | 1.00 MB | 3.05 KB | 335.76x | 3.45 | 0.73 | 289.89 MB/s | 1367.12 MB/s | 0.7806 | 99.24 | - | - | - | - | - | - |
| Gzip L9 | 1.00 MB | 3.05 KB | 335.76x | 3.40 | 0.68 | 293.70 MB/s | 1480.39 MB/s | 0.7858 | 99.24 | - | - | - | - | - | - |
| Brotli Q0 | 1.00 MB | 1.03 KB | 992.97x | 0.33 | 0.73 | 3035.38 MB/s | 1374.49 MB/s | 0.7713 | 99.24 | - | - | - | - | - | - |
| Brotli Q1 | 1.00 MB | 320.00 B | 3276.80x | 0.18 | 0.87 | 5588.37 MB/s | 1152.49 MB/s | 0.7907 | 99.24 | - | - | - | - | - | - |
| Brotli Q2 | 1.00 MB | 66.00 B | 15887.52x | 0.98 | 1.00 | 1017.80 MB/s | 997.82 MB/s | 0.7767 | 99.24 | - | - | - | - | - | - |
| Brotli Q3 | 1.00 MB | 47.00 B | 22310.13x | 0.93 | 1.12 | 1079.53 MB/s | 890.19 MB/s | 0.7764 | 99.24 | - | - | - | - | - | - |
| Brotli Q4 | 1.00 MB | 47.00 B | 22310.13x | 1.29 | 0.96 | 777.13 MB/s | 1041.54 MB/s | 0.7778 | 99.24 | - | - | - | - | - | - |
| Brotli Q5 | 1.00 MB | 99.00 B | 10591.68x | 0.95 | 0.96 | 1054.82 MB/s | 1038.03 MB/s | 0.7735 | 99.24 | - | - | - | - | - | - |
| Brotli Q6 | 1.00 MB | 99.00 B | 10591.68x | 0.97 | 0.96 | 1036.23 MB/s | 1037.55 MB/s | 0.8125 | 99.24 | - | - | - | - | - | - |
| Brotli Q7 | 1.00 MB | 99.00 B | 10591.68x | 0.96 | 1.04 | 1042.20 MB/s | 963.50 MB/s | 0.7734 | 99.25 | - | - | - | - | - | - |
| Brotli Q8 | 1.00 MB | 99.00 B | 10591.68x | 0.94 | 1.17 | 1064.31 MB/s | 856.17 MB/s | 0.7969 | 99.26 | - | - | - | - | - | - |
| Brotli Q9 | 1.00 MB | 99.00 B | 10591.68x | 0.98 | 0.97 | 1018.61 MB/s | 1033.49 MB/s | 0.8211 | 99.26 | - | - | - | - | - | - |
| Brotli Q10 | 1.00 MB | 51.00 B | 20560.31x | 14.99 | 0.98 | 66.72 MB/s | 1016.39 MB/s | 0.7729 | 99.45 | - | - | - | - | - | - |
| Brotli Q11 | 1.00 MB | 51.00 B | 20560.31x | 17.49 | 0.98 | 57.17 MB/s | 1017.54 MB/s | 0.7804 | 99.46 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 0.00% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.136235)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: code_javascript_large

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 1.00 MB | 65.00 B | 16131.94x | 6.05 | 0.23 | 165.25 MB/s | 4261.47 MB/s | 0.7930 | 99.47 | 65 | ❌ | 0.210678 | 0.176264 | ❌ | ✅ |
| SHA256 | 1.00 MB | 64.00 B | 16384.00x | 0.78 | 0.00 | 1285.73 MB/s | 0.00 MB/s | 0.7778 | 99.47 | - | - | - | - | - | - |
| AES-GCM | 1.00 MB | 1.00 MB | 1.00x | 0.53 | 0.49 | 1898.01 MB/s | 2054.65 MB/s | 0.8044 | 99.47 | - | - | - | - | - | - |
| Frackture Encrypted | 1.00 MB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 1.00 MB | 9.47 KB | 108.09x | 1.81 | 0.55 | 553.86 MB/s | 1827.60 MB/s | 0.7769 | 99.47 | - | - | - | - | - | - |
| Gzip L2 | 1.00 MB | 11.69 KB | 87.56x | 2.05 | 0.53 | 488.12 MB/s | 1885.17 MB/s | 0.7789 | 99.47 | - | - | - | - | - | - |
| Gzip L3 | 1.00 MB | 12.10 KB | 84.62x | 2.12 | 0.56 | 471.47 MB/s | 1770.94 MB/s | 0.7846 | 99.47 | - | - | - | - | - | - |
| Gzip L4 | 1.00 MB | 6.05 KB | 169.15x | 3.70 | 0.47 | 270.53 MB/s | 2146.74 MB/s | 0.7893 | 99.47 | - | - | - | - | - | - |
| Gzip L5 | 1.00 MB | 6.05 KB | 169.32x | 3.72 | 0.47 | 268.51 MB/s | 2126.46 MB/s | 0.7778 | 99.47 | - | - | - | - | - | - |
| Gzip L6 | 1.00 MB | 5.29 KB | 193.68x | 3.77 | 0.46 | 265.55 MB/s | 2151.83 MB/s | 0.7847 | 99.47 | - | - | - | - | - | - |
| Gzip L7 | 1.00 MB | 5.29 KB | 193.68x | 3.69 | 0.48 | 271.14 MB/s | 2095.00 MB/s | 0.7883 | 99.47 | - | - | - | - | - | - |
| Gzip L8 | 1.00 MB | 5.29 KB | 193.68x | 3.75 | 0.48 | 266.37 MB/s | 2096.39 MB/s | 0.7755 | 99.47 | - | - | - | - | - | - |
| Gzip L9 | 1.00 MB | 5.29 KB | 193.68x | 3.56 | 0.51 | 280.64 MB/s | 1954.67 MB/s | 0.7782 | 99.47 | - | - | - | - | - | - |
| Brotli Q0 | 1.00 MB | 1.17 KB | 876.74x | 0.45 | 0.48 | 2242.56 MB/s | 2076.36 MB/s | 0.7888 | 99.47 | - | - | - | - | - | - |
| Brotli Q1 | 1.00 MB | 974.00 B | 1076.57x | 0.18 | 0.88 | 5564.80 MB/s | 1135.14 MB/s | 0.7878 | 99.47 | - | - | - | - | - | - |
| Brotli Q2 | 1.00 MB | 310.00 B | 3382.50x | 0.92 | 0.96 | 1081.95 MB/s | 1042.07 MB/s | 0.7697 | 99.47 | - | - | - | - | - | - |
| Brotli Q3 | 1.00 MB | 296.00 B | 3542.49x | 0.99 | 1.00 | 1011.86 MB/s | 1001.68 MB/s | 0.7755 | 99.47 | - | - | - | - | - | - |
| Brotli Q4 | 1.00 MB | 304.00 B | 3449.26x | 1.45 | 0.97 | 687.84 MB/s | 1026.30 MB/s | 0.7812 | 99.47 | - | - | - | - | - | - |
| Brotli Q5 | 1.00 MB | 310.00 B | 3382.50x | 1.03 | 1.09 | 974.96 MB/s | 919.12 MB/s | 0.7819 | 99.47 | - | - | - | - | - | - |
| Brotli Q6 | 1.00 MB | 309.00 B | 3393.45x | 1.03 | 0.97 | 973.04 MB/s | 1028.63 MB/s | 0.7925 | 99.47 | - | - | - | - | - | - |
| Brotli Q7 | 1.00 MB | 311.00 B | 3371.63x | 1.07 | 1.00 | 938.16 MB/s | 996.83 MB/s | 0.7883 | 99.50 | - | - | - | - | - | - |
| Brotli Q8 | 1.00 MB | 311.00 B | 3371.63x | 1.16 | 0.98 | 859.96 MB/s | 1022.02 MB/s | 0.7748 | 99.61 | - | - | - | - | - | - |
| Brotli Q9 | 1.00 MB | 311.00 B | 3371.63x | 1.60 | 1.01 | 626.29 MB/s | 988.51 MB/s | 0.7970 | 99.61 | - | - | - | - | - | - |
| Brotli Q10 | 1.00 MB | 243.00 B | 4315.13x | 13.85 | 1.00 | 72.20 MB/s | 998.21 MB/s | 0.7792 | 99.62 | - | - | - | - | - | - |
| Brotli Q11 | 1.00 MB | 236.00 B | 4443.12x | 16.26 | 0.99 | 61.51 MB/s | 1012.30 MB/s | 0.7880 | 99.62 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 16.33% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.210678)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: code_javascript_minified_large

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 1.00 MB | 65.00 B | 16131.94x | 6.35 | 0.25 | 157.39 MB/s | 4035.58 MB/s | 0.7805 | 99.63 | 65 | ❌ | 0.248601 | 0.216233 | ❌ | ✅ |
| SHA256 | 1.00 MB | 64.00 B | 16384.00x | 0.77 | 0.00 | 1302.64 MB/s | 0.00 MB/s | 0.7677 | 99.63 | - | - | - | - | - | - |
| AES-GCM | 1.00 MB | 1.00 MB | 1.00x | 0.54 | 0.40 | 1866.78 MB/s | 2481.78 MB/s | 0.7785 | 99.63 | - | - | - | - | - | - |
| Frackture Encrypted | 1.00 MB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 1.00 MB | 8.02 KB | 127.69x | 1.79 | 0.53 | 558.81 MB/s | 1884.76 MB/s | 0.7818 | 99.63 | - | - | - | - | - | - |
| Gzip L2 | 1.00 MB | 7.93 KB | 129.10x | 1.78 | 0.47 | 560.60 MB/s | 2113.71 MB/s | 0.7976 | 99.63 | - | - | - | - | - | - |
| Gzip L3 | 1.00 MB | 7.89 KB | 129.74x | 1.71 | 0.47 | 586.33 MB/s | 2107.99 MB/s | 0.7789 | 99.63 | - | - | - | - | - | - |
| Gzip L4 | 1.00 MB | 4.18 KB | 245.22x | 3.47 | 0.46 | 287.97 MB/s | 2179.34 MB/s | 0.7746 | 99.63 | - | - | - | - | - | - |
| Gzip L5 | 1.00 MB | 4.18 KB | 245.22x | 3.48 | 0.44 | 287.53 MB/s | 2270.77 MB/s | 0.7847 | 99.63 | - | - | - | - | - | - |
| Gzip L6 | 1.00 MB | 4.18 KB | 245.22x | 3.45 | 0.46 | 289.60 MB/s | 2171.54 MB/s | 0.7809 | 99.63 | - | - | - | - | - | - |
| Gzip L7 | 1.00 MB | 4.18 KB | 245.22x | 3.52 | 0.47 | 284.30 MB/s | 2137.09 MB/s | 0.7709 | 99.63 | - | - | - | - | - | - |
| Gzip L8 | 1.00 MB | 4.18 KB | 245.22x | 3.38 | 0.56 | 295.94 MB/s | 1794.19 MB/s | 0.7730 | 99.63 | - | - | - | - | - | - |
| Gzip L9 | 1.00 MB | 4.18 KB | 245.22x | 3.61 | 0.46 | 277.11 MB/s | 2167.50 MB/s | 0.7839 | 99.63 | - | - | - | - | - | - |
| Brotli Q0 | 1.00 MB | 600.00 B | 1747.63x | 0.22 | 0.35 | 4551.39 MB/s | 2841.63 MB/s | 0.7957 | 99.63 | - | - | - | - | - | - |
| Brotli Q1 | 1.00 MB | 670.00 B | 1565.04x | 0.19 | 0.78 | 5329.52 MB/s | 1282.50 MB/s | 0.7798 | 99.63 | - | - | - | - | - | - |
| Brotli Q2 | 1.00 MB | 190.00 B | 5518.82x | 0.99 | 0.98 | 1012.22 MB/s | 1025.56 MB/s | 0.7831 | 99.63 | - | - | - | - | - | - |
| Brotli Q3 | 1.00 MB | 177.00 B | 5924.16x | 0.94 | 0.97 | 1068.72 MB/s | 1028.05 MB/s | 0.7823 | 99.63 | - | - | - | - | - | - |
| Brotli Q4 | 1.00 MB | 180.00 B | 5825.42x | 1.36 | 0.97 | 737.19 MB/s | 1027.79 MB/s | 0.7769 | 99.63 | - | - | - | - | - | - |
| Brotli Q5 | 1.00 MB | 224.00 B | 4681.14x | 1.03 | 1.03 | 971.05 MB/s | 973.47 MB/s | 0.7773 | 99.63 | - | - | - | - | - | - |
| Brotli Q6 | 1.00 MB | 224.00 B | 4681.14x | 1.02 | 1.01 | 978.00 MB/s | 985.48 MB/s | 0.7865 | 99.63 | - | - | - | - | - | - |
| Brotli Q7 | 1.00 MB | 220.00 B | 4766.25x | 1.04 | 0.99 | 959.23 MB/s | 1010.57 MB/s | 0.7737 | 99.64 | - | - | - | - | - | - |
| Brotli Q8 | 1.00 MB | 220.00 B | 4766.25x | 1.06 | 0.96 | 946.58 MB/s | 1038.60 MB/s | 0.8943 | 99.71 | - | - | - | - | - | - |
| Brotli Q9 | 1.00 MB | 220.00 B | 4766.25x | 1.33 | 1.29 | 754.07 MB/s | 772.25 MB/s | 0.7835 | 99.71 | - | - | - | - | - | - |
| Brotli Q10 | 1.00 MB | 168.00 B | 6241.52x | 12.21 | 1.03 | 81.93 MB/s | 970.97 MB/s | 0.7751 | 99.71 | - | - | - | - | - | - |
| Brotli Q11 | 1.00 MB | 165.00 B | 6355.01x | 15.28 | 0.98 | 65.45 MB/s | 1016.91 MB/s | 0.7758 | 99.71 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 13.02% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.248601)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: code_python_large

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 1.00 MB | 65.00 B | 16131.94x | 5.99 | 0.23 | 166.99 MB/s | 4260.96 MB/s | 0.7797 | 99.71 | 65 | ❌ | 0.201540 | 0.173739 | ❌ | ✅ |
| SHA256 | 1.00 MB | 64.00 B | 16384.00x | 0.79 | 0.00 | 1271.24 MB/s | 0.00 MB/s | 0.7866 | 99.71 | - | - | - | - | - | - |
| AES-GCM | 1.00 MB | 1.00 MB | 1.00x | 0.52 | 0.49 | 1936.05 MB/s | 2034.07 MB/s | 0.7742 | 99.71 | - | - | - | - | - | - |
| Frackture Encrypted | 1.00 MB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 1.00 MB | 21.20 KB | 48.31x | 2.17 | 0.69 | 461.29 MB/s | 1439.92 MB/s | 0.7918 | 99.71 | - | - | - | - | - | - |
| Gzip L2 | 1.00 MB | 18.40 KB | 55.65x | 2.10 | 0.61 | 476.59 MB/s | 1646.84 MB/s | 0.7796 | 99.71 | - | - | - | - | - | - |
| Gzip L3 | 1.00 MB | 15.33 KB | 66.81x | 2.07 | 0.59 | 482.78 MB/s | 1695.19 MB/s | 0.7811 | 99.71 | - | - | - | - | - | - |
| Gzip L4 | 1.00 MB | 9.00 KB | 113.75x | 3.64 | 0.56 | 274.61 MB/s | 1796.38 MB/s | 0.7710 | 99.71 | - | - | - | - | - | - |
| Gzip L5 | 1.00 MB | 8.24 KB | 124.30x | 3.61 | 0.48 | 276.84 MB/s | 2084.41 MB/s | 0.7775 | 99.71 | - | - | - | - | - | - |
| Gzip L6 | 1.00 MB | 8.10 KB | 126.47x | 4.04 | 0.44 | 247.83 MB/s | 2262.84 MB/s | 0.7808 | 99.71 | - | - | - | - | - | - |
| Gzip L7 | 1.00 MB | 6.06 KB | 169.10x | 3.78 | 0.46 | 264.76 MB/s | 2174.31 MB/s | 0.7777 | 99.71 | - | - | - | - | - | - |
| Gzip L8 | 1.00 MB | 6.06 KB | 169.10x | 3.79 | 0.48 | 263.52 MB/s | 2104.53 MB/s | 0.7740 | 99.71 | - | - | - | - | - | - |
| Gzip L9 | 1.00 MB | 6.06 KB | 169.10x | 3.74 | 0.50 | 267.05 MB/s | 1993.06 MB/s | 0.7700 | 99.71 | - | - | - | - | - | - |
| Brotli Q0 | 1.00 MB | 1.89 KB | 543.02x | 0.94 | 0.60 | 1068.49 MB/s | 1677.93 MB/s | 0.7940 | 99.71 | - | - | - | - | - | - |
| Brotli Q1 | 1.00 MB | 1.78 KB | 575.19x | 0.28 | 0.78 | 3540.34 MB/s | 1282.26 MB/s | 0.7759 | 99.71 | - | - | - | - | - | - |
| Brotli Q2 | 1.00 MB | 589.00 B | 1780.26x | 0.90 | 1.00 | 1106.49 MB/s | 1002.56 MB/s | 0.7778 | 99.71 | - | - | - | - | - | - |
| Brotli Q3 | 1.00 MB | 560.00 B | 1872.46x | 0.94 | 0.97 | 1058.21 MB/s | 1026.42 MB/s | 0.7983 | 99.71 | - | - | - | - | - | - |
| Brotli Q4 | 1.00 MB | 574.00 B | 1826.79x | 1.40 | 0.96 | 712.61 MB/s | 1044.24 MB/s | 0.7868 | 99.71 | - | - | - | - | - | - |
| Brotli Q5 | 1.00 MB | 578.00 B | 1814.15x | 1.18 | 0.99 | 846.64 MB/s | 1010.13 MB/s | 0.7879 | 99.71 | - | - | - | - | - | - |
| Brotli Q6 | 1.00 MB | 575.00 B | 1823.61x | 1.21 | 1.08 | 828.54 MB/s | 927.85 MB/s | 0.7872 | 99.71 | - | - | - | - | - | - |
| Brotli Q7 | 1.00 MB | 576.00 B | 1820.44x | 1.14 | 1.08 | 880.21 MB/s | 926.63 MB/s | 0.7920 | 99.82 | - | - | - | - | - | - |
| Brotli Q8 | 1.00 MB | 576.00 B | 1820.44x | 1.23 | 1.01 | 811.31 MB/s | 994.12 MB/s | 0.8106 | 100.09 | - | - | - | - | - | - |
| Brotli Q9 | 1.00 MB | 576.00 B | 1820.44x | 2.85 | 1.45 | 350.53 MB/s | 688.60 MB/s | 0.8061 | 100.09 | - | - | - | - | - | - |
| Brotli Q10 | 1.00 MB | 484.00 B | 2166.48x | 18.59 | 1.35 | 53.80 MB/s | 738.38 MB/s | 0.8001 | 100.17 | - | - | - | - | - | - |
| Brotli Q11 | 1.00 MB | 491.00 B | 2135.59x | 21.72 | 1.56 | 46.05 MB/s | 641.32 MB/s | 0.7924 | 100.94 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 13.79% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.201540)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: mixed_payload_large

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 1.00 MB | 65.00 B | 16131.94x | 6.40 | 0.30 | 156.29 MB/s | 3350.78 MB/s | 0.7919 | 100.95 | 65 | ❌ | 0.067139 | 0.050524 | ❌ | ✅ |
| SHA256 | 1.00 MB | 64.00 B | 16384.00x | 0.79 | 0.00 | 1259.86 MB/s | 0.00 MB/s | 0.7937 | 100.95 | - | - | - | - | - | - |
| AES-GCM | 1.00 MB | 1.00 MB | 1.00x | 0.61 | 0.60 | 1637.01 MB/s | 1665.87 MB/s | 0.7987 | 100.95 | - | - | - | - | - | - |
| Frackture Encrypted | 1.00 MB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 1.00 MB | 26.07 KB | 39.28x | 2.45 | 0.76 | 408.16 MB/s | 1309.11 MB/s | 0.7903 | 100.95 | - | - | - | - | - | - |
| Gzip L2 | 1.00 MB | 16.11 KB | 63.55x | 2.02 | 0.62 | 495.61 MB/s | 1625.12 MB/s | 0.7798 | 100.95 | - | - | - | - | - | - |
| Gzip L3 | 1.00 MB | 18.29 KB | 55.98x | 2.06 | 0.60 | 484.91 MB/s | 1665.76 MB/s | 0.7788 | 100.95 | - | - | - | - | - | - |
| Gzip L4 | 1.00 MB | 7.42 KB | 138.04x | 3.76 | 0.51 | 266.15 MB/s | 1971.22 MB/s | 0.7692 | 100.95 | - | - | - | - | - | - |
| Gzip L5 | 1.00 MB | 7.00 KB | 146.39x | 4.09 | 0.47 | 244.25 MB/s | 2122.15 MB/s | 0.7757 | 100.95 | - | - | - | - | - | - |
| Gzip L6 | 1.00 MB | 6.63 KB | 154.52x | 3.58 | 0.46 | 279.30 MB/s | 2170.74 MB/s | 0.7789 | 100.95 | - | - | - | - | - | - |
| Gzip L7 | 1.00 MB | 6.63 KB | 154.52x | 3.62 | 0.49 | 275.95 MB/s | 2031.57 MB/s | 0.7787 | 100.95 | - | - | - | - | - | - |
| Gzip L8 | 1.00 MB | 6.63 KB | 154.52x | 3.60 | 0.45 | 278.08 MB/s | 2207.84 MB/s | 0.7836 | 100.95 | - | - | - | - | - | - |
| Gzip L9 | 1.00 MB | 6.63 KB | 154.52x | 3.62 | 0.45 | 276.29 MB/s | 2219.88 MB/s | 0.7843 | 100.95 | - | - | - | - | - | - |
| Brotli Q0 | 1.00 MB | 2.72 KB | 376.91x | 0.53 | 0.37 | 1901.55 MB/s | 2725.92 MB/s | 0.7749 | 100.95 | - | - | - | - | - | - |
| Brotli Q1 | 1.00 MB | 2.57 KB | 397.79x | 0.23 | 0.72 | 4334.43 MB/s | 1380.72 MB/s | 0.7816 | 100.95 | - | - | - | - | - | - |
| Brotli Q2 | 1.00 MB | 1.11 KB | 923.04x | 1.03 | 0.98 | 968.44 MB/s | 1016.82 MB/s | 0.7801 | 100.95 | - | - | - | - | - | - |
| Brotli Q3 | 1.00 MB | 1.09 KB | 939.58x | 0.99 | 0.97 | 1014.07 MB/s | 1029.89 MB/s | 0.7787 | 100.95 | - | - | - | - | - | - |
| Brotli Q4 | 1.00 MB | 1.13 KB | 904.72x | 1.44 | 0.98 | 692.18 MB/s | 1023.61 MB/s | 0.7765 | 100.95 | - | - | - | - | - | - |
| Brotli Q5 | 1.00 MB | 1.01 KB | 1011.16x | 1.21 | 1.13 | 825.48 MB/s | 881.27 MB/s | 0.7779 | 100.95 | - | - | - | - | - | - |
| Brotli Q6 | 1.00 MB | 1.01 KB | 1009.22x | 1.21 | 1.04 | 823.08 MB/s | 959.18 MB/s | 0.7701 | 100.95 | - | - | - | - | - | - |
| Brotli Q7 | 1.00 MB | 1.02 KB | 1007.28x | 1.29 | 1.02 | 777.32 MB/s | 981.68 MB/s | 0.7725 | 100.95 | - | - | - | - | - | - |
| Brotli Q8 | 1.00 MB | 1.02 KB | 1007.28x | 1.27 | 1.01 | 788.90 MB/s | 992.25 MB/s | 0.7773 | 101.04 | - | - | - | - | - | - |
| Brotli Q9 | 1.00 MB | 1.02 KB | 1007.28x | 3.55 | 1.04 | 281.45 MB/s | 957.08 MB/s | 0.7792 | 101.04 | - | - | - | - | - | - |
| Brotli Q10 | 1.00 MB | 912.00 B | 1149.75x | 15.09 | 1.01 | 66.28 MB/s | 987.10 MB/s | 0.7852 | 101.04 | - | - | - | - | - | - |
| Brotli Q11 | 1.00 MB | 900.00 B | 1165.08x | 18.16 | 0.99 | 55.08 MB/s | 1010.18 MB/s | 0.7843 | 101.04 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 24.75% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.067139)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: structured_sqlite_large

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 1.00 MB | 65.00 B | 16131.94x | 6.02 | 0.24 | 166.22 MB/s | 4213.88 MB/s | 0.7786 | 101.05 | 65 | ❌ | 0.043278 | 0.043278 | ❌ | ✅ |
| SHA256 | 1.00 MB | 64.00 B | 16384.00x | 0.76 | 0.00 | 1307.28 MB/s | 0.00 MB/s | 0.7649 | 101.05 | - | - | - | - | - | - |
| AES-GCM | 1.00 MB | 1.00 MB | 1.00x | 0.51 | 0.42 | 1954.29 MB/s | 2389.67 MB/s | 0.7779 | 101.05 | - | - | - | - | - | - |
| Frackture Encrypted | 1.00 MB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 1.00 MB | 6.34 KB | 161.57x | 1.85 | 0.60 | 540.09 MB/s | 1664.89 MB/s | 0.7952 | 101.05 | - | - | - | - | - | - |
| Gzip L2 | 1.00 MB | 6.33 KB | 161.72x | 1.77 | 0.50 | 564.58 MB/s | 1995.00 MB/s | 0.7781 | 101.05 | - | - | - | - | - | - |
| Gzip L3 | 1.00 MB | 6.03 KB | 169.92x | 1.73 | 0.47 | 576.64 MB/s | 2110.71 MB/s | 0.7789 | 101.05 | - | - | - | - | - | - |
| Gzip L4 | 1.00 MB | 2.66 KB | 385.22x | 3.53 | 1.12 | 283.36 MB/s | 896.58 MB/s | 0.7823 | 101.05 | - | - | - | - | - | - |
| Gzip L5 | 1.00 MB | 2.66 KB | 385.65x | 3.56 | 1.27 | 281.03 MB/s | 788.99 MB/s | 0.7763 | 101.05 | - | - | - | - | - | - |
| Gzip L6 | 1.00 MB | 2.47 KB | 414.95x | 3.77 | 0.82 | 265.49 MB/s | 1212.21 MB/s | 0.7837 | 101.05 | - | - | - | - | - | - |
| Gzip L7 | 1.00 MB | 2.47 KB | 414.95x | 3.52 | 0.72 | 283.89 MB/s | 1397.35 MB/s | 0.7803 | 101.05 | - | - | - | - | - | - |
| Gzip L8 | 1.00 MB | 2.47 KB | 414.95x | 4.20 | 0.96 | 237.97 MB/s | 1039.96 MB/s | 0.7812 | 101.05 | - | - | - | - | - | - |
| Gzip L9 | 1.00 MB | 2.47 KB | 414.95x | 6.49 | 0.96 | 154.02 MB/s | 1037.27 MB/s | 0.7781 | 101.05 | - | - | - | - | - | - |
| Brotli Q0 | 1.00 MB | 1.79 KB | 573.31x | 0.38 | 0.47 | 2611.42 MB/s | 2145.28 MB/s | 0.7768 | 101.05 | - | - | - | - | - | - |
| Brotli Q1 | 1.00 MB | 1.32 KB | 777.88x | 0.21 | 0.70 | 4752.15 MB/s | 1419.58 MB/s | 0.7755 | 101.05 | - | - | - | - | - | - |
| Brotli Q2 | 1.00 MB | 513.00 B | 2044.01x | 0.96 | 0.98 | 1036.31 MB/s | 1021.51 MB/s | 0.7750 | 101.05 | - | - | - | - | - | - |
| Brotli Q3 | 1.00 MB | 500.00 B | 2097.15x | 0.98 | 1.01 | 1019.12 MB/s | 988.66 MB/s | 0.7792 | 101.05 | - | - | - | - | - | - |
| Brotli Q4 | 1.00 MB | 522.00 B | 2008.77x | 1.48 | 0.98 | 677.72 MB/s | 1020.38 MB/s | 0.7743 | 101.05 | - | - | - | - | - | - |
| Brotli Q5 | 1.00 MB | 530.00 B | 1978.45x | 1.23 | 1.01 | 813.20 MB/s | 992.38 MB/s | 0.7748 | 101.05 | - | - | - | - | - | - |
| Brotli Q6 | 1.00 MB | 530.00 B | 1978.45x | 1.20 | 1.02 | 830.60 MB/s | 981.58 MB/s | 0.7981 | 101.05 | - | - | - | - | - | - |
| Brotli Q7 | 1.00 MB | 528.00 B | 1985.94x | 1.23 | 1.00 | 813.31 MB/s | 1000.05 MB/s | 0.7776 | 101.06 | - | - | - | - | - | - |
| Brotli Q8 | 1.00 MB | 528.00 B | 1985.94x | 1.24 | 1.03 | 809.01 MB/s | 969.31 MB/s | 0.7733 | 101.15 | - | - | - | - | - | - |
| Brotli Q9 | 1.00 MB | 528.00 B | 1985.94x | 2.22 | 1.01 | 450.68 MB/s | 994.79 MB/s | 0.7888 | 101.15 | - | - | - | - | - | - |
| Brotli Q10 | 1.00 MB | 401.00 B | 2614.90x | 16.10 | 1.00 | 62.11 MB/s | 996.28 MB/s | 0.7983 | 101.16 | - | - | - | - | - | - |
| Brotli Q11 | 1.00 MB | 392.00 B | 2674.94x | 22.97 | 0.98 | 43.54 MB/s | 1015.48 MB/s | 0.7855 | 101.16 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 0.00% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.043278)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: structured_pickle_large

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 1.00 MB | 65.00 B | 16131.94x | 6.05 | 0.24 | 165.19 MB/s | 4122.01 MB/s | 0.7810 | 101.16 | 65 | ❌ | 0.212640 | 0.180567 | ❌ | ✅ |
| SHA256 | 1.00 MB | 64.00 B | 16384.00x | 0.79 | 0.00 | 1266.57 MB/s | 0.00 MB/s | 0.7895 | 101.16 | - | - | - | - | - | - |
| AES-GCM | 1.00 MB | 1.00 MB | 1.00x | 0.46 | 0.55 | 2162.58 MB/s | 1824.68 MB/s | 0.7756 | 101.16 | - | - | - | - | - | - |
| Frackture Encrypted | 1.00 MB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 1.00 MB | 8.90 KB | 115.08x | 1.75 | 0.49 | 572.91 MB/s | 2026.33 MB/s | 0.7912 | 101.16 | - | - | - | - | - | - |
| Gzip L2 | 1.00 MB | 7.69 KB | 133.24x | 1.79 | 0.52 | 560.14 MB/s | 1924.95 MB/s | 0.7829 | 101.16 | - | - | - | - | - | - |
| Gzip L3 | 1.00 MB | 7.74 KB | 132.26x | 1.73 | 0.49 | 577.19 MB/s | 2048.29 MB/s | 0.7807 | 101.16 | - | - | - | - | - | - |
| Gzip L4 | 1.00 MB | 4.15 KB | 246.72x | 3.53 | 0.47 | 283.20 MB/s | 2137.83 MB/s | 0.7678 | 101.16 | - | - | - | - | - | - |
| Gzip L5 | 1.00 MB | 4.15 KB | 246.72x | 3.41 | 0.56 | 293.65 MB/s | 1770.90 MB/s | 0.7773 | 101.16 | - | - | - | - | - | - |
| Gzip L6 | 1.00 MB | 4.15 KB | 246.72x | 3.51 | 0.53 | 284.71 MB/s | 1869.42 MB/s | 0.7761 | 101.16 | - | - | - | - | - | - |
| Gzip L7 | 1.00 MB | 4.15 KB | 246.72x | 3.39 | 0.48 | 294.65 MB/s | 2077.55 MB/s | 0.7878 | 101.16 | - | - | - | - | - | - |
| Gzip L8 | 1.00 MB | 4.15 KB | 246.72x | 3.46 | 0.42 | 289.31 MB/s | 2364.14 MB/s | 0.7791 | 101.16 | - | - | - | - | - | - |
| Gzip L9 | 1.00 MB | 4.15 KB | 246.72x | 3.45 | 0.44 | 290.15 MB/s | 2264.91 MB/s | 0.7806 | 101.16 | - | - | - | - | - | - |
| Brotli Q0 | 1.00 MB | 676.00 B | 1551.15x | 0.16 | 0.60 | 6217.32 MB/s | 1664.44 MB/s | 0.7813 | 101.16 | - | - | - | - | - | - |
| Brotli Q1 | 1.00 MB | 636.00 B | 1648.70x | 0.18 | 0.91 | 5712.88 MB/s | 1102.97 MB/s | 0.7819 | 101.16 | - | - | - | - | - | - |
| Brotli Q2 | 1.00 MB | 176.00 B | 5957.82x | 1.02 | 1.14 | 983.65 MB/s | 876.58 MB/s | 0.7800 | 101.16 | - | - | - | - | - | - |
| Brotli Q3 | 1.00 MB | 150.00 B | 6990.51x | 0.97 | 0.97 | 1034.93 MB/s | 1031.57 MB/s | 0.7793 | 101.16 | - | - | - | - | - | - |
| Brotli Q4 | 1.00 MB | 149.00 B | 7037.42x | 1.29 | 1.00 | 777.77 MB/s | 998.83 MB/s | 0.7831 | 101.16 | - | - | - | - | - | - |
| Brotli Q5 | 1.00 MB | 195.00 B | 5377.31x | 0.99 | 0.97 | 1008.59 MB/s | 1035.58 MB/s | 0.7857 | 101.16 | - | - | - | - | - | - |
| Brotli Q6 | 1.00 MB | 195.00 B | 5377.31x | 1.17 | 1.00 | 854.49 MB/s | 999.66 MB/s | 0.7772 | 101.16 | - | - | - | - | - | - |
| Brotli Q7 | 1.00 MB | 197.00 B | 5322.72x | 1.03 | 1.05 | 971.15 MB/s | 954.92 MB/s | 0.7746 | 101.16 | - | - | - | - | - | - |
| Brotli Q8 | 1.00 MB | 197.00 B | 5322.72x | 1.00 | 1.00 | 1002.03 MB/s | 1000.40 MB/s | 0.7731 | 101.17 | - | - | - | - | - | - |
| Brotli Q9 | 1.00 MB | 197.00 B | 5322.72x | 1.21 | 0.98 | 827.42 MB/s | 1017.81 MB/s | 0.7702 | 101.17 | - | - | - | - | - | - |
| Brotli Q10 | 1.00 MB | 141.00 B | 7436.71x | 13.89 | 0.99 | 71.98 MB/s | 1012.24 MB/s | 0.7769 | 101.17 | - | - | - | - | - | - |
| Brotli Q11 | 1.00 MB | 139.00 B | 7543.71x | 16.39 | 0.95 | 61.03 MB/s | 1056.74 MB/s | 0.7802 | 101.17 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 15.08% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.212640)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: text_plain_large

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 1.00 MB | 65.00 B | 16131.94x | 5.89 | 0.25 | 169.65 MB/s | 4049.88 MB/s | 0.7775 | 101.19 | 65 | ❌ | 0.313108 | 0.244711 | ❌ | ✅ |
| SHA256 | 1.00 MB | 64.00 B | 16384.00x | 0.77 | 0.00 | 1300.78 MB/s | 0.00 MB/s | 0.7688 | 101.19 | - | - | - | - | - | - |
| AES-GCM | 1.00 MB | 1.00 MB | 1.00x | 0.53 | 0.39 | 1893.86 MB/s | 2572.60 MB/s | 0.7769 | 101.19 | - | - | - | - | - | - |
| Frackture Encrypted | 1.00 MB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 1.00 MB | 11.11 KB | 92.13x | 1.85 | 0.53 | 539.31 MB/s | 1887.69 MB/s | 0.7804 | 101.19 | - | - | - | - | - | - |
| Gzip L2 | 1.00 MB | 8.50 KB | 120.53x | 1.74 | 0.56 | 573.88 MB/s | 1796.82 MB/s | 0.7767 | 101.19 | - | - | - | - | - | - |
| Gzip L3 | 1.00 MB | 8.54 KB | 119.89x | 1.72 | 0.49 | 582.38 MB/s | 2053.14 MB/s | 0.7769 | 101.19 | - | - | - | - | - | - |
| Gzip L4 | 1.00 MB | 5.39 KB | 190.10x | 3.43 | 0.49 | 291.42 MB/s | 2024.22 MB/s | 0.7746 | 101.19 | - | - | - | - | - | - |
| Gzip L5 | 1.00 MB | 5.38 KB | 190.17x | 3.46 | 0.45 | 288.71 MB/s | 2217.62 MB/s | 0.7746 | 101.19 | - | - | - | - | - | - |
| Gzip L6 | 1.00 MB | 5.38 KB | 190.17x | 3.49 | 0.42 | 286.38 MB/s | 2360.24 MB/s | 0.7804 | 101.19 | - | - | - | - | - | - |
| Gzip L7 | 1.00 MB | 5.38 KB | 190.17x | 3.57 | 0.43 | 280.05 MB/s | 2311.95 MB/s | 0.7699 | 101.19 | - | - | - | - | - | - |
| Gzip L8 | 1.00 MB | 5.38 KB | 190.17x | 3.54 | 0.50 | 282.66 MB/s | 2010.62 MB/s | 0.7759 | 101.19 | - | - | - | - | - | - |
| Gzip L9 | 1.00 MB | 5.38 KB | 190.17x | 3.54 | 0.49 | 282.37 MB/s | 2037.09 MB/s | 0.7662 | 101.19 | - | - | - | - | - | - |
| Brotli Q0 | 1.00 MB | 749.00 B | 1399.97x | 0.17 | 0.34 | 6058.81 MB/s | 2973.01 MB/s | 0.7805 | 101.19 | - | - | - | - | - | - |
| Brotli Q1 | 1.00 MB | 806.00 B | 1300.96x | 0.20 | 0.70 | 5097.28 MB/s | 1438.25 MB/s | 0.7705 | 101.19 | - | - | - | - | - | - |
| Brotli Q2 | 1.00 MB | 379.00 B | 2766.69x | 0.90 | 0.98 | 1107.37 MB/s | 1022.79 MB/s | 0.7732 | 101.19 | - | - | - | - | - | - |
| Brotli Q3 | 1.00 MB | 366.00 B | 2864.96x | 0.96 | 0.97 | 1041.24 MB/s | 1034.75 MB/s | 0.7709 | 101.19 | - | - | - | - | - | - |
| Brotli Q4 | 1.00 MB | 367.00 B | 2857.16x | 1.26 | 1.00 | 795.25 MB/s | 1001.98 MB/s | 0.7690 | 101.19 | - | - | - | - | - | - |
| Brotli Q5 | 1.00 MB | 395.00 B | 2654.62x | 1.05 | 1.00 | 956.92 MB/s | 999.29 MB/s | 0.7674 | 101.19 | - | - | - | - | - | - |
| Brotli Q6 | 1.00 MB | 395.00 B | 2654.62x | 1.03 | 0.96 | 973.90 MB/s | 1038.86 MB/s | 0.7778 | 101.19 | - | - | - | - | - | - |
| Brotli Q7 | 1.00 MB | 397.00 B | 2641.25x | 1.07 | 0.99 | 937.00 MB/s | 1015.12 MB/s | 0.7739 | 101.20 | - | - | - | - | - | - |
| Brotli Q8 | 1.00 MB | 397.00 B | 2641.25x | 1.11 | 1.00 | 903.24 MB/s | 1000.51 MB/s | 0.7708 | 101.27 | - | - | - | - | - | - |
| Brotli Q9 | 1.00 MB | 397.00 B | 2641.25x | 1.91 | 0.97 | 522.62 MB/s | 1032.97 MB/s | 0.7737 | 101.27 | - | - | - | - | - | - |
| Brotli Q10 | 1.00 MB | 321.00 B | 3266.59x | 12.06 | 0.97 | 82.93 MB/s | 1030.58 MB/s | 0.7799 | 101.27 | - | - | - | - | - | - |
| Brotli Q11 | 1.00 MB | 318.00 B | 3297.41x | 14.84 | 0.97 | 67.37 MB/s | 1026.74 MB/s | 0.7798 | 101.27 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 21.84% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.313108)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: text_log_large

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 1.00 MB | 65.00 B | 16131.94x | 5.94 | 0.24 | 168.41 MB/s | 4187.55 MB/s | 0.7722 | 101.28 | 65 | ❌ | 0.199651 | 0.123128 | ❌ | ✅ |
| SHA256 | 1.00 MB | 64.00 B | 16384.00x | 0.76 | 0.00 | 1307.78 MB/s | 0.00 MB/s | 0.7647 | 101.28 | - | - | - | - | - | - |
| AES-GCM | 1.00 MB | 1.00 MB | 1.00x | 0.49 | 0.36 | 2020.30 MB/s | 2770.89 MB/s | 0.7735 | 101.28 | - | - | - | - | - | - |
| Frackture Encrypted | 1.00 MB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 1.00 MB | 9.86 KB | 103.87x | 1.75 | 0.51 | 571.22 MB/s | 1950.33 MB/s | 0.7776 | 101.28 | - | - | - | - | - | - |
| Gzip L2 | 1.00 MB | 9.64 KB | 106.24x | 1.86 | 0.59 | 538.33 MB/s | 1699.55 MB/s | 0.7724 | 101.28 | - | - | - | - | - | - |
| Gzip L3 | 1.00 MB | 9.86 KB | 103.89x | 1.77 | 0.67 | 565.31 MB/s | 1483.88 MB/s | 0.7735 | 101.28 | - | - | - | - | - | - |
| Gzip L4 | 1.00 MB | 8.92 KB | 114.80x | 3.53 | 0.75 | 283.66 MB/s | 1327.79 MB/s | 0.7749 | 101.28 | - | - | - | - | - | - |
| Gzip L5 | 1.00 MB | 6.03 KB | 169.78x | 3.44 | 0.52 | 290.67 MB/s | 1922.24 MB/s | 0.7731 | 101.28 | - | - | - | - | - | - |
| Gzip L6 | 1.00 MB | 6.03 KB | 169.78x | 3.87 | 0.51 | 258.52 MB/s | 1944.55 MB/s | 0.7786 | 101.28 | - | - | - | - | - | - |
| Gzip L7 | 1.00 MB | 5.36 KB | 191.07x | 3.78 | 0.50 | 264.86 MB/s | 2017.02 MB/s | 0.7715 | 101.28 | - | - | - | - | - | - |
| Gzip L8 | 1.00 MB | 5.23 KB | 195.92x | 3.95 | 0.45 | 253.05 MB/s | 2217.17 MB/s | 0.7750 | 101.28 | - | - | - | - | - | - |
| Gzip L9 | 1.00 MB | 5.23 KB | 195.92x | 3.92 | 0.55 | 255.13 MB/s | 1824.52 MB/s | 0.7745 | 101.28 | - | - | - | - | - | - |
| Brotli Q0 | 1.00 MB | 833.00 B | 1258.79x | 0.32 | 0.52 | 3172.62 MB/s | 1911.24 MB/s | 0.7744 | 101.28 | - | - | - | - | - | - |
| Brotli Q1 | 1.00 MB | 883.00 B | 1187.52x | 0.18 | 0.63 | 5622.02 MB/s | 1582.24 MB/s | 0.7770 | 101.28 | - | - | - | - | - | - |
| Brotli Q2 | 1.00 MB | 246.00 B | 4262.50x | 0.90 | 1.01 | 1108.40 MB/s | 992.61 MB/s | 0.7707 | 101.28 | - | - | - | - | - | - |
| Brotli Q3 | 1.00 MB | 233.00 B | 4500.33x | 0.92 | 0.96 | 1089.54 MB/s | 1037.52 MB/s | 0.7749 | 101.28 | - | - | - | - | - | - |
| Brotli Q4 | 1.00 MB | 232.00 B | 4519.72x | 1.27 | 0.97 | 785.09 MB/s | 1032.87 MB/s | 0.7760 | 101.28 | - | - | - | - | - | - |
| Brotli Q5 | 1.00 MB | 267.00 B | 3927.25x | 1.03 | 0.98 | 971.98 MB/s | 1021.16 MB/s | 0.7706 | 101.28 | - | - | - | - | - | - |
| Brotli Q6 | 1.00 MB | 267.00 B | 3927.25x | 1.00 | 1.01 | 1003.80 MB/s | 986.52 MB/s | 0.7677 | 101.28 | - | - | - | - | - | - |
| Brotli Q7 | 1.00 MB | 265.00 B | 3956.89x | 1.01 | 0.98 | 985.90 MB/s | 1016.08 MB/s | 0.7617 | 101.28 | - | - | - | - | - | - |
| Brotli Q8 | 1.00 MB | 265.00 B | 3956.89x | 0.98 | 0.97 | 1015.69 MB/s | 1035.06 MB/s | 0.7816 | 101.28 | - | - | - | - | - | - |
| Brotli Q9 | 1.00 MB | 265.00 B | 3956.89x | 1.47 | 0.98 | 681.29 MB/s | 1020.44 MB/s | 0.7767 | 101.28 | - | - | - | - | - | - |
| Brotli Q10 | 1.00 MB | 193.00 B | 5433.04x | 12.91 | 1.01 | 77.45 MB/s | 985.80 MB/s | 0.7782 | 101.28 | - | - | - | - | - | - |
| Brotli Q11 | 1.00 MB | 192.00 B | 5461.33x | 15.88 | 0.96 | 62.98 MB/s | 1038.13 MB/s | 0.7777 | 101.28 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 38.33% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.199651)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: text_json_large

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 1.00 MB | 65.00 B | 16131.94x | 5.76 | 0.27 | 173.68 MB/s | 3765.88 MB/s | 0.7857 | 101.29 | 65 | ❌ | 0.203007 | 0.142893 | ❌ | ✅ |
| SHA256 | 1.00 MB | 64.00 B | 16384.00x | 0.77 | 0.00 | 1300.94 MB/s | 0.00 MB/s | 0.7687 | 101.29 | - | - | - | - | - | - |
| AES-GCM | 1.00 MB | 1.00 MB | 1.00x | 0.44 | 0.40 | 2274.34 MB/s | 2523.04 MB/s | 0.7764 | 101.29 | - | - | - | - | - | - |
| Frackture Encrypted | 1.00 MB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 1.00 MB | 16.19 KB | 63.26x | 1.99 | 0.61 | 501.92 MB/s | 1627.44 MB/s | 0.7771 | 101.29 | - | - | - | - | - | - |
| Gzip L2 | 1.00 MB | 15.00 KB | 68.29x | 1.97 | 0.54 | 508.91 MB/s | 1837.67 MB/s | 0.7778 | 101.29 | - | - | - | - | - | - |
| Gzip L3 | 1.00 MB | 13.73 KB | 74.57x | 1.97 | 0.59 | 506.60 MB/s | 1692.74 MB/s | 0.7755 | 101.29 | - | - | - | - | - | - |
| Gzip L4 | 1.00 MB | 7.35 KB | 139.33x | 3.43 | 0.60 | 291.34 MB/s | 1674.55 MB/s | 0.7948 | 101.29 | - | - | - | - | - | - |
| Gzip L5 | 1.00 MB | 8.49 KB | 120.60x | 3.62 | 0.56 | 275.93 MB/s | 1794.66 MB/s | 0.7714 | 101.29 | - | - | - | - | - | - |
| Gzip L6 | 1.00 MB | 6.29 KB | 162.70x | 6.37 | 0.47 | 157.07 MB/s | 2127.91 MB/s | 0.7771 | 101.29 | - | - | - | - | - | - |
| Gzip L7 | 1.00 MB | 5.35 KB | 191.49x | 6.42 | 0.52 | 155.77 MB/s | 1916.86 MB/s | 0.7743 | 101.29 | - | - | - | - | - | - |
| Gzip L8 | 1.00 MB | 5.35 KB | 191.49x | 3.98 | 0.47 | 251.15 MB/s | 2114.46 MB/s | 0.7702 | 101.29 | - | - | - | - | - | - |
| Gzip L9 | 1.00 MB | 5.35 KB | 191.49x | 3.84 | 0.43 | 260.31 MB/s | 2306.19 MB/s | 0.7731 | 101.29 | - | - | - | - | - | - |
| Brotli Q0 | 1.00 MB | 1.22 KB | 838.19x | 0.42 | 0.36 | 2365.98 MB/s | 2739.75 MB/s | 0.7695 | 101.29 | - | - | - | - | - | - |
| Brotli Q1 | 1.00 MB | 1.25 KB | 821.12x | 0.20 | 0.93 | 4890.21 MB/s | 1080.78 MB/s | 0.7777 | 101.29 | - | - | - | - | - | - |
| Brotli Q2 | 1.00 MB | 368.00 B | 2849.39x | 0.91 | 1.00 | 1103.44 MB/s | 1001.01 MB/s | 0.7723 | 101.29 | - | - | - | - | - | - |
| Brotli Q3 | 1.00 MB | 359.00 B | 2920.82x | 0.90 | 0.96 | 1111.10 MB/s | 1036.83 MB/s | 0.7784 | 101.29 | - | - | - | - | - | - |
| Brotli Q4 | 1.00 MB | 351.00 B | 2987.40x | 1.36 | 0.98 | 734.03 MB/s | 1015.95 MB/s | 0.7756 | 101.30 | - | - | - | - | - | - |
| Brotli Q5 | 1.00 MB | 372.00 B | 2818.75x | 1.06 | 1.00 | 941.41 MB/s | 998.65 MB/s | 0.7715 | 101.30 | - | - | - | - | - | - |
| Brotli Q6 | 1.00 MB | 372.00 B | 2818.75x | 1.01 | 0.95 | 989.80 MB/s | 1050.92 MB/s | 0.7749 | 101.30 | - | - | - | - | - | - |
| Brotli Q7 | 1.00 MB | 376.00 B | 2788.77x | 1.09 | 0.99 | 921.20 MB/s | 1012.75 MB/s | 0.7724 | 101.30 | - | - | - | - | - | - |
| Brotli Q8 | 1.00 MB | 376.00 B | 2788.77x | 1.07 | 1.02 | 932.81 MB/s | 976.10 MB/s | 0.7696 | 101.36 | - | - | - | - | - | - |
| Brotli Q9 | 1.00 MB | 373.00 B | 2811.20x | 1.73 | 1.04 | 576.80 MB/s | 966.11 MB/s | 0.7773 | 101.36 | - | - | - | - | - | - |
| Brotli Q10 | 1.00 MB | 300.00 B | 3495.25x | 13.69 | 1.03 | 73.03 MB/s | 969.81 MB/s | 0.7691 | 101.36 | - | - | - | - | - | - |
| Brotli Q11 | 1.00 MB | 293.00 B | 3578.76x | 16.55 | 1.09 | 60.41 MB/s | 919.73 MB/s | 0.8153 | 101.36 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 29.61% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.203007)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: text_csv_large

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 1.00 MB | 65.00 B | 16131.94x | 5.98 | 0.33 | 167.14 MB/s | 3023.89 MB/s | 0.7755 | 101.37 | 65 | ❌ | 0.199575 | 0.188218 | ❌ | ✅ |
| SHA256 | 1.00 MB | 64.00 B | 16384.00x | 0.78 | 0.00 | 1274.36 MB/s | 0.00 MB/s | 0.7847 | 101.37 | - | - | - | - | - | - |
| AES-GCM | 1.00 MB | 1.00 MB | 1.00x | 0.51 | 0.39 | 1959.87 MB/s | 2542.51 MB/s | 0.7729 | 101.37 | - | - | - | - | - | - |
| Frackture Encrypted | 1.00 MB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 1.00 MB | 7.08 KB | 144.65x | 2.19 | 0.60 | 457.40 MB/s | 1668.90 MB/s | 0.7740 | 101.37 | - | - | - | - | - | - |
| Gzip L2 | 1.00 MB | 7.20 KB | 142.14x | 1.69 | 0.44 | 591.35 MB/s | 2287.20 MB/s | 0.7771 | 101.37 | - | - | - | - | - | - |
| Gzip L3 | 1.00 MB | 7.18 KB | 142.53x | 1.72 | 0.48 | 582.88 MB/s | 2102.39 MB/s | 0.7847 | 101.37 | - | - | - | - | - | - |
| Gzip L4 | 1.00 MB | 4.17 KB | 245.28x | 3.97 | 0.47 | 251.59 MB/s | 2111.69 MB/s | 0.7929 | 101.37 | - | - | - | - | - | - |
| Gzip L5 | 1.00 MB | 4.17 KB | 245.28x | 4.76 | 0.68 | 209.88 MB/s | 1464.35 MB/s | 0.7739 | 101.37 | - | - | - | - | - | - |
| Gzip L6 | 1.00 MB | 4.17 KB | 245.28x | 3.41 | 0.45 | 292.91 MB/s | 2223.39 MB/s | 0.7661 | 101.37 | - | - | - | - | - | - |
| Gzip L7 | 1.00 MB | 4.17 KB | 245.28x | 3.53 | 0.51 | 282.98 MB/s | 1950.52 MB/s | 0.7886 | 101.37 | - | - | - | - | - | - |
| Gzip L8 | 1.00 MB | 4.17 KB | 245.28x | 3.37 | 0.48 | 296.90 MB/s | 2062.33 MB/s | 0.7698 | 101.37 | - | - | - | - | - | - |
| Gzip L9 | 1.00 MB | 4.17 KB | 245.28x | 3.70 | 0.50 | 270.51 MB/s | 1985.32 MB/s | 0.7754 | 101.37 | - | - | - | - | - | - |
| Brotli Q0 | 1.00 MB | 681.00 B | 1539.76x | 0.28 | 0.53 | 3527.69 MB/s | 1876.16 MB/s | 0.7709 | 101.37 | - | - | - | - | - | - |
| Brotli Q1 | 1.00 MB | 690.00 B | 1519.68x | 0.26 | 0.83 | 3898.94 MB/s | 1209.80 MB/s | 0.7771 | 101.37 | - | - | - | - | - | - |
| Brotli Q2 | 1.00 MB | 188.00 B | 5577.53x | 0.90 | 1.02 | 1114.08 MB/s | 983.57 MB/s | 0.7715 | 101.37 | - | - | - | - | - | - |
| Brotli Q3 | 1.00 MB | 171.00 B | 6132.02x | 0.96 | 0.98 | 1036.58 MB/s | 1024.03 MB/s | 0.7714 | 101.37 | - | - | - | - | - | - |
| Brotli Q4 | 1.00 MB | 171.00 B | 6132.02x | 1.32 | 1.00 | 759.77 MB/s | 996.63 MB/s | 0.7691 | 101.37 | - | - | - | - | - | - |
| Brotli Q5 | 1.00 MB | 195.00 B | 5377.31x | 0.98 | 1.02 | 1018.16 MB/s | 979.95 MB/s | 0.7734 | 101.37 | - | - | - | - | - | - |
| Brotli Q6 | 1.00 MB | 195.00 B | 5377.31x | 0.96 | 0.97 | 1039.02 MB/s | 1035.06 MB/s | 0.7759 | 101.37 | - | - | - | - | - | - |
| Brotli Q7 | 1.00 MB | 196.00 B | 5349.88x | 1.03 | 0.98 | 974.56 MB/s | 1024.89 MB/s | 0.7736 | 101.37 | - | - | - | - | - | - |
| Brotli Q8 | 1.00 MB | 196.00 B | 5349.88x | 1.01 | 0.97 | 991.30 MB/s | 1028.80 MB/s | 0.7676 | 101.37 | - | - | - | - | - | - |
| Brotli Q9 | 1.00 MB | 196.00 B | 5349.88x | 1.28 | 1.02 | 783.88 MB/s | 978.01 MB/s | 0.7768 | 101.37 | - | - | - | - | - | - |
| Brotli Q10 | 1.00 MB | 150.00 B | 6990.51x | 12.66 | 1.00 | 78.99 MB/s | 995.94 MB/s | 0.7924 | 101.37 | - | - | - | - | - | - |
| Brotli Q11 | 1.00 MB | 151.00 B | 6944.21x | 14.81 | 0.98 | 67.52 MB/s | 1023.21 MB/s | 0.7804 | 101.37 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 5.69% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.199575)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: code_javascript_xlarge

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 10.00 MB | 65.00 B | 161319.38x | 6.24 | 0.29 | 1602.54 MB/s | 34175.18 MB/s | 8.0441 | 100.59 | 65 | ❌ | 0.210678 | 0.176264 | ❌ | ✅ |
| SHA256 | 10.00 MB | 64.00 B | 163840.00x | 7.72 | 0.00 | 1295.96 MB/s | 0.00 MB/s | 7.7163 | 100.67 | - | - | - | - | - | - |
| AES-GCM | 10.00 MB | 10.00 MB | 1.00x | 6.98 | 11.96 | 1431.68 MB/s | 836.12 MB/s | 7.7917 | 126.23 | - | - | - | - | - | - |
| Frackture Encrypted | 10.00 MB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 10.00 MB | 85.69 KB | 119.50x | 22.57 | 6.97 | 443.06 MB/s | 1434.20 MB/s | 7.8268 | 126.52 | - | - | - | - | - | - |
| Gzip L2 | 10.00 MB | 116.52 KB | 87.88x | 20.20 | 8.10 | 494.98 MB/s | 1235.24 MB/s | 7.7304 | 126.52 | - | - | - | - | - | - |
| Gzip L3 | 10.00 MB | 91.91 KB | 111.42x | 18.07 | 5.85 | 553.50 MB/s | 1710.01 MB/s | 7.7029 | 126.52 | - | - | - | - | - | - |
| Gzip L4 | 10.00 MB | 56.13 KB | 182.42x | 35.83 | 5.68 | 279.09 MB/s | 1759.83 MB/s | 7.7947 | 126.52 | - | - | - | - | - | - |
| Gzip L5 | 10.00 MB | 56.13 KB | 182.44x | 36.56 | 5.85 | 273.55 MB/s | 1708.84 MB/s | 7.7325 | 126.52 | - | - | - | - | - | - |
| Gzip L6 | 10.00 MB | 49.97 KB | 204.94x | 36.13 | 5.90 | 276.77 MB/s | 1695.88 MB/s | 7.7182 | 126.52 | - | - | - | - | - | - |
| Gzip L7 | 10.00 MB | 49.97 KB | 204.94x | 35.89 | 5.57 | 278.67 MB/s | 1793.76 MB/s | 7.7327 | 126.52 | - | - | - | - | - | - |
| Gzip L8 | 10.00 MB | 49.97 KB | 204.94x | 35.62 | 5.95 | 280.73 MB/s | 1681.51 MB/s | 7.7230 | 126.52 | - | - | - | - | - | - |
| Gzip L9 | 10.00 MB | 49.97 KB | 204.94x | 35.80 | 5.59 | 279.34 MB/s | 1788.91 MB/s | 7.7138 | 126.52 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 16.33% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.210678)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: code_javascript_minified_xlarge

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 10.00 MB | 65.00 B | 161319.38x | 6.04 | 0.25 | 1655.53 MB/s | 40253.60 MB/s | 7.7475 | 86.65 | 65 | ❌ | 0.248601 | 0.216233 | ❌ | ✅ |
| SHA256 | 10.00 MB | 64.00 B | 163840.00x | 7.66 | 0.00 | 1305.42 MB/s | 0.00 MB/s | 7.6604 | 86.65 | - | - | - | - | - | - |
| AES-GCM | 10.00 MB | 10.00 MB | 1.00x | 11.73 | 11.61 | 852.34 MB/s | 861.54 MB/s | 7.7252 | 126.53 | - | - | - | - | - | - |
| Frackture Encrypted | 10.00 MB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 10.00 MB | 76.69 KB | 133.53x | 19.16 | 12.84 | 521.85 MB/s | 778.60 MB/s | 7.8067 | 105.19 | - | - | - | - | - | - |
| Gzip L2 | 10.00 MB | 76.64 KB | 133.62x | 17.78 | 5.66 | 562.54 MB/s | 1767.93 MB/s | 7.7041 | 105.19 | - | - | - | - | - | - |
| Gzip L3 | 10.00 MB | 76.62 KB | 133.65x | 16.97 | 5.32 | 589.20 MB/s | 1880.29 MB/s | 7.7563 | 105.19 | - | - | - | - | - | - |
| Gzip L4 | 10.00 MB | 39.92 KB | 256.50x | 34.40 | 6.12 | 290.68 MB/s | 1634.16 MB/s | 7.7089 | 105.19 | - | - | - | - | - | - |
| Gzip L5 | 10.00 MB | 39.92 KB | 256.50x | 33.93 | 5.74 | 294.76 MB/s | 1742.41 MB/s | 7.7052 | 105.19 | - | - | - | - | - | - |
| Gzip L6 | 10.00 MB | 39.92 KB | 256.50x | 43.38 | 5.77 | 230.55 MB/s | 1733.17 MB/s | 7.7158 | 105.19 | - | - | - | - | - | - |
| Gzip L7 | 10.00 MB | 39.92 KB | 256.50x | 34.75 | 5.71 | 287.78 MB/s | 1752.63 MB/s | 7.6973 | 105.19 | - | - | - | - | - | - |
| Gzip L8 | 10.00 MB | 39.92 KB | 256.50x | 35.16 | 5.64 | 284.45 MB/s | 1772.47 MB/s | 7.7474 | 105.19 | - | - | - | - | - | - |
| Gzip L9 | 10.00 MB | 39.92 KB | 256.50x | 34.39 | 5.71 | 290.79 MB/s | 1752.59 MB/s | 7.7118 | 105.19 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 13.02% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.248601)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: code_python_xlarge

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 10.00 MB | 65.00 B | 161319.38x | 5.95 | 0.25 | 1680.29 MB/s | 39962.12 MB/s | 7.7447 | 108.54 | 65 | ❌ | 0.201540 | 0.173739 | ❌ | ✅ |
| SHA256 | 10.00 MB | 64.00 B | 163840.00x | 7.63 | 0.00 | 1309.89 MB/s | 0.00 MB/s | 7.6342 | 108.54 | - | - | - | - | - | - |
| AES-GCM | 10.00 MB | 10.00 MB | 1.00x | 4.54 | 11.29 | 2202.43 MB/s | 885.35 MB/s | 7.6759 | 126.54 | - | - | - | - | - | - |
| Frackture Encrypted | 10.00 MB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 10.00 MB | 192.75 KB | 53.13x | 20.73 | 7.01 | 482.47 MB/s | 1426.07 MB/s | 7.7021 | 126.54 | - | - | - | - | - | - |
| Gzip L2 | 10.00 MB | 188.72 KB | 54.26x | 20.82 | 6.61 | 480.29 MB/s | 1511.96 MB/s | 7.6784 | 126.54 | - | - | - | - | - | - |
| Gzip L3 | 10.00 MB | 151.14 KB | 67.75x | 19.10 | 6.30 | 523.44 MB/s | 1588.07 MB/s | 7.6919 | 126.54 | - | - | - | - | - | - |
| Gzip L4 | 10.00 MB | 82.70 KB | 123.82x | 35.16 | 5.92 | 284.43 MB/s | 1688.18 MB/s | 7.7100 | 126.54 | - | - | - | - | - | - |
| Gzip L5 | 10.00 MB | 75.26 KB | 136.06x | 35.67 | 5.94 | 280.33 MB/s | 1684.82 MB/s | 7.6911 | 126.54 | - | - | - | - | - | - |
| Gzip L6 | 10.00 MB | 74.32 KB | 137.78x | 38.89 | 5.73 | 257.16 MB/s | 1743.80 MB/s | 7.6850 | 126.54 | - | - | - | - | - | - |
| Gzip L7 | 10.00 MB | 55.20 KB | 185.52x | 36.88 | 6.09 | 271.14 MB/s | 1641.28 MB/s | 7.6921 | 126.54 | - | - | - | - | - | - |
| Gzip L8 | 10.00 MB | 55.20 KB | 185.52x | 36.53 | 5.62 | 273.75 MB/s | 1780.25 MB/s | 7.6700 | 126.54 | - | - | - | - | - | - |
| Gzip L9 | 10.00 MB | 55.20 KB | 185.52x | 36.49 | 5.57 | 274.08 MB/s | 1794.24 MB/s | 7.6878 | 126.54 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 13.79% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.201540)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: mixed_payload_xlarge

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 10.00 MB | 65.00 B | 161319.38x | 5.89 | 0.24 | 1698.94 MB/s | 41582.46 MB/s | 7.9420 | 126.54 | 65 | ❌ | 0.067139 | 0.050524 | ❌ | ✅ |
| SHA256 | 10.00 MB | 64.00 B | 163840.00x | 7.65 | 0.00 | 1306.37 MB/s | 0.00 MB/s | 7.6548 | 126.54 | - | - | - | - | - | - |
| AES-GCM | 10.00 MB | 10.00 MB | 1.00x | 4.43 | 4.70 | 2259.73 MB/s | 2125.57 MB/s | 7.7451 | 126.54 | - | - | - | - | - | - |
| Frackture Encrypted | 10.00 MB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 10.00 MB | 270.98 KB | 37.79x | 21.96 | 7.23 | 455.35 MB/s | 1382.79 MB/s | 7.7309 | 126.54 | - | - | - | - | - | - |
| Gzip L2 | 10.00 MB | 240.50 KB | 42.58x | 21.89 | 7.16 | 456.88 MB/s | 1397.41 MB/s | 7.7208 | 126.54 | - | - | - | - | - | - |
| Gzip L3 | 10.00 MB | 143.12 KB | 71.55x | 18.71 | 6.35 | 534.46 MB/s | 1575.74 MB/s | 7.6986 | 126.54 | - | - | - | - | - | - |
| Gzip L4 | 10.00 MB | 62.33 KB | 164.27x | 35.98 | 5.65 | 277.92 MB/s | 1770.15 MB/s | 7.6947 | 126.54 | - | - | - | - | - | - |
| Gzip L5 | 10.00 MB | 58.60 KB | 174.73x | 34.93 | 5.81 | 286.30 MB/s | 1722.19 MB/s | 7.7055 | 126.54 | - | - | - | - | - | - |
| Gzip L6 | 10.00 MB | 55.77 KB | 183.61x | 35.12 | 5.57 | 284.75 MB/s | 1795.90 MB/s | 7.7292 | 126.54 | - | - | - | - | - | - |
| Gzip L7 | 10.00 MB | 55.77 KB | 183.61x | 34.94 | 5.85 | 286.18 MB/s | 1709.65 MB/s | 7.7854 | 126.54 | - | - | - | - | - | - |
| Gzip L8 | 10.00 MB | 55.77 KB | 183.61x | 34.80 | 6.34 | 287.32 MB/s | 1577.17 MB/s | 7.7643 | 126.54 | - | - | - | - | - | - |
| Gzip L9 | 10.00 MB | 55.77 KB | 183.61x | 37.22 | 5.77 | 268.70 MB/s | 1731.83 MB/s | 7.7838 | 126.54 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 24.75% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.067139)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: structured_sqlite_xlarge

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 10.00 MB | 65.00 B | 161319.38x | 5.94 | 0.24 | 1683.24 MB/s | 41169.04 MB/s | 7.8153 | 126.54 | 65 | ❌ | 0.043278 | 0.043278 | ❌ | ✅ |
| SHA256 | 10.00 MB | 64.00 B | 163840.00x | 7.67 | 0.00 | 1304.63 MB/s | 0.00 MB/s | 7.6650 | 126.54 | - | - | - | - | - | - |
| AES-GCM | 10.00 MB | 10.00 MB | 1.00x | 4.79 | 5.06 | 2089.81 MB/s | 1974.95 MB/s | 7.7330 | 126.55 | - | - | - | - | - | - |
| Frackture Encrypted | 10.00 MB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 10.00 MB | 57.39 KB | 178.43x | 17.37 | 6.08 | 575.71 MB/s | 1643.96 MB/s | 7.7163 | 126.55 | - | - | - | - | - | - |
| Gzip L2 | 10.00 MB | 57.38 KB | 178.45x | 16.80 | 5.93 | 595.08 MB/s | 1686.25 MB/s | 8.1887 | 126.05 | - | - | - | - | - | - |
| Gzip L3 | 10.00 MB | 54.42 KB | 188.16x | 17.32 | 5.76 | 577.31 MB/s | 1737.46 MB/s | 7.6938 | 126.11 | - | - | - | - | - | - |
| Gzip L4 | 10.00 MB | 21.06 KB | 486.13x | 34.91 | 11.07 | 286.49 MB/s | 903.06 MB/s | 7.6868 | 126.11 | - | - | - | - | - | - |
| Gzip L5 | 10.00 MB | 21.06 KB | 486.17x | 33.77 | 12.18 | 296.11 MB/s | 820.73 MB/s | 7.6886 | 126.11 | - | - | - | - | - | - |
| Gzip L6 | 10.00 MB | 19.09 KB | 536.27x | 33.60 | 9.58 | 297.60 MB/s | 1043.91 MB/s | 7.7081 | 126.11 | - | - | - | - | - | - |
| Gzip L7 | 10.00 MB | 19.09 KB | 536.27x | 34.90 | 8.05 | 286.52 MB/s | 1241.65 MB/s | 7.7832 | 126.11 | - | - | - | - | - | - |
| Gzip L8 | 10.00 MB | 19.09 KB | 536.27x | 42.07 | 9.20 | 237.70 MB/s | 1087.20 MB/s | 7.7116 | 126.11 | - | - | - | - | - | - |
| Gzip L9 | 10.00 MB | 19.09 KB | 536.27x | 64.02 | 8.89 | 156.19 MB/s | 1124.72 MB/s | 7.7561 | 126.11 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 0.00% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.043278)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: text_plain_xlarge

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 10.00 MB | 65.00 B | 161319.38x | 6.03 | 0.27 | 1657.22 MB/s | 37650.18 MB/s | 7.7541 | 126.90 | 65 | ❌ | 0.313108 | 0.244711 | ❌ | ✅ |
| SHA256 | 10.00 MB | 64.00 B | 163840.00x | 7.67 | 0.00 | 1303.96 MB/s | 0.00 MB/s | 7.6689 | 126.90 | - | - | - | - | - | - |
| AES-GCM | 10.00 MB | 10.00 MB | 1.00x | 4.48 | 5.13 | 2229.90 MB/s | 1948.86 MB/s | 7.7191 | 126.90 | - | - | - | - | - | - |
| Frackture Encrypted | 10.00 MB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 10.00 MB | 86.19 KB | 118.81x | 18.02 | 6.07 | 554.91 MB/s | 1646.74 MB/s | 7.7397 | 126.90 | - | - | - | - | - | - |
| Gzip L2 | 10.00 MB | 78.82 KB | 129.91x | 16.92 | 5.66 | 591.18 MB/s | 1765.81 MB/s | 7.6960 | 126.90 | - | - | - | - | - | - |
| Gzip L3 | 10.00 MB | 81.20 KB | 126.11x | 17.17 | 5.71 | 582.28 MB/s | 1752.51 MB/s | 7.7044 | 126.90 | - | - | - | - | - | - |
| Gzip L4 | 10.00 MB | 50.07 KB | 204.53x | 34.99 | 5.79 | 285.77 MB/s | 1728.10 MB/s | 7.7291 | 126.90 | - | - | - | - | - | - |
| Gzip L5 | 10.00 MB | 50.06 KB | 204.54x | 34.15 | 5.87 | 292.86 MB/s | 1702.67 MB/s | 7.8528 | 126.90 | - | - | - | - | - | - |
| Gzip L6 | 10.00 MB | 50.06 KB | 204.54x | 37.92 | 5.96 | 263.73 MB/s | 1677.24 MB/s | 7.7576 | 126.90 | - | - | - | - | - | - |
| Gzip L7 | 10.00 MB | 50.06 KB | 204.54x | 37.75 | 5.73 | 264.89 MB/s | 1746.22 MB/s | 7.7178 | 126.90 | - | - | - | - | - | - |
| Gzip L8 | 10.00 MB | 50.06 KB | 204.54x | 34.74 | 5.71 | 287.83 MB/s | 1751.28 MB/s | 7.6967 | 126.90 | - | - | - | - | - | - |
| Gzip L9 | 10.00 MB | 50.06 KB | 204.54x | 34.87 | 5.75 | 286.77 MB/s | 1739.02 MB/s | 7.7896 | 126.90 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 21.84% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.313108)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: text_log_xlarge

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 10.00 MB | 65.00 B | 161319.38x | 6.30 | 0.32 | 1588.20 MB/s | 31251.46 MB/s | 7.7216 | 126.90 | 65 | ❌ | 0.199651 | 0.123128 | ❌ | ✅ |
| SHA256 | 10.00 MB | 64.00 B | 163840.00x | 7.65 | 0.00 | 1307.36 MB/s | 0.00 MB/s | 7.6490 | 126.90 | - | - | - | - | - | - |
| AES-GCM | 10.00 MB | 10.00 MB | 1.00x | 4.83 | 4.94 | 2072.13 MB/s | 2022.29 MB/s | 7.6807 | 126.90 | - | - | - | - | - | - |
| Frackture Encrypted | 10.00 MB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 10.00 MB | 94.86 KB | 107.94x | 17.61 | 6.41 | 567.83 MB/s | 1559.62 MB/s | 7.7013 | 126.91 | - | - | - | - | - | - |
| Gzip L2 | 10.00 MB | 92.80 KB | 110.35x | 25.62 | 8.10 | 390.34 MB/s | 1235.05 MB/s | 7.6885 | 126.91 | - | - | - | - | - | - |
| Gzip L3 | 10.00 MB | 94.86 KB | 107.95x | 17.14 | 6.07 | 583.52 MB/s | 1647.25 MB/s | 7.7105 | 126.91 | - | - | - | - | - | - |
| Gzip L4 | 10.00 MB | 84.85 KB | 120.68x | 34.18 | 7.55 | 292.57 MB/s | 1323.89 MB/s | 7.7498 | 126.91 | - | - | - | - | - | - |
| Gzip L5 | 10.00 MB | 56.30 KB | 181.89x | 34.85 | 6.24 | 286.93 MB/s | 1602.67 MB/s | 7.6917 | 126.91 | - | - | - | - | - | - |
| Gzip L6 | 10.00 MB | 56.30 KB | 181.89x | 38.87 | 6.43 | 257.28 MB/s | 1555.24 MB/s | 7.6886 | 126.91 | - | - | - | - | - | - |
| Gzip L7 | 10.00 MB | 50.70 KB | 201.99x | 37.69 | 5.81 | 265.33 MB/s | 1721.65 MB/s | 7.6935 | 126.91 | - | - | - | - | - | - |
| Gzip L8 | 10.00 MB | 49.91 KB | 205.19x | 39.54 | 5.70 | 252.92 MB/s | 1755.69 MB/s | 7.7087 | 126.91 | - | - | - | - | - | - |
| Gzip L9 | 10.00 MB | 49.91 KB | 205.19x | 39.59 | 5.74 | 252.61 MB/s | 1741.49 MB/s | 7.7129 | 126.91 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 38.33% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.199651)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: text_json_xlarge

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 10.00 MB | 65.00 B | 161319.38x | 5.86 | 0.24 | 1706.88 MB/s | 41519.62 MB/s | 7.7601 | 126.91 | 65 | ❌ | 0.203007 | 0.142893 | ❌ | ✅ |
| SHA256 | 10.00 MB | 64.00 B | 163840.00x | 7.70 | 0.00 | 1298.70 MB/s | 0.00 MB/s | 7.7000 | 126.91 | - | - | - | - | - | - |
| AES-GCM | 10.00 MB | 10.00 MB | 1.00x | 4.52 | 4.85 | 2212.44 MB/s | 2063.72 MB/s | 7.7621 | 126.91 | - | - | - | - | - | - |
| Frackture Encrypted | 10.00 MB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 10.00 MB | 160.78 KB | 63.69x | 20.20 | 7.13 | 495.15 MB/s | 1402.60 MB/s | 7.8667 | 126.91 | - | - | - | - | - | - |
| Gzip L2 | 10.00 MB | 148.28 KB | 69.06x | 19.40 | 6.34 | 515.58 MB/s | 1577.29 MB/s | 8.0991 | 126.91 | - | - | - | - | - | - |
| Gzip L3 | 10.00 MB | 134.09 KB | 76.36x | 21.28 | 6.71 | 469.82 MB/s | 1489.22 MB/s | 7.7831 | 126.91 | - | - | - | - | - | - |
| Gzip L4 | 10.00 MB | 68.59 KB | 149.30x | 36.83 | 6.51 | 271.54 MB/s | 1536.70 MB/s | 7.8254 | 126.91 | - | - | - | - | - | - |
| Gzip L5 | 10.00 MB | 79.54 KB | 128.74x | 38.65 | 5.98 | 258.74 MB/s | 1671.26 MB/s | 7.7747 | 126.91 | - | - | - | - | - | - |
| Gzip L6 | 10.00 MB | 58.58 KB | 174.79x | 38.51 | 6.70 | 259.70 MB/s | 1492.32 MB/s | 7.8759 | 126.91 | - | - | - | - | - | - |
| Gzip L7 | 10.00 MB | 50.03 KB | 204.70x | 44.26 | 8.08 | 225.92 MB/s | 1237.51 MB/s | 7.7748 | 126.91 | - | - | - | - | - | - |
| Gzip L8 | 10.00 MB | 50.03 KB | 204.70x | 43.30 | 6.12 | 230.95 MB/s | 1634.26 MB/s | 7.9298 | 126.91 | - | - | - | - | - | - |
| Gzip L9 | 10.00 MB | 50.03 KB | 204.70x | 40.20 | 5.76 | 248.76 MB/s | 1735.99 MB/s | 7.7969 | 126.91 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 29.61% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.203007)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ❌ Failed
- **Fault Errors**: Raw empty raised unexpected KeyError: 'Empty payload'

---

## Dataset: text_csv_xlarge

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 10.00 MB | 65.00 B | 161319.38x | 6.67 | 0.25 | 1498.17 MB/s | 39933.23 MB/s | 7.8041 | 126.91 | 65 | ❌ | 0.199575 | 0.188218 | ❌ | ✅ |
| SHA256 | 10.00 MB | 64.00 B | 163840.00x | 7.68 | 0.00 | 1301.64 MB/s | 0.00 MB/s | 7.6826 | 126.91 | - | - | - | - | - | - |
| AES-GCM | 10.00 MB | 10.00 MB | 1.00x | 4.57 | 5.74 | 2186.28 MB/s | 1742.98 MB/s | 7.9788 | 126.91 | - | - | - | - | - | - |
| Frackture Encrypted | 10.00 MB | FAILED | - | - | - | - | - | - | - | - | - | - | - | - | - |
| Gzip L1 | 10.00 MB | 67.96 KB | 150.68x | 23.71 | 8.37 | 421.84 MB/s | 1194.36 MB/s | 7.9744 | 126.91 | - | - | - | - | - | - |
| Gzip L2 | 10.00 MB | 69.74 KB | 146.83x | 18.21 | 6.11 | 549.06 MB/s | 1637.11 MB/s | 7.7534 | 126.91 | - | - | - | - | - | - |
| Gzip L3 | 10.00 MB | 69.72 KB | 146.87x | 16.80 | 5.80 | 595.38 MB/s | 1725.46 MB/s | 7.9158 | 126.91 | - | - | - | - | - | - |
| Gzip L4 | 10.00 MB | 39.92 KB | 256.50x | 33.97 | 5.80 | 294.35 MB/s | 1725.25 MB/s | 7.7684 | 126.91 | - | - | - | - | - | - |
| Gzip L5 | 10.00 MB | 39.92 KB | 256.50x | 35.07 | 5.76 | 285.12 MB/s | 1734.81 MB/s | 7.7829 | 126.91 | - | - | - | - | - | - |
| Gzip L6 | 10.00 MB | 39.92 KB | 256.50x | 40.05 | 5.89 | 249.72 MB/s | 1696.67 MB/s | 7.9409 | 126.91 | - | - | - | - | - | - |
| Gzip L7 | 10.00 MB | 39.92 KB | 256.50x | 40.38 | 5.94 | 247.67 MB/s | 1683.64 MB/s | 7.7512 | 126.04 | - | - | - | - | - | - |
| Gzip L8 | 10.00 MB | 39.92 KB | 256.50x | 34.24 | 5.80 | 292.04 MB/s | 1725.05 MB/s | 7.7260 | 126.10 | - | - | - | - | - | - |
| Gzip L9 | 10.00 MB | 39.92 KB | 256.50x | 34.11 | 5.61 | 293.18 MB/s | 1782.39 MB/s | 7.7244 | 126.10 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=32B, Total=65B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 5.69% improvement over 5 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.199575)
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
