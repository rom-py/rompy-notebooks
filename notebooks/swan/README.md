# SWAN notebooks

These notebooks show how to set up and run [SWAN](https://swanmodel.sourceforge.io) with [rompy-swan](https://rom-py.github.io/rompy-swan/). rompy-swan extends [rompy](https://rom-py.github.io/rompy/) with everything specific to SWAN. New to rompy? [What rompy does](../../docs/why-rompy.md) explains the ideas shared by all models.

The collection has two parts:

- **Tutorial:** an ordered path from zero to a nonstationary hindcast. Start here if you are new to rompy or rompy-swan.
- **Examples:** self-contained notebooks on specific features. Pick the one you need and adapt it to your data.

All notebooks model the coast off Perth, Western Australia, on 1 January 2023.

## Getting started

You need Python with `rompy`, `rompy-swan`, Jupyter, cartopy and wavespectra. See the [installation guide](../../docs/installation_guide.md).

The example data is in [`data/`](data), so the notebooks run from a clone of this repository without further setup. Each notebook writes its files to a local `_output/` folder, which is safe to delete.

To **run SWAN**, the notebooks use the public Docker image `ghcr.io/rom-py/swan`, so you only need [Docker](https://docs.docker.com/get-docker/) installed and running. Cells that run SWAN are skipped if Docker is not available, and everything else still works. If you have your own SWAN installation, see [Running SWAN](examples/running_swan.ipynb).

## Tutorial

Work through these in order:

| # | Notebook | You will learn |
|---|---|---|
| 1 | [Your first SWAN model](tutorial/01_first_model.ipynb) | The whole workflow: grid, bathymetry, a wave boundary, physics, generate and run |
| 2 | [The computational grid and spectrum](tutorial/02_grid_and_spectrum.ipynb) | Placing the grid, coordinates, the spectral grid and direction conventions |
| 3 | [Input grids: bathymetry and wind](tutorial/03_input_grids.ipynb) | Bathymetry and wind from datasets, and SWAN's stationary and nonstationary modes |
| 4 | [Wave boundaries](tutorial/04_wave_boundaries.ipynb) | Parametric boundaries and spectra from a regional wave model |
| 5 | [Choosing model settings](tutorial/05_model_settings.ipynb) | Startup, physics and numerics, SWAN's defaults and rompy-swan's checks |
| 6 | [A nonstationary hindcast](tutorial/06_nonstationary_hindcast.ipynb) | A day of waves off Perth: time steps, output, checking the run and plotting results |
| 7 | [Configuration as YAML and the rompy CLI](tutorial/07_yaml_and_cli.ipynb) | The same model as a YAML file, generated and run from the command line |

## Examples

### Grids and inputs

| Notebook | Shows |
|---|---|
| [Grid types](examples/grid_types.ipynb) | Rotated Cartesian grids, curvilinear and unstructured grids, grid geometry |
| [Input grids](examples/input_grids.ipynb) | Data sources, currents, water levels and other fields, data selection, hand-written input grids |

### Wave boundaries

| Notebook | Shows |
|---|---|
| [Parametric boundaries](examples/boundaries_parametric.ipynb) | Spectral shapes, sides and segments, varying parameters and TPAR files |
| [Boundaries from spectra](examples/boundaries_from_spectra.ipynb) | `Boundnest1`, `BoundspecSide` and `BoundspecSegmentXY`, selection options and checks |
| [Nesting](examples/nesting.ipynb) | A coarse parent run providing the boundary of a finer child run |

### Model settings

| Notebook | Shows |
|---|---|
| [Physics](examples/physics.ipynb) | Source-term packages, breaking, friction, triads, set-up, obstacles, vegetation |
| [Numerics](examples/numerics.ipynb) | Propagation schemes, convergence, and choosing the time step |
| [Output](examples/output.ipynb) | Output locations, maps, tables and spectra, output times and quantities |

### Workflows

| Notebook | Shows |
|---|---|
| [Stationary and nonstationary computations](examples/stationary_and_nonstationary.ipynb) | SWAN's modes and computations, and how their results differ |
| [Hotstart and chained runs](examples/hotstart_and_chained_runs.ipynb) | Continuing a run from a saved wave field |
| [Running SWAN](examples/running_swan.ipynb) | Local and Docker backends, MPI, and checking a run |
| [Physics sensitivity](examples/physics_sensitivity.ipynb) | Generating and comparing variants with different source-term packages |

## Where did the previous notebooks go?

The earlier notebooks were reorganised into the tutorial and examples above. They remain in the repository history.

| Previous notebook | Now covered by |
|---|---|
| `tutorial_01_rompy_orientation` | [Tutorial 1](tutorial/01_first_model.ipynb) and [What rompy does](../../docs/why-rompy.md) |
| `tutorial_02_swan_procedural`, `example_procedural` | [Tutorial 1](tutorial/01_first_model.ipynb) and [Tutorial 6](tutorial/06_nonstationary_hindcast.ipynb) |
| `tutorial_03_swan_declarative`, `example_declarative` | [Tutorial 7](tutorial/07_yaml_and_cli.ipynb) |
| `tutorial_04_swan_data` | [Tutorial 3](tutorial/03_input_grids.ipynb) and [Input grids](examples/input_grids.ipynb) |
| `tutorial_05_swan_components` | [Tutorial 5](tutorial/05_model_settings.ipynb), [Physics](examples/physics.ipynb) and [Numerics](examples/numerics.ipynb) |
| `tutorial_06_swan_workspace` | [Tutorial 6](tutorial/06_nonstationary_hindcast.ipynb) and [Running SWAN](examples/running_swan.ipynb) |
| `tutorial_07_swan_sensitivity`, `example_sensitivity` | [Physics sensitivity](examples/physics_sensitivity.ipynb) |
| `boundary/boundnest1`, `boundary/boundspec_side`, `boundary/boundspec_segment` | [Boundaries from spectra](examples/boundaries_from_spectra.ipynb) |
| `components/output` | [Output](examples/output.ipynb) |
