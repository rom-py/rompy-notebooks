# Example data

These are small sample datasets used by the SWAN tutorial and examples. They cover the coast off Perth, Western Australia, on 1 January 2023, so the notebooks run from a clone of this repository without further setup.

| File | Contents | Used by |
|---|---|---|
| `etopo15s_perth.nc` | Elevation (m, positive up) at 15 arc-seconds, 114–116°E, 34–31°S, from [ETOPO 2022](https://www.ncei.noaa.gov/products/etopo-global-relief-model) (NOAA, public domain), downloaded from the [CoastWatch ERDDAP server](https://coastwatch.pfeg.noaa.gov/erddap/griddap/ETOPO_2022_v1_15s.html) | All notebooks |
| `era5-20230101.nc` | ERA5 10 m wind components, hourly, 113–116°E, 35–29°S | Wind input |
| `ww3-spectra-20230101-short.nc` | WAVEWATCH III 2D spectra at 19 sites off Perth, 3-hourly | Spectral boundaries |
| `catalog.yaml` | Intake catalogue pointing at the bathymetry and wind files | Input grids example |

`era5-20230101.nc` and `ww3-spectra-20230101-short.nc` are copied from the [rompy-xbeach test data](https://github.com/rom-py/rompy-xbeach/tree/output/tests/data).

To use your own data, point the paths in a notebook to your files. [Input grids](../examples/input_grids.ipynb) explains which source reads which format.
