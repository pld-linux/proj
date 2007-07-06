Summary:	Cartographic projection software
Summary(pl.UTF-8):	Oprogramowanie do rzutów kartograficznych
Name:		proj
Version:	4.5.0
Release:	1
Group:		Libraries
License:	MIT
# use ftp.gdal.org (same IP) because of NS problems with remotesensing.org
Source0:	ftp://ftp.remotesensing.org/proj/%{name}-%{version}.tar.gz
# Source0-md5:	336fc8a12abbc4709e0bc1fb88a77436
Source1:	ftp://ftp.remotesensing.org/proj/%{name}-pdf-docs.tar.gz
# Source1-md5:	7c8f48f0fddf0d5730f4b27b3f09e6c1
URL:		http://www.remotesensing.org/proj/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cartographic projection software.

%description -l pl.UTF-8
Oprogramowanie do rzutów kartograficznych.

%package devel
Summary:	proj header files
Summary(pl.UTF-8):	Pliki nagłówkowe proj
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains proj header files.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe niezbędne do tworzenia aplikacji
korzystających z biblioteki proj.

%package static
Summary:	proj static libraries
Summary(pl.UTF-8):	Biblioteki statyczne libPropList
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains static proj libraries.

%description static -l pl.UTF-8
Ten pakiet zawiera statyczne biblioteki proj.

%package progs
Summary:	Cartographic projection software
Summary(pl.UTF-8):	Oprogramowanie do rzutów kartograficznych
Group:		Applications
Requires:	%{name} = %{version}-%{release}

%description progs
Package contains cartographic projection and coordinate system
filters.

%description progs -l pl.UTF-8
Ten pakiet zawiera filtry do rzutów kartograficznych i układów
współrzędnych.

%package doc
Summary:	Manuals for cartographic projection software
Summary(pl.UTF-8):	Dokumentacja do proj
Group:		Documentation
Requires:	%{name} = %{version}-%{release}

%description doc
Manuals for cartographic projection software.

%description doc -l pl.UTF-8
Dokumentacja do oprogramowania do rzutów kartograficznych proj.

%prep
%setup -q -a1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

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
%{_datadir}/proj/esri.extra
%{_datadir}/proj/other.extra

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
