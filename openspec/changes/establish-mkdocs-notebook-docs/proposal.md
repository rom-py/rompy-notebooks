## Why

The notebook repository has no local documentation build or automated quality gate, while the main `rompy` documentation imports these notebooks during its MkDocs build. As a result, stale links, malformed notebooks, empty files, stored execution errors, and missing assets can remain unnoticed until the downstream documentation build runs.

This change establishes a local, reproducible documentation and audit baseline before larger notebook repairs or upstream documentation work begin.

## What Changes

- Add a local MkDocs site presenting the notebooks as a navigable gallery grouped by model and topic.
- Add the dependencies and developer instructions required to build and preview the site locally.
- Add structural notebook checks for valid JSON, empty notebooks, checkpoint/generated files, stored error outputs, and documentation links/assets.
- Add a documentation build check using strict MkDocs validation.
- Audit and safely clean repository-owned documentation defects, including stale references and the tracked empty SCHISM notebook, without deleting user-generated working-tree files.
- Record execution-heavy or externally dependent notebooks as such rather than pretending that rendering validates model execution.
- Keep notebook execution validation as a separate follow-up concern, with a small smoke-test foundation where it can be done without requiring model binaries or remote services.

## Capabilities

### New Capabilities

- `notebook-documentation-site`: A local MkDocs site that renders and organizes the repository notebooks and supporting documentation.
- `notebook-quality-gate`: Automated structural and documentation checks that detect common notebook and site-integrity failures.

### Modified Capabilities

<!-- No existing OpenSpec capabilities are present. -->

## Impact

- Adds MkDocs configuration, documentation pages, and documentation/build dependencies to this repository.
- Adds test or validation tooling covering notebook structure and site integrity.
- Removes or corrects repository-owned stale/empty documentation inputs where confirmed by the audit.
- Establishes a contract for the main `rompy` repository to consume a known-good notebook tree; upstream workflow changes are intentionally deferred to a later change.
- Does not execute SWAN, XBeach, or SCHISM model binaries as part of the initial documentation build.
