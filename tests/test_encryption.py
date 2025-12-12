"""
Tests for encryption mode and security functionality
"""
import pytest
import numpy as np
import json
import sys
import os
from hypothesis import given, settings
from hypothesis.strategies import text, binary

# Add parent directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

# Import frackture module
try:
    from frackture import (
        frackture_preprocess_universal_v2_6,
        frackture_v3_3_safe,
        frackture_v3_3_reconstruct,
        frackture_encrypt_payload,
        frackture_decrypt_payload,
        frackture_deterministic_hash
    )
except ImportError:
    import importlib.util
    module_path = os.path.join(os.path.dirname(__file__), '..', 'frackture (2).py')
    spec = importlib.util.spec_from_file_location("frackture_2", module_path)
    frackture_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(frackture_module)
    
    frackture_preprocess_universal_v2_6 = frackture_module.frackture_preprocess_universal_v2_6
    frackture_v3_3_safe = frackture_module.frackture_v3_3_safe
    frackture_v3_3_reconstruct = frackture_module.frackture_v3_3_reconstruct
    frackture_encrypt_payload = frackture_module.frackture_encrypt_payload
    frackture_decrypt_payload = frackture_module.frackture_decrypt_payload
    frackture_deterministic_hash = frackture_module.frackture_deterministic_hash

class TestEncryption:
    """Test encryption/decryption functionality"""
    
    def test_encryption_basic_functionality(self, small_data, encryption_keys):
        """Test basic encryption/decryption functionality"""
        # Preprocess and encode
        preprocessed = frackture_preprocess_universal_v2_6(small_data)
        payload = frackture_v3_3_safe(preprocessed)
        
        for key in encryption_keys:
            # Encrypt
            encrypted = frackture_encrypt_payload(payload, key)
            
            # Verify encrypted structure
            assert isinstance(encrypted, dict)
            assert "data" in encrypted
            assert "signature" in encrypted
            assert "metadata" in encrypted
            assert encrypted["data"] == payload
            assert "key_id" in encrypted["metadata"]
            
            # Decrypt with correct key
            decrypted = frackture_decrypt_payload(encrypted, key)
            assert decrypted == payload
    
    def test_encryption_wrong_key_rejection(self, small_data):
        """Test that encryption rejects incorrect keys"""
        correct_key = "correct_key"
        wrong_key = "wrong_key"
        
        # Create payload
        preprocessed = frackture_preprocess_universal_v2_6(small_data)
        payload = frackture_v3_3_safe(preprocessed)
        
        # Encrypt with correct key
        encrypted = frackture_encrypt_payload(payload, correct_key)
        
        # Try to decrypt with wrong key - should fail
        with pyteraises(ValueError, match="Invalid key or corrupted payload"):
            frackture_decrypt_payload(encrypted, wrong_key)
    
    def test_encryption_key_mismatch_detection(self):
        """Test detection of key mismatches"""
        key1 = "key1"
        key2 = "key2"
        test_data = "key mismatch test"
        
        # Create payload
        preprocessed = frackture_preprocess_universal_v2_6(test_data)
        payload = frackture_v3_3_safe(preprocessed)
        
        # Encrypt with key1
        encrypted = frackture_encrypt_payload(payload, key1)
        
        # Modify metadata to simulate key mismatch
        encrypted["metadata"]["key_id"] = "different_key_id"
        
        # Try to decrypt - should fail due to key mismatch
        with pyteraises(ValueError, match="Key mismatch"):
            frackture_decrypt_payload(encrypted, key1)
    
    def test_encryption_payload_tamper_detection(self, encryption_keys):
        """Test detection of tampered payloads"""
        key = encryption_keys[0]
        test_data = "tamper detection test"
        
        # Create and encrypt payload
        preprocessed = frackture_preprocess_universal_v2_6(test_data)
        payload = frackture_v3_3_safe(preprocessed)
        encrypted = frackture_encrypt_payload(payload, key)
        
        # Tamper with data
        encrypted["data"]["symbolic"] = "tampered_symbolic"
        
        # Try to decrypt tampered payload - should fail
        with pyteraises(ValueError, match="Invalid key or corrupted payload"):
            frackture_decrypt_payload(encrypted, key)
    
    def test_encryption_metadata_consistency(self, encryption_keys):
        """Test metadata consistency in encryption"""
        test_data = "metadata consistency test"
        preprocessed = frackture_preprocess_universal_v2_6(test_data)
        payload = frackture_v3_3_safe(preprocessed)
        
        for key in encryption_keys:
            encrypted = frackture_encrypt_payload(payload, key)
            
            # Check metadata structure
            assert "key_id" in encrypted["metadata"]
            assert isinstance(encrypted["metadata"]["key_id"], str)
            assert len(encrypted["metadata"]["key_id"]) == 8
            
            # Key ID should be deterministic
            encrypted2 = frackture_encrypt_payload(payload, key)
            assert encrypted["metadata"]["key_id"] == encrypted2["metadata"]["key_id"]
    
    def test_encryption_signature_uniqueness(self):
        """Test that signatures are unique for different payloads"""
        key = "test_key"
        data1 = "first payload"
        data2 = "second payload"
        
        preprocessed1 = frackture_preprocess_universal_v2_6(data1)
        preprocessed2 = frackture_preprocess_universal_v2_6(data2)
        payload1 = frackture_v3_3_safe(preprocessed1)
        payload2 = frackture_v3_3_safe(preprocessed2)
        
        encrypted1 = frackture_encrypt_payload(payload1, key)
        encrypted2 = frackture_encrypt_payload(payload2, key)
        
        # Signatures should be different for different payloads
        assert encrypted1["signature"] != encrypted2["signature"]
    
    def test_encryption_signature_determinism(self):
        """Test that signatures are deterministic"""
        key = "test_key"
        test_data = "signature determinism test"
        
        preprocessed = frackture_preprocess_universal_v2_6(test_data)
        payload = frackture_v3_3_safe(preprocessed)
        
        # Encrypt same payload multiple times
        encrypted1 = frackture_encrypt_payload(payload, key)
        encrypted2 = frackture_encrypt_payload(payload, key)
        
        # Signatures should be identical for same input
        assert encrypted1["signature"] == encrypted2["signature"]
    
    @given(text(min_size=1, max_size=1000))
    @settings(max_examples=50)
    def test_encryption_property_based(self, test_data):
        """Property-based test for encryption functionality"""
        key = "property_test_key"
        
        try:
            # Preprocess and encode
            preprocessed = frackture_preprocess_universal_v2_6(test_data)
            payload = frackture_v3_3_safe(preprocessed)
            
            # Encrypt
            encrypted = frackture_encrypt_payload(payload, key)
            
            # Decrypt
            decrypted = frackture_decrypt_payload(encrypted, key)
            
            # Should get original payload back
            assert decrypted == payload
            
            # Verify structure
            assert isinstance(encrypted, dict)
            assert len(encrypted) == 3  # data, signature, metadata
            assert "key_id" in encrypted["metadata"]
        except Exception as e:
            pytefail(f"Encryption property test failed: {e}")
    
    def test_encryption_adversarial_inputs(self, adversarial_inputs):
        """Test encryption with adversarial inputs"""
        key = "adversarial_test_key"
        
        for test_data in adversarial_inputs:
            try:
                # Preprocess and encode
                preprocessed = frackture_preprocess_universal_v2_6(test_data)
                payload = frackture_v3_3_safe(preprocessed)
                
                # Encrypt
                encrypted = frackture_encrypt_payload(payload, key)
                
                # Decrypt
                decrypted = frackture_decrypt_payload(encrypted, key)
                
                # Should get original payload back
                assert decrypted == payload
            except Exception as e:
                pytefail(f"Encryption failed for adversarial input {repr(test_data)}: {e}")
    
    def test_encryption_empty_payload(self):
        """Test encryption with minimal payload"""
        key = "empty_test_key"
        
        # Create minimal payload
        minimal_payload = {
            "symbolic": "a" * 64,  # Valid hex string
            "entropy": [1.0] * 16  # Valid entropy data
        }
        
        # Encrypt and decrypt
        encrypted = frackture_encrypt_payload(minimal_payload, key)
        decrypted = frackture_decrypt_payload(encrypted, key)
        
        assert decrypted == minimal_payload
    
    def test_encryption_large_payload(self, large_data):
        """Test encryption with large payload"""
        key = "large_payload_test_key"
        
        # Create large payload
        preprocessed = frackture_preprocess_universal_v2_6(large_data)
        payload = frackture_v3_3_safe(preprocessed)
        
        # Encrypt and decrypt
        encrypted = frackture_encrypt_payload(payload, key)
        decrypted = frackture_decrypt_payload(encrypted, key)
        
        assert decrypted == payload
    
    def test_encryption_hmac_security(self):
        """Test HMAC-based security features"""
        key = "hmac_security_test"
        test_data = "HMAC security test"
        
        preprocessed = frackture_preprocess_universal_v2_6(test_data)
        payload = frackture_v3_3_safe(preprocessed)
        
        encrypted = frackture_encrypt_payload(payload, key)
        
        # Test with various tampering attempts
        tamper_tests = [
            # Modify signature
            lambda e: e.update({"signature": "invalid_signature"}),
            # Modify data
            lambda e: e["data"].update({"symbolic": "modified"}),
            # Modify metadata
            lambda e: e["metadata"].update({"key_id": "different"}),
            # Add extra field
            lambda e: e.update({"extra_field": "hacker"}),
            # Remove required field
            lambda e: e.pop("signature"),
        ]
        
        for tamper in tamper_tests:
            tampered_encrypted = encrypted.copy()
            tamper(tampered_encrypted)
            
            with pyteraises(ValueError):
                frackture_decrypt_payload(tampered_encrypted, key)
    
    def test_encryption_key_strength_variation(self):
        """Test encryption with keys of varying strengths"""
        test_data = "key strength test"
        preprocessed = frackture_preprocess_universal_v2_6(test_data)
        payload = frackture_v3_3_safe(preprocessed)
        
        keys = [
            "a",  # Very short
            "a" * 256,  # Very long
            "unicode_🎉_key",  # Unicode
            "Key With Spaces",  # Spaces
            "key\nwith\tcontrol",  # Control characters
        ]
        
        for key in keys:
            try:
                encrypted = frackture_encrypt_payload(payload, key)
                decrypted = frackture_decrypt_payload(encrypted, key)
                assert decrypted == payload
            except Exception as e:
                pytefail(f"Key strength test failed for key '{repr(key)}': {e}")
    
    def test_encryption_cross_platform_consistency(self):
        """Test encryption consistency across different inputs"""
        test_data_list = [
            "test1",
            "test2",
            "test3"
        ]
        key = "consistency_test_key"
        
        results = []
        for test_data in test_data_list:
            preprocessed = frackture_preprocess_universal_v2_6(test_data)
            payload = frackture_v3_3_safe(preprocessed)
            encrypted = frackture_encrypt_payload(payload, key)
            decrypted = frackture_decrypt_payload(encrypted, key)
            
            results.append(decrypted)
        
        # Each should work independently
        assert len(results) == len(test_data_list)
        assert all(r == payload for r in results)
    
    def test_encryption_none_handling(self):
        """Test encryption with None values in payload"""
        key = "none_test_key"
        
        # Create payload with None values
        payload_with_none = {
            "symbolic": None,
            "entropy": [None] * 16
        }
        
        # Should handle None gracefully
        try:
            encrypted = frackture_encrypt_payload(payload_with_none, key)
            decrypted = frackture_decrypt_payload(encrypted, key)
            assert decrypted == payload_with_none
        except Exception as e:
            # JSON serialization of None is valid, so this should work
            pytefail(f"None handling failed: {e}")
    
    def test_encryption_numeric_precision(self):
        """Test encryption with high precision numeric data"""
        key = "precision_test_key"
        
        # Create payload with high precision numbers
        high_precision_payload = {
            "symbolic": "a" * 64,
            "entropy": [float(i) / 1000000 for i in range(16)]  # Very small increments
        }
        
        encrypted = frackture_encrypt_payload(high_precision_payload, key)
        decrypted = frackture_decrypt_payload(encrypted, key)
        
        # Should preserve precision
        for orig, dec in zip(high_precision_payload["entropy"], decrypted["entropy"]):
            assert abs(orig - dec) < 1e-15  # Very small tolerance for precision