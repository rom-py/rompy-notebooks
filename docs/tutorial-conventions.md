# Notebook tutorial conventions

These conventions keep model notebook collections predictable while allowing each model to grow at its own pace.

## Content roles

Every model notebook has one primary role:

- **Journey** — an ordered lesson for newcomers. It states learning goals and prerequisites, builds on earlier lessons, and links to the next and previous steps where applicable.
- **Tutorial** — a focused lesson for one workflow or capability. It explains the concept, shows a minimal example, and links to related material without requiring linear progression.
- **Reference** — a specialist or broad example intended for lookup. It identifies the feature demonstrated and avoids presenting itself as a complete learning path.

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
- `kind`: `journey`, `tutorial`, or `reference`;
- `level`: `beginner`, `intermediate`, or `advanced`;
- `topics`: a non-empty list of concise topic names;
- `execution`: `render-only`, `configuration-only`, or `runtime-dependent`.

The metadata describes instructional context; it does not replace explanations in the notebook or navigation in the model overview.

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
