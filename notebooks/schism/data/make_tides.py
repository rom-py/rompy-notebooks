"""Make the tidal constituents used by the notebooks (tides/).

TPXO9 v5a (Egbert and Erofeeva, https://www.tpxo.net) elevation and current
constituents around Perth, from Oceanum Datamesh, written as a pyTMD database in
the ATLAS-netcdf format that rompy-schism reads: tides/database.json and one file
per constituent in tides/tpxo9-perth/.

Usage: python make_tides.py tides 114.8 116.0 -33.0 -31.3 M2,S2,N2,K2,K1,O1,P1,Q1

Needs a Datamesh token (DATAMESH_TOKEN) and the oceanum package. make_tides.py is
not needed to run the notebooks: tides/ is committed next to it. TPXO is free for
research and non-commercial use; see https://www.tpxo.net/tpxo-products-and-registration.
"""

import json
import sys
from pathlib import Path

import numpy as np
import xarray as xr
from oceanum.datamesh import Connector

out = Path(sys.argv[1])
x0, x1, y0, y1 = map(float, sys.argv[2:6])
cons = [c.upper() for c in sys.argv[6].split(",")]
name = "tpxo9"

ds = Connector().load_datasource("tpxo9_v5a_cons")
ds = ds.sel(lon=slice(x0, x1), lat=slice(y0, y1), con=cons).load()
lon, lat = ds.lon.values, ds.lat.values
dep = ds.dep.transpose("lon", "lat").values  # ATLAS arrays are (nx, ny)
atlas = out / "tpxo9-perth"
atlas.mkdir(parents=True, exist_ok=True)


def coords(kind):
    return {
        f"lon_{kind}": (("nx",), lon, {"units": "degrees_east"}),
        f"lat_{kind}": (("ny",), lat, {"units": "degrees_north"}),
    }


grid = xr.Dataset(
    {
        **coords("z"),
        **coords("u"),
        **coords("v"),
        **{
            f"h{k}": (("nx", "ny"), np.nan_to_num(dep), {"units": "meters"})
            for k in "zuv"
        },
    },
    attrs={"title": "ATLAS bathymetry file", "type": "OTIS grid file"},
)
grid.to_netcdf(atlas / f"grid_{name}.nc")

files = {"h": [], "u": []}
for con in cons:
    c = con.lower()
    h = ds.h.sel(con=con).transpose("lon", "lat").values
    hm = np.nan_to_num(h)  # pyTMD reads ATLAS-netcdf elevations in metres
    xr.Dataset(
        {
            **coords("z"),
            "hRe": (("nx", "ny"), hm.real.astype("f4"), {"units": "meter"}),
            "hIm": (("nx", "ny"), hm.imag.astype("f4"), {"units": "meter"}),
            "con": (("nct",), np.array(list(f"{c:<4}"), dtype="S1")),
        },
        attrs={"title": "ATLAS tidal elevation file", "type": "OTIS elevation file"},
    ).to_netcdf(atlas / f"h_{c}_{name}.nc")
    tr = {}
    for comp in "uv":
        vel = ds[comp].sel(con=con).transpose("lon", "lat").values
        tr[comp] = np.nan_to_num(vel * dep)  # transport in m2/s, as pyTMD reads it
    xr.Dataset(
        {
            **coords("u"),
            **coords("v"),
            "uRe": (("nx", "ny"), tr["u"].real, {"units": "meter^2/sec"}),
            "uIm": (("nx", "ny"), tr["u"].imag, {"units": "meter^2/sec"}),
            "vRe": (("nx", "ny"), tr["v"].real, {"units": "meter^2/sec"}),
            "vIm": (("nx", "ny"), tr["v"].imag, {"units": "meter^2/sec"}),
            "con": (("nct",), np.array(list(f"{c:<4}"), dtype="S1")),
        },
        attrs={"title": "ATLAS tidal transport file", "type": "OTIS transport file"},
    ).to_netcdf(atlas / f"u_{c}_{name}.nc")
    files["h"].append(f"tpxo9-perth/h_{c}_{name}.nc")
    files["u"].append(f"tpxo9-perth/u_{c}_{name}.nc")

common = {
    "format": "ATLAS-netcdf",
    "grid_file": f"tpxo9-perth/grid_{name}.nc",
    "name": "TPXO9-perth",
    "projection": "EPSG:4326",
    "scale": 1,
    "reference": "https://www.tpxo.net/global",
    "version": "v5a",
}
database = {
    "elevation": {"TPXO9-perth": {**common, "model_file": files["h"], "type": "z"}},
    "current": {
        "TPXO9-perth": {
            **common,
            "model_file": {"u": files["u"], "v": files["u"]},
            "type": ["U", "V"],
        }
    },
}
(out / "database.json").write_text(json.dumps(database, indent=2))
