"""
Universal preprocessing module for Frackture.

This module handles converting various input types (strings, bytes, lists, arrays, etc.)
into normalized 768-length vectors that serve as the foundation for all Frackture operations.
"""

import numpy as np
from typing import Union, Any


def frackture_preprocess_universal_v2_6(data: Union[str, bytes, dict, list, np.ndarray, Any]) -> np.ndarray:
    """
    Convert any input data into a normalized 768-length vector.
    
    This universal preprocessing function handles multiple input types:
    - str: Converted to UTF-8 bytes
    - bytes: Used directly  
    - dict: Sorted and converted to string, then UTF-8 bytes
    - list: Converted to float32 array and flattened
    - np.ndarray: Used directly and flattened
    - any other type: Converted to string, then UTF-8 bytes
    
    Args:
        data: Input data of any supported type
        
    Returns:
        np.ndarray: Normalized 768-length float32 vector
        
    Raises:
        Exception: Returns zero vector if preprocessing fails
    """
    try:
        if isinstance(data, str):
            # String input: encode to UTF-8 bytes
            vec = np.frombuffer(data.encode("utf-8"), dtype=np.uint8)
        elif isinstance(data, dict):
            # Dictionary input: sort items, convert to string, encode
            flat = str(sorted(data.items()))
            vec = np.frombuffer(flat.encode("utf-8"), dtype=np.uint8)
        elif isinstance(data, bytes):
            # Bytes input: use directly
            vec = np.frombuffer(data, dtype=np.uint8)
        elif isinstance(data, list):
            # List input: convert to float32 array and flatten
            vec = np.array(data, dtype=np.float32).flatten()
        elif isinstance(data, np.ndarray):
            # NumPy array: flatten (preserve dtype)
            vec = data.flatten()
        else:
            # Any other type: convert to string, then UTF-8 bytes
            vec = np.frombuffer(str(data).encode("utf-8"), dtype=np.uint8)
        
        # Normalize to float32
        normed = vec.astype(np.float32)
        
        # Normalize to [0, 1] range with small epsilon to avoid division by zero
        min_val = np.min(normed)
        max_val = np.max(normed)
        range_val = max_val - min_val + 1e-8
        
        normed = (normed - min_val) / range_val
        
        # Pad or truncate to exactly 768 elements using wrap mode
        if len(normed) < 768:
            # Pad with wrapped values
            padded = np.pad(normed, (0, 768 - len(normed)), mode='wrap')
        else:
            # Truncate if too long
            padded = normed[:768]
        
        return padded
    
    except Exception as e:
        # Return zero vector on any preprocessing error
        return np.zeros(768, dtype=np.float32)


def preprocess_batch(data_list: list) -> np.ndarray:
    """
    Preprocess a batch of data items.
    
    Args:
        data_list: List of data items to preprocess
        
    Returns:
        np.ndarray: Stack of preprocessed vectors (batch_size, 768)
    """
    return np.stack([frackture_preprocess_universal_v2_6(item) for item in data_list])


def validate_preprocessed_vector(vector: np.ndarray) -> bool:
    """
    Validate that a vector is properly preprocessed.
    
    Args:
        vector: Vector to validate
        
    Returns:
        bool: True if vector is valid 768-length float32 array
    """
    return (
        isinstance(vector, np.ndarray) and
        vector.dtype == np.float32 and
        len(vector) == 768 and
        np.all(vector >= 0.0) and
        np.all(vector <= 1.0)
    )