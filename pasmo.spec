Name:		pasmo
Summary:	Portable Z80 cross assembler
Version:	0.5.5
Release:	2
License:	GPLv2
Group:		Development/Other
Url:		https://pasmo.speccy.org/
Source0:	https://pasmo.speccy.org/bin/pasmo-%{version}.tar.gz

%description
Pasmo is a Z80 cross assembler, written in standard C++ that compiles easily
in multiple platforms.

Actually can generate object code in the following formats: raw binary,
Intel HEX, PRL for CP/M Plus RSX, Plus3Dos (Spectrum +3 disk), TAP, TZX and
CDT (Spectrum and Amstrad CPC emulators tape images), AmsDos (Amstrad CPC disk)
and MSX (for use with BLOAD from disk in Basic).

%prep
%autosetup -p1

%build
autoreconf -vfi
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/pasmo
