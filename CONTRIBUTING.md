# Contributing to rompy-notebooks

Keep notebook examples focused and runnable where their external requirements permit. Avoid committing Jupyter checkpoints, caches, or generated run directories.

## Documentation validation

Install the documentation tools and run the combined quality gate before opening a pull request:

```bash
python -m pip install -r requirements-docs.txt
make docs-build
```

The documentation build renders stored notebook outputs without executing model code. Full SWAN, XBeach, and SCHISM execution requires additional model-specific runtimes and is handled separately from the documentation gate.
