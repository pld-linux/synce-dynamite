
%define	_realname	dynamite

Summary:	SynCE Dynamite - a tool to use data compressed with PKWARE DCL
Summary(pl):	SynCE Dynamite - narz�dzie do dekompresji danych spakowanych PKWARE DCL
Name:		synce-%{_realname}
Version:	0.1
Release:	1
License:	MIT
Group:		Applications
Source0:	http://dl.sourceforge.net/synce/%{_realname}-%{version}.tar.gz
# Source0-md5:	5e99d9172f60b8084cc6f6ba1a8c8261
URL:		http://synce.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1.4
BuildRequires:	libtool
BuildRequires:	rpmbuild(macros) >= 1.213
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dynamite is a tool for decompressing data compressed with PKWARE Data
Compression Library and it was created from the specification provided
by a post in the comp.compression newsgroup.

%description -l pl
Dynamite jest narz�dziem s�u��cym do dekompresji danych spakowanych za
pomoc� PKWARE Data Compression Library. Zosta�o stworzone zgodnie ze
specyfikacj� zamieszczon� wiadomo�ci wys�anej na grup� dyskusyjn�
comp.compression.

%package libs
Summary:	The Dynamite library
Summary(pl):	Biblioteka Dynamite
Group:		Libraries

%description libs
The dynamite library. It is needed to squeeze out juicy .cab files
from self-extracting installation programs created by the Setup
Factory installation program.

%description libs -l pl
Biblioteka Dynamite. Jest ona potrzebna do wydobycia plik�w .cab z
program�w instalacyjnych utworzonych za pomoc� programu Setup Factory.

%package libs-devel
Summary:	Header files for the Dynamite library
Summary(pl):	Pliki nag��wkowe biblioteki Dynamite
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description libs-devel
Header files for the Dynamite library.

%description libs-devel -l pl
Pliki nag��wkowe biblioteki Dynamite.

%package libs-static
Summary:	Static Dynamite library
Summary(pl):	Statyczna biblioteka Dynamite
Group:		Development/Libraries
Requires:	%{name}-libs-devel = %{version}-%{release}

%description libs-static
Static Dynamite library.

%description libs-static -l pl
Statyczna biblioteka Dynamite.

%prep
%setup -q -n %{_realname}-%{version}

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
%attr(755,root,root) %{_bindir}/*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdynamite.so.*.*.*

%files libs-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdynamite.so
%{_libdir}/libdynamite.la
%{_includedir}/libdynamite.h
%{_aclocaldir}/dynamite.m4

%files libs-static
%defattr(644,root,root,755)
%{_libdir}/libdynamite.a
