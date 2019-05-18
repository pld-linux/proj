#
# Conditional build:
%bcond_without	java	# Java/JNI support

Summary:	Cartographic projection software
Summary(pl.UTF-8):	Oprogramowanie do rzutów kartograficznych
Name:		proj
Version:	6.1.0
Release:	1
Group:		Libraries
License:	MIT
Source0:	http://download.osgeo.org/proj/%{name}-%{version}.tar.gz
# Source0-md5:	4ec5d9240b0e290670886519f250946c
Source1:	http://download.osgeo.org/proj/%{name}-pdf-docs.tar.gz
# Source1-md5:	7c8f48f0fddf0d5730f4b27b3f09e6c1
Source2:	https://raw.githubusercontent.com/OSGeo/proj-datumgrid/master/scripts/nad2bin.c
# Source2-md5:	d061e9107864c06c997cda0910de81bc
Patch0:		%{name}-am.patch
URL:		http://proj4.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
%{?with_java:BuildRequires:	jdk}
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cartographic projection software.

%description -l pl.UTF-8
Oprogramowanie do rzutów kartograficznych.

%package devel
Summary:	proj header files
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki proj
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
Summary(pl.UTF-8):	Dokumentacja do oprogramowania proj
Group:		Documentation
Requires:	%{name} = %{version}-%{release}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description doc
Manuals for cartographic projection software.

%description doc -l pl.UTF-8
Dokumentacja do oprogramowania do rzutów kartograficznych proj.

%prep
%setup -q -a1
%patch0 -p1
cp %{SOURCE2} .

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_java:--without-jni}

%{__make}

# build nad2bin, removed from proj but required by e.g. grass.spec
%{__cc} %{rpmcflags} %{rpmldflags} -o nad2bin nad2bin.c

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install nad2bin $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog CITATION NEWS README
%attr(755,root,root) %{_libdir}/libproj.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libproj.so.15
%dir %{_datadir}/proj
%{_datadir}/proj/CH
%{_datadir}/proj/GL27
%{_datadir}/proj/ITRF2000
%{_datadir}/proj/ITRF2008
%{_datadir}/proj/ITRF2014
%{_datadir}/proj/nad27
%{_datadir}/proj/nad83
%{_datadir}/proj/nad.lst
%{_datadir}/proj/null
%{_datadir}/proj/world
%{_datadir}/proj/other.extra
%{_datadir}/proj/proj.db

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libproj.so
%{_libdir}/libproj.la
%{_includedir}/proj
%{_includedir}/geodesic.h
%{_includedir}/org_proj4_PJ.h
%{_includedir}/proj.h
%{_includedir}/proj_api.h
%{_includedir}/proj_constants.h
%{_includedir}/proj_experimental.h
%{_includedir}/proj_symbol_rename.h
%{_pkgconfigdir}/proj.pc
%{_mandir}/man3/geodesic.3*
%{_mandir}/man3/pj_init.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libproj.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cct
%attr(755,root,root) %{_bindir}/cs2cs
%attr(755,root,root) %{_bindir}/geod
%attr(755,root,root) %{_bindir}/gie
%attr(755,root,root) %{_bindir}/invgeod
%attr(755,root,root) %{_bindir}/invproj
%attr(755,root,root) %{_bindir}/nad2bin
%attr(755,root,root) %{_bindir}/proj
%attr(755,root,root) %{_bindir}/projinfo
%{_mandir}/man1/cct.1*
%{_mandir}/man1/cs2cs.1*
%{_mandir}/man1/geod.1*
%{_mandir}/man1/gie.1*
%{_mandir}/man1/proj.1*
%{_mandir}/man1/projinfo.1*

%files doc
%defattr(644,root,root,755)
%doc *.pdf
