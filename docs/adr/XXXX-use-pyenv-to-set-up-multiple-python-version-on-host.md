# Use PyEnv to set up multiple Python version on host

* Status: proposed
* Date: 2020-04-07

## Context and Problem Statement

Testing python projects requires must often be done on multiple versions of Python on
the host development machine, which can be cumbersome. As a reminder, at time of
writing, we only actively support linux, MacOS, and POSIX unix systems.


## Decision Drivers <!-- optional -->


## Considered Options

* [PyEnv](https://github.com/pyenv/pyenv)
* Install each version manually (through various means, be through package management
  tools or by downloading and installing libraries)
  *

## Decision Outcome

Chosen option: "PyEnv", because it allows to manage the full workflow of installing and
uninstalling Python versions.
