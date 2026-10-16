"""Helpers for reporting isolated example output workspaces."""
from __future__ import annotations

import importlib.metadata
import json
from pathlib import Path


def report(workspace: str | Path, *, tier: str, artefacts: list[str] | None = None) -> dict:
    """Return a reproducibility report for generated files in *workspace*."""
    directory = Path(workspace)
    names = artefacts or sorted(path.name for path in directory.iterdir() if path.is_file())
    return {
        "workspace": str(directory),
        "tier": tier,
        "artefacts": [{"path": name, "policy": "ignored"} for name in names],
        "environment": {"rompy": _version("rompy")},
        "scientific_validation": False,
        "note": "Generated artefacts document structural processing only; they are not scientific validation evidence.",
    }


def write_report(workspace: str | Path, destination: str | Path, *, tier: str) -> Path:
    destination = Path(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(report(workspace, tier=tier), indent=2) + "\n", encoding="utf-8")
    return destination


def _version(package: str) -> str:
    try:
        return importlib.metadata.version(package)
    except importlib.metadata.PackageNotFoundError:
        return "unavailable"
