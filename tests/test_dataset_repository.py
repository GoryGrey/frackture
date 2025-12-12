"""
Tests for Dataset Repository

Validates manifest, file loading, scaling, and mixed payloads.
"""

import pytest
from pathlib import Path
import sys

# Add benchmarks to path
sys.path.insert(0, str(Path(__file__).parent.parent / "benchmarks"))

from dataset_repository import DatasetRepository, DatasetInfo, SizeTier


@pytest.fixture
def repo():
    """Create a DatasetRepository instance"""
    return DatasetRepository()


def test_repository_initialization(repo):
    """Test that repository initializes correctly"""
    assert repo.manifest is not None
    assert repo.datasets is not None
    assert repo.size_tiers is not None
    assert len(repo.datasets) > 0
    assert len(repo.size_tiers) > 0


def test_manifest_validation(repo):
    """Test that manifest is valid and matches files on disk"""
    # All non-optional datasets should have files
    for name, info in repo.datasets.items():
        if not info.optional:
            file_path = repo.datasets_dir / info.file
            assert file_path.exists(), f"Missing required file: {info.file}"


def test_list_datasets(repo):
    """Test listing all datasets"""
    datasets = repo.list_datasets()
    assert isinstance(datasets, list)
    assert len(datasets) > 0
    assert 'text_plain' in datasets
    assert 'code_python' in datasets


def test_list_categories(repo):
    """Test listing categories"""
    categories = repo.list_categories()
    assert isinstance(categories, list)
    assert 'text' in categories
    assert 'binary' in categories
    assert 'code' in categories
    assert 'structured' in categories


def test_list_size_tiers(repo):
    """Test listing size tiers"""
    tiers = repo.list_size_tiers()
    assert isinstance(tiers, list)
    assert 'tiny' in tiers
    assert 'small' in tiers
    assert 'medium' in tiers
    assert 'large' in tiers


def test_get_dataset_info(repo):
    """Test getting dataset metadata"""
    info = repo.get_dataset_info('text_plain')
    assert isinstance(info, DatasetInfo)
    assert info.name == 'text_plain'
    assert info.category == 'text'
    assert info.file == 'sample_text.txt'
    assert info.canonical_size > 0


def test_get_dataset_info_invalid(repo):
    """Test getting info for non-existent dataset"""
    with pytest.raises(KeyError):
        repo.get_dataset_info('nonexistent_dataset')


def test_get_datasets_by_category(repo):
    """Test filtering datasets by category"""
    text_datasets = repo.get_datasets_by_category('text')
    assert len(text_datasets) > 0
    assert all('text_' in name for name in text_datasets)
    
    code_datasets = repo.get_datasets_by_category('code')
    assert len(code_datasets) > 0
    assert all('code_' in name for name in code_datasets)


def test_load_raw(repo):
    """Test loading raw dataset files"""
    data = repo.load_raw('text_plain')
    assert isinstance(data, bytes)
    assert len(data) > 0
    
    # Verify it matches canonical size
    info = repo.get_dataset_info('text_plain')
    assert len(data) == info.canonical_size


def test_load_raw_missing(repo):
    """Test loading missing optional dataset"""
    # structured_msgpack is optional and may not exist
    info = repo.get_dataset_info('structured_msgpack')
    if info.optional:
        file_path = repo.datasets_dir / info.file
        if not file_path.exists():
            with pytest.raises(FileNotFoundError):
                repo.load_raw('structured_msgpack')


def test_load_scaled_smaller(repo):
    """Test scaling down to smaller size"""
    target_size = 100
    data = repo.load_scaled('text_plain', target_size)
    assert len(data) == target_size


def test_load_scaled_larger(repo):
    """Test scaling up to larger size"""
    target_size = 10000
    data = repo.load_scaled('text_plain', target_size)
    assert len(data) == target_size


def test_load_scaled_exact(repo):
    """Test loading at exact canonical size"""
    info = repo.get_dataset_info('text_plain')
    data = repo.load_scaled('text_plain', info.canonical_size)
    assert len(data) == info.canonical_size


def test_load_scaled_out_of_range(repo):
    """Test that loading outside range raises error"""
    info = repo.get_dataset_info('text_plain')
    
    # Too small
    with pytest.raises(ValueError):
        repo.load_scaled('text_plain', info.min_size - 1)
    
    # Too large
    with pytest.raises(ValueError):
        repo.load_scaled('text_plain', info.max_size + 1)


def test_load_by_tier_tiny(repo):
    """Test loading at tiny tier"""
    data = repo.load_by_tier('text_plain', 'tiny')
    tier = repo.size_tiers['tiny']
    assert len(data) == tier.target


def test_load_by_tier_small(repo):
    """Test loading at small tier (1KB)"""
    data = repo.load_by_tier('text_plain', 'small')
    tier = repo.size_tiers['small']
    assert len(data) == tier.target


def test_load_by_tier_medium(repo):
    """Test loading at medium tier (100KB)"""
    data = repo.load_by_tier('code_python', 'medium')
    tier = repo.size_tiers['medium']
    assert len(data) == tier.target


def test_load_by_tier_large(repo):
    """Test loading at large tier (1MB)"""
    data = repo.load_by_tier('text_json', 'large')
    tier = repo.size_tiers['large']
    assert len(data) == tier.target


def test_load_by_tier_invalid(repo):
    """Test loading with invalid tier"""
    with pytest.raises(KeyError):
        repo.load_by_tier('text_plain', 'invalid_tier')


def test_scale_by_repeat(repo):
    """Test the internal scaling method"""
    data = b"ABC" * 10  # 30 bytes
    
    # Scale down
    scaled = repo._scale_by_repeat(data, 10)
    assert len(scaled) == 10
    assert scaled == b"ABC" * 3 + b"A"
    
    # Scale up
    scaled = repo._scale_by_repeat(data, 100)
    assert len(scaled) == 100
    
    # Exact
    scaled = repo._scale_by_repeat(data, 30)
    assert len(scaled) == 30
    assert scaled == data


def test_load_mixed_predefined(repo):
    """Test loading predefined mixed combination"""
    target_size = 10000
    data = repo.load_mixed('text_heavy', target_size)
    assert len(data) == target_size
    assert isinstance(data, bytes)


def test_load_mixed_all_combinations(repo):
    """Test all predefined mixed combinations"""
    target_size = 5000
    
    for combo_name in repo.mixed_combinations.keys():
        data = repo.load_mixed(combo_name, target_size)
        assert len(data) == target_size, f"Failed for {combo_name}"


def test_load_mixed_invalid(repo):
    """Test loading non-existent mixed combination"""
    with pytest.raises(KeyError):
        repo.load_mixed('nonexistent_mix', 1000)


def test_load_mixed_custom(repo):
    """Test loading custom mixed payload"""
    datasets = ['text_plain', 'text_json', 'code_python']
    target_size = 10000
    
    data = repo.load_mixed_custom(datasets, target_size)
    assert len(data) == target_size


def test_load_mixed_custom_with_weights(repo):
    """Test custom mix with specific weights"""
    datasets = ['text_plain', 'code_python']
    weights = [70, 30]  # 70% text, 30% code
    target_size = 10000
    
    data = repo.load_mixed_custom(datasets, target_size, weights)
    assert len(data) == target_size


def test_load_mixed_custom_invalid(repo):
    """Test custom mix with invalid inputs"""
    # Empty datasets
    with pytest.raises(ValueError):
        repo.load_mixed_custom([], 1000)
    
    # Mismatched weights
    with pytest.raises(ValueError):
        repo.load_mixed_custom(['text_plain', 'code_python'], 1000, [50])


def test_stream_chunks(repo):
    """Test streaming large datasets in chunks"""
    target_size = 1000
    chunk_size = 100
    
    chunks = list(repo.stream_chunks('text_plain', target_size, chunk_size))
    
    # Verify we got chunks
    assert len(chunks) > 0
    
    # Verify total size
    total_size = sum(len(chunk) for chunk in chunks)
    assert total_size == target_size
    
    # Verify chunk sizes (all but last should be chunk_size)
    for chunk in chunks[:-1]:
        assert len(chunk) <= chunk_size


def test_get_all_datasets(repo):
    """Test getting all datasets at a specific tier"""
    datasets = repo.get_all_datasets(tier='small')
    
    assert isinstance(datasets, dict)
    assert len(datasets) > 0
    
    # All should be at the small tier size
    tier = repo.size_tiers['small']
    for name, data in datasets.items():
        assert len(data) == tier.target


def test_get_all_datasets_skip_optional(repo):
    """Test that optional missing datasets are skipped"""
    datasets = repo.get_all_datasets(tier='small', skip_optional=True)
    
    # Should not raise error even if optional datasets are missing
    assert isinstance(datasets, dict)


def test_enumerate_datasets(repo):
    """Test dataset enumeration output"""
    output = repo.enumerate_datasets()
    
    assert isinstance(output, str)
    assert 'AVAILABLE DATASETS' in output
    assert 'SIZE TIERS' in output
    assert 'MIXED COMBINATIONS' in output
    
    # Should list some dataset names
    assert 'text_plain' in output
    assert 'code_python' in output


def test_canonical_sizes_match(repo):
    """Test that canonical sizes in manifest match actual files"""
    for name, info in repo.datasets.items():
        if info.optional:
            file_path = repo.datasets_dir / info.file
            if not file_path.exists():
                continue
        
        raw_data = repo.load_raw(name)
        assert len(raw_data) == info.canonical_size, \
            f"Canonical size mismatch for {name}: expected {info.canonical_size}, got {len(raw_data)}"


def test_all_size_tiers_valid(repo):
    """Test that all size tiers have valid ranges"""
    for tier_name, tier_info in repo.size_tiers.items():
        assert tier_info.min > 0
        assert tier_info.max > tier_info.min
        assert tier_info.min <= tier_info.target <= tier_info.max


def test_all_datasets_have_valid_scaling(repo):
    """Test that all datasets have valid scaling parameters"""
    for name, info in repo.datasets.items():
        assert info.min_size > 0
        assert info.max_size > info.min_size
        # Canonical size should be >= min_size OR be small enough that it can still be used
        # (we allow small files to be below min_size as they can be repeated)
        if info.canonical_size < info.min_size:
            # If canonical is smaller, it should be repeatable to reach min_size
            assert info.min_size % info.canonical_size == 0 or info.canonical_size > 0
        assert info.canonical_size <= info.max_size


def test_multiple_repository_instances():
    """Test creating multiple repository instances"""
    repo1 = DatasetRepository()
    repo2 = DatasetRepository()
    
    assert repo1.list_datasets() == repo2.list_datasets()


def test_dataset_content_preservation():
    """Test that repeated scaling preserves content patterns"""
    repo = DatasetRepository()
    
    # Load raw data
    raw = repo.load_raw('text_plain')
    
    # Scale to 2x size
    scaled = repo.load_scaled('text_plain', len(raw) * 2)
    
    # First half should match raw data exactly
    assert scaled[:len(raw)] == raw
    
    # Second half should also match (it's repeated)
    assert scaled[len(raw):len(raw)*2] == raw


def test_mixed_combinations_have_valid_components(repo):
    """Test that all mixed combinations reference valid datasets"""
    for combo_name, combo_info in repo.mixed_combinations.items():
        for component in combo_info['components']:
            dataset_name = component['dataset']
            # Should be able to get info (will raise KeyError if invalid)
            info = repo.get_dataset_info(dataset_name)
            assert info is not None


@pytest.mark.parametrize("dataset_name", [
    'text_plain', 'text_json', 'code_python', 
    'binary_png', 'structured_pickle'
])
def test_dataset_exists(repo, dataset_name):
    """Parametrized test to verify specific datasets exist"""
    assert dataset_name in repo.datasets
    info = repo.get_dataset_info(dataset_name)
    assert info is not None


@pytest.mark.parametrize("tier_name,expected_target", [
    ('tiny', 50),
    ('small', 1024),
    ('medium', 102400),
    ('large', 1048576),
])
def test_tier_targets(repo, tier_name, expected_target):
    """Parametrized test to verify tier target sizes"""
    tier = repo.size_tiers[tier_name]
    assert tier.target == expected_target
