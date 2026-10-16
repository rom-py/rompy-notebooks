## Context

Examples use both local test fixtures and externally acquired model data. Documentation must remain render-only and offline-capable, while executed examples need a predictable fixture and output contract. Existing helpers already use temporary directories and explicit acquisition in several lessons, but there is no repository-wide manifest or report.

## Goals / Non-Goals

**Goals:**

- Make data provenance discoverable and machine-readable.
- Make fixture acquisition explicit and repeatable.
- Keep generated outputs isolated from source notebooks and Git.
- Report enough environment and source information to reproduce an example.

**Non-Goals:**

- Bundling large scientific datasets.
- Hiding network or credential requirements.
- Guaranteeing scientific validity or model skill.
- Committing every generated file.

## Decisions

1. Use a versioned manifest under `data/` describing fixture names, sources, releases, checksums where available, and acquisition commands.
2. Provide an explicit acquisition command; never acquire data from render-only MkDocs targets.
3. Use named temporary/cache directories for generated outputs and write a deterministic JSON report listing artefacts and policy (`committed`, `regenerated`, or `ignored`).
4. Keep notebook metadata declarative and let reports capture actual environment/plugin versions at execution time.
5. Prefer small local fixtures for tests and examples; document external fixtures as optional inputs with honest fallbacks.

## Risks / Trade-offs

- [Source changes] Remote releases can disappear → record immutable release URLs/checksums and retain a small fallback fixture where feasible.
- [Large outputs] Generated model files can consume disk → use temporary directories and report sizes without committing them.
- [Reproducibility drift] Dependency updates alter outputs → report versions and use structural assertions rather than byte-for-byte scientific claims.
- [Credential leakage] Acquisition commands may require credentials → document environment variables without storing secrets.

## Migration Plan

1. Inventory current fixtures and external data references.
2. Add the manifest and provenance/acquisition helper.
3. Standardize example output reporting and ignore rules.
4. Update representative notebooks and workflow docs.
5. Add tests and run all documentation/selected-execution checks.
