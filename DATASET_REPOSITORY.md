# Dataset Repository Implementation

This document describes the new real dataset system for Frackture benchmarking.

## Overview

The dataset repository replaces synthetic `DatasetGenerator` with a comprehensive system for loading, scaling, and managing real, redistribution-safe sample files.

## Components

### 1. Dataset Files (`benchmarks/datasets/`)

Curated sample files covering all major content types:

**Text (4 files):**
- `sample_text.txt` - Natural language prose (596 bytes)
- `sample_log.log` - Application log entries (625 bytes)
- `sample_data.json` - Structured JSON data (814 bytes)
- `sample_data.csv` - Tabular CSV data (222 bytes)

**Binary (4 files):**
- `sample_image.png` - Minimal PNG (69 bytes)
- `sample_image.jpg` - Minimal JPEG (138 bytes)
- `sample_document.pdf` - Minimal PDF (457 bytes)
- `sample_animation.gif` - Minimal GIF (43 bytes)

**Code (3 files):**
- `sample_code.js` - JavaScript source (563 bytes)
- `sample_minified.min.js` - Minified JS (223 bytes)
- `sample_module.py` - Python module (1206 bytes)

**Structured (3 files):**
- `sample_database.db` - SQLite database (12KB)
- `sample_pickle.pkl` - Python pickle (161 bytes)
- `sample_msgpack.msgpack` - MessagePack (85 bytes, optional)

**Mixed (1 file):**
- `sample_mixed.bin` - Multi-format bundle (1878 bytes)

### 2. Manifest (`benchmarks/datasets/manifest.yaml`)

YAML configuration describing:
- Dataset metadata (category, description, compressibility)
- Canonical file sizes
- Scaling rules (method, min/max sizes)
- Size tier definitions (tiny to huge)
- Predefined mixed combinations

### 3. DatasetRepository (`benchmarks/dataset_repository.py`)

Python class providing:
- `load_raw(name)` - Load original file
- `load_scaled(name, size)` - Scale to target size
- `load_by_tier(name, tier)` - Load at size tier
- `load_mixed(combination, size)` - Mixed payload from manifest
- `load_mixed_custom(datasets, size, weights)` - Custom mix
- `stream_chunks(name, size, chunk_size)` - Stream large files
- `get_all_datasets(tier)` - All datasets at tier
- `enumerate_datasets()` - Pretty-print all datasets

### 4. CLI Tool (`benchmarks/dataset_cli.py`)

Command-line interface:
```bash
# List all datasets
python dataset_cli.py list

# Show dataset info
python dataset_cli.py info text_plain

# Load and save dataset
python dataset_cli.py load text_plain --tier medium --save output.bin

# Test all datasets
python dataset_cli.py test

# Load mixed payload
python dataset_cli.py mixed --combination text_heavy --size 100000

# Show categories
python dataset_cli.py categories
```

### 5. Generator Script (`benchmarks/datasets/generate_samples.py`)

Script to regenerate all sample files with correct sizes.

### 6. Updated Benchmark (`benchmarks/benchmark_frackture.py`)

Enhanced to support both real and synthetic datasets:
```bash
# Use real datasets (default)
python benchmark_frackture.py

# Use synthetic datasets (legacy)
python benchmark_frackture.py --synthetic
```

### 7. Test Suite (`tests/test_dataset_repository.py`)

45 comprehensive tests validating:
- Repository initialization
- Manifest validation
- File loading and scaling
- Mixed payloads
- Size tiers
- Streaming
- Edge cases

## Size Tiers

| Tier    | Target   | Range             | Use Case          |
|---------|----------|-------------------|-------------------|
| tiny    | 50 B     | 1 B - 99 B       | Minimal payloads  |
| small   | 1 KB     | 100 B - 10 KB    | Headers, metadata |
| medium  | 100 KB   | 10 KB - 500 KB   | Documents, configs|
| large   | 1 MB     | 500 KB - 5 MB    | Large files       |
| xlarge  | 10 MB    | 5 MB - 50 MB     | Media files       |
| xxlarge | 100 MB   | 50 MB - 500 MB   | Large datasets    |
| huge    | 1 GB     | 500 MB - 10 GB   | Optional, skipped |

## Mixed Combinations

Predefined payload mixes:
- **text_heavy** - 70% text, 30% other
- **binary_heavy** - 70% binary, 30% other
- **code_heavy** - Code with metadata
- **structured_heavy** - Structured data formats
- **balanced** - Equal mix of all categories

## Scaling Methods

**Repeat Method:**
- Small sizes: Truncate original file
- Large sizes: Repeat + truncate to exact target
- Preserves content patterns when scaled

## Features

✅ **Redistribution-safe** - All files are minimal/synthetic  
✅ **Comprehensive** - Covers all major content types  
✅ **Scalable** - Files scale from 35 bytes to 100MB+  
✅ **Validated** - Full test coverage with 45 tests  
✅ **Documented** - Complete README and CLI help  
✅ **Backward compatible** - Synthetic mode still available  
✅ **Streaming support** - Chunk reads for 100MB+ files  
✅ **Mixed payloads** - Combine multiple dataset types  
✅ **CLI integration** - Easy exploration and testing  

## Usage Examples

### Python API

```python
from benchmarks.dataset_repository import DatasetRepository

# Initialize
repo = DatasetRepository()

# Load at specific tier
data = repo.load_by_tier('text_plain', 'medium')  # 100KB

# Load scaled
data = repo.load_scaled('code_python', 50000)  # Exactly 50KB

# Mixed payload
mixed = repo.load_mixed('balanced', 100000)  # 100KB balanced mix

# Stream large file
for chunk in repo.stream_chunks('text_json', 100_000_000):
    process(chunk)

# Get all datasets
all_datasets = repo.get_all_datasets(tier='large')  # All at 1MB
```

### CLI

```bash
# Explore datasets
python dataset_cli.py list
python dataset_cli.py categories
python dataset_cli.py info text_plain

# Load and test
python dataset_cli.py load text_json --tier medium --preview
python dataset_cli.py test --tiers tiny small medium

# Mixed payloads
python dataset_cli.py mixed --combination code_heavy --size 1000000
```

### Benchmarks

```bash
# Real datasets (auto-detected)
python benchmark_frackture.py --small-only

# Force real datasets
python benchmark_frackture.py --real

# Legacy synthetic
python benchmark_frackture.py --synthetic
```

## File Structure

```
benchmarks/
├── datasets/
│   ├── __init__.py
│   ├── README.md
│   ├── manifest.yaml
│   ├── generate_samples.py
│   ├── sample_text.txt
│   ├── sample_log.log
│   ├── sample_data.json
│   ├── sample_data.csv
│   ├── sample_image.png
│   ├── sample_image.jpg
│   ├── sample_document.pdf
│   ├── sample_animation.gif
│   ├── sample_database.db
│   ├── sample_pickle.pkl
│   ├── sample_msgpack.msgpack (optional)
│   ├── sample_code.js
│   ├── sample_minified.min.js
│   ├── sample_module.py
│   └── sample_mixed.bin
├── dataset_repository.py
├── dataset_cli.py
└── benchmark_frackture.py (updated)

tests/
└── test_dataset_repository.py (new)
```

## Dependencies

- **pyyaml** - Added to `requirements.txt` for manifest parsing
- All other dependencies unchanged

## Acceptance Criteria ✅

All requirements from the ticket have been met:

✅ **Directory structure** - `benchmarks/datasets/` with all required samples  
✅ **Content classes** - Text, binary, structured, code, mixed covered  
✅ **Manifest** - YAML manifest with types, sizes, and scaling rules  
✅ **Size tiers** - 7 tiers from sub-100B to 100MB+  
✅ **DatasetRepository** - Replaces DatasetGenerator  
✅ **Streaming** - Chunks bytes from files  
✅ **Concatenate/repeat** - Hits target sizes exactly  
✅ **Mixed payloads** - Combines multiple categories  
✅ **Down-sampling** - Truncates for tiny payloads  
✅ **Streaming** - Chunked reads for 100MB+ cases  
✅ **Tests** - 45 unit tests validate manifest sync  
✅ **CLI enumerate** - Lists all datasets with details  
✅ **CLI fetch** - Gets every category/size  
✅ **Graceful skipping** - Reports when optional files missing  

## Testing

Run tests:
```bash
# Dataset repository tests
python -m pytest tests/test_dataset_repository.py -v

# Validate all datasets
cd benchmarks
python dataset_cli.py test

# Quick sanity check
python dataset_cli.py test --tiers tiny small medium
```

All 45 tests pass successfully.

## Documentation

- Main README updated with dataset info
- New `benchmarks/datasets/README.md` with usage guide
- CLI has built-in help: `python dataset_cli.py --help`
- This implementation document (DATASET_REPOSITORY.md)

## Future Enhancements

Possible improvements:
- Add more file types (YAML, XML, protobuf, etc.)
- Support compression pre-processing for some formats
- Add dataset versioning
- Include checksums in manifest
- Add download option for optional large files
- Support for streaming from remote sources
