#!/usr/bin/bash -eux
rpmbuild -ba pythonname.spec

XY=$(rpm --eval '%python3_version_nodots')
RPMDIR=$(rpm --eval '%_topdir')/RPMS/noarch

echo "Provides for python${XY}-foo"
rpm -qp --provides ${RPMDIR}/python${XY}-foo-0-0.noarch.rpm
rpm -qp --provides ${RPMDIR}/python${XY}-foo-0-0.noarch.rpm | grep -q '^python-foo = 0-0$'
rpm -qp --provides ${RPMDIR}/python${XY}-foo-0-0.noarch.rpm | grep -q '^python3-foo = 0-0$'

echo "Provides for python3-foo"
rpm -qp --provides ${RPMDIR}/python3-foo-0-0.noarch.rpm
rpm -qp --provides ${RPMDIR}/python3-foo-0-0.noarch.rpm     | grep -q '^python-foo = 0-0$'
rpm -qp --provides ${RPMDIR}/python3-foo-0-0.noarch.rpm     | grep -q '^python'${XY}'-foo = 0-0$'

echo "Provides for python2-foo"
rpm -qp --provides ${RPMDIR}/python2-foo-0-0.noarch.rpm
rpm -qp --provides ${RPMDIR}/python2-foo-0-0.noarch.rpm     | grep -q '^python-foo = 0-0$' && exit 1 || true

echo "Provides for python-foo"
rpm -qp --provides ${RPMDIR}/python-foo-0-0.noarch.rpm
rpm -qp --provides ${RPMDIR}/python-foo-0-0.noarch.rpm      | grep -q '^python2-foo = 0-0$' && exit 1 || true

echo "Provides for python35-foo"
rpm -qp --provides ${RPMDIR}/python35-foo-0-0.noarch.rpm
rpm -qp --provides ${RPMDIR}/python35-foo-0-0.noarch.rpm    | grep -q '^python-foo = 0-0$' && exit 1 || true
rpm -qp --provides ${RPMDIR}/python35-foo-0-0.noarch.rpm    | grep -q '^python3-foo = 0-0$' && exit 1 || true
