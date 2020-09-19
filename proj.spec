Summary:	Cartographic projection software
Summary(pl.UTF-8):	Oprogramowanie do rzutów kartograficznych
Name:		proj
Version:	7.1.1
Release:	1
Group:		Libraries
License:	MIT
Source0:	http://download.osgeo.org/proj/%{name}-%{version}.tar.gz
# Source0-md5:	b7ce84943dcf2b660b11c2ef9657dad5
Source1:	http://download.osgeo.org/proj/%{name}-pdf-docs.tar.gz
# Source1-md5:	7c8f48f0fddf0d5730f4b27b3f09e6c1
Source2:	https://raw.githubusercontent.com/OSGeo/proj-datumgrid/master/scripts/nad2bin.c
# Source2-md5:	d061e9107864c06c997cda0910de81bc
Patch0:		%{name}-am.patch
URL:		https://proj.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	curl-devel
BuildRequires:	gtest-devel >= 1.8.0
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	sqlite3-devel >= 3.11
Requires:	sqlite3 >= 3.11
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
Requires:	curl-devel
Requires:	libstdc++-devel >= 6:4.7
Requires:	libtiff-devel
Requires:	sqlite3-devel >= 3.11

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
BuildArch:	noarch

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
	--with-external-gtest

%{__make}

# build nad2bin, removed from proj but required by e.g. grass.spec
%{__cc} %{rpmcflags} %{rpmldflags} -o nad2bin nad2bin.c

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libproj.la

install nad2bin $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog CITATION NEWS README
%attr(755,root,root) %{_libdir}/libproj.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libproj.so.19
%dir %{_datadir}/proj
%{_datadir}/proj/CH
%{_datadir}/proj/GL27
%{_datadir}/proj/ITRF2000
%{_datadir}/proj/ITRF2008
%{_datadir}/proj/ITRF2014
%{_datadir}/proj/nad27
%{_datadir}/proj/nad83
%{_datadir}/proj/nad.lst
%{_datadir}/proj/world
%{_datadir}/proj/other.extra
%{_datadir}/proj/proj.db
%{_datadir}/proj/proj.ini
%{_datadir}/proj/deformation_model.schema.json
%{_datadir}/proj/projjson.schema.json

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libproj.so
%{_includedir}/proj
%{_includedir}/geodesic.h
%{_includedir}/proj.h
%{_includedir}/proj_api.h
%{_includedir}/proj_constants.h
%{_includedir}/proj_experimental.h
%{_includedir}/proj_symbol_rename.h
%{_pkgconfigdir}/proj.pc

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
%attr(755,root,root) %{_bindir}/projsync
%{_mandir}/man1/cct.1*
%{_mandir}/man1/cs2cs.1*
%{_mandir}/man1/geod.1*
%{_mandir}/man1/gie.1*
%{_mandir}/man1/proj.1*
%{_mandir}/man1/projinfo.1*
%{_mandir}/man1/projsync.1*

%files doc
%defattr(644,root,root,755)
%doc *.pdf
