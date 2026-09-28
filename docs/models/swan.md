# SWAN

SWAN has a seven-lesson tutorial and twelve focused examples, all on one model of the coast off Perth. The tutorial goes from a first stationary run to a nonstationary hindcast and its YAML configuration; the examples cover one feature each.

## Recommended path

Start with the [SWAN learning tutorial](../swan-tutorial.md) and follow the lessons in order. The examples are listed on the same page, and the [SWAN catalogue](../generated/notebooks-by-model.md#swan) provides the complete reference view.

## Coverage

The collection covers regular, curvilinear and unstructured grids, input grids from data (bathymetry, wind, currents, water level), parametric and spectral boundaries, nesting, physics and numerics options, output locations and formats, stationary and nonstationary computations, hotstarts, YAML and the rompy CLI, running SWAN locally, with Docker and with MPI, and physics sensitivity. See the [coverage matrix](coverage.md).

!!! note
    The notebooks store their outputs, including the results of the SWAN runs made with the public Docker image `ghcr.io/rom-py/swan`. Documentation builds render these outputs without executing the notebooks or SWAN.
