"""Generate metadata-backed notebook reference pages for MkDocs."""
from __future__ import annotations

import argparse
from pathlib import Path

from notebook_inventory import build_inventory


def link(record: dict, prefix: str = "../") -> str:
    path = Path(record["path"]).with_suffix("")
    return f"{prefix}{path.as_posix()}/"


def render_record(record: dict, prefix: str = "../") -> str:
    title = record.get("title") or record["id"].replace("-", " ").title()
    prerequisites = ", ".join(record["prerequisites"]) or "None"
    requirements = ", ".join(record["execution_requirements"]) or "None"
    return (
        f"- [{title}]({link(record, prefix)}) — **{record['level']}**, "
        f"{record['kind']}; topics: {', '.join(record['topics'])}; "
        f"prerequisites: {prerequisites}; execution: {record['execution']} "
        f"({requirements})"
    )


def generate(root: Path, destination: Path) -> None:
    records, errors = build_inventory(root)
    if errors:
        raise ValueError("\n".join(errors))
    published = [record for record in records if record["published"]]
    destination.mkdir(parents=True, exist_ok=True)
    all_text = ["# All notebooks", "", "Generated from notebook metadata. Each published notebook appears once.", ""]
    all_text += [render_record(record) for record in published]
    (destination / "all-notebooks.md").write_text("\n".join(all_text) + "\n", encoding="utf-8")

    by_model = destination / "notebooks-by-model.md"
    model_text = ["# Notebooks by model", "", "Generated from notebook metadata.", ""]
    for model in sorted({record["model"] for record in published}):
        model_text += [f"## {model.upper()}", ""]
        model_text += [render_record(record) for record in published if record["model"] == model]
        model_text.append("")
    by_model.write_text("\n".join(model_text), encoding="utf-8")

    topics = sorted({topic for record in published for topic in record["topics"]})
    topic_text = ["# Notebooks by topic", "", "Generated from notebook metadata.", ""]
    for topic in topics:
        topic_text += [f"## {topic}", ""]
        topic_text += [render_record(record) for record in published if topic in record["topics"]]
        topic_text.append("")
    (destination / "notebooks-by-topic.md").write_text("\n".join(topic_text), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path, default=Path("docs/generated"))
    args = parser.parse_args()
    generate(args.root.resolve(), args.root / args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
