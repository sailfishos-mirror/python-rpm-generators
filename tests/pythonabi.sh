#!/usr/bin/bash -eux
rpmbuild -ba pythonabi.spec

PYVER=$(rpm --eval '%python3_version')
RPMDIR=$(rpm --eval '%_topdir')/RPMS
ARCH=$(rpm --eval '%_arch')
ABI='^python(abi) = '${PYVER}'$'

rpm -qp --provides ${RPMDIR}/${ARCH}/python-interpreter-0-0.${ARCH}.rpm | grep "${ABI}"
rpm -qp --requires ${RPMDIR}/${ARCH}/python-interpreter-0-0.${ARCH}.rpm | grep -v "${ABI}"

rpm -qp --requires ${RPMDIR}/${ARCH}/python-arched-0-0.${ARCH}.rpm | grep "${ABI}"
rpm -qp --provides ${RPMDIR}/${ARCH}/python-arched-0-0.${ARCH}.rpm | grep -v "${ABI}"

rpm -qp --requires ${RPMDIR}/noarch/python-noarch-0-0.noarch.rpm | grep "${ABI}"
rpm -qp --provides ${RPMDIR}/noarch/python-noarch-0-0.noarch.rpm | grep -v "${ABI}"

rpm -qp --provides ${RPMDIR}/${ARCH}/python-misplaced-interpreter-0-0.${ARCH}.rpm | grep -v "${ABI}"
rpm -qp --requires ${RPMDIR}/noarch/python-misplaced-library-0-0.noarch.rpm | grep -v "${ABI}"
