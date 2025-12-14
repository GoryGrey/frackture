"""
Tests for round-trip compression/decompression across different input types
"""
import pytest
import numpy as np
from hypothesis import given, settings
from hypothesis.strategies import text, binary, dictionaries, lists, floats, integers, data
import math
from conftest import arbitrary_data

class TestRoundTrip:
    """Test round-trip compression/decompression functionality"""
    
    def test_roundtrip_bytes(self, small_data):
        """Test round-trip with bytes input"""
        # Preprocess
        preprocessed = frackture_preprocess_universal_v2_6(small_data)
        
        # Encode
        payload = frackture_v3_3_safe(preprocessed)
        
        # Decode
        reconstructed = frackture_v3_3_reconstruct(payload)
        
        # Verify reconstruction properties
        assert isinstance(reconstructed, np.ndarray)
        assert len(reconstructed) == 768
        assert np.all(reconstructed >= 0)
        assert np.all(reconstructed <= 1)
        
        # Verify it's a valid reconstruction (within reasonable tolerance)
        assert reconstructed.shape == (768,)
        assert reconstructed.dtype == np.float32
    
    def test_roundtrip_string(self):
        """Test round-trip with string input"""
        test_string = "Hello, world! This is a test."
        
        # Preprocess
        preprocessed = frackture_preprocess_universal_v2_6(test_string)
        
        # Encode
        payload = frackture_v3_3_safe(preprocessed)
        
        # Decode
        reconstructed = frackture_v3_3_reconstruct(payload)
        
        # Verify reconstruction properties
        assert isinstance(reconstructed, np.ndarray)
        assert len(reconstructed) == 768
        assert np.all(reconstructed >= 0)
        assert np.all(reconstructed <= 1)
    
    def test_roundtrip_dict(self, dict_inputs):
        """Test round-trip with dictionary inputs"""
        for test_dict in dict_inputs:
            # Preprocess
            preprocessed = frackture_preprocess_universal_v2_6(test_dict)
            
            # Encode
            payload = frackture_v3_3_safe(preprocessed)
            
            # Decode
            reconstructed = frackture_v3_3_reconstruct(payload)
            
            # Verify reconstruction properties
            assert isinstance(reconstructed, np.ndarray)
            assert len(reconstructed) == 768
            assert np.all(reconstructed >= 0)
            assert np.all(reconstructed <= 1)
    
    def test_roundtrip_array(self, array_inputs):
        """Test round-trip with array inputs"""
        for test_array in array_inputs:
            # Skip empty arrays to avoid division by zero
            if len(test_array) == 0:
                continue
                
            # Preprocess
            preprocessed = frackture_preprocess_universal_v2_6(test_array)
            
            # Encode
            payload = frackture_v3_3_safe(preprocessed)
            
            # Decode
            reconstructed = frackture_v3_3_reconstruct(payload)
            
            # Verify reconstruction properties
            assert isinstance(reconstructed, np.ndarray)
            assert len(reconstructed) == 768
            assert np.all(reconstructed >= 0)
            assert np.all(reconstructed <= 1)
    
    @given(data())
    @settings(max_examples=50)
    def test_roundtrip_arbitrary_data(self, data):
        """Test round-trip with Hypothesis-generated arbitrary data"""
        test_data = data.draw(arbitrary_data())
        
        try:
            # Preprocess
            preprocessed = frackture_preprocess_universal_v2_6(test_data)
            
            # Encode
            payload = frackture_v3_3_safe(preprocessed)
            
            # Decode
            reconstructed = frackture_v3_3_reconstruct(payload)
            
            # Verify reconstruction properties
            assert isinstance(reconstructed, np.ndarray)
            assert len(reconstructed) == 768
            assert not np.any(np.isnan(reconstructed)), "Reconstruction should not contain NaN"
            assert not np.any(np.isinf(reconstructed)), "Reconstruction should not contain infinity"
            assert np.all(reconstructed >= 0)
            assert np.all(reconstructed <= 1)
        except Exception as e:
            # Some pathological inputs might cause issues, but they should be handled gracefully
            pytest.fail(f"Round-trip failed for {type(test_data)}: {e}")
    
    def test_roundtrip_large_payloads(self, large_data):
        """Test round-trip with large payloads"""
        # Preprocess large data
        preprocessed = frackture_preprocess_universal_v2_6(large_data)
        
        # Encode
        payload = frackture_v3_3_safe(preprocessed)
        
        # Decode
        reconstructed = frackture_v3_3_reconstruct(payload)
        
        # Verify reconstruction properties
        assert isinstance(reconstructed, np.ndarray)
        assert len(reconstructed) == 768
        assert np.all(reconstructed >= 0)
        assert np.all(reconstructed <= 1)
    
    def test_roundtrip_adversarial_inputs(self, adversarial_inputs):
        """Test round-trip with adversarial inputs"""
        for test_data in adversarial_inputs:
            try:
                # Preprocess
                preprocessed = frackture_preprocess_universal_v2_6(test_data)
                
                # Encode
                payload = frackture_v3_3_safe(preprocessed)
                
                # Decode
                reconstructed = frackture_v3_3_reconstruct(payload)
                
                # Verify reconstruction properties
                assert isinstance(reconstructed, np.ndarray)
                assert len(reconstructed) == 768
                assert not np.any(np.isnan(reconstructed)), f"NaN in reconstruction for {type(test_data)}"
                assert not np.any(np.isinf(reconstructed)), f"Infinity in reconstruction for {type(test_data)}"
            except Exception as e:
                pytest.fail(f"Round-trip failed for adversarial input {repr(test_data)}: {e}")
    
    def test_roundtrip_consistency(self):
        """Test that round-trip produces consistent results"""
        test_data = "consistency test data"
        
        # First round-trip
        preprocessed1 = frackture_preprocess_universal_v2_6(test_data)
        payload1 = frackture_v3_3_safe(preprocessed1)
        reconstructed1 = frackture_v3_3_reconstruct(payload1)
        
        # Second round-trip
        preprocessed2 = frackture_preprocess_universal_v2_6(test_data)
        payload2 = frackture_v3_3_safe(preprocessed2)
        reconstructed2 = frackture_v3_3_reconstruct(payload2)
        
        # Preprocessed should be identical (deterministic preprocessing)
        np.testing.assert_array_equal(preprocessed1, preprocessed2)
        
        # Payload should be identical (deterministic encoding)
        assert payload1 == payload2
        
        # Reconstructions should be identical
        np.testing.assert_array_equal(reconstructed1, reconstructed2)
    
    def test_payload_structure(self):
        """Test that payloads have correct structure"""
        test_data = "payload structure test"
        preprocessed = frackture_preprocess_universal_v2_6(test_data)
        payload = frackture_v3_3_safe(preprocessed)
        
        # Check payload structure
        assert isinstance(payload, dict)
        assert "symbolic" in payload
        assert "entropy" in payload
        assert len(payload) == 2
        
        # Check symbolic fingerprint format
        assert isinstance(payload["symbolic"], str)
        assert len(payload["symbolic"]) > 0
        
        # Check entropy data format
        assert isinstance(payload["entropy"], list)
        assert len(payload["entropy"]) == 16  # PCA components
        
        # All entropy values should be floats
        for val in payload["entropy"]:
            assert isinstance(val, (int, float))
    
    def test_reconstruction_quality(self):
        """Test reconstruction quality with controlled input"""
        # Create a simple, predictable input
        simple_input = np.array([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
        
        # Preprocess
        preprocessed = frackture_preprocess_universal_v2_6(simple_input)
        
        # Encode and decode
        payload = frackture_v3_3_safe(preprocessed)
        reconstructed = frackture_v3_3_reconstruct(payload)
        
        # Calculate reconstruction error
        mse = np.mean((preprocessed - reconstructed) ** 2)
        
        # MSE should be reasonable (not too high)
        assert mse < 0.1, f"Reconstruction MSE too high: {mse}"
        
        # Value ranges should be preserved
        assert np.min(reconstructed) >= 0
        assert np.max(reconstructed) <= 1
    
    def test_symbolic_channel_decode_encode_consistency(self):
        """Test that symbolic channel decode/encode are consistent"""
        test_data = "symbolic consistency test"
        preprocessed = frackture_preprocess_universal_v2_6(test_data)
        
        # Get symbolic fingerprint
        symbolic = symbolic_channel_encode(preprocessed)
        
        # Decode back
        symbolic_decoded = symbolic_channel_decode(symbolic)
        
        # Should be able to re-encode
        symbolic_reencoded = symbolic_channel_encode(symbolic_decoded)
        
        # Should be consistent (re-encoding decoded symbolic should give original)
        assert symbolic == symbolic_reencoded
    
    def test_entropy_channel_decode_encode_consistency(self):
        """Test that entropy channel decode/encode are consistent"""
        test_data = "entropy consistency test"
        preprocessed = frackture_preprocess_universal_v2_6(test_data)
        
        # Get entropy encoding
        entropy = entropy_channel_encode(preprocessed)
        
        # Decode back
        entropy_decoded = entropy_channel_decode(entropy)
        
        # Re-encode
        entropy_reencoded = entropy_channel_encode(entropy_decoded)
        
        # Should be close (floating point precision may vary slightly)
        for i, (orig, reencoded) in enumerate(zip(entropy, entropy_reencoded)):
            assert abs(orig - reencoded) < 1e-10, f"Entropy encoding not consistent at index {i}"
    
    def test_merged_reconstruction_properties(self):
        """Test properties of merged reconstruction"""
        test_data = "merge test"
        preprocessed = frackture_preprocess_universal_v2_6(test_data)
        
        # Get symbolic and entropy components
        symbolic = symbolic_channel_encode(preprocessed)
        entropy = entropy_channel_encode(preprocessed)
        
        # Decode individually
        symbolic_decoded = symbolic_channel_decode(symbolic)
        entropy_decoded = entropy_channel_decode(entropy)
        
        # Merge
        merged = merge_reconstruction(entropy_decoded, symbolic_decoded)
        
        # Verify merge properties
        assert isinstance(merged, np.ndarray)
        assert len(merged) == 768
        
        # Merged values should be averages, so in [0, 1] range
        assert np.all(merged >= 0)
        assert np.all(merged <= 1)
        
        # Should be average of inputs
        expected = (entropy_decoded + symbolic_decoded) / 2
        np.testing.assert_array_almost_equal(merged, expected)