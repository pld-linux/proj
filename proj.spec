Summary:	Cartographic projection software
Name:		proj
Version:	4.4.5
Release:	1
Copyright:	MIT
URL:		http://www.remotesensing.org/proj
Source0:	ftp://ftp.remotesensing.org/pub/proj/%{name}-%{version}.tar.gz
Source1:	ftp://ftp.remotesensing.org/pub/proj/OF90-284.pdf
Source2:	ftp://ftp.remotesensing.org/pub/proj/PROJ.4.3.pdf
Source3:	ftp://ftp.remotesensing.org/pub/proj/SWISS.pdf
Source4:	ftp://ftp.remotesensing.org/pub/proj/PROJ.4.3.I2.pdf
Group:		Libraries
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cartographic projection software

%package devel
Summary:	Cartographic projection software
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
proj headers files

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe i biblioteki niezbêdne do
tworzenia aplikacji korzystaj±cych z biblioteki proj.

%package static
Summary:	proj static libraries
Summary(pl):	Biblioteki statyczne libPropList
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
This package contains static libraries for building proj applications.

%description static -l pl
Ten pakiet zawiera statyczne biblioteki niezbêdne do tworzenia
aplikacji korzystaj±cych z biblioteki proj.

%package progs
Summary:	Cartographic projection software
Group:		Applications
Requires:	%{name} = %{version}

%description progs
Package contains cartographic projection and coordinate system filters

%package doc
Summary:	Manuals for cartographic projection software
Group:		Applications
Requires:	%{name} = %{version}

%description doc
Manuals for cartographic projection software
%prep
%setup -q
cp %{SOURCE1} ./
cp %{SOURCE2} ./
cp %{SOURCE3} ./
cp %{SOURCE4} ./

%build

%configure2_13

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%{_libdir}/libproj.so.*.*
%{_datadir}/proj/GL27
%{_datadir}/proj/nad27
%{_datadir}/proj/nad83
%{_datadir}/proj/proj_def.dat
%{_datadir}/proj/world
%{_datadir}/proj/epsg

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%{_libdir}/libproj.so
%{_libdir}/libproj.la
%{_includedir}/*
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/libproj.a

%files doc
%defattr(644,root,root,755)
%doc OF90-284.pdf
%doc PROJ.4.3.I2.pdf
%doc PROJ.4.3.pdf
%doc SWISS.pdf
