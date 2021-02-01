%global debug_package %{nil}
Name:           PCem
Version:        16
Release:        1%{?dist}
Summary:        PCem (short for PC Emulator) is an IBM PC emulator for Windows and Linux that specializes in running old operating systems and software that are designed for IBM PC compatibles. Originally developed as an IBM PC XT emulator, it later emulates other IBM PC compatible computers as well. (from wikipedia)
License:        GPLv2
URL:            http://pcem-emulator.co.uk
Source0:        http://pcem-emulator.co.uk/files/PCemV%{version}Linux.tar.gz
Source1:        https://github.com/ajacocks/PCem-RPM/raw/master/PCemV16.man
Patch0:         https://github.com/ajacocks/PCem-RPM/raw/master/PCemV16Linux-configure.patch

BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  openal-soft-devel
BuildRequires:  SDL2-devel
BuildRequires:  wxGTK3-devel

Requires:       openal-soft
Requires:       SDL2
Requires:       wxGTK3

%description
PCem (short for PC Emulator) is an IBM PC emulator for Windows and Linux that specializes in running old operating systems and software that are designed for IBM PC compatibles. Originally developed as an IBM PC XT emulator, it later emulates other IBM PC compatible computers as well. (from wikipedia)

%prep
%setup -c

%patch0 -p1

%build
./configure
aclocal
automake
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_docdir}
install -p -m 755 pcem %{buildroot}/%{_bindir}
install -d -p -m 755 %{buildroot}/%{_docdir}/pcem
install -p -m 644 Readme-BSD.txt %{buildroot}/%{_docdir}/pcem
install -p -m 644 Readme-LINUX.txt %{buildroot}/%{_docdir}/pcem
install -p -m 644 readme.txt %{buildroot}/%{_docdir}/pcem
install -d -p -m 755 %{buildroot}/%{_mandir}/man1
gzip -c %{_sourcedir}/PCemV16.man > %{buildroot}/%{_mandir}/man1/pcem.1.gz
install -d -p -m 755 %{buildroot}/%{_datadir}/pcem
install -d -p -m 755 %{buildroot}/%{_datadir}/pcem/roms

%files
%{_bindir}/pcem
%doc %{_docdir}/pcem/Readme-BSD.txt
%doc %{_docdir}/pcem/Readme-LINUX.txt
%doc %{_docdir}/pcem/readme.txt
%doc %{_mandir}/man1/pcem.1.gz
%dir %{_datadir}/pcem
%dir %{_datadir}/pcem/roms

%changelog
* Sat Jun 13 2020 <alexander@redhat.com>
- Initial revision of package
