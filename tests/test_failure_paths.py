"""
Tests for failure paths and error handling in Frackture
"""
import pytest
import numpy as np
import json
from hypothesis import given, settings
from hypothesis.strategies import text, binary, integers, floats
import sys
import os


# Add parent directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

# Import frackture module
try:
    from frackture import (
        frackture_preprocess_universal_v2_6,
        frackture_v3_3_safe,
        frackture_v3_3_reconstruct,
        frackture_encrypt_payload,
        frackture_decrypt_payload,
        frackture_deterministic_hash,
        optimize_frackture,
        frackture_symbolic_fingerprint_f_infinity,
        symbolic_channel_encode,
        symbolic_channel_decode,
        entropy_channel_encode,
        entropy_channel_decode,
        merge_reconstruction
    )
except ImportError:
    import importlib.util
    module_path = os.path.join(os.path.dirname(__file__), '..', 'frackture (2).py')
    spec = importlib.util.spec_from_file_location("frackture_2", module_path)
    frackture_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(frackture_module)
    
    frackture_preprocess_universal_v2_6 = frackture_module.frackture_preprocess_universal_v2_6
    frackture_v3_3_safe = frackture_module.frackture_v3_3_safe
    frackture_v3_3_reconstruct = frackture_module.frackture_v3_3_reconstruct
    frackture_encrypt_payload = frackture_module.frackture_encrypt_payload
    frackture_decrypt_payload = frackture_module.frackture_decrypt_payload
    frackture_deterministic_hash = frackture_module.frackture_deterministic_hash
    optimize_frackture = frackture_module.optimize_frackture
    frackture_symbolic_fingerprint_f_infinity = frackture_module.frackture_symbolic_fingerprint_f_infinity
    symbolic_channel_encode = frackture_module.symbolic_channel_encode
    symbolic_channel_decode = frackture_module.symbolic_channel_decode
    entropy_channel_encode = frackture_module.entropy_channel_encode
    entropy_channel_decode = frackture_module.entropy_channel_decode
    merge_reconstruction = frackture_module.merge_reconstruction

class TestFailurePaths:
    """Test failure paths and error handling"""
    
    def test_malformed_payload_reconstruction(self, malformed_payloads):
        """Test reconstruction with malformed payloads"""
        for payload in malformed_payloads:
            try:
                reconstructed = frackture_v3_3_reconstruct(payload)
                # If it doesn't raise an exception, it should return something reasonable
                assert isinstance(reconstructed, np.ndarray)
                assert len(reconstructed) == 768
                assert not np.any(np.isnan(reconstructed)), f"NaN in reconstruction for payload: {payload}"
                assert not np.any(np.isinf(reconstructed)), f"Infinity in reconstruction for payload: {payload}"
            except (ValueError, TypeError, KeyError) as e:
                # These are expected for some malformed payloads
                print(f"Expected error for malformed payload: {e}")
            except Exception as e:
                pytefail(f"Unexpected error for payload {payload}: {e}")
    
    def test_empty_payload_reconstruction(self):
        """Test reconstruction with empty payload"""
        empty_payload = {}
        
        with pyteraises(KeyError):
            frackture_v3_3_reconstruct(empty_payload)
    
    def test_none_payload_reconstruction(self):
        """Test reconstruction with None payload"""
        with pyteraises(TypeError):
            frackture_v3_3_reconstruct(None)
    
    def test_invalid_symbolic_fingerprint(self):
        """Test reconstruction with invalid symbolic fingerprint"""
        invalid_payloads = [
            {"symbolic": None, "entropy": [1.0] * 16},
            {"symbolic": "not_hex_string", "entropy": [1.0] * 16},
            {"symbolic": "", "entropy": [1.0] * 16},
            {"symbolic": "xyz", "entropy": [1.0] * 16},  # Odd length hex
            {"symbolic": "12", "entropy": [1.0] * 16},    # Too short
            {"symbolic": "12" * 50, "entropy": [1.0] * 16},  # Too long
        ]
        
        for payload in invalid_payloads:
            try:
                reconstructed = frackture_v3_3_reconstruct(payload)
                # Should handle gracefully or raise appropriate error
                assert isinstance(reconstructed, np.ndarray)
            except (ValueError, TypeError) as e:
                # Expected for truly invalid input
                pass
    
    def test_invalid_entropy_data(self):
        """Test reconstruction with invalid entropy data"""
        invalid_payloads = [
            {"symbolic": "a" * 64, "entropy": None},
            {"symbolic": "a" * 64, "entropy": "not_a_list"},
            {"symbolic": "a" * 64, "entropy": []},  # Empty
            {"symbolic": "a" * 64, "entropy": [float('nan')] * 16},
            {"symbolic": "a" * 64, "entropy": [float('inf')] * 16},
            {"symbolic": "a" * 64, "entropy": ["not_numbers"] * 16},
            {"symbolic": "a" * 64, "entropy": [1, 2, 3] + [4] * 13},  # Wrong length
        ]
        
        for payload in invalid_payloads:
            try:
                reconstructed = frackture_v3_3_reconstruct(payload)
                # Should handle gracefully or raise appropriate error
                assert isinstance(reconstructed, np.ndarray)
            except (ValueError, TypeError, IndexError) as e:
                # Expected for truly invalid input
                pass
    
    def test_preprocessing_extreme_values(self):
        """Test preprocessing with extreme values"""
        extreme_inputs = [
            np.array([float('inf')]),  # Infinity
            np.array([float('-inf')]), # Negative infinity
            np.array([float('nan')]),  # NaN
            np.array([1e308, 1e308]),  # Very large numbers
            np.array([1e-308, 1e-308]), # Very small numbers
        ]
        
        for test_input in extreme_inputs:
            try:
                result = frackture_preprocess_universal_v2_6(test_input)
                # Should handle extreme values gracefully
                assert isinstance(result, np.ndarray)
                assert len(result) == 768
            except Exception as e:
                # Should handle gracefully without crashing
                pytefail(f"Failed to handle extreme value: {e}")
    
    def test_preprocessing_invalid_types(self):
        """Test preprocessing with invalid input types"""
        invalid_inputs = [
            lambda x: x,  # Function
            Exception(),  # Exception object
            object(),      # Generic object
        ]
        
        for test_input in invalid_inputs:
            try:
                result = frackture_preprocess_universal_v2_6(test_input)
                # Should handle gracefully
                assert isinstance(result, np.ndarray)
                assert len(result) == 768
            except Exception as e:
                # May raise exception, but should be handled gracefully
                pytefail(f"Failed to handle invalid type: {e}")
    
    def test_optimization_with_bad_input(self):
        """Test optimization with problematic inputs"""
        bad_inputs = [
            np.array([]),  # Empty array
            np.array([float('inf')]),  # Infinity
            np.array([float('nan')]),  # NaN
            None,  # None input
            "invalid",  # String that can't be processed
        ]
        
        for bad_input in bad_inputs:
            try:
                if bad_input is not None:
                    # Try to preprocess first
                    processed = frackture_preprocess_universal_v2_6(bad_input)
                    # Then optimize
                    best_payload, best_mse = optimize_frackture(processed)
                    assert best_payload is not None
                    assert best_mse is not None
                    assert best_mse >= 0
            except Exception as e:
                # Optimization should handle bad input gracefully
                print(f"Optimization handled bad input {repr(bad_input)}: {e}")
    
    def test_optimization_edge_cases(self):
        """Test optimization with edge cases"""
        # Very small input
        small_input = np.array([0.1])
        best_payload, best_mse = optimize_frackture(small_input)
        assert best_payload is not None
        assert best_mse >= 0
        
        # Very large input
        large_input = np.random.rand(10000)
        best_payload, best_mse = optimize_frackture(large_input)
        assert best_payload is not None
        assert best_mse >= 0
        
        # Constant input
        constant_input = np.ones(100) * 0.5
        best_payload, best_mse = optimize_frackture(constant_input)
        assert best_payload is not None
        assert best_mse >= 0
    
    def test_symbolic_fingerprint_with_extreme_passes(self):
        """Test symbolic fingerprinting with extreme pass counts"""
        test_input = frackture_preprocess_universal_v2_6("extreme passes test")
        
        # Test with very few passes
        try:
            fp1 = frackture_symbolic_fingerprint_f_infinity(test_input, passes=0)
            assert isinstance(fp1, str)
        except Exception as e:
            pytefail(f"Failed with 0 passes: {e}")
        
        # Test with many passes
        try:
            fp2 = frackture_symbolic_fingerprint_f_infinity(test_input, passes=100)
            assert isinstance(fp2, str)
        except Exception as e:
            pytefail(f"Failed with 100 passes: {e}")
        
        # All should be valid hex strings
        for passes in [0, 1, 2, 5, 10, 100]:
            fp = frackture_symbolic_fingerprint_f_infinity(test_input, passes=passes)
            try:
                bytes.fromhex(fp)
                assert len(fp) == 64  # Should maintain length
            except ValueError:
                pytefail(f"Invalid hex for {passes} passes: {fp}")
    
    def test_entropy_channel_with_malformed_input(self):
        """Test entropy channel with malformed input"""
        malformed_inputs = [
            None,
            "not an array",
            np.array([]),  # Empty
            np.array([float('nan')]),  # NaN
            np.array([float('inf')]),  # Infinity
        ]
        
        for malformed in malformed_inputs:
            try:
                if malformed is not None:
                    result = entropy_channel_encode(malformed)
                    assert isinstance(result, list)
                    assert len(result) == 16  # PCA components
            except Exception as e:
                # Should handle gracefully
                print(f"Entropy channel handled malformed input {repr(malformed)}: {e}")
    
    def test_merge_reconstruction_edge_cases(self):
        """Test merge reconstruction with edge cases"""
        # Test with different sized arrays
        small_entropy = np.array([0.1] * 50)
        small_symbolic = np.array([0.2] * 50)
        
        try:
            merged = merge_reconstruction(small_entropy, small_symbolic)
            assert len(merged) == 50  # Should use smaller size
        except Exception as e:
            pytefail(f"Failed to merge small arrays: {e}")
        
        # Test with arrays containing extreme values
        extreme_entropy = np.array([0.0, 1.0, float('inf'), float('-inf'), float('nan')])
        normal_symbolic = np.array([0.5] * 5)
        
        try:
            merged = merge_reconstruction(extreme_entropy, normal_symbolic)
            # Should handle extreme values
            assert isinstance(merged, np.ndarray)
        except Exception as e:
            pytefail(f"Failed to merge extreme values: {e}")
    
    def test_encryption_with_corrupted_data(self):
        """Test encryption with various forms of data corruption"""
        key = "corruption_test_key"
        test_data = "corruption test"
        
        # Create valid encrypted payload
        preprocessed = frackture_preprocess_universal_v2_6(test_data)
        payload = frackture_v3_3_safe(preprocessed)
        encrypted = frackture_encrypt_payload(payload, key)
        
        # Test various corruption scenarios
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
            with pyteraises(ValueError):
                frackture_decrypt_payload(corrupted, key)
    
    def test_memory_error_recovery(self):
        """Test recovery from memory-related errors"""
        # Test with very large input that might cause memory issues
        try:
            large_data = np.random.rand(100000)  # Large but manageable
            preprocessed = frackture_preprocess_universal_v2_6(large_data)
            
            payload = frackture_v3_3_safe(preprocessed)
            reconstructed = frackture_v3_3_reconstruct(payload)
            
            assert isinstance(reconstructed, np.ndarray)
            assert len(reconstructed) == 768
        except MemoryError:
            # This is acceptable for very large inputs
            pass
        except Exception as e:
            pytefail(f"Unexpected error with large input: {e}")
    
    def test_concurrent_access_simulation(self):
        """Simulate concurrent access patterns"""
        import threading
        import time
        
        results = []
        errors = []
        
        def process_data(data_id):
            try:
                test_data = f"concurrent_test_{data_id}"
                preprocessed = frackture_preprocess_universal_v2_6(test_data)
                payload = frackture_v3_3_safe(preprocessed)
                reconstructed = frackture_v3_3_reconstruct(payload)
                results.append((data_id, len(reconstructed)))
            except Exception as e:
                errors.append((data_id, e))
        
        # Create multiple threads
        threads = []
        for i in range(10):
            thread = threading.Thread(target=process_data, args=(i,))
            threads.append(thread)
        
        # Start all threads
        for thread in threads:
            thread.start()
        
        # Wait for all to complete
        for thread in threads:
            thread.join()
        
        # Should have no errors and all results
        assert len(errors) == 0, f"Concurrent access errors: {errors}"
        assert len(results) == 10, f"Expected 10 results, got {len(results)}"
        
        # All reconstructions should be valid
        for data_id, length in results:
            assert length == 768, f"Reconstruction {data_id} has wrong length: {length}"
    
    def test_division_by_zero_handling(self):
        """Test handling of division by zero scenarios"""
        # Create input that might cause division by zero
        zero_input = np.zeros(100)
        
        try:
            preprocessed = frackture_preprocess_universal_v2_6(zero_input)
            
            # Should handle division by zero gracefully
            assert isinstance(preprocessed, np.ndarray)
            assert len(preprocessed) == 768
            
            # Further processing should also work
            payload = frackture_v3_3_safe(preprocessed)
            reconstructed = frackture_v3_3_reconstruct(payload)
            
            assert isinstance(reconstructed, np.ndarray)
            assert len(reconstructed) == 768
        except ZeroDivisionError:
            pytefail("Division by zero not handled properly")
        except Exception as e:
            pytefail(f"Unexpected error with zero input: {e}")
    
    def test_array_overflow_handling(self):
        """Test handling of array overflow conditions"""
        # Test with very large values that might cause overflow
        large_values = np.array([1e10, 1e20, 1e30, 1e40])
        
        try:
            preprocessed = frackture_preprocess_universal_v2_6(large_values)
            assert isinstance(preprocessed, np.ndarray)
            
            # Should not overflow to invalid values
            assert not np.any(np.isinf(preprocessed) & (preprocessed > 0))
            assert not np.any(np.isnan(preprocessed))
        except (OverflowError, ValueError) as e:
            # May raise overflow error, but should be handled
            print(f"Overflow handled: {e}")
        except Exception as e:
            pytefail(f"Unexpected error with large values: {e}")
    
    def test_recursive_error_handling(self):
        """Test handling of deeply nested structures"""
        # Create deeply nested structure
        nested = {}
        current = nested
        for i in range(100):  # Very deep nesting
            current["level"] = {}
            current = current["level"]
        current["final"] = "deep_value"
        
        try:
            preprocessed = frackture_preprocess_universal_v2_6(nested)
            assert isinstance(preprocessed, np.ndarray)
            assert len(preprocessed) == 768
        except RecursionError:
            # May hit recursion limit, but should be handled gracefully
            pass
        except Exception as e:
            pytefail(f"Error handling deep nesting: {e}")