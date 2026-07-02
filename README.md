# qcom-oss-pypi-pilot

A minimal pilot package demonstrating how to publish a Python package to PyPI
from a Qualcomm Open Source project.

## Installation

```bash
pip install qcom-oss-pypi-pilot
```

## Usage

```python
from qcom_oss_pypi_pilot import hello

print(hello.greet())          # Hello, World!
print(hello.greet("PyPI"))    # Hello, PyPI!
```

Or from the command line (if the entry-point is installed):

```bash
qcom-hello
```

## Development

```bash
# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# Install in editable mode with test dependencies
pip install -e ".[dev]"

# Run tests
pytest
```

## License

BSD-3-Clause — see [LICENSE](LICENSE) for details.
