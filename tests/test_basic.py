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

# Import the main module (handling the space in filename)
module_path = os.path.join(os.path.dirname(__file__), '..', 'frackture (2).py')
spec = importlib.util.spec_from_file_location("frackture_2", module_path)
frackture_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(frackture_module)

# Expose functions
frackture_preprocess_universal_v2_6 = frackture_module.frackture_preprocess_universal_v2_6
frackture_v3_3_safe = frackture_module.frackture_v3_3_safe
frackture_v3_3_reconstruct = frackture_module.frackture_v3_3_reconstruct
CompressionTier = frackture_module.CompressionTier
select_tier = frackture_module.select_tier

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


class TestTinyTier:
    """Tests for tiny tier (<100 bytes) compression mode"""
    
    def test_tier_detection_tiny(self):
        """Test that tier selector correctly identifies tiny inputs"""
        tiny_data = b"x" * 50  # 50 bytes
        detected_tier = select_tier(tiny_data)
        assert detected_tier == CompressionTier.TINY
    
    def test_tier_detection_default(self):
        """Test that tier selector correctly identifies default inputs"""
        default_data = b"x" * 1000  # 1 KB
        detected_tier = select_tier(default_data)
        assert detected_tier == CompressionTier.DEFAULT
    
    def test_tier_detection_large(self):
        """Test that tier selector correctly identifies large inputs"""
        large_data = b"x" * (11 * 1024 * 1024)  # 11 MB
        detected_tier = select_tier(large_data)
        assert detected_tier == CompressionTier.LARGE
    
    def test_tiny_preprocessing(self):
        """Test that tiny tier preprocessing uses hash-based padding"""
        tiny_data = b"hello"  # 5 bytes
        
        # Preprocess with explicit tiny tier
        preprocessed = frackture_preprocess_universal_v2_6(tiny_data, tier=CompressionTier.TINY)
        
        # Should still produce 768-length vector
        assert isinstance(preprocessed, np.ndarray)
        assert len(preprocessed) == 768
        assert preprocessed.dtype == np.float32
        
        # Should be normalized [0, 1]
        assert np.all(preprocessed >= 0)
        assert np.all(preprocessed <= 1)
    
    def test_tiny_auto_detection(self):
        """Test that tiny inputs automatically set tier_name to 'tiny' (or 'micro' for <50 bytes)"""
        tiny_data = b"test"  # 4 bytes
        
        # Auto-detect tier
        tier = select_tier(tiny_data)
        # 4 bytes should be detected as MICRO tier with new micro-tier optimization
        assert tier in [CompressionTier.TINY, CompressionTier.MICRO]
        
        # Preprocess with auto-detected tier
        preprocessed = frackture_preprocess_universal_v2_6(tiny_data, tier=tier)
        
        # Encode with auto-detected tier
        payload = frackture_v3_3_safe(preprocessed, tier=tier)
        
        # Should have tier_name='tiny' or 'micro' (FrackturePayload format)
        assert hasattr(payload, 'tier_name')
        assert payload.tier_name in ["tiny", "micro"]
    
    def test_tiny_manual_tier_override(self):
        """Test that tier can be manually overridden"""
        data = b"test"
        
        # Force default tier even though input is tiny
        preprocessed = frackture_preprocess_universal_v2_6(data, tier=CompressionTier.DEFAULT)
        payload = frackture_v3_3_safe(preprocessed, tier=CompressionTier.DEFAULT)
        
        # Should have tier_name='default' (FrackturePayload format)
        assert hasattr(payload, 'tier_name')
        assert payload.tier_name == "default"
    
    def test_tiny_reconstruction_stability(self):
        """Test that reconstruction produces stable, valid output for tiny inputs"""
        tiny_data = b"tiny"  # 4 bytes
        
        # Preprocess and encode
        preprocessed = frackture_preprocess_universal_v2_6(tiny_data)
        payload = frackture_v3_3_safe(preprocessed)
        
        # Multiple reconstructions should be identical
        recon1 = frackture_v3_3_reconstruct(payload)
        recon2 = frackture_v3_3_reconstruct(payload)
        
        # Check they're identical
        assert np.allclose(recon1, recon2)
        
        # Check properties
        assert len(recon1) == 768
        assert np.all(np.isfinite(recon1))
    
    def test_tiny_vs_default_tier_difference(self):
        """Test that tiny tier produces different encoding than default tier"""
        data = b"test"  # Small enough to be tiny
        
        # Encode as tiny
        tiny_preprocessed = frackture_preprocess_universal_v2_6(data, tier=CompressionTier.TINY)
        tiny_payload = frackture_v3_3_safe(tiny_preprocessed, tier=CompressionTier.TINY)
        
        # Encode as default
        default_preprocessed = frackture_preprocess_universal_v2_6(data, tier=CompressionTier.DEFAULT)
        default_payload = frackture_v3_3_safe(default_preprocessed, tier=CompressionTier.DEFAULT)
        
        # Symbolic fingerprints should differ (different processing)
        assert tiny_payload.symbolic != default_payload.symbolic
        
        # But both should be valid 64-char hex (when converted to hex)
        assert len(tiny_payload.symbolic.hex()) == 64
        assert len(default_payload.symbolic.hex()) == 64