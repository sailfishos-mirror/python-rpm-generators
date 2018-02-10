# Disable automatic bytecompilation. We install only one script and we will
# never "import" it.
%undefine py_auto_byte_compile

Name:           python-rpm-generators
Summary:        Dependency generators for Python RPMs
Version:        5
Release:        1%{?dist}

# Originally all those files were part of RPM, so license is kept here
License:        GPLv2+
Url:            https://src.fedoraproject.org/python-rpm-generators
# Commit is the last change in following files
Source0:        https://raw.githubusercontent.com/rpm-software-management/rpm/102eab50b3d0d6546dfe082eac0ade21e6b3dbf1/COPYING
Source1:        python.attr
Source2:        pythondeps.sh
Source3:        pythondistdeps.py

BuildArch:      noarch

%description
%{summary}.

%package -n python3-rpm-generators
Summary:        %{summary}
Requires:       python3-setuptools
# The point of split
Conflicts:      rpm-build < 4.13.0.1-2

%description -n python3-rpm-generators
%{summary}.

%prep
%autosetup -c -T
cp -a %{sources} .

%install
install -Dpm0644 -t %{buildroot}%{_fileattrsdir} python.attr
install -Dpm0755 -t %{buildroot}%{_rpmconfigdir} pythondeps.sh pythondistdeps.py

%files -n python3-rpm-generators
%license COPYING
%{_fileattrsdir}/python.attr
%{_rpmconfigdir}/pythondeps.sh
%{_rpmconfigdir}/pythondistdeps.py

%changelog
* Sun Feb 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 5-1
- Fork upstream generators
- "Fix" support of environment markers

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.14.0-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 28 2017 Tomas Orsava <torsava@redhat.com> - 4.14.0-2
- Switch bootsrapping macro to a bcond for modularity

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
