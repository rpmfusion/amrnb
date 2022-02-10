Name:           amrnb
Version:        11.0.0.0
Release:        15%{?dist}
Summary:        Adaptive Multi-Rate (AMR) Speech Codec
Group:          System Environment/Libraries
License:        Distributable
URL:            http://www.penguin.cz/~utx/amr
Source0:        http://ftp.penguin.cz/pub/users/utx/amr/%{name}-%{version}.tar.bz2
Source1:        http://www.3gpp.org/ftp/Specs/archive/26_series/26.104/26104-b00.zip
BuildRequires:  unzip
BuildRequires:  gcc-c++

%description
Adaptive Multi-Rate Narrow-Band decoder and encoder library.
(3GPP TS 26.104 V 11.0.0)

http://www.3gpp.org/ftp/Specs/html-info/26104.htm


%package tools
Group:          Applications/Multimedia
Summary:        Adaptive Multi-Rate (AMR) Speech Codec tools
Requires:       %{name} = %{version}-%{release}

%description tools
Adaptive Multi-Rate Narrow-Band decoding and encoding tools.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q
cp -p %{SOURCE1} .


%build
%configure --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build


%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc AUTHORS ChangeLog NEWS README TODO readme.txt
%license COPYING
%{_libdir}/*.so.*

%files tools
%{_bindir}/*

%files devel
%{_includedir}/amrnb
%{_libdir}/*.so


%changelog
* Thu Feb 10 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 11.0.0.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 11.0.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 11.0.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 19 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 11.0.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 11.0.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 10 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 11.0.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 11.0.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 19 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 11.0.0.0-8
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 RPM Fusion Release Engineering <sergio@serjux.com> - 11.0.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 02 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 11.0.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 01 2017 Nicolas Chauvet <kwizart@gmail.com> - 11.0.0.0-5
- Avoid wget hack

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 11.0.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Mar 25 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 11.0.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Sep 01 2014 Sérgio Basto <sergio@serjux.com> - 11.0.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri May 30 2014 Hans de Goede <j.w.r.degoede@gmail.com> - 11.0.0.0-1
- New upstream release 11.0.0.0
- Fix FTBFS (rf#3243)

* Tue Mar 12 2013 Nicolas Chauvet <kwizart@gmail.com> - 7.0.0.2-7
- https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Feb 09 2012 Nicolas Chauvet <kwizart@gmail.com> - 7.0.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 7.0.0.2-5
- rebuild for new F11 features

* Sat Aug 16 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 7.0.0.2-4
- wget the needed sources in %%prep instead of letting the Makefile do it
  so that we can use an IP address to work around there being no
  /etc/resolv.conf in the buildroot

* Fri Jul 25 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 7.0.0.2-3
- Release bump for rpmfusion

* Thu Jun 12 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 7.0.0.2-2
- Fix rpath on x86_64
- Put tools in a seperate -tools package

* Thu Jun 12 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 7.0.0.2-1
- Initial rpmfusion package based on upstream specfile
