## Why

The documentation site currently exposes the same notebooks through four overlapping entry points: Notebook Gallery, Discover notebooks, model pages, and the Notebooks sidebar. Their inventories and presentation differ, which makes the site feel inconsistent and forces users to guess which route is authoritative.

## What Changes

- Replace the overlapping top-level notebook entry points with a small, logical information architecture.
- Make learning journeys the primary path for newcomers.
- Make one metadata-backed Notebook Catalogue the authoritative reference index.
- Remove the duplicate curated gallery and duplicate Notebooks sidebar catalogue.
- Keep model pages focused on scope, coverage, and recommended journeys rather than repeating every notebook.
- Group installation, usage, execution, conventions, and coverage under Guides.
- Use human-readable notebook titles in generated catalogue views while retaining stable metadata IDs internally.
- Preserve direct notebook download links and model-specific lesson navigation.

## Capabilities

### New Capabilities

- `documentation-information-architecture`: A clear top-level documentation hierarchy with distinct learning, reference, and guide roles.
- `authoritative-notebook-catalogue`: One complete metadata-backed catalogue used as the reference inventory for published notebooks.

### Modified Capabilities

<!-- No existing main specs are currently available; this change consolidates the recently implemented navigation behavior. -->

## Impact

- `mkdocs.yml` navigation and generated documentation pages.
- `docs/index.md`, `docs/gallery.md`, model overview pages, and guide pages.
- Notebook inventory and discoverability generation under `scripts/`.
- Notebook audit checks and documentation tests.
- Existing notebook URLs should remain stable where practical; removed index routes require clear replacement links.
