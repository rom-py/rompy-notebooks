## ADDED Requirements

### Requirement: Local documentation site
The repository SHALL provide a MkDocs site that can be built locally from a clean checkout and SHALL include an index, setup guidance, audit status, and links to the repository's existing notebook groups.

#### Scenario: Build the local site
- **WHEN** a contributor runs the documented documentation build command in a supported environment
- **THEN** MkDocs produces a site without configuration errors

#### Scenario: Preview the local site
- **WHEN** a contributor runs the documented preview command
- **THEN** a local MkDocs development server starts with the notebook gallery available

### Requirement: Notebook staging
The documentation workflow SHALL stage the selected source notebooks and their required local assets under the generated documentation tree before building the site.

#### Scenario: Stage source notebooks
- **WHEN** the documentation build workflow starts
- **THEN** existing source notebooks are copied into the staging tree using paths that preserve their documented relative assets

#### Scenario: Exclude generated notebook files
- **WHEN** the staging tree is created
- **THEN** checkpoint directories, Python caches, and explicitly excluded generated run artifacts are absent from the staged documentation

### Requirement: Curated notebook navigation
The site SHALL provide navigation grouped by common, backend, SWAN, SCHISM, and XBeach content, and SHALL link only to notebook paths that exist in the staged tree.

#### Scenario: Navigate the notebook gallery
- **WHEN** a user opens the notebook gallery
- **THEN** the site presents model/topic groupings and links to the corresponding existing notebooks

#### Scenario: Missing source is detected
- **WHEN** a navigation entry refers to a notebook that is not staged
- **THEN** the documentation validation fails with the missing path identified

### Requirement: Render-only documentation contract
The MkDocs notebook plugin SHALL render notebooks without executing model code, and the documentation shall state that a successful site build is not evidence of successful model execution.

#### Scenario: Build without model runtimes
- **WHEN** a contributor builds documentation without SWAN, XBeach, or SCHISM executables
- **THEN** the documentation build does not attempt to run those model binaries

#### Scenario: Explain execution status
- **WHEN** a user reads the local documentation site
- **THEN** the site identifies render-only notebooks and points to separate execution validation where available
