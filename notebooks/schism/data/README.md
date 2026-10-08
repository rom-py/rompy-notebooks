# Example data

These are small sample datasets used by the SCHISM tutorial and examples. They cover the coast off Perth, Western Australia, from 31 December 2022 to 6 January 2023, so the notebooks run from a clone of this repository without further setup.

| File | Contents | Used by |
|---|---|---|
| `hgrid.gr3` | SCHISM mesh of the Perth coast: 6,790 nodes, 400 m at the coast to 2.5 km offshore, with Rottnest and Garden islands. One open boundary on the west, north and south sides. Made with `make_mesh.py` | All notebooks |
| `tides/` | [TPXO9](https://www.tpxo.net) v5a tidal constituents (M2, S2, N2, K2, K1, O1, P1, Q1; elevations and currents), 114.8–116°E, 33–31.3°S, as a pyTMD database (`database.json`). Made with `make_tides.py` from [Oceanum Datamesh](https://oceanum.io) | Tidal boundaries |
| `era5-perth-20230101-05.nc` | [ERA5](https://cds.climate.copernicus.eu) 10 m wind and mean sea-level pressure, hourly, 114–117°E, 34.5–30.5°S (Copernicus Climate Change Service), from Oceanum Datamesh | Atmospheric forcing |
| `glorys-perth-20230101-05.nc` | [GLORYS12V1](https://data.marine.copernicus.eu/product/GLOBAL_MULTIYEAR_PHY_001_030) daily ocean reanalysis: sea level, currents, temperature and salinity, 114.8–116°E, 32.8–31.4°S, 0–2000 m (Copernicus Marine Service) | Ocean boundaries, 3D |
| `etopo15s_perth.nc` | Elevation at 15 arc-seconds from [ETOPO 2022](https://www.ncei.noaa.gov/products/etopo-global-relief-model) (NOAA, public domain); the same file as the SWAN notebooks | Making a mesh |
| `ww3-spectra-20230101-short.nc` | WAVEWATCH III 2D spectra at 19 sites off Perth, 3-hourly, 1 January 2023; the same file as the SWAN notebooks | Waves (WWM) |

TPXO is free for research and non-commercial use; see [TPXO registration](https://www.tpxo.net/tpxo-products-and-registration). Copernicus data are free to use and redistribute with attribution.

`make_mesh.py` and `make_tides.py` show how the mesh and the tides were made. They are not needed to run the notebooks. [Making a mesh](../examples/making_a_mesh.ipynb) explains the mesh.
