"""Stage tracked notebook sources for the MkDocs site."""
from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

EXCLUDED_PARTS = {".ipynb_checkpoints", "__pycache__"}
EXCLUDED_PATHS = {
    Path("notebooks/swan/example_procedural/run1"),
}


def repository_root() -> Path:
    return Path(__file__).resolve().parents[1]


def tracked_notebook_files(root: Path) -> list[Path]:
    result = subprocess.run(
        ["git", "-C", str(root), "ls-files", "notebooks"],
        check=True,
        capture_output=True,
        text=True,
    )
    return [
        root / line
        for line in result.stdout.splitlines()
        if line.endswith((".ipynb", ".png")) and (root / line).is_file()
    ]


def excluded(relative: Path) -> bool:
    return bool(EXCLUDED_PARTS.intersection(relative.parts)) or any(
        relative == path or path in relative.parents for path in EXCLUDED_PATHS
    )


def sync(root: Path | None = None) -> Path:
    root = root or repository_root()
    destination = root / "docs" / "notebooks"
    if destination.exists():
        shutil.rmtree(destination)
    copied = 0
    for source in tracked_notebook_files(root):
        relative = source.relative_to(root)
        if excluded(relative):
            continue
        target = destination / relative.relative_to("notebooks")
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
        copied += 1
    if copied == 0:
        raise RuntimeError("No tracked notebook sources were staged")
    print(f"Staged {copied} notebook/assets files in {destination}")
    return destination


if __name__ == "__main__":
    sync()
