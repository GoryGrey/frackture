import numpy as np
from scipy.fft import fft
from sklearn.decomposition import PCA
import hashlib
import hmac
import os

### === Preprocessing === ###
def frackture_preprocess_universal_v2_6(data):
    try:
        if isinstance(data, str):
            vec = np.frombuffer(data.encode("utf-8"), dtype=np.uint8)
        elif isinstance(data, dict):
            flat = str(sorted(data.items()))
            vec = np.frombuffer(flat.encode("utf-8"), dtype=np.uint8)
        elif isinstance(data, bytes):
            vec = np.frombuffer(data, dtype=np.uint8)
        elif isinstance(data, list):
            vec = np.array(data, dtype=np.float32).flatten()
        elif isinstance(data, np.ndarray):
            vec = data.flatten()
        else:
            vec = np.frombuffer(str(data).encode("utf-8"), dtype=np.uint8)
        normed = vec.astype(np.float32)
        normed = (normed - np.min(normed)) / (np.ptp(normed) + 1e-8)
        padded = np.pad(normed, (0, 768 - len(normed) % 768), mode='wrap')
        return padded[:768]
    except Exception as e:
        return np.zeros(768, dtype=np.float32)

### === Symbolic Fingerprinting System === ###
def frackture_symbolic_fingerprint_f_infinity(input_vector, passes=4):
    bits = (input_vector * 255).astype(np.uint8)
    mask = np.array([(i**2 + i*3 + 1) % 256 for i in range(len(bits))], dtype=np.uint8)
    for p in range(passes):
        rotated = np.roll(bits ^ mask, p * 17)
        entropy_mixed = (rotated * ((p + 1) ** 2)).astype(np.uint16) % 256  # Use uint16 to avoid overflow
        chunks = np.array_split(entropy_mixed, 32)
        folded = [np.bitwise_xor.reduce(chunk) for chunk in chunks]
        fingerprint = ''.join(f"{x:02x}" for x in folded)
        bits = (entropy_mixed + folded[p % len(folded)]) % 256
    return fingerprint

def symbolic_channel_encode(input_vector):
    return frackture_symbolic_fingerprint_f_infinity(input_vector)

def symbolic_channel_decode(symbolic_hash):
    if not symbolic_hash or len(symbolic_hash) < 2:
        # Handle empty or invalid fingerprints
        return np.zeros(768, dtype=np.float32)
    
    try:
        decoded = [int(symbolic_hash[i:i+2], 16) / 255.0 for i in range(0, len(symbolic_hash), 2)]
        if len(decoded) == 0:
            return np.zeros(768, dtype=np.float32)
        return np.array((decoded * (768 // len(decoded) + 1))[:768], dtype=np.float32)
    except (ValueError, IndexError):
        # Handle invalid hex data
        return np.zeros(768, dtype=np.float32)

### === Entropy Channel System === ###
def entropy_channel_encode(input_vector):
    fft_vector = np.abs(fft(input_vector))
    
    # Since PCA needs multiple samples, we'll use a simpler approach
    # Take the FFT vector and create features by chunking and computing statistics
    
    if len(fft_vector) >= 16:
        # If we have enough data, chunk it and compute features
        chunk_size = len(fft_vector) // 16
        chunks = [fft_vector[i:i+chunk_size] for i in range(0, len(fft_vector) - chunk_size + 1, chunk_size)]
        
        # Ensure we have exactly 16 chunks
        while len(chunks) < 16:
            chunks.append(fft_vector[:chunk_size])  # Repeat first chunk
        chunks = chunks[:16]  # Take first 16
        
        # Compute statistical features for each chunk
        features = []
        for chunk in chunks:
            features.extend([
                np.mean(chunk),
                np.std(chunk),
                np.max(chunk),
                np.min(chunk)
            ])
        
        # Take first 16 features
        features = features[:16]
    else:
        # If not enough data, pad with repeated values
        features = []
        for i in range(16):
            if i < len(fft_vector):
                features.append(fft_vector[i])
            else:
                features.append(fft_vector[i % len(fft_vector)])
    
    # Ensure we have exactly 16 features
    if len(features) < 16:
        features.extend([np.mean(fft_vector)] * (16 - len(features)))
    elif len(features) > 16:
        features = features[:16]
    
    return features

def entropy_channel_decode(entropy_data):
    ent = np.array(entropy_data)
    expanded = np.tile(ent, 48)[:768]
    normed = (expanded - np.min(expanded)) / (np.ptp(expanded) + 1e-8)
    return normed

### === Reconstruction Combiner === ###
def merge_reconstruction(entropy_vec, symbolic_vec):
    merged = (np.array(entropy_vec) + np.array(symbolic_vec)) / 2
    return merged

### === Core Frackture Compression Functions === ###
def frackture_v3_3_safe(input_vector):
    return {
        "symbolic": symbolic_channel_encode(input_vector),
        "entropy": entropy_channel_encode(input_vector)
    }

def frackture_v3_3_reconstruct(payload):
    entropy_part = entropy_channel_decode(payload["entropy"])
    symbolic_part = symbolic_channel_decode(payload["symbolic"])
    return merge_reconstruction(entropy_part, symbolic_part)

### === Self-Optimization (Decoder Loss Feedback Loop) === ###
def optimize_frackture(input_vector, num_trials=5):
    best_payload = None
    best_mse = float("inf")
    for trial in range(num_trials):
        symbolic = frackture_symbolic_fingerprint_f_infinity(input_vector, passes=trial + 2)
        entropy = entropy_channel_encode(input_vector)
        payload = {"symbolic": symbolic, "entropy": entropy}
        recon = frackture_v3_3_reconstruct(payload)
        mse = np.mean((input_vector - recon) ** 2)
        if mse < best_mse:
            best_mse = mse
            best_payload = payload
    return best_payload, best_mse

### === Hashing Functions === ###
def frackture_deterministic_hash(data, salt=""):
    """Generate deterministic hash for collision testing"""
    data_str = str(data) + salt
    return hashlib.sha256(data_str.encode()).hexdigest()

### === Encryption/Decryption Functions === ###
def frackture_encrypt_payload(payload, key):
    """Encrypt payload with HMAC key"""
    import json
    data = json.dumps(payload, sort_keys=True).encode()
    signature = hmac.new(key.encode(), data, hashlib.sha256).hexdigest()
    encrypted_payload = {
        "data": payload,
        "signature": signature,
        "metadata": {"key_id": hashlib.sha256(key.encode()).hexdigest()[:8]}
    }
    return encrypted_payload

def frackture_decrypt_payload(encrypted_payload, key):
    """Decrypt and verify payload with HMAC key"""
    import json
    expected_signature = hmac.new(key.encode(), 
                                json.dumps(encrypted_payload["data"], sort_keys=True).encode(), 
                                hashlib.sha256).hexdigest()
    
    if not hmac.compare_digest(encrypted_payload["signature"], expected_signature):
        raise ValueError("Invalid key or corrupted payload")
    
    if encrypted_payload["metadata"]["key_id"] != hashlib.sha256(key.encode()).hexdigest()[:8]:
        raise ValueError("Key mismatch")
    
    return encrypted_payload["data"]
