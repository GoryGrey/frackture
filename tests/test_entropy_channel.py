import pytest
import numpy as np
import sys
sys.path.insert(0, '/home/engine/project')
from importlib import import_module

frackture = import_module('frackture (2)')


@pytest.mark.unit
class TestEntropyChannel:
    
    def test_entropy_encode_returns_list(self, normalized_vector):
        result = frackture.entropy_channel_encode(normalized_vector)
        assert isinstance(result, list)
    
    def test_entropy_encode_length(self, normalized_vector):
        result = frackture.entropy_channel_encode(normalized_vector)
        assert len(result) == 16
    
    def test_entropy_encode_numeric(self, normalized_vector):
        result = frackture.entropy_channel_encode(normalized_vector)
        assert all(isinstance(x, (int, float, np.number)) for x in result)
    
    def test_entropy_encode_deterministic(self, normalized_vector):
        result1 = frackture.entropy_channel_encode(normalized_vector)
        result2 = frackture.entropy_channel_encode(normalized_vector)
        np.testing.assert_array_almost_equal(result1, result2)
    
    def test_entropy_encode_different_inputs(self, normalized_vector, random_vector):
        result1 = frackture.entropy_channel_encode(normalized_vector)
        result2 = frackture.entropy_channel_encode(random_vector)
        assert not np.allclose(result1, result2)
    
    def test_entropy_decode_returns_array(self):
        entropy_data = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0,
                       9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0]
        result = frackture.entropy_channel_decode(entropy_data)
        assert isinstance(result, np.ndarray)
    
    def test_entropy_decode_length(self):
        entropy_data = [1.0] * 16
        result = frackture.entropy_channel_decode(entropy_data)
        assert len(result) == 768
    
    def test_entropy_decode_normalized(self):
        entropy_data = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0,
                       9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0]
        result = frackture.entropy_channel_decode(entropy_data)
        assert np.min(result) >= 0
        assert np.max(result) <= 1
    
    def test_entropy_encode_decode_consistency(self, normalized_vector):
        encoded = frackture.entropy_channel_encode(normalized_vector)
        decoded = frackture.entropy_channel_decode(encoded)
        assert len(decoded) == len(normalized_vector)
    
    def test_entropy_decode_deterministic(self):
        entropy_data = [1.0] * 16
        result1 = frackture.entropy_channel_decode(entropy_data)
        result2 = frackture.entropy_channel_decode(entropy_data)
        np.testing.assert_array_equal(result1, result2)


@pytest.mark.edge
class TestEntropyChannelEdgeCases:
    
    def test_entropy_encode_zeros(self):
        zeros = np.zeros(768, dtype=np.float32)
        result = frackture.entropy_channel_encode(zeros)
        assert len(result) == 16
    
    def test_entropy_encode_ones(self):
        ones = np.ones(768, dtype=np.float32)
        result = frackture.entropy_channel_encode(ones)
        assert len(result) == 16
    
    def test_entropy_encode_constant_vector(self):
        constant = np.full(768, 0.5, dtype=np.float32)
        result = frackture.entropy_channel_encode(constant)
        assert len(result) == 16
    
    def test_entropy_decode_zeros(self):
        zeros = [0.0] * 16
        result = frackture.entropy_channel_decode(zeros)
        assert len(result) == 768
    
    def test_entropy_decode_negative_values(self):
        negative = [-1.0, -2.0, -3.0] * 5 + [-4.0]
        result = frackture.entropy_channel_decode(negative)
        assert len(result) == 768
        assert np.all(result >= 0) and np.all(result <= 1)
    
    def test_entropy_decode_large_values(self):
        large = [1000.0, 2000.0, 3000.0] * 5 + [4000.0]
        result = frackture.entropy_channel_decode(large)
        assert len(result) == 768
        assert np.all(result >= 0) and np.all(result <= 1)
    
    def test_entropy_decode_mixed_values(self):
        mixed = [-100.0, 0.0, 100.0, 200.0, -50.0, 50.0] * 2 + [0.0] * 4
        result = frackture.entropy_channel_decode(mixed)
        assert len(result) == 768
    
    def test_entropy_encode_alternating_pattern(self):
        alternating = np.array([0.0, 1.0] * 384, dtype=np.float32)
        result = frackture.entropy_channel_encode(alternating)
        assert len(result) == 16
