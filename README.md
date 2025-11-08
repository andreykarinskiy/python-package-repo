# python-package-repo

A minimal example project prepared for publishing to PyPI. The package exposes a
single helper `hello` that prints a greeting.

## Installation

```bash
pip install python-package-repo
```

## Usage

```python
from python_package_repo import hello

hello("World")
```

## Development Setup

```bash
python -m venv .venv
.venv\Scripts\activate  # PowerShell: .venv\Scripts\Activate.ps1
pip install -e .[dev]
```

## Build and Publish

Build the source distribution and wheel:

```bash
python -m build
```

Upload the artifacts in `dist/`:

```bash
python -m twine upload dist/*
```

See `pyproject.toml` for additional project metadata.