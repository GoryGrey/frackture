# Frackture Benchmark Datasets

This directory contains curated, redistribution-safe sample files used for benchmarking Frackture's compression, encryption, and hashing performance.

## Overview

All sample files are small base files designed to be:
- **Redistribution-safe**: No copyright issues, all files are minimal/synthetic
- **Representative**: Cover real-world content types
- **Scalable**: Can be repeated/concatenated to create larger test files

## Dataset Categories

### Text Datasets
- **sample_text.txt** - Natural language prose/documentation
- **sample_log.log** - Structured application log entries
- **sample_data.json** - JSON structured data
- **sample_data.csv** - Comma-separated tabular data

### Binary Datasets
- **sample_image.png** - Minimal valid PNG (1x1 pixel)
- **sample_image.jpg** - Minimal valid JPEG
- **sample_document.pdf** - Minimal valid PDF document
- **sample_animation.gif** - Minimal valid GIF (1x1 pixel)

### Code Datasets
- **sample_code.js** - JavaScript source code
- **sample_minified.min.js** - Minified JavaScript
- **sample_module.py** - Python source module

### Structured Datasets
- **sample_database.db** - SQLite database with tables
- **sample_pickle.pkl** - Python pickle serialized object
- **sample_msgpack.msgpack** - MessagePack serialized data (optional)

### Mixed Payloads
- **sample_mixed.bin** - Multi-format payload combining text, JSON, binary, and code

## Size Tiers

The manifest defines standard size tiers for benchmarking:

| Tier    | Target Size | Range                    | Use Case                    |
|---------|-------------|--------------------------|----------------------------|
| tiny    | 50 B        | 1 B - 99 B              | Minimal payloads           |
| small   | 1 KB        | 100 B - 10 KB           | Headers, metadata          |
| medium  | 100 KB      | 10 KB - 500 KB          | Documents, configs         |
| large   | 1 MB        | 500 KB - 5 MB           | Large files                |
| xlarge  | 10 MB       | 5 MB - 50 MB            | Media files                |
| xxlarge | 100 MB      | 50 MB - 500 MB          | Large datasets             |
| huge    | 1 GB        | 500 MB - 10 GB          | Very large datasets (optional) |

## Usage

### Using the CLI

```bash
# List all available datasets
python3 dataset_cli.py list

# Show information about a specific dataset
python3 dataset_cli.py info text_plain

# Load a dataset at a specific tier
python3 dataset_cli.py load text_plain --tier medium --save output.bin

# Test all datasets at all tiers
python3 dataset_cli.py test

# Load a mixed payload combination
python3 dataset_cli.py mixed --combination text_heavy --size 100000
```

### Using the Repository in Code

```python
from dataset_repository import DatasetRepository

# Initialize repository
repo = DatasetRepository()

# List available datasets
datasets = repo.list_datasets()

# Load raw dataset
raw_data = repo.load_raw('text_plain')

# Load scaled to specific size
data_100kb = repo.load_scaled('text_plain', 102400)

# Load at specific tier
data_medium = repo.load_by_tier('text_plain', 'medium')

# Get all datasets at a tier
all_medium = repo.get_all_datasets(tier='medium')

# Load mixed payload
mixed = repo.load_mixed('text_heavy', 100000)

# Stream large files in chunks
for chunk in repo.stream_chunks('text_plain', 100_000_000, chunk_size=1024*1024):
    process_chunk(chunk)
```

### Using in Benchmarks

```bash
# Run benchmarks with real datasets (default)
python3 benchmark_frackture.py

# Explicitly use real datasets
python3 benchmark_frackture.py --real

# Use synthetic datasets (legacy)
python3 benchmark_frackture.py --synthetic
```

## Manifest Format

The `manifest.yaml` file describes all datasets and their properties:

```yaml
datasets:
  text_plain:
    category: text
    subcategory: plain
    file: sample_text.txt
    canonical_size: 596
    description: "Natural language text"
    compressibility: high
    scaling:
      method: repeat
      min_size: 50
      max_size: 100_000_000
```

### Mixed Combinations

The manifest also defines predefined mixed payload combinations:

- **text_heavy** - 70% text formats, 30% other
- **binary_heavy** - 70% binary formats, 30% other
- **code_heavy** - Mix of code formats with metadata
- **structured_heavy** - Mix of structured data formats
- **balanced** - Equal mix of all categories

## Generating Datasets

To regenerate the sample files:

```bash
python3 generate_samples.py
```

This will create all sample files with the exact sizes expected by the manifest.

## Validation

The test suite validates that:
- All non-optional files exist on disk
- Canonical sizes match actual file sizes
- All datasets can be loaded and scaled
- Mixed combinations reference valid datasets

Run tests with:

```bash
cd ../..
python -m pytest tests/test_dataset_repository.py -v
```

## Adding New Datasets

To add a new dataset:

1. Create the sample file in this directory
2. Add an entry to `manifest.yaml` with:
   - Unique name
   - Category and subcategory
   - File path and canonical size
   - Scaling parameters
3. Mark as `optional: true` if the file may not exist
4. Run tests to validate

## License

All sample files are minimal/synthetic and redistribution-safe. The dataset repository follows the same MIT license as Frackture.
