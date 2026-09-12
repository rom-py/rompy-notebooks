# SWAN learning journey

This is the guided path through Rompy using a small SWAN example domain. Follow the lessons in order; use the [notebook gallery](gallery.md) when you want the complete reference collection.

!!! note
    The journey's required path prepares and inspects model configuration. The documentation site does not execute SWAN. Runtime-dependent execution is clearly marked as optional.

## Journey map

| Step | Notebook | Main idea | Builds on |
| --- | --- | --- | --- |
| 1 | [Rompy and SWAN: orientation](notebooks/swan/journey_01_rompy_orientation.ipynb) | Core Rompy objects and execution boundary | — |
| 2 | [Build a SWAN workspace procedurally](notebooks/swan/journey_02_swan_procedural.ipynb) | Grid, time range, and Python configuration | 1 |
| 3 | [Configure SWAN declaratively with YAML](notebooks/swan/journey_03_swan_declarative.ipynb) | Serialised configuration and reproducibility | 2 |
| 4 | [Prepare SWAN grids and input data](notebooks/swan/journey_04_swan_data.ipynb) | Bathymetry, wind, and wave boundaries | 3 |
| 5 | [Configure SWAN components and outputs](notebooks/swan/journey_05_swan_components.ipynb) | Physics, numerics, boundaries, and outputs | 4 |
| 6 | [Inspect and optionally execute a SWAN workspace](notebooks/swan/journey_06_swan_workspace.ipynb) | Generation versus actual model execution | 5 |
| 7 | [Compare SWAN configurations with sensitivity analysis](notebooks/swan/journey_07_swan_sensitivity.ipynb) | Parameter variation and reproducibility | 6 |

## Related reference material

The journey is intentionally shorter than the reference collection. Continue with:

- [SWAN procedural example](notebooks/swan/example_procedural.ipynb)
- [SWAN declarative example](notebooks/swan/example_declarative.ipynb)
- [SWAN boundary notebooks](gallery.md#swan)
- [SWAN output components](notebooks/swan/components/output.ipynb)
- [SWAN sensitivity example](notebooks/swan/example_sensitivity.ipynb)
- [General Rompy getting started guide](https://rom-py.github.io/rompy/getting_started/)
- [General Rompy core concepts](https://rom-py.github.io/rompy/core_concepts/)

## Example contract

The mandatory lessons use a compact Perth-area teaching domain:

- regular `SwanGrid` with 9 × 7 points;
- 0.25° grid spacing;
- a six-hour period beginning at `2023-01-01T00:00:00`;
- local input paths shown as explicit placeholders where real bathymetry, wind, or wave data are required.

This keeps the narrative coherent while avoiding hidden downloads and large committed datasets. A compatible `rompy-swan` installation is required to execute the Python cells; a SWAN binary is only required for the optional execution step.
