.PHONY: docs-stage docs-build docs-serve docs-build-executed docs-serve-executed execute-docs notebook-audit test

PYTHON ?= python

notebook-audit: docs-stage
	$(PYTHON) scripts/notebook_audit.py

docs-stage:
	$(PYTHON) scripts/sync_docs.py
	$(PYTHON) scripts/notebook_inventory.py --output docs/generated/notebook-inventory.json
	$(PYTHON) scripts/discoverability.py

docs-build: docs-stage notebook-audit
	mkdocs build --strict

docs-build-executed: docs-stage notebook-audit
	$(PYTHON) scripts/execute_docs_notebooks.py
	mkdocs build --strict

docs-serve: docs-stage
	mkdocs serve

docs-serve-executed: docs-stage
	$(PYTHON) scripts/execute_docs_notebooks.py
	mkdocs serve

execute-docs: docs-stage
	$(PYTHON) scripts/execute_docs_notebooks.py

test: notebook-audit
	pytest -q
