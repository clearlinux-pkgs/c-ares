#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : c-ares
Version  : 1.11.0
Release  : 2
URL      : http://c-ares.haxx.se/download/c-ares-1.11.0.tar.gz
Source0  : http://c-ares.haxx.se/download/c-ares-1.11.0.tar.gz
Summary  : asynchronous DNS lookup library
Group    : Development/Tools
License  : GPL-2.0+ MIT X11
Requires: c-ares-lib
Requires: c-ares-doc

%description
___       __ _ _ __ ___  ___
/ __| ___ / _` | '__/ _ \/ __|
| (_  |___| (_| | | |  __/\__ \
\___|     \__,_|_|  \___||___/

%package dev
Summary: dev components for the c-ares package.
Group: Development
Requires: c-ares-lib
Provides: c-ares-devel

%description dev
dev components for the c-ares package.


%package doc
Summary: doc components for the c-ares package.
Group: Documentation

%description doc
doc components for the c-ares package.


%package lib
Summary: lib components for the c-ares package.
Group: Libraries

%description lib
lib components for the c-ares package.


%prep
%setup -q -n c-ares-1.11.0

%build
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
