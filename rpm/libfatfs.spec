#
# spec file for package libfatfs
#
# Copyright (c) 2024 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:			libfatfs
Version:		0.15
Release:		1
Summary:		FAT file system library for embedded systems
License:		LGPL-3.0-only
Group:			System/Libraries
URL:			http://elm-chan.org/fsw/ff/00index_e.html
Source:			%{name}-%{version}.tar.xz
Source1:		meson.build
Source4:		diskio.c
Source5:		ffconf.h

%if 0%{?suse_version} >= 1500
BuildRequires:	gcc-c++ 
%else
BuildRequires:	gcc48-c++
%endif

BuildRequires:	pkg-config

%if 0%{?suse_version} >= 1504
BuildRequires:	meson >= 0.58.0
BuildRequires:	pkgconfig(libsystemd)
%else
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake
BuildRequires:	libtool
Source200:      autogen.sh
Source201:      Makefile.in
Source202:      configure.ac
Source203:		pkgconfig.pc.in
%endif

%description
FatFs is a generic FAT/exFAT filesystem module for small embedded systems. 
The FatFs module is written in compliance with ANSI C (C89) and completely separated from the disk I/O layer. 
Therefore it is independent of the platform. 
It can be incorporated into small microcontrollers with limited resource, such as 8051, PIC, AVR, ARM, Z80, RX and etc.

%define MAJOR_VERSION %(echo %{version} | cut -d. -f1)
%define MINOR_VERSION %(echo %{version} | cut -d. -f2)
%define _libvrs %{MAJOR_VERSION}_%{MINOR_VERSION}

%package -n %{name}%{_libvrs}
Summary:        Generic FAT Filesystem Module

%description -n %{name}%{_libvrs}
FatFs is a generic FAT/exFAT filesystem module for small embedded systems. 
The FatFs module is written in compliance with ANSI C (C89) and completely separated from the disk I/O layer. 
Therefore it is independent of the platform. 
It can be incorporated into small microcontrollers with limited resource, such as 8051, PIC, AVR, ARM, Z80, RX and etc.

%package devel
Summary:	FAT file system library for embedded systems
Group:		Development/Libraries/C and C++
Requires:	%{name}%{_libvrs} = %{version}

%description devel
FatFs is a generic FAT/exFAT filesystem module for small embedded systems. 
The FatFs module is written in compliance with ANSI C (C89) and completely separated from the disk I/O layer. 
Therefore it is independent of the platform. 
It can be incorporated into small microcontrollers with limited resource, such as 8051, PIC, AVR, ARM, Z80, RX and etc.

%prep
%if 0%{?suse_version} < 1200
%setup
%else
%autosetup
%endif

%if 0%{?suse_version} < 1500
export CC=gcc-4.8
export CXX=g++-4.8 
%endif

install --mode=644 %{S:4} source/diskio.c
install --mode=644 %{S:5} source/ffconf.h

%if 0%{?suse_version} >= 1504
install --mode=644 %{S:1} meson.build
%meson
%else
install --mode=755 %{S:200} .
install --mode=644 %{S:201} .
install --mode=644 %{S:202} .
install --mode=644 %{S:203} .
NOCONFIGURE=1 ./autogen.sh
%configure
%endif

%build
%if 0%{?suse_version} >= 1504
%meson_build
%else
make all
%endif

%install
%if 0%{?suse_version} >= 1504
%meson_install
%else
%makeinstall
%endif

%files -n %{name}%{_libvrs}
%defattr(-,root,root)
%if 0%{?suse_version} >= 1500
%license LICENSE.txt
%endif
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root)

%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/pkgconfig/*.pc

%dir %{_includedir}/fatfs
%{_includedir}/fatfs/*.h

%post -n %{name}%{_libvrs} -p /sbin/ldconfig

%postun -n %{name}%{_libvrs} -p /sbin/ldconfig

%changelog


