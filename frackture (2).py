import copy
import hashlib
import hmac
import json
import math
import struct
from dataclasses import dataclass, asdict
from enum import Enum
from typing import Any, Dict, Iterable, Optional, Union, Iterator

import numpy as np
from scipy.fft import fft

_FRACKTURE_SYMBOLIC_HEX_LEN = 64
_FRACKTURE_ENTROPY_LEN = 16
_FRACKTURE_ENCRYPTION_VERSION = 1

_UNSET = object()


class CompressionTier(Enum):
    """Enumeration of compression tiers based on input size."""
    TINY = "tiny"        # < 100 bytes
    DEFAULT = "default"  # 100 bytes - 10 MB
    LARGE = "large"      # 10+ MB


### === Compact Payload Format === ###
@dataclass
class FrackturePayload:
    """
    Compact payload format for Frackture compression.
    
    Stores the same data as the legacy dict format but in a more efficient
    binary format suitable for serialization.
    
    For backward compatibility, also supports dict-like access.
    """
    symbolic: bytes  # 32 bytes raw
    entropy: list  # 16 float32 values quantized to uint16
    tier_name: str  # Tier metadata
    version: int = 1  # Payload format version
    
    def __getitem__(self, key):
        """Allow dict-like access for backward compatibility."""
        if key == "symbolic":
            return self.symbolic.hex()  # Return hex string for compatibility
        elif key == "entropy":
            return [float(x) / 1000.0 for x in self.entropy]  # Dequantize to floats
        elif key == "tier_name":
            return self.tier_name
        else:
            raise KeyError(f"'{key}'")
    
    def __contains__(self, key):
        """Allow 'in' operator for backward compatibility."""
        return key in ("symbolic", "entropy", "tier_name")
    
    def keys(self):
        """Return dict-like keys for backward compatibility."""
        return ("symbolic", "entropy", "tier_name")
    
    def values(self):
        """Return dict-like values for backward compatibility."""
        return (self.__getitem__("symbolic"), self.__getitem__("entropy"), self.__getitem__("tier_name"))
    
    def items(self):
        """Return dict-like items for backward compatibility."""
        return [(k, self[k]) for k in self.keys()]
    
    def to_bytes(self) -> bytes:
        """Serialize payload to compact binary format."""
        # Header: version (5 bits) + tier flags (3 bits)
        tier_flags = {
            CompressionTier.TINY: 0b001,
            CompressionTier.DEFAULT: 0b010,
            CompressionTier.LARGE: 0b100
        }.get(CompressionTier(self.tier_name), 0b010)
        
        header = (self.version << 3) | tier_flags
        
        # Pack entropy values as uint16 (quantized from float32)
        # Scale factor for quantization - adjust based on typical entropy ranges
        entropy_data = struct.pack('<' + 'H' * 16, *self.entropy)
        
        # Total format: header (1 byte) + symbolic (32 bytes) + entropy (32 bytes)
        return bytes([header]) + self.symbolic + entropy_data
    
    @classmethod
    def from_bytes(cls, data: bytes) -> 'FrackturePayload':
        """Deserialize payload from compact binary format."""
        if len(data) < 65:  # 1 + 32 + 32
            raise ValueError("Invalid compact payload: too short")
        
        # Parse header
        header = data[0]
        version = (header >> 3) & 0x1F  # 5 bits for version
        tier_flags = header & 0x07  # 3 bits for tier
        
        if version != 1:
            raise ValueError(f"Unsupported payload version: {version}")
        
        tier_map = {
            0b001: CompressionTier.TINY.value,
            0b010: CompressionTier.DEFAULT.value,
            0b100: CompressionTier.LARGE.value
        }
        tier_name = tier_map.get(tier_flags, CompressionTier.DEFAULT.value)
        
        # Extract symbolic (32 bytes) and entropy (32 bytes = 16 × uint16)
        symbolic = data[1:33]
        entropy_bytes = data[33:65]
        entropy = list(struct.unpack('<' + 'H' * 16, entropy_bytes))
        
        return cls(symbolic=symbolic, entropy=entropy, tier_name=tier_name, version=version)
    
    def to_legacy_dict(self) -> Dict[str, Any]:
        """Convert to legacy dict format for compatibility."""
        return {
            "symbolic": self.symbolic.hex(),
            "entropy": [float(x) / 1000.0 for x in self.entropy],  # Dequantize
            "tier_name": self.tier_name,
        }
    
    @classmethod
    def from_legacy_dict(cls, payload_dict: Dict[str, Any]) -> 'FrackturePayload':
        """Create payload from legacy dict format."""
        validate_frackture_payload(payload_dict)
        
        symbolic = bytes.fromhex(payload_dict["symbolic"])
        # Quantize float32 values to uint16
        quantized_entropy = [int(max(0, min(65535, x * 1000.0))) for x in payload_dict["entropy"]]
        
        return cls(
            symbolic=symbolic,
            entropy=quantized_entropy,
            tier_name=payload_dict.get("tier_name", CompressionTier.DEFAULT.value),
            version=1
        )


def serialize_frackture_payload(payload: Union[Dict[str, Any], FrackturePayload]) -> bytes:
    """
    Serialize Frackture payload to compact binary format.
    
    Args:
        payload: Either legacy dict or FrackturePayload instance
        
    Returns:
        bytes: Compact binary serialization
    """
    if isinstance(payload, FrackturePayload):
        return payload.to_bytes()
    elif isinstance(payload, dict):
        return FrackturePayload.from_legacy_dict(payload).to_bytes()
    else:
        raise ValueError("Payload must be dict or FrackturePayload")


def deserialize_frackture_payload(data: bytes) -> FrackturePayload:
    """
    Deserialize Frackture payload from compact binary format.
    
    Args:
        data: Compact binary payload
        
    Returns:
        FrackturePayload: Deserialized payload
    """
    return FrackturePayload.from_bytes(data)


def select_tier(data: Union[str, bytes, dict, list, np.ndarray, Any]) -> CompressionTier:
    """
    Classify input data into a compression tier based on size.
    
    Args:
        data: Input data of any type
        
    Returns:
        CompressionTier: The appropriate tier for the input
    """
    try:
        if isinstance(data, bytes):
            size = len(data)
        elif isinstance(data, str):
            size = len(data.encode("utf-8"))
        elif isinstance(data, dict):
            size = len(str(sorted(data.items())).encode("utf-8"))
        elif isinstance(data, (list, tuple)):
            size = len(str(data).encode("utf-8"))
        elif isinstance(data, np.ndarray):
            size = data.nbytes
        else:
            size = len(str(data).encode("utf-8"))
    except Exception:
        return CompressionTier.DEFAULT
    
    if size < 100:
        return CompressionTier.TINY
    elif size >= 10 * 1024 * 1024:  # 10 MB
        return CompressionTier.LARGE
    else:
        return CompressionTier.DEFAULT


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
        # Support both dict and FrackturePayload formats
        if isinstance(payload, FrackturePayload):
            # Validate FrackturePayload directly
            if not isinstance(payload.symbolic, bytes) or len(payload.symbolic) != 32:
                raise ValueError("Invalid symbolic fingerprint")
            if not isinstance(payload.entropy, list) or len(payload.entropy) != 16:
                raise ValueError("Invalid entropy channel")
            if not isinstance(payload.tier_name, str):
                raise ValueError("Invalid tier_name")
        elif isinstance(payload, dict):
            # For dict validation, only validate if it has content (for backward compatibility)
            if payload:  # Only validate non-empty dicts
                if "symbolic" not in payload or "entropy" not in payload:
                    raise ValueError("Frackture payload missing required keys")
                
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
        else:
            raise ValueError("Frackture payload must be a dict or FrackturePayload")

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
def frackture_preprocess_universal_v2_6(data, tier: Optional[CompressionTier] = None):
    """
    Preprocess input data into a normalized 768-length vector.
    
    For tiny tier (<100 bytes), uses deterministic hash-based padding with
    variance guards and lighter processing.
    
    Args:
        data: Input data of any type (str, bytes, dict, list, np.ndarray, etc.)
        tier: Optional CompressionTier. If None, will auto-detect.
        
    Returns:
        np.ndarray: Normalized 768-length float32 vector
    """
    # Auto-detect tier if not provided
    if tier is None:
        tier = select_tier(data)
    
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
        
        # For tiny tier, use hash-based deterministic padding
        if tier == CompressionTier.TINY:
            min_val = np.min(normed) if len(normed) > 0 else 0
            max_val = np.max(normed) if len(normed) > 0 else 1
            ptp = max_val - min_val
            
            # Variance guard: if range is too small, use normalized values
            if ptp < 1e-8:
                normed = np.ones_like(normed) * 0.5
            else:
                normed = (normed - min_val) / (ptp + 1e-8)
            
            # Hash-based deterministic padding for tiny inputs
            data_hash = hashlib.sha256(str(normed.tolist()).encode()).digest()
            hash_vec = np.frombuffer(data_hash, dtype=np.uint8).astype(np.float32) / 255.0
            
            # Tile hash values to reach 768 samples
            num_repeats = (768 // len(hash_vec)) + 1
            padded = np.tile(hash_vec, num_repeats)[:768]
            
            # Blend original data with hash-based padding
            blend_ratio = min(len(normed) / 768.0, 1.0)
            padded_normed = np.pad(normed, (0, 768 - len(normed)), mode="wrap")
            final = blend_ratio * padded_normed + (1 - blend_ratio) * padded
            return final.astype(np.float32)
        else:
            # Standard preprocessing for other tiers
            normed = (normed - np.min(normed)) / (np.ptp(normed) + 1e-8)
            padded = np.pad(normed, (0, 768 - len(normed) % 768), mode="wrap")
            return padded[:768].astype(np.float32)
            
    except Exception as e:
        print(f"DEBUG: frackture_preprocess_universal_v2_6 failed for input {type(data)}: {e}")
        return np.zeros(768, dtype=np.float32)


### === Symbolic Fingerprinting System === ###
def frackture_symbolic_fingerprint_f_infinity(input_vector, passes=4, tier: Optional[CompressionTier] = None):
    """
    Generate symbolic fingerprint via recursive XOR and masking.
    
    For tiny tier, uses lighter pass counts (2 instead of 4) for efficiency.
    
    Args:
        input_vector: Input vector to fingerprint
        passes: Number of XOR passes (default 4, reduced to 2 for tiny tier)
        tier: Optional CompressionTier. If tiny, overrides passes to 2.
        
    Returns:
        str: 64-character hex fingerprint
    """
    # Use lighter passes for tiny tier
    if tier == CompressionTier.TINY:
        passes = 2
    
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


def symbolic_channel_encode(input_vector, tier: Optional[CompressionTier] = None):
    return frackture_symbolic_fingerprint_f_infinity(input_vector, tier=tier)


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
def frackture_v3_3_safe(input_vector, tier: Optional[CompressionTier] = None):
    """
    Safe Frackture encoding with dual-channel compression.
    
    Returns a lightweight FrackturePayload dataclass that exposes .to_bytes() / .from_bytes().
    
    Args:
        input_vector: Preprocessed 768-length vector
        tier: Optional CompressionTier. If None, defaults to DEFAULT.
        
    Returns:
        FrackturePayload: Compact payload with .to_bytes() / .from_bytes() methods
    """
    if tier is None:
        tier = CompressionTier.DEFAULT
    
    symbolic_hex = symbolic_channel_encode(input_vector, tier=tier)
    entropy_values = entropy_channel_encode(input_vector)
    
    return FrackturePayload(
        symbolic=bytes.fromhex(symbolic_hex),
        entropy=[int(max(0, min(65535, x * 1000.0))) for x in entropy_values],
        tier_name=tier.value,
        version=1
    )


def frackture_v3_3_reconstruct(payload):
    """
    Reconstruct approximate representation from Frackture payload.
    
    Accepts legacy dict, FrackturePayload dataclass, or raw bytes.
    Honors tier metadata for specialized reconstruction:
    - Tiny tier: Heavier weighting on symbolic fingerprint (70/30 split)
    - Other tiers: Balanced 50/50 merge
    
    Args:
        payload: Frackture payload (dict, FrackturePayload, or bytes)
        
    Returns:
        np.ndarray: Reconstructed 768-length vector
    """
    # Handle different payload types for backward compatibility
    if isinstance(payload, bytes):
        payload_obj = deserialize_frackture_payload(payload)
        tier_name = payload_obj.tier_name
        symbolic_hex = payload_obj.symbolic.hex()
        entropy_data = [float(x) / 1000.0 for x in payload_obj.entropy]  # Dequantize
    elif isinstance(payload, FrackturePayload):
        tier_name = payload.tier_name
        symbolic_hex = payload.symbolic.hex()
        entropy_data = [float(x) / 1000.0 for x in payload.entropy]  # Dequantize
    elif isinstance(payload, dict):
        # For empty dicts, raise KeyError to maintain test compatibility
        if not payload:
            raise KeyError("Empty payload")
        validate_frackture_payload(payload)
        tier_name = payload.get("tier_name")
        symbolic_hex = payload["symbolic"]
        entropy_data = payload["entropy"]
    else:
        raise ValueError("Payload must be dict, FrackturePayload, or bytes")

    entropy_part = entropy_channel_decode(entropy_data)
    symbolic_part = symbolic_channel_decode(symbolic_hex)
    
    if tier_name == CompressionTier.TINY.value:
        # For tiny tier, weight symbolic more heavily (better identity preservation)
        # Symbolic: 70%, Entropy: 30%
        return (0.7 * np.array(symbolic_part) + 0.3 * np.array(entropy_part)).astype(np.float32)
    else:
        # Default balanced merge
        return merge_reconstruction(entropy_part, symbolic_part)


### === Self-Optimization (Decoder Loss Feedback Loop) === ###
def optimize_frackture(input_vector, num_trials=5, tier: Optional[CompressionTier] = None):
    """
    Self-optimizing encoder that minimizes reconstruction MSE.
    
    For tiny tier, uses reduced trial count (2 instead of 5) for efficiency.
    
    Args:
        input_vector: Preprocessed 768-length vector
        num_trials: Number of optimization trials (reduced to 2 for tiny tier)
        tier: Optional CompressionTier. If tiny, reduces trials automatically.
        
    Returns:
        tuple: (best_payload, best_mse)
    """
    if tier == CompressionTier.TINY:
        num_trials = 2
    
    best_payload = None
    best_mse = float("inf")
    for trial in range(num_trials):
        symbolic_hex = frackture_symbolic_fingerprint_f_infinity(input_vector, passes=trial + 2, tier=tier)
        entropy_values = entropy_channel_encode(input_vector)
        
        # Create FrackturePayload for consistency
        payload = FrackturePayload(
            symbolic=bytes.fromhex(symbolic_hex),
            entropy=[int(max(0, min(65535, x * 1000.0))) for x in entropy_values],
            tier_name=(tier or CompressionTier.DEFAULT).value,
            version=1
        )
        
        recon = frackture_v3_3_reconstruct(payload)
        mse = np.mean((input_vector - recon) ** 2)
        if mse < best_mse:
            best_mse = mse
            best_payload = payload
    return best_payload, best_mse


### === Simple Wrapper Functions === ###
def compress_simple(data, tier=None, optimize=False, return_format="compact"):
    """
    Simplified compression wrapper that performs preprocess → encode → optimization → compact serialization.
    
    Args:
        data: Input data to compress (str, bytes, dict, list, np.ndarray, etc.)
        tier: Optional CompressionTier. If None, will auto-detect.
        optimize: If True, run optimization to minimize MSE.
        return_format: "compact" (bytes) or "json" (dict) for legacy compatibility.
        
    Returns:
        bytes or dict: Compressed payload in requested format
    """
    # Auto-detect tier if not provided
    if tier is None:
        tier = select_tier(data)
    
    # Preprocess input
    input_vector = frackture_preprocess_universal_v2_6(data, tier)
    
    # Encode with optional optimization
    if optimize:
        payload, _ = optimize_frackture(input_vector, tier=tier)
    else:
        payload = frackture_v3_3_safe(input_vector, tier=tier)
    
    # Serialize in requested format
    if return_format == "compact":
        return payload.to_bytes()
    elif return_format == "json":
        return payload.to_legacy_dict()
    else:
        raise ValueError("return_format must be 'compact' or 'json'")


def decompress_simple(payload, input_data=None):
    """
    Simplified decompression wrapper for any payload format.
    
    Args:
        payload: Compressed payload (bytes, FrackturePayload, or dict)
        input_data: Original input for comparison (optional)
        
    Returns:
        np.ndarray: Reconstructed 768-length vector
    """
    return frackture_v3_3_reconstruct(payload)


# Preset helpers for common use cases
def compress_preset_tiny(data, optimize=False, return_format="compact"):
    """Compress using TINY tier preset."""
    return compress_simple(data, tier=CompressionTier.TINY, optimize=optimize, return_format=return_format)


def compress_preset_default(data, optimize=False, return_format="compact"):
    """Compress using DEFAULT tier preset.""" 
    return compress_simple(data, tier=CompressionTier.DEFAULT, optimize=optimize, return_format=return_format)


def compress_preset_large(data, optimize=False, return_format="compact"):
    """Compress using LARGE tier preset."""
    return compress_simple(data, tier=CompressionTier.LARGE, optimize=optimize, return_format=return_format)


### === Hashing Functions === ###

_HASH_CHUNK_SIZE = 1024 * 1024  # 1MiB


try:
    # usedforsecurity available in Python 3.9+
    _HASHER_TEMPLATE = hashlib.sha256(usedforsecurity=False)
except TypeError:
    _HASHER_TEMPLATE = hashlib.sha256()


def _dump_component(data: Any, is_key: bool = False) -> bytes:
    """Helper to dump a single component for streaming hash."""
    try:
        # keys in json must be strings
        if is_key and not isinstance(data, str):
            data = str(data)
        
        return json.dumps(
            data,
            ensure_ascii=False,
            separators=(",", ":"),
            default=str,
        ).encode("utf-8")
    except (TypeError, ValueError):
        return str(data).encode("utf-8")


def _stream_json_like(data: Any) -> Iterator[bytes]:
    """Stream JSON-like representation of data."""
    if isinstance(data, dict):
        yield b"{"
        items = sorted(data.items())
        for i, (k, v) in enumerate(items):
            if i > 0:
                yield b","
            yield _dump_component(k, is_key=True)
            yield b":"
            yield from _stream_json_like(v)
        yield b"}"
    elif isinstance(data, (list, tuple)):
        yield b"["
        for i, v in enumerate(data):
            if i > 0:
                yield b","
            yield from _stream_json_like(v)
        yield b"]"
    else:
        yield _dump_component(data)


def normalize_to_bytes(data: Any) -> Iterator[Union[bytes, memoryview]]:
    """Normalize arbitrary data into bytes for hashing.

    Fast-paths bytes-like objects and uses deterministic JSON for dict/list.
    Returns an iterator of bytes/memoryview chunks to avoid large copies.
    """

    if isinstance(data, FrackturePayload):
        yield data.to_bytes()
        return

    if isinstance(data, memoryview):
        yield data
        return

    if isinstance(data, (bytes, bytearray)):
        yield memoryview(data)
        return

    if isinstance(data, str):
        yield data.encode("utf-8")
        return

    if isinstance(data, np.ndarray):
        try:
            yield memoryview(data)
        except (ValueError, TypeError):
            # Fallback for non-contiguous arrays
            yield data.tobytes()
        return

    if isinstance(data, (dict, list, tuple)):
        yield from _stream_json_like(data)
        return

    yield str(data).encode("utf-8")


def frackture_deterministic_hash(data, salt=""):
    """Generate deterministic hash for collision testing."""

    hasher = _HASHER_TEMPLATE.copy()

    for chunk in normalize_to_bytes(data):
        mv = chunk if isinstance(chunk, memoryview) else memoryview(chunk)
        if len(mv) <= _HASH_CHUNK_SIZE:
            hasher.update(mv)
        else:
            for offset in range(0, len(mv), _HASH_CHUNK_SIZE):
                hasher.update(mv[offset : offset + _HASH_CHUNK_SIZE])

    if salt:
        hasher.update(str(salt).encode("utf-8"))

    return hasher.hexdigest()


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
