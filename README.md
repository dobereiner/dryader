
# dryader

**dryader** is a lightweight Python library for downloading datasets from [DRYAD](https://datadryad.org/).  
It provides a simple command-line interface (CLI) and Python API for fetching dataset files efficiently.

## Features
- Download DRYAD datasets via DOI
- Parallel downloads for improved speed
- Cross-platform support (Windows, macOS, Linux)
- CLI and Python API for flexible usage

## Installation

### Install from source
```bash
git clone https://github.com/dobereiner/dryader.git
cd dryader
pip install -e .
```

### Install directly from GitHub
```bash
pip install git+https://github.com/dobereiner/dryader.git
```

## Usage

### CLI
```bash
dryader <DOI> -o <output_directory> -t <threads>
```
Example:
```bash
dryader 10.5061/dryad.8pk0p2ns8 -o downloads -t 4
```
- `<DOI>` – DRYAD dataset DOI
- `-o, --output` – Output directory (default: `downloads`)
- `-t, --threads` – Number of parallel downloads (default: `4`)

### Python API
```python
from dryader import get_file_links, download_files_parallel

doi = "10.5061/dryad.8pk0p2ns8"
file_links = get_file_links(doi)
download_files_parallel(file_links, output_dir="downloads", max_workers=4)
```

## Development
To contribute, clone the repository and install dependencies:
```bash
git clone https://github.com/dobereiner/dryader.git
cd dryader
pip install -e .
pip install pytest requests-mock
```

Run tests:
```bash
pytest
```

## License
MIT License © 2025