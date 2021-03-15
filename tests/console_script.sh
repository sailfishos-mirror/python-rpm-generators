#!/usr/bin/bash -eux
RPMDIR=$(rpm --eval '%_topdir')/RPMS/noarch
RPMPKG="${RPMDIR}/isort-5.7.0-0.noarch.rpm"

mkdir -p $(rpm --eval '%_topdir')/SOURCES/

spectool -g -R isort.spec

for py_version in 3.6 3.7 3.8 3.9; do
  rpmbuild -ba --define "python3_test_version ${py_version}" isort.spec
  rpm -qp --requires ${RPMPKG} | grep "python${py_version}dist(setuptools)"
done

for py_version in 3.10 3.11; do
  rpmbuild -ba --define "python3_test_version ${py_version}" isort.spec
  rpm -qp --requires ${RPMPKG} | grep "python${py_version}dist(setuptools)" && exit 1 || true
done
