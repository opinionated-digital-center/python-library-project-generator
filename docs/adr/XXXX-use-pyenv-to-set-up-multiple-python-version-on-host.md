# Use PyEnv to set up multiple Python version on host

* Status: proposed
* Date: 2020-04-07

## Context and Problem Statement

It is common that multiple versions of Python need to be install on development
machines, which can be cumbersome.

## Decision Drivers <!-- optional -->

As a reminder, at time of writing, ODC only actively support linux, MacOS, and
POSIX unix systems.

## Considered Options

* [PyEnv](https://github.com/pyenv/pyenv).
* [PipEnv](https://github.com/pypa/pipenv).
* Developing on virtual machine or docker containers.
* [altinstall](https://hackersandslackers.com/multiple-versions-python-ubuntu/)
  on Ubuntu, and equivalent on other plateforms
* Install each version manually (through various means, be through package management
  tools or by downloading and installing libraries).

## Decision Outcome

Chosen option: "PyEnv", because it allows to manage the full workflow of installing and
uninstalling Python versions.
