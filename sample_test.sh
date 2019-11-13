#!/bin/bash

set -ex

# Show environment.
gcc --version
# Build logic.
make
# Test logic.
make test
