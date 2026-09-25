# SCHISM learning journey

This is the guided path through Rompy using a regional SCHISM case. Follow the lessons in order; use the [notebook gallery](gallery.md) for the complete reference collection.

!!! warning
    The journey generates and inspects configuration and model inputs but does not execute SCHISM in the documentation build. A SCHISM binary, MPI, external data, and scientific validation are runtime and project responsibilities.

## Journey map

| Step | Notebook | Main idea | Builds on |
| --- | --- | --- | --- |
| 1 | [SCHISM and Rompy: orientation](notebooks/schism/journey_01_rompy_orientation.ipynb) | Core configuration objects and the execution boundary | — |
| 2 | [Build a SCHISM workspace procedurally](notebooks/schism/journey_02_schism_procedural.ipynb) | Grid, configuration, and workspace generation | 1 |
| 3 | [SCHISM grids and input data](notebooks/schism/journey_03_schism_grid_data.ipynb) | Unstructured mesh, vertical grid, and fixture paths | 2 |
| 4 | [SCHISM external data and forcing](notebooks/schism/journey_04_schism_forcing.ipynb) | ERA5, HYCOM, tidal, and wave-source processing | 3 |
| 5 | [SCHISM boundary conditions and namelists](notebooks/schism/journey_05_schism_boundaries.ipynb) | Boundary semantics and model controls | 4 |
| 6 | [Complete regional SCHISM case study](notebooks/schism/journey_06_schism_real_case.ipynb) | Integrated regional workspace generation | 5 |
| 7 | [SCHISM execution and output verification](notebooks/schism/journey_07_schism_execution.ipynb) | Optional runtime, backends, and output checks | 6 |

## Related reference material

The journey is complemented by the retained broad example and the shared documentation:

- [SCHISM demonstration](notebooks/schism/schism_demo.ipynb)
- [SCHISM notebooks by model](generated/notebooks-by-model.md#schism)
- [Rompy data concepts](data-concepts.md)
- [Rompy run lifecycle](run-lifecycle.md)
- [Model notebook coverage](models/coverage.md)

## Example contract

The journey uses the shared `rom-py/rompy-test-data` fixture bundle for mesh and external-data demonstrations. The lessons make the source-to-configuration-to-generated-file hand-off explicit, but generated inputs are not evidence of a scientifically validated simulation. Execution additionally requires a compatible SCHISM installation, MPI launcher, and any selected backend or external data access.
