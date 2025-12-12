# Release Guide

This document describes how to build, test, and publish releases for Frackture.

## Prerequisites

1. Install development dependencies:
   ```bash
   make install-dev
   ```

2. Ensure you have PyPI credentials configured:
   - For username/password: Set `TWINE_USERNAME` and `TWINE_PASSWORD` environment variables
   - For API token (recommended): Create a `.pypirc` file or use `TWINE_USERNAME=__token__` and `TWINE_PASSWORD=<your-token>`

3. (Optional) Install `act` for local CI testing:
   ```bash
   # macOS
   brew install act
   
   # Linux
   curl https://raw.githubusercontent.com/nektos/act/master/install.sh | sudo bash
   ```

## Development Workflow

### Running Tests Locally

```bash
# Run all tests
make test

# Run tests with coverage
make test-cov

# Run linter
make lint

# Format code
make format

# Run both lint and tests
make check
```

### Running Benchmarks

```bash
# Full benchmark suite
make benchmark

# Quick smoke test
cd benchmarks && python benchmark_frackture.py --quick
```

## Release Process

### 1. Prepare the Release

1. **Update changelog/documentation** if needed
   
2. **Ensure all tests pass**:
   ```bash
   make check
   ```

3. **Run benchmark smoke test**:
   ```bash
   cd benchmarks && python benchmark_frackture.py --quick
   ```

### 2. Version Tagging

Frackture uses **setuptools-scm** for automatic versioning based on git tags.

1. **Create and push a version tag**:
   ```bash
   # Tag the release (use semantic versioning)
   git tag v0.1.0
   
   # Push the tag to origin
   git push origin v0.1.0
   ```

2. **Tag format**: Use `vX.Y.Z` format (e.g., `v1.0.0`, `v0.2.1`)
   - `X` = Major version (breaking changes)
   - `Y` = Minor version (new features, backward compatible)
   - `Z` = Patch version (bug fixes)

### 3. Automated Release via GitHub Actions

Once you push a tag, GitHub Actions will automatically:

1. ✅ Run linting across Python 3.8-3.12
2. ✅ Run tests on Linux, Windows, and macOS
3. ✅ Run benchmark smoke test
4. 📦 Build distribution packages (wheel and sdist)
5. 🚀 Publish to PyPI (requires trusted publishing setup)

**Monitor the release**: Check the [Actions tab](https://github.com/GoryGrey/frackture/actions) to ensure all steps pass.

### 4. Manual Release (if needed)

If you need to publish manually or test the build:

#### Test Build

```bash
# Build packages
make build

# Check the built packages
ls -lh dist/
```

The `dist/` directory should contain:
- `frackture-X.Y.Z-py3-none-any.whl` (wheel)
- `frackture-X.Y.Z.tar.gz` (source distribution)

#### Test Installation

```bash
# Install from wheel in a fresh virtual environment
python -m venv test-env
source test-env/bin/activate  # On Windows: test-env\Scripts\activate
pip install dist/frackture-*.whl

# Test import
python -c "import frackture; print(frackture.__version__)"

# Test CLI
frackture version

# Cleanup
deactivate
rm -rf test-env
```

#### Publish to Test PyPI

Test publishing before releasing to production PyPI:

```bash
make publish-test
```

Then test installation from Test PyPI:
```bash
pip install --index-url https://test.pypi.org/simple/ frackture
```

#### Publish to PyPI

Once you've verified everything:

```bash
make publish
```

Or manually:
```bash
twine upload dist/*
```

## CI/CD Configuration

### GitHub Actions Trusted Publishing

**Recommended**: Use PyPI trusted publishing (no need for API tokens in secrets).

1. Go to [PyPI Publishing Settings](https://pypi.org/manage/account/publishing/)
2. Add a new "pending publisher":
   - PyPI Project Name: `frackture`
   - Owner: `GoryGrey`
   - Repository: `frackture`
   - Workflow name: `ci.yml`
   - Environment: `pypi`

### Alternative: Manual Secrets

If not using trusted publishing, add to GitHub repository secrets:
- `PYPI_API_TOKEN`: Your PyPI API token

Update `.github/workflows/ci.yml` to use:
```yaml
- name: Publish to PyPI
  env:
    TWINE_USERNAME: __token__
    TWINE_PASSWORD: ${{ secrets.PYPI_API_TOKEN }}
  run: twine upload dist/*
```

## Local CI Testing with Act

Test GitHub Actions workflows locally:

```bash
# Test the CI workflow
act -j test

# Test linting job
act -j lint

# Test full workflow for a tag
act -j build --eventpath test-event.json
```

Create `test-event.json`:
```json
{
  "ref": "refs/tags/v0.1.0",
  "repository": {
    "name": "frackture",
    "full_name": "GoryGrey/frackture"
  }
}
```

## Version Numbering

### Automatic Version from Git Tags

setuptools-scm automatically determines the version:

- **Tagged commit**: Uses the tag (e.g., `v1.0.0` → `1.0.0`)
- **Post-tag commits**: Appends `.postN` (e.g., `1.0.0.post1`)
- **No tags**: Uses `0.0.0` or configured fallback

### Check Current Version

```bash
# From git tags
git describe --tags

# From installed package
python -c "from importlib.metadata import version; print(version('frackture'))"

# Using Makefile
make version
```

## Troubleshooting

### Build Issues

**Problem**: `setuptools-scm` can't determine version
```
LookupError: setuptools-scm was unable to detect version
```

**Solution**: Ensure you're in a git repository with at least one commit:
```bash
git init
git add .
git commit -m "Initial commit"
```

### PyPI Upload Issues

**Problem**: Package already exists on PyPI
```
HTTPError: 400 Bad Request - File already exists
```

**Solution**: You can't re-upload the same version. Increment the version tag:
```bash
git tag v0.1.1
git push origin v0.1.1
```

**Problem**: Invalid credentials
```
HTTPError: 403 Forbidden
```

**Solution**: Check your PyPI credentials:
- Verify `TWINE_USERNAME` and `TWINE_PASSWORD` are set
- For API tokens, username should be `__token__`
- Ensure the token has upload permissions for the `frackture` package

### Test Failures

**Problem**: Tests fail in CI but pass locally

**Solution**:
1. Check Python version compatibility (CI tests multiple versions)
2. Run tests in a clean virtual environment
3. Check for missing dependencies in `pyproject.toml`

## Rollback

If you need to roll back a release:

1. **Yank the release from PyPI** (doesn't delete, but hides it):
   ```bash
   # Via web interface: https://pypi.org/manage/project/frackture/
   # Or use twine (requires twine >= 4.0.2):
   # twine upload --skip-existing --repository pypi --yank "reason" dist/*
   ```

2. **Delete the git tag locally and remotely**:
   ```bash
   git tag -d v0.1.0
   git push origin :refs/tags/v0.1.0
   ```

3. **Fix the issue and release a new version**

## Resources

- [Semantic Versioning](https://semver.org/)
- [setuptools-scm Documentation](https://github.com/pypa/setuptools_scm/)
- [PyPI Trusted Publishing](https://docs.pypi.org/trusted-publishers/)
- [Python Packaging Guide](https://packaging.python.org/)
