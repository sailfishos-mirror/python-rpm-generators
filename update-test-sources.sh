#!/bin/bash

#
# Requirements:
# - pip >= 20.0.1
# - poetry   # Due to bug: https://github.com/pypa/pip/issues/9701
#

# First prune old test data
rm -rf ./tests/data/scripts_pythondistdeps/usr

# First run the test suite, it will download the test-data again
python3 -m pytest --capture=no -vvv

# Archive the test data into a file with today's date
archive=test-sources-$(date +%Y-%m-%d).tar.gz
tar -zcvf ${archive} -C ./tests/data/scripts_pythondistdeps/ usr

# Now manually run:
# $ fedpkg new-sources ${archive}
