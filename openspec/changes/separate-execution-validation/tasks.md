## 1. Validation contract

- [x] 1.1 Define execution metadata for eligibility, group, and runtime prerequisites
- [x] 1.2 Document the four validation tiers and evidence boundaries

## 2. Selected execution

- [x] 2.1 Implement metadata-based notebook selection
- [x] 2.2 Execute selected notebooks in staged copies without modifying sources
- [x] 2.3 Produce a current-run execution report with environment and limitation fields
- [x] 2.4 Fail clearly on selected-notebook errors or unmet prerequisites

## 3. Runtime separation

- [x] 3.1 Add opt-in model-runtime targets for SWAN, XBeach, and SCHISM
- [x] 3.2 Keep default documentation and CI commands free of model-runtime requirements
- [x] 3.3 Update CI/workflow documentation with tier-specific commands

## 4. Verification

- [x] 4.1 Add tests for metadata selection, source preservation, reporting, and failure handling
- [x] 4.2 Run structural audit, render-only build, and selected execution
- [x] 4.3 Verify optional runtime targets fail clearly when prerequisites are unavailable
