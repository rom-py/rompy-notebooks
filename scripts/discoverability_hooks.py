"""MkDocs hook for metadata-driven tutorial navigation."""
from __future__ import annotations

from html import escape
from pathlib import Path

from mkdocs.utils import get_relative_url

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
    if not current or not current.get("published") or current.get("kind") != "tutorial":
        return html
    tutorial = sorted(
        (record for record in records if record.get("published") and record.get("model") == current["model"] and record.get("kind") == "tutorial"),
        key=lambda record: record.get("tutorial", 0),
    )
    index = next((i for i, record in enumerate(tutorial) if record["id"] == current["id"]), None)
    if index is None:
        return html
    links = []
    for label, offset in (("Previous lesson", -1), ("Next lesson", 1)):
        target_index = index + offset
        if 0 <= target_index < len(tutorial):
            target = tutorial[target_index]
            target_file = files.get_file_from_path(target["path"])
            if target_file is None:
                raise RuntimeError(f"Tutorial navigation target not found: {target['path']}")
            relative = get_relative_url(target_file.url, page.url)
            text = escape(f"{label}: {target['id']}")
            links.append(f'<a href="{escape(relative, quote=True)}">{text}</a>')
    if not links:
        return html
    return html + '<hr><p class="tutorial-navigation">' + " · ".join(links) + "</p>"
