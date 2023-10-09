%define module	pytz

Summary:	World timezone definitions for Python

Name:		python-%{module}
Version:	2023.3.post1
Release:	1
License:	MIT
Group:		Development/Python
Url:		http://pytz.sourceforge.net/
# https://pypi.org/project/pytz/
Source0:	https://files.pythonhosted.org/packages/source/p/pytz/pytz-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python-setuptools
%rename python3-pytz

%description
pytz brings the Olson tz database into Python. This library allows
accurate and cross platform timezone calculations using Python 2.3 or
higher. It also solves the issue of ambiguous times at the end of
daylight savings, which you can read more about in the Python Library
Reference (datetime.tzinfo).

Amost all (over 540) of the Olson timezones are supported.

%prep
%autosetup -p1 -n %{module}-%{version}

%install
PYTHONDONTWRITEBYTECODE= python setup.py install --root=%{buildroot}

%files
%doc *.txt
%{py3_puresitedir}/%{module}-%{version}-*.egg-info
%{py3_puresitedir}/pytz
