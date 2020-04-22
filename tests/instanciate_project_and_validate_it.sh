#!/bin/bash

set -ex

# Prepare directories
if [ ! -z $1 ]; then
  COOKIE_DIR=$1
else
  COOKIE_DIR=$PWD
fi

mkdir -p /projects
cd /projects

# Instanciate project
cookiecutter --default-config --no-input ${COOKIE_DIR}
cd a-generated-python-project

# Install dev env
make setup-dev-host
source $HOME/.bashrc
make setup-dev-env-minimal

# Build project
make tox
