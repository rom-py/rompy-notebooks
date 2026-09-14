# Model notebook coverage

The model collections intentionally have different levels of maturity. This matrix records the current coverage without creating placeholder notebooks.

| Section | SWAN | XBeach | SCHISM |
| --- | --- | --- | --- |
| Getting started | Established | Partial | Partial |
| Procedural workflow | Established | Established | Partial |
| Declarative workflow | Established | Established | Not yet covered |
| Grids and input data | Established | Established | Established (real fixture case) |
| Boundary conditions | Established | Established | Established (2-D; 3-D contract inspected) |
| Physics/components | Partial | Established | Not yet covered |
| Outputs and diagnostics | Established | Established | Not yet covered |
| Execution and backends | Partial | Partial | Partial |
| Advanced workflows | Established | Partial | Partial (forcing-family case study; runtime remains external) |

**Established** means the collection has focused content that can be used today. **Partial** means content exists but does not yet form a complete instructional treatment. **Not yet covered** is an explicit gap for a future change.

The enriched case studies now follow a source → configuration → generated artefact → verification pattern. “Established” does not mean scientifically validated or runtime-complete.

- [SWAN notebooks](swan.md)
- [XBeach notebooks](xbeach.md)
- [SCHISM notebooks](schism.md)
