.DEFAULT_GOAL := all

all: install test run deploy

install:
	@echo "Installing pipenv and dependencies."
	# Ваш код тут
	pip install pipenv
	pipenv --three
	pipenv install ntplib
	pipenv install requests
	pipenv install pytest
	pipenv lock


test:
	@echo "Start tests."
	# Ваш код тут
	#pipenv shell 
	pipenv run python3 -m pytest ./tests/tests.py
	exit 0

run:
	@echo "Run Python app."
	# Ваш код тут
	pipenv shell
	python3 app.py >>results.txt
	exit
deploy:
	@echo "Adding and Committing results.txt to git."
	git add results.txt 
	git commit -m "Lab2:1st make commit"
	git push origin main
