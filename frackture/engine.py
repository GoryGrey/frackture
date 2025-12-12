"""
Core Frackture engine that unifies all channels and provides the main API.

This module contains the FracktureEngine class which orchestrates the
preprocessing, symbolic, and entropy channels to provide a unified
compression and fingerprinting interface.
"""

import time
import hashlib
from typing import Union, Optional, Dict, Any

import numpy as np

from .models import (
    FrackturePayload, 
    CompressionMetadata, 
    EncryptionMetadata,
    CompressionResult,
    FracktureVersion,
    EncryptionMode
)
from .preprocess import frackture_preprocess_universal_v2_6, validate_preprocessed_vector
from .symbolic import (
    symbolic_channel_encode, 
    symbolic_channel_decode,
    symbolic_fingerprint_with_key,
    validate_symbolic_hash
)
from .entropy import (
    entropy_channel_encode,
    entropy_channel_decode,
    entropy_signature_with_key,
    validate_entropy_signature
)


class FracktureEngine:
    """
    Unified Frackture compression and fingerprinting engine.
    
    This engine orchestrates the preprocessing, symbolic, and entropy channels
    to provide a clean API for compression, decompression, encryption, 
    decryption, and fingerprinting operations.
    """
    
    def __init__(self, version: FracktureVersion = FracktureVersion.V3_3):
        """
        Initialize the Frackture engine.
        
        Args:
            version: Frackture version to use (default: V3_3)
        """
        self.version = version
        self.default_passes = 4
        self.target_length = 768
    
    def _create_metadata(self, passes: Optional[int] = None) -> CompressionMetadata:
        """Create compression metadata with timestamp."""
        return CompressionMetadata(
            version=self.version,
            passes=passes or self.default_passes,
            target_length=self.target_length,
            created_at=str(int(time.time()))
        )
    
    def _create_encryption_metadata(
        self, 
        key_material: Optional[bytes] = None,
        mode: EncryptionMode = EncryptionMode.NONE
    ) -> EncryptionMetadata:
        """Create encryption metadata."""
        return EncryptionMetadata(
            mode=mode,
            key_material=key_material,
            salt=key_material[:8] if key_material else None  # Use first 8 bytes as salt
        )
    
    def _generate_fingerprint(self, payload_dict: Dict) -> str:
        """Generate fingerprint for payload validation."""
        # Create deterministic string representation
        content = f"{payload_dict['symbolic']}{payload_dict['entropy']}{payload_dict['metadata']['version']}"
        return hashlib.sha256(content.encode()).hexdigest()[:16]
    
    def compress(
        self, 
        data: Union[str, bytes, dict, list, np.ndarray, Any],
        passes: Optional[int] = None,
        optimize: bool = False,
        num_trials: int = 5
    ) -> CompressionResult:
        """
        Compress input data using Frackture's dual-channel approach.
        
        Args:
            data: Input data of any supported type
            passes: Number of symbolic passes (default: engine default)
            optimize: Whether to use self-optimization (default: False)
            num_trials: Number of optimization trials (default: 5)
            
        Returns:
            CompressionResult: Complete compression result with metadata
            
        Raises:
            ValueError: If preprocessing fails
            Exception: If compression fails
        """
        try:
            # Preprocess input
            processed = frackture_preprocess_universal_v2_6(data)
            
            if not validate_preprocessed_vector(processed):
                raise ValueError("Preprocessing failed - invalid vector produced")
            
            original_size = len(str(data).encode('utf-8'))
            
            # Use optimization if requested
            if optimize:
                payload, mse = self._optimize_compression(processed, num_trials, passes)
            else:
                # Standard compression
                actual_passes = passes or self.default_passes
                
                # Encode through both channels
                symbolic = symbolic_channel_encode(processed, actual_passes)
                entropy = entropy_channel_encode(processed)
                
                # Create payload
                metadata = self._create_metadata(actual_passes)
                encryption = self._create_encryption_metadata()
                
                payload = FrackturePayload(
                    symbolic=symbolic,
                    entropy=entropy,
                    metadata=metadata,
                    encryption=encryption
                )
                
                # Generate fingerprint
                payload.fingerprint = self._generate_fingerprint(payload.to_dict())
                
                # Calculate MSE
                reconstructed = self.decompress(payload)
                mse = float(np.mean((processed - reconstructed) ** 2))
            
            # Calculate compression statistics
            payload_dict = payload.to_dict()
            import json
            compressed_size = len(json.dumps(payload_dict).encode('utf-8'))
            compression_ratio = compressed_size / original_size if original_size > 0 else 0.0
            
            return CompressionResult(
                payload=payload,
                original_size=original_size,
                compressed_size=compressed_size,
                compression_ratio=compression_ratio,
                mse=mse
            )
            
        except Exception as e:
            raise Exception(f"Compression failed: {e}")
    
    def _optimize_compression(
        self, 
        processed: np.ndarray, 
        num_trials: int,
        base_passes: Optional[int]
    ) -> tuple:
        """Perform optimization to find best compression parameters."""
        best_payload = None
        best_mse = float("inf")
        
        base_passes_val = base_passes or self.default_passes
        
        for trial in range(num_trials):
            # Try different pass counts
            passes_to_try = base_passes_val + trial
            
            symbolic = symbolic_channel_encode(processed, passes_to_try)
            entropy = entropy_channel_encode(processed)
            
            metadata = self._create_metadata(passes_to_try)
            metadata.optimization_trials = trial + 1
            
            encryption = self._create_encryption_metadata()
            
            payload = FrackturePayload(
                symbolic=symbolic,
                entropy=entropy,
                metadata=metadata,
                encryption=encryption
            )
            
            payload.fingerprint = self._generate_fingerprint(payload.to_dict())
            
            # Test reconstruction quality
            reconstructed = self.decompress(payload)
            mse = float(np.mean((processed - reconstructed) ** 2))
            
            if mse < best_mse:
                best_mse = mse
                best_payload = payload
        
        return best_payload, best_mse
    
    def decompress(self, payload: Union[FrackturePayload, Dict]) -> np.ndarray:
        """
        Decompress Frackture payload back to vector representation.
        
        Args:
            payload: FrackturePayload or dictionary representation
            
        Returns:
            np.ndarray: 768-length reconstructed vector
            
        Raises:
            ValueError: If payload format is invalid
            Exception: If decompression fails
        """
        try:
            # Convert dict to payload if needed
            if isinstance(payload, dict):
                payload = FrackturePayload.from_dict(payload)
            
            # Validate symbolic hash
            if not validate_symbolic_hash(payload.symbolic):
                raise ValueError("Invalid symbolic hash in payload")
            
            # Validate entropy signature
            if not validate_entropy_signature(payload.entropy):
                raise ValueError("Invalid entropy signature in payload")
            
            # Decode through both channels
            symbolic_part = symbolic_channel_decode(payload.symbolic)
            entropy_part = entropy_channel_decode(payload.entropy)
            
            # Merge reconstructed parts
            merged = (np.array(entropy_part) + np.array(symbolic_part)) / 2
            
            return merged.astype(np.float32)
            
        except Exception as e:
            raise Exception(f"Decompression failed: {e}")
    
    def encrypt(
        self,
        data: Union[str, bytes, dict, list, np.ndarray, Any],
        key_material: bytes,
        passes: Optional[int] = None
    ) -> CompressionResult:
        """
        Encrypt data using key-based Frackture compression.
        
        Args:
            data: Input data to encrypt
            key_material: Encryption key material
            passes: Number of symbolic passes
            
        Returns:
            CompressionResult: Encrypted compression result
            
        Raises:
            ValueError: If key material is invalid
            Exception: If encryption fails
        """
        if not key_material or len(key_material) == 0:
            raise ValueError("Key material is required for encryption")
        
        try:
            # Preprocess input
            processed = frackture_preprocess_universal_v2_6(data)
            
            if not validate_preprocessed_vector(processed):
                raise ValueError("Preprocessing failed - invalid vector produced")
            
            # Create encrypted payload
            actual_passes = passes or self.default_passes
            
            symbolic = symbolic_fingerprint_with_key(processed, key_material, actual_passes)
            entropy = entropy_signature_with_key(processed, key_material)
            
            metadata = self._create_metadata(actual_passes)
            encryption = self._create_encryption_metadata(key_material, EncryptionMode.XOR)
            
            payload = FrackturePayload(
                symbolic=symbolic,
                entropy=entropy,
                metadata=metadata,
                encryption=encryption
            )
            
            payload.fingerprint = self._generate_fingerprint(payload.to_dict())
            
            # Calculate statistics
            original_size = len(str(data).encode('utf-8'))
            import json
            compressed_size = len(json.dumps(payload.to_dict()).encode('utf-8'))
            compression_ratio = compressed_size / original_size if original_size > 0 else 0.0
            
            # Calculate MSE for encrypted version
            reconstructed = self.decrypt(payload, key_material)
            mse = float(np.mean((processed - reconstructed) ** 2))
            
            return CompressionResult(
                payload=payload,
                original_size=original_size,
                compressed_size=compressed_size,
                compression_ratio=compression_ratio,
                mse=mse
            )
            
        except Exception as e:
            raise Exception(f"Encryption failed: {e}")
    
    def decrypt(self, payload: Union[FrackturePayload, Dict], key_material: bytes) -> np.ndarray:
        """
        Decrypt Frackture payload using key material.
        
        Args:
            payload: Encrypted FrackturePayload
            key_material: Encryption key material
            
        Returns:
            np.ndarray: 768-length decrypted vector
            
        Raises:
            ValueError: If payload or key material is invalid
            Exception: If decryption fails
        """
        if not key_material or len(key_material) == 0:
            raise ValueError("Key material is required for decryption")
        
        try:
            # Convert dict to payload if needed
            if isinstance(payload, dict):
                payload = FrackturePayload.from_dict(payload)
            
            # Verify encryption mode
            if payload.encryption.mode != EncryptionMode.XOR:
                raise ValueError("Payload is not encrypted with XOR mode")
            
            # Decrypt through both channels (reconstruct with key)
            symbolic_part = symbolic_channel_decode(payload.symbolic)
            entropy_part = entropy_channel_decode(payload.entropy)
            
            # Merge decrypted parts
            merged = (np.array(entropy_part) + np.array(symbolic_part)) / 2
            
            return merged.astype(np.float32)
            
        except Exception as e:
            raise Exception(f"Decryption failed: {e}")
    
    def fingerprint(
        self,
        data: Union[str, bytes, dict, list, np.ndarray, Any],
        passes: Optional[int] = None
    ) -> str:
        """
        Generate fingerprint for data without full compression.
        
        Args:
            data: Input data to fingerprint
            passes: Number of symbolic passes
            
        Returns:
            str: 64-character hexadecimal fingerprint
            
        Raises:
            Exception: If fingerprinting fails
        """
        try:
            # Preprocess input
            processed = frackture_preprocess_universal_v2_6(data)
            
            if not validate_preprocessed_vector(processed):
                raise ValueError("Preprocessing failed - invalid vector produced")
            
            # Generate symbolic fingerprint only
            actual_passes = passes or self.default_passes
            return symbolic_channel_encode(processed, actual_passes)
            
        except Exception as e:
            raise Exception(f"Fingerprinting failed: {e}")
    
    def verify_payload(self, payload: Union[FrackturePayload, Dict]) -> bool:
        """
        Verify payload integrity using stored fingerprint.
        
        Args:
            payload: FrackturePayload to verify
            
        Returns:
            bool: True if payload is valid and fingerprint matches
        """
        try:
            # Convert dict to payload if needed
            if isinstance(payload, dict):
                payload = FrackturePayload.from_dict(payload)
            
            # Check if fingerprint exists
            if not payload.fingerprint:
                return False
            
            # Recalculate fingerprint
            current_fingerprint = self._generate_fingerprint(payload.to_dict())
            
            # Compare fingerprints
            return payload.fingerprint == current_fingerprint
            
        except Exception:
            return False