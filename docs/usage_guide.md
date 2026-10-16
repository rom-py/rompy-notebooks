# Using the notebooks

## How each model's notebooks are organised

- **Learning tutorial:** an ordered path from a first model to a complete setup. Each lesson builds on the previous one and ends with a link to the next.
- **Examples:** self-contained notebooks on one feature, such as a type of wave boundary or a physics option. Read them in any order.
- **Reference:** broader or specialist notebooks for lookup.

The [catalogue](catalogue.md) lists every notebook by model and by topic, with its level and what it needs to run.

## What each notebook tells you first

The first cell says what the notebook covers, what to read first and what you will learn. The last cells link to the next lesson or to related notebooks.

## Data and generated files

- Example data is committed next to the notebooks, for example in `notebooks/xbeach/data/`, and read with paths relative to the notebook. Run notebooks from their own folder, which is what Jupyter does by default.
- Notebooks write model workspaces to a local `_output/` folder, which git ignores and which is safe to delete.

## Stored outputs

The notebooks are committed with their outputs, and this site shows those outputs. Running a notebook again regenerates them in your environment. Results can differ slightly with other package or model versions.

## Using your own data

Replace the example paths with your own files, or point the source objects at a catalogue or data service. The [data concepts](data-concepts.md) page and each model's data notebooks explain which classes read which formats.
