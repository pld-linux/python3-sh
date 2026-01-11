#
# Conditional build:
%bcond_without	tests	# functional tests

%define 	module		sh
Summary:	Python subprocess replacement
Summary(pl.UTF-8):	Zamiennik modułu subprocess dla Pythona
Name:		python3-%{module}
Version:	2.2.2
Release:	1
License:	MIT
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/s/sh/%{module}-%{version}.tar.gz
# Source0-md5:	961d38de16f88556bd70381eddd7f415
URL:		https://pypi.org/project/sh/
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.8.1
BuildRequires:	python3-poetry-core >= 1.0.0
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest >= 7.4.0
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.8.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
sh is a full-fledged subprocess replacement for Python 3 and PyPy that
allows you to call any program as if it were a function.

%description -l pl.UTF-8
sh to w pełni rozwinięty zamiennik modułu subprocess dla Pythona 3 i
PyPy, pozwalający na wywołanie dowolnego programu tak, jakby był
funkcją.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build_pyproject

%if %{with tests}
PYTHONPATH=$(pwd) \
%{__python3} tests/sh_test.py
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE.txt MIGRATION.md README.rst
%{py3_sitescriptdir}/sh.py
%{py3_sitescriptdir}/__pycache__/sh.cpython-*.pyc
%{py3_sitescriptdir}/%{module}-%{version}.dist-info
