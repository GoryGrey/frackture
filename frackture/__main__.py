"""
CLI entry point for Frackture package.

This module allows the frackture package to be executed as a module:
    python -m frackture compress input.txt
    python -m frackture fingerprint data.txt
"""

from .cli import main

if __name__ == "__main__":
    main()