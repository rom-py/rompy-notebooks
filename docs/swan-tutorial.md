# SWAN learning tutorial

These notebooks show how to set up and run [SWAN](https://swanmodel.sourceforge.io) with [rompy-swan](https://rom-py.github.io/rompy-swan/), which extends [rompy](https://rom-py.github.io/rompy/) with everything specific to SWAN.

The collection has two parts:

- **Tutorial:** an ordered path from zero to a nonstationary hindcast. Start here if you are new to rompy or rompy-swan.
- **Examples:** self-contained notebooks on specific features. Pick the one you need and adapt it to your data.

All notebooks model the coast off Perth, Western Australia, on 1 January 2023, with ETOPO bathymetry, ERA5 winds and WAVEWATCH III boundary spectra.

## Getting started

You need Python with `rompy`, `rompy-swan`, Jupyter, cartopy and wavespectra. See the [installation guide](installation_guide.md).

The example data is in [`notebooks/swan/data/`](https://github.com/rom-py/rompy-notebooks/tree/main/notebooks/swan/data), so the notebooks run from a clone of this repository without further setup. Each notebook writes its files to a local `_output/` folder, which is safe to delete.

To **run SWAN**, the notebooks use the public Docker image `ghcr.io/rom-py/swan`, built with NetCDF output, so you only need [Docker](https://docs.docker.com/get-docker/) installed and running. Cells that run SWAN are skipped if Docker is not available, and everything else still works. If you have your own SWAN installation, see [Running SWAN](notebooks/swan/examples/running_swan.ipynb).

!!! note
    The pages on this site show the outputs stored in the notebooks, including the results of the SWAN runs. The documentation build does not run the notebooks or SWAN.

## Tutorial

Work through these in order:

| # | Notebook | You will learn |
|---|---|---|
| 1 | [Your first SWAN model](notebooks/swan/tutorial/01_first_model.ipynb) | The whole workflow: grid, bathymetry, a wave boundary, physics, generate and run |
| 2 | [The computational grid and spectrum](notebooks/swan/tutorial/02_grid_and_spectrum.ipynb) | Placing the grid, coordinates, the spectral grid and direction conventions |
| 3 | [Input grids: bathymetry and wind](notebooks/swan/tutorial/03_input_grids.ipynb) | Bathymetry and wind from datasets, and SWAN's stationary and nonstationary modes |
| 4 | [Wave boundaries](notebooks/swan/tutorial/04_wave_boundaries.ipynb) | Parametric boundaries and spectra from a regional wave model |
| 5 | [Choosing model settings](notebooks/swan/tutorial/05_model_settings.ipynb) | Startup, physics and numerics, SWAN's defaults and rompy-swan's checks |
| 6 | [A nonstationary hindcast](notebooks/swan/tutorial/06_nonstationary_hindcast.ipynb) | A day of waves off Perth: time steps, output, checking the run and plotting results |
| 7 | [Configuration as YAML and the rompy CLI](notebooks/swan/tutorial/07_yaml_and_cli.ipynb) | The same model as a YAML file, generated and run from the command line |

## Examples

### Grids and inputs

| Notebook | Shows |
|---|---|
| [Grid types](notebooks/swan/examples/grid_types.ipynb) | Rotated Cartesian grids, curvilinear and unstructured grids, grid geometry |
| [Input grids](notebooks/swan/examples/input_grids.ipynb) | Data sources, currents, water levels and other fields, data selection, hand-written input grids |

### Wave boundaries

| Notebook | Shows |
|---|---|
| [Parametric boundaries](notebooks/swan/examples/boundaries_parametric.ipynb) | Spectral shapes, sides and segments, varying parameters and TPAR files |
| [Boundaries from spectra](notebooks/swan/examples/boundaries_from_spectra.ipynb) | `Boundnest1`, `BoundspecSide` and `BoundspecSegmentXY`, selection options and checks |
| [Nesting](notebooks/swan/examples/nesting.ipynb) | A coarse parent run providing the boundary of a finer child run |

### Model settings

| Notebook | Shows |
|---|---|
| [Physics](notebooks/swan/examples/physics.ipynb) | Source-term packages, breaking, friction, triads, set-up, obstacles, vegetation |
| [Numerics](notebooks/swan/examples/numerics.ipynb) | Propagation schemes, convergence, and choosing the time step |
| [Output](notebooks/swan/examples/output.ipynb) | Output locations, maps, tables and spectra, output times and quantities |

### Workflows

| Notebook | Shows |
|---|---|
| [Stationary and nonstationary computations](notebooks/swan/examples/stationary_and_nonstationary.ipynb) | SWAN's modes and computations, and how their results differ |
| [Hotstart and chained runs](notebooks/swan/examples/hotstart_and_chained_runs.ipynb) | Continuing a run from a saved wave field |
| [Running SWAN](notebooks/swan/examples/running_swan.ipynb) | Local and Docker backends, MPI, and checking a run |
| [Physics sensitivity](notebooks/swan/examples/physics_sensitivity.ipynb) | Generating and comparing variants with different source-term packages |

## Related material

- [rompy-swan documentation](https://rom-py.github.io/rompy-swan/)
- [SWAN user manual](https://swanmodel.sourceforge.io/online_doc/swanuse/swanuse.html)
- [SWAN notebooks by topic](generated/notebooks-by-topic.md)
- [Rompy data concepts](data-concepts.md)
- [Rompy run lifecycle](run-lifecycle.md)
