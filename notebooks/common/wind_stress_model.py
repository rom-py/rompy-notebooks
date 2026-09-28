"""A toy 'model' used by the rompy hands-on notebook.

It stands in for a real model executable: it reads its settings from
params.txt in the current directory, reads the wind file named there,
computes the wind stress on the sea surface, and writes output.csv.
"""

from pathlib import Path

import numpy as np
import xarray as xr

params = {}
for line in Path("params.txt").read_text().splitlines():
    if "=" in line and not line.startswith("#"):
        key, value = (part.strip() for part in line.split("=", 1))
        params[key] = value

wind = xr.open_dataset(params["wind_file"])
speed = np.hypot(wind[params["u_var"]], wind[params["v_var"]])
stress = float(params["air_density"]) * float(params["drag_coefficient"]) * speed**2
spatial = [dim for dim in stress.dims if dim != params["time_var"]]
stress.mean(dim=spatial).to_dataframe(name="mean_stress").to_csv("output.csv")
print(f"Wind stress written for {stress.sizes[params['time_var']]} times")
