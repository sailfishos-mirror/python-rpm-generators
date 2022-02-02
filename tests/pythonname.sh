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


echo "Obsoletes for python${X_Y}-foo"
rpm -qp --obsoletes ${RPMDIR}/python${X_Y}-foo-0-0.noarch.rpm
test $(rpm -qp --obsoletes ${RPMDIR}/python${X_Y}-foo-0-0.noarch.rpm | wc -l) -eq 0

echo "Obsoletes for python3-foo"
rpm -qp --obsoletes ${RPMDIR}/python3-foo-0-0.noarch.rpm
# In ELN/RHEL the pythonX.Y-* Obsoletes is generated, but not in Fedora, so we check for it explicitly.
rpm -qp --obsoletes ${RPMDIR}/python3-foo-0-0.noarch.rpm | grep -q '^python'${X_Y}'-py_provides < 0-0$' && exit 1 || true
test $(rpm -qp --obsoletes ${RPMDIR}/python3-foo-0-0.noarch.rpm | wc -l) -eq 0

echo "Obsoletes for python2-foo"
rpm -qp --obsoletes ${RPMDIR}/python2-foo-0-0.noarch.rpm
test $(rpm -qp --obsoletes ${RPMDIR}/python2-foo-0-0.noarch.rpm | wc -l) -eq 0

echo "Obsoletes for python-foo"
rpm -qp --obsoletes ${RPMDIR}/python-foo-0-0.noarch.rpm
test $(rpm -qp --obsoletes ${RPMDIR}/python-foo-0-0.noarch.rpm | wc -l) -eq 0

echo "Obsoletes for python3.5-foo"
rpm -qp --obsoletes ${RPMDIR}/python3.5-foo-0-0.noarch.rpm
test $(rpm -qp --obsoletes ${RPMDIR}/python3.5-foo-0-0.noarch.rpm | wc -l) -eq 0

echo "Obsoletes for python3-python_provide"
rpm -qp --obsoletes ${RPMDIR}/python3-python_provide-0-0.noarch.rpm
# The deprecated %python_provide macro always obsoletes python-foo
rpm -qp --obsoletes ${RPMDIR}/python3-python_provide-0-0.noarch.rpm     | grep -q '^python-python_provide < 0-0$'
# In ELN/RHEL the pythonX.Y-* Obsoletes is generated, but not in Fedora, so we check for it explicitly.
rpm -qp --obsoletes ${RPMDIR}/python3-python_provide-0-0.noarch.rpm     | grep -q '^python'${X_Y}'-python_provide < 0-0$' && exit 1 || true
test $(rpm -qp --obsoletes ${RPMDIR}/python3-python_provide-0-0.noarch.rpm | grep python-python_provide | wc -l) -eq 1
test $(rpm -qp --obsoletes ${RPMDIR}/python3-python_provide-0-0.noarch.rpm | wc -l) -eq 1

echo "Obsoletes for python3-py_provides"
rpm -qp --obsoletes ${RPMDIR}/python3-py_provides-0-0.noarch.rpm
rpm -qp --obsoletes ${RPMDIR}/python3-py_provides-0-0.noarch.rpm        | grep -q '^python-py_provides < 0-0$' && exit 1 || true
# In ELN/RHEL the pythonX.Y-* Obsoletes is generated, but not in Fedora, so we check for it explicitly.
rpm -qp --obsoletes ${RPMDIR}/python3-py_provides-0-0.noarch.rpm        | grep -q '^python'${X_Y}'-py_provides < 0-0$' && exit 1 || true
test $(rpm -qp --obsoletes ${RPMDIR}/python3-py_provides-0-0.noarch.rpm | wc -l) -eq 0

