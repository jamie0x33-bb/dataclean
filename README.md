# dataclean

Lightweight CSV data cleaning utility for Python.

## Install

```bash
pip install .
```

## Usage

```python
from dataclean import clean_csv

# Remove duplicates and normalize whitespace
clean_csv("input.csv", "output.csv", dedup=True, strip=True)
```

### CLI

```bash
dataclean input.csv -o output.csv --dedup --strip --drop-empty
```

## Features

- Remove duplicate rows
- Strip leading/trailing whitespace
- Drop rows where all fields are empty
- Normalize line endings
- Configurable column selection

## Requirements

- Python 3.8+

## License

MIT
