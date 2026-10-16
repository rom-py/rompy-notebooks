## ADDED Requirements

### Requirement: Example data has a machine-readable provenance manifest
The repository SHALL provide a versioned manifest for example fixtures and external datasets containing an identifier, source, version or release, variables/scope, and acquisition status.

#### Scenario: Inspect fixture provenance
- **WHEN** a user reads the example-data manifest
- **THEN** they can identify the source, version, scope, and whether the data is local or acquired

### Requirement: Acquisition is explicit and optional
Fixture acquisition SHALL be a separately invoked command and SHALL NOT run during render-only documentation builds.

#### Scenario: Offline documentation build
- **WHEN** a user runs the standard documentation build without acquired fixtures
- **THEN** the build does not attempt network access or fail solely because optional data is absent

#### Scenario: Explicit acquisition
- **WHEN** a user invokes the acquisition command
- **THEN** the command reports each requested fixture and fails clearly on unavailable sources or missing credentials
