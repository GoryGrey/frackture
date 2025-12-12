"""
Pytest configuration and shared fixtures for Frackture tests
"""
import pytest
import numpy as np
from hypothesis import settings, strategies as st
from hypothesis.strategies import integers, floats, text, binary, lists, dictionaries
import json
import os
import sys
import importlib.util

# Add the parent directory to sys.path so we can import the main module
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

# Expose all functions from the module
globals().update({name: getattr(frackture_module, name) for name in dir(frackture_module) if not name.startswith('_')})

@pytest.fixture
def small_data():
    """Small test data for basic operations"""
    return b"hello world"

@pytest.fixture
def medium_data():
    """Medium-sized test data"""
    return b"this is a moderately sized test data for compression testing" * 10

@pytest.fixture
def large_data():
    """Large test data to test performance and edge cases"""
    return os.urandom(1024 * 100)  # 100KB of random data

@pytest.fixture
def adversarial_inputs():
    """Adversarial inputs for testing edge cases"""
    return [
        b"",  # Empty data
        b"\x00" * 100,  # All zeros
        b"\xff" * 100,  # All ones
        b"\x00\x01\x02" * 1000,  # Repeating pattern
        "unicode test: 🎉 ñáéíóú".encode('utf-8'),  # Unicode data
        "混合内容测试".encode('utf-8'),  # Non-Latin text
        json.dumps({"nested": {"data": [1, 2, {"complex": True}]}}).encode(),  # Complex JSON
    ]

@pytest.fixture
def dict_inputs():
    """Dictionary inputs for preprocessing tests"""
    return [
        {"key": "value"},
        {"a": 1, "b": [2, 3, 4], "c": {"nested": "dict"}},
        {i: f"value_{i}" for i in range(100)},  # Large dict
        {},  # Empty dict
    ]

@pytest.fixture
def array_inputs():
    """Array inputs for preprocessing tests"""
    return [
        [1, 2, 3, 4, 5],
        np.random.rand(50),
        np.random.rand(100, 3),  # 2D array
        np.zeros(100),
        np.ones(50) * 42.5,
        [],  # Empty list
        np.array([]),  # Empty numpy array
    ]

@pytest.fixture
def encryption_keys():
    """Test encryption keys"""
    return [
        "test_key_123",
        "complex_key_with_unicode_🎉",
        "a" * 100,  # Long key
        "short",  # Short key
    ]

@pytest.fixture
def malformed_payloads():
    """Malformed payloads for failure testing"""
    return [
        {"missing_keys": True},  # Missing required keys
        {"symbolic": "invalid_hex", "entropy": [1.0, 2.0]},  # Invalid symbolic format
        {"symbolic": "a" * 64, "entropy": "not_a_list"},  # Invalid entropy format
        {"symbolic": None, "entropy": [1.0]},  # None values
        {"symbolic": "a" * 64, "entropy": [float('nan')]},  # NaN values
        {"symbolic": "a" * 64, "entropy": [float('inf')]},  # Infinity values
    ]

# Hypothesis strategy for generating diverse test data
@st.composite
def arbitrary_data(draw):
    """Hypothesis strategy for generating arbitrary test data"""
    data_type = draw(st.sampled_from(['bytes', 'str', 'dict', 'list', 'numpy']))
    
    if data_type == 'bytes':
        return os.urandom(draw(st.integers(min_value=1, max_value=1000)))
    elif data_type == 'str':
        return draw(st.text(min_size=1, max_size=1000))
    elif data_type == 'dict':
        return dict(zip(
            draw(st.lists(st.text(min_size=1, max_size=10), min_size=1, max_size=50)),
            draw(st.lists(st.one_of(st.text(), st.integers(), st.floats()), min_size=1, max_size=50))
        ))
    elif data_type == 'list':
        return draw(st.lists(st.one_of(st.integers(), st.floats(), st.text()), min_size=1, max_size=100))
    elif data_type == 'numpy':
        return np.random.rand(draw(st.integers(min_value=1, max_value=100)))

# Hypothesis settings
settings.register_profile("fast", max_examples=50)
settings.register_profile("coverage", max_examples=200)
settings.load_profile("coverage")

# Helper functions for tests
def assert_fixed_fingerprint_length(fingerprint):
    """Assert that a fingerprint maintains fixed length"""
    assert isinstance(fingerprint, str)
    # Fingerprint should be hex-encoded, so length should be even
    assert len(fingerprint) % 2 == 0
    # Verify it's valid hex
    try:
        bytes.fromhex(fingerprint)
    except ValueError:
        assert False, f"Invalid hex fingerprint: {fingerprint}"

def assert_mse_not_degraded(baseline_mse, optimized_mse):
    """Assert that optimization doesn't degrade MSE"""
    assert optimized_mse <= baseline_mse, f"MSE degraded: {baseline_mse} -> {optimized_mse}"

def assert_reconstruction_preserves_properties(original, reconstructed, tolerance=1e-6):
    """Assert that reconstruction preserves important properties"""
    assert isinstance(reconstructed, np.ndarray)
    assert len(reconstructed) == 768
    assert np.all(reconstructed >= 0), "Reconstructed values should be non-negative"
    assert np.all(reconstructed <= 1), "Reconstructed values should be in [0, 1] range"