#!/bin/bash

SCRIPT_DIR=$(dirname $0)

pushd ${SCRIPT_DIR} > /dev/null

# build docker image only is not already build (see https://stackoverflow.com/a/46425380/4374048)
if [[ "$(docker images -q cookie-test 2> /dev/null)" == "" ]]; then
  docker build -t cookie-test . -f ./Dockerfile
fi
BASE_DIR="/template"
docker run --rm -it -v $(pwd)/..:${BASE_DIR} cookie-test ${BASE_DIR}/tests/instanciate_project_and_validate_it.sh ${BASE_DIR}

popd > /dev/null
