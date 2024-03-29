#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v5
# autospec commit: c02b2fe
#
# Source0 file verified with key 0x5CC908FDB71E12C2 (daniel@haxx.se)
#
Name     : c-ares
Version  : 1.28.0
Release  : 33
URL      : https://c-ares.haxx.se/download/c-ares-1.28.0.tar.gz
Source0  : https://c-ares.haxx.se/download/c-ares-1.28.0.tar.gz
Source1  : https://c-ares.haxx.se/download/c-ares-1.28.0.tar.gz.asc
Summary  : asynchronous DNS lookup library
Group    : Development/Tools
License  : GPL-2.0+ MIT X11
Requires: c-ares-lib = %{version}-%{release}
Requires: c-ares-license = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : file
BuildRequires : pkgconfig(gmock)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
%setup -q -n c-ares-1.28.0
cd %{_builddir}/c-ares-1.28.0
pushd ..
cp -a c-ares-1.28.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1711721594
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%configure --disable-static
make  %{?_smp_mflags}  DEFAULTFLAGS="$CFLAGS"

unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --disable-static
make  %{?_smp_mflags}  DEFAULTFLAGS="$CFLAGS"
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :
cd ../buildavx2;
make %{?_smp_mflags} check || : || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1711721594
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/c-ares
cp %{_builddir}/c-ares-%{version}/LICENSE.md %{buildroot}/usr/share/package-licenses/c-ares/12127d9b9e698989a5b23087aa7c39f5e6eb264e || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/ares.h
/usr/include/ares_build.h
/usr/include/ares_dns.h
/usr/include/ares_dns_record.h
/usr/include/ares_nameser.h
/usr/include/ares_rules.h
/usr/include/ares_version.h
/usr/lib64/libcares.so
/usr/lib64/pkgconfig/libcares.pc
/usr/share/man/man3/ares_cancel.3
/usr/share/man/man3/ares_create_query.3
/usr/share/man/man3/ares_destroy.3
/usr/share/man/man3/ares_destroy_options.3
/usr/share/man/man3/ares_dns_class_fromstr.3
/usr/share/man/man3/ares_dns_class_t.3
/usr/share/man/man3/ares_dns_class_tostr.3
/usr/share/man/man3/ares_dns_datatype_t.3
/usr/share/man/man3/ares_dns_flags_t.3
/usr/share/man/man3/ares_dns_mapping.3
/usr/share/man/man3/ares_dns_opcode_t.3
/usr/share/man/man3/ares_dns_opcode_tostr.3
/usr/share/man/man3/ares_dns_opt_datatype_t.3
/usr/share/man/man3/ares_dns_opt_get_datatype.3
/usr/share/man/man3/ares_dns_opt_get_name.3
/usr/share/man/man3/ares_dns_parse.3
/usr/share/man/man3/ares_dns_rcode_t.3
/usr/share/man/man3/ares_dns_rcode_tostr.3
/usr/share/man/man3/ares_dns_rec_type_fromstr.3
/usr/share/man/man3/ares_dns_rec_type_t.3
/usr/share/man/man3/ares_dns_record.3
/usr/share/man/man3/ares_dns_record_create.3
/usr/share/man/man3/ares_dns_record_destroy.3
/usr/share/man/man3/ares_dns_record_duplicate.3
/usr/share/man/man3/ares_dns_record_get_flags.3
/usr/share/man/man3/ares_dns_record_get_id.3
/usr/share/man/man3/ares_dns_record_get_opcode.3
/usr/share/man/man3/ares_dns_record_get_rcode.3
/usr/share/man/man3/ares_dns_record_query_add.3
/usr/share/man/man3/ares_dns_record_query_cnt.3
/usr/share/man/man3/ares_dns_record_query_get.3
/usr/share/man/man3/ares_dns_record_query_set_name.3
/usr/share/man/man3/ares_dns_record_query_set_type.3
/usr/share/man/man3/ares_dns_record_rr_add.3
/usr/share/man/man3/ares_dns_record_rr_cnt.3
/usr/share/man/man3/ares_dns_record_rr_del.3
/usr/share/man/man3/ares_dns_record_rr_get.3
/usr/share/man/man3/ares_dns_record_rr_get_const.3
/usr/share/man/man3/ares_dns_rr.3
/usr/share/man/man3/ares_dns_rr_get_addr.3
/usr/share/man/man3/ares_dns_rr_get_addr6.3
/usr/share/man/man3/ares_dns_rr_get_bin.3
/usr/share/man/man3/ares_dns_rr_get_class.3
/usr/share/man/man3/ares_dns_rr_get_keys.3
/usr/share/man/man3/ares_dns_rr_get_name.3
/usr/share/man/man3/ares_dns_rr_get_opt.3
/usr/share/man/man3/ares_dns_rr_get_opt_byid.3
/usr/share/man/man3/ares_dns_rr_get_opt_cnt.3
/usr/share/man/man3/ares_dns_rr_get_str.3
/usr/share/man/man3/ares_dns_rr_get_ttl.3
/usr/share/man/man3/ares_dns_rr_get_type.3
/usr/share/man/man3/ares_dns_rr_get_u16.3
/usr/share/man/man3/ares_dns_rr_get_u32.3
/usr/share/man/man3/ares_dns_rr_get_u8.3
/usr/share/man/man3/ares_dns_rr_key_datatype.3
/usr/share/man/man3/ares_dns_rr_key_t.3
/usr/share/man/man3/ares_dns_rr_key_to_rec_type.3
/usr/share/man/man3/ares_dns_rr_key_tostr.3
/usr/share/man/man3/ares_dns_rr_set_addr.3
/usr/share/man/man3/ares_dns_rr_set_addr6.3
/usr/share/man/man3/ares_dns_rr_set_bin.3
/usr/share/man/man3/ares_dns_rr_set_opt.3
/usr/share/man/man3/ares_dns_rr_set_str.3
/usr/share/man/man3/ares_dns_rr_set_u16.3
/usr/share/man/man3/ares_dns_rr_set_u32.3
/usr/share/man/man3/ares_dns_rr_set_u8.3
/usr/share/man/man3/ares_dns_section_t.3
/usr/share/man/man3/ares_dns_section_tostr.3
/usr/share/man/man3/ares_dns_write.3
/usr/share/man/man3/ares_dup.3
/usr/share/man/man3/ares_expand_name.3
/usr/share/man/man3/ares_expand_string.3
/usr/share/man/man3/ares_fds.3
/usr/share/man/man3/ares_free_data.3
/usr/share/man/man3/ares_free_hostent.3
/usr/share/man/man3/ares_free_string.3
/usr/share/man/man3/ares_freeaddrinfo.3
/usr/share/man/man3/ares_get_servers.3
/usr/share/man/man3/ares_get_servers_csv.3
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
/usr/share/man/man3/ares_opt_param_t.3
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
/usr/share/man/man3/ares_parse_uri_reply.3
/usr/share/man/man3/ares_process.3
/usr/share/man/man3/ares_query.3
/usr/share/man/man3/ares_query_dnsrec.3
/usr/share/man/man3/ares_queue.3
/usr/share/man/man3/ares_queue_active_queries.3
/usr/share/man/man3/ares_queue_wait_empty.3
/usr/share/man/man3/ares_reinit.3
/usr/share/man/man3/ares_save_options.3
/usr/share/man/man3/ares_search.3
/usr/share/man/man3/ares_search_dnsrec.3
/usr/share/man/man3/ares_send.3
/usr/share/man/man3/ares_send_dnsrec.3
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
/usr/share/man/man3/ares_svcb_param_t.3
/usr/share/man/man3/ares_threadsafety.3
/usr/share/man/man3/ares_timeout.3
/usr/share/man/man3/ares_tlsa_match_t.3
/usr/share/man/man3/ares_tlsa_selector_t.3
/usr/share/man/man3/ares_tlsa_usage_t.3
/usr/share/man/man3/ares_version.3

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libcares.so.2.13.0
/usr/lib64/libcares.so.2
/usr/lib64/libcares.so.2.13.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/c-ares/12127d9b9e698989a5b23087aa7c39f5e6eb264e
