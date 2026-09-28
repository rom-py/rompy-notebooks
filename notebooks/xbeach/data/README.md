# Example data

These are small sample datasets used by the XBeach tutorial and examples. They cover a beach south of Perth, Western Australia, on 1–2 January 2023. They are copied from the [rompy-xbeach test data](https://github.com/rom-py/rompy-xbeach/tree/output/tests/data), so the notebooks run from a clone of this repository without further setup.

| File | Contents | Used by |
|---|---|---|
| `bathy.tif` | Elevation (m, positive up), GeoTIFF, WGS84 | Most notebooks |
| `bathy.nc` | The same elevation as NetCDF | Data sources |
| `bathy_xyz.zip` | Elevation as a zipped x, y, z point cloud | Data sources |
| `catalog.yaml` | Intake catalogue pointing at the bathymetry files | Data sources |
| `ww3-spectra-20230101-short.nc` | WAVEWATCH III 2D spectra at 19 sites, 3-hourly | Waves, complete setup, runs |
| `smc-params-20230101.nc` | WAVEWATCH III parameters and winds at 91 sites, hourly | Wind, waves from parameters |
| `gridded_wave_parameters.nc` | Gridded wave parameters, hourly | Waves from parameters |
| `wave-params-20230101.csv` | Wave parameters at one location | Waves from parameters |
| `era5-20230101.nc` | ERA5 10 m winds | Forcing, wind |
| `wind.csv` | Wind speed, direction and components at one location | Wind, data sources |
| `swaus_tide_cons/` | OTIS tidal constituents for south-west Australia | Forcing, water levels |
| `tide_cons_station.csv` | Tidal constituents at one site | Water levels |
| `ssh_gridded.nc`, `ssh_stations.nc`, `ssh.csv` | Sea-surface height on a grid, at stations and at one location | Water levels, data selection |

To use your own data, point the paths in a notebook to your files. The tutorial explains which source class reads which format.
