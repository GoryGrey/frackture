"""
Basic smoke tests for Frackture
"""
import pytest
import numpy as np
import sys
import os
import importlib.util

# Add parent directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

# Import the main module - try new package structure first, fall back to old
try:
    import frackture as frackture_module
except ImportError:
    # Fall back to old module with space in filename
    module_path = os.path.join(os.path.dirname(__file__), '..', 'frackture (2).py')
    spec = importlib.util.spec_from_file_location("frackture_2", module_path)
    frackture_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(frackture_module)

# Expose functions
frackture_preprocess_universal_v2_6 = frackture_module.frackture_preprocess_universal_v2_6
frackture_v3_3_safe = frackture_module.frackture_v3_3_safe
frackture_v3_3_reconstruct = frackture_module.frackture_v3_3_reconstruct

class TestBasic:
    """Basic functionality tests"""
    
    def test_import(self):
        """Test that we can import and use basic functions"""
        assert frackture_preprocess_universal_v2_6 is not None
        assert frackture_v3_3_safe is not None
        assert frackture_v3_3_reconstruct is not None
    
    def test_basic_preprocessing(self):
        """Test basic preprocessing"""
        test_data = "hello world"
        result = frackture_preprocess_universal_v2_6(test_data)
        
        assert isinstance(result, np.ndarray)
        assert len(result) == 768
        assert result.dtype == np.float32
    
    def test_basic_roundtrip(self):
        """Test basic roundtrip"""
        test_data = "hello world"
        
        # Preprocess
        preprocessed = frackture_preprocess_universal_v2_6(test_data)
        
        # Encode
        payload = frackture_v3_3_safe(preprocessed)
        
        # Decode
        reconstructed = frackture_v3_3_reconstruct(payload)
        
        # Verify
        assert isinstance(reconstructed, np.ndarray)
        assert len(reconstructed) == 768