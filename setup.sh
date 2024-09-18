#!/bin/bash

# setup.sh - Script to set up the rompy-notebooks environment

echo "Starting the setup of rompy-notebooks..."

# Function to check if a command exists
command_exists () {
    command -v "$1" &> /dev/null ;
}

# Check if conda is installed
if command_exists conda; then
    echo "Conda detected. Proceeding with Conda setup..."

    # Create the environment from environment.yml
    echo "Creating the conda environment from environment.yml..."
    conda env create -f environment.yml

    echo "Setup complete! To activate the environment, run:"
    echo "    conda activate rompy-notebooks"
else
    echo "Conda not found. Please install Conda and try again."
    exit 1
fi

echo "You can now start using the rompy-notebooks."
echo "To start Jupyter Notebook, run:"
echo "    jupyter lab
"
exit 0
