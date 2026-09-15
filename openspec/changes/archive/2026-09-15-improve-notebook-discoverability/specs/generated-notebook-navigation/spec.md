## ADDED Requirements

### Requirement: Model and topic indexes expose published notebooks
The documentation site SHALL provide generated views that list published notebooks by model and topic, including title, level, prerequisites, execution requirements, and a link to the notebook page.

#### Scenario: Browse a model index
- **WHEN** a user opens a model index
- **THEN** the page lists the published notebooks for that model with their learning metadata and links

#### Scenario: Browse a capability topic
- **WHEN** a user selects a topic represented by published notebooks
- **THEN** the site shows the matching notebooks across supported models

### Requirement: Ordered journeys provide previous and next links
Each published notebook belonging to an ordered learning journey SHALL expose links to its previous and next lessons when those lessons exist.

#### Scenario: Middle journey lesson
- **WHEN** a user views a lesson with both earlier and later lessons
- **THEN** the page provides working previous and next links in journey order

#### Scenario: First or last journey lesson
- **WHEN** a user views the first or last lesson
- **THEN** the page provides only the link that exists and does not render a broken counterpart

### Requirement: Generated links resolve to published pages
Generated indexes and journey links SHALL resolve to documentation pages represented in the current inventory and SHALL not link to excluded or missing notebooks.

#### Scenario: Excluded notebook
- **WHEN** a notebook is excluded from publication
- **THEN** it does not appear in generated indexes or journey navigation

#### Scenario: Stale link detection
- **WHEN** generation encounters a link target absent from the published inventory
- **THEN** the documentation quality check reports the source record and target rather than silently emitting a broken link
