# Publishing to PyPI Guide

This guide will help you publish your `llmself` package to PyPI using uv.

## Prerequisites

1. **PyPI Account**: Create accounts on both [TestPyPI](https://test.pypi.org/) and [PyPI](https://pypi.org/)
2. **API Tokens**: Generate API tokens for both platforms
3. **Dependencies**: Install required publishing tools

## Step-by-Step Publishing Process

### 1. Install Publishing Dependencies

```bash
uv add --dev twine
```

### 2. Update Package Information

Before publishing, make sure to update the following in `pyproject.toml`:
- `version`: Increment the version number
- `authors`: Replace with your actual name and email
- `project.urls`: Update with your actual repository URLs

### 3. Configure Authentication

#### Option A: Using API Tokens (Recommended)

Create a `.pypirc` file in your home directory:

```ini
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = pypi-your-api-token-here

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-your-testpypi-token-here
```

#### Option B: Using Environment Variables

```bash
export TWINE_USERNAME=__token__
export TWINE_PASSWORD=pypi-your-api-token-here
```

### 4. Build the Package

```bash
# Clean previous builds
rm -rf dist/

# Build the package
uv build
```

This will create:
- `dist/llmself-0.1.0.tar.gz` (source distribution)
- `dist/llmself-0.1.0-py3-none-any.whl` (wheel distribution)

### 5. Check the Package

```bash
uv run twine check dist/*
```

### 6. Test on TestPyPI (Recommended)

First, upload to TestPyPI to make sure everything works:

```bash
uv run twine upload --repository testpypi dist/*
```

Then test the installation:

```bash
pip install --index-url https://test.pypi.org/simple/ llmself
```

### 7. Upload to PyPI

Once you've verified everything works on TestPyPI:

```bash
uv run twine upload dist/*
```

### 8. Verify the Upload

Check your package on PyPI: https://pypi.org/project/llmself/

Test installation:

```bash
pip install llmself
```

## Automation Script

You can use the provided script to automate the build process:

```bash
python scripts/publish.py
```

## Version Management

For future releases:

1. Update the version in `pyproject.toml`
2. Update the changelog/release notes
3. Commit your changes
4. Tag the release: `git tag v0.1.1`
5. Push tags: `git push --tags`
6. Repeat the publishing process

## Troubleshooting

### Common Issues

1. **Package name already exists**: Choose a unique name or add a prefix
2. **Authentication errors**: Double-check your API tokens
3. **Build errors**: Ensure all dependencies are properly specified
4. **Upload errors**: Check package metadata and file permissions

### Useful Commands

```bash
# Check package metadata
uv run python -m build --help

# List package contents
tar -tzf dist/llmself-0.1.0.tar.gz

# Check wheel contents
unzip -l dist/llmself-0.1.0-py3-none-any.whl
```

## Security Notes

- Never commit API tokens to version control
- Use environment variables or `.pypirc` for authentication
- Consider using trusted publishing with GitHub Actions for automation
