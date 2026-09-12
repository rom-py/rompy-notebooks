"""Fast, dependency-free checks for tracked notebook sources and staged docs."""
from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path

EXCLUDED_PARTS = {".ipynb_checkpoints", "__pycache__"}
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)#]+)")
SWAN_JOURNEY = [
    Path("notebooks/swan/journey_01_rompy_orientation.ipynb"),
    Path("notebooks/swan/journey_02_swan_procedural.ipynb"),
    Path("notebooks/swan/journey_03_swan_declarative.ipynb"),
    Path("notebooks/swan/journey_04_swan_data.ipynb"),
    Path("notebooks/swan/journey_05_swan_components.ipynb"),
    Path("notebooks/swan/journey_06_swan_workspace.ipynb"),
    Path("notebooks/swan/journey_07_swan_sensitivity.ipynb"),
]


def tracked_files(root: Path) -> list[Path]:
    result = subprocess.run(
        ["git", "-C", str(root), "ls-files", "notebooks"],
        check=True,
        capture_output=True,
        text=True,
    )
    return [root / line for line in result.stdout.splitlines()]


def audit_notebooks(root: Path) -> list[str]:
    failures: list[str] = []
    notebooks = [p for p in tracked_files(root) if p.suffix == ".ipynb"]
    for path in notebooks:
        relative = path.relative_to(root)
        if not path.is_file():
            # A deleted tracked path is handled by Git review; do not inspect it.
            continue
        if not path.read_bytes():
            failures.append(f"empty notebook: {relative}")
            continue
        try:
            notebook = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
            failures.append(f"invalid notebook JSON: {relative}: {exc}")
            continue
        if notebook.get("nbformat") != 4:
            failures.append(f"unsupported notebook format: {relative}")
        if not isinstance(notebook.get("metadata"), dict):
            failures.append(f"missing notebook metadata: {relative}")
        if not isinstance(notebook.get("cells"), list):
            failures.append(f"missing cells list: {relative}")
        for number, cell in enumerate(notebook.get("cells", [])):
            for output in cell.get("outputs", []) if isinstance(cell, dict) else []:
                if output.get("output_type") == "error":
                    failures.append(f"stored execution error: {relative} cell {number}")
    return failures


def audit_journey(root: Path) -> list[str]:
    failures: list[str] = []
    for index, relative in enumerate(SWAN_JOURNEY):
        path = root / relative
        if not path.is_file():
            failures.append(f"missing SWAN journey notebook: {relative}")
            continue
        try:
            notebook = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeDecodeError, json.JSONDecodeError):
            continue
        markdown = "\n".join(
            "".join(cell.get("source", []))
            for cell in notebook.get("cells", [])
            if isinstance(cell, dict) and cell.get("cell_type") == "markdown"
        )
        for marker in ("Learning goals", "Prerequisites", "## Checkpoint"):
            if marker.lower() not in markdown.lower():
                failures.append(f"SWAN journey missing {marker}: {relative}")
        if index < len(SWAN_JOURNEY) - 1:
            next_name = SWAN_JOURNEY[index + 1].stem
            if next_name not in markdown:
                failures.append(f"SWAN journey missing next link: {relative} -> {next_name}")
        if index > 0:
            previous_name = SWAN_JOURNEY[index - 1].stem
            if previous_name not in markdown:
                failures.append(f"SWAN journey missing previous link: {relative} -> {previous_name}")
    return failures


def audit_hygiene(root: Path) -> list[str]:
    failures: list[str] = []
    for path in tracked_files(root):
        relative = path.relative_to(root)
        if EXCLUDED_PARTS.intersection(relative.parts):
            failures.append(f"generated path is tracked: {relative}")
    staged = root / "docs" / "notebooks"
    if staged.exists():
        for path in staged.rglob("*"):
            if EXCLUDED_PARTS.intersection(path.relative_to(staged).parts):
                failures.append(f"generated path is staged: {path.relative_to(root)}")
    return failures


def audit_links(root: Path) -> list[str]:
    failures: list[str] = []
    docs = root / "docs"
    if not docs.exists():
        return ["missing docs directory"]
    for page in docs.rglob("*.md"):
        for target in LINK_RE.findall(page.read_text(encoding="utf-8")):
            if "://" in target or target.startswith("#"):
                continue
            resolved = (page.parent / target).resolve()
            if not resolved.exists():
                failures.append(f"missing documentation target: {page.relative_to(root)} -> {target}")
    return failures


def run(root: Path) -> int:
    failures = audit_notebooks(root) + audit_journey(root) + audit_hygiene(root) + audit_links(root)
    if failures:
        print("Notebook quality gate failed:")
        print("\n".join(f"- {failure}" for failure in failures))
        return 1
    print("Notebook quality gate passed")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    raise SystemExit(run(args.root.resolve()))
