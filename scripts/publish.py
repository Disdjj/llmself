#!/usr/bin/env python3
"""
Script to help publish the package to PyPI
"""

import subprocess
import sys
from pathlib import Path


def run_command(cmd, check=True):
    """Run a command and print it."""
    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, check=check)
    return result


def main():
    """Main publishing workflow."""
    # Ensure we're in the project root
    project_root = Path(__file__).parent.parent
    print(f"Working in: {project_root}")
    
    # Clean previous builds
    print("\n1. Cleaning previous builds...")
    dist_dir = project_root / "dist"
    if dist_dir.exists():
        import shutil
        shutil.rmtree(dist_dir)
    
    # Build the package
    print("\n2. Building the package...")
    run_command(["uv", "build"])
    
    # Check the built package
    print("\n3. Checking the built package...")
    run_command(["uv", "run", "twine", "check", "dist/*"])
    
    print("\n4. Package built successfully!")
    print("Next steps:")
    print("- Review the built files in the 'dist/' directory")
    print("- Test install: uv pip install dist/*.whl")
    print("- Upload to TestPyPI first: uv run twine upload --repository testpypi dist/*")
    print("- Upload to PyPI: uv run twine upload dist/*")


if __name__ == "__main__":
    main()
