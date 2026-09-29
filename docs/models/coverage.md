# Model notebook coverage

The model collections intentionally have different levels of maturity. This matrix records the current coverage without creating placeholder notebooks.

| Section | SWAN | XBeach | SCHISM |
| --- | --- | --- | --- |
| Getting started | Established | Established | Established |
| Procedural workflow | Established | Established | Established |
| Declarative workflow | Established | Established | Established |
| Grids and input data | Established | Established | Established |
| Boundary conditions | Established | Established | Established (tides, ocean model, 3D, waves) |
| Physics/components | Established | Established | Established |
| Outputs and diagnostics | Established | Established | Established |
| Execution and backends | Established (local, Docker, MPI, CLI) | Established (local, Docker, MPI, CLI) | Established (local, Docker, MPI, CLI) |
| Advanced workflows | Established (nesting, hotstart, physics sensitivity) | Established (hotstart, parameter sweep) | Established (baroclinic 3D, waves, hotstart, friction sensitivity) |

**Established** means the collection has focused content that can be used today. **Partial** means content exists but does not yet form a complete instructional treatment. **Not yet covered** is an explicit gap for a future change.

The enriched case studies now follow a source → configuration → generated artefact → verification pattern. “Established” does not mean scientifically validated or runtime-complete.

- [SWAN notebooks](swan.md)
- [XBeach notebooks](xbeach.md)
- [SCHISM notebooks](schism.md)
