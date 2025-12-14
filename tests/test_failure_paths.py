"""Tests for failure paths and error handling in Frackture."""

import pytest
import numpy as np


class TestFailurePaths:
    """Test failure paths and error handling"""

    def test_malformed_payload_reconstruction(self, malformed_payloads):
        for payload in malformed_payloads:
            with pytest.raises(ValueError):
                frackture_v3_3_reconstruct(payload)

    def test_empty_payload_reconstruction(self):
        with pytest.raises(ValueError):
            frackture_v3_3_reconstruct({})

    def test_none_payload_reconstruction(self):
        with pytest.raises(ValueError):
            frackture_v3_3_reconstruct(None)

    def test_invalid_symbolic_fingerprint(self):
        invalid_payloads = [
            {"symbolic": None, "entropy": [1.0] * 16},
            {"symbolic": "not_hex_string", "entropy": [1.0] * 16},
            {"symbolic": "", "entropy": [1.0] * 16},
            {"symbolic": "xyz", "entropy": [1.0] * 16},
            {"symbolic": "12", "entropy": [1.0] * 16},
            {"symbolic": "12" * 50, "entropy": [1.0] * 16},
        ]

        for payload in invalid_payloads:
            with pytest.raises(ValueError):
                frackture_v3_3_reconstruct(payload)

    def test_invalid_entropy_data(self):
        invalid_payloads = [
            {"symbolic": "a" * 64, "entropy": None},
            {"symbolic": "a" * 64, "entropy": "not_a_list"},
            {"symbolic": "a" * 64, "entropy": []},
            {"symbolic": "a" * 64, "entropy": [float("nan")] * 16},
            {"symbolic": "a" * 64, "entropy": [float("inf")] * 16},
            {"symbolic": "a" * 64, "entropy": ["not_numbers"] * 16},
            {"symbolic": "a" * 64, "entropy": [1, 2, 3] + [4] * 13},
        ]

        for payload in invalid_payloads:
            with pytest.raises(ValueError):
                frackture_v3_3_reconstruct(payload)

    def test_encryption_with_corrupted_data(self):
        key = "corruption_test_key"
        test_data = "corruption test"

        preprocessed = frackture_preprocess_universal_v2_6(test_data)
        payload = frackture_v3_3_safe(preprocessed)
        encrypted = frackture_encrypt_payload(payload, key)

        corruption_tests = [
            # Corrupt signature
            {"data": encrypted["data"], "signature": "invalid", "metadata": encrypted["metadata"]},
            # Corrupt metadata
            {"data": encrypted["data"], "signature": encrypted["signature"], "metadata": {}},
            # Missing data
            {"signature": encrypted["signature"], "metadata": encrypted["metadata"]},
            # Extra data
            {**encrypted, "extra": "hacker_data"},
            # Type corruption
            {"data": "not_dict", "signature": encrypted["signature"], "metadata": encrypted["metadata"]},
        ]

        for corrupted in corruption_tests:
            with pytest.raises(ValueError):
                frackture_decrypt_payload(corrupted, key)

    def test_preprocessing_extreme_values(self):
        extreme_inputs = [
            np.array([float("inf")]),
            np.array([float("-inf")]),
            np.array([float("nan")]),
            np.array([1e308, 1e308]),
            np.array([1e-308, 1e-308]),
        ]

        for test_input in extreme_inputs:
            result = frackture_preprocess_universal_v2_6(test_input)
            assert isinstance(result, np.ndarray)
            assert len(result) == 768
