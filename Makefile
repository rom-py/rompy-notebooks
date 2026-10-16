.PHONY: docs-stage docs-build docs-serve docs-build-executed docs-serve-executed execute-docs execute-docs-selected validate-runtime runtime-swan runtime-xbeach runtime-schism example-data notebook-audit test

PYTHON ?= python

notebook-audit: docs-stage
	$(PYTHON) scripts/notebook_audit.py

example-data:
	$(PYTHON) scripts/example_data.py

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
	$(PYTHON) scripts/execute_docs_notebooks.py --report .cache/selected-execution.json

execute-docs-selected: execute-docs

# Model-runtime checks are intentionally opt-in and environment-specific.
validate-runtime: docs-stage
	$(PYTHON) scripts/execute_docs_notebooks.py --include-runtime --report .cache/runtime-execution.json

runtime-swan:
	$(PYTHON) scripts/runtime_preflight.py swan

runtime-xbeach:
	$(PYTHON) scripts/runtime_preflight.py xbeach

runtime-schism:
	$(PYTHON) scripts/runtime_preflight.py schism

test: notebook-audit
	pytest -q
