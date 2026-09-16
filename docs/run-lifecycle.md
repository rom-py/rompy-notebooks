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

## Why the separation matters

- Documentation can demonstrate configuration and generation without requiring model binaries.
- The same run description can target different backends.
- Failures can be located: source access, input generation, runtime, or output interpretation.
- A declarative experiment can be reviewed before expensive execution.

Follow this lifecycle in the [SWAN journey](swan-journey.md), [XBeach journey](notebooks/xbeach/journey_01_rompy_orientation.ipynb), or [SCHISM journey](notebooks/schism/journey_01_rompy_orientation.ipynb).
