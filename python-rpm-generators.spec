# This package is part of the Python 3 bootstrapping sequence.
#
# The python3-devel subpackage has a runtime dependency on this package.
# Therefore it needs to be built before Python 3 itself. To facilitate this,
# this package has a bootstrapping mode—triggered by the macro below—that skips
# bytecompilation and therefore no Python is actually needed for building of
# this package. After Python 3 is built, this package can be rebuilt in
# normal mode again.
#
# Note, however, that even the bootstrapping version of this package is fully
# functional as Python will simply bytecompile the Python files when they are
# run. There will be a warning that the bytecompiled file cannot be saved
# (unless Python is run with root privileges), but the script will work.
#
# More info on the Python 3 bootstrapping sequence in the `python3` spec file.
#
%global bootstrapping_python 0


# Disable automatic (Python 2) bytecompilation in %%__os_install_post.
# When not in bootstrapping mode, the scripts are bytecompiled
# in the %%install section.
%undefine py_auto_byte_compile

%global srcname rpm

# These macros are copied from the `rpm` package so it's trivial to keep
# the two packages on the same upstream version.
%global rpmver 4.14.0
#global snapver rc2
%global rel 1

%global srcver %{version}%{?snapver:-%{snapver}}
%global srcdir %{?snapver:testing}%{!?snapver:rpm-%(echo %{version} | cut -d'.' -f1-2).x}

Name:           python-rpm-generators
Summary:        Requires and Provides generators for Python RPMs
Version:        %{rpmver}
Release:        %{?snapver:0.%{snapver}.}%{rel}%{?dist}
License:        GPLv2+
Url:            http://www.rpm.org/
Source0:        http://ftp.rpm.org/releases/%{srcdir}/%{srcname}-%{srcver}.tar.bz2

BuildArch:      noarch

%if ! 0%{?bootstrapping_python}
BuildRequires:  python3-devel
%endif

# Enable rich Provides generator (pythondistdeps.py instead of pythondeps.sh)
# Downstream only
Patch1: rpm-4.13.x-pythondistdeps-fileattr.patch
# Switch the shebang of pythondistdeps.py to Python 3
# Downstream only: https://github.com/rpm-software-management/rpm/pull/212
Patch2: rpm-4.13.x-pythondistdeps-python3.patch

# Handle Platform-Python implemented as a separate Python stack
# https://fedoraproject.org/wiki/Changes/Platform_Python_Stack
Patch3: rpm-4.13.x-pythondeps-platform-python-abi.patch
Patch4: rpm-4.13.x-pythondistdeps.py-platform-python.patch

%description
This package provides scripts that analyse Python binary RPM packages
and add appropriate Provides and Requires tags to them.


%package -n     python3-rpm-generators
Summary:        %{summary}
Requires:       python3-setuptools
# We're installing files into rpm's directories, therefore we're requiring it
# to be installed so the directories are created.
Requires:       rpm
# Conflicts with older versions of `rpm-build` because it copies several files
# to the same locations which is ok only when they have the same contents.
Conflicts:      rpm-build < 4.13.0.1-2
%{?python_provide:%python_provide python3-rpm-generators}

%description -n python3-rpm-generators
This package provides scripts that analyse Python binary RPM packages
and add appropriate Provides and Requires tags to them.


%prep
%autosetup -n %{srcname}-%{srcver} -p1


%build
%if ! 0%{?bootstrapping_python}
%{__python3} -m compileall scripts/
%endif


%install
install -Dm 644 fileattrs/python.attr -t %{buildroot}/%{_fileattrsdir}
install -Dm 755 scripts/pythondeps.sh \
                scripts/pythondistdeps.py \
                -t %{buildroot}/%{_rpmconfigdir}

%if ! 0%{?bootstrapping_python}
install -Dm 755 scripts/__pycache__/* \
                -t %{buildroot}/%{_rpmconfigdir}/__pycache__
%endif


%files -n python3-rpm-generators
%license COPYING
%{_fileattrsdir}/python.attr
%{_rpmconfigdir}/pythondeps.sh
%{_rpmconfigdir}/pythondistdeps.py

%if ! 0%{?bootstrapping_python}
%{_rpmconfigdir}/__pycache__
%endif


%changelog
* Fri Oct 20 2017 Tomas Orsava <torsava@redhat.com> - 4.14.0-1
- Rebase to rpm 4.14.0 final (http://rpm.org/wiki/Releases/4.14.0)
- Re-synchronize version/release macros with the rpm Fedora package

* Mon Sep 18 2017 Tomas Orsava <torsava@redhat.com> - 4.14.0-0.rc1.1
- Update to a new upstream version of RPM
- Drop upstreamed patches
- Renumber remaining patches

* Thu Aug 24 2017 Miro Hrončok <mhroncok@redhat.com> - 4.13.0.1-4
- Add patch 10: Do not provide pythonXdist for platform-python packages (rhbz#1484607)

* Tue Aug 08 2017 Tomas Orsava <torsava@redhat.com> - 4.13.0.1-3
- Add patch 9: Generate requires and provides for platform-python(abi)
  (https://fedoraproject.org/wiki/Changes/Platform_Python_Stack)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.0.1-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May 18 2017 Tomas Orsava <torsava@redhat.com> - 4.13.0.1-2
- Added a license file
- Added a dependency on rpm for the proper directory structure
- Properly owning the __pycache__ directory

* Tue May 02 2017 Tomas Orsava <torsava@redhat.com> - 4.13.0.1-1
- Splitting Python RPM generators from the `rpm` package to standalone one
