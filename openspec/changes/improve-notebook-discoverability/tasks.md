## 1. Metadata and inventory

- [x] 1.1 Audit current notebook metadata and define the normalized metadata schema
- [x] 1.2 Add or normalize publication, identifier, model, kind, level, topics, prerequisites, and execution metadata across published notebooks
- [x] 1.3 Implement a deterministic notebook inventory parser and validator
- [x] 1.4 Add exclusion reasons and publication-drift diagnostics for experiments and legacy notebooks

## 2. Generated discoverability views

- [x] 2.1 Generate model and topic index data from the validated inventory
- [x] 2.2 Add generated model/topic reference pages to the documentation build
- [x] 2.3 Add ordered journey metadata and previous/next links
- [x] 2.4 Validate that generated links target published, existing documentation pages

## 3. Integration and quality gates

- [x] 3.1 Reconcile gallery, curated navigation, and inventory coverage
- [x] 3.2 Extend notebook audit tests for metadata, inventory determinism, exclusions, and stale paths
- [x] 3.3 Integrate inventory validation into the standard documentation quality gate
- [x] 3.4 Update contributor and documentation workflow guidance with metadata conventions

## 4. Verification

- [x] 4.1 Run notebook audit and the complete test suite
- [x] 4.2 Run render-only and executed documentation builds
- [x] 4.3 Review generated model/topic indexes and journey navigation visually
