# SCHISM

SCHISM has a seven-lesson tutorial and nine focused examples, all on one model of the coast off Perth. The tutorial goes from a first tidal run to a tide and wind hindcast and its YAML configuration; the examples cover one feature each.

## Recommended path

Start with the [SCHISM learning tutorial](../schism-tutorial.md) and follow the lessons in order. The examples are listed on the same page, and the [SCHISM catalogue](../generated/notebooks-by-model.md#schism) provides the complete reference view.

## Coverage

The collection covers the unstructured mesh and making one, 2D and 3D vertical grids, bottom friction, tidal and ocean-model open boundaries, atmospheric forcing, `param.nml` settings, a baroclinic 3D model started from an ocean model, waves with WWM, output and stations, hotstarts, YAML and the rompy CLI, running SCHISM locally, with Docker and with MPI, and friction sensitivity. See the [coverage matrix](coverage.md).

!!! note
    The notebooks store their outputs, including the results of the SCHISM runs made with the public Docker image `ghcr.io/rom-py/schism`. Documentation builds render these outputs without executing the notebooks or SCHISM.
