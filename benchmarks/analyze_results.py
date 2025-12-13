#!/usr/bin/env python3
import json
import argparse
import sys
import os
from collections import defaultdict
import statistics

def load_results(filepath):
    """Load benchmark results from a JSON file."""
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading {filepath}: {e}", file=sys.stderr)
        sys.exit(1)

def generate_sparkline(data, min_val=None, max_val=None):
    """Generate a simple ASCII sparkline."""
    if not data:
        return ""
    
    # Unicode blocks:  ▂▃▄▅▆▇█
    bars = u" ▂▃▄▅▆▇█"
    
    if min_val is None:
        min_val = min(data)
    if max_val is None:
        max_val = max(data)
    
    if max_val == min_val:
        return bars[len(bars) // 2] * len(data)
    
    range_val = max_val - min_val
    
    result = ""
    for val in data:
        normalized = (val - min_val) / range_val
        index = int(normalized * (len(bars) - 1))
        result += bars[index]
    
    return result

def analyze_payload_size(results_data):
    """Analyze if payload size is fixed."""
    sizes = []
    
    for dataset, methods in results_data.items():
        for m in methods:
            if m['name'] == 'Frackture':
                sizes.append(m.get('serialized_total_bytes', 0))

    if not sizes:
        return {"is_fixed": False, "min": 0, "max": 0, "avg": 0, "variance": 0}

    min_size = min(sizes)
    max_size = max(sizes)
    avg_size = statistics.mean(sizes)
    variance = statistics.variance(sizes) if len(sizes) > 1 else 0
    
    is_fixed = (max_size - min_size) < 5 # Allow 5 bytes variance
    
    return {
        "is_fixed": is_fixed,
        "min": min_size,
        "max": max_size,
        "avg": avg_size,
        "variance": variance,
        "samples": len(sizes)
    }

def get_compression_stats(results_data, tier_filter=None):
    """Get compression stats for Frackture, optionally filtered by tier/size."""
    ratios = []
    throughputs = []
    
    for dataset, methods in results_data.items():
        for m in methods:
            if m['name'] == 'Frackture':
                # Skip if we want to filter by size and it doesn't match
                if tier_filter:
                    if tier_filter == 'small' and m['original_size'] > 102400: continue
                    if tier_filter == 'large' and m['original_size'] < 102400: continue
                
                ratios.append(m['compression_ratio'])
                throughputs.append(m['encode_throughput'])
    
    return ratios, throughputs

def compare_methods(results_data):
    """Compare Frackture against other methods."""
    stats = defaultdict(lambda: {'ratios': [], 'speeds': [], 'mem': []})
    
    for dataset, methods in results_data.items():
        for m in methods:
            name = m['name']
            # Normalize names (preserve multi-level sweeps when present)
            if m.get('gzip_level') is not None:
                norm_name = f"Gzip L{m['gzip_level']}"
            elif m.get('brotli_quality') is not None:
                norm_name = f"Brotli Q{m['brotli_quality']}"
            elif "Gzip" in name:
                norm_name = "Gzip"
            elif "Brotli" in name:
                norm_name = "Brotli"
            elif "AES" in name:
                norm_name = "AES"
            elif "SHA" in name:
                norm_name = "SHA"
            elif "Frackture" in name and "Encrypted" not in name:
                norm_name = "Frackture"
            elif "Frackture Encrypted" in name:
                norm_name = "Frackture Encrypted"
            else:
                norm_name = name
            
            stats[norm_name]['ratios'].append(m['compression_ratio'])
            stats[norm_name]['speeds'].append(m['encode_throughput'])
            stats[norm_name]['mem'].append(m.get('peak_memory_mb', 0))
            
    summary = {}
    for name, data in stats.items():
        summary[name] = {
            'avg_ratio': statistics.mean(data['ratios']) if data['ratios'] else 0,
            'avg_speed': statistics.mean(data['speeds']) if data['speeds'] else 0,
            'avg_mem': statistics.mean(data['mem']) if data['mem'] else 0,
            'count': len(data['ratios'])
        }
    return summary

def analyze_optimization(results_data):
    """Analyze optimization gains."""
    gains = []
    for dataset, methods in results_data.items():
        for m in methods:
            if m['name'] == 'Frackture':
                gains.append(m.get('optimization_improvement_pct', 0))
    
    if not gains:
        return 0, 0, []
        
    return statistics.mean(gains), max(gains), gains

def categorize_dataset(name):
    if "random" in name: return "Random"
    if "repetitive" in name: return "Repetitive"
    return "Mixed/Other"

def analyze_data_types(results_data):
    """Analyze performance by data characteristics (Random vs Repetitive)."""
    categories = defaultdict(lambda: {'ratios': [], 'mses': []})
    
    for dataset, methods in results_data.items():
        cat = categorize_dataset(dataset)
        for m in methods:
            if m['name'] == 'Frackture':
                categories[cat]['ratios'].append(m['compression_ratio'])
                categories[cat]['mses'].append(m.get('optimized_mse', 0))
    
    summary = {}
    for cat, data in categories.items():
        summary[cat] = {
            'avg_ratio': statistics.mean(data['ratios']) if data['ratios'] else 0,
            'avg_mse': statistics.mean(data['mses']) if data['mses'] else 0
        }
    return summary

def analyze_reliability(results_data):
    """Analyze reliability metrics: Lossless, Determinism, Fault Injection."""
    lossless_count = 0
    lossy_count = 0
    deterministic_count = 0
    nondeterministic_count = 0
    fault_passed_count = 0
    fault_failed_count = 0
    total_frackture_runs = 0
    
    for dataset, methods in results_data.items():
        for m in methods:
            if m['name'] == 'Frackture':
                total_frackture_runs += 1
                if m.get('is_lossless', False):
                    lossless_count += 1
                else:
                    lossy_count += 1
                
                if m.get('is_deterministic', False):
                    deterministic_count += 1
                else:
                    nondeterministic_count += 1
                
                if m.get('fault_injection_passed', False):
                    fault_passed_count += 1
                else:
                    fault_failed_count += 1

    return {
        "is_lossy": lossy_count > 0,
        "lossless_runs": lossless_count,
        "lossy_runs": lossy_count,
        "is_deterministic": nondeterministic_count == 0,
        "deterministic_runs": deterministic_count,
        "nondeterministic_runs": nondeterministic_count,
        "fault_injection_passed": fault_passed_count > 0 and fault_failed_count == 0, # Strict
        "fault_passed_runs": fault_passed_count,
        "fault_failed_runs": fault_failed_count,
        "total_runs": total_frackture_runs
    }

def analyze_by_size_tier(results_data):
    """Analyze performance by size tier."""
    tiers = defaultdict(lambda: {'ratios': [], 'speeds': []})
    
    for dataset, methods in results_data.items():
        for m in methods:
            if m['name'] == 'Frackture':
                size = m['original_size']
                if size < 100:
                    tier = "Tiny (<100B)"
                elif size < 1024 * 1024:
                    tier = "Small/Medium (100KB+)"
                elif size < 100 * 1024 * 1024:
                    tier = "Large (1MB+)"
                else:
                    tier = "Extreme (>100MB)"
                
                tiers[tier]['ratios'].append(m['compression_ratio'])
                tiers[tier]['speeds'].append(m['encode_throughput'])
    
    summary = {}
    for tier, data in tiers.items():
        summary[tier] = {
            'avg_ratio': statistics.mean(data['ratios']) if data['ratios'] else 0,
            'avg_speed': statistics.mean(data['speeds']) if data['speeds'] else 0,
            'count': len(data['ratios'])
        }
    return summary

def main():
    parser = argparse.ArgumentParser(description="Analyze Frackture benchmark results")
    parser.add_argument('input_file', nargs='?', help="Path to JSON results file")
    parser.add_argument('--output-dir', default='analysis', help="Directory to save analysis reports")
    
    args = parser.parse_args()
    
    # Find latest result if not specified
    if not args.input_file:
        results_dir = os.path.join(os.path.dirname(__file__), 'results')
        if not os.path.exists(results_dir):
            print(f"Results directory not found: {results_dir}")
            sys.exit(1)
            
        files = [os.path.join(results_dir, f) for f in os.listdir(results_dir) if f.endswith('.json')]
        if not files:
            print("No result files found in benchmarks/results/")
            sys.exit(1)
        args.input_file = max(files, key=os.path.getmtime)
        print(f"Using latest result file: {args.input_file}")

    data = load_results(args.input_file)
    results = data.get('results', {})
    
    if not results:
        print("No results found in JSON file.")
        sys.exit(1)

    # 1. Payload Size Analysis
    payload_stats = analyze_payload_size(results)
    
    # 2. Compression & Throughput Stats
    frackture_ratios, frackture_speeds = get_compression_stats(results)
    
    # 3. Method Comparison
    method_comparison = compare_methods(results)
    
    # 4. Optimization Analysis
    opt_avg, opt_max, opt_gains = analyze_optimization(results)
    
    # 5. Data Type Analysis
    type_stats = analyze_data_types(results)

    # 6. Reliability Analysis
    reliability = analyze_reliability(results)
    
    # 7. Size Tier Analysis
    tier_stats = analyze_by_size_tier(results)

    # Ensure output directory exists
    os.makedirs(args.output_dir, exist_ok=True)
    
    # --- Generate Markdown Report ---
    report_path = os.path.join(args.output_dir, 'report.md')
    
    with open(report_path, 'w') as f:
        f.write(f"# Frackture Analysis Dashboard\n\n")
        f.write(f"**Source:** `{os.path.basename(args.input_file)}`\n")
        f.write(f"**Timestamp:** {data.get('timestamp', 'N/A')}\n\n")
        
        # Summary Metrics
        f.write("## 1. Executive Summary\n\n")
        f.write("| Metric | Value |\n")
        f.write("|---|---|\n")
        f.write(f"| **Avg Compression Ratio** | {statistics.mean(frackture_ratios):.2f}x |\n")
        f.write(f"| **Avg Throughput** | {statistics.mean(frackture_speeds):.2f} MB/s |\n")
        f.write(f"| **Avg Optimization Gain** | {opt_avg:.2f}% |\n")
        f.write(f"| **Payload Fixed?** | {'Yes' if payload_stats['is_fixed'] else 'No'} (Range: {payload_stats['min']}-{payload_stats['max']} bytes) |\n")
        f.write(f"| **Lossless?** | {'Yes' if not reliability['is_lossy'] else 'No'} (Lossy runs: {reliability['lossy_runs']}/{reliability['total_runs']}) |\n")
        f.write(f"| **Deterministic?** | {'Yes' if reliability['is_deterministic'] else 'No'} |\n")
        f.write("\n")
        
        # Explicit Answers
        f.write("## 2. Key Questions\n\n")
        
        f.write("### Is the payload size fixed at 96 bytes?\n")
        if payload_stats['is_fixed']:
            f.write(f"**Yes.** The payload size remains consistent at approximately {payload_stats['avg']:.0f} bytes.\n")
        else:
            f.write(f"**No.** The payload size varies between {payload_stats['min']} and {payload_stats['max']} bytes (Avg: {payload_stats['avg']:.1f}). This contradicts the 96-byte target in some cases.\n")
        f.write("\n")

        f.write("### Is Frackture lossy or lossless?\n")
        if reliability['is_lossy']:
            f.write(f"**Lossy.** Frackture is primarily a lossy compression algorithm. {reliability['lossy_runs']} out of {reliability['total_runs']} runs were lossy. Reconstruction relies on minimizing MSE rather than exact bitwise restoration.\n")
        else:
             f.write(f"**Lossless.** All runs were verified as lossless.\n")
        f.write("\n")
        
        f.write("### What compression gains does Frackture achieve?\n")
        f.write(f"On average, Frackture achieves **{statistics.mean(frackture_ratios):.2f}x** compression.\n")
        f.write("- **Best case:** {:.2f}x\n".format(max(frackture_ratios) if frackture_ratios else 0))
        f.write("- **Worst case:** {:.2f}x\n".format(min(frackture_ratios) if frackture_ratios else 0))
        f.write("\n")
        
        f.write("### How does it compare to Gzip/Brotli/AES/SHA?\n")
        f.write("| Method | Ratio | Speed (MB/s) | Memory (MB) |\n")
        f.write("|---|---|---|---|\n")
        
        # Sort by Ratio desc
        sorted_methods = sorted(method_comparison.items(), key=lambda x: x[1]['avg_ratio'], reverse=True)
        
        for name, stats in sorted_methods:
            f.write(f"| {name} | {stats['avg_ratio']:.2f}x | {stats['avg_speed']:.2f} | {stats['avg_mem']:.1f} |\n")
        f.write("\n")

        f.write("### Is determinism validated?\n")
        if reliability['is_deterministic']:
             f.write(f"**Yes.** All {reliability['deterministic_runs']} runs produced identical outputs for identical inputs.\n")
        else:
             f.write(f"**No.** Determinism failed in {reliability['nondeterministic_runs']} cases.\n")
        f.write("\n")
        
        # Highlight Tables
        f.write("## 3. Performance Highlights\n\n")

        f.write("### Performance by Size Tier\n")
        f.write("| Tier | Avg Ratio | Avg Speed (MB/s) | Count |\n")
        f.write("|---|---|---|---|\n")
        for tier, stats in tier_stats.items():
             f.write(f"| {tier} | {stats['avg_ratio']:.2f}x | {stats['avg_speed']:.2f} | {stats['count']} |\n")
        f.write("\n")
        
        f.write("### Random vs Repetitive Data\n")
        f.write("| Data Type | Avg Ratio | Avg MSE |\n")
        f.write("|---|---|---|\n")
        for cat, stats in type_stats.items():
             f.write(f"| {cat} | {stats['avg_ratio']:.2f}x | {stats['avg_mse']:.4f} |\n")
        f.write("\n")
        
        f.write("### Optimization Gains\n")
        f.write(f"The optimization loop improved reconstruction MSE by an average of **{opt_avg:.2f}%** (Max: {opt_max:.2f}%).\n")
        f.write(f"Trend: `{generate_sparkline(opt_gains)}`\n")
        f.write("\n")

        f.write("### Reliability & Fault Injection\n")
        f.write(f"- **Fault Injection:** {'Passed' if reliability['fault_injection_passed'] else 'Failed'}\n")
        f.write(f"- **Passed Runs:** {reliability['fault_passed_runs']}\n")
        f.write(f"- **Failed Runs:** {reliability['fault_failed_runs']}\n")
        f.write("\n")

        f.write("### Throughput Distribution\n")
        f.write(f"Encoding Speed (MB/s): `{generate_sparkline(frackture_speeds)}`\n")
        f.write(f"Range: {min(frackture_speeds):.2f} - {max(frackture_speeds):.2f} MB/s\n")

    print(f"Report generated: {report_path}")

    # --- Generate Insights JSON ---
    insights = {
        "summary": {
            "avg_compression_ratio": statistics.mean(frackture_ratios) if frackture_ratios else 0,
            "avg_throughput_mbs": statistics.mean(frackture_speeds) if frackture_speeds else 0,
            "payload_variance": payload_stats['variance'],
            "is_payload_fixed": payload_stats['is_fixed']
        },
        "reliability": reliability,
        "comparisons": method_comparison,
        "data_types": type_stats,
        "size_tiers": tier_stats,
        "optimization": {
            "avg_gain_pct": opt_avg,
            "max_gain_pct": opt_max
        },
        "best_datasets": [], # To be implemented if needed
        "failed_cases": [] # To be implemented if needed
    }
    
    json_path = os.path.join(args.output_dir, 'insights.json')
    with open(json_path, 'w') as f:
        json.dump(insights, f, indent=2)
        
    print(f"Insights generated: {json_path}")

if __name__ == "__main__":
    main()
