%undefine _debugsource_packages

Name: aardvark-dns
Version: 1.13.1
Release: 1
Source0: https://github.com/containers/aardvark-dns/archive/refs/tags/v%{version}.tar.gz
Source1: vendor.tar.xz
Summary: DNS server for A/AAAA container records
URL: https://github.com/containers/aardvark-dns
License: Apache-2.0
Group: Servers
BuildRequires: golang
BuildRequires: go-md2man
BuildRequires: rust
BuildRequires: protobuf-compiler
BuildRequires: cargo

%description
Aardvark-dns is an authoritative dns server for A/AAAA container records.
It can forward other requests to configured resolvers.

%prep
%autosetup -p1 -a 1
mkdir .cargo
cat >>.cargo/config.toml <<'EOF'

[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF


%build
%make_build PREFIX=%{_prefix}

%install
%make_install PREFIX=%{_prefix}

%files
%{_libexecdir}/podman/aardvark-dns
