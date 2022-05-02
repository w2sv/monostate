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

# --------------
# Building
# --------------
build: test
	rm -rf asciiplot.egg-info
	rm -rf build
	rm -rf dist

	python setup.py sdist bdist_wheel --dist-dir ./dist

upload: build
	python -m twine check dist/*
	python setup.py sdist bdist_wheel upload

	# Adding release tag to push:
	# git tag -a v0.1.1 -m "Alter short pypi description"