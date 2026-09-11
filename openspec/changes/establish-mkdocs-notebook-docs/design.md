## Context

`rompy-notebooks` contains the source notebooks consumed by the main `rompy` documentation build. The notebook repository currently has no site configuration, no documented local preview workflow, and almost no automated checks. The downstream build copies the notebook tree and renders stored outputs without executing notebook code.

The initial solution must improve visibility and detect repository/documentation defects without requiring SWAN, XBeach, or SCHISM binaries, Docker, MPI, remote catalogs, or model-specific data services. Existing uncommitted working-tree files are user work and are outside the cleanup scope.

## Goals / Non-Goals

**Goals:**

- Provide a local MkDocs site with a curated, model-oriented notebook gallery.
- Make rendering and strict site validation reproducible from a clean checkout.
- Add fast checks for notebook structure and known repository hygiene problems.
- Keep generated documentation artifacts out of the source tree and exclude checkpoints.
- Correct confirmed repository-owned defects discovered in the audit.
- Make the boundary between documentation rendering and actual notebook/model execution explicit.

**Non-Goals:**

- Running full numerical models during the MkDocs build.
- Pinning or redesigning all rompy ecosystem dependencies in this change.
- Repairing every notebook or guaranteeing that every notebook executes.
- Changing the main `rompy` repository or its deployment workflow.
- Removing or rewriting uncommitted user-generated files.

## Decisions

1. **Use MkDocs with Material and mkdocs-jupyter.** This matches the main repository and provides a useful local preview while allowing notebooks to be rendered with stored outputs. Sphinx is not selected because it would create a second documentation technology and would not align with the downstream site.

2. **Use a generated documentation staging tree.** A small sync command will copy the selected repository notebooks and required assets into a generated `docs/notebooks/` tree before MkDocs runs. Checkpoints, caches, and known generated run directories will be excluded. This avoids duplicating notebooks in Git while keeping MkDocs' `docs_dir` model straightforward.

3. **Provide explicit commands rather than hiding work in MkDocs hooks.** `make docs-build`/a documented script will sync sources and run `mkdocs build --strict`; `make docs-serve` will sync and start the preview server. CI will invoke the same build path. Direct `mkdocs build` may be documented as unsupported unless the staging tree is already present.

4. **Separate rendering from execution.** The documentation build will use `execute: false`. Structural checks will inspect JSON and stored outputs, while lightweight execution tests remain a separate follow-up. This prevents expensive or environment-dependent model runs from blocking documentation publication.

5. **Prefer an explicit inventory/navigation page.** Navigation will list existing notebooks only, and the inventory/check will detect links to missing notebook paths. This avoids silently carrying forward the stale filenames currently referenced by upstream documentation.

6. **Make cleanup conservative and evidence-based.** The change will remove the tracked zero-byte SCHISM notebook and prevent checkpoint/generated artifacts from entering the site. It will not mass-delete outputs or alter dirty working-tree content; broader notebook repairs will be separate changes.

## Risks / Trade-offs

- **[Risk]** Staged copies can become stale if users run MkDocs directly. → **Mitigation:** provide wrapper commands and CI that always synchronize first; make the staging directory clearly generated and ignored.
- **[Risk]** Rendering stored outputs can give a false impression of execution health. → **Mitigation:** label the site/build as render-only and add checks for stored error outputs; plan execution smoke tests separately.
- **[Risk]** Copying assets may increase build complexity. → **Mitigation:** keep the sync rules narrow, test required relative assets, and report missing source files clearly.
- **[Risk]** Strict link validation may reveal many existing upstream-only links. → **Mitigation:** scope this change to the local site and maintain a current local inventory; update the main repository in a later coordinated change.
- **[Risk]** Documentation dependencies may drift. → **Mitigation:** declare compatible minimum versions and document the supported local build environment; full ecosystem pinning remains future work.
