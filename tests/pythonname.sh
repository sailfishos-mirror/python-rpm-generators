#!/usr/bin/bash -eux
rpmbuild -ba pythonname.spec

X_Y=$(rpm --eval '%python3_version')
RPMDIR=$(rpm --eval '%_topdir')/RPMS/noarch

echo "Provides for python${X_Y}-foo"
rpm -qp --provides ${RPMDIR}/python${X_Y}-foo-0-0.noarch.rpm
rpm -qp --provides ${RPMDIR}/python${X_Y}-foo-0-0.noarch.rpm | grep -q '^python-foo = 0-0$'
rpm -qp --provides ${RPMDIR}/python${X_Y}-foo-0-0.noarch.rpm | grep -q '^python3-foo = 0-0$'

echo "Provides for python3-foo"
rpm -qp --provides ${RPMDIR}/python3-foo-0-0.noarch.rpm
rpm -qp --provides ${RPMDIR}/python3-foo-0-0.noarch.rpm     | grep -q '^python-foo = 0-0$'
rpm -qp --provides ${RPMDIR}/python3-foo-0-0.noarch.rpm     | grep -q '^python'${X_Y}'-foo = 0-0$'

echo "Provides for python2-foo"
rpm -qp --provides ${RPMDIR}/python2-foo-0-0.noarch.rpm
rpm -qp --provides ${RPMDIR}/python2-foo-0-0.noarch.rpm     | grep -q '^python-foo = 0-0$' && exit 1 || true

echo "Provides for python-foo"
rpm -qp --provides ${RPMDIR}/python-foo-0-0.noarch.rpm
rpm -qp --provides ${RPMDIR}/python-foo-0-0.noarch.rpm      | grep -q '^python2-foo = 0-0$' && exit 1 || true

echo "Provides for python3.5-foo"
rpm -qp --provides ${RPMDIR}/python3.5-foo-0-0.noarch.rpm
rpm -qp --provides ${RPMDIR}/python3.5-foo-0-0.noarch.rpm    | grep -q '^python-foo = 0-0$' && exit 1 || true
rpm -qp --provides ${RPMDIR}/python3.5-foo-0-0.noarch.rpm    | grep -q '^python3-foo = 0-0$' && exit 1 || true

echo "Provides for python3-python_provide"
rpm -qp --provides ${RPMDIR}/python3-python_provide-0-0.noarch.rpm
test $(rpm -qp --provides ${RPMDIR}/python3-python_provide-0-0.noarch.rpm | grep python-python_provide | wc -l) -eq 1

echo "Provides for python3-py_provides"
rpm -qp --provides ${RPMDIR}/python3-py_provides-0-0.noarch.rpm
test $(rpm -qp --provides ${RPMDIR}/python3-py_provides-0-0.noarch.rpm | grep python-py_provides | wc -l) -eq 1
