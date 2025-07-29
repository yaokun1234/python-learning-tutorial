# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Environment Setup

This is a Python learning environment with:
- Python 3.9.6 virtual environment located in `.venv/`
- Virtual environment activated with: `source .venv/bin/activate`
- Deactivate virtual environment with: `deactivate`

## Development Commands

### Python Environment
```bash
# Activate virtual environment
source .venv/bin/activate

# Install packages
pip install package_name

# List installed packages
pip list

# Generate requirements file
pip freeze > requirements.txt

# Install from requirements
pip install -r requirements.txt

# Run Python scripts
python script_name.py

# Interactive Python shell
python
```

### Code Quality
```bash
# Format code (if black is installed)
black .

# Check code style (if flake8 is installed)
flake8 .

# Type checking (if mypy is installed)
mypy .
```

### Testing
```bash
# Run tests with pytest (if installed)
pytest

# Run specific test file
pytest test_file.py

# Run with coverage (if pytest-cov is installed)
pytest --cov=.
```

## Architecture Notes

This is a clean Python learning environment. When creating new projects:
- Create a main project directory for each learning topic
- Use descriptive file names that indicate the concept being learned
- Consider organizing by topic (e.g., `basics/`, `data_structures/`, `algorithms/`)
- Add appropriate dependencies to requirements.txt as needed