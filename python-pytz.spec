%define module	pytz

Summary:	World timezone definitions for Python

Name:		python-%{module}
Version:	2017.3
Release:	1
License:	MIT
Group:		Development/Python
Url:		http://pytz.sourceforge.net/
Source0:	https://pypi.python.org/packages/60/88/d3152c234da4b2a1f7a989f89609ea488225eaea015bc16fbde2b3fdfefa/pytz-%{version}.zip
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
PYTHONDONTWRITEBYTECODE= %__python2 setup.py install --root=%{buildroot} --record=FILELIST.P2
sed -i 's/.*egg-info.*$//' FILELIST.P2
popd

pushd python3
PYTHONDONTWRITEBYTECODE= %__python3 setup.py install --root=%{buildroot} --record=FILELIST.P3
sed -i 's/.*egg-info.*$//' FILELIST.P3
sed -i 's/.*pyc$//' FILELIST.P3
find %{buildroot}%{py3_puresitedir} -name "*pyc" -delete
popd

%files -f python3/FILELIST.P3
%doc python3/*.txt
%{py3_puresitedir}/%{module}-%{version}-*.egg-info

%files -n python2-%{module} -f python2/FILELIST.P2
%doc python2/*.txt
%{py2_puresitedir}/%{module}-%{version}-*.egg-info


