"""Symbolic compression engine using recursive logic and entropy signatures."""

from .core import (
    compress,
    decompress,
    entropy_channel_decode,
    entropy_channel_encode,
    frackture_preprocess_universal_v2_6,
    frackture_symbolic_fingerprint_f_infinity,
    frackture_v3_3_reconstruct,
    frackture_v3_3_safe,
    merge_reconstruction,
    optimize_frackture,
    symbolic_channel_decode,
    symbolic_channel_encode,
)
from .version import __author__, __description__, __license__, __version__

__all__ = [
    "__version__",
    "__author__",
    "__license__",
    "__description__",
    "compress",
    "decompress",
    "frackture_v3_3_safe",
    "frackture_v3_3_reconstruct",
    "optimize_frackture",
    "frackture_preprocess_universal_v2_6",
    "frackture_symbolic_fingerprint_f_infinity",
    "symbolic_channel_encode",
    "symbolic_channel_decode",
    "entropy_channel_encode",
    "entropy_channel_decode",
    "merge_reconstruction",
]
