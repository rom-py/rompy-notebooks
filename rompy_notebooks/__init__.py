"""
Example and tutorial notebooks for ROMPY
"""

import os
import importlib.resources

__version__ = "0.1.0"


def get_notebooks_dir():
    """
    Return the directory containing the example notebooks.
    """
    # For package installed via pip
    try:
        # This works for Python 3.9+
        return str(importlib.resources.files('rompy_notebooks').joinpath('notebooks_data'))
    except AttributeError:
        # Fallback for older Python versions
        import rompy_notebooks
        package_dir = os.path.dirname(rompy_notebooks.__file__)
        return os.path.join(package_dir, 'notebooks_data')