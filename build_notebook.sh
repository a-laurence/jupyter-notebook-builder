#!/bin/zsh

pip3 install --upgrade pip
pip3 install --user pipenv

python3 -m pipenv install .
python3 -m pipenv run pre-commit install
python3 -m pipenv run python python-scripts/build-notebook.py
