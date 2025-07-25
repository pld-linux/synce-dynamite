%define		realname	libdynamite
Summary:	SynCE Dynamite - a tool to use data compressed with PKWARE DCL
Summary(pl.UTF-8):	SynCE Dynamite - narzędzie do dekompresji danych spakowanych PKWARE DCL
Name:		synce-dynamite
Version:	0.1.1
Release:	3
License:	MIT
Group:		Applications/File
Source0:	http://downloads.sourceforge.net/synce/%{realname}-%{version}.tar.gz
# Source0-md5:	238bf243dba2166a2e0e141b18065235
Patch0:		%{name}-ac.patch
URL:		http://www.synce.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1.4
BuildRequires:	libtool
BuildRequires:	rpmbuild(macros) >= 1.213
Requires:	%{name}-libs = %{version}-%{release}
Obsoletes:	dynamite
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dynamite is a tool for decompressing data compressed with PKWARE Data
Compression Library and it was created from the specification provided
by a post in the comp.compression newsgroup.

%description -l pl.UTF-8
Dynamite jest narzędziem służącym do dekompresji danych spakowanych za
pomocą PKWARE Data Compression Library. Zostało stworzone zgodnie ze
specyfikacją zamieszczoną w wiadomości wysłanej na grupę dyskusyjną
comp.compression.

%package libs
Summary:	The Dynamite library
Summary(pl.UTF-8):	Biblioteka Dynamite
Group:		Libraries
Obsoletes:	dynamite-libs

%description libs
The dynamite library. It is needed to squeeze out juicy .cab files
from self-extracting installation programs created by the Setup
Factory installation program.

%description libs -l pl.UTF-8
Biblioteka Dynamite, służąca do wydobywania plików .cab z programów
instalacyjnych utworzonych za pomocą programu Setup Factory.

%package libs-devel
Summary:	Header files for the Dynamite library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Dynamite
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Obsoletes:	dynamite-devel

%description libs-devel
Header files for the Dynamite library.

%description libs-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Dynamite.

%package libs-static
Summary:	Static Dynamite library
Summary(pl.UTF-8):	Statyczna biblioteka Dynamite
Group:		Development/Libraries
Requires:	%{name}-libs-devel = %{version}-%{release}
Obsoletes:	dynamite-static

%description libs-static
Static Dynamite library.

%description libs-static -l pl.UTF-8
Statyczna biblioteka Dynamite.

%prep
%setup -q -n %{realname}-%{version}
%patch -P0 -p1

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

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE
%attr(755,root,root) %{_bindir}/dynamite
%{_mandir}/man1/dynamite.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdynamite.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdynamite.so.0

%files libs-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdynamite.so
%{_libdir}/libdynamite.la
%{_includedir}/libdynamite.h
%{_pkgconfigdir}/libdynamite.pc

%files libs-static
%defattr(644,root,root,755)
%{_libdir}/libdynamite.a
