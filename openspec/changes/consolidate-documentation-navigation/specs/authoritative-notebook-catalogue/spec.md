## ADDED Requirements

### Requirement: One catalogue is the complete notebook reference
The notebook catalogue SHALL be generated from the validated inventory and SHALL include every published notebook exactly once in its complete view.

#### Scenario: Catalogue completeness
- **WHEN** the catalogue is generated from the inventory
- **THEN** every published inventory record appears in the complete catalogue and no excluded record appears

### Requirement: Catalogue views share one inventory
Model and topic catalogue views SHALL be filtered views of the same inventory and SHALL use consistent titles, links, and metadata presentation.

#### Scenario: Notebook appears in multiple filters
- **WHEN** a published notebook matches a model and several topics
- **THEN** every matching view links to the same notebook page and presents the same title and metadata

### Requirement: Catalogue labels are human-readable
Generated catalogue views SHALL display human-readable notebook titles while retaining stable IDs for validation and link identity.

#### Scenario: Stable identifier is internal
- **WHEN** a catalogue entry is rendered
- **THEN** the visible label is a readable title rather than a path-derived technical identifier
