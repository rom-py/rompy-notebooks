# Rompy plugin architecture

Rompy keeps the core model-run concepts small and lets plugins provide model, data, and execution-specific behavior.

```text
                 Rompy core
       ModelRun · TimeRange · sources · backends
              /          |          \
             /           |           \
     model plugins   data plugins   backend plugins
      SWAN/XBeach/    files/catalogs   local/MPI/Docker/
       SCHISM          Datamesh        schedulers
```

## Three plugin boundaries

### Model plugins

Model plugins define grids, configuration objects, input components, templates, and model-native output contracts. `rompy-swan`, `rompy-xbeach`, and `rompy-schism` provide the vocabulary needed to prepare those models without placing every model assumption in Rompy core.

### Data-source plugins

Data plugins define how a source is opened or queried. A file, catalogue, Datamesh dataset, or wave-spectra provider can be selected through a source interface while the model-facing request still declares variables, coordinates, domain, and time.

This is the boundary described in [Data concepts](data-concepts.md): provider access and model preparation are related, but not the same concern.

### Backend plugins

Backend plugins define where and how a prepared workspace runs. A local process, MPI execution, container, or scheduler can consume the generated workspace without changing the model configuration itself.

## Why this architecture is useful

- Model plugins can evolve independently of the core package.
- Data providers can be replaced without rewriting model configuration.
- Runtime environments remain optional and explicit.
- A configuration can be reviewed and tested at the level appropriate to the available environment.

The plugin boundary is an extension point, not a guarantee that every plugin supports every source or workflow. Always check the model/plugin documentation and generated-file contract.
