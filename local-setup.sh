#!/bin/bash

# Create a virtual environment and install the required packages
python -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install the required packages
pip install .[dev]