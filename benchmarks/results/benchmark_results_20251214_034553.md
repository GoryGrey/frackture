# Frackture Benchmark Results

**Generated:** 2025-12-14 03:45:53
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
| Frackture | 41.00 B | 414.00 B | 0.10x | 8.90 | 0.28 | 0.00 MB/s | 0.14 MB/s | 0.0120 | 66.94 | 414 | ❌ | 0.186650 | 0.186650 | ❌ | ✅ |
| SHA256 | 41.00 B | 32.00 B | 1.28x | 0.01 | 0.00 | 6.67 MB/s | 0.00 MB/s | 0.0059 | 66.94 | - | - | - | - | - | - |
| AES-GCM | 41.00 B | 57.00 B | 0.72x | 1.60 | 0.23 | 0.02 MB/s | 0.17 MB/s | 0.0125 | 67.29 | - | - | - | - | - | - |
| Frackture Encrypted | 41.00 B | 579.00 B | 0.07x | 1.16 | 0.13 | 0.03 MB/s | 0.29 MB/s | 0.0055 | 67.29 | - | - | - | - | - | - |
| Gzip L6 | 41.00 B | 59.00 B | 0.69x | 0.14 | 0.05 | 0.29 MB/s | 0.78 MB/s | 0.0073 | 67.38 | - | - | - | - | - | - |
| Brotli Q6 | 41.00 B | 45.00 B | 0.91x | 1.08 | 0.01 | 0.04 MB/s | 3.77 MB/s | 0.0137 | 67.90 | - | - | - | - | - | - |

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
| Frackture | 33.00 B | 412.00 B | 0.08x | 5.58 | 0.31 | 0.01 MB/s | 0.10 MB/s | 0.0095 | 67.91 | 412 | ❌ | 0.160084 | 0.160084 | ❌ | ✅ |
| SHA256 | 33.00 B | 32.00 B | 1.03x | 0.00 | 0.00 | 6.63 MB/s | 0.00 MB/s | 0.0047 | 67.91 | - | - | - | - | - | - |
| AES-GCM | 33.00 B | 49.00 B | 0.67x | 0.11 | 0.05 | 0.28 MB/s | 0.64 MB/s | 0.0058 | 67.91 | - | - | - | - | - | - |
| Frackture Encrypted | 33.00 B | 577.00 B | 0.06x | 1.30 | 0.15 | 0.02 MB/s | 0.21 MB/s | 0.0070 | 67.91 | - | - | - | - | - | - |
| Gzip L6 | 33.00 B | 51.00 B | 0.65x | 0.09 | 0.04 | 0.36 MB/s | 0.78 MB/s | 0.0095 | 67.97 | - | - | - | - | - | - |
| Brotli Q6 | 33.00 B | 36.00 B | 0.92x | 0.20 | 0.02 | 0.16 MB/s | 1.61 MB/s | 0.0120 | 68.20 | - | - | - | - | - | - |

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
| Frackture | 10.00 B | 413.00 B | 0.02x | 5.01 | 0.24 | 0.00 MB/s | 0.04 MB/s | 0.0076 | 68.20 | 413 | ❌ | 0.152638 | 0.152638 | ❌ | ✅ |
| SHA256 | 10.00 B | 32.00 B | 0.31x | 0.00 | 0.00 | 2.26 MB/s | 0.00 MB/s | 0.0042 | 68.20 | - | - | - | - | - | - |
| AES-GCM | 10.00 B | 26.00 B | 0.38x | 0.14 | 0.05 | 0.07 MB/s | 0.18 MB/s | 0.0061 | 68.20 | - | - | - | - | - | - |
| Frackture Encrypted | 10.00 B | 578.00 B | 0.02x | 1.15 | 0.13 | 0.01 MB/s | 0.07 MB/s | 0.0044 | 68.20 | - | - | - | - | - | - |
| Gzip L6 | 10.00 B | 30.00 B | 0.33x | 0.06 | 0.03 | 0.15 MB/s | 0.28 MB/s | 0.0060 | 68.26 | - | - | - | - | - | - |
| Brotli Q6 | 10.00 B | 14.00 B | 0.71x | 0.08 | 0.01 | 0.12 MB/s | 1.15 MB/s | 0.0067 | 68.32 | - | - | - | - | - | - |

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
| Frackture | 50.00 B | 406.00 B | 0.12x | 7.60 | 0.30 | 0.01 MB/s | 0.16 MB/s | 0.0074 | 68.33 | 406 | ❌ | 0.107452 | 0.107452 | ❌ | ✅ |
| SHA256 | 50.00 B | 32.00 B | 1.56x | 0.00 | 0.00 | 11.43 MB/s | 0.00 MB/s | 0.0042 | 68.33 | - | - | - | - | - | - |
| AES-GCM | 50.00 B | 66.00 B | 0.76x | 0.13 | 0.10 | 0.36 MB/s | 0.48 MB/s | 0.0088 | 68.33 | - | - | - | - | - | - |
| Frackture Encrypted | 50.00 B | 571.00 B | 0.09x | 1.17 | 0.12 | 0.04 MB/s | 0.38 MB/s | 0.0054 | 68.33 | - | - | - | - | - | - |
| Gzip L6 | 50.00 B | 73.00 B | 0.68x | 0.06 | 0.03 | 0.76 MB/s | 1.60 MB/s | 0.0064 | 68.35 | - | - | - | - | - | - |
| Brotli Q6 | 50.00 B | 54.00 B | 0.93x | 0.24 | 0.02 | 0.20 MB/s | 3.07 MB/s | 0.0091 | 68.63 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=128B, Total=406B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 0.00% improvement over 2 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.107452)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ✅ Passed

---

## Dataset: tiny_tiny_repetitive

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 50.00 B | 346.00 B | 0.14x | 4.85 | 0.29 | 0.01 MB/s | 0.16 MB/s | 0.0065 | 68.63 | 346 | ❌ | 0.175098 | 0.175098 | ❌ | ✅ |
| SHA256 | 50.00 B | 32.00 B | 1.56x | 0.01 | 0.00 | 9.48 MB/s | 0.00 MB/s | 0.0050 | 68.63 | - | - | - | - | - | - |
| AES-GCM | 50.00 B | 66.00 B | 0.76x | 0.13 | 0.07 | 0.36 MB/s | 0.71 MB/s | 0.0088 | 68.63 | - | - | - | - | - | - |
| Frackture Encrypted | 50.00 B | 511.00 B | 0.10x | 1.22 | 0.13 | 0.04 MB/s | 0.38 MB/s | 0.0050 | 68.63 | - | - | - | - | - | - |
| Gzip L6 | 50.00 B | 25.00 B | 2.00x | 0.07 | 0.03 | 0.72 MB/s | 1.44 MB/s | 0.0067 | 68.66 | - | - | - | - | - | - |
| Brotli Q6 | 50.00 B | 11.00 B | 4.55x | 0.07 | 0.01 | 0.64 MB/s | 3.65 MB/s | 0.0072 | 68.70 | - | - | - | - | - | - |

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
