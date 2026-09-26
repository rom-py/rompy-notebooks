.PHONY: docs-stage docs-build docs-serve docs-build-executed docs-serve-executed docs-build-figures docs-serve-figures execute-docs execute-docs-selected execute-docs-figures validate-runtime runtime-swan runtime-xbeach runtime-schism example-data notebook-audit test

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

docs-build-figures: docs-stage notebook-audit
	$(PYTHON) scripts/execute_docs_notebooks.py --group figures
	mkdocs build --strict

docs-serve-figures: docs-stage
	$(PYTHON) scripts/execute_docs_notebooks.py --group figures
	mkdocs serve

execute-docs: docs-stage
	$(PYTHON) scripts/execute_docs_notebooks.py --report .cache/selected-execution.json

execute-docs-selected: execute-docs

execute-docs-figures: docs-stage
	$(PYTHON) scripts/execute_docs_notebooks.py --group figures --report .cache/figures-execution.json

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
