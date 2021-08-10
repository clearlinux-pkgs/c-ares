#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x5CC908FDB71E12C2 (daniel@haxx.se)
#
Name     : c-ares
Version  : 1.17.2
Release  : 18
URL      : https://c-ares.haxx.se/download/c-ares-1.17.2.tar.gz
Source0  : https://c-ares.haxx.se/download/c-ares-1.17.2.tar.gz
Source1  : https://c-ares.haxx.se/download/c-ares-1.17.2.tar.gz.asc
Summary  : asynchronous DNS lookup library
Group    : Development/Tools
License  : GPL-2.0+ MIT X11
Requires: c-ares-lib = %{version}-%{release}
Requires: c-ares-license = %{version}-%{release}
BuildRequires : buildreq-cmake

%description
___       __ _ _ __ ___  ___
/ __| ___ / _` | '__/ _ \/ __|
| (_  |___| (_| | | |  __/\__ \
\___|     \__,_|_|  \___||___/

%package dev
Summary: dev components for the c-ares package.
Group: Development
Requires: c-ares-lib = %{version}-%{release}
Provides: c-ares-devel = %{version}-%{release}
Requires: c-ares = %{version}-%{release}

%description dev
dev components for the c-ares package.


%package lib
Summary: lib components for the c-ares package.
Group: Libraries
Requires: c-ares-license = %{version}-%{release}

%description lib
lib components for the c-ares package.


%package license
Summary: license components for the c-ares package.
Group: Default

%description license
license components for the c-ares package.


%prep
%setup -q -n c-ares-1.17.2
cd %{_builddir}/c-ares-1.17.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1628605661
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%configure --disable-static
make  %{?_smp_mflags}  DEFAULTFLAGS="$CFLAGS"

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1628605661
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/c-ares
cp %{_builddir}/c-ares-1.17.2/LICENSE.md %{buildroot}/usr/share/package-licenses/c-ares/e9c597f9b6cf935773ee731d4170b0c2ba142dbb
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/ares.h
/usr/include/ares_build.h
/usr/include/ares_dns.h
/usr/include/ares_rules.h
/usr/include/ares_version.h
/usr/lib64/libcares.so
/usr/lib64/pkgconfig/libcares.pc
/usr/share/man/man3/ares_cancel.3
/usr/share/man/man3/ares_create_query.3
/usr/share/man/man3/ares_destroy.3
/usr/share/man/man3/ares_destroy_options.3
/usr/share/man/man3/ares_dup.3
/usr/share/man/man3/ares_expand_name.3
/usr/share/man/man3/ares_expand_string.3
/usr/share/man/man3/ares_fds.3
/usr/share/man/man3/ares_free_data.3
/usr/share/man/man3/ares_free_hostent.3
/usr/share/man/man3/ares_free_string.3
/usr/share/man/man3/ares_freeaddrinfo.3
/usr/share/man/man3/ares_get_servers.3
/usr/share/man/man3/ares_get_servers_ports.3
/usr/share/man/man3/ares_getaddrinfo.3
/usr/share/man/man3/ares_gethostbyaddr.3
/usr/share/man/man3/ares_gethostbyname.3
/usr/share/man/man3/ares_gethostbyname_file.3
/usr/share/man/man3/ares_getnameinfo.3
/usr/share/man/man3/ares_getsock.3
/usr/share/man/man3/ares_inet_ntop.3
/usr/share/man/man3/ares_inet_pton.3
/usr/share/man/man3/ares_init.3
/usr/share/man/man3/ares_init_options.3
/usr/share/man/man3/ares_library_cleanup.3
/usr/share/man/man3/ares_library_init.3
/usr/share/man/man3/ares_library_init_android.3
/usr/share/man/man3/ares_library_initialized.3
/usr/share/man/man3/ares_mkquery.3
/usr/share/man/man3/ares_parse_a_reply.3
/usr/share/man/man3/ares_parse_aaaa_reply.3
/usr/share/man/man3/ares_parse_caa_reply.3
/usr/share/man/man3/ares_parse_mx_reply.3
/usr/share/man/man3/ares_parse_naptr_reply.3
/usr/share/man/man3/ares_parse_ns_reply.3
/usr/share/man/man3/ares_parse_ptr_reply.3
/usr/share/man/man3/ares_parse_soa_reply.3
/usr/share/man/man3/ares_parse_srv_reply.3
/usr/share/man/man3/ares_parse_txt_reply.3
/usr/share/man/man3/ares_process.3
/usr/share/man/man3/ares_query.3
/usr/share/man/man3/ares_save_options.3
/usr/share/man/man3/ares_search.3
/usr/share/man/man3/ares_send.3
/usr/share/man/man3/ares_set_local_dev.3
/usr/share/man/man3/ares_set_local_ip4.3
/usr/share/man/man3/ares_set_local_ip6.3
/usr/share/man/man3/ares_set_servers.3
/usr/share/man/man3/ares_set_servers_csv.3
/usr/share/man/man3/ares_set_servers_ports.3
/usr/share/man/man3/ares_set_servers_ports_csv.3
/usr/share/man/man3/ares_set_socket_callback.3
/usr/share/man/man3/ares_set_socket_configure_callback.3
/usr/share/man/man3/ares_set_socket_functions.3
/usr/share/man/man3/ares_set_sortlist.3
/usr/share/man/man3/ares_strerror.3
/usr/share/man/man3/ares_timeout.3
/usr/share/man/man3/ares_version.3

%files lib
%defattr(-,root,root,-)
/usr/lib64/libcares.so.2
/usr/lib64/libcares.so.2.4.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/c-ares/e9c597f9b6cf935773ee731d4170b0c2ba142dbb
