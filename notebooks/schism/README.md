# SCHISM notebooks

These notebooks show how to set up and run [SCHISM](https://schism-dev.github.io/schism/master/) with [rompy-schism](https://rom-py.github.io/rompy-schism/). rompy-schism extends [rompy](https://rom-py.github.io/rompy/) with everything specific to SCHISM. New to rompy? [What rompy does](../../docs/why-rompy.md) explains the ideas shared by all models.

The collection has two parts:

- **Tutorial:** an ordered path from zero to a tide and wind hindcast. Start here if you are new to rompy or rompy-schism.
- **Examples:** self-contained notebooks on specific features. Pick the one you need and adapt it to your data.

All notebooks model the coast off Perth, Western Australia, in early January 2023.

## Getting started

You need Python with `rompy`, `rompy-schism`, Jupyter and pyTMD. See the [installation guide](../../docs/installation_guide.md).

The example data is in [`data/`](data), so the notebooks run from a clone of this repository without further setup. Each notebook writes its files to a local `_output/` folder, which is safe to delete.

To **run SCHISM**, the notebooks use the public Docker image `ghcr.io/rom-py/schism`, so you only need [Docker](https://docs.docker.com/get-docker/) installed and running. Cells that run SCHISM are skipped if Docker is not available, and everything else still works. If you have your own SCHISM installation, see [Running SCHISM](examples/running_schism.ipynb).

## Tutorial

Work through these in order:

| # | Notebook | You will learn |
|---|---|---|
| 1 | [Your first SCHISM model](tutorial/01_first_model.ipynb) | The whole workflow: mesh, tides at the open boundary, settings, generate and run |
| 2 | [The mesh and the vertical grid](tutorial/02_mesh_and_vertical_grid.ipynb) | The unstructured mesh and its boundaries, bottom friction, 2D and 3D vertical grids |
| 3 | [Tides and open boundaries](tutorial/03_tides_and_open_boundaries.ipynb) | Tidal constituents from a tide model, boundary types and `bctides.in` |
| 4 | [Atmospheric forcing](tutorial/04_atmospheric_forcing.ipynb) | Wind and air pressure from a reanalysis as sflux files |
| 5 | [Choosing model settings](tutorial/05_model_settings.ipynb) | The `param.nml` namelist, SCHISM's defaults and rompy-schism's checks |
| 6 | [A tide and wind hindcast](tutorial/06_tide_and_wind_hindcast.ipynb) | Four days off Perth: forcing, output, checking the run and plotting results |
| 7 | [Configuration as YAML and the rompy CLI](tutorial/07_yaml_and_cli.ipynb) | The same model as a YAML file, generated and run from the command line |

## Examples

### Mesh

| Notebook | Shows |
|---|---|
| [Making a mesh](examples/making_a_mesh.ipynb) | From bathymetry to `hgrid.gr3` with gmsh, and checking a mesh |

### Open boundaries

| Notebook | Shows |
|---|---|
| [Tidal boundaries](examples/tidal_boundaries.ipynb) | Constituents, nodal corrections, the tidal potential, extrapolation and a mean level |
| [Ocean boundaries](examples/ocean_boundaries.ipynb) | Water levels from an ocean model, on their own or added to the tide |
| [Baroclinic 3D model](examples/baroclinic_3d.ipynb) | Temperature, salinity and currents from an ocean model at the boundary and at the start |
| [Waves with WWM](examples/waves_wwm.ipynb) | Wave spectra at the boundary and SCHISM coupled with the WWM wave model |

### Workflows

| Notebook | Shows |
|---|---|
| [Output](examples/output.ipynb) | Choosing output variables, scribes, reading 2D and 3D output, stations |
| [Hotstart and chained runs](examples/hotstart_and_chained_runs.ipynb) | Continuing a run from its saved state |
| [Running SCHISM](examples/running_schism.ipynb) | Local and Docker backends, MPI and scribes, and checking a run |
| [Friction sensitivity](examples/friction_sensitivity.ipynb) | Generating and comparing variants with different bottom friction |

## Where did the previous notebooks go?

The earlier notebooks were reorganised into the tutorial and examples above. They remain in the repository history.

| Previous notebook | Now covered by |
|---|---|
| `tutorial_01_rompy_orientation` | [Tutorial 1](tutorial/01_first_model.ipynb) and [What rompy does](../../docs/why-rompy.md) |
| `tutorial_02_schism_procedural`, `schism_demo` | [Tutorial 1](tutorial/01_first_model.ipynb) and [Tutorial 6](tutorial/06_tide_and_wind_hindcast.ipynb) |
| `tutorial_03_schism_grid_data` | [Tutorial 2](tutorial/02_mesh_and_vertical_grid.ipynb) and [Making a mesh](examples/making_a_mesh.ipynb) |
| `tutorial_04_schism_forcing` | [Tutorial 3](tutorial/03_tides_and_open_boundaries.ipynb), [Tutorial 4](tutorial/04_atmospheric_forcing.ipynb), [Ocean boundaries](examples/ocean_boundaries.ipynb) and [Waves with WWM](examples/waves_wwm.ipynb) |
| `tutorial_05_schism_boundaries` | [Tutorial 3](tutorial/03_tides_and_open_boundaries.ipynb), [Tutorial 5](tutorial/05_model_settings.ipynb) and [Tidal boundaries](examples/tidal_boundaries.ipynb) |
| `tutorial_06_schism_real_case` | [Tutorial 6](tutorial/06_tide_and_wind_hindcast.ipynb) and [Baroclinic 3D model](examples/baroclinic_3d.ipynb) |
| `tutorial_07_schism_execution` | [Running SCHISM](examples/running_schism.ipynb) and [Output](examples/output.ipynb) |
