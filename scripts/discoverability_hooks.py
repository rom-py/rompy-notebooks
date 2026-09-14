"""MkDocs hook for metadata-driven journey navigation."""
from __future__ import annotations

from pathlib import Path

try:
    from .notebook_inventory import build_inventory
except ImportError:  # MkDocs loads hooks as standalone modules
    from notebook_inventory import build_inventory


def on_page_content(html, page, config, files):
    source = getattr(page.file, "src_path", "")
    if not source.endswith(".ipynb"):
        return html
    root = Path(config.config_file_path).parent
    records, errors = build_inventory(root)
    if errors:
        raise RuntimeError("Notebook inventory validation failed: " + "; ".join(errors))
    current = next((record for record in records if record["path"] == source), None)
    if not current or not current.get("published") or current.get("kind") != "journey":
        return html
    journey = sorted(
        (record for record in records if record.get("published") and record.get("model") == current["model"] and record.get("kind") == "journey"),
        key=lambda record: record.get("journey", 0),
    )
    index = next((i for i, record in enumerate(journey) if record["id"] == current["id"]), None)
    if index is None:
        return html
    links = []
    page_dir = Path(source).parent
    for label, offset in (("Previous lesson", -1), ("Next lesson", 1)):
        target_index = index + offset
        if 0 <= target_index < len(journey):
            target = journey[target_index]
            target_dir = Path(target["path"]).with_suffix("")
            relative = Path("../") / target_dir.relative_to(page_dir)
            links.append(f"[{label}: {target['id']}]({relative.as_posix()}/)")
    if not links:
        return html
    return html + '<hr><p class="journey-navigation">' + " · ".join(links) + "</p>"
