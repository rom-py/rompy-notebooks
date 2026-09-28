# Build and execution

## Install documentation tools

From the repository root, install the documentation dependencies:

```bash
python -m pip install -r requirements-docs.txt
```

## Example data and provenance

Example datasets are described in [`data/example-data.json`](https://github.com/rom-py/rompy-notebooks/blob/main/data/example-data.json). Check optional fixture availability with:

```bash
make example-data
```

Small model-specific datasets are committed next to the notebooks that use them (for example `notebooks/xbeach/data/`), so those notebooks run from a clone without an acquisition step. Larger shared fixtures are acquired explicitly and are never part of a render-only documentation build. For the optional SCHISM bundle, use `python scripts/example_data.py --acquire-schism`. Generated model inputs belong in temporary or ignored workspaces and are not scientific validation evidence.

## Build or preview locally

The wrapper commands stage tracked notebooks, excluding checkpoints and generated run output:

```bash
make docs-build
make docs-serve
```

These standard commands are render-only: they stage notebooks and do not execute them. `docs-build` runs the notebook quality gate and then `mkdocs build --strict`. `docs-serve` stages the notebooks and starts a local preview server.

To preview the plots and outputs produced by the figure-selected Tutorial notebooks, use the explicit figure targets:

```bash
make docs-build-figures
make docs-serve-figures
```

These commands execute only notebooks marked with `execution_group: figures` in staged copies under `docs/notebooks/` before rendering. They require `nbclient`, the model plugin and notebook dependencies, and any fixture data used by those lessons. Runtime-dependent lessons are skipped; no source notebooks or generated outputs are committed.

The broader `make docs-build-executed` target remains available for executing all eligible Tutorial notebooks locally.

## Validation tiers

The project separates documentation rendering from execution:

1. **Structural audit** (`make notebook-audit`) checks notebook JSON, metadata, links, and hygiene.
2. **Render-only build** (`make docs-build`) is the default CI gate and does not execute notebooks or model binaries.
3. **Selected execution** (`make execute-docs-selected`) runs notebooks explicitly marked eligible in staged copies and writes `.cache/selected-execution.json`.
4. **Runtime validation** is opt-in and environment-specific; it is never implied by stored outputs or a successful documentation build.

Selected execution is a configuration/data check, not scientific validation. Its report records this limitation explicitly.

Full notebook execution is a separate integration concern. Individual examples may require:

- rompy model plugins and their compatible versions;
- local SWAN, XBeach, or SCHISM executables;
- Docker or MPI;
- external data catalogs or package test-data directories.

## Model groups

### SWAN

SWAN examples cover procedural and declarative configuration, sensitivity analysis, boundary conditions, and output components.

### SCHISM

The SCHISM demonstration covers configuration and backend-oriented setup.

### XBeach

The XBeach tutorial and examples cover grids, data sources, bathymetry, forcing, physics, sediment, boundaries, output, hotstarts, YAML and the CLI, and running XBeach with Docker and MPI. Their outputs are committed, including the XBeach runs.
