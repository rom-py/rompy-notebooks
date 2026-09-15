## Context

The standard build currently stages notebooks, audits their structure, and renders them without execution. A separate executed-docs target exists, but selection and evidence boundaries need to be explicit. Model binaries, MPI, Docker, external data, and credentials must remain optional.

## Goals / Non-Goals

**Goals:**

- Define stable validation tiers and commands.
- Select lightweight notebooks using metadata.
- Produce clear pass/fail results with execution mode and environment scope.
- Keep normal docs CI independent of model binaries and network access.

**Non-Goals:**

- Running full scientific model validation in ordinary CI.
- Claiming scientific correctness from notebook execution.
- Automatically downloading external fixtures during render-only builds.

## Decisions

1. Keep Tier 1 audit and Tier 2 render-only build as the default quality gate.
2. Use explicit notebook metadata for lightweight execution eligibility and runtime dependency declarations.
3. Keep model-runtime checks as separately invoked, environment-specific targets.
4. Write execution reports outside source notebooks and clearly label them as current-run evidence.
5. Fail closed when a selected notebook has unmet prerequisites rather than silently skipping it.

## Risks / Trade-offs

- [Environment drift] A notebook can pass in one environment and fail in another → report Python/plugin versions and environment tier.
- [Fixture/network dependence] Lightweight examples may need data → require local fixtures or explicit opt-in acquisition.
- [False confidence] Execution can pass while science is unsuitable → repeat scientific-validation caveats in reports and docs.
- [CI cost] Runtime suites can be expensive → keep them opt-in or scheduled.

## Migration Plan

1. Add execution eligibility and runtime metadata to notebooks.
2. Extract selection and reporting into a dependency-light script.
3. Add Makefile commands for selected execution and optional runtime validation.
4. Update CI and workflow documentation to invoke only default tiers.
5. Validate all tiers with representative notebooks and preserve existing commands.
