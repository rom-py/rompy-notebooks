# Validation concepts: a typed input contract

Rompy does not treat model configuration as an arbitrary block of text. Its configuration objects are defined as typed Pydantic models, so an input description is validated as it is constructed—before Rompy writes model-native files or attempts to run a model.

## From text files to an explicit contract

Traditional model inputs are often unstructured text:

```text
keyword value value value
another-keyword value
...                  # errors may appear only when the model starts
```

The model may accept the file as text while rejecting a value later, silently applying a default, or failing with an opaque parser message. The file format describes syntax, but often provides little help while the configuration is being assembled.

Rompy makes the contract explicit in Python objects:

```text
Typed field + type constraints + domain rules
                    |
                    v
          validated Rompy configuration
                    |
                    v
             model-native input files
```

The declarative description can therefore be checked, reviewed, shared, and regenerated before it reaches the model parser.

## Two layers of validation

### Basic typed validation

Pydantic checks that fields have the expected types and shapes. For example, a time range must contain valid times, a grid must contain numeric dimensions, and a list of variables must contain strings rather than an accidentally supplied scalar or unrelated object.

Invalid values produce a structured validation error that identifies the field and the received value close to the point where the configuration was created.

### Domain-specific validation

Rompy and its model plugins can add rules that express the model domain, not just Python syntax. Examples include bounded physical parameters, required combinations of fields, supported enumerations, compatible component types, valid coordinate or dimension contracts, and model-specific configuration relationships.

These rules turn configuration into an executable contract between the modeller, Rompy, and the target model plugin.

## Why this matters

- Errors are found while assembling the run, rather than after a model starts.
- Editor/type-checking tools can expose the available configuration vocabulary.
- Shared YAML or Python descriptions retain structure instead of relying on positional text conventions.
- Model plugins can encode their own rules while keeping Rompy core model-neutral.
- Generated text files become a deliberate output of a validated description, not the primary place where correctness is discovered.

This is complementary to the [data concepts](data-concepts.md): source plugins define how data is located and selected, while typed model/data objects define what the run expects.

## What the contract does not promise

Pydantic validation can establish that a configuration is structurally and domain-valid according to the declared rules. It cannot determine whether a dataset is scientifically suitable, whether boundary conditions represent reality, or whether a model has adequate skill for the intended question. Those remain modelling and scientific-validation responsibilities.

See the [run lifecycle](run-lifecycle.md) and [build and execution guide](workflow.md) to place validation in the broader Rompy workflow.
