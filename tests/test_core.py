"""Tests for Frackture core functionality."""

import numpy as np

from frackture import (
    compress,
    decompress,
    frackture_preprocess_universal_v2_6,
    frackture_v3_3_reconstruct,
    frackture_v3_3_safe,
    optimize_frackture,
)


def test_preprocess_string():
    """Test preprocessing of string input."""
    data = "hello world"
    result = frackture_preprocess_universal_v2_6(data)
    assert isinstance(result, np.ndarray)
    assert result.shape == (768,)
    assert result.dtype == np.float32


def test_preprocess_bytes():
    """Test preprocessing of bytes input."""
    data = b"hello world"
    result = frackture_preprocess_universal_v2_6(data)
    assert isinstance(result, np.ndarray)
    assert result.shape == (768,)


def test_preprocess_dict():
    """Test preprocessing of dict input."""
    data = {"key": "value", "num": 42}
    result = frackture_preprocess_universal_v2_6(data)
    assert isinstance(result, np.ndarray)
    assert result.shape == (768,)


def test_preprocess_list():
    """Test preprocessing of list input."""
    data = [1.0, 2.0, 3.0, 4.0, 5.0]
    result = frackture_preprocess_universal_v2_6(data)
    assert isinstance(result, np.ndarray)
    assert result.shape == (768,)


def test_preprocess_ndarray():
    """Test preprocessing of numpy array input."""
    data = np.random.random(100)
    result = frackture_preprocess_universal_v2_6(data)
    assert isinstance(result, np.ndarray)
    assert result.shape == (768,)


def test_preprocess_normalized():
    """Test that preprocessed output is normalized."""
    data = "test data"
    result = frackture_preprocess_universal_v2_6(data)
    assert np.min(result) >= 0.0
    assert np.max(result) <= 1.0


def test_compress_decompress_bytes():
    """Test basic compress/decompress cycle."""
    data = b"Hello world. This is a test."
    compressed = compress(data)
    assert isinstance(compressed, dict)
    assert "symbolic" in compressed
    assert "entropy" in compressed

    reconstructed = decompress(compressed)
    assert isinstance(reconstructed, np.ndarray)
    assert reconstructed.shape == (768,)


def test_compress_decompress_string():
    """Test compress/decompress with string."""
    data = "Hello world"
    compressed = compress(data)
    reconstructed = decompress(compressed)
    assert isinstance(reconstructed, np.ndarray)
    assert reconstructed.shape == (768,)


def test_frackture_v3_3_safe():
    """Test frackture_v3_3_safe compression."""
    data = np.random.random(768)
    payload = frackture_v3_3_safe(data)

    assert isinstance(payload, dict)
    assert "symbolic" in payload
    assert "entropy" in payload
    assert isinstance(payload["symbolic"], str)
    assert isinstance(payload["entropy"], list)


def test_frackture_v3_3_reconstruct():
    """Test frackture_v3_3_reconstruct."""
    data = np.random.random(768)
    payload = frackture_v3_3_safe(data)
    reconstructed = frackture_v3_3_reconstruct(payload)

    assert isinstance(reconstructed, np.ndarray)
    assert reconstructed.shape == (768,)


def test_optimize_frackture():
    """Test optimize_frackture function."""
    data = np.random.random(768)
    payload, mse = optimize_frackture(data, num_trials=3)

    assert isinstance(payload, dict)
    assert "symbolic" in payload
    assert "entropy" in payload
    assert isinstance(mse, (int, float))
    assert mse >= 0.0


def test_symbolic_fingerprint_deterministic():
    """Test that symbolic fingerprint is deterministic."""
    data = np.random.random(768)
    payload1 = frackture_v3_3_safe(data)
    payload2 = frackture_v3_3_safe(data)

    assert payload1["symbolic"] == payload2["symbolic"]


def test_entropy_encoding_fixed_size():
    """Test that entropy encoding produces fixed size output."""
    data = np.random.random(768)
    payload = frackture_v3_3_safe(data)

    assert len(payload["entropy"]) == 16
