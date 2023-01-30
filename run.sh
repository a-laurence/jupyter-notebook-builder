#!/bin/bash

pip3 install --upgrade pip
pip3 install --user pipenv
python3 -m pipenv install --dev --skip-lock
python3 -m pipenv run pre-commit install

export NOTEBOOK_NAME=""
export TEMPLATE="template.txt"

for (( i=1; i<=$#; i++ )); do
  j=$((i+1))
  case "${!i}" in
      "--name")
        NOTEBOOK_NAME="${!j}";;
      "-t")
        TEMPLATE="${!j}";;
      *)
        ;;
  esac
done

python3 -m pipenv run python python_scripts/notebook_builder.py
