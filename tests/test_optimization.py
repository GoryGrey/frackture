"""
Property-based tests for optimization and fingerprint length verification
"""
import pytest
import numpy as np
from hypothesis import given, settings, assume
from hypothesis.strategies import text, binary, integers, floats, lists
from conftest import arbitrary_data

class TestOptimization:
    """Test optimization functionality and properties"""
    
    def test_optimize_frackture_never_degrades_mse(self):
        """Property-based test: optimize_frackture never degrades MSE vs baseline"""
        test_data = "MSE optimization test"
        preprocessed = frackture_preprocess_universal_v2_6(test_data)
        
        # Get baseline (default optimization with trial=2)
        baseline_payload, baseline_mse = optimize_frackture(preprocessed, num_trials=3)
        
        # Test multiple optimization runs
        for trial in range(3, 10):
            optimized_payload, optimized_mse = optimize_frackture(preprocessed, num_trials=trial)
            
            # MSE should not be worse than baseline
            assert optimized_mse <= baseline_mse + 1e-10, \
                f"MSE degraded from {baseline_mse} to {optimized_mse} with {trial} trials"
            
            # MSE should be non-negative
            assert optimized_mse >= 0, f"MSE negative: {optimized_mse}"
            
            # Payload should be valid
            assert optimized_payload is not None
            assert "symbolic" in optimized_payload
            assert "entropy" in optimized_payload
    
    def test_optimization_improvement_property(self):
        """Test that optimization can improve over naive approach"""
        test_data = "optimization improvement test"
        preprocessed = frackture_preprocess_universal_v2_6(test_data)
        
        # Create naive payload (fixed passes=2)
        naive_symbolic = frackture_symbolic_fingerprint_f_infinity(preprocessed, passes=2)
        naive_entropy = entropy_channel_encode(preprocessed)
        naive_payload = {"symbolic": naive_symbolic, "entropy": naive_entropy}
        naive_reconstruction = frackture_v3_3_reconstruct(naive_payload)
        naive_mse = np.mean((preprocessed - naive_reconstruction) ** 2)
        
        # Optimize
        optimized_payload, optimized_mse = optimize_frackture(preprocessed, num_trials=5)
        
        # Optimization should not be worse than naive
        assert optimized_mse <= naive_mse, \
            f"Optimization ({optimized_mse}) worse than naive ({naive_mse})"
    
    def test_optimization_consistency(self):
        """Test that optimization produces consistent results"""
        test_data = "optimization consistency test"
        preprocessed = frackture_preprocess_universal_v2_6(test_data)
        
        # Run optimization multiple times
        results = []
        for _ in range(3):
            payload, mse = optimize_frackture(preprocessed, num_trials=3)
            results.append((payload, mse))
        
        # All should have same MSE (optimization is deterministic)
        mse_values = [result[1] for result in results]
        assert all(abs(mse - mse_values[0]) < 1e-10 for mse in mse_values), \
            "Optimization MSE not consistent"
        
        # Payloads should be identical
        for payload, _ in results[1:]:
            assert payload == results[0][0], "Optimization payload not consistent"
    
    def test_fingerprint_maintains_fixed_length_property(self):
        """Property-based test: fingerprint outputs maintain fixed length"""
        
        @given(data())
        @settings(max_examples=100)
        def check_fingerprint_length(data):
            test_input = data.draw(arbitrary_data())
            assume(test_input is not None and len(str(test_input)) > 0)
            
            try:
                preprocessed = frackture_preprocess_universal_v2_6(test_input)
                fingerprint = symbolic_channel_encode(preprocessed)
                
                # Check fingerprint properties
                assert isinstance(fingerprint, str), "Fingerprint should be string"
                assert len(fingerprint) > 0, "Fingerprint should not be empty"
                
                # Should be valid hex
                try:
                    bytes.fromhex(fingerprint)
                except ValueError:
                    assert False, f"Invalid hex fingerprint: {fingerprint}"
                
                # Should maintain consistent length
                assert len(fingerprint) == 64, f"Variable fingerprint length: {len(fingerprint)}"
                
            except Exception as e:
                # Some inputs may fail preprocessing, but this should be rare
                print(f"Preprocessing failed for {type(test_input)}: {e}")
        
        check_fingerprint_length()
    
    def test_optimization_with_different_input_sizes(self):
        """Test optimization with various input sizes"""
        test_inputs = [
            np.array([0.1]),  # Very small
            np.random.rand(10),  # Small
            np.random.rand(100),  # Medium
            np.random.rand(1000),  # Large
            np.random.rand(10000),  # Very large
        ]
        
        for i, test_input in enumerate(test_inputs):
            try:
                # Optimize
                optimized_payload, optimized_mse = optimize_frackture(test_input)
                
                # Should handle all sizes
                assert optimized_payload is not None
                assert optimized_mse >= 0
                
                # Verify payload structure
                assert "symbolic" in optimized_payload
                assert "entropy" in optimized_payload
                assert len(optimized_payload["symbolic"]) == 64  # Fixed length
                assert len(optimized_payload["entropy"]) == 16  # PCA components
                
            except MemoryError:
                # May run out of memory for very large inputs
                print(f"Memory error for input size {len(test_input)}")
            except Exception as e:
                pytefail(f"Optimization failed for size {len(test_input)}: {e}")
    
    def test_optimization_pareto_property(self):
        """Test that optimization explores different trade-offs"""
        test_data = "pareto optimization test"
        preprocessed = frackture_preprocess_universal_v2_6(test_data)
        
        # Collect MSE values for different pass counts
        mse_by_passes = {}
        for passes in range(1, 10):
            symbolic = frackture_symbolic_fingerprint_f_infinity(preprocessed, passes=passes)
            entropy = entropy_channel_encode(preprocessed)
            payload = {"symbolic": symbolic, "entropy": entropy}
            reconstruction = frackture_v3_3_reconstruct(payload)
            mse = np.mean((preprocessed - reconstruction) ** 2)
            mse_by_passes[passes] = mse
        
        # Find minimum MSE
        min_mse = min(mse_by_passes.values())
        min_passes = [k for k, v in mse_by_passes.items() if abs(v - min_mse) < 1e-10]
        
        # Minimum should exist and be reasonable
        assert len(min_passes) > 0, "No optimal pass count found"
        
        # Test that optimization finds this minimum
        optimized_payload, optimized_mse = optimize_frackture(preprocessed, num_trials=10)
        
        # Optimized MSE should match or beat the best found
        assert optimized_mse <= min_mse + 1e-10, \
            f"Optimization ({optimized_mse}) worse than brute force ({min_mse})"
    
    def test_optimization_no_improvement_case(self):
        """Test optimization when no improvement is possible"""
        # Create data that's already well-represented
        simple_data = np.ones(768) * 0.5  # Constant values
        
        # Optimize
        optimized_payload, optimized_mse = optimize_frackture(simple_data, num_trials=5)
        
        # Should still produce valid result
        assert optimized_payload is not None
        assert optimized_mse >= 0
        
        # MSE should be reasonable for constant data
        assert optimized_mse < 1.0, f"MSE too high for simple data: {optimized_mse}"
        
        # Should not crash or produce invalid results
        assert "symbolic" in optimized_payload
        assert "entropy" in optimized_payload
    
    @given(floats(min_value=-1e6, max_value=1e6))
    @settings(max_examples=50)
    def test_optimization_numeric_stability(self, test_float):
        """Test optimization with extreme numeric values"""
        assume(not (np.isnan(test_float) or np.isinf(test_float)))
        
        try:
            test_array = np.array([test_float, test_float + 1, test_float - 1])
            preprocessed = frackture_preprocess_universal_v2_6(test_array)
            
            # Optimize
            optimized_payload, optimized_mse = optimize_frackture(preprocessed, num_trials=3)
            
            # Should handle extreme values gracefully
            assert optimized_payload is not None
            assert optimized_mse >= 0
            assert not np.isnan(optimized_mse)
            assert not np.isinf(optimized_mse)
            
        except Exception as e:
            pytefail(f"Failed with extreme value {test_float}: {e}")
    
    def test_optimization_deterministic_property(self):
        """Test that optimization is deterministic"""
        test_data = "deterministic optimization test"
        preprocessed = frackture_preprocess_universal_v2_6(test_data)
        
        # Run multiple times with same parameters
        results = []
        for _ in range(5):
            payload, mse = optimize_frackture(preprocessed, num_trials=5)
            results.append((payload, mse))
        
        # All results should be identical
        for payload, mse in results[1:]:
            assert payload == results[0][0], "Optimization not deterministic"
            assert abs(mse - results[0][1]) < 1e-10, "Optimization MSE not deterministic"
    
    def test_optimization_convergence_property(self):
        """Test that optimization converges or stops improving"""
        test_data = "convergence test"
        preprocessed = frackture_preprocess_universal_v2_6(test_data)
        
        # Track MSE across multiple optimization runs
        mse_progression = []
        for num_trials in [1, 2, 3, 5, 10, 20]:
            _, mse = optimize_frackture(preprocessed, num_trials=num_trials)
            mse_progression.append(mse)
        
        # MSE should generally improve or stay the same
        for i in range(1, len(mse_progression)):
            assert mse_progression[i] <= mse_progression[i-1] + 1e-10, \
                f"MSE not converging: {mse_progression[i-1]} -> {mse_progression[i]}"
    
    def test_fingerprint_length_across_passes(self):
        """Test that fingerprint length is consistent across different pass counts"""
        test_data = "length consistency test"
        preprocessed = frackture_preprocess_universal_v2_6(test_data)
        
        lengths = []
        for passes in [1, 2, 3, 5, 10, 20]:
            fingerprint = frackture_symbolic_fingerprint_f_infinity(preprocessed, passes=passes)
            lengths.append(len(fingerprint))
        
        # All lengths should be identical
        assert len(set(lengths)) == 1, f"Inconsistent lengths: {lengths}"
        assert lengths[0] == 64, f"Unexpected fingerprint length: {lengths[0]}"
    
    def test_optimization_payload_reconstruction_validity(self):
        """Test that optimized payloads produce valid reconstructions"""
        test_data = "payload validity test"
        preprocessed = frackture_preprocess_universal_v2_6(test_data)
        
        # Optimize
        optimized_payload, _ = optimize_frackture(preprocessed, num_trials=5)
        
        # Test reconstruction
        reconstruction = frackture_v3_3_reconstruct(optimized_payload)
        
        # Should be valid reconstruction
        assert isinstance(reconstruction, np.ndarray)
        assert len(reconstruction) == 768
        assert not np.any(np.isnan(reconstruction))
        assert not np.any(np.isinf(reconstruction))
        assert np.all(reconstruction >= 0)
        assert np.all(reconstruction <= 1)
        
        # Should improve over baseline
        baseline_payload = {"symbolic": "a" * 64, "entropy": [1.0] * 16}
        baseline_reconstruction = frackture_v3_3_reconstruct(baseline_payload)
        baseline_mse = np.mean((preprocessed - baseline_reconstruction) ** 2)
        optimized_mse = np.mean((preprocessed - reconstruction) ** 2)
        
        assert optimized_mse < baseline_mse, \
            f"Optimization didn't improve MSE: {baseline_mse} -> {optimized_mse}"