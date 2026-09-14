## 1. Metadata and inventory

- [ ] 1.1 Audit current notebook metadata and define the normalized metadata schema
- [ ] 1.2 Add or normalize publication, identifier, model, kind, level, topics, prerequisites, and execution metadata across published notebooks
- [ ] 1.3 Implement a deterministic notebook inventory parser and validator
- [ ] 1.4 Add exclusion reasons and publication-drift diagnostics for experiments and legacy notebooks

## 2. Generated discoverability views

- [ ] 2.1 Generate model and topic index data from the validated inventory
- [ ] 2.2 Add generated model/topic reference pages to the documentation build
- [ ] 2.3 Add ordered journey metadata and previous/next links
- [ ] 2.4 Validate that generated links target published, existing documentation pages

## 3. Integration and quality gates

- [ ] 3.1 Reconcile gallery, curated navigation, and inventory coverage
- [ ] 3.2 Extend notebook audit tests for metadata, inventory determinism, exclusions, and stale paths
- [ ] 3.3 Integrate inventory validation into the standard documentation quality gate
- [ ] 3.4 Update contributor and documentation workflow guidance with metadata conventions

## 4. Verification

- [ ] 4.1 Run notebook audit and the complete test suite
- [ ] 4.2 Run render-only and executed documentation builds
- [ ] 4.3 Review generated model/topic indexes and journey navigation visually
