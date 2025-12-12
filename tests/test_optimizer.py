import pytest
import numpy as np
import sys
sys.path.insert(0, '/home/engine/project')
from importlib import import_module

frackture = import_module('frackture (2)')


@pytest.mark.unit
class TestOptimizer:
    
    def test_optimize_returns_tuple(self, normalized_vector):
        result = frackture.optimize_frackture(normalized_vector)
        assert isinstance(result, tuple)
        assert len(result) == 2
    
    def test_optimize_returns_payload_and_mse(self, normalized_vector):
        payload, mse = frackture.optimize_frackture(normalized_vector)
        assert isinstance(payload, dict)
        assert isinstance(mse, (int, float, np.number))
    
    def test_optimize_payload_structure(self, normalized_vector):
        payload, mse = frackture.optimize_frackture(normalized_vector)
        assert "symbolic" in payload
        assert "entropy" in payload
        assert isinstance(payload["symbolic"], str)
        assert isinstance(payload["entropy"], list)
    
    def test_optimize_mse_non_negative(self, normalized_vector):
        payload, mse = frackture.optimize_frackture(normalized_vector)
        assert mse >= 0
    
    def test_optimize_mse_finite(self, normalized_vector):
        payload, mse = frackture.optimize_frackture(normalized_vector)
        assert np.isfinite(mse)
    
    def test_optimize_single_trial(self, normalized_vector):
        payload, mse = frackture.optimize_frackture(normalized_vector, num_trials=1)
        assert payload is not None
        assert mse >= 0
    
    def test_optimize_multiple_trials(self, normalized_vector):
        payload, mse = frackture.optimize_frackture(normalized_vector, num_trials=10)
        assert payload is not None
        assert mse >= 0
    
    def test_optimize_improves_over_baseline(self, normalized_vector):
        baseline_payload = frackture.frackture_v3_3_safe(normalized_vector)
        baseline_recon = frackture.frackture_v3_3_reconstruct(baseline_payload)
        baseline_mse = np.mean((normalized_vector - baseline_recon) ** 2)
        
        optimized_payload, optimized_mse = frackture.optimize_frackture(normalized_vector, num_trials=5)
        
        assert optimized_mse <= baseline_mse * 1.1
    
    def test_optimize_deterministic(self, normalized_vector):
        payload1, mse1 = frackture.optimize_frackture(normalized_vector, num_trials=3)
        payload2, mse2 = frackture.optimize_frackture(normalized_vector, num_trials=3)
        
        assert payload1["symbolic"] == payload2["symbolic"]
        np.testing.assert_array_almost_equal(payload1["entropy"], payload2["entropy"])
        assert mse1 == mse2
    
    def test_optimize_reconstruction_valid(self, normalized_vector):
        payload, mse = frackture.optimize_frackture(normalized_vector)
        reconstructed = frackture.frackture_v3_3_reconstruct(payload)
        
        assert len(reconstructed) == len(normalized_vector)
        assert np.all(reconstructed >= 0)
        assert np.all(reconstructed <= 1)
    
    def test_optimize_mse_matches_reconstruction(self, normalized_vector):
        payload, reported_mse = frackture.optimize_frackture(normalized_vector)
        reconstructed = frackture.frackture_v3_3_reconstruct(payload)
        calculated_mse = np.mean((normalized_vector - reconstructed) ** 2)
        
        np.testing.assert_almost_equal(reported_mse, calculated_mse, decimal=6)


@pytest.mark.integration
class TestOptimizerIntegration:
    
    def test_optimize_text_input(self, sample_text):
        preprocessed = frackture.frackture_preprocess_universal_v2_6(sample_text)
        payload, mse = frackture.optimize_frackture(preprocessed)
        
        assert payload is not None
        assert mse >= 0
    
    def test_optimize_bytes_input(self, sample_bytes):
        preprocessed = frackture.frackture_preprocess_universal_v2_6(sample_bytes)
        payload, mse = frackture.optimize_frackture(preprocessed)
        
        assert payload is not None
        assert mse >= 0
    
    def test_optimize_dict_input(self, sample_dict):
        preprocessed = frackture.frackture_preprocess_universal_v2_6(sample_dict)
        payload, mse = frackture.optimize_frackture(preprocessed)
        
        assert payload is not None
        assert mse >= 0
    
    def test_optimize_array_input(self, sample_numpy_array):
        preprocessed = frackture.frackture_preprocess_universal_v2_6(sample_numpy_array)
        payload, mse = frackture.optimize_frackture(preprocessed)
        
        assert payload is not None
        assert mse >= 0
    
    def test_optimize_end_to_end(self, sample_text):
        preprocessed = frackture.frackture_preprocess_universal_v2_6(sample_text)
        payload, mse = frackture.optimize_frackture(preprocessed, num_trials=5)
        reconstructed = frackture.frackture_v3_3_reconstruct(payload)
        
        assert len(reconstructed) == len(preprocessed)
        mse_check = np.mean((preprocessed - reconstructed) ** 2)
        np.testing.assert_almost_equal(mse, mse_check, decimal=6)


@pytest.mark.edge
class TestOptimizerEdgeCases:
    
    def test_optimize_zeros(self):
        zeros = np.zeros(768, dtype=np.float32)
        payload, mse = frackture.optimize_frackture(zeros)
        
        assert payload is not None
        assert mse >= 0
    
    def test_optimize_ones(self):
        ones = np.ones(768, dtype=np.float32)
        payload, mse = frackture.optimize_frackture(ones)
        
        assert payload is not None
        assert mse >= 0
    
    def test_optimize_constant(self):
        constant = np.full(768, 0.5, dtype=np.float32)
        payload, mse = frackture.optimize_frackture(constant)
        
        assert payload is not None
        assert mse >= 0
    
    def test_optimize_alternating(self):
        alternating = np.array([0.0, 1.0] * 384, dtype=np.float32)
        payload, mse = frackture.optimize_frackture(alternating)
        
        assert payload is not None
        assert mse >= 0
    
    def test_optimize_random(self, random_vector):
        payload, mse = frackture.optimize_frackture(random_vector)
        
        assert payload is not None
        assert mse >= 0
    
    def test_optimize_zero_trials_uses_default(self, normalized_vector):
        payload, mse = frackture.optimize_frackture(normalized_vector, num_trials=0)
        
        assert payload is not None or mse == float("inf")
    
    def test_optimize_large_trials(self, normalized_vector):
        payload, mse = frackture.optimize_frackture(normalized_vector, num_trials=20)
        
        assert payload is not None
        assert mse >= 0
