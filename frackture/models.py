"""
Structured data models for Frackture payloads and metadata.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional, Union
from enum import Enum


class FracktureVersion(Enum):
    """Supported Frackture versions for compatibility."""
    V3_3 = "3.3"


class EncryptionMode(Enum):
    """Supported encryption modes."""
    NONE = "none"
    XOR = "xor"


@dataclass
class CompressionMetadata:
    """Metadata about compression parameters."""
    version: FracktureVersion = FracktureVersion.V3_3
    passes: int = 4
    target_length: int = 768
    optimization_trials: int = 0
    created_at: Optional[str] = None


@dataclass
class EncryptionMetadata:
    """Metadata about encryption parameters."""
    mode: EncryptionMode = EncryptionMode.NONE
    key_material: Optional[bytes] = None
    key_id: Optional[str] = None
    salt: Optional[bytes] = None


@dataclass
class FrackturePayload:
    """
    Complete Frackture payload with all metadata.
    
    This structured format ensures determinism and compatibility across
    different versions and configurations.
    """
    # Core data
    symbolic: str
    entropy: List[float]
    
    # Metadata
    metadata: CompressionMetadata
    encryption: EncryptionMetadata
    
    # Validation
    fingerprint: Optional[str] = None
    
    def to_dict(self) -> Dict:
        """Convert payload to dictionary for serialization."""
        return {
            "symbolic": self.symbolic,
            "entropy": self.entropy,
            "metadata": {
                "version": self.metadata.version.value,
                "passes": self.metadata.passes,
                "target_length": self.metadata.target_length,
                "optimization_trials": self.metadata.optimization_trials,
                "created_at": self.metadata.created_at,
            },
            "encryption": {
                "mode": self.encryption.mode.value,
                "key_id": self.encryption.key_id,
                "salt": self.encryption.salt.hex() if self.encryption.salt else None,
            },
            "fingerprint": self.fingerprint,
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> "FrackturePayload":
        """Create payload from dictionary (deserialization)."""
        metadata = CompressionMetadata(
            version=FracktureVersion(data["metadata"]["version"]),
            passes=data["metadata"]["passes"],
            target_length=data["metadata"]["target_length"],
            optimization_trials=data["metadata"]["optimization_trials"],
            created_at=data["metadata"]["created_at"],
        )
        
        encryption = EncryptionMetadata(
            mode=EncryptionMode(data["encryption"]["mode"]),
            key_id=data["encryption"]["key_id"],
            salt=bytes.fromhex(data["encryption"]["salt"]) if data["encryption"]["salt"] else None,
        )
        
        return cls(
            symbolic=data["symbolic"],
            entropy=data["entropy"],
            metadata=metadata,
            encryption=encryption,
            fingerprint=data.get("fingerprint"),
        )


@dataclass
class CompressionResult:
    """Result of a compression operation."""
    payload: FrackturePayload
    original_size: int
    compressed_size: int
    compression_ratio: float
    mse: Optional[float] = None
    optimization_improvement: Optional[float] = None