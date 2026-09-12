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


def test_audit_current_swan_journey_passes():
    assert notebook_audit.audit_journey(Path.cwd()) == []


def test_audit_current_model_metadata_passes():
    assert notebook_audit.audit_notebooks(Path.cwd()) == []


def test_audit_current_value_narrative_passes():
    assert notebook_audit.audit_value_narrative(Path.cwd()) == []


def test_audit_current_visual_verification_passes():
    assert notebook_audit.audit_visual_verification(Path.cwd()) == []


def test_audit_current_model_docs_passes():
    assert notebook_audit.audit_model_docs(Path.cwd()) == []


def test_audit_model_docs_detects_missing_overview(tmp_path):
    assert any(
        "missing swan model overview" in item
        for item in notebook_audit.audit_model_docs(tmp_path)
    )


def test_audit_model_metadata_rejects_invalid_values(tmp_path, monkeypatch):
    notebook = tmp_path / "notebooks" / "swan" / "example.ipynb"
    notebook.parent.mkdir(parents=True)
    write_notebook(notebook)
    data = json.loads(notebook.read_text())
    data["metadata"]["rompy_notebooks"] = {
        "model": "xbeach",
        "kind": "invalid",
        "level": "beginner",
        "topics": ["configuration"],
        "execution": "render-only",
    }
    notebook.write_text(json.dumps(data))
    monkeypatch.setattr(notebook_audit, "tracked_files", lambda root: [notebook])
    failures = notebook_audit.audit_notebooks(tmp_path)
    assert any("model must be 'swan'" in item for item in failures)
    assert any("unsupported kind 'invalid'" in item for item in failures)


def test_audit_journey_detects_missing_step(tmp_path, monkeypatch):
    monkeypatch.setattr(notebook_audit, "SWAN_JOURNEY", [Path("notebooks/missing.ipynb")])
    assert notebook_audit.audit_journey(tmp_path) == [
        "missing SWAN journey notebook: notebooks/missing.ipynb"
    ]


def test_audit_current_xbeach_journey_passes():
    assert notebook_audit.audit_xbeach_journey(Path.cwd()) == []


def test_audit_current_schism_journey_passes():
    assert notebook_audit.audit_schism_journey(Path.cwd()) == []


def test_audit_schism_journey_detects_missing_execution_context(tmp_path, monkeypatch):
    path = tmp_path / "notebooks" / "schism" / "journey_01_only.ipynb"
    path.parent.mkdir(parents=True)
    write_notebook(path)
    data = json.loads(path.read_text())
    data["cells"][0]["cell_type"] = "markdown"
    data["cells"][0]["source"] = ["**Learning goals:** learn\\n", "## Checkpoint\\n"]
    path.write_text(json.dumps(data))
    monkeypatch.setattr(notebook_audit, "SCHISM_JOURNEY", [path])
    failures = notebook_audit.audit_schism_journey(tmp_path)
    assert any("missing Prerequisites" in item for item in failures)
    assert any("missing Execution contract" in item for item in failures)


def test_audit_xbeach_journey_detects_missing_step(tmp_path, monkeypatch):
    paths = [
        tmp_path / "notebooks" / "xbeach" / "journey_01_first.ipynb",
        tmp_path / "notebooks" / "xbeach" / "journey_02_second.ipynb",
    ]
    paths[0].parent.mkdir(parents=True)
    for path in paths:
        write_notebook(path)
        data = json.loads(path.read_text())
        data["cells"][0]["cell_type"] = "markdown"
        data["cells"][0]["source"] = [
            "# Lesson\n",
            "**Learning goals:** learn\n",
            "**Prerequisites:** Python\n",
            "**Execution contract:** render-only\n",
            "## Checkpoint\n",
        ]
        path.write_text(json.dumps(data))
    monkeypatch.setattr(notebook_audit, "XBEACH_JOURNEY", paths)
    failures = notebook_audit.audit_xbeach_journey(tmp_path)
    assert any("missing next link" in item for item in failures)


def test_audit_xbeach_journey_detects_missing_execution_context(tmp_path, monkeypatch):
    path = tmp_path / "notebooks" / "xbeach" / "journey_01_only.ipynb"
    path.parent.mkdir(parents=True)
    write_notebook(path)
    data = json.loads(path.read_text())
    data["cells"][0]["cell_type"] = "markdown"
    data["cells"][0]["source"] = ["**Learning goals:** learn\n", "## Checkpoint\n"]
    path.write_text(json.dumps(data))
    monkeypatch.setattr(notebook_audit, "XBEACH_JOURNEY", [path])
    failures = notebook_audit.audit_xbeach_journey(tmp_path)
    assert any("missing Prerequisites" in item for item in failures)
    assert any("missing Execution contract" in item for item in failures)


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
