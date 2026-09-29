# Installation

The notebooks need Python 3.10 or later, rompy, the model plugins and a few scientific Python packages. Model binaries are only needed to run the models, and the notebooks say when they are.

## 1. Get the notebooks

Clone the repository. The notebooks read example data from folders next to them, so a clone is the simplest way to run them:

```bash
git clone https://github.com/rom-py/rompy-notebooks.git
cd rompy-notebooks
```

## 2. Create a Python environment

Use a virtual environment (or a conda environment) and install the requirements. This installs rompy, rompy-swan, rompy-xbeach, rompy-schism, JupyterLab and the plotting and data libraries the notebooks use:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## 3. Start Jupyter

```bash
jupyter lab
```

Then open a notebook, for example the first lesson of a [learning tutorial](index.md#how-to-use-this-site). [Using the notebooks](usage_guide.md) explains how they read data and write files.

## Running the models

Generating a model workspace needs only the Python packages above. Running the model needs the model itself:

- The notebooks use public Docker images of each model, `ghcr.io/rom-py/xbeach`, `ghcr.io/rom-py/swan` and `ghcr.io/rom-py/schism`, so [Docker](https://docs.docker.com/get-docker/) is enough. Cells that run a model are skipped when Docker is not available.
- To use a local installation of a model instead, see the "Running" example of each model.

## Building this site

Building the documentation needs different tools and does not run any model. See the [build and execution guide](workflow.md).
