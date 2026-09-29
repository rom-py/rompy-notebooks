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

Small model-specific datasets are committed next to the notebooks that use them (for example `notebooks/xbeach/data/`, `notebooks/swan/data/` and `notebooks/schism/data/`), so those notebooks run from a clone without an acquisition step. Larger shared fixtures are acquired explicitly and are never part of a render-only documentation build. Generated model inputs belong in temporary or ignored workspaces and are not scientific validation evidence.

## Build or preview locally

The wrapper commands stage tracked notebooks, excluding checkpoints and generated run output:

```bash
make docs-build
make docs-serve
```

These standard commands are render-only: they stage notebooks and do not execute them. `docs-build` runs the notebook quality gate and then `mkdocs build --strict`. `docs-serve` stages the notebooks and starts a local preview server.

The notebooks are committed with their outputs, including the model runs, so the rendered pages show them without executing anything. `make docs-build-executed` executes the eligible Tutorial notebooks in staged copies before rendering, for local checks.

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

The SWAN tutorial and examples cover grids, input grids, parametric and spectral boundaries, nesting, physics, numerics, output, stationary and nonstationary computations, hotstarts, YAML and the CLI, running SWAN with Docker and MPI, and physics sensitivity. Their outputs are committed, including the SWAN runs.

### SCHISM

The SCHISM tutorial and examples cover the mesh and vertical grid, making a mesh, tides and ocean-model boundaries, atmospheric forcing, model settings, a baroclinic 3D model, waves with WWM, output, hotstarts, YAML and the CLI, running SCHISM with Docker and MPI, and friction sensitivity. Their outputs are committed, including the SCHISM runs.

### XBeach

The XBeach tutorial and examples cover grids, data sources, bathymetry, forcing, physics, sediment, boundaries, output, hotstarts, YAML and the CLI, and running XBeach with Docker and MPI. Their outputs are committed, including the XBeach runs.
