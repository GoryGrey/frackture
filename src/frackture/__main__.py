"""
CLI entry point for Frackture
"""
import sys
import json
import argparse
from pathlib import Path
from . import (
    frackture_preprocess_universal_v2_6,
    frackture_v3_3_safe,
    frackture_v3_3_reconstruct,
    frackture_deterministic_hash,
    optimize_frackture
)


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description="Frackture: Symbolic compression and fingerprinting"
    )
    parser.add_argument(
        "command",
        choices=["compress", "decompress", "hash", "optimize", "version"],
        help="Command to execute"
    )
    parser.add_argument(
        "-i", "--input",
        help="Input file path (or stdin if not provided)"
    )
    parser.add_argument(
        "-o", "--output",
        help="Output file path (or stdout if not provided)"
    )
    parser.add_argument(
        "--trials",
        type=int,
        default=5,
        help="Number of optimization trials (for optimize command)"
    )
    
    args = parser.parse_args()
    
    if args.command == "version":
        try:
            from ._version import __version__
            print(f"Frackture version {__version__}")
        except ImportError:
            print("Frackture version: development")
        return 0
    
    # Read input
    if args.input:
        with open(args.input, "rb") as f:
            data = f.read()
    else:
        data = sys.stdin.buffer.read()
    
    # Execute command
    if args.command == "compress":
        preprocessed = frackture_preprocess_universal_v2_6(data)
        payload = frackture_v3_3_safe(preprocessed)
        # Convert numpy types to JSON-serializable
        output = {
            "symbolic": payload["symbolic"],
            "entropy": [float(x) for x in payload["entropy"]]
        }
        output_data = json.dumps(output, indent=2).encode()
        
    elif args.command == "decompress":
        payload = json.loads(data.decode())
        reconstructed = frackture_v3_3_reconstruct(payload)
        output_data = reconstructed.tobytes()
        
    elif args.command == "hash":
        hash_value = frackture_deterministic_hash(data)
        output_data = hash_value.encode()
        
    elif args.command == "optimize":
        preprocessed = frackture_preprocess_universal_v2_6(data)
        payload, mse = optimize_frackture(preprocessed, num_trials=args.trials)
        output = {
            "symbolic": payload["symbolic"],
            "entropy": [float(x) for x in payload["entropy"]],
            "mse": float(mse)
        }
        output_data = json.dumps(output, indent=2).encode()
    
    # Write output
    if args.output:
        with open(args.output, "wb") as f:
            f.write(output_data)
    else:
        sys.stdout.buffer.write(output_data)
        if args.command in ["hash", "compress", "optimize"]:
            sys.stdout.write("\n")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
