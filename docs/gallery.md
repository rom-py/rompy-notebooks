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

Start with the [SCHISM learning journey](models/schism.md) for the progressive path and real-data case study.

- [SCHISM demonstration](notebooks/schism/schism_demo.ipynb)
- [Complete regional case study](notebooks/schism/journey_06_schism_real_case.ipynb)

## XBeach

Start with the [XBeach learning journey](models/xbeach.md) for a recommended sequence, then use these focused notebooks as a reference catalogue.

- [Procedural example](notebooks/xbeach/example-procedural.ipynb)
- [Declarative example](notebooks/xbeach/example-declarative.ipynb)
- [Physics](notebooks/xbeach/components/tutorial_01_physics.ipynb)
- [Sediment](notebooks/xbeach/components/tutorial_02_sediment.ipynb)
- [Output](notebooks/xbeach/components/tutorial_03_output.ipynb)
- [Boundary conditions](notebooks/xbeach/components/tutorial_04_boundary-conditions.ipynb)
- [Hotstart](notebooks/xbeach/components/tutorial_05_hotstart.ipynb)
- [MPI](notebooks/xbeach/components/tutorial_06_mpi.ipynb)
- [Bathymetry data](notebooks/xbeach/data-interface/tutorial-bathy.ipynb)
- [Forcing data](notebooks/xbeach/data-interface/tutorial-forcing.ipynb)
- [Grid data](notebooks/xbeach/data-interface/tutorial-grid.ipynb)
- [Source data](notebooks/xbeach/data-interface/tutorial-source.ipynb)
- [Time-series forcing](notebooks/xbeach/data-interface/tutorial-timeseries-forcing.ipynb)
- [Wave boundary](notebooks/xbeach/data-interface/tutorial-wave-boundary.ipynb)

Notebook source files remain under [`notebooks/`](https://github.com/rom-py/rompy-notebooks/tree/main/notebooks) and are staged into the documentation tree during the build. See the [build and execution guide](workflow.md) for the distinction between rendering and actually executing a model.
