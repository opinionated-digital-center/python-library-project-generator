#!/bin/bash

SCRIPT_DIR=$(dirname $0)

pushd ${SCRIPT_DIR} > /dev/null

docker build -t cookie-test . -f ./Dockerfile.tests
docker run --rm -it -v $(pwd)/..:/template cookie-test /template/tests/instanciate_project_and_validate_it.sh

popd > /dev/null