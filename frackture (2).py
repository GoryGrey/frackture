import copy
import hashlib
import hmac
import json
import math
from typing import Any, Dict, Iterable, Optional, Union

import numpy as np
from scipy.fft import fft

_FRACKTURE_SYMBOLIC_HEX_LEN = 64
_FRACKTURE_ENTROPY_LEN = 16
_FRACKTURE_ENCRYPTION_VERSION = 1

_UNSET = object()


def _key_to_bytes(key: Union[str, bytes, bytearray]) -> bytes:
    if isinstance(key, (bytes, bytearray)):
        return bytes(key)
    if isinstance(key, str):
        return key.encode("utf-8")
    raise ValueError("Key must be str or bytes")


def _compute_key_id(key_bytes: bytes) -> str:
    return hashlib.sha256(key_bytes).hexdigest()[:8]


def _canonical_json_bytes(obj: Any) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":")).encode("utf-8")


def validate_frackture_payload(
    payload: Optional[Dict[str, Any]] = None,
    *,
    symbolic: Any = _UNSET,
    entropy: Any = _UNSET,
) -> None:
    """Validate raw Frackture payload structure.

    Valid payloads must have:
      - symbolic: 64-char hex string
      - entropy: 16 finite numeric values

    Payloads may optionally include tier metadata keys:
      - tier_name, category_name, actual_size_bytes, target_size_bytes

    Raises ValueError on any corruption/mismatch.
    """

    if payload is not None:
        if not isinstance(payload, dict):
            raise ValueError("Frackture payload must be a dict")
        if "symbolic" not in payload or "entropy" not in payload:
            raise ValueError("Frackture payload missing required keys")
        symbolic = payload["symbolic"]
        entropy = payload["entropy"]

        for key in ("tier_name", "category_name"):
            if key in payload and payload[key] is not None and not isinstance(payload[key], str):
                raise ValueError(f"Invalid payload metadata: {key}")

        for key in ("actual_size_bytes", "target_size_bytes"):
            if key in payload and payload[key] is not None:
                value = payload[key]
                if not isinstance(value, (int, np.integer)):
                    raise ValueError(f"Invalid payload metadata: {key}")
                if int(value) < 0:
                    raise ValueError(f"Invalid payload metadata: {key}")

    if symbolic is not _UNSET:
        if not isinstance(symbolic, str):
            raise ValueError("Invalid symbolic fingerprint")
        if len(symbolic) != _FRACKTURE_SYMBOLIC_HEX_LEN:
            raise ValueError("Invalid symbolic fingerprint")
        try:
            raw = bytes.fromhex(symbolic)
        except ValueError as e:
            raise ValueError("Invalid symbolic fingerprint") from e
        if len(raw) != _FRACKTURE_SYMBOLIC_HEX_LEN // 2:
            raise ValueError("Invalid symbolic fingerprint")

    if entropy is not _UNSET:
        if isinstance(entropy, np.ndarray):
            entropy_iter: Iterable[Any] = entropy.tolist()
        else:
            entropy_iter = entropy

        if not isinstance(entropy_iter, (list, tuple)):
            raise ValueError("Invalid entropy channel")
        if len(entropy_iter) != _FRACKTURE_ENTROPY_LEN:
            raise ValueError("Invalid entropy channel")

        for value in entropy_iter:
            try:
                f = float(value)
            except (TypeError, ValueError) as e:
                raise ValueError("Invalid entropy channel") from e
            if not math.isfinite(f):
                raise ValueError("Invalid entropy channel")


def _normalize_frackture_payload(payload: Dict[str, Any]) -> Dict[str, Any]:
    validate_frackture_payload(payload)

    normalized = copy.deepcopy(payload)
    normalized["entropy"] = [float(x) for x in normalized["entropy"]]

    for key in ("actual_size_bytes", "target_size_bytes"):
        if key in normalized and normalized[key] is not None:
            normalized[key] = int(normalized[key])

    return normalized


### === Preprocessing === ###
def frackture_preprocess_universal_v2_6(data):
    try:
        if isinstance(data, str):
            vec = np.frombuffer(data.encode("utf-8"), dtype=np.uint8)
        elif isinstance(data, dict):
            flat = str(sorted(data.items()))
            vec = np.frombuffer(flat.encode("utf-8"), dtype=np.uint8)
        elif isinstance(data, bytes):
            vec = np.frombuffer(data, dtype=np.uint8)
        elif isinstance(data, list):
            vec = np.array(data, dtype=np.float32).flatten()
        elif isinstance(data, np.ndarray):
            vec = data.flatten()
        else:
            vec = np.frombuffer(str(data).encode("utf-8"), dtype=np.uint8)
        normed = vec.astype(np.float32)
        normed = (normed - np.min(normed)) / (np.ptp(normed) + 1e-8)
        padded = np.pad(normed, (0, 768 - len(normed) % 768), mode="wrap")
        return padded[:768]
    except Exception:
        return np.zeros(768, dtype=np.float32)


### === Symbolic Fingerprinting System === ###
def frackture_symbolic_fingerprint_f_infinity(input_vector, passes=4):
    bits = (input_vector * 255).astype(np.uint8)
    mask = np.array([(i**2 + i * 3 + 1) % 256 for i in range(len(bits))], dtype=np.uint8)
    for p in range(passes):
        rotated = np.roll(bits ^ mask, p * 17)
        entropy_mixed = (rotated * ((p + 1) ** 2)).astype(np.uint16) % 256
        chunks = np.array_split(entropy_mixed, 32)
        folded = [np.bitwise_xor.reduce(chunk) for chunk in chunks]
        fingerprint = "".join(f"{x:02x}" for x in folded)
        bits = (entropy_mixed + folded[p % len(folded)]) % 256
    return fingerprint


def symbolic_channel_encode(input_vector):
    return frackture_symbolic_fingerprint_f_infinity(input_vector)


def symbolic_channel_decode(symbolic_hash):
    validate_frackture_payload(symbolic=symbolic_hash)

    try:
        decoded = [int(symbolic_hash[i : i + 2], 16) / 255.0 for i in range(0, len(symbolic_hash), 2)]
    except (ValueError, IndexError) as e:
        raise ValueError("Corrupted symbolic fingerprint") from e

    return np.array((decoded * (768 // len(decoded) + 1))[:768], dtype=np.float32)


### === Entropy Channel System === ###
def entropy_channel_encode(input_vector):
    fft_vector = np.abs(fft(input_vector))

    if len(fft_vector) >= 16:
        chunk_size = len(fft_vector) // 16
        chunks = [
            fft_vector[i : i + chunk_size]
            for i in range(0, len(fft_vector) - chunk_size + 1, chunk_size)
        ]

        while len(chunks) < 16:
            chunks.append(fft_vector[:chunk_size])
        chunks = chunks[:16]

        features = []
        for chunk in chunks:
            features.extend([np.mean(chunk), np.std(chunk), np.max(chunk), np.min(chunk)])

        features = features[:16]
    else:
        features = []
        for i in range(16):
            if i < len(fft_vector):
                features.append(fft_vector[i])
            else:
                features.append(fft_vector[i % len(fft_vector)])

    if len(features) < 16:
        features.extend([np.mean(fft_vector)] * (16 - len(features)))
    elif len(features) > 16:
        features = features[:16]

    return [float(x) for x in features]


def entropy_channel_decode(entropy_data):
    validate_frackture_payload(entropy=entropy_data)

    ent = np.array([float(x) for x in entropy_data], dtype=np.float32)
    expanded = np.tile(ent, 48)[:768]

    if not np.all(np.isfinite(expanded)):
        raise ValueError("Corrupted entropy channel")

    normed = (expanded - np.min(expanded)) / (np.ptp(expanded) + 1e-8)
    return normed.astype(np.float32)


### === Reconstruction Combiner === ###
def merge_reconstruction(entropy_vec, symbolic_vec):
    merged = (np.array(entropy_vec) + np.array(symbolic_vec)) / 2
    return merged


### === Core Frackture Compression Functions === ###
def frackture_v3_3_safe(input_vector):
    return {"symbolic": symbolic_channel_encode(input_vector), "entropy": entropy_channel_encode(input_vector)}


def frackture_v3_3_reconstruct(payload):
    validate_frackture_payload(payload)

    entropy_part = entropy_channel_decode(payload["entropy"])
    symbolic_part = symbolic_channel_decode(payload["symbolic"])
    return merge_reconstruction(entropy_part, symbolic_part)


### === Self-Optimization (Decoder Loss Feedback Loop) === ###
def optimize_frackture(input_vector, num_trials=5):
    best_payload = None
    best_mse = float("inf")
    for trial in range(num_trials):
        symbolic = frackture_symbolic_fingerprint_f_infinity(input_vector, passes=trial + 2)
        entropy = entropy_channel_encode(input_vector)
        payload = {"symbolic": symbolic, "entropy": entropy}
        recon = frackture_v3_3_reconstruct(payload)
        mse = np.mean((input_vector - recon) ** 2)
        if mse < best_mse:
            best_mse = mse
            best_payload = payload
    return best_payload, best_mse


### === Hashing Functions === ###
def frackture_deterministic_hash(data, salt=""):
    """Generate deterministic hash for collision testing"""

    data_str = str(data) + salt
    return hashlib.sha256(data_str.encode()).hexdigest()


### === Encryption/Decryption Functions === ###
def frackture_encrypt_payload(payload, key):
    """Wrap and authenticate a payload with an HMAC-SHA256 signature."""

    normalized_payload = _normalize_frackture_payload(payload)

    key_bytes = _key_to_bytes(key)
    metadata = {"version": _FRACKTURE_ENCRYPTION_VERSION, "key_id": _compute_key_id(key_bytes)}

    to_sign = {"data": normalized_payload, "metadata": metadata}
    signature = hmac.new(key_bytes, _canonical_json_bytes(to_sign), hashlib.sha256).hexdigest()

    return {"data": normalized_payload, "signature": signature, "metadata": metadata}


def frackture_verify_encrypted_payload(encrypted_payload: Any) -> None:
    if not isinstance(encrypted_payload, dict):
        raise ValueError("Invalid encrypted payload")

    if set(encrypted_payload.keys()) != {"data", "signature", "metadata"}:
        raise ValueError("Invalid encrypted payload")

    metadata = encrypted_payload.get("metadata")
    if not isinstance(metadata, dict):
        raise ValueError("Invalid encrypted payload")

    if set(metadata.keys()) != {"version", "key_id"}:
        raise ValueError("Invalid encrypted payload")

    if metadata.get("version") != _FRACKTURE_ENCRYPTION_VERSION:
        raise ValueError("Unsupported encrypted payload version")

    key_id = metadata.get("key_id")
    if not isinstance(key_id, str) or len(key_id) != 8:
        raise ValueError("Invalid encrypted payload")

    signature = encrypted_payload.get("signature")
    if not isinstance(signature, str):
        raise ValueError("Invalid encrypted payload")
    try:
        sig_bytes = bytes.fromhex(signature)
    except ValueError as e:
        raise ValueError("Invalid encrypted payload") from e
    if len(sig_bytes) != 32:
        raise ValueError("Invalid encrypted payload")

    data = encrypted_payload.get("data")
    if not isinstance(data, dict):
        raise ValueError("Invalid encrypted payload")

    validate_frackture_payload(data)


def frackture_verify_payload_integrity(encrypted_payload: Any, key: Union[str, bytes, bytearray]) -> None:
    frackture_verify_encrypted_payload(encrypted_payload)

    key_bytes = _key_to_bytes(key)

    expected_key_id = _compute_key_id(key_bytes)
    if encrypted_payload["metadata"]["key_id"] != expected_key_id:
        raise ValueError("Key mismatch")

    to_sign = {"data": encrypted_payload["data"], "metadata": encrypted_payload["metadata"]}
    expected_signature = hmac.new(key_bytes, _canonical_json_bytes(to_sign), hashlib.sha256).hexdigest()

    if not hmac.compare_digest(encrypted_payload["signature"], expected_signature):
        raise ValueError("Invalid key or corrupted payload")


def frackture_decrypt_payload(encrypted_payload, key):
    """Verify and unwrap an encrypted payload."""

    frackture_verify_payload_integrity(encrypted_payload, key)
    return copy.deepcopy(encrypted_payload["data"])
