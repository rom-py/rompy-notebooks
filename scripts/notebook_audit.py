"""Fast, dependency-free checks for tracked notebook sources and staged docs."""
from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path

EXCLUDED_PARTS = {".ipynb_checkpoints", "__pycache__"}
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)#]+)")


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
    failures = audit_notebooks(root) + audit_hygiene(root) + audit_links(root)
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
