# rompy-notebooks

Welcome to the **rompy-notebooks** repository! This collection of Jupyter notebooks is designed to help you learn how to set up and use **rompy** across various ocean modeling software, including SWAN, XBeach, and SCHISM.

## Contents

- **notebooks/**: Model-specific and common notebooks demonstrating usage examples.
- **data/**: Sample datasets used in the notebooks.
- **docs/**: Additional documentation and guides, including the [SWAN learning journey](docs/swan-journey.md).
- **requirements.txt**: List of dependencies to run the notebooks.

## Getting Started

See the [installation guide](docs/installation_guide.md) for instructions on how to set up the notebook environment. To browse the local documentation site and validate notebook structure, see the [build and execution guide](docs/workflow.md):

```bash
python -m pip install -r requirements-docs.txt
make docs-build
```

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines. Documentation changes should pass `make docs-build`.

## License

This project is licensed under the terms of the [MIT license](LICENSE).
