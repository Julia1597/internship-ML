#!/bin/bash

set -e

# Activation environnement
source .venv/bin/activate

# Lancement pipeline
python Main.py
