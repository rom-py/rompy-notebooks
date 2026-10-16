# Notebook tutorial conventions

These conventions keep model notebook collections predictable while allowing each model to grow at its own pace.

## Content roles

Every model notebook has one primary role:

- **Tutorial** — an ordered lesson for newcomers. It states learning goals and prerequisites, builds on earlier lessons, and links to the next and previous steps where applicable.
- **Example** — a focused lesson for one workflow or capability. It explains the concept, shows a minimal example, and links to related material without requiring linear progression.
- **Reference** — a specialist or broad example intended for lookup. It identifies the feature demonstrated and avoids presenting itself as a complete learning path.

## Notebook layout and structure

The XBeach and SWAN collections use the layout below. It is the target for the other models, which will move to it as their collections are revised:

```text
notebooks/<model>/
├── README.md       index: tutorial table and examples grouped by theme
├── tutorial/       ordered lessons, 01_first_model.ipynb, 02_..., ...
├── examples/       focused notebooks, one feature each
└── data/           small committed datasets with a README of their contents
```

Every notebook opens with one markdown cell containing:

- a numbered title for tutorial lessons (`# 2. Defining the model grid`) or a plain title for examples;
- **What this shows:** one or two sentences;
- **Prerequisites:** links to earlier lessons or examples, or "none";
- **You will learn:** three to five bullet points;
- **Data used:** the files from `data/`, or "none".

Sections are numbered `## 1. ...`, `## 2. ...` after a `## Setup` cell. Notebooks end with `## Summary` (or `## Next steps`), a **Next:** link for tutorial lessons, and **See also:** links to related examples. The notebook audit checks the opening sections for XBeach and SWAN.

Links between notebooks are written as relative `.ipynb` links so they work in Jupyter and on GitHub; the MkDocs hook translates them for the site. Links to a model's `README.md` go to its learning tutorial page on the site, and links to data or other repository files go to GitHub.

Notebooks read their data with paths relative to the notebook (`../data/bathy.tif`) and write generated files to a local, git-ignored `_output/` folder. Notebooks are committed with their outputs, which the documentation renders without re-running them.

## Notebook metadata

Model notebooks carry a `rompy_notebooks` metadata object:

```json
{
  "model": "swan",
  "kind": "tutorial",
  "level": "intermediate",
  "topics": ["configuration"],
  "execution": "render-only"
}
```

Allowed values are:

- `model`: `swan`, `xbeach`, or `schism`;
- `kind`: `tutorial`, `example`, or `reference`;
- `level`: `beginner`, `intermediate`, or `advanced`;
- `topics`: a non-empty list of concise topic names;
- `execution`: `render-only`, `configuration-only`, or `runtime-dependent`.
- `execution_group`: usually `tutorials` or `reference`; selected execution runs one group at a time;
- `execution_eligible`: explicit boolean controlling lightweight selected execution;
- `runtime_requirements`: list of required model binaries or services for the declared execution tier.

The metadata describes instructional context; it does not replace explanations in the notebook or navigation in the model overview. The `id` is stable and unique, `published` controls inclusion in generated indexes, `prerequisites` and `execution_requirements` describe what a reader needs, and tutorial lessons use a positive `tutorial` number. Excluded notebooks must provide an `exclusion_reason`.

## Showing Rompy's value

Lessons involving grids, forcing, boundaries, or workspace generation should make the practical transformation visible. Explain the equivalent manual workflow, name the Rompy objects that represent it, show representative generated artefacts, and include a plot or metadata check when fixtures support one. Be precise about the boundary: Rompy orchestrates configured filtering, interpolation, extraction, and model-format conversion, while the modeller remains responsible for source selection, scientific assumptions, data quality, and runtime validation.

Use short headings or callouts such as **Without Rompy**, **With Rompy**, **Generated artefacts**, and **Verification**. Documentation rendering remains render-only; these explanations must not imply that a model binary ran.

## Author checklist

Before adding or changing a model notebook:

1. Choose exactly one primary content role.
2. State the audience, learning goals, and prerequisites near the beginning.
3. Keep model execution separate from documentation rendering.
4. Add accurate `rompy_notebooks` metadata.
5. Link to the model overview and nearby content when useful.
6. Add the notebook to the curated model navigation and the complete gallery.
7. Run `make docs-build` to validate JSON, structure, links, and strict rendering.

Model overviews use shared conceptual sections where content exists. Do not add empty notebooks solely to make SWAN, XBeach, and SCHISM look symmetrical; record missing coverage in the [coverage matrix](models/coverage.md) instead.
