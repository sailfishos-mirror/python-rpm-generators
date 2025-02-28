#!/usr/bin/bash -eux
# Use update-test-sources.sh to update the test data

# When the tests run in python-rpm-generators,
# the structure on disk does not match the dist-git repository.
# We apparently must use the standard-test-source role to grab the sources.
# OTOH in other packages, we must use fedpkg(-minimal) or centpkg(-minimal),
# depending on the destination OS.
# The --force flag is required in full-blown fedpkg/centpkg (the source is unused in spec),
# and it is ignored in fedpkg/centpkg-minimal (all sources are always downloaded).
test -f test-sources-*.tar.gz || fedpkg sources --force || centpkg sources --force

tar -xvf test-sources-*.tar.gz -C ./tests/data/scripts_pythondistdeps/
cd tests/
python3 -m pytest -vvv
