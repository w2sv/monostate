SHELL=/bin/bash

# --------------
# Installation
# --------------
install:
	rm -rf env
	mamba env create -f environment.yml --prefix ./env

# --------------
# Testing
# --------------
test: mypy pytest  # run with -k flag in order to continue in case of recipe failure

mypy:
	mypy monostate/

pytest:
	coverage run -m pytest -vv tests/
	coverage xml

# --------------
# Building
# --------------
wheel:
	rm -rf monostate.egg-info
	rm -rf build
	rm -rf dist

	python setup.py sdist bdist_wheel --dist-dir ./dist

upload: wheel
	python -m twine check dist/*
	python setup.py sdist bdist_wheel upload