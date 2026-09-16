# Validation concepts

Rompy workflows produce several kinds of evidence. They should not be confused with one another.

```text
Valid notebook structure
        ↓
Successful configuration/data processing
        ↓
Generated model inputs
        ↓
Successful model execution
        ↓
Scientifically suitable experiment
```

Each step is stronger evidence for a different question, but none silently proves the next step.

## Evidence levels

### Structural validity

The notebook is valid JSON, has the expected metadata, contains no stored execution errors, and links to existing documentation. This is the minimum documentation quality gate.

### Processing validity

The configured Rompy objects open their sources, select the requested domain and period, and write expected model-native artefacts. Dimension checks, variable checks, plots, and file previews are useful evidence here.

### Runtime validity

The target model binary starts and consumes the generated workspace with the required MPI, container, or scheduler environment. This is optional and environment-specific.

### Scientific validity

The data, assumptions, boundary conditions, resolution, calibration, and resulting model skill are appropriate for the intended scientific question. This requires domain expertise and cannot be established by a documentation build or a structural test.

## Why the distinction matters

It prevents two common mistakes:

- treating stored notebook output as proof that the current environment still works;
- treating successful file generation as proof that the model setup is scientifically correct.

Rompy makes the preparation contract explicit and inspectable. The modeller remains responsible for deciding whether the source data and generated experiment are fit for purpose.

See the [build and execution guide](workflow.md) for the repository's validation tiers and commands.
