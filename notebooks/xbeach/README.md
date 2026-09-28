# XBeach notebooks

These notebooks show how to set up and run [XBeach](https://xbeach.readthedocs.io) with [rompy-xbeach](https://rom-py.github.io/rompy-xbeach/). rompy-xbeach extends [rompy](https://rom-py.github.io/rompy/) with everything specific to XBeach.

The collection has two parts:

- **Tutorial:** an ordered path from zero to a complete, running model. Start here if you are new to rompy or rompy-xbeach.
- **Examples:** self-contained notebooks on specific features. Pick the one you need and adapt it to your data.

## Getting started

You need Python with `rompy`, `rompy-xbeach`, Jupyter, cartopy and wavespectra. See the [installation guide](../../docs/installation_guide.md).

The example data is in [`data/`](data), so the notebooks run from a clone of this repository without further setup. Each notebook writes its files to a local `_output/` folder, which is safe to delete.

To **run XBeach**, the notebooks use the public Docker image `ghcr.io/rom-py/xbeach`, so you only need [Docker](https://docs.docker.com/get-docker/) installed and running. Cells that run XBeach are skipped if Docker is not available, and everything else still works. If you have your own XBeach installation, see [Running XBeach](examples/running_xbeach.ipynb).

## Tutorial

Work through these in order:

| # | Notebook | You will learn |
|---|---|---|
| 1 | [Your first XBeach model](tutorial/01_first_model.ipynb) | The whole workflow: grid, bathymetry, waves, physics, generate and run |
| 2 | [Defining the model grid](tutorial/02_model_grid.ipynb) | Placing and orienting an XBeach grid correctly |
| 3 | [Bathymetry from your data](tutorial/03_bathymetry.ipynb) | Reading, interpolating and extending bathymetry |
| 4 | [Adding forcing](tutorial/04_forcing.ipynb) | Wave, wind and water level forcing from datasets |
| 5 | [Choosing model settings](tutorial/05_model_settings.ipynb) | Physics, boundaries, sediment and output components |
| 6 | [A complete storm-impact setup](tutorial/06_complete_setup.ipynb) | A realistic model built from real forcing data |
| 7 | [Configuration as YAML and the rompy CLI](tutorial/07_yaml_and_cli.ipynb) | The same model as a YAML file, run from the command line |

## Examples

### Grid and bathymetry

| Notebook | Shows |
|---|---|
| [Grid plotting and export](examples/grid_plotting_and_export.ipynb) | Coastlines, projections, overlays, and saving grids to KML or GeoJSON |
| [Data sources](examples/data_sources.ipynb) | Every source type: GeoTIFF, NetCDF, XYZ, intake, spectra, tidal constituents, CSV |
| [Bathymetry options](examples/bathymetry_options.ipynb) | Depth convention, interpolation, and seaward and lateral extension |

### Wave boundaries

| Notebook | Shows |
|---|---|
| [Parametric wave boundaries](examples/waves_parametric.ipynb) | Constant waves, bichromatic wave groups, no waves |
| [Wave boundaries from spectra](examples/waves_from_spectra.ipynb) | JONSWAP, JONSWAP table and SWAN boundaries from 2D spectra, and common settings |
| [Wave boundaries from parameters](examples/waves_from_parameters.ipynb) | JONSWAP boundaries from Hs, Tp and direction at stations, on grids or from a CSV |
| [Existing files and reuse](examples/waves_from_files_and_reuse.ipynb) | Boundary files made elsewhere, and reusing boundaries from a previous run |

### Wind and water levels

| Notebook | Shows |
|---|---|
| [Wind forcing](examples/wind.ipynb) | Gridded, station and point winds, and switching wind on |
| [Water level forcing](examples/water_levels.ipynb) | Tide from constituents, water level data, and surge plus tide |

### Model components

| Notebook | Shows |
|---|---|
| [Physics](examples/physics.ipynb) | Wave models, breakers, friction, viscosity, roller, vegetation, numerics |
| [Sediment and morphology](examples/sediment_and_morphology.ipynb) | Transport, morfac, avalanching, bed composition, hard layers, groundwater |
| [Flow and tide boundaries](examples/flow_and_tide_boundaries.ipynb) | Boundary types on each side of the grid, and water level boundaries |
| [Output](examples/output.ipynb) | Map, point and run-up output, timing and hotstart files |

### Workflows

| Notebook | Shows |
|---|---|
| [Data selection options](examples/data_selection.ipynb) | The rompy options shared by all forcing classes: coords, variables, filters, time cropping |
| [Hotstart and chained runs](examples/hotstart_and_chained_runs.ipynb) | Continuing a simulation from a saved model state |
| [Running XBeach](examples/running_xbeach.ipynb) | Local and Docker backends, MPI, and `rompy run` |
| [Parameter sweep](examples/parameter_sweep.ipynb) | Generating and comparing a set of model variants |

## Where did the previous notebooks go?

The earlier notebooks were reorganised into the tutorial and examples above. They remain in the repository history.

| Previous notebook | Now covered by |
|---|---|
| `example-procedural` | [Tutorial 1](tutorial/01_first_model.ipynb) and [Tutorial 6](tutorial/06_complete_setup.ipynb) |
| `example-declarative` | [Tutorial 7](tutorial/07_yaml_and_cli.ipynb) |
| `components/tutorial_01_physics` | [Tutorial 5](tutorial/05_model_settings.ipynb) and [Physics](examples/physics.ipynb) |
| `components/tutorial_02_sediment` | [Tutorial 5](tutorial/05_model_settings.ipynb) and [Sediment and morphology](examples/sediment_and_morphology.ipynb) |
| `components/tutorial_03_output` | [Output](examples/output.ipynb) |
| `components/tutorial_04_boundary-conditions` | [Flow and tide boundaries](examples/flow_and_tide_boundaries.ipynb) |
| `components/tutorial_05_hotstart` | [Hotstart and chained runs](examples/hotstart_and_chained_runs.ipynb) |
| `components/tutorial_06_mpi` | [Running XBeach](examples/running_xbeach.ipynb) |
| `data-interface/tutorial-grid` | [Tutorial 2](tutorial/02_model_grid.ipynb) and [Grid plotting and export](examples/grid_plotting_and_export.ipynb) |
| `data-interface/tutorial-source` | [Tutorial 3](tutorial/03_bathymetry.ipynb) and [Data sources](examples/data_sources.ipynb) |
| `data-interface/tutorial-bathy` | [Tutorial 3](tutorial/03_bathymetry.ipynb) and [Bathymetry options](examples/bathymetry_options.ipynb) |
| `data-interface/tutorial-forcing` | [Tutorial 4](tutorial/04_forcing.ipynb), [Wind](examples/wind.ipynb) and [Water levels](examples/water_levels.ipynb) |
| `data-interface/tutorial-timeseries-forcing` | [Wind](examples/wind.ipynb), [Water levels](examples/water_levels.ipynb) and [Waves from parameters](examples/waves_from_parameters.ipynb) |
| `data-interface/tutorial-wave-boundary` | The four wave boundary examples |
