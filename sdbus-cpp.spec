%define major 2
%define libname %mklibname sdbus-cpp
%define devname %mklibname sdbus-cpp -d
%define codegen sdbus-cpp-xml2cpp

Summary: High-level C++ D-Bus library
Name: sdbus-cpp
Version: 2.3.1
Release: 1
Source0: https://github.com/Kistler-Group/sdbus-cpp/archive/refs/tags/v%{version}.tar.gz
URL: https://github.com/Kistler-Group/sdbus-cpp
License: LGPL-2.1
Group: System/Libraries
BuildSystem: cmake
BuildRequires: pkgconfig(libsystemd)
BuildRequires: pkgconfig(expat)
BuildOption: -DSDBUSCPP_BUILD_CODEGEN=ON

%description
High-level C++ D-Bus library.

%conf -a
%if %{cross_compiling}
# Workaround for -isystem /usr/include appearing in build flags
sed -i -e 's,-isystem /usr/include,,' _OMV_rpm_build/build.ninja
%endif

%package -n %{libname}
Summary: High-level C++ D-Bus library
Group: System/Libraries

%description -n %{libname}
High-level C++ D-Bus library.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%package -n %{codegen}
Summary: sdbus-c++ xml to cpp code generation tool 
Group: Development/C
Requires: %{libname} = %{EVRD}
Requires: %{devname}

%description -n %{codegen}
The codegen tool sdbus-c++-xml2cpp genrates high level C++ bindings out of the D-Bus IDL XML description.

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%doc %{_docdir}/sdbus-c++
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_libdir}/cmake/*

%files -n %{codegen}
%{_bindir}/sdbus-c++-xml2cpp
