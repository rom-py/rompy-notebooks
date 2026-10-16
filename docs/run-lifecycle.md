# The Rompy run lifecycle

Rompy separates describing an experiment from preparing and running it. This separation is what lets the same configuration be inspected, generated locally, or handed to a different execution backend.

```text
configuration + sources + time/domain contract
                    |
                    v
              ModelRun.generate()
                    |
                    v
          model-native workspace
                    |
          optional run(backend=...)
                    |
                    v
       model outputs and diagnostics
```

## Four distinct stages

### 1. Describe

Create typed objects for the model configuration, grid, time range, data sources, boundaries, outputs, and runtime settings. At this point the description is a portable experiment specification; no model binary needs to have run.

### 2. Generate

`ModelRun.generate()` resolves the configured sources and writes the files expected by the target model. This is where filtering, interpolation, extraction, coordinate conversion, and model-specific formatting happen.

Generated files should be inspected. Their presence or structural correctness confirms that preparation worked, but not that the scientific setup is appropriate.

### 3. Execute

`ModelRun.run(backend=...)` adds an execution environment: a local process, MPI launcher, Docker container, scheduler, or another backend. Execution is optional and has prerequisites that are separate from configuration and generation.

### 4. Inspect and validate

Read generated inputs and model outputs, check dimensions and ranges, plot fields, and assess whether the experiment is scientifically suitable. Rompy can support these checks, but it cannot replace domain expertise or model-skill evaluation.

## Repeating a run: variants and experiments

Because a run is described by objects, a variant is a copy with one change: a different friction coefficient, wave boundary or period. Each variant generates its own workspace under its own run id, so the inputs can be compared before anything runs and the outputs afterwards. The same pattern covers sensitivity tests, calibration and ensembles.

Chained runs work the same way: a second run starts from the saved state of the first instead of from rest.

## Why the separation matters

- Documentation can demonstrate configuration and generation without requiring model binaries.
- The same run description can target different backends.
- Failures can be located: source access, input generation, runtime, or output interpretation.
- A declarative experiment can be reviewed before expensive execution.

## See it in the notebooks

- XBeach: [generate and run a first model](notebooks/xbeach/tutorial/01_first_model.ipynb), [check a generated workspace](notebooks/xbeach/tutorial/06_complete_setup.ipynb), [run with a local installation, Docker or MPI](notebooks/xbeach/examples/running_xbeach.ipynb), [variants in a parameter sweep](notebooks/xbeach/examples/parameter_sweep.ipynb) and [chained runs](notebooks/xbeach/examples/hotstart_and_chained_runs.ipynb).
- SWAN: [a nonstationary hindcast, checked and analysed](notebooks/swan/tutorial/06_nonstationary_hindcast.ipynb), [running with Docker and MPI](notebooks/swan/examples/running_swan.ipynb), [chained runs](notebooks/swan/examples/hotstart_and_chained_runs.ipynb) and [variants in a sensitivity study](notebooks/swan/examples/physics_sensitivity.ipynb).
- SCHISM: [a tide and wind hindcast, checked and analysed](notebooks/schism/tutorial/06_tide_and_wind_hindcast.ipynb), [running with Docker and MPI](notebooks/schism/examples/running_schism.ipynb), [chained runs](notebooks/schism/examples/hotstart_and_chained_runs.ipynb) and [variants in a sensitivity study](notebooks/schism/examples/friction_sensitivity.ipynb).
