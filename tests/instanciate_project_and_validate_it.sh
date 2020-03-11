#!/bin/bash

set -e

echo "Running tests"

mkdir -p /app
cd /app

echo "Instanciate project"
cookiecutter --default-config --no-input /template
cd python_boilerplate

echo "Install dev env"
make setup-dev-host

# Don't remove 4 following lines until bugfix in docker container :
# The 4 following lines should not be here, but currently, we don't know why .bashrc file is not loaded
# in test docker container.
export PATH="/root/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
. /root/.poetry/env

make setup-dev-env-minimal

echo "Build project"
make tox
