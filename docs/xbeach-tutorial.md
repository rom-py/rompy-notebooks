# XBeach learning tutorial

These notebooks show how to set up and run [XBeach](https://xbeach.readthedocs.io) with [rompy-xbeach](https://rom-py.github.io/rompy-xbeach/), which extends [rompy](https://rom-py.github.io/rompy/) with everything specific to XBeach.

The collection has two parts:

- **Tutorial:** an ordered path from zero to a complete, running model. Start here if you are new to rompy or rompy-xbeach.
- **Examples:** self-contained notebooks on specific features. Pick the one you need and adapt it to your data.

## Getting started

You need Python with `rompy`, `rompy-xbeach`, Jupyter, cartopy and wavespectra. See the [installation guide](installation_guide.md).

The example data is in [`notebooks/xbeach/data/`](https://github.com/rom-py/rompy-notebooks/tree/main/notebooks/xbeach/data), so the notebooks run from a clone of this repository without further setup. Each notebook writes its files to a local `_output/` folder, which is safe to delete.

To **run XBeach**, the notebooks use the public Docker image `ghcr.io/rom-py/xbeach`, so you only need [Docker](https://docs.docker.com/get-docker/) installed and running. Cells that run XBeach are skipped if Docker is not available, and everything else still works. If you have your own XBeach installation, see [Running XBeach](notebooks/xbeach/examples/running_xbeach.ipynb).

!!! note
    The pages on this site show the outputs stored in the notebooks, including the results of the XBeach runs. The documentation build does not run the notebooks or XBeach.

## Tutorial

Work through these in order:

| # | Notebook | You will learn |
|---|---|---|
| 1 | [Your first XBeach model](notebooks/xbeach/tutorial/01_first_model.ipynb) | The whole workflow: grid, bathymetry, waves, physics, generate and run |
| 2 | [Defining the model grid](notebooks/xbeach/tutorial/02_model_grid.ipynb) | Placing and orienting an XBeach grid correctly |
| 3 | [Bathymetry from your data](notebooks/xbeach/tutorial/03_bathymetry.ipynb) | Reading, interpolating and extending bathymetry |
| 4 | [Adding forcing](notebooks/xbeach/tutorial/04_forcing.ipynb) | Wave, wind and water level forcing from datasets |
| 5 | [Choosing model settings](notebooks/xbeach/tutorial/05_model_settings.ipynb) | Physics, boundaries, sediment and output components |
| 6 | [A complete storm-impact setup](notebooks/xbeach/tutorial/06_complete_setup.ipynb) | A realistic model built from real forcing data |
| 7 | [Configuration as YAML and the rompy CLI](notebooks/xbeach/tutorial/07_yaml_and_cli.ipynb) | The same model as a YAML file, run from the command line |

## Examples

### Grid and bathymetry

| Notebook | Shows |
|---|---|
| [Grid plotting and export](notebooks/xbeach/examples/grid_plotting_and_export.ipynb) | Coastlines, projections, overlays, and saving grids to KML or GeoJSON |
| [Data sources](notebooks/xbeach/examples/data_sources.ipynb) | Every source type: GeoTIFF, NetCDF, XYZ, intake, spectra, tidal constituents, CSV |
| [Bathymetry options](notebooks/xbeach/examples/bathymetry_options.ipynb) | Depth convention, interpolation, and seaward and lateral extension |

### Wave boundaries

| Notebook | Shows |
|---|---|
| [Constant and bichromatic waves](notebooks/xbeach/examples/waves_params.ipynb) | Constant waves, bichromatic wave groups, no waves |
| [Wave boundaries from spectra](notebooks/xbeach/examples/waves_from_spectra.ipynb) | JONSWAP, JONSWAP table and SWAN boundaries from 2D spectra, and common settings |
| [Wave boundaries from parameters](notebooks/xbeach/examples/waves_from_parameters.ipynb) | JONSWAP boundaries from Hs, Tp and direction at stations, on grids or from a CSV |
| [Existing files and reuse](notebooks/xbeach/examples/waves_from_files_and_reuse.ipynb) | Boundary files made elsewhere, and reusing boundaries from a previous run |

### Wind and water levels

| Notebook | Shows |
|---|---|
| [Wind forcing](notebooks/xbeach/examples/wind.ipynb) | Gridded, station and point winds, and switching wind on |
| [Water level forcing](notebooks/xbeach/examples/water_levels.ipynb) | Tide from constituents, water level data, and surge plus tide |

### Model components

| Notebook | Shows |
|---|---|
| [Physics](notebooks/xbeach/examples/physics.ipynb) | Wave models, breakers, friction, viscosity, roller, vegetation, numerics |
| [Sediment and morphology](notebooks/xbeach/examples/sediment_and_morphology.ipynb) | Transport, morfac, avalanching, bed composition, hard layers, groundwater |
| [Flow and tide boundaries](notebooks/xbeach/examples/flow_and_tide_boundaries.ipynb) | Boundary types on each side of the grid, and water level boundaries |
| [Output](notebooks/xbeach/examples/output.ipynb) | Map, point and run-up output, timing and hotstart files |

### Workflows

| Notebook | Shows |
|---|---|
| [Data selection options](notebooks/xbeach/examples/data_selection.ipynb) | The rompy options shared by all forcing classes: coords, variables, filters, time cropping |
| [Hotstart and chained runs](notebooks/xbeach/examples/hotstart_and_chained_runs.ipynb) | Continuing a simulation from a saved model state |
| [Running XBeach](notebooks/xbeach/examples/running_xbeach.ipynb) | Local and Docker backends, MPI, and `rompy run` |
| [Parameter sweep](notebooks/xbeach/examples/parameter_sweep.ipynb) | Generating and comparing a set of model variants |

## Related material

- [rompy-xbeach documentation](https://rom-py.github.io/rompy-xbeach/)
- [XBeach notebooks by topic](generated/notebooks-by-topic.md)
- [Rompy data concepts](data-concepts.md)
- [Rompy run lifecycle](run-lifecycle.md)
