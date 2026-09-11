## ADDED Requirements

### Requirement: Notebook structure validation
The quality gate SHALL validate every tracked source notebook and SHALL report invalid JSON, zero-byte notebooks, unsupported/missing notebook metadata where required, and stored error outputs.

#### Scenario: Invalid notebook is present
- **WHEN** a tracked notebook cannot be parsed as notebook JSON
- **THEN** the quality gate fails and identifies the notebook and parse failure

#### Scenario: Stored execution error is present
- **WHEN** a notebook contains an error output from a prior execution
- **THEN** the quality gate fails and identifies the notebook and affected cell

### Requirement: Repository hygiene validation
The quality gate SHALL reject checkpoint files, Python caches, and generated documentation staging content from the tracked documentation source set, while preserving unrelated user working-tree files.

#### Scenario: Checkpoint appears in source inventory
- **WHEN** a checkpoint notebook is discovered under the source notebook tree
- **THEN** it is excluded from staging and the check reports it as ignored or actionable according to the documented policy

#### Scenario: Empty tracked notebook is present
- **WHEN** a tracked notebook has no content
- **THEN** the quality gate fails until it is restored, intentionally removed, or explicitly allowlisted with a documented reason

### Requirement: Documentation integrity validation
The quality gate SHALL verify that navigation and local documentation links to notebooks and assets resolve within the staged site.

#### Scenario: Documentation links to missing content
- **WHEN** a local documentation link points to a missing notebook or asset
- **THEN** validation fails and reports the referring page and missing target

#### Scenario: All local targets resolve
- **WHEN** every local navigation and asset reference resolves
- **THEN** the documentation integrity check passes

### Requirement: CI and developer entry points
The repository SHALL expose one documented command for the combined structural checks and strict documentation build, and CI SHALL run that same command.

#### Scenario: Combined validation passes
- **WHEN** a clean checkout satisfies notebook checks and MkDocs strict build requirements
- **THEN** the documented validation command exits successfully

#### Scenario: Validation failure is actionable
- **WHEN** any structural, link, or build check fails
- **THEN** the command exits non-zero and reports the relevant file and failure category
