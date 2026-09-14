"""Build and validate the metadata-backed notebook inventory.

The normalized ``rompy_notebooks`` contract is:

* ``id``: stable kebab-case identifier, unique within the repository;
* ``model``: ``swan``, ``xbeach``, or ``schism``;
* ``kind``: ``journey``, ``tutorial``, or ``reference``;
* ``level``: ``beginner``, ``intermediate``, or ``advanced``;
* ``topics``: non-empty list of topic identifiers;
* ``execution``: render-only, configuration-only, or runtime-dependent;
* ``prerequisites`` and ``execution_requirements``: lists of strings;
* ``published``: explicit boolean, with ``exclusion_reason`` when false;
* ``journey``: optional positive integer for ordered journey lessons.
"""
from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path

MODELS = {"swan", "xbeach", "schism"}
KINDS = {"journey", "tutorial", "reference"}
LEVELS = {"beginner", "intermediate", "advanced"}
EXECUTION = {"render-only", "configuration-only", "runtime-dependent"}
REQUIRED = ("id", "model", "kind", "level", "topics", "execution", "prerequisites", "execution_requirements", "published")


def tracked_notebooks(root: Path) -> list[Path]:
    result = subprocess.run(
        ["git", "-C", str(root), "ls-files", "notebooks"],
        check=True, capture_output=True, text=True,
    )
    return sorted(root / p for p in result.stdout.splitlines() if p.endswith(".ipynb"))


def load_notebook(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _metadata(path: Path, root: Path) -> dict:
    metadata = load_notebook(path).get("metadata", {}).get("rompy_notebooks")
    return metadata if isinstance(metadata, dict) else {}


def validate_metadata(relative: Path, metadata: dict) -> list[str]:
    errors: list[str] = []
    prefix = f"invalid inventory metadata: {relative}"
    missing = [field for field in REQUIRED if field not in metadata]
    if missing:
        return [f"{prefix}: missing fields {', '.join(missing)}"]
    if not isinstance(metadata["id"], str) or not metadata["id"].strip():
        errors.append(f"{prefix}: id must be a non-empty string")
    if metadata["model"] not in MODELS:
        errors.append(f"{prefix}: unsupported model {metadata['model']!r}")
    if metadata["kind"] not in KINDS:
        errors.append(f"{prefix}: unsupported kind {metadata['kind']!r}")
    if metadata["level"] not in LEVELS:
        errors.append(f"{prefix}: unsupported level {metadata['level']!r}")
    if metadata["execution"] not in EXECUTION:
        errors.append(f"{prefix}: unsupported execution {metadata['execution']!r}")
    for field in ("topics", "prerequisites", "execution_requirements"):
        value = metadata[field]
        if not isinstance(value, list) or not all(isinstance(item, str) and item.strip() for item in value):
            errors.append(f"{prefix}: {field} must be a list of non-empty strings")
    if not isinstance(metadata["published"], bool):
        errors.append(f"{prefix}: published must be boolean")
    if metadata["published"] is False and not isinstance(metadata.get("exclusion_reason"), str):
        errors.append(f"{prefix}: excluded notebooks require exclusion_reason")
    if "journey" in metadata and (not isinstance(metadata["journey"], int) or metadata["journey"] < 1):
        errors.append(f"{prefix}: journey must be a positive integer")
    return errors


def build_inventory(root: Path) -> tuple[list[dict], list[str]]:
    records: list[dict] = []
    errors: list[str] = []
    for path in tracked_notebooks(root):
        relative = path.relative_to(root)
        if relative.parts[1] not in MODELS:
            continue
        metadata = _metadata(path, root)
        errors.extend(validate_metadata(relative, metadata))
        records.append({"path": relative.as_posix(), **metadata})
    seen: dict[str, str] = {}
    for record in records:
        identifier = record.get("id")
        if isinstance(identifier, str) and identifier in seen:
            errors.append(f"duplicate inventory id {identifier!r}: {seen[identifier]} and {record['path']}")
        elif isinstance(identifier, str):
            seen[identifier] = record["path"]
    records.sort(key=lambda record: (str(record.get("id", "")), record["path"]))
    return records, errors


def run(root: Path, output: Path | None = None) -> int:
    records, errors = build_inventory(root)
    if errors:
        print("Notebook inventory validation failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    payload = {"version": 1, "notebooks": records}
    encoded = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if output:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(encoded, encoding="utf-8")
    else:
        print(encoded, end="")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    raise SystemExit(run(args.root.resolve(), args.output))
