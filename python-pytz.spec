%define module	pytz


Name:		python-pytz
Summary:	World timezone definitions for Python
Version:	2026.3.post1
Release:	1
License:	MIT
Group:		Development/Python
URL:		https://pythonhosted.org/pytz/
# https://pypi.org/project/pytz/
Source0:	https://files.pythonhosted.org/packages/source/p/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source100:	%{name}.rpmlintrc

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	fdupes
%rename python3-pytz

%description
pytz brings the Olson tz database into Python. This library allows
accurate and cross platform timezone calculations using Python 2.3 or
higher. It also solves the issue of ambiguous times at the end of
daylight savings, which you can read more about in the Python Library
Reference (datetime.tzinfo).

Amost all (over 540) of the Olson timezones are supported.

%prep -a
# Remove bundled egg-info
rm -rf %{module}.egg-info

%install -a
%fdupes %{buildroot}%{python_sitelib}/%{module}/zoneinfo

%files
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}*.*-info
