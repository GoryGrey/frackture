"""
Entropy channel module for Frackture.

This module implements the entropy channel using FFT analysis and PCA
to create frequency-domain signatures that complement the symbolic channel.
"""

import numpy as np
from scipy.fft import fft
from sklearn.decomposition import PCA
from typing import List, Tuple


def entropy_channel_encode(input_vector: np.ndarray) -> List[float]:
    """
    Encode input vector through entropy channel using FFT + PCA.
    
    The entropy channel captures frequency-domain characteristics:
    1. Apply FFT to get frequency spectrum
    2. Use PCA for dimensionality reduction  
    3. Return compact 16-component signature
    
    Args:
        input_vector: 768-length normalized vector
        
    Returns:
        List[float]: 16-component entropy signature
        
    Raises:
        ValueError: If input vector is not 768 elements
    """
    if len(input_vector) != 768:
        raise ValueError(f"Input vector must be 768 elements, got {len(input_vector)}")
    
    # Apply FFT to get frequency spectrum
    fft_vector = np.abs(fft(input_vector))
    
    # For single samples, use statistical summarization instead of PCA
    # This gives us 16 meaningful components without needing multiple samples
    reduced = []
    
    # Split FFT spectrum into 16 segments and compute statistics
    segment_size = len(fft_vector) // 16
    if segment_size == 0:
        # If vector is too small, pad with zeros
        reduced = [0.0] * 16
    else:
        for i in range(16):
            start_idx = i * segment_size
            end_idx = min(start_idx + segment_size, len(fft_vector))
            
            segment = fft_vector[start_idx:end_idx]
            if len(segment) > 0:
                # Use mean and std of segment as features (convert to Python float)
                mean_val = float(np.mean(segment))
                std_val = float(np.std(segment) / 2.0)
                reduced.extend([mean_val, std_val])  # 2 features per segment
            else:
                reduced.extend([0.0, 0.0])
        
        # Take only first 16 components
        reduced = reduced[:16]
        
        # If we got fewer than 16, pad with zeros
        while len(reduced) < 16:
            reduced.append(0.0)
    
    return reduced


def entropy_channel_decode(entropy_data: List[float]) -> np.ndarray:
    """
    Decode entropy signature back to approximate vector representation.
    
    This attempts reconstruction by:
    1. Expanding 16 components to 768 via tiling
    2. Normalizing to [0, 1] range
    
    Args:
        entropy_data: 16-component entropy signature
        
    Returns:
        np.ndarray: 768-length normalized vector (approximation)
        
    Raises:
        ValueError: If entropy data doesn't have 16 components
    """
    if len(entropy_data) != 16:
        raise ValueError(f"Entropy data must have 16 components, got {len(entropy_data)}")
    
    try:
        # Convert to numpy array
        ent = np.array(entropy_data)
        
        # Expand to 768 elements by tiling
        expanded = np.tile(ent, 48)[:768]
        
        # Normalize to [0, 1] range
        min_val = np.min(expanded)
        max_val = np.max(expanded)
        range_val = max_val - min_val + 1e-8
        
        normed = (expanded - min_val) / range_val
        
        return normed.astype(np.float32)
    
    except Exception as e:
        raise ValueError(f"Failed to decode entropy data: {e}")


def compute_frequency_spectrum(input_vector: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """
    Compute full frequency spectrum for analysis.
    
    Args:
        input_vector: 768-length normalized vector
        
    Returns:
        Tuple[np.ndarray, np.ndarray]: (frequencies, magnitudes)
        
    Raises:
        ValueError: If input vector is not 768 elements
    """
    if len(input_vector) != 768:
        raise ValueError(f"Input vector must be 768 elements, got {len(input_vector)}")
    
    # Apply FFT
    fft_result = fft(input_vector)
    
    # Get magnitude spectrum
    magnitudes = np.abs(fft_result)
    
    # Generate frequency bins
    frequencies = np.fft.fftfreq(len(input_vector))
    
    return frequencies, magnitudes


def apply_key_based_spectral_masking(
    frequencies: np.ndarray, 
    key_material: bytes
) -> np.ndarray:
    """
    Apply key-based masking to frequency spectrum for encryption.
    
    Args:
        frequencies: Input frequency magnitudes
        key_material: Encryption key material
        
    Returns:
        np.ndarray: Masked frequency magnitudes
    """
    if not key_material:
        return frequencies
    
    # Generate mask from key material
    key_mask = np.frombuffer(
        (key_material * (len(frequencies) // len(key_material) + 1))[:len(frequencies)],
        dtype=np.uint8
    ).astype(np.float32)
    
    # Ensure uint8 range for masking operation
    # Use bitwise AND with 0xFF to ensure we stay in uint8 range
    masked = ((frequencies.astype(np.uint16) ^ key_mask.astype(np.uint16)) & 0xFF).astype(np.uint8)
    
    # Normalize back to reasonable range
    masked = masked / 255.0
    
    return masked


def entropy_signature_with_key(
    input_vector: np.ndarray,
    key_material: bytes
) -> List[float]:
    """
    Generate entropy signature with key-based masking for encryption.
    
    Args:
        input_vector: 768-length normalized vector
        key_material: Encryption key material
        
    Returns:
        List[float]: 16-component encrypted entropy signature
    """
    if len(input_vector) != 768:
        raise ValueError(f"Input vector must be 768 elements, got {len(input_vector)}")
    
    # Apply FFT
    fft_vector = np.abs(fft(input_vector))
    
    # Apply key-based masking to spectrum
    if key_material:
        fft_vector = apply_key_based_spectral_masking(fft_vector, key_material)
    
    # For single samples, use statistical summarization instead of PCA
    # This gives us 16 meaningful components without needing multiple samples
    reduced = []
    
    # Split FFT spectrum into 16 segments and compute statistics
    segment_size = len(fft_vector) // 16
    if segment_size == 0:
        # If vector is too small, pad with zeros
        reduced = [0.0] * 16
    else:
        for i in range(16):
            start_idx = i * segment_size
            end_idx = min(start_idx + segment_size, len(fft_vector))
            
            segment = fft_vector[start_idx:end_idx]
            if len(segment) > 0:
                # Use mean and std of segment as features (convert to Python float)
                mean_val = float(np.mean(segment))
                std_val = float(np.std(segment) / 2.0)
                reduced.extend([mean_val, std_val])  # 2 features per segment
            else:
                reduced.extend([0.0, 0.0])
        
        # Take only first 16 components
        reduced = reduced[:16]
        
        # If we got fewer than 16, pad with zeros
        while len(reduced) < 16:
            reduced.append(0.0)
    
    return reduced


def validate_entropy_signature(entropy_data: List[float]) -> bool:
    """
    Validate entropy signature format.
    
    Args:
        entropy_data: Signature to validate
        
    Returns:
        bool: True if valid 16-component float list
    """
    try:
        return (
            len(entropy_data) == 16 and
            all(isinstance(x, (int, float, np.number)) and not np.isnan(x) for x in entropy_data)
        )
    except Exception:
        return False