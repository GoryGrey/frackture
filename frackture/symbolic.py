"""
Symbolic fingerprinting module for Frackture.

This module implements the symbolic channel of Frackture, providing
identity-preserving fingerprint generation and reconstruction.
"""

import numpy as np
from typing import Tuple, List


def frackture_symbolic_fingerprint_f_infinity(
    input_vector: np.ndarray, 
    passes: int = 4
) -> str:
    """
    Generate symbolic fingerprint using recursive XOR/masking operations.
    
    This function creates an identity-preserving hash by:
    1. Converting input to 8-bit values
    2. Applying progressive XOR masks and rotations
    3. Chunking and folding operations for compression
    4. Multiple passes for enhanced entropy
    
    Args:
        input_vector: 768-length normalized vector
        passes: Number of recursive passes (default: 4)
        
    Returns:
        str: 64-character hexadecimal fingerprint (32 chunks of 2 hex chars each)
        
    Raises:
        ValueError: If input vector is not 768 elements
    """
    if len(input_vector) != 768:
        raise ValueError(f"Input vector must be 768 elements, got {len(input_vector)}")
    
    # Convert to 8-bit representation
    bits = (input_vector * 255).astype(np.uint8)
    
    # Generate progressive mask based on index
    mask = np.array([
        (i**2 + i*3 + 1) % 256 
        for i in range(len(bits))
    ], dtype=np.uint8)
    
    # Apply recursive passes
    for p in range(passes):
        # Rotate and XOR with mask
        rotated = np.roll(bits ^ mask, p * 17)
        
        # Entropy mixing with pass-dependent scaling (ensure uint8 range)
        scaling = (p + 1) ** 2
        entropy_mixed = (rotated.astype(np.uint16) * scaling) % 256
        
        # Chunk into 32 segments and fold with XOR reduction
        chunks = np.array_split(entropy_mixed, 32)
        folded = [np.bitwise_xor.reduce(chunk) for chunk in chunks]
        
        # Create hexadecimal fingerprint
        fingerprint = ''.join(f"{x:02x}" for x in folded)
        
        # Feed forward for next iteration (ensure uint8 range)
        fold_val = folded[p % len(folded)]
        bits = (entropy_mixed.astype(np.uint16) + fold_val) % 256
    
    return fingerprint


def symbolic_channel_encode(input_vector: np.ndarray, passes: int = 4) -> str:
    """
    Encode input vector through symbolic channel.
    
    Args:
        input_vector: 768-length normalized vector
        passes: Number of fingerprint passes
        
    Returns:
        str: Symbolic fingerprint
    """
    return frackture_symbolic_fingerprint_f_infinity(input_vector, passes)


def symbolic_channel_decode(symbolic_hash: str) -> np.ndarray:
    """
    Decode symbolic hash back to approximate vector representation.
    
    Note: This is not a true inverse operation - it's a best-effort
    reconstruction that preserves some structural properties.
    
    Args:
        symbolic_hash: 64-character hexadecimal fingerprint
        
    Returns:
        np.ndarray: 768-length normalized vector (approximation)
        
    Raises:
        ValueError: If symbolic hash is not valid hex format
    """
    if len(symbolic_hash) != 64:
        raise ValueError(f"Symbolic hash must be 64 characters, got {len(symbolic_hash)}")
    
    try:
        # Convert hex pairs back to [0, 1] range values
        decoded_values = [
            int(symbolic_hash[i:i+2], 16) / 255.0 
            for i in range(0, len(symbolic_hash), 2)
        ]
        
        # Expand to 768 elements by tiling
        repeated = (decoded_values * (768 // len(decoded_values) + 1))[:768]
        
        return np.array(repeated, dtype=np.float32)
    
    except ValueError as e:
        raise ValueError(f"Invalid symbolic hash format: {e}")


def apply_key_based_masking(bits: np.ndarray, key_material: bytes) -> np.ndarray:
    """
    Apply key-based masking to symbolic channel for encryption.
    
    Args:
        bits: Input bit array (uint8)
        key_material: Encryption key material
        
    Returns:
        np.ndarray: Masked bit array
    """
    if not key_material:
        return bits
    
    # Generate mask from key material
    key_mask = np.frombuffer(
        (key_material * (len(bits) // len(key_material) + 1))[:len(bits)],
        dtype=np.uint8
    )
    
    # Ensure uint8 range for masking operation
    # Use bitwise AND with 0xFF to ensure we stay in uint8 range
    masked = (bits.astype(np.uint16) ^ key_mask.astype(np.uint16)) & 0xFF
    return masked.astype(np.uint8)


def symbolic_fingerprint_with_key(
    input_vector: np.ndarray, 
    key_material: bytes,
    passes: int = 4
) -> str:
    """
    Generate symbolic fingerprint with key-based masking for encryption.
    
    Args:
        input_vector: 768-length normalized vector
        key_material: Encryption key material
        passes: Number of fingerprint passes
        
    Returns:
        str: Encrypted symbolic fingerprint
    """
    if len(input_vector) != 768:
        raise ValueError(f"Input vector must be 768 elements, got {len(input_vector)}")
    
    # Convert to 8-bit representation with masking
    bits = (input_vector * 255).astype(np.uint8)
    bits = apply_key_based_masking(bits, key_material)
    
    # Generate mask and apply recursive passes (simplified for encryption)
    mask = np.array([
        (i**2 + i*3 + 1) % 256 
        for i in range(len(bits))
    ], dtype=np.uint8)
    
    for p in range(passes):
        rotated = np.roll(bits ^ mask, p * 17)
        # Entropy mixing with pass-dependent scaling (ensure uint8 range)
        scaling = (p + 1) ** 2
        entropy_mixed = (rotated.astype(np.uint16) * scaling) % 256
        
        chunks = np.array_split(entropy_mixed, 32)
        folded = [np.bitwise_xor.reduce(chunk) for chunk in chunks]
        
        fingerprint = ''.join(f"{x:02x}" for x in folded)
        # Feed forward for next iteration (ensure uint8 range)
        fold_val = folded[p % len(folded)]
        bits = (entropy_mixed.astype(np.uint16) + fold_val) % 256
    
    return fingerprint


def validate_symbolic_hash(symbolic_hash: str) -> bool:
    """
    Validate symbolic hash format.
    
    Args:
        symbolic_hash: Hash string to validate
        
    Returns:
        bool: True if valid 64-character hex string
    """
    try:
        return (
            len(symbolic_hash) == 64 and
            all(c in '0123456789abcdef' for c in symbolic_hash.lower())
        )
    except Exception:
        return False