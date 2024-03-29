#!/usr/bin/bash -eux
X_Y=$(rpm --eval '%python3_version')
RPMDIR=$(rpm --eval '%_topdir')/RPMS/noarch

mkdir -p $(rpm --eval '%_topdir')/SOURCES/

spectool -g -R pythondist.spec
rpmbuild -ba pythondist.spec


rpm -qp --provides ${RPMDIR}/python3-zope-component-4.3.0-0.noarch.rpm | grep '^python3dist(zope\.component)' && exit 1 || true
rpm -qp --provides ${RPMDIR}/python3-zope-component-4.3.0-0.noarch.rpm | grep '^python3dist(zope-component)'
rpm -qp --provides ${RPMDIR}/python3-zope-component-4.3.0-0.noarch.rpm | grep '^python'$X_Y'dist(zope\.component)' && exit 1 || true
rpm -qp --provides ${RPMDIR}/python3-zope-component-4.3.0-0.noarch.rpm | grep '^python'$X_Y'dist(zope-component)'

rpm -qp --requires ${RPMDIR}/python3-zope-component-4.3.0-0.noarch.rpm | grep '^python'$X_Y'dist(zope-event)'
rpm -qp --requires ${RPMDIR}/python3-zope-component-4.3.0-0.noarch.rpm | grep '^python'$X_Y'dist(zope-interface)'


rpm -qp --provides ${RPMDIR}/python3.7-zope-component-4.3.0-0.noarch.rpm | grep '^python3dist(zope\.component)' && exit 1 || true
rpm -qp --provides ${RPMDIR}/python3.7-zope-component-4.3.0-0.noarch.rpm | grep '^python3dist(zope-component)' && exit 1 || true
rpm -qp --provides ${RPMDIR}/python3.7-zope-component-4.3.0-0.noarch.rpm | grep '^python3\.7dist(zope\.component)' && exit 1 || true
rpm -qp --provides ${RPMDIR}/python3.7-zope-component-4.3.0-0.noarch.rpm | grep '^python3\.7dist(zope-component)'

rpm -qp --requires ${RPMDIR}/python3.7-zope-component-4.3.0-0.noarch.rpm | grep '^python3\.7dist(zope-event)'
rpm -qp --requires ${RPMDIR}/python3.7-zope-component-4.3.0-0.noarch.rpm | grep '^python3\.7dist(zope-interface)'

if [ "$X_Y" != "3.9" ]; then
rpm -qp --provides ${RPMDIR}/python3.9-zope-component-4.3.0-0.noarch.rpm | grep '^python3dist(zope\.component)' && exit 1 || true
rpm -qp --provides ${RPMDIR}/python3.9-zope-component-4.3.0-0.noarch.rpm | grep '^python3dist(zope-component)' && exit 1 || true
rpm -qp --provides ${RPMDIR}/python3.9-zope-component-4.3.0-0.noarch.rpm | grep '^python3\.9dist(zope\.component)' && exit 1 || true
rpm -qp --provides ${RPMDIR}/python3.9-zope-component-4.3.0-0.noarch.rpm | grep '^python3\.9dist(zope-component)'

rpm -qp --requires ${RPMDIR}/python3.9-zope-component-4.3.0-0.noarch.rpm | grep '^python3\.9dist(zope-event)'
rpm -qp --requires ${RPMDIR}/python3.9-zope-component-4.3.0-0.noarch.rpm | grep '^python3\.9dist(zope-interface)'
fi

if [ "$X_Y" != "3.10" ]; then
rpm -qp --provides ${RPMDIR}/python3.10-zope-component-4.3.0-0.noarch.rpm | grep '^python3dist(zope\.component)' && exit 1 || true
rpm -qp --provides ${RPMDIR}/python3.10-zope-component-4.3.0-0.noarch.rpm | grep '^python3dist(zope-component)' && exit 1 || true
rpm -qp --provides ${RPMDIR}/python3.10-zope-component-4.3.0-0.noarch.rpm | grep '^python3\.10dist(zope\.component)' && exit 1 || true
rpm -qp --provides ${RPMDIR}/python3.10-zope-component-4.3.0-0.noarch.rpm | grep '^python3\.10dist(zope-component)'

rpm -qp --requires ${RPMDIR}/python3.10-zope-component-4.3.0-0.noarch.rpm | grep '^python3\.10dist(zope-event)'
rpm -qp --requires ${RPMDIR}/python3.10-zope-component-4.3.0-0.noarch.rpm | grep '^python3\.10dist(zope-interface)'
fi
