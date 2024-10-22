%define major 2
%define libname %mklibname sdbus-cpp
%define devname %mklibname sdbus-cpp -d

Summary: High-level C++ D-Bus library
Name: sdbus-cpp
Version: 2.0.0
Release: 1
Source0: https://github.com/Kistler-Group/sdbus-cpp/archive/%{name}-%{version}.tar.gz
URL: https://github.com/Kistler-Group/sdbus-cpp
License: LGPL-2.1
Group: System/Libraries
BuildRequires: cmake
BuildRequires: ninja
BuildRequires: pkgconfig(libsystemd)

%description
High-level C++ D-Bus library.

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

%prep
%autosetup -p1
%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%doc %{_docdir}/sdbus-c++
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_libdir}/cmake/*
