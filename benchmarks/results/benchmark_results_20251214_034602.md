# Frackture Benchmark Results

**Generated:** 2025-12-14 03:46:02
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
| Frackture | 41.00 B | 414.00 B | 0.10x | 6.60 | 0.33 | 0.01 MB/s | 0.12 MB/s | 0.0078 | 67.13 | 414 | ❌ | 0.186650 | 0.186650 | ❌ | ✅ |
| SHA256 | 41.00 B | 32.00 B | 1.28x | 0.00 | 0.00 | 9.41 MB/s | 0.00 MB/s | 0.0042 | 67.13 | - | - | - | - | - | - |
| AES-GCM | 41.00 B | 57.00 B | 0.72x | 1.27 | 0.23 | 0.03 MB/s | 0.17 MB/s | 0.0105 | 67.48 | - | - | - | - | - | - |
| Frackture Encrypted | 41.00 B | 579.00 B | 0.07x | 1.13 | 0.12 | 0.03 MB/s | 0.32 MB/s | 0.0049 | 67.49 | - | - | - | - | - | - |
| Gzip L6 | 41.00 B | 59.00 B | 0.69x | 0.10 | 0.08 | 0.38 MB/s | 0.51 MB/s | 0.0070 | 67.57 | - | - | - | - | - | - |
| Brotli Q6 | 41.00 B | 45.00 B | 0.91x | 0.95 | 0.01 | 0.04 MB/s | 4.02 MB/s | 0.0110 | 68.11 | - | - | - | - | - | - |

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
| Frackture | 33.00 B | 412.00 B | 0.08x | 4.78 | 0.22 | 0.01 MB/s | 0.14 MB/s | 0.0068 | 68.12 | 412 | ❌ | 0.160084 | 0.160084 | ❌ | ✅ |
| SHA256 | 33.00 B | 32.00 B | 1.03x | 0.00 | 0.00 | 7.39 MB/s | 0.00 MB/s | 0.0043 | 68.12 | - | - | - | - | - | - |
| AES-GCM | 33.00 B | 49.00 B | 0.67x | 0.13 | 0.05 | 0.24 MB/s | 0.62 MB/s | 0.0061 | 68.12 | - | - | - | - | - | - |
| Frackture Encrypted | 33.00 B | 577.00 B | 0.06x | 1.19 | 0.12 | 0.03 MB/s | 0.26 MB/s | 0.0053 | 68.12 | - | - | - | - | - | - |
| Gzip L6 | 33.00 B | 51.00 B | 0.65x | 0.07 | 0.04 | 0.43 MB/s | 0.84 MB/s | 0.0057 | 68.19 | - | - | - | - | - | - |
| Brotli Q6 | 33.00 B | 36.00 B | 0.92x | 0.15 | 0.01 | 0.20 MB/s | 2.22 MB/s | 0.0070 | 68.42 | - | - | - | - | - | - |

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
| Frackture | 10.00 B | 413.00 B | 0.02x | 4.86 | 0.21 | 0.00 MB/s | 0.05 MB/s | 0.0060 | 68.42 | 413 | ❌ | 0.152638 | 0.152638 | ❌ | ✅ |
| SHA256 | 10.00 B | 32.00 B | 0.31x | 0.00 | 0.00 | 2.69 MB/s | 0.00 MB/s | 0.0035 | 68.42 | - | - | - | - | - | - |
| AES-GCM | 10.00 B | 26.00 B | 0.38x | 0.09 | 0.05 | 0.10 MB/s | 0.18 MB/s | 0.0054 | 68.42 | - | - | - | - | - | - |
| Frackture Encrypted | 10.00 B | 578.00 B | 0.02x | 1.17 | 0.12 | 0.01 MB/s | 0.08 MB/s | 0.0043 | 68.42 | - | - | - | - | - | - |
| Gzip L6 | 10.00 B | 30.00 B | 0.33x | 0.06 | 0.03 | 0.15 MB/s | 0.31 MB/s | 0.0058 | 68.46 | - | - | - | - | - | - |
| Brotli Q6 | 10.00 B | 14.00 B | 0.71x | 0.08 | 0.01 | 0.13 MB/s | 1.43 MB/s | 0.0064 | 68.54 | - | - | - | - | - | - |

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
| Frackture | 50.00 B | 411.00 B | 0.12x | 4.75 | 0.21 | 0.01 MB/s | 0.23 MB/s | 0.0063 | 68.54 | 411 | ❌ | 0.139928 | 0.139928 | ❌ | ✅ |
| SHA256 | 50.00 B | 32.00 B | 1.56x | 0.00 | 0.00 | 14.58 MB/s | 0.00 MB/s | 0.0033 | 68.54 | - | - | - | - | - | - |
| AES-GCM | 50.00 B | 66.00 B | 0.76x | 0.09 | 0.05 | 0.51 MB/s | 0.91 MB/s | 0.0059 | 68.54 | - | - | - | - | - | - |
| Frackture Encrypted | 50.00 B | 576.00 B | 0.09x | 1.12 | 0.16 | 0.04 MB/s | 0.31 MB/s | 0.0047 | 68.54 | - | - | - | - | - | - |
| Gzip L6 | 50.00 B | 73.00 B | 0.68x | 0.09 | 0.03 | 0.55 MB/s | 1.47 MB/s | 0.0070 | 68.58 | - | - | - | - | - | - |
| Brotli Q6 | 50.00 B | 54.00 B | 0.93x | 0.24 | 0.01 | 0.20 MB/s | 6.44 MB/s | 0.0092 | 68.85 | - | - | - | - | - | - |

### Frackture Verification Details

- **Payload Sizing**: Symbolic=32B, Entropy=128B, Total=411B
- **96B Target**: ❌ Missed (target: ~96B)
- **Optimization**: 0.00% improvement over 2 trials
- **Reconstruction**: ❌ Lossy (MSE: 0.139928)
- **Determinism**: ✅ Deterministic
- **Fault Injection**: ✅ Passed

---

## Dataset: tiny_tiny_repetitive

### Performance & Verification Metrics

| Method | Original | Compressed | Ratio | Encode (ms) | Decode (ms) | Enc Speed | Dec Speed | Hash (ms) | Mem (MB) | Payload (B) | 96B? | MSE Baseline | MSE Optimized | Lossless? | Deterministic? |
|--------|----------|------------|-------|-------------|-------------|-----------|-----------|-----------|----------|-------------|------|--------------|---------------|-----------|-----------------|
| Frackture | 50.00 B | 346.00 B | 0.14x | 4.73 | 0.24 | 0.01 MB/s | 0.20 MB/s | 0.0065 | 68.85 | 346 | ❌ | 0.175098 | 0.175098 | ❌ | ✅ |
| SHA256 | 50.00 B | 32.00 B | 1.56x | 0.00 | 0.00 | 14.58 MB/s | 0.00 MB/s | 0.0033 | 68.85 | - | - | - | - | - | - |
| AES-GCM | 50.00 B | 66.00 B | 0.76x | 0.09 | 0.04 | 0.51 MB/s | 1.07 MB/s | 0.0050 | 68.85 | - | - | - | - | - | - |
| Frackture Encrypted | 50.00 B | 511.00 B | 0.10x | 1.07 | 0.12 | 0.04 MB/s | 0.40 MB/s | 0.0043 | 68.85 | - | - | - | - | - | - |
| Gzip L6 | 50.00 B | 25.00 B | 2.00x | 0.07 | 0.03 | 0.72 MB/s | 1.53 MB/s | 0.0062 | 68.88 | - | - | - | - | - | - |
| Brotli Q6 | 50.00 B | 11.00 B | 4.55x | 0.09 | 0.01 | 0.55 MB/s | 4.16 MB/s | 0.0083 | 68.91 | - | - | - | - | - | - |

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
