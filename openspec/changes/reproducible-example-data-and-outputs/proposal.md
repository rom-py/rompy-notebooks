## Why

The notebooks now generate realistic model inputs, but their data provenance, fixture acquisition, and output handling are not yet uniform. Users need a reliable way to understand what can be reproduced locally, what requires optional downloads, and which generated files are transient or illustrative.

## What Changes

- Define a compact fixture and provenance contract for data-driven examples.
- Add a documented, explicit fixture acquisition command without making render-only builds dependent on network access.
- Standardize temporary/ignored output workspaces and generated artefact reporting.
- Record fixture, Rompy/plugin, execution-tier, and limitation metadata in reproducibility reports.
- Add output-policy guidance distinguishing committed, regenerated, and ignored artefacts.

## Capabilities

### New Capabilities

- `example-data-provenance`: Versioned fixture manifests, acquisition instructions, and provenance reporting.
- `reproducible-output-workspaces`: Deterministic example output locations and artefact policy reporting.

### Modified Capabilities

<!-- No existing main specs are currently available. -->

## Impact

- `data/`, fixture helper scripts, notebook metadata, and documentation workflow guidance.
- Makefile targets and tests for acquisition, provenance, and output hygiene.
- No model runtime or scientific validation requirements become mandatory.
