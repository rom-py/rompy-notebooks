"""Execute eligible staged notebooks without modifying notebook sources."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import nbformat
from nbclient import NotebookClient
from nbclient.exceptions import CellExecutionError



def staged_notebooks(root: Path) -> list[Path]:
    """Return notebooks staged under the documentation tree."""
    staging = root / "docs" / "notebooks"
    return sorted(staging.rglob("*.ipynb")) if staging.is_dir() else []


def execution_mode(path: Path) -> str | None:
    try:
        notebook = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError):
        return None
    metadata = notebook.get("metadata", {}).get("rompy_notebooks", {})
    return metadata.get("execution") if isinstance(metadata, dict) else None


def eligible_notebooks(root: Path, *, include_runtime: bool = False) -> tuple[list[Path], list[Path]]:
    """Return (eligible, skipped) staged journey notebooks."""
    eligible: list[Path] = []
    skipped: list[Path] = []
    for path in staged_notebooks(root):
        # The default build executes the curated journeys, not every reference notebook.
        if not path.name.startswith("journey_"):
            skipped.append(path)
            continue
        mode = execution_mode(path)
        if mode == "runtime-dependent" and not include_runtime:
            skipped.append(path)
        elif mode in {"render-only", "configuration-only"} or include_runtime:
            eligible.append(path)
        else:
            skipped.append(path)
    return eligible, skipped


def execute_notebooks(root: Path, *, include_runtime: bool = False) -> list[Path]:
    """Execute staged notebooks in place and return the executed paths."""
    eligible, skipped = eligible_notebooks(root, include_runtime=include_runtime)
    for path in skipped:
        print(f"Skipping {path.relative_to(root)}")
    for path in eligible:
        print(f"Executing {path.relative_to(root)}")
        notebook = nbformat.read(path, as_version=4)
        try:
            NotebookClient(
                notebook,
                timeout=600,
                kernel_name="python3",
                resources={"metadata": {"path": str(root)}},
                allow_errors=False,
            ).execute()
        except CellExecutionError as exc:
            cell = getattr(exc, "cell_index", "unknown")
            raise RuntimeError(f"Notebook execution failed: {path.relative_to(root)} (cell {cell})") from exc
        nbformat.write(notebook, path)
    print(f"Executed {len(eligible)} notebook(s); skipped {len(skipped)}")
    return eligible


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--include-runtime", action="store_true", help="also execute runtime-dependent notebooks")
    args = parser.parse_args()
    execute_notebooks(args.root.resolve(), include_runtime=args.include_runtime)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
