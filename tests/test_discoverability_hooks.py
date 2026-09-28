"""Regression tests for navigation added after notebook HTML rendering."""
from html.parser import HTMLParser
from pathlib import Path
from types import SimpleNamespace
from urllib.parse import urljoin

import pytest
from mkdocs.structure.files import File, Files
from mkdocs_jupyter.plugin import NotebookFile

from scripts import discoverability_hooks
from scripts.notebook_inventory import build_inventory


class NavigationLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            self.hrefs.append(dict(attrs)["href"])


@pytest.mark.parametrize("use_directory_urls", [True, False])
def test_all_published_tutorial_links_resolve(use_directory_urls):
    root = Path.cwd()
    records, errors = build_inventory(root)
    assert errors == []
    files = Files([
        NotebookFile(
            File(record["path"], str(root / "docs"), str(root / "site"), use_directory_urls),
            use_directory_urls,
            str(root / "site"),
        )
        for record in records if record["published"]
    ])
    config = SimpleNamespace(config_file_path=str(root / "mkdocs.yml"))
    tutorials = [r for r in records if r["published"] and r["kind"] == "tutorial"]
    for current in tutorials:
        series = sorted(
            (r for r in tutorials if r["model"] == current["model"]),
            key=lambda r: r.get("tutorial", 0),
        )
        index = series.index(current)
        neighbours = [series[i] for i in (index - 1, index + 1) if 0 <= i < len(series)]
        file = files.get_file_from_path(current["path"])
        page = SimpleNamespace(file=file, url=file.url)
        html = discoverability_hooks.on_page_content("<p>Lesson</p>", page, config, files)
        links = NavigationLinks()
        links.feed(html)
        # A deployment subpath must be preserved, not replaced by a root-relative link.
        base = "https://example.org/rompy-notebooks/"
        assert [urljoin(base + page.url, href) for href in links.hrefs] == [
            base + files.get_file_from_path(record["path"]).url for record in neighbours
        ]
        assert "[Previous lesson:" not in html
        assert "[Next lesson:" not in html
        assert html.startswith("<p>Lesson</p>")


def test_navigation_escapes_link_text_and_url(monkeypatch):
    records = [
        {"path": f"notebooks/{i}.ipynb", "id": identifier, "published": True,
         "kind": "tutorial", "model": "swan", "tutorial": i}
        for i, identifier in enumerate(["first", '<next & "lesson">'])
    ]
    monkeypatch.setattr(discoverability_hooks, "build_inventory", lambda root: (records, []))
    page = SimpleNamespace(file=SimpleNamespace(src_path="notebooks/0.ipynb"), url="notebooks/0/")
    files = SimpleNamespace(get_file_from_path=lambda path: SimpleNamespace(url='notebooks/1/?a=1&b="2"'))
    result = discoverability_hooks.on_page_content("", page, SimpleNamespace(config_file_path="mkdocs.yml"), files)
    assert 'Next lesson: &lt;next &amp; &quot;lesson&quot;&gt;' in result
    assert 'href="../1/?a=1&amp;b=&quot;2&quot;"' in result


def test_non_notebook_page_is_unchanged():
    page = SimpleNamespace(file=SimpleNamespace(src_path="index.md"))
    assert discoverability_hooks.on_page_content("<p>Home</p>", page, None, None) == "<p>Home</p>"
