## ADDED Requirements

### Requirement: Top-level navigation has distinct user purposes
The documentation site SHALL expose distinct top-level areas for starting guidance, learning journeys, the notebook catalogue, and operational guides, without duplicating a complete notebook list in multiple areas.

#### Scenario: User opens the site navigation
- **WHEN** the user views the top-level navigation
- **THEN** each entry has one clear purpose and no duplicate Gallery, Discover, or Notebooks catalogue entries are present

### Requirement: Model pages orient users without duplicating catalogues
Each model overview SHALL explain model coverage and link to its recommended journey and catalogue view without reproducing the complete notebook inventory.

#### Scenario: User opens a model overview
- **WHEN** the user selects a model overview
- **THEN** the page provides scope, coverage, recommended learning path, and links to relevant catalogue views

### Requirement: Existing notebook routes remain usable
Navigation consolidation SHALL preserve direct notebook page routes and provide replacement links for any removed catalogue landing page.

#### Scenario: User follows an existing notebook URL
- **WHEN** the user opens a previously published notebook route
- **THEN** the notebook page remains available with its download and journey navigation controls
