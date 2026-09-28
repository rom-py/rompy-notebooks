# Data concepts: declarative, on-demand inputs

Rompy's data model is more than a convenient file reader. It lets a model run describe **what data is needed**, **where it comes from**, and **how it must be transformed** without embedding a copy of the source dataset in the run description.

## The key idea

A Rompy input is a declarative data request:

```text
source plugin + variables + time range + model domain + transformation rules
                                      |
                                      v
                    fetch only the required slice
                                      |
                                      v
                         model-native input files
```

The run description contains the request and the transformation contract. It does not need to carry the entire reanalysis archive, bathymetry dataset, wave catalogue, or ocean model output alongside it.

## Source plugins define the data boundary

Sources are selected through plugin interfaces. A source plugin knows how to open a particular kind of provider or file—such as an intake catalogue, a local dataset, a Datamesh source, a wave-spectra source, or a model-specific fixture—while the model configuration describes the data variables and spatial/temporal contract it needs.

This separates two concerns:

- **Provider access:** how to locate and read a dataset.
- **Model preparation:** which variables, coordinates, period, domain, interpolation, extraction, and output format the run requires.

The same model-oriented description can therefore be reused with a different provider plugin when the source satisfies the same data contract.

## Only fetch what the run needs

The time range and model grid/domain are not just labels. They constrain the request. Rompy can select the relevant time window and crop or interpolate the relevant spatial region before writing model-native files. This reduces transfer and processing cost, avoids carrying irrelevant data through the workflow, and makes the generated workspace match the declared experiment.

The modeller still owns the scientific decisions: dataset suitability, variables, coordinate interpretation, interpolation method, quality control, and boundary assumptions. On-demand selection makes those decisions explicit; it does not make them automatically correct.

## Why declarative descriptions are shareable

A complete run description can be versioned and shared as code or YAML:

```text
shared run description
    ├── model and grid
    ├── time period
    ├── source plugin + dataset identity
    ├── selection and transformation rules
    └── output contract

provider data remains external and is acquired only when needed
```

A colleague can inspect the experiment, substitute an approved provider or local cache, and regenerate the same class of model inputs without receiving a copy of every upstream dataset. Reproducibility comes from the run description, source identity/version, selection rules, and environment—not from silently bundling a large data archive.

## See it in the notebooks

- [SWAN grids and input data](notebooks/swan/tutorial_04_swan_data.ipynb) — regular-grid bathymetry, wind, and nested boundary preparation.
- [XBeach bathymetry](notebooks/xbeach/tutorial/03_bathymetry.ipynb), [forcing](notebooks/xbeach/tutorial/04_forcing.ipynb) and [data selection options](notebooks/xbeach/examples/data_selection.ipynb) — sources, interpolation onto the grid, and cropping to the model domain and run period.
- [SCHISM forcing](notebooks/schism/tutorial_04_schism_forcing.ipynb) — mesh-aware atmospheric, ocean, tidal, and wave processing.

The notebooks bundle small sample datasets so that they run without downloads. A real run points the same objects at your own files, catalogues or data services.

These lessons show the concrete transformations. This page provides the shared mental model that connects them.

!!! warning
    A portable declarative description is not by itself scientific validation. Always record source provenance, inspect generated inputs, and validate the resulting model setup for the intended experiment.
