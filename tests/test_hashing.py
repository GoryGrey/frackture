"""
Tests for hashing determinism and collision sampling
"""
import pytest
import numpy as np
from hypothesis import given, settings
from hypothesis.strategies import text, binary, integers, floats, lists
import hashlib
from collections import defaultdict

class TestHashing:
    """Test hashing determinism and collision detection"""
    
    def test_deterministic_hash_consistency(self):
        """Test that deterministic hashing produces consistent results"""
        test_data = "deterministic hash test"
        
        # Hash the same data multiple times
        hash1 = frackture_deterministic_hash(test_data)
        hash2 = frackture_deterministic_hash(test_data)
        hash3 = frackture_deterministic_hash(test_data)
        
        # All should be identical
        assert hash1 == hash2 == hash3
        assert len(hash1) == 64  # SHA256 hex string length
    
    def test_deterministic_hash_uniqueness(self):
        """Test that different data produces different hashes"""
        test_data_list = [
            "data1",
            "data2", 
            "data3",
            "similar but different",
            "",
            " ",  # Single space
            "  ",  # Double space
        ]
        
        hashes = [frackture_deterministic_hash(data) for data in test_data_list]
        
        # All hashes should be unique
        assert len(hashes) == len(set(hashes)), "Found hash collision in basic test"
    
    def test_deterministic_hash_salt_consistency(self):
        """Test that salt produces consistent results"""
        test_data = "salted hash test"
        salt = "test_salt_123"
        
        # Hash with salt multiple times
        hash1 = frackture_deterministic_hash(test_data, salt)
        hash2 = frackture_deterministic_hash(test_data, salt)
        
        # Should be identical
        assert hash1 == hash2
    
    def test_deterministic_hash_salt_uniqueness(self):
        """Test that different salts produce different hashes for same data"""
        test_data = "same data"
        salt1 = "salt1"
        salt2 = "salt2"
        salt3 = "different_salt"
        
        hash1 = frackture_deterministic_hash(test_data, salt1)
        hash2 = frackture_deterministic_hash(test_data, salt2)
        hash3 = frackture_deterministic_hash(test_data, salt3)
        
        # All should be different
        assert hash1 != hash2
        assert hash1 != hash3
        assert hash2 != hash3
    
    def test_symbolic_fingerprint_determinism(self):
        """Test that symbolic fingerprints are deterministic"""
        test_data = "symbolic determinism test"
        
        # Preprocess
        preprocessed = frackture_preprocess_universal_v2_6(test_data)
        
        # Generate fingerprints multiple times
        fingerprint1 = symbolic_channel_encode(preprocessed)
        fingerprint2 = symbolic_channel_encode(preprocessed)
        fingerprint3 = symbolic_channel_encode(preprocessed)
        
        # All should be identical
        assert fingerprint1 == fingerprint2 == fingerprint3
        assert isinstance(fingerprint1, str)
        assert len(fingerprint1) > 0
    
    def test_symbolic_fingerprint_uniqueness(self):
        """Test that different data produces different symbolic fingerprints"""
        test_data_list = [
            "data1",
            "data2",
            "completely different data",
            "similar but not the same",
        ]
        
        fingerprints = []
        for data in test_data_list:
            preprocessed = frackture_preprocess_universal_v2_6(data)
            fingerprint = symbolic_channel_encode(preprocessed)
            fingerprints.append(fingerprint)
        
        # All fingerprints should be unique
        assert len(fingerprints) == len(set(fingerprints)), "Found symbolic fingerprint collision"
    
    def test_symbolic_fingerprint_fixed_properties(self):
        """Test that symbolic fingerprints maintain fixed properties"""
        test_data = "fingerprint properties test"
        preprocessed = frackture_preprocess_universal_v2_6(test_data)
        fingerprint = symbolic_channel_encode(preprocessed)
        
        # Should be hex string
        assert isinstance(fingerprint, str)
        
        # Should be valid hex
        try:
            bytes.fromhex(fingerprint)
        except ValueError:
            pytefail(f"Invalid hex fingerprint: {fingerprint}")
        
        # Length should be even (hex pairs)
        assert len(fingerprint) % 2 == 0
        
        # Should have reasonable length (based on 32 chunks)
        expected_length = 32 * 2  # 32 chunks, 2 hex chars each
        assert len(fingerprint) == expected_length
    
    def test_collision_sampling_basic(self):
        """Test collision sampling with controlled inputs"""
        # Generate many similar inputs to test for collisions
        test_inputs = [f"test_input_{i}" for i in range(100)]
        fingerprints = {}
        collisions = []
        
        for data in test_inputs:
            preprocessed = frackture_preprocess_universal_v2_6(data)
            fingerprint = symbolic_channel_encode(preprocessed)
            
            if fingerprint in fingerprints:
                collisions.append((data, fingerprints[fingerprint]))
            else:
                fingerprints[fingerprint] = data
        
        # Should have no collisions with controlled inputs
        assert len(collisions) == 0, f"Found {len(collisions)} collisions in basic test"
    
    def test_collision_sampling_adversarial(self, adversarial_inputs):
        """Test collision sampling with adversarial inputs"""
        fingerprints = {}
        collisions = []
        
        for i, data in enumerate(adversarial_inputs):
            try:
                preprocessed = frackture_preprocess_universal_v2_6(data)
                fingerprint = symbolic_channel_encode(preprocessed)
                
                if fingerprint in fingerprints:
                    collisions.append((i, data, fingerprints[fingerprint]))
                else:
                    fingerprints[fingerprint] = (i, data)
            except Exception as e:
                pytefail(f"Error processing adversarial input {i}: {e}")
        
        # Log collisions if found (may be expected in some cases)
        if collisions:
            print(f"Found {len(collisions)} collisions in adversarial test")
            for idx, current, previous in collisions:
                print(f"Collision {idx}: {repr(current)} vs {repr(previous[1])}")
    
    def test_collision_sampling_large_scale(self):
        """Test collision sampling with large number of inputs"""
        # Generate many random inputs
        import random
        import string
        
        test_inputs = []
        for i in range(1000):
            # Generate random string of varying lengths
            length = random.randint(1, 100)
            random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
            test_inputs.append(random_string)
        
        fingerprints = {}
        collisions = []
        
        for data in test_inputs:
            try:
                preprocessed = frackture_preprocess_universal_v2_6(data)
                fingerprint = symbolic_channel_encode(preprocessed)
                
                if fingerprint in fingerprints:
                    collisions.append((data, fingerprints[fingerprint]))
                else:
                    fingerprints[fingerprint] = data
            except Exception as e:
                pytefail(f"Error processing large-scale input: {e}")
        
        # Print collision rate for analysis
        collision_rate = len(collisions) / len(test_inputs)
        print(f"Large-scale collision rate: {collision_rate:.4f}")
        
        # Should have reasonable collision rate (not too high)
        assert collision_rate < 0.1, f"High collision rate: {collision_rate}"
    
    def test_hash_vs_symbolic_comparison(self):
        """Compare deterministic hashing with symbolic fingerprinting"""
        test_data = "comparison test"
        preprocessed = frackture_preprocess_universal_v2_6(test_data)
        
        # Get deterministic hash
        det_hash = frackture_deterministic_hash(test_data)
        
        # Get symbolic fingerprint
        symbolic_fp = symbolic_channel_encode(preprocessed)
        
        # They should be different (different algorithms)
        assert det_hash != symbolic_fp
        
        # But both should be deterministic
        det_hash2 = frackture_deterministic_hash(test_data)
        symbolic_fp2 = symbolic_channel_encode(preprocessed)
        
        assert det_hash == det_hash2
        assert symbolic_fp == symbolic_fp2
    
    @given(text(min_size=1, max_size=500))
    @settings(max_examples=100)
    def test_hash_property_based(self, test_data):
        """Property-based test for deterministic hashing"""
        try:
            # Test determinism
            hash1 = frackture_deterministic_hash(test_data)
            hash2 = frackture_deterministic_hash(test_data)
            assert hash1 == hash2
            
            # Test format
            assert isinstance(hash1, str)
            assert len(hash1) == 64  # SHA256 hex
            
            # Test salt determinism
            salt = "test_salt"
            salted_hash1 = frackture_deterministic_hash(test_data, salt)
            salted_hash2 = frackture_deterministic_hash(test_data, salt)
            assert salted_hash1 == salted_hash2
            
            # Unsalted and salted should be different
            assert hash1 != salted_hash1
            
        except Exception as e:
            pytefail(f"Hash property test failed: {e}")
    
    def test_entropy_channel_uniqueness(self):
        """Test that entropy channel encoding is unique for different inputs"""
        test_data_list = [
            "entropy_test_1",
            "entropy_test_2", 
            "different entropy test",
            "similar but different entropy",
        ]
        
        entropy_encodings = []
        for data in test_data_list:
            preprocessed = frackture_preprocess_universal_v2_6(data)
            entropy = entropy_channel_encode(preprocessed)
            entropy_encodings.append(entropy)
        
        # All entropy encodings should be unique
        assert len(entropy_encodings) == len(set(tuple(e) for e in entropy_encodings)), \
            "Found entropy encoding collision"
    
    def test_fingerprint_length_consistency(self):
        """Test that fingerprint length is consistent across inputs"""
        test_inputs = [
            "short",
            "this is a much longer test input string",
            b"byte string input",
            {"dict": "input"},
            [1, 2, 3, 4, 5],
        ]
        
        for data in test_inputs:
            preprocessed = frackture_preprocess_universal_v2_6(data)
            fingerprint = symbolic_channel_encode(preprocessed)
            
            # All should have same length
            assert len(fingerprint) == 64, f"Fingerprint length inconsistent for {type(data)}"
    
    def test_collision_resistance_property(self):
        """Test collision resistance property of hashing functions"""
        # This tests that it's computationally hard to find collisions
        
        # Generate many inputs with controlled differences
        base_input = "collision_test_base"
        variations = [base_input + str(i) for i in range(50)]
        
        hashes = {}
        for var in variations:
            h = frackture_deterministic_hash(var)
            if h in hashes:
                pytefail(f"Collision found: {var} and {hashes[h]}")
            else:
                hashes[h] = var
        
        # Should have no collisions with controlled variations
        assert len(hashes) == len(variations)
    
    def test_different_pass_counts(self):
        """Test symbolic fingerprinting with different pass counts"""
        test_data = "pass count test"
        preprocessed = frackture_preprocess_universal_v2_6(test_data)
        
        # Generate fingerprints with different pass counts
        fingerprints = {}
        for passes in [1, 2, 3, 4, 5, 10]:
            fp = frackture_symbolic_fingerprint_f_infinity(preprocessed, passes=passes)
            fingerprints[passes] = fp
        
        # All should be different for different pass counts
        unique_fingerprints = set(fingerprints.values())
        assert len(unique_fingerprints) == len(fingerprints), \
            "Some pass counts produced same fingerprint"
        
        # But each should be consistent for same pass count
        for passes in fingerprints:
            fp1 = frackture_symbolic_fingerprint_f_infinity(preprocessed, passes=passes)
            assert fp1 == fingerprints[passes]
    
    def test_fingerprint_entropy_distribution(self):
        """Test that fingerprints have good entropy distribution"""
        test_inputs = [f"entropy_test_{i}" for i in range(100)]
        hex_chars = '0123456789abcdef'
        
        all_hex_values = []
        for data in test_inputs:
            preprocessed = frackture_preprocess_universal_v2_6(data)
            fingerprint = symbolic_channel_encode(preprocessed)
            
            # Count hex character distribution
            hex_counts = {char: 0 for char in hex_chars}
            for char in fingerprint:
                if char in hex_counts:
                    hex_counts[char] += 1
            
            # Check distribution is not too skewed
            counts = list(hex_counts.values())
            max_count = max(counts)
            min_count = min(counts)
            
            # Should not be too imbalanced
            assert max_count - min_count < len(fingerprint) * 0.1, \
                f"Fingerprint has skewed hex distribution: {hex_counts}"
            
            all_hex_values.extend(fingerprint)
        
        # Overall distribution should be reasonable
        total_counts = {char: all_hex_values.count(char) for char in hex_chars}
        counts = list(total_counts.values())
        assert max(counts) - min(counts) < len(all_hex_values) * 0.05, \
            "Overall hex distribution is too skewed"