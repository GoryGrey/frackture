#!/usr/bin/env python3
"""
Main test runner for Frackture verification suite
"""
import subprocess
import sys
import os

def run_tests():
    """Run the complete test suite with coverage"""
    # Change to project directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Run pytest with coverage
    cmd = [
        sys.executable, "-m", "pytest", 
        "tests/", 
        "-v",
        "--tb=short", 
        "--cov=frackture (2)",
        "--cov-report=term-missing",
        "--cov-report=html:htmlcov",
        "--hypothesis-show-statistics"
    ]
    
    print("Running Frackture verification tests...")
    print("Command:", " ".join(cmd))
    print("-" * 60)
    
    try:
        result = subprocess.run(cmd, check=False)
        return result.returncode
    except Exception as e:
        print(f"Error running tests: {e}")
        return 1

if __name__ == "__main__":
    exit_code = run_tests()
    sys.exit(exit_code)