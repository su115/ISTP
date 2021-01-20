#! /bin/bash

#pipenv shell
pipenv install
pipenv run python3 -m pytest $PWD/tests/tests.py
