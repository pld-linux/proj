#
# Conditional build:
%bcond_without	java	# Java/JNI support

%{?use_default_jdk:%use_default_jdk}
Summary:	Cartographic projection software
Summary(pl.UTF-8):	Oprogramowanie do rzutów kartograficznych
Name:		proj
Version:	9.8.1
Release:	1
Group:		Libraries
License:	MIT
Source0:	http://download.osgeo.org/proj/%{name}-%{version}.tar.gz
# Source0-md5:	337d10673c73377fb83d7c7ddbe8a5c4
Source1:	http://download.osgeo.org/proj/%{name}-pdf-docs.tar.gz
# Source1-md5:	7c8f48f0fddf0d5730f4b27b3f09e6c1
Source2:	https://raw.githubusercontent.com/OSGeo/proj-datumgrid/master/scripts/nad2bin.c
# Source2-md5:	d061e9107864c06c997cda0910de81bc
URL:		https://proj.org/
BuildRequires:	cmake >= 3.16
BuildRequires:	curl-devel
BuildRequires:	gcc  >= 5:3.2
BuildRequires:	libstdc++-devel >= 6:7
BuildRequires:	libtiff-devel
BuildRequires:	nlohmann-json-devel >= 3.7.0
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 2.022
BuildRequires:	sqlite3-devel >= 3.11
%if %{with java}
%{?buildrequires_jdk}
%endif
Requires:	sqlite3 >= 3.11
Obsoletes:	proj-static < 9
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
Requires:	libstdc++-devel >= 6:7
Requires:	libtiff-devel
Requires:	sqlite3-devel >= 3.11

%description devel
This package contains proj header files.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe niezbędne do tworzenia aplikacji
korzystających z biblioteki proj.

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
cp %{SOURCE2} .

%build
%cmake -B build \
	-DNLOHMANN_JSON_ORIGIN=external

%{__make} -C build

# build nad2bin, removed from proj but required by e.g. grass.spec
%{__cc} %{rpmcflags} %{rpmldflags} -o build/nad2bin nad2bin.c

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

install build/nad2bin $RPM_BUILD_ROOT%{_bindir}

# packaged as %doc
%{__rm} $RPM_BUILD_ROOT%{_docdir}/{AUTHORS.md,COPYING,NEWS.md}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS.md CITATION COPYING ChangeLog NEWS.md README.md
%{_libdir}/libproj.so.*.*.*
%ghost %{_libdir}/libproj.so.25
%{_datadir}/proj

%files devel
%defattr(644,root,root,755)
%{_libdir}/libproj.so
%{_includedir}/proj
%{_includedir}/geodesic.h
%{_includedir}/proj.h
%{_includedir}/proj_constants.h
%{_includedir}/proj_experimental.h
%{_includedir}/proj_symbol_rename.h
%{_includedir}/projapps_lib.h
%{_pkgconfigdir}/proj.pc
%{_libdir}/cmake/proj
%{_libdir}/cmake/proj4

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
%{bash_compdir}/projinfo

%files doc
%defattr(644,root,root,755)
%doc *.pdf
