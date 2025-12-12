"""
Dataset Repository for Frackture Benchmarks

Loads and manages real dataset samples with intelligent scaling.
Replaces the synthetic DatasetGenerator with real, redistribution-safe samples.
"""

import yaml
from pathlib import Path
from typing import Dict, List, Optional, Union, Iterator
import io
from dataclasses import dataclass


@dataclass
class DatasetInfo:
    """Metadata about a dataset"""
    name: str
    category: str
    subcategory: str
    file: str
    canonical_size: int
    description: str
    compressibility: str
    scaling_method: str
    min_size: int
    max_size: int
    optional: bool = False


@dataclass
class SizeTier:
    """Size tier configuration"""
    name: str
    min: int
    max: int
    target: int
    optional: bool = False


class DatasetRepository:
    """
    Repository for loading and scaling real dataset samples.
    
    Features:
    - Loads real files from benchmarks/datasets/
    - Scales by repeating/concatenating to target size
    - Down-samples for tiny payloads
    - Streams chunked reads for 100MB+ cases
    - Builds mixed payloads from multiple datasets
    - Validates manifest against on-disk files
    """
    
    def __init__(self, datasets_dir: Optional[Path] = None, manifest_path: Optional[Path] = None):
        """
        Initialize the dataset repository.
        
        Args:
            datasets_dir: Path to datasets directory (default: benchmarks/datasets/)
            manifest_path: Path to manifest file (default: datasets_dir/manifest.yaml)
        """
        if datasets_dir is None:
            datasets_dir = Path(__file__).parent / "datasets"
        
        self.datasets_dir = Path(datasets_dir)
        
        if manifest_path is None:
            manifest_path = self.datasets_dir / "manifest.yaml"
        
        self.manifest_path = Path(manifest_path)
        
        # Load manifest
        self._load_manifest()
        
        # Validate files exist
        self._validate_files()
    
    def _load_manifest(self):
        """Load and parse the manifest file"""
        if not self.manifest_path.exists():
            raise FileNotFoundError(f"Manifest not found: {self.manifest_path}")
        
        with open(self.manifest_path, 'r') as f:
            self.manifest = yaml.safe_load(f)
        
        # Parse datasets
        self.datasets: Dict[str, DatasetInfo] = {}
        for name, config in self.manifest.get('datasets', {}).items():
            self.datasets[name] = DatasetInfo(
                name=name,
                category=config['category'],
                subcategory=config['subcategory'],
                file=config['file'],
                canonical_size=config['canonical_size'],
                description=config['description'],
                compressibility=config['compressibility'],
                scaling_method=config['scaling']['method'],
                min_size=config['scaling']['min_size'],
                max_size=config['scaling']['max_size'],
                optional=config.get('optional', False)
            )
        
        # Parse size tiers
        self.size_tiers: Dict[str, SizeTier] = {}
        for name, config in self.manifest.get('size_tiers', {}).items():
            self.size_tiers[name] = SizeTier(
                name=name,
                min=config['min'],
                max=config['max'],
                target=config['target'],
                optional=config.get('optional', False)
            )
        
        # Parse mixed combinations
        self.mixed_combinations = self.manifest.get('mixed_combinations', {})
    
    def _validate_files(self):
        """Validate that dataset files exist on disk"""
        missing = []
        for name, info in self.datasets.items():
            file_path = self.datasets_dir / info.file
            if not file_path.exists():
                if not info.optional:
                    missing.append(f"{name} -> {info.file}")
        
        if missing:
            raise FileNotFoundError(
                f"Missing required dataset files:\n  " + "\n  ".join(missing)
            )
    
    def list_datasets(self) -> List[str]:
        """List all available dataset names"""
        return list(self.datasets.keys())
    
    def list_categories(self) -> List[str]:
        """List all dataset categories"""
        return sorted(set(info.category for info in self.datasets.values()))
    
    def list_size_tiers(self) -> List[str]:
        """List all size tier names"""
        return list(self.size_tiers.keys())
    
    def get_dataset_info(self, name: str) -> DatasetInfo:
        """Get metadata for a specific dataset"""
        if name not in self.datasets:
            raise KeyError(f"Dataset not found: {name}")
        return self.datasets[name]
    
    def get_datasets_by_category(self, category: str) -> List[str]:
        """Get all dataset names in a category"""
        return [
            name for name, info in self.datasets.items()
            if info.category == category
        ]
    
    def load_raw(self, name: str) -> bytes:
        """Load the raw dataset file without scaling"""
        info = self.get_dataset_info(name)
        file_path = self.datasets_dir / info.file
        
        if not file_path.exists():
            if info.optional:
                raise FileNotFoundError(f"Optional dataset not available: {name}")
            raise FileNotFoundError(f"Dataset file not found: {file_path}")
        
        with open(file_path, 'rb') as f:
            return f.read()
    
    def load_scaled(self, name: str, target_size: int) -> bytes:
        """
        Load dataset scaled to target size.
        
        Args:
            name: Dataset name
            target_size: Target size in bytes
            
        Returns:
            Scaled dataset bytes
        """
        info = self.get_dataset_info(name)
        
        # Validate size is within scaling limits
        if target_size < info.min_size:
            raise ValueError(
                f"Target size {target_size} below minimum {info.min_size} for {name}"
            )
        if target_size > info.max_size:
            raise ValueError(
                f"Target size {target_size} above maximum {info.max_size} for {name}"
            )
        
        # Load raw data
        raw_data = self.load_raw(name)
        
        # Scale to target size
        if info.scaling_method == 'repeat':
            return self._scale_by_repeat(raw_data, target_size)
        else:
            raise ValueError(f"Unknown scaling method: {info.scaling_method}")
    
    def load_by_tier(self, name: str, tier: str) -> bytes:
        """
        Load dataset scaled to a specific size tier.
        
        Args:
            name: Dataset name
            tier: Size tier name (tiny, small, medium, large, xlarge, xxlarge, huge)
            
        Returns:
            Scaled dataset bytes
        """
        if tier not in self.size_tiers:
            raise KeyError(f"Unknown size tier: {tier}")
        
        tier_info = self.size_tiers[tier]
        return self.load_scaled(name, tier_info.target)
    
    def _scale_by_repeat(self, data: bytes, target_size: int) -> bytes:
        """
        Scale data by repeating/concatenating.
        
        For sizes smaller than the original, truncate.
        For sizes larger than the original, repeat and truncate.
        """
        if not data:
            raise ValueError("Cannot scale empty data")
        
        data_size = len(data)
        
        if target_size <= data_size:
            # Truncate or use as-is
            return data[:target_size]
        
        # Calculate how many repetitions we need
        repetitions = (target_size // data_size) + 1
        repeated = data * repetitions
        
        # Truncate to exact target size
        return repeated[:target_size]
    
    def load_mixed(self, combination_name: str, target_size: int) -> bytes:
        """
        Load a mixed payload combining multiple datasets.
        
        Args:
            combination_name: Name of the mixed combination from manifest
            target_size: Target total size in bytes
            
        Returns:
            Mixed payload bytes
        """
        if combination_name not in self.mixed_combinations:
            raise KeyError(f"Unknown mixed combination: {combination_name}")
        
        combo = self.mixed_combinations[combination_name]
        components = combo['components']
        
        # Calculate total weight
        total_weight = sum(c['weight'] for c in components)
        
        # Build mixed payload
        mixed_data = b''
        
        for component in components:
            dataset_name = component['dataset']
            weight = component['weight']
            
            # Calculate size for this component
            component_size = int((weight / total_weight) * target_size)
            
            # Load and scale component
            try:
                component_data = self.load_scaled(dataset_name, max(50, component_size))
                mixed_data += component_data[:component_size]
            except (FileNotFoundError, KeyError) as e:
                # Skip optional datasets that don't exist
                info = self.datasets.get(dataset_name)
                if info and info.optional:
                    continue
                raise
        
        # Ensure we hit the target size exactly
        if len(mixed_data) < target_size:
            # Pad with first component
            first_dataset = components[0]['dataset']
            padding_needed = target_size - len(mixed_data)
            first_info = self.get_dataset_info(first_dataset)
            # Use at least min_size for the component
            padding = self.load_scaled(first_dataset, max(padding_needed, first_info.min_size))
            mixed_data += padding[:padding_needed]
        
        return mixed_data[:target_size]
    
    def load_mixed_custom(self, datasets: List[str], target_size: int, 
                         weights: Optional[List[int]] = None) -> bytes:
        """
        Load a custom mixed payload from specified datasets.
        
        Args:
            datasets: List of dataset names to combine
            target_size: Target total size in bytes
            weights: Optional weights for each dataset (default: equal weights)
            
        Returns:
            Mixed payload bytes
        """
        if not datasets:
            raise ValueError("Must specify at least one dataset")
        
        if weights is None:
            weights = [1] * len(datasets)
        
        if len(weights) != len(datasets):
            raise ValueError("Number of weights must match number of datasets")
        
        # Calculate total weight
        total_weight = sum(weights)
        
        # Build mixed payload
        mixed_data = b''
        
        for dataset_name, weight in zip(datasets, weights):
            # Calculate size for this component
            component_size = int((weight / total_weight) * target_size)
            
            # Load and scale component
            component_data = self.load_scaled(dataset_name, max(50, component_size))
            mixed_data += component_data[:component_size]
        
        # Ensure we hit the target size exactly
        if len(mixed_data) < target_size:
            # Pad with first dataset
            padding_needed = target_size - len(mixed_data)
            first_info = self.get_dataset_info(datasets[0])
            # Use at least min_size for the component
            padding = self.load_scaled(datasets[0], max(padding_needed, first_info.min_size))
            mixed_data += padding[:padding_needed]
        
        return mixed_data[:target_size]
    
    def stream_chunks(self, name: str, target_size: int, chunk_size: int = 1024*1024) -> Iterator[bytes]:
        """
        Stream dataset in chunks for very large sizes (100MB+).
        
        Args:
            name: Dataset name
            target_size: Target total size in bytes
            chunk_size: Size of each chunk (default: 1MB)
            
        Yields:
            Chunks of data
        """
        info = self.get_dataset_info(name)
        raw_data = self.load_raw(name)
        
        bytes_yielded = 0
        
        while bytes_yielded < target_size:
            # Determine how much to yield in this chunk
            remaining = target_size - bytes_yielded
            current_chunk_size = min(chunk_size, remaining)
            
            # Create chunk by repeating raw data
            chunk = self._scale_by_repeat(raw_data, current_chunk_size)
            
            yield chunk
            bytes_yielded += len(chunk)
    
    def get_all_datasets(self, tier: str = 'medium', 
                        skip_optional: bool = True) -> Dict[str, bytes]:
        """
        Get all datasets at a specific size tier.
        
        Args:
            tier: Size tier name (default: 'medium' = 100KB)
            skip_optional: Skip optional datasets that don't exist
            
        Returns:
            Dictionary mapping dataset name to scaled bytes
        """
        datasets = {}
        
        for name in self.list_datasets():
            info = self.datasets[name]
            
            # Skip optional datasets if requested
            if skip_optional and info.optional:
                file_path = self.datasets_dir / info.file
                if not file_path.exists():
                    continue
            
            try:
                datasets[name] = self.load_by_tier(name, tier)
            except FileNotFoundError:
                if not skip_optional:
                    raise
        
        return datasets
    
    def enumerate_datasets(self) -> str:
        """
        Generate a formatted string listing all available datasets.
        
        Returns:
            Formatted dataset listing
        """
        lines = []
        lines.append("=" * 80)
        lines.append("AVAILABLE DATASETS")
        lines.append("=" * 80)
        lines.append("")
        
        # Group by category
        categories = self.list_categories()
        
        for category in categories:
            lines.append(f"📁 {category.upper()}")
            lines.append("-" * 80)
            
            dataset_names = self.get_datasets_by_category(category)
            for name in dataset_names:
                info = self.datasets[name]
                file_path = self.datasets_dir / info.file
                exists = "✓" if file_path.exists() else "✗"
                optional = " (optional)" if info.optional else ""
                
                lines.append(f"  {exists} {name:30} {info.description}")
                lines.append(f"     File: {info.file} ({info.canonical_size} bytes){optional}")
                lines.append(f"     Scaling: {info.min_size} - {info.max_size} bytes")
            
            lines.append("")
        
        # List size tiers
        lines.append("📏 SIZE TIERS")
        lines.append("-" * 80)
        for tier_name, tier_info in self.size_tiers.items():
            optional = " (optional)" if tier_info.optional else ""
            lines.append(f"  {tier_name:10} target={tier_info.target:>12,} bytes  "
                        f"range=[{tier_info.min:>10,}, {tier_info.max:>12,}]{optional}")
        lines.append("")
        
        # List mixed combinations
        lines.append("🔀 MIXED COMBINATIONS")
        lines.append("-" * 80)
        for combo_name, combo_info in self.mixed_combinations.items():
            lines.append(f"  {combo_name:20} {combo_info['description']}")
            for component in combo_info['components']:
                lines.append(f"     - {component['dataset']:25} weight={component['weight']}")
        lines.append("")
        
        lines.append("=" * 80)
        
        return "\n".join(lines)
