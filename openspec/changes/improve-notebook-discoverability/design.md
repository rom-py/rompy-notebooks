## Context

The repository contains notebooks across common, SWAN, XBeach, and SCHISM collections. MkDocs navigation and the gallery are currently curated separately, while `scripts/notebook_audit.py` performs structural checks. Notebook metadata already exists in cell metadata, but it is not yet a single source of truth for publication, grouping, or journey order.

The design must preserve manual landing pages and editorial descriptions, avoid executing notebooks during normal builds, and keep generated artefacts out of source control.

## Goals / Non-Goals

**Goals:**

- Establish one parseable inventory for published notebooks.
- Validate metadata before documentation generation.
- Generate discoverability pages and journey links without replacing editorial navigation entirely.
- Make missing metadata and inventory drift actionable in tests and audit output.

**Non-Goals:**

- Replacing MkDocs or `mkdocs-jupyter`.
- Automatically publishing every notebook in the repository.
- Changing notebook scientific content or model APIs.
- Adding external search infrastructure.

## Decisions

1. **Use notebook cell metadata as the source of truth.** Existing `rompy_notebooks` metadata travels with each notebook and is visible to tooling. A separate YAML catalogue would duplicate facts and drift. A small metadata parser will normalize model, kind, level, topics, prerequisites, execution requirements, and publication status.

2. **Keep an explicit publication flag.** Notebooks used as experiments, fixtures, or legacy examples must not become public navigation accidentally. Published notebooks SHALL opt in through metadata; excluded notebooks can carry an exclusion reason for audit visibility.

3. **Generate an inventory artifact before MkDocs.** A script will scan notebooks, validate metadata, and emit a deterministic JSON (or equivalent) inventory used by index/navigation generation. The normal render-only build remains the default.

4. **Generate supporting pages, not the entire site nav.** Model indexes and capability/topic listings can be generated from the inventory, while journey ordering and explanatory pages remain explicitly curated in `mkdocs.yml`. This balances consistency with editorial control.

5. **Add journey links through generated notebook context or markdown.** Previous/next links SHALL use the ordered journey metadata and resolve to published notebook pages. The implementation may use a MkDocs hook/template rather than modifying notebook cells, so source notebooks remain clean.

## Risks / Trade-offs

- [Metadata drift] Notebooks can still be edited without updating metadata → enforce the inventory validator in the quality gate and CI.
- [Navigation duplication] Generated indexes may overlap curated pages → define generated pages as reference views and retain curated journey landing pages.
- [Path instability] Renaming notebooks can break links → validate unique IDs and report changed/missing paths.
- [Template coupling] Journey links may depend on Material/MkDocs internals → keep link generation in a small plugin/hook with a render-only fallback.

## Migration Plan

1. Inventory current notebooks and classify published versus excluded files.
2. Add/normalize metadata without changing notebook execution behavior.
3. Implement parser, validator, and tests.
4. Generate model/topic indexes and journey links.
5. Wire inventory validation into the existing audit and documentation checks.
6. Roll back by disabling generated pages/hooks; notebook content and existing curated navigation remain usable.
