#!/usr/bin/env python3
"""
Dataset Repository CLI

Command-line tool for exploring and testing dataset repository.
"""

import argparse
import sys
from pathlib import Path
from dataset_repository import DatasetRepository


def cmd_list(args):
    """List all available datasets"""
    repo = DatasetRepository()
    print(repo.enumerate_datasets())


def cmd_info(args):
    """Show information about a specific dataset"""
    repo = DatasetRepository()
    
    try:
        info = repo.get_dataset_info(args.dataset)
        print(f"Dataset: {info.name}")
        print(f"  Category: {info.category} / {info.subcategory}")
        print(f"  Description: {info.description}")
        print(f"  File: {info.file}")
        print(f"  Canonical Size: {info.canonical_size:,} bytes")
        print(f"  Compressibility: {info.compressibility}")
        print(f"  Scaling Method: {info.scaling_method}")
        print(f"  Size Range: {info.min_size:,} - {info.max_size:,} bytes")
        if info.optional:
            print(f"  Optional: Yes")
            file_path = repo.datasets_dir / info.file
            print(f"  Available: {'Yes' if file_path.exists() else 'No'}")
    except KeyError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    
    return 0


def cmd_load(args):
    """Load and display dataset information"""
    repo = DatasetRepository()
    
    try:
        if args.tier:
            data = repo.load_by_tier(args.dataset, args.tier)
            print(f"Loaded {args.dataset} at tier '{args.tier}': {len(data):,} bytes")
        else:
            data = repo.load_raw(args.dataset)
            print(f"Loaded {args.dataset} (raw): {len(data):,} bytes")
        
        if args.save:
            output_path = Path(args.save)
            with open(output_path, 'wb') as f:
                f.write(data)
            print(f"Saved to: {output_path}")
        
        if args.preview and not args.save:
            preview_size = min(200, len(data))
            print(f"\nPreview (first {preview_size} bytes):")
            print("-" * 80)
            try:
                print(data[:preview_size].decode('utf-8', errors='replace'))
            except:
                print(data[:preview_size])
    
    except (KeyError, FileNotFoundError, ValueError) as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    
    return 0


def cmd_test(args):
    """Test loading all datasets at all tiers"""
    repo = DatasetRepository()
    
    print("Testing dataset repository...")
    print("=" * 80)
    
    tiers_to_test = args.tiers if args.tiers else repo.list_size_tiers()
    datasets_to_test = args.datasets if args.datasets else repo.list_datasets()
    
    total_tests = 0
    passed_tests = 0
    failed_tests = 0
    skipped_tests = 0
    
    for dataset_name in datasets_to_test:
        info = repo.get_dataset_info(dataset_name)
        
        for tier_name in tiers_to_test:
            total_tests += 1
            
            try:
                tier_info = repo.size_tiers[tier_name]
                
                # Skip huge tier unless explicitly requested
                if tier_info.optional and not args.include_optional:
                    print(f"⊘ {dataset_name:30} @ {tier_name:10} - SKIPPED (optional tier)")
                    skipped_tests += 1
                    continue
                
                # Skip if target size is out of range
                if tier_info.target < info.min_size or tier_info.target > info.max_size:
                    print(f"⊘ {dataset_name:30} @ {tier_name:10} - SKIPPED (out of range)")
                    skipped_tests += 1
                    continue
                
                data = repo.load_by_tier(dataset_name, tier_name)
                expected_size = tier_info.target
                actual_size = len(data)
                
                if actual_size == expected_size:
                    print(f"✓ {dataset_name:30} @ {tier_name:10} - OK ({actual_size:,} bytes)")
                    passed_tests += 1
                else:
                    print(f"✗ {dataset_name:30} @ {tier_name:10} - SIZE MISMATCH "
                          f"(expected {expected_size:,}, got {actual_size:,})")
                    failed_tests += 1
            
            except FileNotFoundError as e:
                if info.optional:
                    print(f"⊘ {dataset_name:30} @ {tier_name:10} - SKIPPED (optional, file missing)")
                    skipped_tests += 1
                else:
                    print(f"✗ {dataset_name:30} @ {tier_name:10} - ERROR: {e}")
                    failed_tests += 1
            
            except Exception as e:
                print(f"✗ {dataset_name:30} @ {tier_name:10} - ERROR: {e}")
                failed_tests += 1
    
    print("=" * 80)
    print(f"Total: {total_tests}, Passed: {passed_tests}, Failed: {failed_tests}, Skipped: {skipped_tests}")
    
    return 0 if failed_tests == 0 else 1


def cmd_mixed(args):
    """Load a mixed payload combination"""
    repo = DatasetRepository()
    
    try:
        if args.combination:
            # Load predefined combination
            data = repo.load_mixed(args.combination, args.size)
            print(f"Loaded mixed combination '{args.combination}': {len(data):,} bytes")
        elif args.datasets:
            # Load custom combination
            weights = args.weights if args.weights else None
            data = repo.load_mixed_custom(args.datasets, args.size, weights)
            print(f"Loaded custom mix of {len(args.datasets)} datasets: {len(data):,} bytes")
        else:
            print("Error: Must specify either --combination or --datasets", file=sys.stderr)
            return 1
        
        if args.save:
            output_path = Path(args.save)
            with open(output_path, 'wb') as f:
                f.write(data)
            print(f"Saved to: {output_path}")
    
    except (KeyError, FileNotFoundError, ValueError) as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    
    return 0


def cmd_categories(args):
    """List all categories and datasets in each"""
    repo = DatasetRepository()
    
    categories = repo.list_categories()
    
    print("Dataset Categories")
    print("=" * 80)
    
    for category in categories:
        datasets = repo.get_datasets_by_category(category)
        print(f"\n{category.upper()} ({len(datasets)} datasets)")
        print("-" * 80)
        for name in datasets:
            info = repo.get_dataset_info(name)
            print(f"  • {name:30} - {info.description}")
    
    return 0


def main():
    parser = argparse.ArgumentParser(
        description="Dataset Repository CLI for Frackture benchmarks"
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # List command
    parser_list = subparsers.add_parser('list', help='List all available datasets')
    parser_list.set_defaults(func=cmd_list)
    
    # Info command
    parser_info = subparsers.add_parser('info', help='Show dataset information')
    parser_info.add_argument('dataset', help='Dataset name')
    parser_info.set_defaults(func=cmd_info)
    
    # Load command
    parser_load = subparsers.add_parser('load', help='Load a dataset')
    parser_load.add_argument('dataset', help='Dataset name')
    parser_load.add_argument('--tier', help='Size tier (tiny, small, medium, large, etc.)')
    parser_load.add_argument('--save', help='Save to file')
    parser_load.add_argument('--preview', action='store_true', help='Show preview of data')
    parser_load.set_defaults(func=cmd_load)
    
    # Test command
    parser_test = subparsers.add_parser('test', help='Test loading all datasets')
    parser_test.add_argument('--datasets', nargs='+', help='Specific datasets to test')
    parser_test.add_argument('--tiers', nargs='+', help='Specific tiers to test')
    parser_test.add_argument('--include-optional', action='store_true', 
                            help='Include optional tiers (like huge)')
    parser_test.set_defaults(func=cmd_test)
    
    # Mixed command
    parser_mixed = subparsers.add_parser('mixed', help='Load mixed payload')
    parser_mixed.add_argument('--combination', help='Predefined combination name')
    parser_mixed.add_argument('--datasets', nargs='+', help='Custom dataset list')
    parser_mixed.add_argument('--weights', type=int, nargs='+', help='Weights for custom mix')
    parser_mixed.add_argument('--size', type=int, default=102400, 
                             help='Target size in bytes (default: 100KB)')
    parser_mixed.add_argument('--save', help='Save to file')
    parser_mixed.set_defaults(func=cmd_mixed)
    
    # Categories command
    parser_categories = subparsers.add_parser('categories', 
                                             help='List categories and their datasets')
    parser_categories.set_defaults(func=cmd_categories)
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return 1
    
    return args.func(args)


if __name__ == '__main__':
    sys.exit(main())
