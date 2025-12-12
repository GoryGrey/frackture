.PHONY: help install install-dev test test-cov lint format check build clean publish publish-test version

help:
	@echo "Frackture Development Makefile"
	@echo ""
	@echo "Available targets:"
	@echo "  install         - Install package in editable mode"
	@echo "  install-dev     - Install package with dev dependencies"
	@echo "  test            - Run test suite"
	@echo "  test-cov        - Run tests with coverage report"
	@echo "  lint            - Run linter (ruff check)"
	@echo "  format          - Format code (ruff format)"
	@echo "  check           - Run lint and tests"
	@echo "  build           - Build distribution packages"
	@echo "  clean           - Remove build artifacts"
	@echo "  publish-test    - Upload to Test PyPI"
	@echo "  publish         - Upload to PyPI (requires version tag)"
	@echo "  version         - Show current version"
	@echo "  benchmark       - Run benchmark suite"
	@echo ""

install:
	pip install -e .

install-dev:
	pip install -e ".[dev,benchmark]"

test:
	pytest

test-cov:
	pytest --cov=frackture --cov-report=term-missing --cov-report=html

lint:
	ruff check src tests benchmarks

format:
	ruff format src tests benchmarks

check: lint test

build: clean
	python -m build

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf src/*.egg-info
	rm -rf .pytest_cache
	rm -rf .ruff_cache
	rm -rf htmlcov
	rm -rf .coverage
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete

publish-test: build
	@echo "Publishing to Test PyPI..."
	twine upload --repository testpypi dist/*

publish: build
	@echo "Publishing to PyPI..."
	@echo "Make sure you have:"
	@echo "  1. Tagged the release (git tag vX.Y.Z)"
	@echo "  2. Pushed the tag (git push origin vX.Y.Z)"
	@echo "  3. Set TWINE_USERNAME and TWINE_PASSWORD"
	@echo ""
	@read -p "Continue? [y/N] " -n 1 -r; \
	echo; \
	if [[ $$REPLY =~ ^[Yy]$$ ]]; then \
		twine upload dist/*; \
	else \
		echo "Aborted."; \
	fi

version:
	@python -c "try:\n  from importlib.metadata import version\n  print(version('frackture'))\nexcept:\n  print('Not installed or development version')"

benchmark:
	python benchmarks/benchmark_frackture.py
