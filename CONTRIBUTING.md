# Contributing to rompy-notebooks

Keep notebook examples focused and runnable where their external requirements permit. Avoid committing Jupyter checkpoints, caches, or generated run directories.

## Documentation validation

Install the documentation tools and run the combined quality gate before opening a pull request:

```bash
python -m pip install -r requirements-docs.txt
make docs-build
```

The standard documentation build renders stored notebook outputs without executing model code. For a rendered preview with current journey plots, run `make docs-build-executed`; it executes only staged, non-runtime-dependent journey notebooks and requires their Python dependencies and fixture data. Full SWAN, XBeach, and SCHISM execution requires additional model-specific runtimes and is handled separately from both documentation modes.
