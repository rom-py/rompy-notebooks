## ADDED Requirements

### Requirement: Generated example outputs use isolated workspaces
Example processing SHALL write generated artefacts to temporary or explicitly ignored workspaces and SHALL not modify source notebooks or commit transient outputs.

#### Scenario: Generate example outputs
- **WHEN** a notebook or helper generates model inputs
- **THEN** outputs are written under an isolated workspace and the source notebook remains unchanged

### Requirement: Output reports identify artefacts and reproducibility scope
The example workflow SHALL produce or display a report listing generated artefacts, their locations, execution tier, environment versions, and whether each artefact is committed, regenerated, or ignored.

#### Scenario: Review a generated report
- **WHEN** a user inspects an example output report
- **THEN** they can distinguish current generated files from stored notebook output and understand the reproduction limitations
