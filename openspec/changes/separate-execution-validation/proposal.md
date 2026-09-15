## Why

The repository now has rich notebooks and generated model inputs, but documentation rendering, notebook execution, and model-runtime validation are different activities. Treating them as one build makes failures ambiguous and risks implying that rendered or structurally checked examples have been scientifically or operationally validated.

## What Changes

- Define explicit validation tiers for notebooks and model workflows.
- Keep structural audits and render-only documentation builds mandatory and lightweight.
- Add an opt-in lightweight execution path for selected notebooks.
- Define environment-specific model-runtime checks for SWAN, XBeach, and SCHISM without making them default CI requirements.
- Record execution scope, prerequisites, and results distinctly from rendered documentation.
- Ensure stored notebook outputs are not treated as current execution evidence.

## Capabilities

### New Capabilities

- `execution-validation-tiers`: Explicit, independently runnable validation levels and reporting semantics.
- `selected-notebook-execution`: Controlled execution of notebooks selected by metadata without executing model binaries by default.

### Modified Capabilities

<!-- No existing main specs are currently available. -->

## Impact

- Makefile targets and CI workflows.
- Notebook metadata and execution selection logic.
- Audit and execution scripts under `scripts/`.
- Documentation workflow guidance and validation reports.
- Optional model-specific environments; no new default runtime dependency.
