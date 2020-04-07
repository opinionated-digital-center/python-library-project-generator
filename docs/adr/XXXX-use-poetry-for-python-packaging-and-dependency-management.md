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

### Positive Consequences <!-- optional -->

* [e.g., improvement of quality attribute satisfaction, follow-up decisions required, ...]
* ...

### Negative Consequences <!-- optional -->

* [e.g., compromising quality attribute, follow-up decisions required, ...]
* ...

## Pros and Cons of the Options <!-- optional -->

### [option 1]

[example | description | pointer to more information | ...] <!-- optional -->

* Good, because [argument a]
* Good, because [argument b]
* Bad, because [argument c]
* ... <!-- numbers of pros and cons can vary -->

### [option 2]

[example | description | pointer to more information | ...] <!-- optional -->

* Good, because [argument a]
* Good, because [argument b]
* Bad, because [argument c]
* ... <!-- numbers of pros and cons can vary -->

### [option 3]

[example | description | pointer to more information | ...] <!-- optional -->

* Good, because [argument a]
* Good, because [argument b]
* Bad, because [argument c]
* ... <!-- numbers of pros and cons can vary -->

## Links

* [Tutorial] [Package Python Projects the Proper Way with Poetry](https://hackersandslackers.com/python-poetry-package-manager/)
* [Link type] [Link to ADR] <!-- example: Refined by [ADR-0005](0005-example.md) -->
* ... <!-- numbers of links can vary -->
