/* SPDX-License-Identifier: LGPL-3.0-or-later */

/*
 * Copyright (C) 2026 Perry Werneck <perry.werneck@gmail.com>
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Lesser General Public License as published
 * by the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public License
 * along with this program.  If not, see <https://www.gnu.org/licenses/>.
 */

 #include "ff.h"

 #define N_( x ) x
 
 const char * f_strerror (FRESULT result) {

	static const struct {
		FRESULT result;
		const char *text;
	} errors[] = {
		{ FR_OK,                    N_("Succeeded") },
		{ FR_DISK_ERR,              N_("A hard error occurred in the low level disk I/O layer") },
		{ FR_INT_ERR,               N_("Assertion failed") },
		{ FR_NOT_READY,             N_("The physical drive cannot work") },
		{ FR_NO_FILE,               N_("Could not find the file") },
		{ FR_NO_PATH,               N_("Could not find the path") },
		{ FR_INVALID_NAME,          N_("The path name format is invalid") },
		{ FR_DENIED,                N_("Access denied due to prohibited access or directory full") },
		{ FR_EXIST,                 N_("Access denied due to prohibited access") },
		{ FR_INVALID_OBJECT,        N_("The file/directory object is invalid") },
		{ FR_WRITE_PROTECTED,       N_("The physical drive is write protected") },
		{ FR_INVALID_DRIVE,         N_("The logical drive number is invalid") },
		{ FR_NOT_ENABLED,           N_("The volume has no work area") },
		{ FR_NO_FILESYSTEM,         N_("There is no valid FAT volume") },
		{ FR_MKFS_ABORTED,          N_("The f_mkfs() aborted due to any problem") },
		{ FR_TIMEOUT,               N_("Could not get a grant to access the volume within defined period") },
		{ FR_LOCKED,                N_("The operation is rejected according to the file sharing policy") },
		{ FR_NOT_ENOUGH_CORE,       N_("LFN working buffer could not be allocated") },
		{ FR_TOO_MANY_OPEN_FILES,   N_("Number of open files > FF_FS_LOCK") },
		{ FR_INVALID_PARAMETER,     N_("Given parameter is invalid") },
	};

	int ix;
	for(ix = 0; ix < (sizeof(errors)/sizeof(errors[0])); ix++) {
		if(errors[ix].result == result) {
			return errors[ix].text;
		}
	}

	return N_( "Unexpected fatfs error" );
 }
