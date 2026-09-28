# rompy-notebooks

Tutorials and examples for setting up and running ocean and coastal models with [rompy](https://rom-py.github.io/rompy/) and its model plugins for SWAN, XBeach and SCHISM.

Rompy describes a model run as validated Python objects (or a YAML file), turns datasets into the model's input files, and runs the model locally, in Docker or on a cluster. The notebooks here show how, model by model.

## How to use this site

1. **[What rompy does](why-rompy.md):** the problem rompy solves and the big picture, in a few minutes. The [hands-on notebook](notebooks/common/rompy_hands_on.ipynb) then goes through a complete run with a toy model.
2. **[Installation](installation_guide.md)** and **[using the notebooks](usage_guide.md):** get the notebooks running on your machine.
3. **Concepts:** the ideas behind every model, in more depth: [configuration and validation](validation-concepts.md), [data](data-concepts.md), the [run lifecycle](run-lifecycle.md) and [plugins](plugin-architecture.md).
4. **Learning tutorials:** an ordered path through one model, from a first run to a complete setup: [SWAN](swan-tutorial.md), [XBeach](xbeach-tutorial.md) or [SCHISM](schism-tutorial.md).
5. **[Notebook catalogue](catalogue.md):** every notebook by model and by topic, for when you need a specific feature.

New to rompy? Start with step 1. If you already know rompy, go straight to a learning tutorial or the catalogue.

!!! note
    The pages show the outputs stored in the notebooks. Building this site does not run the notebooks or any model.
