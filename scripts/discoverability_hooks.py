"""MkDocs hooks for notebook pages: relative links and tutorial navigation."""
from __future__ import annotations

import html as html_lib
import posixpath
import re
from pathlib import Path

from markdown.extensions.toc import slugify

try:
    from .notebook_inventory import build_inventory
except ImportError:  # MkDocs loads hooks as standalone modules
    from notebook_inventory import build_inventory

# Relative href/src attributes: no scheme, not absolute, not a bare anchor.
RELATIVE_LINK_RE = re.compile(r'(href|src)="(?![a-z][a-z0-9+.-]*:|/|#)([^"#]+)(#[^"]*)?"')
MODEL_README_RE = re.compile(r"^notebooks/([^/]+)/README\.md$")


def site_link(target: str, source: str, docs_dir: Path, repo_url: str) -> str | None:
    """Return the site URL for a link written relative to a notebook, or None.

    Notebook links are written for Jupyter and GitHub (``02_model_grid.ipynb``,
    ``../README.md``). MkDocs serves each notebook as a directory page one
    level deeper, so these links need translating:

    * staged notebooks become their pages, other staged files are prefixed;
    * a model's ``README.md`` becomes its tutorial page (``<model>-tutorial``);
    * a page in the repository's ``docs/`` folder becomes that site page;
    * any other repository file or folder links to GitHub.
    """
    page_dir = posixpath.splitext(source)[0]
    resolved = posixpath.normpath(posixpath.join(posixpath.dirname(source), target))
    if resolved.startswith("../"):
        return None
    staged = docs_dir / resolved
    if resolved.endswith(".ipynb") and staged.is_file():
        return posixpath.relpath(posixpath.splitext(resolved)[0], page_dir) + "/"
    if staged.is_file():
        return posixpath.relpath(resolved, page_dir)
    if resolved.startswith("docs/") and resolved.endswith(".md") and (docs_dir / resolved[5:]).is_file():
        return posixpath.relpath(posixpath.splitext(resolved[5:])[0], page_dir) + "/"
    readme = MODEL_README_RE.match(resolved)
    if readme and (docs_dir / f"{readme.group(1)}-tutorial.md").is_file():
        return posixpath.relpath(f"{readme.group(1)}-tutorial", page_dir) + "/"
    repository = docs_dir.parent / resolved
    if repo_url and repository.exists():
        kind = "tree" if repository.is_dir() else "blob"
        return f"{repo_url.rstrip('/')}/{kind}/main/{resolved}"
    return None


def site_anchor(anchor: str) -> str:
    """Translate a Jupyter heading anchor (``#8.-Run-XBeach``) to the MkDocs one."""
    return "#" + slugify(anchor[1:].replace("-", " "), "-")


def rewrite_links(html: str, source: str, docs_dir: Path, repo_url: str) -> str:
    def replace(match: re.Match) -> str:
        attribute, target, anchor = match.group(1), match.group(2), match.group(3) or ""
        url = site_link(target, source, docs_dir, repo_url)
        if url is None:
            return match.group(0)
        if anchor and target.endswith(".ipynb"):
            anchor = site_anchor(anchor)
        return f'{attribute}="{url}{anchor}"'

    return RELATIVE_LINK_RE.sub(replace, html)


def on_page_content(html, page, config, files):
    source = getattr(page.file, "src_path", "")
    if not source.endswith(".ipynb"):
        return html
    html = rewrite_links(html, source, Path(config["docs_dir"]), config.get("repo_url") or "")
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
    # Each notebook is served as a directory page, e.g. .../tutorial/02_model_grid/.
    page_dir = posixpath.splitext(source)[0]
    for label, offset in (("Previous lesson", -1), ("Next lesson", 1)):
        target_index = index + offset
        if 0 <= target_index < len(tutorial):
            target = tutorial[target_index]
            url = posixpath.relpath(posixpath.splitext(target["path"])[0], page_dir) + "/"
            title = html_lib.escape(target.get("title") or target["id"])
            links.append(f'<a href="{url}">{label}: {title}</a>')
    if not links:
        return html
    return html + '<hr><p class="tutorial-navigation">' + " · ".join(links) + "</p>"
