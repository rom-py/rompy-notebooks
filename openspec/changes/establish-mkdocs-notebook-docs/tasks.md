## 1. Documentation foundation

- [x] 1.1 Add MkDocs, Material, notebook-rendering, and validation dependencies using the repository's chosen supported installation path.
- [x] 1.2 Add MkDocs configuration with a generated documentation directory, strict-friendly settings, notebook rendering with execution disabled, and curated navigation.
- [x] 1.3 Add source-to-staging documentation sync tooling that copies supported notebooks/assets and excludes checkpoints, caches, and generated run outputs.
- [x] 1.4 Add local index, installation/build/preview instructions, notebook gallery pages, and an explicit render-only execution-status note.
- [x] 1.5 Add documented developer commands for staging, serving, and strict site validation; ensure generated staging/build directories are ignored.

## 2. Audit and cleanup

- [x] 2.1 Implement an inventory of tracked notebooks and local documentation targets used by the quality gate.
- [x] 2.2 Remove the tracked zero-byte `notebooks/schism/schism_basic_setup.ipynb` or replace it with intentional documented content, according to the final audit decision.
- [x] 2.3 Correct local navigation and documentation references so every listed notebook and asset exists; do not mass-delete user or generated working-tree files.
- [x] 2.4 Document known execution-heavy, externally dependent, or currently unverified notebooks without claiming that rendering validates them.

## 3. Quality gate

- [x] 3.1 Add structural notebook checks for JSON validity, empty notebooks, required metadata, and stored execution error outputs.
- [x] 3.2 Add hygiene checks for checkpoint/cache/generated content in the source inventory and staged tree.
- [x] 3.3 Add documentation integrity checks for missing notebook and asset targets.
- [x] 3.4 Add tests covering representative passing notebooks and each confirmed failure category.
- [x] 3.5 Add CI configuration that runs the combined quality checks and strict MkDocs build without requiring model binaries, Docker, MPI, or remote data services.

## 4. Verification and handoff

- [x] 4.1 Run the documented combined validation command from a clean checkout and record its output.
- [x] 4.2 Verify local preview/build behavior and inspect the generated gallery for all model groups.
- [x] 4.3 Review the resulting diff to ensure no user-generated or unrelated notebook outputs were removed.
- [x] 4.4 Update the repository README and contributing guidance with the new documentation and validation workflow.
