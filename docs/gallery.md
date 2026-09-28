# Notebook gallery

The gallery is grouped by the main areas covered by this repository. The complete metadata-driven catalogue is available in [notebooks by model](generated/notebooks-by-model.md) and [notebooks by topic](generated/notebooks-by-topic.md), as well as the site's **Notebooks** sidebar.

## Common and backends

- [Core concepts](notebooks/common/rompy_core_features.ipynb)
- [Backend examples](notebooks/backends/backend_examples.ipynb)

## SWAN

- [Procedural example](notebooks/swan/example_procedural.ipynb)
- [Declarative example](notebooks/swan/example_declarative.ipynb)
- [Sensitivity example](notebooks/swan/example_sensitivity.ipynb)
- [Nested boundary](notebooks/swan/boundary/boundnest1.ipynb)
- [Segment boundary](notebooks/swan/boundary/boundspec_segment.ipynb)
- [Side boundary](notebooks/swan/boundary/boundspec_side.ipynb)
- [Output components](notebooks/swan/components/output.ipynb)

## SCHISM

Start with the [SCHISM learning tutorial](models/schism.md) for the progressive path and real-data case study.

- [SCHISM demonstration](notebooks/schism/schism_demo.ipynb)
- [Complete regional case study](notebooks/schism/tutorial_06_schism_real_case.ipynb)

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
