Name:           python-rpm-generators
Summary:        Dependency generators for Python RPMs
Version:        12
Release:        5%{?dist}

# Originally all those files were part of RPM, so license is kept here
License:        GPLv2+
Url:            https://src.fedoraproject.org/python-rpm-generators
# Commit is the last change in following files
Source0:        https://raw.githubusercontent.com/rpm-software-management/rpm/102eab50b3d0d6546dfe082eac0ade21e6b3dbf1/COPYING
Source1:        python.attr
Source2:        pythondist.attr
Source3:        pythonname.attr
Source4:        pythondistdeps.py
Source5:        pythonbundles.py

BuildArch:      noarch

%description
%{summary}.

%package -n python3-rpm-generators
Summary:        %{summary}
Requires:       python3-packaging
# We have parametric macro generators, we need RPM 4.16 (4.15.90+ is 4.16 alpha)
Requires:       rpm > 4.15.90-0
# This contains the Lua functions we use:
Requires:       python-srpm-macros >= 3.8-5

%description -n python3-rpm-generators
%{summary}.

%prep
%autosetup -c -T
cp -a %{sources} .

%install
install -Dpm0644 -t %{buildroot}%{_fileattrsdir} *.attr
install -Dpm0755 -t %{buildroot}%{_rpmconfigdir} *.py

%files -n python3-rpm-generators
%license COPYING
%{_fileattrsdir}/python.attr
%{_fileattrsdir}/pythondist.attr
%{_fileattrsdir}/pythonname.attr
%{_rpmconfigdir}/pythondistdeps.py
%{_rpmconfigdir}/pythonbundles.py

%changelog
* Wed Mar 31 2021 Miro Hrončok <mhroncok@redhat.com> - 12-5
- Do not generate setuptools requirement for console_scripts on Python 3.10+
- See https://fedoraproject.org/wiki/Changes/Reduce_dependencies_on_python3-setuptools

* Thu Mar 11 2021 Tomas Orsava <torsava@redhat.com> - 12-4
- scripts/pythondistdeps: Treat extras names case-insensitively and always
  output them in lower case (#1936875)

* Mon Feb 22 2021 Tomas Orsava <torsava@redhat.com> - 12-3
- scripts/pythondistdeps: Fix for Python 3.10

* Wed Feb 17 2021 Tomas Orsava <torsava@redhat.com> - 12-2
- scripts/pythondistdeps: Switch from using pkg_resources to importlib.metadata
  for reading the egg/dist-info metadata
- The script no longer requires setuptools but instead requires packaging

* Wed Feb 03 2021 Miro Hrončok <mhroncok@redhat.com> - 12-1
- Disable the dist generators for Python 2
- https://fedoraproject.org/wiki/Changes/Disable_Python_2_Dist_RPM_Generators_and_Freeze_Python_2_Macros

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 11-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct 19 2020 Tomas Orsava <torsava@redhat.com> - 11-12
- Run scripts in an isolated Python environment (#1889080)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 2020 Miro Hrončok <mhroncok@redhat.com> - 11-10
- pythondistdeps: Split Python Extras names after the rightmost plus sign
- pythondistdeps: Handle edge cases of version comparisons more closely to
  upstream, despite irrationality
  See: https://github.com/pypa/packaging/issues/320

* Fri Jul 10 2020 Tomas Orsava <torsava@redhat.com> - 11-9
- pythondistdeps: Implement provides/requires for extras packages
- Enable --require-extras-subpackages
- Adapt Python version marker workaround for setuptools 42+

* Fri Jun 26 2020 Miro Hrončok <mhroncok@redhat.com> - 11-8
- Fix python(abi) requires generator, it picked files from almost good directories
- Add a script to generate Python bundled provides

* Thu May 21 2020 Miro Hrončok <mhroncok@redhat.com> - 11-7
- Use PEP 503 names for requires

* Tue May 05 2020 Miro Hrončok <mhroncok@redhat.com> - 11-6
- Deduplicate automatically provided names trough Python RPM Lua macros

* Wed Apr 29 2020 Tomas Orsava <torsava@redhat.com> - 11-5
- Backporting proposed upstream changes
  https://github.com/rpm-software-management/rpm/pull/1195
  - Only provide python3dist(..) for the main Python versions (BZ#1812083)
  - Preparation for the proper handling of normalized names (BZ#1791530)
  - Add a test suite (and enable it in Fedora CI)
  - Better error messages for unsupported package versions
  - Fix sorting of dev versions

* Tue Apr 28 2020 Miro Hrončok <mhroncok@redhat.com> - 11-4
- Don't define global Lua variables from Python generator

* Mon Apr 20 2020 Gordon Messmer <gordon.messmer@gmail.com> - 11-3
- Handle all-zero versions without crashing

* Tue Apr 07 2020 Miro Hrončok <mhroncok@redhat.com> - 11-2
- Use dynamic %%_prefix value when matching files for python(abi) provides
- Sync with upstream RPM dist generator

* Wed Apr 01 2020 Miro Hrončok <mhroncok@redhat.com> - 11-1
- Rewrite python(abi) generators to Lua to make them faster
- RPM 4.16+ is needed
- Automatically call %%python_provide

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Miro Hrončok <mhroncok@redhat.com> - 10-3
- Also provide pythonXdist() with PEP 503 normalized names (#1791530)

* Fri Jan 03 2020 Miro Hrončok <mhroncok@redhat.com> - 10-2
- Fix more complicated requirement expressions by adding parenthesis

* Wed Jan 01 2020 Miro Hrončok <mhroncok@redhat.com> - 10-1
- Handle version ending with ".*" (#1758141)
- Handle compatible-release operator "~=" (#1758141)
- Use rich deps for semantically versioned dependencies
- Match Python version if minor has multiple digits (e.g. 3.10, #1777382)
- Only add setuptools requirement for egg-info packages

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 24 2019 Tomas Orsava <torsava@redhat.com> - 9-1
- Canonicalize Python versions and properly handle != spec

* Wed Apr 17 2019 Miro Hrončok <mhroncok@redhat.com> - 8-1
- console_scripts entry points to require setuptools
  https://github.com/rpm-software-management/rpm/pull/666

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 20 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 7-1
- Enable requires generator

* Wed Oct 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 6-1
- Tighten regex for depgen

* Sat Jul 28 2018 Miro Hrončok <mhroncok@redhat.com> - 5-4
- Use nonstandardlib for purelib definition (#1609492)

* Sat Jul 28 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 5-3
- Add pythondist generator

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

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
