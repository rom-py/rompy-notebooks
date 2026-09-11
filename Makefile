.PHONY: docs-stage docs-build docs-serve notebook-audit test

PYTHON ?= python

notebook-audit: docs-stage
	$(PYTHON) scripts/notebook_audit.py

docs-stage:
	$(PYTHON) scripts/sync_docs.py

docs-build: docs-stage notebook-audit
	mkdocs build --strict

docs-serve: docs-stage
	mkdocs serve

test: notebook-audit
	pytest -q
