#! /bin/bash

#pipenv shell
pipenv install
pipenv run python3 -m pytest ./tests/tests.py
