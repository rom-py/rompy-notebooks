# SCHISM learning tutorial

These notebooks show how to set up and run [SCHISM](https://schism-dev.github.io/schism/master/) with [rompy-schism](https://rom-py.github.io/rompy-schism/), which extends [rompy](https://rom-py.github.io/rompy/) with everything specific to SCHISM.

The collection has two parts:

- **Tutorial:** an ordered path from zero to a tide and wind hindcast. Start here if you are new to rompy or rompy-schism.
- **Examples:** self-contained notebooks on specific features. Pick the one you need and adapt it to your data.

All notebooks model the coast off Perth, Western Australia, in early January 2023, on an unstructured mesh made from ETOPO bathymetry, with TPXO9 tides, ERA5 wind and pressure, the GLORYS12 ocean reanalysis and WAVEWATCH III spectra.

## Getting started

You need Python with `rompy`, `rompy-schism`, Jupyter and pyTMD. See the [installation guide](installation_guide.md).

The example data is in [`notebooks/schism/data/`](https://github.com/rom-py/rompy-notebooks/tree/main/notebooks/schism/data), so the notebooks run from a clone of this repository without further setup. Each notebook writes its files to a local `_output/` folder, which is safe to delete.

To **run SCHISM**, the notebooks use the public Docker image `ghcr.io/rom-py/schism`, built with MPI, NetCDF and the WWM wave model, so you only need [Docker](https://docs.docker.com/get-docker/) installed and running. Cells that run SCHISM are skipped if Docker is not available, and everything else still works. If you have your own SCHISM installation, see [Running SCHISM](notebooks/schism/examples/running_schism.ipynb).

!!! note
    The pages on this site show the outputs stored in the notebooks, including the results of the SCHISM runs. The documentation build does not run the notebooks or SCHISM.

## Tutorial

Work through these in order:

| # | Notebook | You will learn |
|---|---|---|
| 1 | [Your first SCHISM model](notebooks/schism/tutorial/01_first_model.ipynb) | The whole workflow: mesh, tides at the open boundary, settings, generate and run |
| 2 | [The mesh and the vertical grid](notebooks/schism/tutorial/02_mesh_and_vertical_grid.ipynb) | The unstructured mesh and its boundaries, bottom friction, 2D and 3D vertical grids |
| 3 | [Tides and open boundaries](notebooks/schism/tutorial/03_tides_and_open_boundaries.ipynb) | Tidal constituents from a tide model, boundary types and `bctides.in` |
| 4 | [Atmospheric forcing](notebooks/schism/tutorial/04_atmospheric_forcing.ipynb) | Wind and air pressure from a reanalysis as sflux files |
| 5 | [Choosing model settings](notebooks/schism/tutorial/05_model_settings.ipynb) | The `param.nml` namelist, SCHISM's defaults and rompy-schism's checks |
| 6 | [A tide and wind hindcast](notebooks/schism/tutorial/06_tide_and_wind_hindcast.ipynb) | Four days off Perth: forcing, output, checking the run and plotting results |
| 7 | [Configuration as YAML and the rompy CLI](notebooks/schism/tutorial/07_yaml_and_cli.ipynb) | The same model as a YAML file, generated and run from the command line |

## Examples

### Mesh

| Notebook | Shows |
|---|---|
| [Making a mesh](notebooks/schism/examples/making_a_mesh.ipynb) | From bathymetry to `hgrid.gr3` with gmsh, and checking a mesh |

### Open boundaries

| Notebook | Shows |
|---|---|
| [Tidal boundaries](notebooks/schism/examples/tidal_boundaries.ipynb) | Constituents, nodal corrections, the tidal potential, extrapolation and a mean level |
| [Ocean boundaries](notebooks/schism/examples/ocean_boundaries.ipynb) | Water levels from an ocean model, on their own or added to the tide |
| [Baroclinic 3D model](notebooks/schism/examples/baroclinic_3d.ipynb) | Temperature, salinity and currents from an ocean model at the boundary and at the start |
| [Waves with WWM](notebooks/schism/examples/waves_wwm.ipynb) | Wave spectra at the boundary and SCHISM coupled with the WWM wave model |

### Workflows

| Notebook | Shows |
|---|---|
| [Output](notebooks/schism/examples/output.ipynb) | Choosing output variables, scribes, reading 2D and 3D output, stations |
| [Hotstart and chained runs](notebooks/schism/examples/hotstart_and_chained_runs.ipynb) | Continuing a run from its saved state |
| [Running SCHISM](notebooks/schism/examples/running_schism.ipynb) | Local and Docker backends, MPI and scribes, and checking a run |
| [Friction sensitivity](notebooks/schism/examples/friction_sensitivity.ipynb) | Generating and comparing variants with different bottom friction |

## Related material

- [rompy-schism documentation](https://rom-py.github.io/rompy-schism/)
- [SCHISM manual](https://schism-dev.github.io/schism/master/)
- [SCHISM notebooks by topic](generated/notebooks-by-topic.md)
- [Rompy data concepts](data-concepts.md)
- [Rompy run lifecycle](run-lifecycle.md)
