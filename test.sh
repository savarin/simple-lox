#!/bin/bash

# Stop on the first error
set -e

# Run black for code formatting check
echo "Running black..."
black --check .

# Run pyflakes for static code analysis
echo "Running pyflakes..."
pyflakes .

# Run mypy for type checking
echo "Running mypy..."
mypy --strict .

# Run pytest for running unit tests
echo "Running pytest..."
pytest

echo "All checks passed!"
