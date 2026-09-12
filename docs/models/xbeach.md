# XBeach notebooks

The XBeach collection now includes a compact guided journey plus focused capability tutorials. Start with the journey if you are new to Rompy and XBeach; use the grouped tutorials when you need deeper coverage of one input or component. The complete [notebook gallery](../gallery.md) remains the reference catalogue for lookup.

!!! note
    Documentation builds render notebooks without executing XBeach. Runtime-dependent lessons require an appropriate `rompy-xbeach` environment and XBeach installation. Configuration-only lessons validate Rompy objects or generated inputs but do not run the model.

## Prerequisites

- Basic Python and familiarity with nearshore modelling concepts.
- `rompy` and `rompy-xbeach` installed for the executable code cells.
- An XBeach binary is required only for the optional runtime step; MPI is additionally required only for parallel runs.
- The journey uses deterministic examples and does not require hidden downloads for documentation rendering.

## XBeach learning journey

| Step | Lesson | Focus | Execution |
| --- | --- | --- | --- |
| 1 | [XBeach and Rompy: orientation](../notebooks/xbeach/journey_01_rompy_orientation.ipynb) | Model-run boundary and vocabulary | Render-only |
| 2 | [Procedural workflow](../notebooks/xbeach/journey_02_xbeach_procedural.ipynb) | Time range and grid objects | Configuration-only |
| 3 | [Declarative YAML](../notebooks/xbeach/journey_03_xbeach_declarative.ipynb) | Reproducible serialised configuration | Render-only |
| 4 | [Grids and bathymetry](../notebooks/xbeach/journey_04_xbeach_grid_data.ipynb) | Grid and input-data concepts | Render-only |
| 5 | [Forcing and boundary data](../notebooks/xbeach/journey_05_xbeach_forcing.ipynb) | Waves, wind, tide, and boundaries | Render-only |
| 6 | [Physics and outputs](../notebooks/xbeach/journey_06_xbeach_components.ipynb) | Components, sediment, outputs, hotstarts | Configuration-only |
| 7 | [Execution and reproducibility](../notebooks/xbeach/journey_07_xbeach_execution.ipynb) | Runtime boundary, MPI, and repeatability | Configuration-only |

Each lesson has previous/next links. The journey introduces concepts; the focused tutorials below provide the detailed parameter coverage.

## Workflows

- [XBeach procedural workflow](../notebooks/xbeach/example-procedural.ipynb)
- [XBeach declarative workflow](../notebooks/xbeach/example-declarative.ipynb)

## Grids and input data

- [Grid data](../notebooks/xbeach/data-interface/tutorial-grid.ipynb)
- [Bathymetry data](../notebooks/xbeach/data-interface/tutorial-bathy.ipynb)
- [Forcing data](../notebooks/xbeach/data-interface/tutorial-forcing.ipynb)
- [Source data](../notebooks/xbeach/data-interface/tutorial-source.ipynb)
- [Time-series forcing](../notebooks/xbeach/data-interface/tutorial-timeseries-forcing.ipynb)
- [Wave boundary data](../notebooks/xbeach/data-interface/tutorial-wave-boundary.ipynb)

## Physics, components, and boundaries

- [Physics components](../notebooks/xbeach/components/tutorial_01_physics.ipynb)
- [Sediment components](../notebooks/xbeach/components/tutorial_02_sediment.ipynb)
- [Boundary condition components](../notebooks/xbeach/components/tutorial_04_boundary-conditions.ipynb)
- [Hotstart components](../notebooks/xbeach/components/tutorial_05_hotstart.ipynb)

## Outputs and diagnostics

- [Output components](../notebooks/xbeach/components/tutorial_03_output.ipynb)

## Execution and advanced workflows

- [MPI execution](../notebooks/xbeach/components/tutorial_06_mpi.ipynb)

The journey does not yet cover every scientific XBeach workflow or provide a full runtime integration suite. See the [model coverage matrix](coverage.md) for current XBeach gaps.

## Next model: SCHISM

The next model-specific expansion should grow SCHISM from its broad demonstration into focused tutorials for grid/workspace setup, atmospheric, tidal, and wave forcing, boundary conditions, namelist configuration, execution backends, and output verification. Those lessons must keep binary, MPI, Docker, and external-data requirements separate from render-only documentation.

The complete [notebook gallery](../gallery.md) remains available for lookup.
