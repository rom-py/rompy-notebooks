# Installation guide

The notebook environment and the documentation environment are separate concerns.

## Documentation site

Install the lightweight documentation toolchain from the repository root:

```bash
python -m pip install -r requirements-docs.txt
make docs-build
```

This does not install or execute SWAN, XBeach, or SCHISM model binaries. See the [build and execution guide](workflow.md) for the full validation boundary.

## Notebook execution

To execute a particular notebook, install the compatible `rompy` model plugin and its data/runtime requirements first. These requirements vary by model and are intentionally not hidden behind the documentation build.
