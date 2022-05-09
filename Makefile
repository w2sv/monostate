SHELL=/bin/bash

test: mypy pytest coverage-report  # run with -k flag in order to continue in case of recipe failure

###########
# Testing #
###########

mypy:
	mypy monostate/

pytest:
	coverage run -m pytest -vv tests/

coverage-report:
	coverage xml
	coverage report

##############
# Publishing #
##############

publish: test patch-version _publish

patch-version:
	poetry version patch

_publish:
	poetry publish --build