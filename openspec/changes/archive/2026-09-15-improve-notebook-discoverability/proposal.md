## Why

The site now contains coherent SWAN, XBeach, and SCHISM journeys, but discovery still depends on manually maintained navigation and filenames. A shared metadata-driven inventory will let users find notebooks by model, learning level, topic, or execution requirements while making omissions and navigation drift visible.

## What Changes

- Define a consistent metadata contract for every published notebook.
- Build a validated notebook inventory from notebook metadata.
- Generate model indexes and capability/topic views from that inventory where practical.
- Add explicit previous/next links to ordered learning journeys.
- Reconcile the gallery, sidebar navigation, and audit report against the same inventory.
- Report notebooks that are missing metadata, unlisted, or intentionally excluded.
- Preserve manual editorial control for ordering, grouping, and explanatory landing pages.

## Capabilities

### New Capabilities

- `notebook-inventory`: Discoverable, validated metadata inventory for notebooks and their publication status.
- `generated-notebook-navigation`: Metadata-backed indexes, capability views, and journey previous/next navigation.

### Modified Capabilities

<!-- No existing requirements are changed; this adds discoverability capabilities around the existing documentation site. -->

## Impact

- Notebook metadata in `notebooks/`.
- Documentation generation and audit scripts under `scripts/`.
- MkDocs configuration, navigation, templates, and generated documentation pages.
- Tests covering metadata validation, inventory consistency, and generated navigation.
- No model APIs or scientific processing behavior changes.
