Name:           cgicc
Version:        3.2.16
Release:        1%{?dist}
Summary:        ANSI C++ library for CGI applications

License:        LGPL
URL:            https://www.gnu.org/software/cgicc/index.html
Source0:        https://ftp.gnu.org/gnu/cgicc/cgicc-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gcc-c++
BuildRequires:  doxygen

%description
GNU Cgicc is an ANSI C++ compliant class library that greatly simplifies the
creation of CGI applications for the World Wide Web. cgicc performs the
following functions:

- Parses both GET and POST form data transparently.
- Provides string, integer, floating-point and single- and multiple-choice retrieval methods for form data.
- Provides methods for saving and restoring CGI environments to aid in application debugging.
- Provides full on-the-fly HTML generation capabilities, with support for cookies.
- Supports HTTP file upload.
- Compatible with FastCGI.
- License: LGPL.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup


%build
%configure --disable-static CPPFLAGS="-std=c++11"
%make_build


%install
rm -rf $RPM_BUILD_ROOT
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
mkdir -p $RPM_BUILD_ROOT/usr/share/doc/%{name}
mv $RPM_BUILD_ROOT/usr/doc/%{name}-%{version} $RPM_BUILD_ROOT/usr/share/doc/%{name}/html


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%license COPYING.DOC COPYING.LIB
%{_libdir}/*.so.*
%{_bindir}/cgicc-config

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_docdir}/*
%{_libdir}/pkgconfig/cgicc.pc
%{_datarootdir}/aclocal/cgicc.m4


%changelog
* Tue Oct 11 2016 Emanuele Di Giacomo <emanuele.digiacomo@gmail.com> - 3.2.16-1
- Relase 3.2.16
