Summary:	Cartographic projection software
Summary(pl):	Oprogramowanie do rzut�w kartograficznych
Name:		proj
Version:	4.4.9
Release:	1
Group:		Libraries
License:	MIT
Source0:	ftp://ftp.remotesensing.org/pub/proj/%{name}-%{version}.tar.gz
# Source0-md5:	3cc5c2407c213aadfd154c8df80efd6c
Source1:	ftp://ftp.remotesensing.org/pub/proj/OF90-284.pdf
# Source1-md5:	00ed1f2109a7a81f1b15e1c19235eed5
Source2:	ftp://ftp.remotesensing.org/pub/proj/PROJ.4.3.pdf
# Source2-md5:	94e5c9afe50963ce4360149e7ffb7da6
Source3:	ftp://ftp.remotesensing.org/pub/proj/SWISS.pdf
# Source3-md5:	ca67b903d54dc8f6eb626020cb3e3faa
Source4:	ftp://ftp.remotesensing.org/pub/proj/PROJ.4.3.I2.pdf
# Source4-md5:	2fb167935a0c7d686e89af419d07c66c
URL:		http://www.remotesensing.org/proj/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cartographic projection software.

%description -l pl
Oprogramowanie do rzut�w kartograficznych.

%package devel
Summary:	proj header files
Summary(pl):	Pliki nag��wkowe proj
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains proj header files.

%description devel -l pl
Ten pakiet zawiera pliki nag��wkowe niezb�dne do tworzenia aplikacji
korzystaj�cych z biblioteki proj.

%package static
Summary:	proj static libraries
Summary(pl):	Biblioteki statyczne libPropList
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains static proj libraries.

%description static -l pl
Ten pakiet zawiera statyczne biblioteki proj.

%package progs
Summary:	Cartographic projection software
Summary(pl):	Oprogramowanie do rzut�w kartograficznych
Group:		Applications
Requires:	%{name} = %{version}-%{release}

%description progs
Package contains cartographic projection and coordinate system
filters.

%description progs -l pl
Ten pakiet zawiera filtry do rzut�w kartograficznych i uk�ad�w
wsp�rz�dnych.

%package doc
Summary:	Manuals for cartographic projection software
Summary(pl):	Dokumentacja do proj
Group:		Documentation
Requires:	%{name} = %{version}-%{release}

%description doc
Manuals for cartographic projection software.

%description doc -l pl
Dokumentacja do oprogramowania do rzut�w kartograficznych proj.

%prep
%setup -q
cp -f %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} .

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libproj.so.*.*
%dir %{_datadir}/proj
%{_datadir}/proj/GL27
%{_datadir}/proj/nad27
%{_datadir}/proj/nad83
%{_datadir}/proj/nad.lst
%{_datadir}/proj/proj_def.dat
%{_datadir}/proj/world
%{_datadir}/proj/epsg
%{_datadir}/proj/esri

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libproj.so
%{_libdir}/libproj.la
%{_includedir}/*
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/libproj.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

%files doc
%defattr(644,root,root,755)
%doc *.pdf
