#!/bin/bash

which poetry && ([ $? -eq 0 ]) || curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
