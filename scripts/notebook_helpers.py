"""Small, explicit helpers used by the model journey notebooks."""
from __future__ import annotations

from pathlib import Path


def repository_root(start: str | Path | None = None) -> Path:
    """Find the checkout containing ``notebooks`` and ``scripts``."""
    origin = Path(start or Path.cwd()).resolve()
    candidates = (origin, *origin.parents)
    for candidate in candidates:
        if (candidate / "notebooks").is_dir() and (candidate / "scripts").is_dir():
            return candidate
    raise FileNotFoundError("Could not locate the rompy-notebooks repository root")


def workspace_manifest(path: str | Path) -> list[str]:
    """Return stable relative file names for a generated workspace."""
    root = Path(path)
    if not root.exists():
        return []
    return sorted(str(item.relative_to(root)) for item in root.rglob("*") if item.is_file())


def print_workspace_manifest(path: str | Path) -> list[str]:
    """Print and return the files in a generated workspace."""
    files = workspace_manifest(path)
    print(f"Workspace: {Path(path).resolve()}")
    for name in files:
        print(f"  - {name}")
    return files
