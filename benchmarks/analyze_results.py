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
    is_fixed_96b = True
    
    for dataset, methods in results_data.items():
        for m in methods:
            if m['name'] == 'Frackture':
                sizes.append(m['serialized_total_bytes'])
                if not m.get('payload_is_96b', False) and abs(m['serialized_total_bytes'] - 96) > 5:
                     # Allow some small variance, but the flag should be the source of truth
                     # If the flag is false, we check if it's strictly consistently something else or varying
                     pass

    if not sizes:
        return "No Frackture data found", 0, 0, 0

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
        # Heuristic for tier if not explicitly available, though dataset_type might help
        # For now, we trust the dataset naming or original_size if we implemented filters
        
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
    # Structure: { method: { 'ratios': [], 'speeds': [] } }
    stats = defaultdict(lambda: {'ratios': [], 'speeds': [], 'mem': []})
    
    for dataset, methods in results_data.items():
        for m in methods:
            name = m['name']
            # Normalize names
            if "Gzip" in name: norm_name = "Gzip"
            elif "Brotli" in name: norm_name = "Brotli"
            elif "AES" in name: norm_name = "AES"
            elif "SHA" in name: norm_name = "SHA"
            elif "Frackture" in name and "Encrypted" not in name: norm_name = "Frackture"
            elif "Frackture Encrypted" in name: norm_name = "Frackture Encrypted"
            else: norm_name = name
            
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

def main():
    parser = argparse.ArgumentParser(description="Analyze Frackture benchmark results")
    parser.add_argument('input_file', nargs='?', help="Path to JSON results file")
    parser.add_argument('--output-dir', default='analysis', help="Directory to save analysis reports")
    
    args = parser.parse_args()
    
    # Find latest result if not specified
    if not args.input_file:
        results_dir = os.path.join(os.path.dirname(__file__), 'results')
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
        f.write("\n")
        
        # Explicit Answers
        f.write("## 2. Key Questions\n\n")
        
        f.write("### Is the payload size fixed?\n")
        if payload_stats['is_fixed']:
            f.write(f"**Yes.** The payload size remains consistent at approximately {payload_stats['avg']:.0f} bytes.\n")
        else:
            f.write(f"**No.** The payload size varies between {payload_stats['min']} and {payload_stats['max']} bytes (Avg: {payload_stats['avg']:.1f}). This may indicate fallback behavior on small datasets or variable metadata.\n")
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
        
        # Highlight Tables
        f.write("## 3. Performance Highlights\n\n")
        
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
        "comparisons": method_comparison,
        "data_types": type_stats,
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
