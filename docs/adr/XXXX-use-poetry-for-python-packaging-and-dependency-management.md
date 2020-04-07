# Use Poetry for Python packaging and dependency management

* Status: proposed
* Date: 2020-04-07

## Context and Problem Statement

Standard `setuptool` forces up to use 5 different files to create a package, making it
quite complicated to create packages. we want to find an alternative.

## Considered Options

* [Poetry](https://python-poetry.org/)
* [PipEnv](https://pipenv.pypa.io/en/latest/)
* Stick with [`setuptools`](https://setuptools.readthedocs.io/en/latest/)

## Decision Outcome

Chosen option: "Poetry", because of all the arguments detailed in one of the articles
that helped us decide: [A deeper look into Pipenv and Poetry](https://frostming.com/2019/01-04/pipenv-poetry)

## Links

* [Tutorial] [Package Python Projects the Proper Way with Poetry](https://hackersandslackers.com/python-poetry-package-manager/)
