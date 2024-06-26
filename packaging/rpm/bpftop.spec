# Generated by rust2rpm 26
%bcond_without check

# prevent library files from being installed
%global cargo_install_lib 0

Name:           bpftop
Version:        0.5.1
Release:        %autorelease
Summary:        Dynamic real-time view of running eBPF programs

SourceLicense:  Apache-2.0
# 0BSD OR MIT OR Apache-2.0
# Apache-2.0
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# BSD-2-Clause
# BSD-2-Clause OR Apache-2.0 OR MIT
# BSD-3-Clause
# BSD-3-Clause OR MIT OR Apache-2.0
# LGPL-2.1-only OR BSD-2-Clause
# MIT
# MIT OR Apache-2.0
# MIT OR Zlib OR Apache-2.0
License:        (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (BSD-2-Clause) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND (BSD-3-Clause) AND (BSD-3-Clause OR MIT OR Apache-2.0) AND (LGPL-2.1-only OR BSD-2-Clause) AND (MIT) AND (MIT OR Apache-2.0) AND (MIT OR Zlib OR Apache-2.0)
# LICENSE.dependencies contains a full license breakdown

URL:            https://github.com/Netflix/%{name}
Source0:        https://github.com/Netflix/%{name}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  cargo-rpm-macros >= 26
BuildRequires:  elfutils-libelf-devel
BuildRequires:  zlib-devel
BuildRequires:  clang

Requires:       elfutils-libelf
Requires:       zlib

%global _description %{expand:
Dynamic real-time view of running eBPF programs.}

%description %{_description}

%prep
%autosetup -n %{name}-%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%files
%license LICENSE
%license LICENSE.dependencies
%doc README.md
%{_bindir}/bpftop

%changelog
%autochangelog
