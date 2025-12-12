import pytest
import numpy as np
import sys
sys.path.insert(0, '/home/engine/project')
from importlib import import_module

frackture = import_module('frackture (2)')


@pytest.mark.unit
class TestSymbolicFingerprint:
    
    def test_symbolic_fingerprint_returns_string(self, normalized_vector):
        result = frackture.frackture_symbolic_fingerprint_f_infinity(normalized_vector)
        assert isinstance(result, str)
    
    def test_symbolic_fingerprint_hex_format(self, normalized_vector):
        result = frackture.frackture_symbolic_fingerprint_f_infinity(normalized_vector)
        assert all(c in '0123456789abcdef' for c in result)
    
    def test_symbolic_fingerprint_length(self, normalized_vector):
        result = frackture.frackture_symbolic_fingerprint_f_infinity(normalized_vector)
        assert len(result) == 64
    
    def test_symbolic_fingerprint_deterministic(self, normalized_vector):
        result1 = frackture.frackture_symbolic_fingerprint_f_infinity(normalized_vector)
        result2 = frackture.frackture_symbolic_fingerprint_f_infinity(normalized_vector)
        assert result1 == result2
    
    def test_symbolic_fingerprint_different_inputs(self, normalized_vector, random_vector):
        result1 = frackture.frackture_symbolic_fingerprint_f_infinity(normalized_vector)
        result2 = frackture.frackture_symbolic_fingerprint_f_infinity(random_vector)
        assert result1 != result2
    
    def test_symbolic_fingerprint_default_passes(self, normalized_vector):
        result = frackture.frackture_symbolic_fingerprint_f_infinity(normalized_vector)
        assert isinstance(result, str)
    
    def test_symbolic_fingerprint_single_pass(self, normalized_vector):
        result = frackture.frackture_symbolic_fingerprint_f_infinity(normalized_vector, passes=1)
        assert len(result) == 64
    
    def test_symbolic_fingerprint_multiple_passes(self, normalized_vector):
        result = frackture.frackture_symbolic_fingerprint_f_infinity(normalized_vector, passes=10)
        assert len(result) == 64
    
    def test_symbolic_fingerprint_different_passes_different_results(self, normalized_vector):
        result1 = frackture.frackture_symbolic_fingerprint_f_infinity(normalized_vector, passes=2)
        result2 = frackture.frackture_symbolic_fingerprint_f_infinity(normalized_vector, passes=5)
        assert result1 != result2
    
    def test_symbolic_channel_encode(self, normalized_vector):
        result = frackture.symbolic_channel_encode(normalized_vector)
        assert isinstance(result, str)
        assert len(result) == 64
    
    def test_symbolic_channel_encode_deterministic(self, normalized_vector):
        result1 = frackture.symbolic_channel_encode(normalized_vector)
        result2 = frackture.symbolic_channel_encode(normalized_vector)
        assert result1 == result2
    
    def test_symbolic_channel_decode_returns_array(self):
        symbolic_hash = "a" * 64
        result = frackture.symbolic_channel_decode(symbolic_hash)
        assert isinstance(result, np.ndarray)
        assert len(result) == 768
    
    def test_symbolic_channel_decode_normalized(self):
        symbolic_hash = "ff" * 32
        result = frackture.symbolic_channel_decode(symbolic_hash)
        assert result.dtype == np.float32
        assert np.all(result >= 0) and np.all(result <= 1)
    
    def test_symbolic_encode_decode_consistency(self, normalized_vector):
        encoded = frackture.symbolic_channel_encode(normalized_vector)
        decoded = frackture.symbolic_channel_decode(encoded)
        assert len(decoded) == len(normalized_vector)


@pytest.mark.edge
class TestSymbolicFingerprintEdgeCases:
    
    def test_symbolic_fingerprint_zeros(self):
        zeros = np.zeros(768, dtype=np.float32)
        result = frackture.frackture_symbolic_fingerprint_f_infinity(zeros)
        assert isinstance(result, str)
        assert len(result) == 64
    
    def test_symbolic_fingerprint_ones(self):
        ones = np.ones(768, dtype=np.float32)
        result = frackture.frackture_symbolic_fingerprint_f_infinity(ones)
        assert isinstance(result, str)
        assert len(result) == 64
    
    def test_symbolic_fingerprint_small_vector(self):
        small = np.array([0.5] * 10, dtype=np.float32)
        result = frackture.frackture_symbolic_fingerprint_f_infinity(small)
        assert isinstance(result, str)
    
    def test_symbolic_channel_decode_short_hash(self):
        short_hash = "ab"
        result = frackture.symbolic_channel_decode(short_hash)
        assert len(result) == 768
    
    def test_symbolic_channel_decode_all_zeros(self):
        zeros_hash = "00" * 32
        result = frackture.symbolic_channel_decode(zeros_hash)
        assert len(result) == 768
    
    def test_symbolic_channel_decode_all_max(self):
        max_hash = "ff" * 32
        result = frackture.symbolic_channel_decode(max_hash)
        assert len(result) == 768
    
    def test_symbolic_fingerprint_zero_passes(self, normalized_vector):
        result = frackture.frackture_symbolic_fingerprint_f_infinity(normalized_vector, passes=0)
        assert isinstance(result, str)
