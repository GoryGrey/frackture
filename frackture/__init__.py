"""
Frackture - Symbolic compression and fingerprinting engine.

This package provides a unified API for data compression, encryption,
and fingerprinting using a dual-channel approach combining symbolic
and entropy channels.

Basic Usage:
    from frackture import compress, decompress
    
    data = b"Hello world"
    compressed = compress(data)
    original = decompress(compressed)

Advanced Usage:
    from frackture import FracktureEngine
    
    engine = FracktureEngine()
    result = engine.compress(data, optimize=True)
    vector = engine.decompress(result.payload)
    
    # For encryption
    encrypted = engine.encrypt(data, key_material=b"my-secret-key")
    decrypted = engine.decrypt(encrypted.payload, key_material=b"my-secret-key")
    
    # For fingerprinting only
    fingerprint = engine.fingerprint(data)
"""

# Version information
__version__ = "3.3.0"
__author__ = "Frackture Development Team"

# Import public API
from .engine import FracktureEngine
from .models import (
    FrackturePayload,
    CompressionMetadata,
    EncryptionMetadata,
    CompressionResult,
    FracktureVersion,
    EncryptionMode
)

# Import core functions for convenience
from .preprocess import frackture_preprocess_universal_v2_6
from .symbolic import (
    symbolic_channel_encode,
    symbolic_channel_decode,
    symbolic_fingerprint_with_key
)
from .entropy import (
    entropy_channel_encode,
    entropy_channel_decode,
    entropy_signature_with_key
)

# Global engine instance for convenience functions
_global_engine = FracktureEngine()


def compress(
    data,
    passes: int = None,
    optimize: bool = False,
    num_trials: int = 5
):
    """
    Compress data using Frackture's default engine.
    
    Args:
        data: Input data of any supported type
        passes: Number of symbolic passes (default: 4)
        optimize: Whether to use optimization (default: False)
        num_trials: Number of optimization trials (default: 5)
        
    Returns:
        dict: Serialized FrackturePayload containing compressed data
        
    Example:
        >>> data = b"Hello world"
        >>> result = compress(data)
        >>> print(result['symbolic'])  # 64-char hex fingerprint
        >>> print(len(result['entropy']))  # 16 entropy components
    """
    result = _global_engine.compress(data, passes, optimize, num_trials)
    return result.payload.to_dict()


def decompress(payload):
    """
    Decompress Frackture payload to vector representation.
    
    Args:
        payload: FrackturePayload (dict or object) to decompress
        
    Returns:
        np.ndarray: 768-length reconstructed vector
        
    Example:
        >>> payload = {'symbolic': '...', 'entropy': [...]}
        >>> vector = decompress(payload)
        >>> print(len(vector))  # 768
    """
    return _global_engine.decompress(payload)


def encrypt(data, key_material: bytes, passes: int = None):
    """
    Encrypt data using key-based Frackture compression.
    
    Args:
        data: Input data to encrypt
        key_material: Encryption key material (bytes)
        passes: Number of symbolic passes (default: 4)
        
    Returns:
        dict: Serialized encrypted FrackturePayload
        
    Example:
        >>> data = b"Secret message"
        >>> key = b"my-encryption-key"
        >>> encrypted = encrypt(data, key)
        >>> print(encrypted['encryption']['mode'])  # 'xor'
    """
    result = _global_engine.encrypt(data, key_material, passes)
    return result.payload.to_dict()


def decrypt(payload, key_material: bytes):
    """
    Decrypt Frackture payload using key material.
    
    Args:
        payload: Encrypted FrackturePayload (dict or object)
        key_material: Encryption key material (bytes)
        
    Returns:
        np.ndarray: 768-length decrypted vector
        
    Example:
        >>> encrypted_payload = {...}  # From encrypt()
        >>> key = b"my-encryption-key"
        >>> vector = decrypt(encrypted_payload, key)
    """
    return _global_engine.decrypt(payload, key_material)


def fingerprint(data, passes: int = None):
    """
    Generate fingerprint for data without full compression.
    
    Args:
        data: Input data to fingerprint
        passes: Number of symbolic passes (default: 4)
        
    Returns:
        str: 64-character hexadecimal fingerprint
        
    Example:
        >>> data = b"Test data"
        >>> fp = fingerprint(data)
        >>> print(len(fp))  # 64
        >>> print(fp[:16])  # First 16 characters
    """
    return _global_engine.fingerprint(data, passes)


def verify_payload(payload) -> bool:
    """
    Verify payload integrity using stored fingerprint.
    
    Args:
        payload: FrackturePayload (dict or object) to verify
        
    Returns:
        bool: True if payload is valid and fingerprint matches
        
    Example:
        >>> payload = {...}  # Some payload
        >>> is_valid = verify_payload(payload)
        >>> if is_valid:
        ...     print("Payload is valid")
    """
    return _global_engine.verify_payload(payload)


def get_version() -> str:
    """
    Get current Frackture version.
    
    Returns:
        str: Version string
    """
    return __version__


def create_engine(version=None):
    """
    Create a new FracktureEngine instance.
    
    Args:
        version: Frackture version to use (default: current)
        
    Returns:
        FracktureEngine: New engine instance
        
    Example:
        >>> engine = create_engine()
        >>> result = engine.compress("test data")
    """
    if version is None:
        return FracktureEngine()
    return FracktureEngine(version)


# Define what gets exported with "from frackture import *"
__all__ = [
    # Core classes
    "FracktureEngine",
    "FrackturePayload", 
    "CompressionMetadata",
    "EncryptionMetadata",
    "CompressionResult",
    "FracktureVersion",
    "EncryptionMode",
    
    # Convenience functions
    "compress",
    "decompress", 
    "encrypt",
    "decrypt",
    "fingerprint",
    "verify_payload",
    "get_version",
    "create_engine",
    
    # Core processing functions
    "frackture_preprocess_universal_v2_6",
    "symbolic_channel_encode",
    "symbolic_channel_decode",
    "symbolic_fingerprint_with_key", 
    "entropy_channel_encode",
    "entropy_channel_decode",
    "entropy_signature_with_key",
]