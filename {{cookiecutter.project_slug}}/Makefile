# file modified from https://gist.github.com/lumengxi/0ae4645124cd4066f676
.PHONY: clean-pyc clean-build docs clean

PACKAGE_DIR={{cookiecutter.project_package_name}}

# Check that given variables are set and all have non-empty values,
# die with an error otherwise.
#
# Params:
#   1. Variable name(s) to test.
#   2. (optional) Error message to print.
# Details at https://stackoverflow.com/a/10858332/4374048
check_defined = \
    $(strip $(foreach 1,$1, \
        $(call __check_defined,$1,$(strip $(value 2)))))
__check_defined = \
    $(if $(value $1),, \
      $(error Undefined $1$(if $2, ($2)): please pass as argument (see help target)))

define BROWSER_PYSCRIPT
import os, webbrowser, sys
try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT
BROWSER := python -c "$$BROWSER_PYSCRIPT"

#################################################################
# help
#################################################################

help:
	@echo "SETUP TARGETS:"
	@echo "setup-dev-env-minimal - setup minimal dev environment for all make targets to work"
	@echo "setup-dev-env-full - setup full dev environment to allow IDE completion"
	@echo "setup-pre-commit-hooks - setup pre-commit hooks"
	@echo "setup-release-tools: - setup tools needed for releasing pachage"
	@echo ""
	@echo "MAIN TARGETS:"
	@echo "clean - remove all build, test, coverage and Python artifacts"
	@echo "tox - run tox default targets, usually all tests and checks (see tox.ini)"
	@echo "repl - run the repl tool (bpython in our case)"
	@echo "lint - check style with flake8 (uses tox)"
	@echo "format-check - check format for correctness with isort and black (uses tox)"
	@echo "format - enforce correct format with isort (after a seed-isort-config) and black (does not use tox)"
	@echo "type - checks Python typing (uses tox)"
	@echo "test - run tests quickly with the default Python (3.7 - uses tox)"
	@echo "test-all - run tests on every Python version declared (uses tox)"
	@echo "bdd - run bdd tests (uses tox)"
	@echo "coverage - [TO BE IMPLEMENTED] check code coverage quickly with the default Python"
	@echo "docs - generate Sphinx HTML documentation, including API docs"
	@echo "ci-cd-release - full release - through ci/cd"
	@echo "release - [TO BE IMPLEMENTED] full release - from local (requires linux)"
	@echo "bump NEXT_VERSION=[next_version] - bump versions in all relevant files"
	@echo "publish - publish package to pypi"
	@echo "dist - [TO BE IMPLEMENTED] package"
	@echo "install - install the package to the active Python's site-packages"
	@echo ""
	@echo "SECONDARY TARGETS:"
	@echo "clean-build - remove build artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "clean-test - remove test and coverage artifacts"
	@echo "clean-venv - remove poetry's virtualenv"
	@echo "py36 - run tests quickly with the default Python 3.6 (uses tox)"
	@echo "py37 - run tests quickly with the default Python 3.7 (uses tox)"
	@echo "py38 - run tests quickly with the default Python 3.8 (uses tox)"
	@echo "seed-isort - run seed-isort-config (does not use tox)"
	@echo "isort - run isort to sort imports (does not use tox)"
	@echo "black - run black the uncompromising code formatter (does not use tox)"
	@echo ""
	@echo "GIT TARGETS:"
	@echo "prune-branches - prune obsolete local tracking branches"


#################################################################
# setting up dev env
#################################################################

setup-dev-env-minimal: clean
	poetry install --no-root -E format -E repl

setup-dev-env-full: clean
	poetry install --no-root -E test -E bdd -E type -E format -E lint -E repl

setup-pre-commit-hooks:
	pre-commit install --hook-type pre-commit

setup-release-tools:
	npm install -g semantic-release@"^17.0.4"
	npm install -g @semantic-release/changelog@"^5.0.0"
	npm install -g @semantic-release/exec@"^5.0.0"
	npm install -g @semantic-release/git@"^9.0.0"
	npm install -g @semantic-release/gitlab@"^6.0.2"

#################################################################
# cleaning
#################################################################

clean: clean-build clean-pyc clean-test

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/

clean-venv:
	# poetry env remove might not to work if `virtualenvs.in-project = true`
	# (see https://github.com/python-poetry/poetry/issues/2124)
	# so if not, remove whole `.venv` directory using https://unix.stackexchange.com/questions/153763
	poetry env remove $$(poetry env info -p)/bin/python && ([ $$? -eq 0 ]) || rm -rf $$(poetry env info -p)


#################################################################
# all tests and checks
#################################################################

tox:
	poetry run tox

#################################################################
# repl
#################################################################

repl:
	poetry run bpython

#################################################################
# linting
#################################################################

lint:
	poetry run tox -e lint

#################################################################
# formating
#################################################################

format-check:
	poetry run tox -e format

format: seed-isort isort black

seed-isort:
	-poetry run seed-isort-config

isort:
	poetry run isort -rc $(PACKAGE_DIR) tests features -vb

black:
	poetry run black $(PACKAGE_DIR) tests features

#################################################################
# typing
#################################################################

type:
	poetry run tox -e type

#################################################################
# unit testing
#################################################################

test: py37

py37:
	poetry run tox -e py37

py36:
	poetry run tox -e py36

py38:
	poetry run tox -e py38

test-all:
	poetry run tox -e py37,py36,py38

#################################################################
# acceptance testing / bdd
#################################################################

bdd:
	poetry run tox -e bdd

#################################################################
# coverage
#################################################################

# To use/adjust when we start using coverage. Encourage usage of tox.
#coverage:
#	coverage run --source leviathan_serving setup.py test
#	coverage report -m
#	coverage html
#	$(BROWSER) htmlcov/index.html

#################################################################
# docs
#################################################################

docs:
	poetry run tox -e docs
	$(BROWSER) docs/_build/html/index.html

# To use/adjust when we start using coverage. Encourage usage of tox.
#servedocs: docs
#	watchmedo shell-command -p '*.rst' -c '$(MAKE) -C docs html' -R -D .

#################################################################
# releasing (full cycle)
#################################################################

ci-cd-release:
	npx semantic-release

# To use/adjust when we start using coverage. Use Poetry.
#release: clean
#	python setup.py sdist upload
#	python setup.py bdist_wheel upload

#################################################################
# releasing (steps)
#################################################################

# TODO make it more error proof, meaning:
#  - errors if file not found, if item in file not found
#  - use regex to find first item instead of using ${1}
bump:
	$(call check_defined, NEW_VERSION)
	poetry version $(NEW_VERSION)
	pip install toml
	poetry run python ./scripts/generate_version_file.py

# To use/adjust when we start using coverage. Use Poetry.
#dist: clean
#	python setup.py sdist
#	python setup.py bdist_wheel
#	ls -l dist

publish: clean
	poetry publish --build -r $$PYPI_REPOSITORY_NAME -u $$PYPI_USERNAME -p $$PYPI_PASSWORD

#################################################################
# installing developed package/library
#################################################################

install: clean
	poetry install --no-dev

#################################################################
# git targets
#################################################################

prune-branches:
	git remote prune origin
	git branch -vv | grep ': gone]'|  grep -v "\*" | awk '{ print $$1; }' | xargs git branch -d
