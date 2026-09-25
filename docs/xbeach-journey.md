# XBeach learning journey

This is the guided path through Rompy using a compact XBeach workflow. Follow the lessons in order; use the [notebook gallery](gallery.md) for the complete reference collection.

!!! note
    The journey focuses on configuration and reproducible workspace preparation. The documentation site does not execute XBeach. Runtime-dependent requirements are identified in the final lesson.

## Journey map

| Step | Notebook | Main idea | Builds on |
| --- | --- | --- | --- |
| 1 | [XBeach and Rompy: orientation](notebooks/xbeach/journey_01_rompy_orientation.ipynb) | Rompy model runs and the XBeach workflow boundary | — |
| 2 | [Build an XBeach workspace procedurally](notebooks/xbeach/journey_02_xbeach_procedural.ipynb) | Time range, grid, and Python configuration | 1 |
| 3 | [Configure XBeach declaratively with YAML](notebooks/xbeach/journey_03_xbeach_declarative.ipynb) | Serialised configuration and reproducibility | 2 |
| 4 | [Prepare XBeach grids and bathymetry](notebooks/xbeach/journey_04_xbeach_grid_data.ipynb) | Spatial contracts and bathymetry preparation | 3 |
| 5 | [Prepare XBeach forcing and boundary data](notebooks/xbeach/journey_05_xbeach_forcing.ipynb) | Wave, wind, tide, and water-level requests | 4 |
| 6 | [Configure XBeach physics, sediment, outputs, and hotstarts](notebooks/xbeach/journey_06_xbeach_components.ipynb) | Composable model controls | 5 |
| 7 | [Inspect XBeach execution and reproducibility](notebooks/xbeach/journey_07_xbeach_execution.ipynb) | Generated workspaces, runtime requirements, and verification | 6 |

## Related reference material

The journey is complemented by focused tutorials and examples:

- [XBeach procedural example](notebooks/xbeach/example-procedural.ipynb)
- [XBeach declarative example](notebooks/xbeach/example-declarative.ipynb)
- [Physics, sediment, output, boundary, and hotstart tutorials](gallery.md#xbeach)
- [XBeach data-interface tutorials](gallery.md#xbeach)
- [General Rompy data concepts](data-concepts.md)
- [General Rompy run lifecycle](run-lifecycle.md)

## Example contract

The mandatory lessons use small teaching configurations and render-only examples. They keep source data, model configuration, workspace generation, and optional execution distinct. A compatible `rompy-xbeach` installation is required to execute the Python cells; the XBeach binary and MPI setup are required only for runtime execution.
