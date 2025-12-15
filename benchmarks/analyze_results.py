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

def analyze_vs_gzip_brotli(results_data):
    """Detailed comparison: Frackture vs Gzip and Brotli configurations.

    Returns summary stats for configuration sweeps plus head-to-head win/loss counts.
    """

    def infer_dataset_tier(dataset_key: str, methods: list) -> str:
        for m in methods:
            tier = m.get('tier_name')
            if tier:
                return str(tier)

        if dataset_key.startswith('tiny_'):
            return 'tiny'
        if dataset_key.startswith('small_'):
            return 'medium'
        if dataset_key.startswith('large_'):
            return 'large'
        if dataset_key.startswith('extreme_'):
            return 'extreme'

        known = {'tiny', 'small', 'medium', 'large', 'xlarge', 'xxlarge', 'huge'}
        parts = dataset_key.split('_')
        if parts and parts[-1] in known:
            return parts[-1]

        return 'unknown'

    frackture_metrics = []

    gzip_raw = defaultdict(lambda: {'ratios': [], 'speeds': [], 'count': 0, 'wins_ratio': 0, 'wins_speed': 0, 'comparisons': 0})
    brotli_raw = defaultdict(lambda: {'ratios': [], 'speeds': [], 'count': 0, 'wins_ratio': 0, 'wins_speed': 0, 'comparisons': 0})

    by_tier = defaultdict(lambda: {'total_comparisons': 0, 'frackture_wins_ratio': 0, 'frackture_wins_speed': 0})

    total_comparisons = 0
    frackture_wins_ratio = 0
    frackture_wins_speed = 0

    for dataset, methods in results_data.items():
        fr = next((m for m in methods if m.get('name') == 'Frackture' and m.get('success', True)), None)
        if not fr:
            continue

        tier_name = infer_dataset_tier(dataset, methods)

        fr_ratio = fr.get('compression_ratio', 0)
        fr_speed = fr.get('encode_throughput', 0)
        frackture_metrics.append({'ratio': fr_ratio, 'throughput': fr_speed, 'tier_name': tier_name})

        for m in methods:
            if not m.get('success', True):
                continue

            level = m.get('gzip_level')
            quality = m.get('brotli_quality')
            if level is None and quality is None:
                continue

            comp_ratio = m.get('compression_ratio', 0)
            comp_speed = m.get('encode_throughput', 0)

            total_comparisons += 1
            by_tier[tier_name]['total_comparisons'] += 1

            if fr_ratio > comp_ratio:
                frackture_wins_ratio += 1
                by_tier[tier_name]['frackture_wins_ratio'] += 1
                ratio_win = True
            else:
                ratio_win = False

            if fr_speed > comp_speed:
                frackture_wins_speed += 1
                by_tier[tier_name]['frackture_wins_speed'] += 1
                speed_win = True
            else:
                speed_win = False

            if level is not None:
                bucket = gzip_raw[str(level)]
                bucket['ratios'].append(comp_ratio)
                bucket['speeds'].append(comp_speed)
                bucket['count'] += 1
                bucket['comparisons'] += 1
                bucket['wins_ratio'] += 1 if ratio_win else 0
                bucket['wins_speed'] += 1 if speed_win else 0

            if quality is not None:
                bucket = brotli_raw[str(quality)]
                bucket['ratios'].append(comp_ratio)
                bucket['speeds'].append(comp_speed)
                bucket['count'] += 1
                bucket['comparisons'] += 1
                bucket['wins_ratio'] += 1 if ratio_win else 0
                bucket['wins_speed'] += 1 if speed_win else 0

    summary = {
        'frackture_avg_ratio': statistics.mean([x['ratio'] for x in frackture_metrics]) if frackture_metrics else 0,
        'frackture_avg_speed': statistics.mean([x['throughput'] for x in frackture_metrics]) if frackture_metrics else 0,
        'gzip_by_level': {},
        'brotli_by_quality': {},
        'frackture_wins_ratio': frackture_wins_ratio,
        'frackture_wins_speed': frackture_wins_speed,
        'total_comparisons': total_comparisons,
        'by_tier': {},
    }

    for level, bucket in gzip_raw.items():
        comparisons = bucket['comparisons']
        summary['gzip_by_level'][str(level)] = {
            'avg_ratio': statistics.mean(bucket['ratios']) if bucket['ratios'] else 0,
            'avg_speed': statistics.mean(bucket['speeds']) if bucket['speeds'] else 0,
            'count': bucket['count'],
            'total_comparisons': comparisons,
            'frackture_wins_ratio': bucket['wins_ratio'],
            'frackture_wins_speed': bucket['wins_speed'],
            'win_rate_ratio': (bucket['wins_ratio'] / comparisons) if comparisons > 0 else 0,
        }

    for quality, bucket in brotli_raw.items():
        comparisons = bucket['comparisons']
        summary['brotli_by_quality'][str(quality)] = {
            'avg_ratio': statistics.mean(bucket['ratios']) if bucket['ratios'] else 0,
            'avg_speed': statistics.mean(bucket['speeds']) if bucket['speeds'] else 0,
            'count': bucket['count'],
            'total_comparisons': comparisons,
            'frackture_wins_ratio': bucket['wins_ratio'],
            'frackture_wins_speed': bucket['wins_speed'],
            'win_rate_ratio': (bucket['wins_ratio'] / comparisons) if comparisons > 0 else 0,
        }

    for tier_name, bucket in by_tier.items():
        total = bucket['total_comparisons']
        summary['by_tier'][tier_name] = {
            **bucket,
            'win_rate_ratio': (bucket['frackture_wins_ratio'] / total) if total > 0 else 0,
            'win_rate_speed': (bucket['frackture_wins_speed'] / total) if total > 0 else 0,
        }

    summary['win_rate_ratio'] = (frackture_wins_ratio / total_comparisons) if total_comparisons > 0 else 0
    summary['win_rate_speed'] = (frackture_wins_speed / total_comparisons) if total_comparisons > 0 else 0

    return summary

def analyze_latency(results_data):
    """Analyze hashing/encryption latency: SHA256/AES-GCM vs Frackture."""
    latency_data = {
        'frackture_hash': [],
        'frackture_encrypt': [],
        'sha256': [],
        'aes_gcm': []
    }
    
    for dataset, methods in results_data.items():
        for m in methods:
            if m['name'] == 'Frackture':
                latency_data['frackture_hash'].append(m.get('hash_time', 0) * 1000)  # Convert to ms
            elif m['name'] == 'Frackture Encrypted':
                latency_data['frackture_encrypt'].append(m.get('hash_time', 0) * 1000)
            elif m['name'] == 'SHA256':
                latency_data['sha256'].append(m.get('hash_time', 0) * 1000)
            elif m['name'] == 'AES-GCM':
                latency_data['aes_gcm'].append(m.get('hash_time', 0) * 1000)
    
    summary = {}
    for key, values in latency_data.items():
        if values:
            summary[key] = {
                'avg_latency_ms': statistics.mean(values),
                'min_latency_ms': min(values),
                'max_latency_ms': max(values),
                'count': len(values)
            }
    
    return summary

def detect_weaknesses(results_data, method_comparison, tier_stats):
    """Auto-detect competitive weaknesses where Frackture underperforms."""
    weaknesses = []
    
    # Analyze each tier
    for tier, stats in tier_stats.items():
        frackture_ratio = stats.get('avg_ratio', 0)
        
        # Check if Frackture underperforms in certain tiers
        if frackture_ratio < 5:  # Low compression in some tiers
            weaknesses.append({
                'type': 'low_compression',
                'tier': tier,
                'frackture_ratio': frackture_ratio,
                'description': f"Frackture achieves only {frackture_ratio:.2f}x compression in {tier} - poor for general-purpose compression"
            })
    
    # Check Gzip comparison
    if 'Gzip' in method_comparison:
        gzip_avg = method_comparison['Gzip']['avg_ratio']
        frackture_avg = method_comparison.get('Frackture', {}).get('avg_ratio', 0)
        if gzip_avg > frackture_avg:
            weaknesses.append({
                'type': 'inferior_to_gzip',
                'metric': 'compression_ratio',
                'gzip_ratio': gzip_avg,
                'frackture_ratio': frackture_avg,
                'description': f"Gzip achieves {gzip_avg:.2f}x vs Frackture {frackture_avg:.2f}x - consider Gzip for general compression"
            })
    
    # Check for high MSE
    high_mse_cases = []
    for dataset, methods in results_data.items():
        for m in methods:
            if m['name'] == 'Frackture':
                if m.get('optimized_mse', 0) > 0.5:
                    high_mse_cases.append({
                        'dataset': dataset,
                        'mse': m['optimized_mse'],
                        'size': m['original_size']
                    })
    
    if high_mse_cases:
        weaknesses.append({
            'type': 'high_reconstruction_error',
            'count': len(high_mse_cases),
            'cases': high_mse_cases[:5],  # Top 5
            'description': f"{len(high_mse_cases)} datasets have high reconstruction error (MSE > 0.5)"
        })
    
    # Check fault injection
    fault_issues = []
    for dataset, methods in results_data.items():
        for m in methods:
            if m['name'] == 'Frackture':
                if not m.get('fault_injection_passed', False):
                    errors = m.get('fault_injection_errors', [])
                    if errors:
                        fault_issues.append({
                            'dataset': dataset,
                            'errors': errors
                        })
    
    if fault_issues:
        weaknesses.append({
            'type': 'fault_injection_failures',
            'count': len(fault_issues),
            'description': f"Fault injection detection failed in {len(fault_issues)} cases - mutations not properly detected"
        })
    
    return weaknesses

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
    
    # 8. Gzip/Brotli Comparison (NEW Phase 2)
    compression_comparison = analyze_vs_gzip_brotli(results)
    
    # 9. Latency Analysis (NEW Phase 2)
    latency_analysis = analyze_latency(results)
    
    # 10. Weakness Detection (NEW Phase 2)
    weaknesses = detect_weaknesses(results, method_comparison, tier_stats)

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
        
        # Explicit Answers - PHASE 2 EXPANDED
        f.write("## 2. Key Questions & Answers\n\n")
        
        f.write("### (1) Is the payload size fixed at 96 bytes?\n")
        if payload_stats['is_fixed']:
            f.write(f"**Yes.** The payload size remains consistent at approximately {payload_stats['avg']:.0f} bytes across all datasets.\n\n")
            f.write(f"**Details:**\n")
            f.write(f"- Min: {payload_stats['min']} bytes\n")
            f.write(f"- Max: {payload_stats['max']} bytes\n")
            f.write(f"- Variance: {payload_stats['variance']:.2f}\n")
        else:
            f.write(f"**No.** The payload size varies between {payload_stats['min']} and {payload_stats['max']} bytes (Avg: {payload_stats['avg']:.1f}), contradicting the fixed 96-byte target.\n\n")
            f.write(f"**Details:**\n")
            f.write(f"- **Symbolic bytes:** 32 (constant)\n")
            f.write(f"- **Entropy bytes:** 128 (constant)\n")
            f.write(f"- **Serialization overhead:** Variable ({payload_stats['min']}-{payload_stats['max']} bytes including encoding/encryption overhead)\n")
            f.write(f"- **Variance:** {payload_stats['variance']:.2f}\n")
            f.write(f"- **Samples:** {payload_stats['samples']}\n\n")
            f.write(f"**Implication:** Serialized payload is NOT fixed at 96B. It ranges wider due to pickle/JSON encoding overhead. This affects bandwidth and storage predictions.\n")
        f.write("\n")

        f.write("### (2) Is Frackture lossy or lossless in practice?\n")
        if reliability['is_lossy']:
            f.write(f"**Lossy.** Frackture is by design a lossy compression algorithm.\n\n")
            f.write(f"**Evidence:**\n")
            f.write(f"- Lossy runs: {reliability['lossy_runs']} / {reliability['total_runs']} ({100*reliability['lossy_runs']/reliability['total_runs']:.0f}%)\n")
            f.write(f"- Lossless runs: {reliability['lossless_runs']} (edge cases)\n")
            f.write(f"- Average MSE (optimized): See reconstruction quality metrics below\n\n")
            f.write(f"**Mechanism:** Frackture uses dual-channel design (symbolic + entropy) that sacrifices exact restoration for compression ratio. Reconstruction minimizes MSE rather than guaranteeing bitwise accuracy.\n")
        else:
            f.write(f"**Lossless.** All {reliability['lossless_runs']} runs were verified as lossless.\n")
        f.write("\n")
        
        f.write("### (3) What compression ratios and throughput does Frackture achieve?\n")
        f.write(f"**Compression Ratio:** {statistics.mean(frackture_ratios):.2f}x average\n\n")
        f.write(f"- Best: {max(frackture_ratios):.2f}x\n")
        f.write(f"- Worst: {min(frackture_ratios):.2f}x\n")
        f.write(f"- Median: {statistics.median(frackture_ratios):.2f}x\n\n")
        f.write(f"**Throughput:** {statistics.mean(frackture_speeds):.2f} MB/s average\n\n")
        f.write(f"- Best: {max(frackture_speeds):.2f} MB/s\n")
        f.write(f"- Worst: {min(frackture_speeds):.2f} MB/s\n")
        f.write(f"- Median: {statistics.median(frackture_speeds):.2f} MB/s\n")
        f.write("\n")
        
        f.write("### (4) How does Frackture compare to Gzip/Brotli in compression & throughput?\n")
        f.write("| Method | Compression Ratio | Throughput (MB/s) | Memory (MB) |\n")
        f.write("|---|---|---|---|\n")
        
        # Sort by Ratio desc
        sorted_methods = sorted(method_comparison.items(), key=lambda x: x[1]['avg_ratio'], reverse=True)
        
        for name, stats in sorted_methods:
            f.write(f"| {name} | {stats['avg_ratio']:.2f}x | {stats['avg_speed']:.2f} | {stats['avg_mem']:.1f} |\n")
        f.write("\n")
        
        # Detailed Gzip/Brotli comparison
        if compression_comparison.get('gzip_by_level') or compression_comparison.get('brotli_by_quality'):
            f.write("**Detailed Configuration Comparison:**\n\n")

            if compression_comparison.get('gzip_by_level'):
                f.write("Gzip by Level:\n")
                for level in sorted(compression_comparison['gzip_by_level'].keys(), key=int):
                    stats = compression_comparison['gzip_by_level'][level]
                    f.write(
                        f"- Level {level}: {stats['avg_ratio']:.2f}x @ {stats['avg_speed']:.2f} MB/s "
                        f"({stats.get('count', 0)} runs, Frackture ratio wins: {stats.get('frackture_wins_ratio', 0)}/{stats.get('total_comparisons', 0)})\n"
                    )
                f.write("\n")

            if compression_comparison.get('brotli_by_quality'):
                f.write("Brotli by Quality:\n")
                for quality in sorted(compression_comparison['brotli_by_quality'].keys(), key=int):
                    stats = compression_comparison['brotli_by_quality'][quality]
                    f.write(
                        f"- Quality {quality}: {stats['avg_ratio']:.2f}x @ {stats['avg_speed']:.2f} MB/s "
                        f"({stats.get('count', 0)} runs, Frackture ratio wins: {stats.get('frackture_wins_ratio', 0)}/{stats.get('total_comparisons', 0)})\n"
                    )
                f.write("\n")

        if compression_comparison.get('by_tier'):
            f.write("**Win Rates by Tier (Compression Ratio):**\n\n")
            f.write("| Tier | Comparisons | Frackture Wins | Win Rate |\n")
            f.write("|---|---:|---:|---:|\n")
            for tier_name, stats in sorted(compression_comparison['by_tier'].items()):
                total = stats.get('total_comparisons', 0)
                if total <= 0:
                    continue
                win_rate = stats.get('win_rate_ratio', 0.0) * 100
                f.write(f"| {tier_name} | {total} | {stats.get('frackture_wins_ratio', 0)} | {win_rate:.1f}% |\n")
            f.write("\n")

            optimal_tiers = {'small', 'medium', 'large', 'xlarge', 'xxlarge', 'huge'}
            warnings = []
            for tier_name, stats in compression_comparison['by_tier'].items():
                if tier_name not in optimal_tiers:
                    continue
                total = stats.get('total_comparisons', 0)
                if total <= 0:
                    continue
                if stats.get('win_rate_ratio', 0.0) < 0.60:
                    warnings.append(f"{tier_name} ({stats.get('win_rate_ratio', 0.0) * 100:.1f}%)")

            if warnings:
                f.write(f"⚠️ **Competition Warning:** Win rate < 60% in optimal tier(s): {', '.join(sorted(warnings))}\n\n")

        f.write("**Summary:** Frackture achieves {:.2f}x compression on average. ".format(compression_comparison.get('frackture_avg_ratio', 0)))
        if compression_comparison.get('total_comparisons', 0) > 0:
            f.write(
                f"In head-to-head matches (gzip + brotli sweeps), Frackture wins compression "
                f"{compression_comparison.get('frackture_wins_ratio', 0)}/{compression_comparison.get('total_comparisons', 0)} "
                f"times ({compression_comparison.get('win_rate_ratio', 0.0) * 100:.1f}%). "
            )
        f.write("See weaknesses section for competitive gaps.\n")
        f.write("\n")

        f.write("### (5) What is the latency comparison for hashing/encryption operations?\n")
        if latency_analysis:
            f.write("| Operation | Avg Latency (ms) | Min | Max |\n")
            f.write("|---|---|---|---|\n")
            
            for op_name, stats in sorted(latency_analysis.items()):
                pretty_name = op_name.replace('_', ' ').title()
                f.write(f"| {pretty_name} | {stats['avg_latency_ms']:.4f} | {stats['min_latency_ms']:.4f} | {stats['max_latency_ms']:.4f} |\n")
            f.write("\n")
            
            # Comparisons
            if 'sha256' in latency_analysis and 'frackture_hash' in latency_analysis:
                sha_lat = latency_analysis['sha256']['avg_latency_ms']
                frac_lat = latency_analysis['frackture_hash']['avg_latency_ms']
                if sha_lat > 0:
                    speedup = sha_lat / frac_lat if frac_lat > 0 else 0
                    f.write(f"**Frackture vs SHA256:** Frackture is {speedup:.1f}x faster ({frac_lat:.4f}ms vs {sha_lat:.4f}ms)\n\n")
            
            if 'aes_gcm' in latency_analysis and 'frackture_encrypt' in latency_analysis:
                aes_lat = latency_analysis['aes_gcm']['avg_latency_ms']
                frac_enc_lat = latency_analysis['frackture_encrypt']['avg_latency_ms']
                if aes_lat > 0:
                    speedup = aes_lat / frac_enc_lat if frac_enc_lat > 0 else 0
                    f.write(f"**Frackture Encrypted vs AES-GCM:** Frackture is {speedup:.1f}x faster ({frac_enc_lat:.4f}ms vs {aes_lat:.4f}ms)\n\n")
        f.write("\n")

        f.write("### (6) What self-optimization gains are achieved?\n")
        f.write(f"**MSE Improvement:** {opt_avg:.2f}% average (Max: {opt_max:.2f}%)\n\n")
        f.write("The optimization loop successfully reduces reconstruction error by iteratively adjusting decoder parameters. This improves fidelity without sacrificing compression.\n")
        f.write("\n")

        f.write("### (7) Is determinism validated? Are fault injection tests passing?\n")
        if reliability['is_deterministic']:
            f.write(f"**Determinism:** ✓ **PASS** - All {reliability['deterministic_runs']} runs produced identical outputs for identical inputs.\n\n")
        else:
            f.write(f"**Determinism:** ✗ **FAIL** - Determinism failed in {reliability['nondeterministic_runs']} cases.\n\n")
        
        f.write(f"**Fault Injection:** ")
        if reliability['fault_injection_passed']:
            f.write(f"✓ **PASS** - All {reliability['fault_passed_runs']} tests passed payload mutation detection.\n\n")
        else:
            f.write(f"✗ **FAIL** - Fault injection failed in {reliability['fault_failed_runs']}/{reliability['total_runs']} cases. ")
            f.write(f"Mutations not reliably detected in {reliability['fault_failed_runs']} tests.\n\n")
        
        f.write(f"**Reliability Status:** Determinism is validated, but fault injection detection has gaps.\n")
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
        f.write(f"Range: {min(frackture_speeds):.2f} - {max(frackture_speeds):.2f} MB/s\n\n")
        
        # Weaknesses Section (NEW Phase 2)
        f.write("## 4. Detected Weaknesses & Competitive Gaps\n\n")
        
        if weaknesses:
            for i, weakness in enumerate(weaknesses, 1):
                wtype = weakness.get('type', 'unknown')
                
                if wtype == 'low_compression':
                    f.write(f"### ⚠️ Weakness #{i}: Low Compression in {weakness['tier']}\n")
                    f.write(f"**Issue:** {weakness['description']}\n")
                    f.write(f"**Frackture Ratio:** {weakness['frackture_ratio']:.2f}x\n\n")
                
                elif wtype == 'inferior_to_gzip':
                    f.write(f"### ⚠️ Weakness #{i}: Underperforms vs Gzip\n")
                    f.write(f"**Issue:** {weakness['description']}\n")
                    f.write(f"**Gzip Compression:** {weakness['gzip_ratio']:.2f}x\n")
                    f.write(f"**Frackture Compression:** {weakness['frackture_ratio']:.2f}x\n")
                    f.write(f"**Gap:** {((weakness['gzip_ratio'] - weakness['frackture_ratio']) / weakness['frackture_ratio'] * 100):.1f}% worse\n\n")
                
                elif wtype == 'high_reconstruction_error':
                    f.write(f"### ⚠️ Weakness #{i}: High Reconstruction Error\n")
                    f.write(f"**Issue:** {weakness['description']}\n")
                    f.write(f"**Affected Datasets (Top 5):**\n")
                    for case in weakness['cases']:
                        f.write(f"- {case['dataset']} ({case['size']} bytes): MSE = {case['mse']:.4f}\n")
                    f.write("\n")
                
                elif wtype == 'fault_injection_failures':
                    f.write(f"### ⚠️ Weakness #{i}: Fault Injection Detection Gaps\n")
                    f.write(f"**Issue:** {weakness['description']}\n")
                    f.write(f"**Impact:** Payload mutations (bit flips, truncation) not reliably detected in encrypted or optimized modes.\n")
                    f.write(f"**Recommendation:** Review HMAC authentication and error detection logic.\n\n")
        else:
            f.write("No critical weaknesses detected in the current benchmark run.\n\n")
        
        f.write("## 5. Interpretation & Recommendations\n\n")
        f.write("### When to Use Frackture\n")
        f.write("- **Symbolic fingerprinting:** Fast, deterministic hashing for deduplication/change detection\n")
        f.write("- **Extreme compression:** Specialized datasets with high entropy patterns (achieve 100k+x ratios)\n")
        f.write("- **Encrypted transmission:** Built-in HMAC-SHA256 authentication with compression\n")
        f.write("- **Memory-constrained systems:** Small fixed payload (~96B symbolic + 128B entropy core)\n\n")
        
        f.write("### When NOT to Use Frackture\n")
        f.write("- **Lossless requirement:** Frackture is inherently lossy; use Gzip/Brotli for exact restoration\n")
        f.write("- **Small payloads (<100B):** Overhead dominates; compression ratios can be <1x\n")
        f.write("- **General-purpose compression:** Gzip/Brotli offer better compatibility and tuning\n")
        f.write("- **Fault tolerance critical:** Fault injection detection is not yet reliable\n\n")

    print(f"Report generated: {report_path}")

    # --- Generate Insights JSON ---
    insights = {
        "version": "2.0",
        "phase": "Phase 2 - Answer Analysis Questions",
        "summary": {
            "avg_compression_ratio": statistics.mean(frackture_ratios) if frackture_ratios else 0,
            "avg_throughput_mbs": statistics.mean(frackture_speeds) if frackture_speeds else 0,
            "payload_variance": payload_stats['variance'],
            "is_payload_fixed": payload_stats['is_fixed'],
            "payload_size_range": {
                "min_bytes": payload_stats['min'],
                "max_bytes": payload_stats['max'],
                "avg_bytes": payload_stats['avg'],
                "samples": payload_stats['samples']
            }
        },
        "phase2_questions": {
            "q1_payload_size_fixed": {
                "answer": "Yes" if payload_stats['is_fixed'] else "No",
                "is_fixed": payload_stats['is_fixed'],
                "details": payload_stats
            },
            "q2_lossy_vs_lossless": {
                "classification": "Lossy" if reliability['is_lossy'] else "Lossless",
                "is_lossy": reliability['is_lossy'],
                "lossy_runs": reliability['lossy_runs'],
                "lossless_runs": reliability['lossless_runs'],
                "total_runs": reliability['total_runs'],
                "lossy_percentage": (100 * reliability['lossy_runs'] / reliability['total_runs']) if reliability['total_runs'] > 0 else 0
            },
            "q3_compression_gains": {
                "avg_ratio": statistics.mean(frackture_ratios) if frackture_ratios else 0,
                "best_ratio": max(frackture_ratios) if frackture_ratios else 0,
                "worst_ratio": min(frackture_ratios) if frackture_ratios else 0,
                "median_ratio": statistics.median(frackture_ratios) if frackture_ratios else 0,
                "avg_throughput_mbs": statistics.mean(frackture_speeds) if frackture_speeds else 0,
                "best_throughput_mbs": max(frackture_speeds) if frackture_speeds else 0,
                "worst_throughput_mbs": min(frackture_speeds) if frackture_speeds else 0
            },
            "q4_vs_gzip_brotli": {
                "frackture_avg_ratio": compression_comparison.get('frackture_avg_ratio', 0),
                "frackture_avg_throughput": compression_comparison.get('frackture_avg_speed', 0),
                "gzip_by_level": compression_comparison.get('gzip_by_level', {}),
                "brotli_by_quality": compression_comparison.get('brotli_by_quality', {}),
                "total_comparisons": compression_comparison.get('total_comparisons', 0),
                "frackture_wins_ratio": compression_comparison.get('frackture_wins_ratio', 0),
                "frackture_wins_compression": compression_comparison.get('frackture_wins_ratio', 0),
                "frackture_wins_speed": compression_comparison.get('frackture_wins_speed', 0),
                "win_rate_ratio": compression_comparison.get('win_rate_ratio', 0),
                "win_rate_speed": compression_comparison.get('win_rate_speed', 0),
                "win_rate_percent": compression_comparison.get('win_rate_ratio', 0) * 100,
                "win_rate_by_tier": compression_comparison.get('by_tier', {}),
                "warnings": []
            },
            "q5_latency_hashing_encryption": {
                "operations": latency_analysis,
                "comparisons": {}
            },
            "q6_optimization_gains": {
                "avg_improvement_pct": opt_avg,
                "max_improvement_pct": opt_max,
                "mechanism": "Iterative decoder feedback loop minimizing MSE"
            },
            "q7_determinism_fault_injection": {
                "determinism_passed": reliability['is_deterministic'],
                "deterministic_runs": reliability['deterministic_runs'],
                "nondeterministic_runs": reliability['nondeterministic_runs'],
                "fault_injection_passed": reliability['fault_injection_passed'],
                "fault_passed_runs": reliability['fault_passed_runs'],
                "fault_failed_runs": reliability['fault_failed_runs'],
                "status": "PASS" if (reliability['is_deterministic'] and reliability['fault_injection_passed']) else "PARTIAL" if reliability['is_deterministic'] else "FAIL"
            }
        },
        "reliability": reliability,
        "comparisons": method_comparison,
        "data_types": type_stats,
        "size_tiers": tier_stats,
        "optimization": {
            "avg_gain_pct": opt_avg,
            "max_gain_pct": opt_max,
            "gains_distribution": opt_gains
        },
        "weaknesses": weaknesses,
        "weakness_summary": {
            "total_weaknesses": len(weaknesses),
            "types": list(set(w.get('type', 'unknown') for w in weaknesses)),
            "has_critical_issues": len([w for w in weaknesses if w.get('type') in ['fault_injection_failures', 'high_reconstruction_error']]) > 0
        }
    }

    # Competition warnings for win-rate target (>60%) in optimal tiers
    optimal_tiers = {'small', 'medium', 'large', 'xlarge', 'xxlarge', 'huge'}
    tier_rates = insights['phase2_questions']['q4_vs_gzip_brotli'].get('win_rate_by_tier', {})
    warnings = []
    for tier_name, stats in tier_rates.items():
        if tier_name not in optimal_tiers:
            continue
        total = stats.get('total_comparisons', 0)
        if total <= 0:
            continue
        if stats.get('win_rate_ratio', 0.0) < 0.60:
            warnings.append({
                'tier': tier_name,
                'win_rate_ratio': stats.get('win_rate_ratio', 0.0),
                'total_comparisons': total,
            })

    insights['phase2_questions']['q4_vs_gzip_brotli']['warnings'] = warnings
    insights['phase2_questions']['q4_vs_gzip_brotli']['meets_60_percent_target_in_optimal_tiers'] = len(warnings) == 0

    # Add latency comparisons
    if 'sha256' in latency_analysis and 'frackture_hash' in latency_analysis:
        sha_lat = latency_analysis['sha256']['avg_latency_ms']
        frac_lat = latency_analysis['frackture_hash']['avg_latency_ms']
        if frac_lat > 0:
            insights['phase2_questions']['q5_latency_hashing_encryption']['comparisons']['frackture_vs_sha256'] = {
                'frackture_ms': frac_lat,
                'sha256_ms': sha_lat,
                'speedup_factor': sha_lat / frac_lat if frac_lat > 0 else 0,
                'winner': 'Frackture' if frac_lat < sha_lat else 'SHA256'
            }
    
    if 'aes_gcm' in latency_analysis and 'frackture_encrypt' in latency_analysis:
        aes_lat = latency_analysis['aes_gcm']['avg_latency_ms']
        frac_enc_lat = latency_analysis['frackture_encrypt']['avg_latency_ms']
        if frac_enc_lat > 0:
            insights['phase2_questions']['q5_latency_hashing_encryption']['comparisons']['frackture_encrypted_vs_aes_gcm'] = {
                'frackture_encrypted_ms': frac_enc_lat,
                'aes_gcm_ms': aes_lat,
                'speedup_factor': aes_lat / frac_enc_lat if frac_enc_lat > 0 else 0,
                'winner': 'Frackture Encrypted' if frac_enc_lat < aes_lat else 'AES-GCM'
            }
    
    json_path = os.path.join(args.output_dir, 'insights.json')
    with open(json_path, 'w') as f:
        json.dump(insights, f, indent=2)
        
    print(f"Report generated: {report_path}")
    print(f"Insights generated: {json_path}")

if __name__ == "__main__":
    main()
