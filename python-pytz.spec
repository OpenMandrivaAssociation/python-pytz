%define module	pytz

Summary:	World timezone definitions for Python

Name:		python-%{module}
Version:	2019.3
Release:	1
License:	MIT
Group:		Development/Python
Url:		http://pytz.sourceforge.net/
Source0:	https://files.pythonhosted.org/packages/82/c3/534ddba230bd4fbbd3b7a3d35f3341d014cca213f369a9940925e7e5f691/pytz-2019.3.tar.gz
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(python3)
BuildRequires:	python-setuptools
BuildRequires:	python2-setuptools
%rename python3-pytz

%description
pytz brings the Olson tz database into Python. This library allows
accurate and cross platform timezone calculations using Python 2.3 or
higher. It also solves the issue of ambiguous times at the end of
daylight savings, which you can read more about in the Python Library
Reference (datetime.tzinfo).

Amost all (over 540) of the Olson timezones are supported.

%package -n python2-%{module}
Summary:	World timezone definitions for Python2

Group:		Development/Python
Requires:	python2

%description -n python2-%{module}
pytz brings the Olson tz database into Python. This library allows
accurate and cross platform timezone calculations using Python 2.3 or
higher. It also solves the issue of ambiguous times at the end of
daylight savings, which you can read more about in the Python Library
Reference (datetime.tzinfo).

Amost all (over 540) of the Olson timezones are supported.

%prep
%setup -q -c

mv %{module}-%{version} python2
cp -r python2 python3

%install
pushd python2
PYTHONDONTWRITEBYTECODE= %__python2 setup.py install --root=%{buildroot}
popd

pushd python3
PYTHONDONTWRITEBYTECODE= %__python3 setup.py install --root=%{buildroot}
popd

%files
%doc python3/*.txt
%{py3_puresitedir}/%{module}-%{version}-*.egg-info
%{py3_puresitedir}/pytz

%files -n python2-%{module}
%doc python2/*.txt
%{py2_puresitedir}/pytz
%{py2_puresitedir}/%{module}-%{version}-*.egg-info
