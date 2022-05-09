SHELL=/bin/bash

# --------------
# Testing
# --------------
test: mypy pytest  # run with -k flag in order to continue in case of recipe failure

mypy:
	mypy monostate/

pytest:
	coverage run -m pytest -vv tests/
	coverage xml
