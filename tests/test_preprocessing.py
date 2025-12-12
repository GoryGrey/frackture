"""
Tests for preprocessing edge cases in Frackture
"""
import pytest
import numpy as np
from hypothesis import given, settings
from hypothesis.strategies import text, binary, dictionaries, lists, floats, integers, data, one_of
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from conftest import arbitrary_data

class TestPreprocessing:
    """Test preprocessing functionality across different data types"""
    
    @given(binary())
    @settings(max_examples=100)
    def test_preprocessing_bytes_input(self, data):
        """Test preprocessing with bytes input"""
        result = frackture_preprocess_universal_v2_6(data)
        
        assert isinstance(result, np.ndarray)
        assert len(result) == 768
        assert result.dtype == np.float32
        assert np.all(result >= 0)
        assert np.all(result <= 1)
    
    @given(text())
    @settings(max_examples=100)
    def test_preprocessing_string_input(self, data):
        """Test preprocessing with string input"""
        result = frackture_preprocess_universal_v2_6(data)
        
        assert isinstance(result, np.ndarray)
        assert len(result) == 768
        assert result.dtype == np.float32
        assert np.all(result >= 0)
        assert np.all(result <= 1)
    
    @given(dictionaries(text(), one_of(text(), integers(), floats())))
    @settings(max_examples=100)
    def test_preprocessing_dict_input(self, data):
        """Test preprocessing with dictionary input"""
        result = frackture_preprocess_universal_v2_6(data)
        
        assert isinstance(result, np.ndarray)
        assert len(result) == 768
        assert result.dtype == np.float32
        assert np.all(result >= 0)
        assert np.all(result <= 1)
    
    @given(lists(one_of(integers(), floats())))
    @settings(max_examples=100)
    def test_preprocessing_list_input(self, data):
        """Test preprocessing with list input"""
        result = frackture_preprocess_universal_v2_6(data)
        
        assert isinstance(result, np.ndarray)
        assert len(result) == 768
        assert result.dtype == np.float32
        assert np.all(result >= 0)
        assert np.all(result <= 1)
    
    @given(data())
    @settings(max_examples=100)
    def test_preprocessing_numpy_array_input(self, data):
        """Test preprocessing with numpy array input"""
        # Generate random numpy array
        shape = data.draw(tuples(integers(1, 10), integers(1, 10)))
        array_data = data.draw(lists(floats(), min_size=shape[0]*shape[1], max_size=shape[0]*shape[1]))
        np_array = np.array(array_data).reshape(shape)
        
        result = frackture_preprocess_universal_v2_6(np_array)
        
        assert isinstance(result, np.ndarray)
        assert len(result) == 768
        assert result.dtype == np.float32
        assert np.all(result >= 0)
        assert np.all(result <= 1)
    
    def test_preprocessing_edge_cases(self, adversarial_inputs):
        """Test preprocessing with adversarial inputs"""
        for data in adversarial_inputs:
            result = frackture_preprocess_universal_v2_6(data)
            
            assert isinstance(result, np.ndarray)
            assert len(result) == 768
            assert result.dtype == np.float32
            assert np.all(result >= 0)
            assert np.all(result <= 1)
    
    def test_preprocessing_empty_inputs(self):
        """Test preprocessing with empty inputs"""
        # Empty bytes
        result = frackture_preprocess_universal_v2_6(b"")
        assert len(result) == 768
        assert np.all(result == 0)
        
        # Empty string
        result = frackture_preprocess_universal_v2_6("")
        assert len(result) == 768
        
        # Empty list
        result = frackture_preprocess_universal_v2_6([])
        assert len(result) == 768
        
        # Empty dict
        result = frackture_preprocess_universal_v2_6({})
        assert len(result) == 768
    
    def test_preprocessing_large_arrays(self):
        """Test preprocessing with very large arrays"""
        # Large numpy array
        large_array = np.random.rand(10000)
        result = frackture_preprocess_universal_v2_6(large_array)
        assert len(result) == 768
        assert np.all(result >= 0)
        assert np.all(result <= 1)
        
        # Large list
        large_list = [float(i) for i in range(10000)]
        result = frackture_preprocess_universal_v2_6(large_list)
        assert len(result) == 768
        assert np.all(result >= 0)
        assert np.all(result <= 1)
    
    def test_preprocessing_unicode_handling(self):
        """Test preprocessing with various unicode characters"""
        test_strings = [
            "Hello, 世界! 🌍",
            "Café résumé naïve",
            "Ñoño año",
            "Здра́вствуйте мир",  # Russian
            "नमस्ते दुनिया",  # Hindi
            "أهلاً بالعالم",  # Arabic
        ]
        
        for test_str in test_strings:
            result = frackture_preprocess_universal_v2_6(test_str)
            assert isinstance(result, np.ndarray)
            assert len(result) == 768
            assert result.dtype == np.float32
            assert np.all(result >= 0)
            assert np.all(result <= 1)
    
    def test_preprocessing_special_objects(self):
        """Test preprocessing with special Python objects"""
        # Test various special objects
        special_objects = [
            None,
            True,
            False,
            42,
            3.14159,
            complex(1, 2),
        ]
        
        for obj in special_objects:
            result = frackture_preprocess_universal_v2_6(obj)
            assert isinstance(result, np.ndarray)
            assert len(result) == 768
            assert result.dtype == np.float32
            assert np.all(result >= 0)
            assert np.all(result <= 1)
    
    def test_preprocessing_reproducibility(self):
        """Test that preprocessing produces consistent results"""
        test_data = "consistent test data"
        
        result1 = frackture_preprocess_universal_v2_6(test_data)
        result2 = frackture_preprocess_universal_v2_6(test_data)
        
        np.testing.assert_array_equal(result1, result2)
    
    def test_preprocessing_normalization(self):
        """Test that preprocessing properly normalizes data"""
        # Test with data that has very large range
        large_data = np.array([0.0, 1.0, 1000.0, 1000000.0])
        result = frackture_preprocess_universal_v2_6(large_data)
        
        assert np.all(result >= 0)
        assert np.all(result <= 1)
        
        # Test with data that has negative values
        negative_data = np.array([-1000.0, -1.0, 0.0, 1.0, 1000.0])
        result = frackture_preprocess_universal_v2_6(negative_data)
        
        assert np.all(result >= 0)
        assert np.all(result <= 1)
    
    def test_preprocessing_padding(self):
        """Test that preprocessing properly pads data to 768 elements"""
        # Test with small data
        small_data = np.array([1.0, 2.0, 3.0])
        result = frackture_preprocess_universal_v2_6(small_data)
        assert len(result) == 768
        
        # Test with data that's not a multiple of 768
        medium_data = np.random.rand(500)
        result = frackture_preprocess_universal_v2_6(medium_data)
        assert len(result) == 768
        
        # The padding should preserve the wrap pattern
        expected_length = 768
        assert len(result) == expected_length