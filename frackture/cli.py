#!/usr/bin/env python3
"""
Command Line Interface for Frackture.

Provides simple CLI commands for compression, decompression, encryption,
decryption, and fingerprinting operations.
"""

import argparse
import json
import sys
from typing import Optional

import numpy as np

from .engine import FracktureEngine
from .models import FracktureVersion, EncryptionMode


def load_data(file_path: str) -> str:
    """Load data from file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"Error loading file {file_path}: {e}", file=sys.stderr)
        sys.exit(1)


def save_data(data: str, file_path: str) -> None:
    """Save data to file."""
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(data)
    except Exception as e:
        print(f"Error saving file {file_path}: {e}", file=sys.stderr)
        sys.exit(1)


def compress_command(args):
    """Handle compress command."""
    engine = FracktureEngine()
    
    # Load input data
    data = load_data(args.input)
    
    try:
        # Perform compression
        result = engine.compress(
            data, 
            passes=args.passes,
            optimize=args.optimize,
            num_trials=args.trials
        )
        
        # Output results
        if args.output:
            save_data(json.dumps(result.payload.to_dict(), indent=2), args.output)
            print(f"Compression successful. Output saved to {args.output}")
            print(f"Original size: {result.original_size} bytes")
            print(f"Compressed size: {result.compressed_size} bytes")
            print(f"Compression ratio: {result.compression_ratio:.3f}")
            print(f"Reconstruction MSE: {result.mse:.6f}")
        else:
            print(json.dumps(result.payload.to_dict(), indent=2))
            
    except Exception as e:
        print(f"Compression failed: {e}", file=sys.stderr)
        sys.exit(1)


def decompress_command(args):
    """Handle decompress command."""
    engine = FracktureEngine()
    
    # Load payload
    try:
        with open(args.input, 'r', encoding='utf-8') as f:
            payload_dict = json.load(f)
    except Exception as e:
        print(f"Error loading payload {args.input}: {e}", file=sys.stderr)
        sys.exit(1)
    
    try:
        # Perform decompression
        vector = engine.decompress(payload_dict)
        
        # Output results
        if args.output:
            save_data(str(vector.tolist()), args.output)
            print(f"Decompression successful. Vector saved to {args.output}")
        else:
            print("Decompressed vector (first 10 elements):")
            print(vector[:10].tolist())
            print(f"... ({len(vector)} total elements)")
            
    except Exception as e:
        print(f"Decompression failed: {e}", file=sys.stderr)
        sys.exit(1)


def encrypt_command(args):
    """Handle encrypt command."""
    engine = FracktureEngine()
    
    # Load input data
    data = load_data(args.input)
    
    # Load key material
    try:
        with open(args.key, 'rb') as f:
            key_material = f.read()
    except Exception as e:
        print(f"Error loading key file {args.key}: {e}", file=sys.stderr)
        sys.exit(1)
    
    try:
        # Perform encryption
        result = engine.encrypt(data, key_material, passes=args.passes)
        
        # Output results
        if args.output:
            save_data(json.dumps(result.payload.to_dict(), indent=2), args.output)
            print(f"Encryption successful. Output saved to {args.output}")
            print(f"Original size: {result.original_size} bytes")
            print(f"Encrypted size: {result.compressed_size} bytes")
            print(f"Compression ratio: {result.compression_ratio:.3f}")
        else:
            print(json.dumps(result.payload.to_dict(), indent=2))
            
    except Exception as e:
        print(f"Encryption failed: {e}", file=sys.stderr)
        sys.exit(1)


def decrypt_command(args):
    """Handle decrypt command."""
    engine = FracktureEngine()
    
    # Load payload
    try:
        with open(args.input, 'r', encoding='utf-8') as f:
            payload_dict = json.load(f)
    except Exception as e:
        print(f"Error loading payload {args.input}: {e}", file=sys.stderr)
        sys.exit(1)
    
    # Load key material
    try:
        with open(args.key, 'rb') as f:
            key_material = f.read()
    except Exception as e:
        print(f"Error loading key file {args.key}: {e}", file=sys.stderr)
        sys.exit(1)
    
    try:
        # Perform decryption
        vector = engine.decrypt(payload_dict, key_material)
        
        # Output results
        if args.output:
            save_data(str(vector.tolist()), args.output)
            print(f"Decryption successful. Vector saved to {args.output}")
        else:
            print("Decrypted vector (first 10 elements):")
            print(vector[:10].tolist())
            print(f"... ({len(vector)} total elements)")
            
    except Exception as e:
        print(f"Decryption failed: {e}", file=sys.stderr)
        sys.exit(1)


def fingerprint_command(args):
    """Handle fingerprint command."""
    engine = FracktureEngine()
    
    # Load input data
    data = load_data(args.input)
    
    try:
        # Generate fingerprint
        fingerprint = engine.fingerprint(data, passes=args.passes)
        
        # Output results
        if args.output:
            save_data(fingerprint, args.output)
            print(f"Fingerprint generated successfully. Output saved to {args.output}")
        else:
            print(fingerprint)
            
    except Exception as e:
        print(f"Fingerprint generation failed: {e}", file=sys.stderr)
        sys.exit(1)


def verify_command(args):
    """Handle verify command."""
    engine = FracktureEngine()
    
    # Load payload
    try:
        with open(args.input, 'r', encoding='utf-8') as f:
            payload_dict = json.load(f)
    except Exception as e:
        print(f"Error loading payload {args.input}: {e}", file=sys.stderr)
        sys.exit(1)
    
    try:
        # Verify payload
        is_valid = engine.verify_payload(payload_dict)
        
        if is_valid:
            print("✓ Payload verification successful - payload is valid")
        else:
            print("✗ Payload verification failed - payload is invalid or corrupted")
            sys.exit(1)
            
    except Exception as e:
        print(f"Verification failed: {e}", file=sys.stderr)
        sys.exit(1)


def create_parser() -> argparse.ArgumentParser:
    """Create and configure the argument parser."""
    parser = argparse.ArgumentParser(
        description="Frackture - Symbolic compression and fingerprinting engine",
        prog="frackture"
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Compress command
    compress_parser = subparsers.add_parser("compress", help="Compress data")
    compress_parser.add_argument("input", help="Input file path")
    compress_parser.add_argument("-o", "--output", help="Output file path")
    compress_parser.add_argument("-p", "--passes", type=int, help="Number of symbolic passes")
    compress_parser.add_argument("--optimize", action="store_true", help="Use optimization")
    compress_parser.add_argument("--trials", type=int, default=5, help="Number of optimization trials")
    compress_parser.set_defaults(func=compress_command)
    
    # Decompress command
    decompress_parser = subparsers.add_parser("decompress", help="Decompress data")
    decompress_parser.add_argument("input", help="Input payload file path")
    decompress_parser.add_argument("-o", "--output", help="Output file path")
    decompress_parser.set_defaults(func=decompress_command)
    
    # Encrypt command
    encrypt_parser = subparsers.add_parser("encrypt", help="Encrypt data with key")
    encrypt_parser.add_argument("input", help="Input file path")
    encrypt_parser.add_argument("key", help="Key file path")
    encrypt_parser.add_argument("-o", "--output", help="Output file path")
    encrypt_parser.add_argument("-p", "--passes", type=int, help="Number of symbolic passes")
    encrypt_parser.set_defaults(func=encrypt_command)
    
    # Decrypt command
    decrypt_parser = subparsers.add_parser("decrypt", help="Decrypt data with key")
    decrypt_parser.add_argument("input", help="Input payload file path")
    decrypt_parser.add_argument("key", help="Key file path")
    decrypt_parser.add_argument("-o", "--output", help="Output file path")
    decrypt_parser.set_defaults(func=decrypt_command)
    
    # Fingerprint command
    fingerprint_parser = subparsers.add_parser("fingerprint", help="Generate fingerprint")
    fingerprint_parser.add_argument("input", help="Input file path")
    fingerprint_parser.add_argument("-o", "--output", help="Output file path")
    fingerprint_parser.add_argument("-p", "--passes", type=int, help="Number of symbolic passes")
    fingerprint_parser.set_defaults(func=fingerprint_command)
    
    # Verify command
    verify_parser = subparsers.add_parser("verify", help="Verify payload integrity")
    verify_parser.add_argument("input", help="Input payload file path")
    verify_parser.set_defaults(func=verify_command)
    
    return parser


def main():
    """Main CLI entry point."""
    parser = create_parser()
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    # Execute the appropriate command
    args.func(args)


if __name__ == "__main__":
    main()