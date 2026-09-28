"""Fast, dependency-free checks for tracked notebook sources and staged docs."""
from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path

try:
    from .notebook_inventory import build_inventory
except ImportError:  # pragma: no cover - direct script execution
    from notebook_inventory import build_inventory

EXCLUDED_PARTS = {".ipynb_checkpoints", "__pycache__"}
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)#]+)")
MODEL_NAMES = {"swan", "xbeach", "schism"}
NOTEBOOK_KINDS = {"tutorial", "example", "reference"}
NOTEBOOK_LEVELS = {"beginner", "intermediate", "advanced"}
NOTEBOOK_EXECUTION = {"render-only", "configuration-only", "runtime-dependent"}
MODEL_OVERVIEWS = {
    "swan": Path("docs/models/swan.md"),
    "xbeach": Path("docs/models/xbeach.md"),
    "schism": Path("docs/models/schism.md"),
}
COVERAGE_MATRIX = Path("docs/models/coverage.md")
SWAN_TUTORIAL = [
    Path("notebooks/swan/tutorial_01_rompy_orientation.ipynb"),
    Path("notebooks/swan/tutorial_02_swan_procedural.ipynb"),
    Path("notebooks/swan/tutorial_03_swan_declarative.ipynb"),
    Path("notebooks/swan/tutorial_04_swan_data.ipynb"),
    Path("notebooks/swan/tutorial_05_swan_components.ipynb"),
    Path("notebooks/swan/tutorial_06_swan_workspace.ipynb"),
    Path("notebooks/swan/tutorial_07_swan_sensitivity.ipynb"),
]
SCHISM_TUTORIAL = [
    Path("notebooks/schism/tutorial_01_rompy_orientation.ipynb"),
    Path("notebooks/schism/tutorial_02_schism_procedural.ipynb"),
    Path("notebooks/schism/tutorial_03_schism_grid_data.ipynb"),
    Path("notebooks/schism/tutorial_04_schism_forcing.ipynb"),
    Path("notebooks/schism/tutorial_05_schism_boundaries.ipynb"),
    Path("notebooks/schism/tutorial_06_schism_real_case.ipynb"),
    Path("notebooks/schism/tutorial_07_schism_execution.ipynb"),
]
XBEACH_TUTORIAL = [
    Path("notebooks/xbeach/tutorial/01_first_model.ipynb"),
    Path("notebooks/xbeach/tutorial/02_model_grid.ipynb"),
    Path("notebooks/xbeach/tutorial/03_bathymetry.ipynb"),
    Path("notebooks/xbeach/tutorial/04_forcing.ipynb"),
    Path("notebooks/xbeach/tutorial/05_model_settings.ipynb"),
    Path("notebooks/xbeach/tutorial/06_complete_setup.ipynb"),
    Path("notebooks/xbeach/tutorial/07_yaml_and_cli.ipynb"),
]
XBEACH_EXAMPLES = Path("notebooks/xbeach/examples")
# Opening sections of every notebook in the tutorial/examples layout (see
# docs/tutorial-conventions.md).
LESSON_TEMPLATE = ["What this shows", "Prerequisites", "You will learn", "Data used"]


def tracked_files(root: Path) -> list[Path]:
    result = subprocess.run(
        ["git", "-C", str(root), "ls-files", "notebooks"],
        check=True,
        capture_output=True,
        text=True,
    )
    return [root / line for line in result.stdout.splitlines()]


def audit_inventory(root: Path) -> list[str]:
    """Validate the metadata-backed inventory and published source paths."""
    _, errors = build_inventory(root)
    return errors


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
        if relative.parts[1:2] and relative.parts[1] in MODEL_NAMES:
            failures.extend(audit_model_metadata(relative, notebook))
        for number, cell in enumerate(notebook.get("cells", [])):
            for output in cell.get("outputs", []) if isinstance(cell, dict) else []:
                if output.get("output_type") == "error":
                    failures.append(f"stored execution error: {relative} cell {number}")
    return failures


def audit_model_metadata(relative: Path, notebook: dict) -> list[str]:
    failures: list[str] = []
    metadata = notebook.get("metadata", {}).get("rompy_notebooks")
    prefix = f"invalid model metadata: {relative}"
    if not isinstance(metadata, dict):
        return [f"missing rompy_notebooks metadata: {relative}"]
    required = ("model", "kind", "level", "topics", "execution")
    missing = [field for field in required if field not in metadata]
    if missing:
        failures.append(f"{prefix}: missing fields {', '.join(missing)}")
        return failures
    expected_model = relative.parts[1]
    if metadata["model"] != expected_model:
        failures.append(f"{prefix}: model must be {expected_model!r}")
    if metadata["kind"] not in NOTEBOOK_KINDS:
        failures.append(f"{prefix}: unsupported kind {metadata['kind']!r}")
    if metadata["level"] not in NOTEBOOK_LEVELS:
        failures.append(f"{prefix}: unsupported level {metadata['level']!r}")
    if not isinstance(metadata["topics"], list) or not metadata["topics"] or not all(
        isinstance(topic, str) and topic for topic in metadata["topics"]
    ):
        failures.append(f"{prefix}: topics must be a non-empty list of strings")
    if metadata["execution"] not in NOTEBOOK_EXECUTION:
        failures.append(f"{prefix}: unsupported execution {metadata['execution']!r}")
    return failures


def _markdown(notebook: dict) -> str:
    return "\n".join(
        "".join(cell.get("source", []))
        for cell in notebook.get("cells", [])
        if isinstance(cell, dict) and cell.get("cell_type") == "markdown"
    )


def _audit_ordered_tutorial(
    root: Path,
    tutorial: list[Path],
    label: str,
    *,
    execution_marker: bool = False,
    markers: list[str] | None = None,
) -> list[str]:
    failures: list[str] = []
    for index, relative in enumerate(tutorial):
        path = root / relative
        if not path.is_file():
            failures.append(f"missing {label} tutorial notebook: {relative}")
            continue
        try:
            notebook = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeDecodeError, json.JSONDecodeError):
            continue
        markdown = _markdown(notebook)
        required = list(markers) if markers else ["Learning goals", "Prerequisites", "## Checkpoint"]
        if execution_marker:
            required.append("Execution contract")
        for marker in required:
            if marker.lower() not in markdown.lower():
                failures.append(f"{label} tutorial missing {marker}: {relative}")
        if index < len(tutorial) - 1:
            next_name = tutorial[index + 1].stem
            if next_name not in markdown:
                failures.append(f"{label} tutorial missing next link: {relative} -> {next_name}")
        if index > 0:
            previous_name = tutorial[index - 1].stem
            if previous_name not in markdown:
                failures.append(f"{label} tutorial missing previous link: {relative} -> {previous_name}")
    return failures


def audit_tutorial(root: Path) -> list[str]:
    return _audit_ordered_tutorial(root, SWAN_TUTORIAL, "SWAN")


def audit_xbeach_tutorial(root: Path) -> list[str]:
    return _audit_ordered_tutorial(root, XBEACH_TUTORIAL, "XBeach", markers=LESSON_TEMPLATE)


def audit_xbeach_examples(root: Path) -> list[str]:
    """Check that every XBeach example opens with the lesson template."""
    failures: list[str] = []
    for path in sorted((root / XBEACH_EXAMPLES).glob("*.ipynb")):
        relative = path.relative_to(root)
        try:
            markdown = _markdown(json.loads(path.read_text(encoding="utf-8"))).lower()
        except (OSError, UnicodeDecodeError, json.JSONDecodeError):
            continue
        for marker in LESSON_TEMPLATE:
            if marker.lower() not in markdown:
                failures.append(f"XBeach example missing {marker}: {relative}")
    return failures


def audit_schism_tutorial(root: Path) -> list[str]:
    return _audit_ordered_tutorial(root, SCHISM_TUTORIAL, "SCHISM", execution_marker=True)


def audit_value_narrative(root: Path) -> list[str]:
    failures: list[str] = []
    # XBeach uses the lesson template (LESSON_TEMPLATE) instead of these markers.
    tutorials = [("SWAN", SWAN_TUTORIAL), ("SCHISM", SCHISM_TUTORIAL)]
    for label, paths in tutorials:
        for relative in paths:
            path = root / relative
            if not path.is_file():
                continue
            notebook = json.loads(path.read_text(encoding="utf-8"))
            markdown = "\\n".join(
                "".join(cell.get("source", []))
                for cell in notebook.get("cells", [])
                if cell.get("cell_type") == "markdown"
            ).lower()
            for marker in ("without rompy", "with rompy"):
                if marker not in markdown:
                    failures.append(f"{label} tutorial missing value marker {marker}: {relative}")
    enriched = {
        relative
        for relative in (
            Path("notebooks/swan/tutorial_04_swan_data.ipynb"),
            Path("notebooks/swan/tutorial_06_swan_workspace.ipynb"),
            Path("notebooks/schism/tutorial_03_schism_grid_data.ipynb"),
            Path("notebooks/schism/tutorial_04_schism_forcing.ipynb"),
            Path("notebooks/schism/tutorial_05_schism_boundaries.ipynb"),
            Path("notebooks/schism/tutorial_06_schism_real_case.ipynb"),
        )
    }
    for relative in enriched:
        path = root / relative
        if not path.is_file():
            continue
        notebook = json.loads(path.read_text(encoding="utf-8"))
        markdown = "\\n".join(
            "".join(cell.get("source", []))
            for cell in notebook.get("cells", [])
            if cell.get("cell_type") == "markdown"
        ).lower()
        marker = "generated" if relative in {
            Path("notebooks/swan/tutorial_06_swan_workspace.ipynb"),
            Path("notebooks/schism/tutorial_06_schism_real_case.ipynb"),
        } else "verification"
        if marker not in markdown:
            failures.append(f"tutorial missing value marker {marker}: {relative}")
    return failures


def audit_forcing_depth(root: Path) -> list[str]:
    """Check that enriched case-study notebooks explain source-to-output work."""
    failures: list[str] = []
    required = {
        "SWAN": (Path("notebooks/swan/tutorial_04_swan_data.ipynb"), ("source", "verification")),
        "SCHISM": (Path("notebooks/schism/tutorial_06_schism_real_case.ipynb"), ("source", "generated", "verification", "assumption")),
    }
    for label, (relative, markers) in required.items():
        path = root / relative
        if not path.is_file():
            continue
        notebook = json.loads(path.read_text(encoding="utf-8"))
        text = "\n".join(
            "".join(cell.get("source", []))
            for cell in notebook.get("cells", [])
            if isinstance(cell, dict)
        ).lower()
        missing = [marker for marker in markers if marker not in text]
        if missing:
            failures.append(f"{label} forcing case missing depth markers: {', '.join(missing)}")
    return failures


def audit_visual_verification(root: Path) -> list[str]:
    failures: list[str] = []
    required = {
        "SWAN": [Path("notebooks/swan/tutorial_04_swan_data.ipynb")],
        "XBeach": [Path("notebooks/xbeach/tutorial/02_model_grid.ipynb"), Path("notebooks/xbeach/tutorial/03_bathymetry.ipynb"), Path("notebooks/xbeach/tutorial/04_forcing.ipynb")],
        "SCHISM": [Path("notebooks/schism/tutorial_03_schism_grid_data.ipynb"), Path("notebooks/schism/tutorial_04_schism_forcing.ipynb"), Path("notebooks/schism/tutorial_05_schism_boundaries.ipynb")],
    }
    for label, paths in required.items():
        for relative in paths:
            path = root / relative
            if not path.is_file():
                failures.append(f"missing {label} visual-verification notebook: {relative}")
                continue
            notebook = json.loads(path.read_text(encoding="utf-8"))
            source = "\\n".join("".join(cell.get("source", [])) for cell in notebook.get("cells", []))
            if "matplotlib" not in source or ("plot(" not in source and "pcolormesh" not in source):
                failures.append(f"{label} visual verification lacks a plot: {relative}")
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


def audit_navigation_coverage(root: Path) -> list[str]:
    """Ensure published inventory is represented by generated and curated views."""
    records, errors = build_inventory(root)
    if errors:
        return errors
    mkdocs = (root / "mkdocs.yml").read_text(encoding="utf-8")
    gallery = (root / "docs/gallery.md").read_text(encoding="utf-8")
    failures = []
    all_catalogue = root / "docs/generated/all-notebooks.md"
    all_text = all_catalogue.read_text(encoding="utf-8") if all_catalogue.is_file() else ""
    for record in records:
        if record["published"]:
            route = Path(record["path"]).with_suffix("").as_posix()
            if route not in all_text:
                failures.append(f"published notebook absent from complete catalogue: {record['path']}")
    for generated in ("generated/all-notebooks.md", "generated/notebooks-by-model.md", "generated/notebooks-by-topic.md"):
        if generated not in mkdocs:
            failures.append(f"generated discoverability page absent from navigation: {generated}")
    return failures


def audit_model_docs(root: Path) -> list[str]:
    failures: list[str] = []
    role_terms = ("tutorial", "reference")
    for model, relative in MODEL_OVERVIEWS.items():
        path = root / relative
        if not path.is_file():
            failures.append(f"missing {model} model overview: {relative}")
            continue
        text = path.read_text(encoding="utf-8").lower()
        if "coverage" not in text:
            failures.append(f"model overview missing coverage status: {relative}")
        missing_roles = [role for role in role_terms if role not in text]
        if missing_roles:
            failures.append(f"model overview missing roles {', '.join(missing_roles)}: {relative}")
    matrix = root / COVERAGE_MATRIX
    if not matrix.is_file():
        failures.append(f"missing model coverage matrix: {COVERAGE_MATRIX}")
    else:
        text = matrix.read_text(encoding="utf-8").lower()
        for model in MODEL_NAMES:
            if model not in text:
                failures.append(f"coverage matrix missing model: {model}")
        for status in ("established", "partial", "not yet covered"):
            if status not in text:
                failures.append(f"coverage matrix missing status: {status}")
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
            # MkDocs turns notebook sources into directory pages, while the
            # staged source remains a sibling .ipynb file on disk.
            notebook_source = Path(str(resolved).rstrip("/" ) + ".ipynb")
            if not resolved.exists() and not notebook_source.exists():
                failures.append(f"missing documentation target: {page.relative_to(root)} -> {target}")
    return failures


def run(root: Path) -> int:
    failures = (
        audit_inventory(root)
        + audit_notebooks(root)
        + audit_tutorial(root)
        + audit_xbeach_tutorial(root)
        + audit_xbeach_examples(root)
        + audit_schism_tutorial(root)
        + audit_value_narrative(root)
        + audit_forcing_depth(root)
        + audit_visual_verification(root)
        + audit_model_docs(root)
        + audit_navigation_coverage(root)
        + audit_hygiene(root)
        + audit_links(root)
    )
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
