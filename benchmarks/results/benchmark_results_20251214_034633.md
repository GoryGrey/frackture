# Frackture Benchmark Results

**Generated:** 2025-12-14 03:46:33
**Enhanced Metrics Version:** 2.0.0

## New Verification Metrics

- **Payload Sizing**: Symbolic bytes, entropy bytes, serialized total, 96B validation
- **Reconstruction Quality**: MSE baseline vs optimized, lossless status
- **Optimization**: MSE improvement percentage, trials count
- **Determinism**: Multiple encoding tests, drift detection
- **Fault Injection**: Payload mutation tests, error handling validation

---

## Dataset: tiny_tiny_text

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 41.00 B | 414.00 B | 0.10x | 6.26 | 0.25 | 0.01 MB/s | 0.15 MB/s | 0.0114 | 67.20 | 414 | ❌ | 0.186650 | 0.186650 | ❌ | ✅ |
| SHA256 | 41.00 B | 32.00 B | 1.28x | 0.01 | 0.00 | 5.14 MB/s | 0.00 MB/s | 0.0076 | 67.20 | - | - | - | - | - | - |
| AES-GCM | 41.00 B | 57.00 B | 0.72x | 1.62 | 0.27 | 0.02 MB/s | 0.15 MB/s | 0.0158 | 67.55 | - | - | - | - | - | - |
| Frackture Encrypted | 41.00 B | 579.00 B | 0.07x | 1.81 | 0.22 | 0.02 MB/s | 0.18 MB/s | 0.0068 | 67.55 | - | - | - | - | - | - |
| Gzip L6 | 41.00 B | 59.00 B | 0.69x | 0.12 | 0.06 | 0.32 MB/s | 0.64 MB/s | 0.0116 | 67.64 | - | - | - | - | - | - |
| Brotli Q6 | 41.00 B | 45.00 B | 0.91x | 1.04 | 0.01 | 0.04 MB/s | 3.09 MB/s | 0.0157 | 68.16 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=128B, Total=414B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 0.00% improvement over 2 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.186650)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ✅ Passed

---

## Dataset: tiny_tiny_json

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 33.00 B | 412.00 B | 0.08x | 8.01 | 0.37 | 0.00 MB/s | 0.09 MB/s | 0.0073 | 68.16 | 412 | ❌ | 0.160084 | 0.160084 | ❌ | ✅ |
| SHA256 | 33.00 B | 32.00 B | 1.03x | 0.01 | 0.00 | 5.74 MB/s | 0.00 MB/s | 0.0055 | 68.16 | - | - | - | - | - | - |
| AES-GCM | 33.00 B | 49.00 B | 0.67x | 0.12 | 0.05 | 0.27 MB/s | 0.65 MB/s | 0.0064 | 68.16 | - | - | - | - | - | - |
| Frackture Encrypted | 33.00 B | 577.00 B | 0.06x | 1.20 | 0.13 | 0.03 MB/s | 0.24 MB/s | 0.0049 | 68.16 | - | - | - | - | - | - |
| Gzip L6 | 33.00 B | 51.00 B | 0.65x | 0.09 | 0.04 | 0.34 MB/s | 0.78 MB/s | 0.0070 | 68.23 | - | - | - | - | - | - |
| Brotli Q6 | 33.00 B | 36.00 B | 0.92x | 0.16 | 0.02 | 0.20 MB/s | 1.97 MB/s | 0.0066 | 68.45 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=128B, Total=412B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 0.00% improvement over 2 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.160084)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ✅ Passed

---

## Dataset: tiny_tiny_binary

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 10.00 B | 413.00 B | 0.02x | 4.83 | 0.26 | 0.00 MB/s | 0.04 MB/s | 0.0063 | 68.46 | 413 | ❌ | 0.152638 | 0.152638 | ❌ | ✅ |
| SHA256 | 10.00 B | 32.00 B | 0.31x | 0.00 | 0.00 | 2.87 MB/s | 0.00 MB/s | 0.0033 | 68.46 | - | - | - | - | - | - |
| AES-GCM | 10.00 B | 26.00 B | 0.38x | 0.11 | 0.05 | 0.09 MB/s | 0.21 MB/s | 0.0048 | 68.46 | - | - | - | - | - | - |
| Frackture Encrypted | 10.00 B | 578.00 B | 0.02x | 1.16 | 0.13 | 0.01 MB/s | 0.07 MB/s | 0.0045 | 68.46 | - | - | - | - | - | - |
| Gzip L6 | 10.00 B | 30.00 B | 0.33x | 0.06 | 0.03 | 0.15 MB/s | 0.31 MB/s | 0.0055 | 68.50 | - | - | - | - | - | - |
| Brotli Q6 | 10.00 B | 14.00 B | 0.71x | 0.09 | 0.01 | 0.11 MB/s | 1.15 MB/s | 0.0077 | 68.55 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=128B, Total=413B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 0.00% improvement over 2 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.152638)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ✅ Passed

---

## Dataset: tiny_tiny_random

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 50.00 B | 410.00 B | 0.12x | 4.91 | 0.29 | 0.01 MB/s | 0.17 MB/s | 0.0064 | 68.56 | 410 | ❌ | 0.138932 | 0.138932 | ❌ | ✅ |
| SHA256 | 50.00 B | 32.00 B | 1.56x | 0.00 | 0.00 | 13.06 MB/s | 0.00 MB/s | 0.0037 | 68.56 | - | - | - | - | - | - |
| AES-GCM | 50.00 B | 66.00 B | 0.76x | 0.13 | 0.05 | 0.38 MB/s | 1.01 MB/s | 0.0060 | 68.56 | - | - | - | - | - | - |
| Frackture Encrypted | 50.00 B | 575.00 B | 0.09x | 1.29 | 0.15 | 0.04 MB/s | 0.31 MB/s | 0.0051 | 68.56 | - | - | - | - | - | - |
| Gzip L6 | 50.00 B | 73.00 B | 0.68x | 0.07 | 0.03 | 0.71 MB/s | 1.54 MB/s | 0.0068 | 68.59 | - | - | - | - | - | - |
| Brotli Q6 | 50.00 B | 54.00 B | 0.93x | 0.19 | 0.01 | 0.25 MB/s | 5.97 MB/s | 0.0075 | 68.84 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=128B, Total=410B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 0.00% improvement over 2 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.138932)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ✅ Passed

---

## Dataset: tiny_tiny_repetitive

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 50.00 B | 346.00 B | 0.14x | 4.97 | 0.21 | 0.01 MB/s | 0.23 MB/s | 0.0062 | 68.84 | 346 | ❌ | 0.175098 | 0.175098 | ❌ | ✅ |
| SHA256 | 50.00 B | 32.00 B | 1.56x | 0.00 | 0.00 | 13.61 MB/s | 0.00 MB/s | 0.0035 | 68.84 | - | - | - | - | - | - |
| AES-GCM | 50.00 B | 66.00 B | 0.76x | 0.10 | 0.05 | 0.47 MB/s | 1.03 MB/s | 0.0049 | 68.84 | - | - | - | - | - | - |
| Frackture Encrypted | 50.00 B | 511.00 B | 0.10x | 1.30 | 0.12 | 0.04 MB/s | 0.39 MB/s | 0.0047 | 68.84 | - | - | - | - | - | - |
| Gzip L6 | 50.00 B | 25.00 B | 2.00x | 0.05 | 0.03 | 0.87 MB/s | 1.52 MB/s | 0.0055 | 68.86 | - | - | - | - | - | - |
| Brotli Q6 | 50.00 B | 11.00 B | 4.55x | 0.06 | 0.01 | 0.76 MB/s | 3.94 MB/s | 0.0073 | 68.90 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=128B, Total=346B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 0.00% improvement over 2 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.175098)
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
