%define module	pytz

Summary:	World timezone definitions for Python
Name:		python-%{module}
Version:	2011h
Release:	3
Source0:	%{module}-%{version}.tar.bz2
License:	MIT
Group:		Development/Python
Url:		http://pytz.sourceforge.net/
%py_requires -d
BuildArch:	noarch

%description
pytz brings the Olson tz database into Python. This library allows
accurate and cross platform timezone calculations using Python 2.3 or
higher. It also solves the issue of ambiguous times at the end of
daylight savings, which you can read more about in the Python Library
Reference (datetime.tzinfo).

Amost all (over 540) of the Olson timezones are supported.

%prep
%setup -q -n %{module}-%{version}

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}

%files
%{py_sitedir}/*
%doc *.txt

%changelog
* Fri Feb  8 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2011h-2
- Rebuild due to python modules breakage.

* Mon Jun 27 2011 Lev Givon <lev@mandriva.org> 2011h-1mdv2011.0
+ Revision: 687488
- Update to 2011h.

* Sun May 08 2011 Lev Givon <lev@mandriva.org> 2011g-1
+ Revision: 672505
- Update to 2011g.

* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 2011e-2
+ Revision: 668029
- mass rebuild

* Fri Apr 01 2011 Lev Givon <lev@mandriva.org> 2011e-1
+ Revision: 649666
- Update to 2011e.

* Wed Mar 09 2011 Lev Givon <lev@mandriva.org> 2011c-1
+ Revision: 643098
- Update to 2011c.

* Tue Feb 08 2011 Lev Givon <lev@mandriva.org> 2011b-1
+ Revision: 636877
- Update to 2011b.

* Thu Nov 18 2010 Lev Givon <lev@mandriva.org> 2010o-1mdv2011.0
+ Revision: 598752
- Update to 2010o.

* Thu Nov 04 2010 Paulo Andrade <pcpa@mandriva.com.br> 2010k-2mdv2011.0
+ Revision: 593468
+ rebuild (emptylog)

* Wed Jul 28 2010 Lev Givon <lev@mandriva.org> 2010k-1mdv2011.0
+ Revision: 562607
- Update to 2010k.

* Wed Mar 10 2010 Lev Givon <lev@mandriva.org> 2010e-1mdv2010.1
+ Revision: 517257
- Update to 2010e.

* Mon Jan 04 2010 Lev Givon <lev@mandriva.org> 2009u-1mdv2010.1
+ Revision: 486223
- Update to 2009u.

* Tue Sep 29 2009 Lev Givon <lev@mandriva.org> 2009n-1mdv2010.0
+ Revision: 450927
- Update to 2009n.

* Mon Aug 10 2009 Lev Givon <lev@mandriva.org> 2009j-1mdv2010.0
+ Revision: 414453
- Update to 2009j.

* Sun Jan 04 2009 Funda Wang <fwang@mandriva.org> 2008i-2mdv2009.1
+ Revision: 324092
- rebuild

* Fri Nov 07 2008 Lev Givon <lev@mandriva.org> 2008i-1mdv2009.1
+ Revision: 300408
- Update to 2008i.

* Mon Oct 13 2008 Lev Givon <lev@mandriva.org> 2008h-1mdv2009.1
+ Revision: 293371
- Update to 2008h.

* Fri Jul 11 2008 Lev Givon <lev@mandriva.org> 2008c-1mdv2009.0
+ Revision: 233820
- import python-pytz


* Fri Jul 11 2008 Lev Givon <lev@mandriva.org> 2008c-1mdv2008.1
- Package for Mandriva.

