Name:           pythonname
Version:        0
Release:        0
Summary:        ...
License:        MIT
BuildArch:      noarch

%description
...

%install
touch %{buildroot}/something
touch %{buildroot}/something_else
touch %{buildroot}/something_completely_different


%package -n python-foo
Summary:        ...
%description -n python-foo
...
%files -n python-foo
/*


%package -n python2-foo
Summary:        ...
%description -n python2-foo
...
%files -n python2-foo
/*


%package -n python3-foo
Summary:        ...
%description -n python3-foo
...
%files -n python3-foo
/*


%package -n python%{python3_version_nodots}-foo
Summary:        ...
%description -n python%{python3_version_nodots}-foo
...
%files -n python%{python3_version_nodots}-foo
/*


%package -n python35-foo
Summary:        ...
%description -n python35-foo
...
%files -n python35-foo
/*


%package -n ruby-foo
Summary:        ...
%description -n ruby-foo
...
%files -n ruby-foo
/*
