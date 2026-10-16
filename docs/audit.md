# Audit status

This repository is an actively evolving collection rather than a fully reproducible model test suite.

## Current validation boundary

- The MkDocs build validates documentation rendering and local links.
- The notebook quality gate validates notebook JSON, metadata, stored error outputs, and generated-file hygiene.
- Full execution is not part of the documentation build. SWAN, XBeach, and SCHISM examples may additionally require model binaries, Docker, MPI, remote data, or external package test data.

Known execution concerns and stale outputs are tracked in the repository audit and should be repaired in focused follow-up changes. A successful documentation build must not be interpreted as proof that every notebook executes successfully.
