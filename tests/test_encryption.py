"""
Tests for encryption mode and security functionality
"""

import copy

import pytest
from hypothesis import given, settings
from hypothesis.strategies import text


class TestEncryption:
    """Test encryption/decryption functionality"""

    def test_encryption_basic_functionality(self, small_data, encryption_keys):
        preprocessed = frackture_preprocess_universal_v2_6(small_data)
        payload = frackture_v3_3_safe(preprocessed)

        for key in encryption_keys:
            encrypted = frackture_encrypt_payload(payload, key)

            assert isinstance(encrypted, dict)
            assert set(encrypted.keys()) == {"data", "signature", "metadata"}
            assert encrypted["data"] == payload
            assert "key_id" in encrypted["metadata"]
            assert "version" in encrypted["metadata"]

            decrypted = frackture_decrypt_payload(encrypted, key)
            assert decrypted == payload

    def test_encryption_wrong_key_rejection(self, small_data):
        correct_key = "correct_key"
        wrong_key = "wrong_key"

        preprocessed = frackture_preprocess_universal_v2_6(small_data)
        payload = frackture_v3_3_safe(preprocessed)

        encrypted = frackture_encrypt_payload(payload, correct_key)

        with pytest.raises(ValueError):
            frackture_decrypt_payload(encrypted, wrong_key)

    def test_encryption_key_mismatch_detection(self):
        key = "key1"
        test_data = "key mismatch test"

        preprocessed = frackture_preprocess_universal_v2_6(test_data)
        payload = frackture_v3_3_safe(preprocessed)

        encrypted = frackture_encrypt_payload(payload, key)
        encrypted["metadata"]["key_id"] = "deadbeef"  # valid-length but wrong key id

        with pytest.raises(ValueError):
            frackture_decrypt_payload(encrypted, key)

    def test_encryption_payload_tamper_detection(self, encryption_keys):
        key = encryption_keys[0]
        test_data = "tamper detection test"

        preprocessed = frackture_preprocess_universal_v2_6(test_data)
        payload = frackture_v3_3_safe(preprocessed)
        encrypted = frackture_encrypt_payload(payload, key)

        # Tamper with the payload but keep it structurally valid (HMAC must catch it)
        tampered = copy.deepcopy(encrypted)
        sym = tampered["data"]["symbolic"]
        tampered["data"]["symbolic"] = ("0" if sym[0] != "0" else "1") + sym[1:]

        with pytest.raises(ValueError):
            frackture_decrypt_payload(tampered, key)

    def test_encryption_metadata_consistency(self, encryption_keys):
        test_data = "metadata consistency test"
        preprocessed = frackture_preprocess_universal_v2_6(test_data)
        payload = frackture_v3_3_safe(preprocessed)

        for key in encryption_keys:
            encrypted1 = frackture_encrypt_payload(payload, key)
            encrypted2 = frackture_encrypt_payload(payload, key)

            assert encrypted1["metadata"]["key_id"] == encrypted2["metadata"]["key_id"]
            assert encrypted1["metadata"]["version"] == encrypted2["metadata"]["version"]

    def test_encryption_signature_uniqueness(self):
        key = "test_key"

        payload1 = frackture_v3_3_safe(frackture_preprocess_universal_v2_6("first payload"))
        payload2 = frackture_v3_3_safe(frackture_preprocess_universal_v2_6("second payload"))

        encrypted1 = frackture_encrypt_payload(payload1, key)
        encrypted2 = frackture_encrypt_payload(payload2, key)

        assert encrypted1["signature"] != encrypted2["signature"]

    def test_encryption_signature_determinism(self):
        key = "test_key"
        payload = frackture_v3_3_safe(frackture_preprocess_universal_v2_6("signature determinism test"))

        encrypted1 = frackture_encrypt_payload(payload, key)
        encrypted2 = frackture_encrypt_payload(payload, key)

        assert encrypted1["signature"] == encrypted2["signature"]

    @given(text(min_size=1, max_size=1000))
    @settings(max_examples=50)
    def test_encryption_property_based(self, test_data):
        key = "property_test_key"

        preprocessed = frackture_preprocess_universal_v2_6(test_data)
        payload = frackture_v3_3_safe(preprocessed)

        encrypted = frackture_encrypt_payload(payload, key)
        decrypted = frackture_decrypt_payload(encrypted, key)

        assert decrypted == payload
        assert isinstance(encrypted, dict)
        assert set(encrypted.keys()) == {"data", "signature", "metadata"}

    def test_encryption_adversarial_inputs(self, adversarial_inputs):
        key = "adversarial_test_key"

        for test_data in adversarial_inputs:
            preprocessed = frackture_preprocess_universal_v2_6(test_data)
            payload = frackture_v3_3_safe(preprocessed)

            encrypted = frackture_encrypt_payload(payload, key)
            decrypted = frackture_decrypt_payload(encrypted, key)
            assert decrypted == payload

    def test_encryption_empty_payload(self):
        key = "empty_test_key"

        minimal_payload = {"symbolic": "a" * 64, "entropy": [1.0] * 16}

        encrypted = frackture_encrypt_payload(minimal_payload, key)
        decrypted = frackture_decrypt_payload(encrypted, key)

        assert decrypted == minimal_payload

    def test_encryption_hmac_security(self):
        key = "hmac_security_test"
        payload = frackture_v3_3_safe(frackture_preprocess_universal_v2_6("HMAC security test"))
        encrypted = frackture_encrypt_payload(payload, key)

        tamper_tests = [
            # Modify signature
            lambda e: e.update({"signature": "0" * 64}),
            # Modify data
            lambda e: e["data"].update({"symbolic": ("0" if e["data"]["symbolic"][0] != "0" else "1") + e["data"]["symbolic"][1:]}),
            # Modify metadata
            lambda e: e["metadata"].update({"key_id": "deadbeef"}),
            # Add extra field
            lambda e: e.update({"extra_field": "hacker"}),
            # Remove required field
            lambda e: e.pop("signature"),
        ]

        for tamper in tamper_tests:
            tampered_encrypted = copy.deepcopy(encrypted)
            tamper(tampered_encrypted)

            with pytest.raises(ValueError):
                frackture_decrypt_payload(tampered_encrypted, key)

    def test_encryption_key_strength_variation(self):
        test_data = "key strength test"
        preprocessed = frackture_preprocess_universal_v2_6(test_data)
        payload = frackture_v3_3_safe(preprocessed)

        keys = [
            "a",
            "a" * 256,
            "unicode_🎉_key",
            "Key With Spaces",
            "key\nwith\tcontrol",
        ]

        for key in keys:
            encrypted = frackture_encrypt_payload(payload, key)
            decrypted = frackture_decrypt_payload(encrypted, key)
            assert decrypted == payload

    def test_encryption_rejects_invalid_payload(self):
        key = "invalid_payload_key"

        payload_with_none = {"symbolic": None, "entropy": [None] * 16}
        with pytest.raises(ValueError):
            frackture_encrypt_payload(payload_with_none, key)

    def test_verify_helpers(self):
        key = "verify_helpers_key"
        payload = frackture_v3_3_safe(frackture_preprocess_universal_v2_6("verify helpers test"))
        encrypted = frackture_encrypt_payload(payload, key)

        frackture_verify_encrypted_payload(encrypted)
        frackture_verify_payload_integrity(encrypted, key)

        tampered = copy.deepcopy(encrypted)
        tampered["signature"] = "0" * 64
        with pytest.raises(ValueError):
            frackture_verify_payload_integrity(tampered, key)
