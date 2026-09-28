from pathlib import Path

from scripts.discoverability_hooks import rewrite_links, site_link

REPO = "https://github.com/rom-py/rompy-notebooks"
SOURCE = "notebooks/xbeach/tutorial/02_model_grid.ipynb"


def make_tree(tmp_path: Path) -> Path:
    docs = tmp_path / "docs"
    for path in (
        "docs/notebooks/xbeach/tutorial/01_first_model.ipynb",
        "docs/notebooks/xbeach/tutorial/02_model_grid.ipynb",
        "docs/notebooks/xbeach/tutorial/scheme.png",
        "docs/notebooks/xbeach/examples/output.ipynb",
        "docs/xbeach-tutorial.md",
        "docs/why-rompy.md",
        "notebooks/xbeach/data/bathy.tif",
        "notebooks/xbeach/tutorial/config.yml",
    ):
        (tmp_path / path).parent.mkdir(parents=True, exist_ok=True)
        (tmp_path / path).write_text("")
    return docs


def test_notebook_links_point_to_pages(tmp_path):
    docs = make_tree(tmp_path)
    assert site_link("01_first_model.ipynb", SOURCE, docs, REPO) == "../01_first_model/"
    assert site_link("../examples/output.ipynb", SOURCE, docs, REPO) == "../../examples/output/"
    assert site_link("scheme.png", SOURCE, docs, REPO) == "../scheme.png"


def test_readme_links_point_to_tutorial_page(tmp_path):
    docs = make_tree(tmp_path)
    assert site_link("../README.md", SOURCE, docs, REPO) == "../../../../xbeach-tutorial/"


def test_docs_links_point_to_site_pages(tmp_path):
    docs = make_tree(tmp_path)
    assert site_link("../../../docs/why-rompy.md", SOURCE, docs, REPO) == "../../../../why-rompy/"


def test_repository_files_link_to_github(tmp_path):
    docs = make_tree(tmp_path)
    assert site_link("../data", SOURCE, docs, REPO) == f"{REPO}/tree/main/notebooks/xbeach/data"
    assert site_link("config.yml", SOURCE, docs, REPO) == f"{REPO}/blob/main/notebooks/xbeach/tutorial/config.yml"
    assert site_link("missing.ipynb", SOURCE, docs, REPO) is None


def test_rewrite_keeps_external_links_and_translates_anchors(tmp_path):
    docs = make_tree(tmp_path)
    html = (
        '<a href="01_first_model.ipynb#8.-Run-XBeach">run</a>'
        '<a href="https://xbeach.readthedocs.io">xbeach</a>'
        '<a href="#setup">setup</a>'
        '<a href="../tutorial_03/">site link</a>'
    )
    result = rewrite_links(html, SOURCE, docs, REPO)
    assert 'href="../01_first_model/#8-run-xbeach"' in result
    assert 'href="https://xbeach.readthedocs.io"' in result
    assert 'href="#setup"' in result
    assert 'href="../tutorial_03/"' in result
