# Maintainer: Perry Werneck <perry.werneck@gmail.com>

# SPDX-License-Identifier: LGPL-3.0-or-later 

# Copyright (C) 2026 Perry Werneck <perry.werneck@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

project(
	'libfatfs', 
	['c'],
	version: '0.16.0',
	license: 'GPL-3.0-or-later',
)

project_description = 'FAT file system library for embedded systems'

#
# Versioning
#
pkg_version = meson.project_version()
version_array = pkg_version.split('.')
pkg_major_version = version_array[0].to_int()
pkg_minor_version = version_array[1].to_int()
libversion = '@0@.@1@'.format(pkg_major_version,pkg_minor_version)

#
# Compiler flags
#
cc = meson.get_compiler('c')
enable_debug = get_option('debug') or get_option('buildtype').contains('debug')

linker_flags = [
]

compiler_flags = [
  '-fPIC',
  '-ggdb3',
  '-fPIC'
]

if enable_debug
  compiler_flags += [
	  '-DDEBUG=1'
  ]
else
  compiler_flags += [
	'-DNDEBUG=1'
  ]
endif

add_project_arguments(cc.get_supported_arguments(compiler_flags), language: 'c')

lib_src = [
  'library/diskio.c', 
  'source/ff.c',
  'source/ffsystem.c',  
  'source/ffunicode.c',
 ]

#
# SDK
# https://mesonbuild.com/Pkgconfig-module.html
#
if cc.get_id() != 'msvc'

  pkg = import('pkgconfig')

  pkg.generate(
    name: meson.project_name(),
    description: project_description,
    libraries: [ '-lfatfs' ]
  )

endif

#
# Targets
#
static_library = declare_dependency(
  link_with : static_library(
    'fatfs', 
    lib_src,
    install: true,
    c_args: [ '-fno-lto' ],
    include_directories: [ 'include', 'include/fatfs' ],
  ),
  include_directories: [ 'include' ],
)

dynamic_library = declare_dependency(
  link_with : shared_library(
    meson.project_name(), 
    lib_src,
    install: true,
    version : libversion,
    soversion : libversion,
    include_directories: [ 'include', 'include/fatfs' ],
  ),
  include_directories: [ 'include' ],
)

#
# Install headers
#
install_headers(
  'include/fatfs/diskio.h',
  'include/fatfs/ffconf.h', 
  'include/fatfs/ff.h',
  subdir: 'fatfs'  
)


