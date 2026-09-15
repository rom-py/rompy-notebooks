## Context

The current MkDocs site has manually curated model navigation, a curated gallery, a generated catalogue, and a second Notebooks sidebar. The same notebook can therefore appear with different labels and coverage in several places. The metadata inventory is useful, but it should support one reference catalogue rather than become another competing entry point.

## Goals / Non-Goals

**Goals:**

- Establish five clear top-level areas: Home, Start here, Learning journeys, Notebook catalogue, and Guides.
- Keep model pages as orientation and coverage pages.
- Generate one complete catalogue from the inventory, with model/topic views as subsections of that catalogue.
- Preserve stable notebook routes, download buttons, and journey navigation.
- Add checks preventing duplicate catalogue navigation and incomplete catalogue generation.

**Non-Goals:**

- Redesigning notebook content or model APIs.
- Removing useful model landing pages.
- Adding faceted client-side search beyond MkDocs search and generated views.
- Requiring every notebook to be a journey lesson.

## Decisions

1. **Use one catalogue, not multiple lists.** The generated inventory is authoritative for notebook completeness. The former gallery becomes a short orientation page or is removed from navigation; it must not maintain a competing list.

2. **Use model pages for orientation.** Model pages will describe coverage, prerequisites, and recommended paths, linking to journeys and catalogue filters instead of reproducing all notebook links.

3. **Keep journeys explicit and ordered.** Journey landing pages and lesson order remain editorial because sequencing is pedagogical. Generated previous/next controls continue to derive from metadata.

4. **Group non-notebook material under Guides.** Installation, usage, execution, conventions, and audit/coverage material are operational guides rather than notebook discovery surfaces.

5. **Use human-readable labels from metadata or curated title fields.** Stable IDs remain implementation identifiers and are not displayed as page titles.

## Risks / Trade-offs

- [Deep links] Removing old index pages can surprise users → retain pages as redirects or concise replacement pages where practical.
- [Manual drift] Model landing pages can become stale → audit links and catalogue coverage in tests.
- [Over-generation] A catalogue can become overwhelming → group by model and topic and keep the top-level catalogue landing page explanatory.
- [URL changes] Generated page paths can change → preserve current notebook route structure and use stable generated page names.

## Migration Plan

1. Define the final top-level navigation and classify current pages.
2. Remove duplicate gallery and Notebooks sidebar lists, replacing them with links into the single catalogue.
3. Simplify model overview pages and retain journey links.
4. Update generated catalogue labels and add an all-notebooks view if needed.
5. Add navigation and coverage tests, then run both documentation build modes.
6. Roll back by restoring the previous `mkdocs.yml` navigation; notebook files and generated inventory remain unaffected.
