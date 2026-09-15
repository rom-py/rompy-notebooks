"""Execute eligible staged notebooks without modifying notebook sources."""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

import nbformat
from nbclient import NotebookClient
from nbclient.exceptions import CellExecutionError



def staged_notebooks(root: Path) -> list[Path]:
    """Return notebooks staged under the documentation tree."""
    staging = root / "docs" / "notebooks"
    return sorted(staging.rglob("*.ipynb")) if staging.is_dir() else []


def notebook_metadata(path: Path) -> dict:
    try:
        notebook = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError):
        return None
    metadata = notebook.get("metadata", {}).get("rompy_notebooks", {})
    return metadata if isinstance(metadata, dict) else {}


def execution_mode(path: Path) -> str | None:
    return notebook_metadata(path).get("execution")


def eligible_notebooks(root: Path, *, include_runtime: bool = False, group: str = "journeys") -> tuple[list[Path], list[Path]]:
    """Return (eligible, skipped) notebooks selected by execution metadata."""
    eligible: list[Path] = []
    skipped: list[Path] = []
    for path in staged_notebooks(root):
        metadata = notebook_metadata(path)
        mode = metadata.get("execution")
        metadata_group = metadata.get("execution_group", "journeys" if path.name.startswith("journey_") else "reference")
        eligible_flag = metadata.get("execution_eligible", mode in {"render-only", "configuration-only"})
        if metadata_group != group:
            skipped.append(path)
        elif eligible_flag or (include_runtime and mode == "runtime-dependent"):
            eligible.append(path)
        else:
            skipped.append(path)
    return eligible, skipped


def execute_notebooks(root: Path, *, include_runtime: bool = False, group: str = "journeys", report: Path | None = None) -> list[Path]:
    """Execute staged notebooks in place and return the executed paths."""
    eligible, skipped = eligible_notebooks(root, include_runtime=include_runtime, group=group)
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
    summary = {"tier": "selected-notebook-execution", "started_at": datetime.now(timezone.utc).isoformat(), "group": group, "include_runtime": include_runtime, "executed": [str(path.relative_to(root)) for path in eligible], "skipped": [str(path.relative_to(root)) for path in skipped], "scientific_validation": False, "note": "Current notebook execution is not scientific or model validation."}
    if report:
        report.parent.mkdir(parents=True, exist_ok=True)
        report.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(f"Executed {len(eligible)} notebook(s); skipped {len(skipped)}")
    return eligible


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--include-runtime", action="store_true", help="also execute runtime-dependent notebooks")
    parser.add_argument("--group", default="journeys", help="metadata execution group to select")
    parser.add_argument("--report", type=Path, help="write a current-run JSON report")
    args = parser.parse_args()
    execute_notebooks(args.root.resolve(), include_runtime=args.include_runtime, group=args.group, report=args.report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
