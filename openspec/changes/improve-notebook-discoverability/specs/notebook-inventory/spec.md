## ADDED Requirements

### Requirement: Published notebooks declare discoverability metadata
The inventory system SHALL recognize a notebook as published only when its metadata declares a stable identifier, model, kind, level, and topic list.

#### Scenario: Valid published notebook
- **WHEN** a notebook contains complete discoverability metadata
- **THEN** the inventory includes it with its normalized metadata and source path

#### Scenario: Missing required metadata
- **WHEN** a notebook is marked for publication but omits a required field
- **THEN** inventory validation reports the notebook path and missing field and fails the quality gate

### Requirement: Inventory classification is deterministic
The inventory generator SHALL produce deterministic records sorted by stable identifier and SHALL distinguish published, excluded, and invalid notebooks.

#### Scenario: Repeated inventory generation
- **WHEN** the generator scans the same repository state twice
- **THEN** it produces equivalent records and ordering

#### Scenario: Intentionally excluded notebook
- **WHEN** a notebook declares that it is excluded with a reason
- **THEN** the inventory omits it from published views and records the exclusion reason for audit reporting

### Requirement: Inventory detects publication drift
The quality checks SHALL report published notebooks that are not represented by the documentation inventory and inventory entries whose source paths no longer exist.

#### Scenario: Unlisted published notebook
- **WHEN** a published notebook is absent from the generated inventory or documentation mapping
- **THEN** validation reports the notebook as publication drift

#### Scenario: Missing inventory source
- **WHEN** an inventory record points to a removed or renamed notebook
- **THEN** validation fails and identifies the stale source path
