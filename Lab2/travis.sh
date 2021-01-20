#! /bin/bash

#pipenv shell
pipenv install
pipenv run python3 -m pytest $PWD/Lab2/tests/tests.py
