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

XBeach examples cover procedural and declarative configuration, physics, sediment, output, boundary conditions, hotstarts, MPI, and data interfaces.
