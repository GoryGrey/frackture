"""Core Frackture compression and encoding functionality."""

import numpy as np
from scipy.fft import fft

# === Preprocessing ===


def frackture_preprocess_universal_v2_6(data):
    """Preprocess universal data types into a normalized 768-length vector.

    Handles strings, dicts, bytes, lists, and numpy arrays.
    """
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
        padded = np.pad(normed, (0, 768 - len(normed) % 768), mode="wrap")
        return padded[:768]
    except Exception:
        return np.zeros(768, dtype=np.float32)


# === Symbolic Fingerprinting System ===
def frackture_symbolic_fingerprint_f_infinity(input_vector, passes=4):
    """Generate symbolic fingerprint via recursive XOR/masking.

    Creates an identity-preserving hash using bitwise operations.
    """
    bits = (input_vector * 255).astype(np.uint8)
    mask = np.array([(i**2 + i * 3 + 1) % 256 for i in range(len(bits))], dtype=np.uint8)
    for p in range(passes):
        rotated = np.roll(bits ^ mask, p * 17)
        entropy_mixed = np.array(((rotated.astype(int) * ((p + 1) ** 2)) % 256), dtype=np.uint8)
        chunks = np.array_split(entropy_mixed, 32)
        folded = [np.bitwise_xor.reduce(chunk) for chunk in chunks]
        fingerprint = "".join(f"{x:02x}" for x in folded)
        bits = np.array(
            ((entropy_mixed.astype(int) + folded[p % len(folded)]) % 256),
            dtype=np.uint8,
        )
    return fingerprint


def symbolic_channel_encode(input_vector):
    """Encode input vector to symbolic fingerprint."""
    return frackture_symbolic_fingerprint_f_infinity(input_vector)


def symbolic_channel_decode(symbolic_hash):
    """Decode symbolic hash back to vector form."""
    decoded = [int(symbolic_hash[i : i + 2], 16) / 255.0 for i in range(0, len(symbolic_hash), 2)]
    return np.array((decoded * (768 // len(decoded) + 1))[:768], dtype=np.float32)


# === Entropy Channel System ===
def entropy_channel_encode(input_vector):
    """Encode input vector via FFT and dimensionality reduction."""
    fft_vector = np.abs(fft(input_vector))
    # Divide FFT into 16 chunks and take the mean of each
    # This provides dimensionality reduction from 768 to 16
    chunk_size = len(fft_vector) // 16
    chunks = [fft_vector[i * chunk_size : (i + 1) * chunk_size].mean() for i in range(16)]
    return chunks


def entropy_channel_decode(entropy_data):
    """Decode entropy data back to vector form."""
    ent = np.array(entropy_data)
    expanded = np.tile(ent, 48)[:768]
    normed = (expanded - np.min(expanded)) / (np.ptp(expanded) + 1e-8)
    return normed


# === Reconstruction Combiner ===
def merge_reconstruction(entropy_vec, symbolic_vec):
    """Merge entropy and symbolic vectors for reconstruction."""
    merged = (np.array(entropy_vec) + np.array(symbolic_vec)) / 2
    return merged


# === Core Frackture Compression Functions ===
def frackture_v3_3_safe(input_vector):
    """Compress input vector into symbolic and entropy payloads."""
    return {
        "symbolic": symbolic_channel_encode(input_vector),
        "entropy": entropy_channel_encode(input_vector),
    }


def frackture_v3_3_reconstruct(payload):
    """Reconstruct approximation from symbolic and entropy payloads."""
    entropy_part = entropy_channel_decode(payload["entropy"])
    symbolic_part = symbolic_channel_decode(payload["symbolic"])
    return merge_reconstruction(entropy_part, symbolic_part)


# === Self-Optimization (Decoder Loss Feedback Loop) ===
def optimize_frackture(input_vector, num_trials=5):
    """Optimize compression payload over multiple trials.

    Iterates over symbolic passes to minimize reconstruction MSE.
    """
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


# Convenience aliases for user-facing API
def compress(data):
    """Compress data into fixed-size payload.

    Args:
        data: Input data (str, bytes, dict, list, or ndarray)

    Returns:
        dict: Compressed payload with 'symbolic' and 'entropy' channels
    """
    preprocessed = frackture_preprocess_universal_v2_6(data)
    return frackture_v3_3_safe(preprocessed)


def decompress(payload):
    """Decompress fixed-size payload back to approximation.

    Args:
        payload: dict with 'symbolic' and 'entropy' keys

    Returns:
        ndarray: Reconstructed approximation (768-length vector)
    """
    return frackture_v3_3_reconstruct(payload)
