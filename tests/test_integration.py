import pytest
import numpy as np
import sys
sys.path.insert(0, '/home/engine/project')
from importlib import import_module

frackture = import_module('frackture (2)')


@pytest.mark.integration
class TestIntegration:
    
    def test_full_pipeline_text(self, sample_text):
        preprocessed = frackture.frackture_preprocess_universal_v2_6(sample_text)
        payload = frackture.frackture_v3_3_safe(preprocessed)
        reconstructed = frackture.frackture_v3_3_reconstruct(payload)
        
        assert len(reconstructed) == len(preprocessed)
        assert isinstance(reconstructed, np.ndarray)
    
    def test_full_pipeline_bytes(self, sample_bytes):
        preprocessed = frackture.frackture_preprocess_universal_v2_6(sample_bytes)
        payload = frackture.frackture_v3_3_safe(preprocessed)
        reconstructed = frackture.frackture_v3_3_reconstruct(payload)
        
        assert len(reconstructed) == len(preprocessed)
    
    def test_full_pipeline_dict(self, sample_dict):
        preprocessed = frackture.frackture_preprocess_universal_v2_6(sample_dict)
        payload = frackture.frackture_v3_3_safe(preprocessed)
        reconstructed = frackture.frackture_v3_3_reconstruct(payload)
        
        assert len(reconstructed) == len(preprocessed)
    
    def test_full_pipeline_numpy_array(self, sample_numpy_array):
        preprocessed = frackture.frackture_preprocess_universal_v2_6(sample_numpy_array)
        payload = frackture.frackture_v3_3_safe(preprocessed)
        reconstructed = frackture.frackture_v3_3_reconstruct(payload)
        
        assert len(reconstructed) == len(preprocessed)
    
    def test_payload_structure(self, normalized_vector):
        payload = frackture.frackture_v3_3_safe(normalized_vector)
        
        assert isinstance(payload, dict)
        assert "symbolic" in payload
        assert "entropy" in payload
        assert isinstance(payload["symbolic"], str)
        assert isinstance(payload["entropy"], list)
    
    def test_payload_symbolic_format(self, normalized_vector):
        payload = frackture.frackture_v3_3_safe(normalized_vector)
        
        assert len(payload["symbolic"]) == 64
        assert all(c in '0123456789abcdef' for c in payload["symbolic"])
    
    def test_payload_entropy_format(self, normalized_vector):
        payload = frackture.frackture_v3_3_safe(normalized_vector)
        
        assert len(payload["entropy"]) == 16
        assert all(isinstance(x, (int, float, np.number)) for x in payload["entropy"])
    
    def test_reconstruction_shape(self, normalized_vector):
        payload = frackture.frackture_v3_3_safe(normalized_vector)
        reconstructed = frackture.frackture_v3_3_reconstruct(payload)
        
        assert reconstructed.shape == normalized_vector.shape
    
    def test_reconstruction_bounded(self, normalized_vector):
        payload = frackture.frackture_v3_3_safe(normalized_vector)
        reconstructed = frackture.frackture_v3_3_reconstruct(payload)
        
        assert np.all(reconstructed >= 0)
        assert np.all(reconstructed <= 1)
    
    def test_merge_reconstruction(self):
        entropy_vec = np.array([0.5] * 768, dtype=np.float32)
        symbolic_vec = np.array([0.3] * 768, dtype=np.float32)
        
        merged = frackture.merge_reconstruction(entropy_vec, symbolic_vec)
        
        assert len(merged) == 768
        np.testing.assert_array_almost_equal(merged, np.array([0.4] * 768))
    
    def test_merge_reconstruction_different_values(self):
        entropy_vec = np.zeros(768, dtype=np.float32)
        symbolic_vec = np.ones(768, dtype=np.float32)
        
        merged = frackture.merge_reconstruction(entropy_vec, symbolic_vec)
        
        assert len(merged) == 768
        np.testing.assert_array_almost_equal(merged, np.array([0.5] * 768))
    
    def test_end_to_end_deterministic(self, sample_text):
        preprocessed = frackture.frackture_preprocess_universal_v2_6(sample_text)
        
        payload1 = frackture.frackture_v3_3_safe(preprocessed)
        payload2 = frackture.frackture_v3_3_safe(preprocessed)
        
        assert payload1["symbolic"] == payload2["symbolic"]
        np.testing.assert_array_almost_equal(payload1["entropy"], payload2["entropy"])
    
    def test_reconstruction_deterministic(self, normalized_vector):
        payload = frackture.frackture_v3_3_safe(normalized_vector)
        
        recon1 = frackture.frackture_v3_3_reconstruct(payload)
        recon2 = frackture.frackture_v3_3_reconstruct(payload)
        
        np.testing.assert_array_equal(recon1, recon2)
    
    def test_reconstruction_mse_reasonable(self, normalized_vector):
        payload = frackture.frackture_v3_3_safe(normalized_vector)
        reconstructed = frackture.frackture_v3_3_reconstruct(payload)
        
        mse = np.mean((normalized_vector - reconstructed) ** 2)
        assert mse < 1.0


@pytest.mark.integration
class TestIntegrationEdgeCases:
    
    def test_empty_input_full_pipeline(self):
        preprocessed = frackture.frackture_preprocess_universal_v2_6("")
        payload = frackture.frackture_v3_3_safe(preprocessed)
        reconstructed = frackture.frackture_v3_3_reconstruct(payload)
        
        assert len(reconstructed) == 768
    
    def test_large_input_full_pipeline(self, large_inputs):
        preprocessed = frackture.frackture_preprocess_universal_v2_6(large_inputs["text"])
        payload = frackture.frackture_v3_3_safe(preprocessed)
        reconstructed = frackture.frackture_v3_3_reconstruct(payload)
        
        assert len(reconstructed) == 768
    
    def test_zeros_vector_full_pipeline(self):
        zeros = np.zeros(768, dtype=np.float32)
        payload = frackture.frackture_v3_3_safe(zeros)
        reconstructed = frackture.frackture_v3_3_reconstruct(payload)
        
        assert len(reconstructed) == 768
    
    def test_ones_vector_full_pipeline(self):
        ones = np.ones(768, dtype=np.float32)
        payload = frackture.frackture_v3_3_safe(ones)
        reconstructed = frackture.frackture_v3_3_reconstruct(payload)
        
        assert len(reconstructed) == 768


@pytest.mark.integration
class TestErrorHandling:
    
    def test_reconstruct_empty_dict(self):
        with pytest.raises(KeyError):
            frackture.frackture_v3_3_reconstruct({})
    
    def test_reconstruct_missing_symbolic(self):
        payload = {"entropy": [1.0] * 16}
        with pytest.raises(KeyError):
            frackture.frackture_v3_3_reconstruct(payload)
    
    def test_reconstruct_missing_entropy(self):
        payload = {"symbolic": "a" * 64}
        with pytest.raises(KeyError):
            frackture.frackture_v3_3_reconstruct(payload)
    
    def test_reconstruct_invalid_symbolic_type(self):
        payload = {"symbolic": 123, "entropy": [1.0] * 16}
        with pytest.raises((TypeError, AttributeError)):
            frackture.frackture_v3_3_reconstruct(payload)
    
    def test_reconstruct_invalid_entropy_type(self):
        payload = {"symbolic": "a" * 64, "entropy": "invalid"}
        with pytest.raises((TypeError, ValueError)):
            frackture.frackture_v3_3_reconstruct(payload)
    
    def test_reconstruct_empty_symbolic(self):
        payload = {"symbolic": "", "entropy": [1.0] * 16}
        with pytest.raises(ZeroDivisionError):
            frackture.frackture_v3_3_reconstruct(payload)
    
    def test_reconstruct_short_entropy(self):
        payload = {"symbolic": "a" * 64, "entropy": [1.0, 2.0]}
        with pytest.raises(ValueError):
            frackture.frackture_v3_3_reconstruct(payload)
    
    def test_reconstruct_empty_entropy(self):
        payload = {"symbolic": "a" * 64, "entropy": []}
        with pytest.raises(ValueError):
            frackture.frackture_v3_3_reconstruct(payload)
