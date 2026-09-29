# Notebook gallery

The gallery is grouped by the main areas covered by this repository. The complete metadata-driven catalogue is available in [notebooks by model](generated/notebooks-by-model.md) and [notebooks by topic](generated/notebooks-by-topic.md), as well as the site's **Notebooks** sidebar.

## Common and backends

- [Core concepts](notebooks/common/rompy_core_features.ipynb)
- [Backend examples](notebooks/backends/backend_examples.ipynb)

## SWAN

Start with the [SWAN learning tutorial](swan-tutorial.md), an ordered path from a first model to a nonstationary hindcast, then use the examples for specific features.

- [Grid types](notebooks/swan/examples/grid_types.ipynb)
- [Input grids](notebooks/swan/examples/input_grids.ipynb)
- [Parametric boundaries](notebooks/swan/examples/boundaries_parametric.ipynb)
- [Boundaries from spectra](notebooks/swan/examples/boundaries_from_spectra.ipynb)
- [Nesting](notebooks/swan/examples/nesting.ipynb)
- [Physics](notebooks/swan/examples/physics.ipynb)
- [Numerics](notebooks/swan/examples/numerics.ipynb)
- [Output](notebooks/swan/examples/output.ipynb)
- [Stationary and nonstationary computations](notebooks/swan/examples/stationary_and_nonstationary.ipynb)
- [Hotstart and chained runs](notebooks/swan/examples/hotstart_and_chained_runs.ipynb)
- [Running SWAN](notebooks/swan/examples/running_swan.ipynb)
- [Physics sensitivity](notebooks/swan/examples/physics_sensitivity.ipynb)

## SCHISM

Start with the [SCHISM learning tutorial](schism-tutorial.md), an ordered path from a first model to a tide and wind hindcast, then use the examples for specific features.

- [Making a mesh](notebooks/schism/examples/making_a_mesh.ipynb)
- [Tidal boundaries](notebooks/schism/examples/tidal_boundaries.ipynb)
- [Ocean boundaries](notebooks/schism/examples/ocean_boundaries.ipynb)
- [Baroclinic 3D model](notebooks/schism/examples/baroclinic_3d.ipynb)
- [Waves with WWM](notebooks/schism/examples/waves_wwm.ipynb)
- [Output](notebooks/schism/examples/output.ipynb)
- [Hotstart and chained runs](notebooks/schism/examples/hotstart_and_chained_runs.ipynb)
- [Running SCHISM](notebooks/schism/examples/running_schism.ipynb)
- [Friction sensitivity](notebooks/schism/examples/friction_sensitivity.ipynb)

## XBeach

Start with the [XBeach learning tutorial](xbeach-tutorial.md), an ordered path from a first model to a complete storm-impact setup, then use the examples for specific features.

- [Grid plotting and export](notebooks/xbeach/examples/grid_plotting_and_export.ipynb)
- [Data sources](notebooks/xbeach/examples/data_sources.ipynb)
- [Bathymetry options](notebooks/xbeach/examples/bathymetry_options.ipynb)
- [Constant and bichromatic waves](notebooks/xbeach/examples/waves_params.ipynb)
- [Wave boundaries from spectra](notebooks/xbeach/examples/waves_from_spectra.ipynb)
- [Wave boundaries from parameters](notebooks/xbeach/examples/waves_from_parameters.ipynb)
- [Wave boundary files and reuse](notebooks/xbeach/examples/waves_from_files_and_reuse.ipynb)
- [Wind forcing](notebooks/xbeach/examples/wind.ipynb)
- [Water level forcing](notebooks/xbeach/examples/water_levels.ipynb)
- [Physics](notebooks/xbeach/examples/physics.ipynb)
- [Sediment and morphology](notebooks/xbeach/examples/sediment_and_morphology.ipynb)
- [Flow and tide boundaries](notebooks/xbeach/examples/flow_and_tide_boundaries.ipynb)
- [Output](notebooks/xbeach/examples/output.ipynb)
- [Data selection options](notebooks/xbeach/examples/data_selection.ipynb)
- [Hotstart and chained runs](notebooks/xbeach/examples/hotstart_and_chained_runs.ipynb)
- [Running XBeach](notebooks/xbeach/examples/running_xbeach.ipynb)
- [Parameter sweep](notebooks/xbeach/examples/parameter_sweep.ipynb)

Notebook source files remain under [`notebooks/`](https://github.com/rom-py/rompy-notebooks/tree/main/notebooks) and are staged into the documentation tree during the build. See the [build and execution guide](workflow.md) for the distinction between rendering and actually executing a model.
