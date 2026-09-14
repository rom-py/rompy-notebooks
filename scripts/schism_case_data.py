"""Explicit acquisition of the shared SCHISM notebook fixture bundle."""
from __future__ import annotations

import os
import shutil
import tempfile
import zipfile
from pathlib import Path

import requests

DATA_REPO = "rom-py/rompy-test-data"
RELEASES_URL = f"https://api.github.com/repos/{DATA_REPO}/releases/latest"
REQUIRED_FILES = ("hgrid.gr3", "vgrid.in", "era5.nc", "hycom.nc")


def describe_fixture(path: str | Path) -> dict[str, object]:
    """Return a compact, JSON-friendly inventory for a SCHISM fixture."""
    import xarray as xr

    fixture = Path(path)
    if fixture.suffix != ".nc":
        return {"path": str(fixture), "kind": "file"}
    with xr.open_dataset(fixture) as dataset:
        return {
            "path": str(fixture),
            "dimensions": {name: int(size) for name, size in dataset.sizes.items()},
            "variables": {name: list(variable.dims) for name, variable in dataset.data_vars.items()},
            "coordinates": list(dataset.coords),
        }


def assert_netcdf_contract(path: str | Path, *, variables: tuple[str, ...] = (), dimensions: tuple[str, ...] = ()) -> None:
    """Assert the structural contract of a generated or source NetCDF file."""
    import xarray as xr

    with xr.open_dataset(path) as dataset:
        missing_variables = sorted(set(variables) - set(dataset.data_vars))
        missing_dimensions = sorted(set(dimensions) - set(dataset.sizes))
    if missing_variables or missing_dimensions:
        raise AssertionError(
            f"{path} does not satisfy its contract: "
            f"missing variables={missing_variables}, dimensions={missing_dimensions}"
        )



def _complete(path: Path) -> bool:
    return all((path / name).is_file() for name in REQUIRED_FILES)


def ensure_schism_data(destination: str | Path | None = None) -> Path:
    """Return the shared SCHISM fixture directory, downloading it explicitly if needed.

    The default location is ``tests/data/schism`` in this repository. Set
    ``ROMPY_NOTEBOOK_DATA`` or pass *destination* to use another location.
    Unlike the sibling pytest conftest implementations, this function never
    runs at import time.
    """
    target = Path(destination or os.environ.get("ROMPY_NOTEBOOK_DATA", "tests/data/schism"))
    if _complete(target):
        return target.resolve()

    response = requests.get(RELEASES_URL, timeout=30)
    response.raise_for_status()
    zip_url = response.json()["zipball_url"]
    target.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as temporary:
        archive = Path(temporary) / "rompy-test-data.zip"
        with requests.get(zip_url, stream=True, timeout=120) as download:
            download.raise_for_status()
            with archive.open("wb") as handle:
                for chunk in download.iter_content(chunk_size=1024 * 1024):
                    if chunk:
                        handle.write(chunk)
        with zipfile.ZipFile(archive) as bundle:
            roots = {member.split("/", 1)[0] for member in bundle.namelist() if "/" in member}
            if len(roots) != 1:
                raise RuntimeError("Unexpected rompy-test-data archive layout")
            root = next(iter(roots))
            prefix = f"{root}/data/schism/"
            extracted = Path(temporary) / "schism"
            for member in bundle.namelist():
                if member.startswith(prefix) and not member.endswith("/"):
                    relative = Path(member[len(prefix) :])
                    output = extracted / relative
                    output.parent.mkdir(parents=True, exist_ok=True)
                    output.write_bytes(bundle.read(member))
        if not _complete(extracted):
            raise RuntimeError("rompy-test-data release lacks the SCHISM fixture bundle")
        if target.exists():
            shutil.rmtree(target)
        shutil.copytree(extracted, target)
    return target.resolve()
