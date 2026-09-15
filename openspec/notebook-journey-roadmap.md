# Rompy Notebook Journey Roadmap

This document captures the likely follow-on changes after the documentation-site foundation. It is a planning aid, not a published documentation page. Each phase should become its own OpenSpec change once its scope is ready.

## Product direction

The repository should take users from a model-neutral introduction to Rompy, through one complete model journey, and then into deeper model-specific tutorials and reference material.

```text
Learn Rompy
    |
    v
First complete journey: SWAN
    |
    +--> Model tutorials: SWAN
    +--> Model tutorials: XBeach
    +--> Model tutorials: SCHISM
    |
    v
Reference gallery and execution guidance
```

The existing XBeach notebooks are the most comprehensive tutorial collection and should provide the strongest stylistic and structural reference. SWAN is the preferred first complete journey because its configuration flow is comparatively approachable and already has procedural, declarative, boundary, output, and sensitivity examples.

## Completed foundation

### `establish-mkdocs-notebook-docs`

Completed in commit `8de53a5`.

Delivered:

- local MkDocs + Material site;
- generated notebook staging that excludes checkpoints and unrelated untracked files;
- render-only documentation builds with notebook execution disabled;
- notebook structural quality checks;
- local preview and CI commands;
- initial gallery and model-group navigation.

This foundation intentionally does not claim that a rendered notebook is an executable model workflow.

## Completed follow-on work

The following roadmap changes have since been implemented in the repository:

- `create-swan-first-journey` — SWAN now has a coherent seven-lesson journey from Rompy orientation through workspace generation and execution guidance.
- `standardize-model-tutorial-layout` — SWAN, XBeach, and SCHISM use consistent journey metadata, numbering, navigation, and lesson conventions.
- `expand-xbeach-learning-path` — XBeach has a connected seven-lesson path plus focused data-interface and component tutorials.
- `expand-schism-tutorials` — SCHISM has focused grid, forcing, boundary/namelist, complete-case, and execution lessons with real generated artefacts where supported.

The completed case-study work demonstrates structural generation and processing contracts; it does not claim scientific validation or model-runtime success in every environment.

## Follow-on changes

### 1. `create-swan-first-journey`

**Purpose:** Create the first coherent, end-to-end learning path through Rompy using SWAN.

**Expected content:**

1. Rompy concepts and core objects;
2. the smallest useful SWAN workspace;
3. procedural versus declarative configuration;
4. grids, bathymetry, wind, and boundary data;
5. SWAN physics and output configuration;
6. workspace generation and inspection;
7. optional SWAN execution and result inspection;
8. sensitivity analysis and reproducibility.

**Scope:**

- actual new or substantially curated notebooks are part of this change;
- add a dedicated learning-journey section to the site;
- link from journey notebooks to deeper SWAN references;
- make execution prerequisites and optional cells explicit;
- avoid requiring a SWAN binary for documentation rendering.

**Dependencies:** documentation foundation complete.

**Exit criteria:** a new user can follow the SWAN path from first Rompy concepts to a generated model workspace without guessing which notebook comes next.

### 2. `standardize-model-tutorial-layout`

**Purpose:** Define and apply a shared information architecture for model-specific tutorial collections.

**Target layout:**

```text
<Model>
├── Getting started
├── Procedural workflow
├── Declarative workflow
├── Grids and input data
├── Boundary conditions
├── Physics/components
├── Outputs and diagnostics
├── Execution and backends
└── Advanced workflows
```

**Scope:**

- document the distinction between journey, tutorial, and reference notebooks;
- establish naming, numbering, prerequisites, learning objectives, summaries, and next-step conventions;
- curate existing SWAN and XBeach notebooks into the structure where practical;
- avoid duplicating detailed material merely to achieve visual symmetry;
- identify missing tutorial areas as explicit future work.

**Dependencies:** SWAN journey should provide a tested pattern before broad adoption.

**Exit criteria:** users can predict where to find a capability in every model collection, even when the amount of content differs by model.

### 3. `expand-xbeach-learning-path`

**Purpose:** Turn the existing comprehensive XBeach material into a navigable model tutorial path.

**Likely content groups:**

- procedural and declarative workflows;
- grid and bathymetry data;
- wind, tide, and wave forcing;
- physics and sediment transport;
- boundary conditions;
- outputs and hotstarts;
- MPI and execution;
- advanced configuration.

**Scope:**

- preserve the existing detailed tutorials where they are useful;
- add an XBeach overview/starting point rather than rewriting every notebook;
- connect the capability tutorials into a progression;
- clearly label notebooks that demonstrate configuration only versus actual execution.

**Dependencies:** shared tutorial layout; lessons learned from the SWAN journey.

**Exit criteria:** XBeach becomes the deepest and most complete model tutorial collection without requiring users to infer its sequence from filenames.

### 4. `expand-schism-tutorials`

**Purpose:** Grow SCHISM from one large demonstration notebook into a set of focused tutorials.

**Likely content groups:**

- procedural configuration;
- grid and workspace setup;
- atmospheric, tidal, and wave forcing;
- boundary conditions;
- namelist configuration;
- execution backends;
- output verification;
- advanced workflows.

**Scope:**

- split or supplement the current broad demonstration carefully;
- retain a complete example for reference;
- do not imply XBeach-level coverage until examples actually exist;
- isolate binary, MPI, Docker, and external-data requirements from render-only examples.

**Dependencies:** shared tutorial layout; clarified SCHISM data and runtime prerequisites.

**Exit criteria:** a user can learn the major SCHISM configuration concepts through focused notebooks, with honest coverage and runtime limitations.

### 5. `improve-notebook-discoverability` **(complete)**

**Purpose:** Make the site useful as both a guided course and a reference catalogue.

**Potential work:**

- distinguish “Learn Rompy”, “Model tutorials”, and “Reference gallery” in navigation;
- add consistent notebook metadata such as model, level, prerequisites, execution requirements, and topic;
- generate model indexes from notebook metadata where this reduces manual drift;
- add previous/next journey links;
- expose missing, untracked, or intentionally excluded notebooks in the audit report;
- ensure the gallery and sidebar are generated from the same inventory.

**Dependencies:** at least one complete journey and an agreed metadata convention.

**Exit criteria:** users can discover a notebook by learning goal, model, or capability, and omissions are visible rather than silent.

### 6. `separate-execution-validation` **(complete)**

**Purpose:** Add confidence about actual notebook/model execution without making documentation builds dependent on model runtimes.

**Potential validation tiers:**

```text
Tier 1: JSON and structural audit       always required
Tier 2: render-only MkDocs build       always required
Tier 3: lightweight notebook execution selected notebooks
Tier 4: model integration execution     opt-in / scheduled / environment-specific
```

**Scope:**

- define which notebooks are expected to execute without model binaries;
- define runtime environments for SWAN, XBeach, and SCHISM integration tests;
- add explicit handling for external data and remote services;
- prevent stored outputs from being mistaken for current execution evidence.

**Dependencies:** stable journey notebooks and clear execution contracts.

**Exit criteria:** documentation CI remains lightweight while executable examples have a separate, trustworthy validation path.

### 7. `reproducible-example-data-and-outputs` **(next)**

**Purpose:** Improve repeatability and provenance for examples that use data, generated files, or stored outputs.

**Potential work:**

- identify which example inputs can be kept small and local;
- document external-data provenance and retrieval steps;
- standardize relative paths and temporary workspaces;
- decide which generated outputs should be committed, ignored, or regenerated;
- add version/model/plugin information to notebooks where useful.

**Dependencies:** execution-validation design and model-specific tutorial review.

**Exit criteria:** users can understand where inputs came from, what was actually run, and how to reproduce or refresh stored outputs.

### 5a. `consolidate-documentation-navigation` **(complete)**

This follow-on consolidation removed overlapping gallery, discovery, and notebook catalogue entry points and established one logical documentation hierarchy.

## Suggested order

The journey, tutorial, discoverability, navigation, and execution-validation work is complete. The next planned change is reproducible example data and outputs:

```text
1–6. completed journey, catalogue, navigation, and validation work
          |
          v
7. reproducible-example-data-and-outputs
```

The dependency arrows are deliberately soft. For example, SCHISM work may begin earlier if there is an immediate documentation need, but the shared layout and execution conventions should be established before attempting broad restructuring.

## Decisions to revisit when creating the first change

- How many notebooks should constitute the minimum SWAN journey: a compact 4–5 notebook path or a fuller 7–8 notebook course?
- Should journey notebooks be new files, curated copies of existing examples, or a mixture?
- Should optional execution cells live in the journey notebooks or in separate execution notebooks?
- Which audience is primary: Rompy beginners, ocean-model users new to Rompy, or experienced Rompy developers?
- What level of stored output is desirable for the first journey when current SWAN examples have runtime and data dependencies?
