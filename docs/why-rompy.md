# What rompy does

Setting up an ocean or coastal model involves the same chores whatever the model:

- define where the model is (a grid) and when it runs (a period);
- turn bathymetry, wind, waves and water levels from datasets in many formats into the model's own input files;
- write the model settings in the model's own format;
- run the model somewhere, and repeat for the next event, site or variant.

Every model does these in its own way: SWAN reads a command file (`INPUT`), XBeach a flat `params.txt` file, SCHISM a set of Fortran namelists. [Rompy](https://rom-py.github.io/rompy/) gives the chores one structure in Python, and model plugins such as rompy-swan, rompy-xbeach and rompy-schism fill in what is specific to each model.

## Without and with rompy

| Task | Without rompy | With rompy |
|---|---|---|
| Describe the model | Hand-edited text files. Mistakes surface when the model starts, or not at all. | Python objects that check their values as you build them. Rompy writes the text files. |
| Prepare input data | One script per dataset to crop, interpolate and convert. | Data objects that pair a source with the grid and period. Rompy extracts only what the run needs. |
| Share and reproduce | Scripts, plus notes on how they were run. | The whole run as one Python object or YAML file, checked again when loaded. |
| Run the model | Shell scripts tied to one machine. | The same workspace, run locally, in Docker or with MPI by choosing a backend. |
| Try variants | Copy directories and edit them by hand. | Copy the configuration, change one setting, and generate a new workspace. |

## The big picture

A model run in rompy goes through three steps:

```text
  1. Describe                2. Generate                 3. Run (optional)
  ───────────                ───────────                 ─────────────────
  period       when
  grid         where         ModelRun writes the         a backend runs the
  data         forcing   ─▶  model's input files     ─▶  model on the workspace:
  components   settings      and forcing into a          local, Docker, MPI,
                             workspace                   a scheduler
  checked as you build them
```

The same steps look alike in every model. This is the XBeach version from the [first XBeach tutorial](notebooks/xbeach/tutorial/01_first_model.ipynb), shortened:

```python
from rompy.core.time import TimeRange
from rompy.model import ModelRun
from rompy.backends import DockerConfig
from rompy_xbeach.config import Config

period = TimeRange(start="2023-01-01T00:00", end="2023-01-01T00:30", interval="10m")
config = Config(grid=grid, bathy=bathy, input=forcing, physics=physics)  # the model plugin

run = ModelRun(run_id="first_model", period=period, output_dir="runs", config=config)
workspace = run()  # 2. generate: params.txt, bathymetry and boundary files

backend = DockerConfig(image="ghcr.io/rom-py/xbeach", executable="xbeach")
run.run(backend, workspace_dir=workspace)  # 3. run XBeach in Docker
```

Rompy provides `TimeRange`, `ModelRun`, the data sources and the backends. The plugin provides `Config` and everything inside it.

## Four ideas

These ideas run through every tutorial. Each has a page with more detail.

1. **The model is described by checked objects, in Python or YAML.** Each setting is a typed field with its allowed values, and plugins add the model's own rules, such as which wave boundary types a wave model accepts. The same description can be written in Python or as a YAML file. See [Configuration and validation](validation-concepts.md).
2. **Input data is a request, not a copy.** A data object names a source, the variables and how to read them. Rompy selects the part that covers the grid and period, and converts it to the model's format. See [Data](data-concepts.md).
3. **Describing, generating and running are separate steps.** You can check a configuration and inspect the generated files before a model binary is involved, and run the same workspace on different machines. See [Run lifecycle](run-lifecycle.md).
4. **A small core with plugins.** Models, data sources and run backends are plugins, so each can grow without changing the others. See [Plugins](plugin-architecture.md).

## The same ideas in each model

| | SWAN | XBeach | SCHISM |
|---|---|---|---|
| Plugin | rompy-swan | rompy-xbeach | rompy-schism |
| Configuration | `SwanConfig` | `Config` | `SCHISMConfig` |
| Grid | `SwanGrid`, regular | `RegularGrid`, regular and rotated | `SCHISMGrid`, unstructured mesh |
| Forcing data | `SwanDataGrid`, boundary classes such as `Boundnest1` | `XBeachBathy`, wave boundary classes, `WindGrid`, `TideConsGrid` | `SCHISMData`: atmospheric, ocean, tidal and wave forcing |
| Files rompy writes | the `INPUT` command file | `params.txt` | namelists such as `param.nml` |

## What stays with the modeller

Rompy checks that a configuration is complete and consistent, and does the repetitive work. It does not decide whether a dataset suits the question, whether the settings are physically sensible, or whether the model results are right. Look at the generated inputs and outputs, and validate the model against observations as you would without rompy.

## Where next

- [Install](installation_guide.md) the notebook environment and [get the notebooks running](usage_guide.md).
- Read the concept pages in order, starting with [Configuration and validation](validation-concepts.md), or go straight to a model.
- Follow a learning tutorial: [SWAN](swan-tutorial.md), [XBeach](xbeach-tutorial.md) or [SCHISM](schism-tutorial.md).
