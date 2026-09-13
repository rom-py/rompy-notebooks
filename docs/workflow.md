# Build and execution

## Install documentation tools

From the repository root, install the documentation dependencies:

```bash
python -m pip install -r requirements-docs.txt
```

## Build or preview locally

The wrapper commands stage tracked notebooks, excluding checkpoints and generated run output:

```bash
make docs-build
make docs-serve
```

These standard commands are render-only: they stage notebooks and do not execute them. `docs-build` runs the notebook quality gate and then `mkdocs build --strict`. `docs-serve` stages the notebooks and starts a local preview server.

To preview the plots and outputs produced by eligible journey notebooks, use the explicit executed targets:

```bash
make docs-build-executed
make docs-serve-executed
```

These commands execute staged copies under `docs/notebooks/` before rendering. They require `nbclient`, the notebook Python dependencies, and any fixture data used by configuration-only lessons. Runtime-dependent lessons are skipped by default; no source notebooks or generated outputs are committed.

## Validation contract

The site uses `mkdocs-jupyter` with notebook execution disabled. The standard build renders stored outputs and therefore does not require model binaries, Docker, MPI, or remote data services. The separate quality gate checks notebook structure and stored error outputs, but it also does not execute model code.

The executed build is an opt-in integration workflow. It runs only `journey_*.ipynb` files with `render-only` or `configuration-only` metadata, using the repository root as the working directory. It may require local fixture data and package dependencies, and it can take substantially longer than the standard build.

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

XBeach examples cover procedural and declarative configuration, physics, sediment, output, boundary conditions, hotstarts, MPI, and data interfaces.
