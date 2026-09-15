## ADDED Requirements

### Requirement: Notebook execution is metadata-selected
The selected execution command SHALL execute only notebooks explicitly marked as eligible and SHALL support selecting one notebook or a named execution group.

#### Scenario: Eligible notebook selection
- **WHEN** a notebook is marked lightweight and selected
- **THEN** it executes in a staged or temporary copy without modifying the source notebook

#### Scenario: Runtime-dependent notebook omitted
- **WHEN** a notebook requires a model binary or MPI and is not selected for runtime validation
- **THEN** the default selected execution command does not execute it

### Requirement: Execution prerequisites are enforced
The execution command SHALL report unmet prerequisites and fail clearly rather than silently treating an omitted notebook as passed.

#### Scenario: Missing dependency
- **WHEN** a selected notebook cannot import a declared dependency
- **THEN** execution reports the notebook and missing prerequisite as a failure
