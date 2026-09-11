import json
from pathlib import Path

from scripts import notebook_audit


def write_notebook(path: Path, *, outputs=None):
    path.write_text(
        json.dumps(
            {
                "cells": [
                    {
                        "cell_type": "code",
                        "execution_count": 1,
                        "metadata": {},
                        "outputs": outputs or [],
                        "source": ["print('ok')"],
                    }
                ],
                "metadata": {},
                "nbformat": 4,
                "nbformat_minor": 5,
            }
        )
    )


def test_audit_current_tracked_notebooks_passes():
    assert notebook_audit.audit_notebooks(Path.cwd()) == []


def test_audit_detects_empty_notebook(tmp_path, monkeypatch):
    notebook = tmp_path / "notebooks" / "empty.ipynb"
    notebook.parent.mkdir()
    notebook.touch()
    monkeypatch.setattr(notebook_audit, "tracked_files", lambda root: [notebook])
    assert "empty notebook: notebooks/empty.ipynb" in notebook_audit.audit_notebooks(tmp_path)


def test_audit_detects_invalid_json(tmp_path, monkeypatch):
    notebook = tmp_path / "notebooks" / "invalid.ipynb"
    notebook.parent.mkdir()
    notebook.write_text("not json")
    monkeypatch.setattr(notebook_audit, "tracked_files", lambda root: [notebook])
    assert any("invalid notebook JSON" in item for item in notebook_audit.audit_notebooks(tmp_path))


def test_audit_detects_stored_execution_error(tmp_path, monkeypatch):
    notebook = tmp_path / "notebooks" / "error.ipynb"
    notebook.parent.mkdir()
    write_notebook(notebook, outputs=[{"output_type": "error", "ename": "NameError"}])
    monkeypatch.setattr(notebook_audit, "tracked_files", lambda root: [notebook])
    assert "stored execution error: notebooks/error.ipynb cell 0" in notebook_audit.audit_notebooks(tmp_path)


def test_audit_links_detects_missing_target(tmp_path):
    docs = tmp_path / "docs"
    docs.mkdir()
    (docs / "index.md").write_text("[missing](notebooks/nope.ipynb)")
    assert notebook_audit.audit_links(tmp_path)
