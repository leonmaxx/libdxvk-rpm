%undefine _hardened_build

Name:			libdxvk
Version:		0.96
Release:		8%{?dist}
Summary:		A Vulkan-based translation layer for Direct3D 10/11
License:		zlib
Url:			https://github.com/doitsujin/dxvk
Source0:		dxvk-%{version}.tar.gz
Source1:		dxvk-native-headers-master.zip

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  wine-devel
BuildRequires:  glslang
BuildRequires:  vulkan-devel

%if 0%{?rhel}
BuildRequires:  devtoolset-8-gcc-c++
BuildRequires:  devtoolset-8-libstdc++-devel
%endif

Requires: vulkan

%description
A Vulkan-based translation layer for Direct3D 10/11 which allows running 3D applications on Linux using Wine.

%package devel
Version:        %{version}
Release:        %{release}
Summary:        Development files for DXVK
License:        zlib
Requires:		libdxvk%{_isa} = %{version}-%{release}

%description devel
%{summary}.

%prep
%setup -q -n dxvk-%{version}

mkdir include/native
unzip -j %{SOURCE1} -d include/native

%build

%if 0%{?rhel}
. /opt/rh/devtoolset-8/enable

%define _vpath_srcdir .
%define _vpath_builddir ./build
%endif

%meson
%meson_build

%install

%if 0%{?rhel}
. /opt/rh/devtoolset-8/enable
%endif

%meson_install

%files
%defattr(-,root,root)
%doc LICENSE README.md RELEASE
%{_libdir}/*.so

%files devel
%{_includedir}/*
%{_libdir}/pkgconfig/libdxvk.pc


%changelog
* Thu Feb 21 2019 Leonid Maksymchuk <leonmaxx@4menteam.com>
- initial packaging
