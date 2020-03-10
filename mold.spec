#%{?scl:%scl_package mold}
%{!?scl:%global pkg_name %{name}}

Name: mold	
Version: 0.1
Release: %{?release}%{!?release:6}%{?dist}
Summary: a faster linker

License: AGPL
URL: https://github.com/rui314/mold
%if 0%{?gh_commit:1}
Source0: https://github.com/rui314/mold/%{gh_commit}.tar.gz#/%{name}-%{version}.tar.gz	
%else
Source0: https://github.com/rui314/mold/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
%endif

BuildRequires: %{?scl_prefix}gcc, %{?scl_prefix}binutils, %{?scl_prefix}gcc-c++, tbb-devel, zlib-devel, xxhash-devel
Requires: tbb, xxhash

%description

%prep
%if 0%{?gh_commit:1}
%setup -n %{pkg_name}-%{gh_commit} -q
%else
%setup -n %{pkg_name}-%{version} -q
%endif

%build

make %{?_smp_mflags}

%install
PREFIX=%{buildroot}/%{_usr} make install
PREFIX=%{buildroot}/%{_usr} make install

%files
%{_usr}/bin/mold

%changelog