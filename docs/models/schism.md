# SCHISM notebooks

SCHISM has a progressive learning journey, focused tutorials, and a retained broad procedural reference example. The journey uses the shared `rom-py/rompy-test-data` fixture bundle for a complete Australian regional case with real mesh, vertical-grid, ERA5, HYCOM, and tidal inputs.

!!! warning
    Documentation builds render SCHISM notebooks without executing them. The real-data lessons acquire fixtures only when explicitly run. Actual SCHISM execution additionally requires a SCHISM binary and MPI; Docker is optional.

## Prerequisites

- Python with `rompy` and `rompy-schism` installed.
- The shared SCHISM fixture bundle. Run a lesson from the repository; it uses `scripts/schism_case_data.py` and downloads the sibling-project fixture release only when the data is absent.
- A SCHISM executable and MPI launcher are required only for the optional runtime step.

## Learning journey

Follow the lessons in order:

1. [SCHISM and Rompy: orientation](../notebooks/schism/journey_01_rompy_orientation.ipynb)
2. [Build a SCHISM workspace procedurally](../notebooks/schism/journey_02_schism_procedural.ipynb)
3. [SCHISM grids and input data](../notebooks/schism/journey_03_schism_grid_data.ipynb)
4. [Real atmospheric and ocean forcing](../notebooks/schism/journey_04_schism_forcing.ipynb)
5. [SCHISM boundaries and namelists](../notebooks/schism/journey_05_schism_boundaries.ipynb)
6. [Complete regional SCHISM case study](../notebooks/schism/journey_06_schism_real_case.ipynb)
7. [SCHISM execution and output verification](../notebooks/schism/journey_07_schism_execution.ipynb)

## Reference

- [Broad SCHISM procedural demonstration](../notebooks/schism/schism_demo.ipynb)

The reference demonstrates a larger end-to-end configuration. The focused journey separates its concepts so that fixture preparation, workspace generation, and optional execution are explicit.

## Coverage status

| Section | Status | Current content |
| --- | --- | --- |
| Getting started | Established | Orientation lesson |
| Procedural workflow | Established | Procedural workspace lesson |
| Declarative workflow | Partial | Configuration concepts; dedicated YAML lesson remains follow-up |
| Grids and input data | Established | Real mesh, vertical grid, and fixture resolver |
| Atmospheric forcing | Established | Real ERA5 forcing |
| Ocean and tidal boundaries | Established | Real HYCOM and tidal fixture configuration |
| Physics/components | Partial | Covered in the reference example |
| Outputs and diagnostics | Partial | Output verification contract; runtime output requires SCHISM |
| Execution and backends | Partial | MPI/Docker prerequisites and optional runtime workflow |
| Advanced workflows | Not yet covered | — |

See the [model coverage matrix](coverage.md) for cross-model status. Runtime validation remains environment-dependent because this repository does not include a SCHISM binary.
