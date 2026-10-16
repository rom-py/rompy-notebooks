## ADDED Requirements

### Requirement: Validation tiers are independently identifiable
The project SHALL identify structural audit, render-only build, selected notebook execution, and model-runtime validation as separate tiers with distinct prerequisites and evidence.

#### Scenario: Default quality gate
- **WHEN** a contributor runs the standard test or documentation build
- **THEN** only structural and render-only tiers are required

#### Scenario: Optional runtime tier
- **WHEN** a contributor requests model-runtime validation
- **THEN** the command identifies its model environment and does not change the default gate

### Requirement: Reports distinguish current execution from stored output
Validation reports SHALL identify whether results came from the current run or stored notebook output and SHALL state that execution is not scientific validation.

#### Scenario: Executed notebook report
- **WHEN** a selected notebook executes successfully
- **THEN** the report records current-run status, execution scope, environment, and the scientific-validation limitation
