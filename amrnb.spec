Name:           amrnb
Version:        7.0.0.2
Release:        3%{?dist}
Summary:        Adaptive Multi-Rate (AMR) Speech Codec
Group:          System Environment/Libraries
License:        Distributable
URL:            http://www.penguin.cz/~utx/amr
Source0:        http://ftp.penguin.cz/pub/users/utx/amr/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  wget unzip

%description
Adaptive Multi-Rate Narrow-Band decoder and encoder library.
(3GPP TS 26.104 V 7.0.0)

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


%build
%configure --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%clean
rm -rf $RPM_BUILD_ROOT


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr (-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README TODO readme.txt
%{_libdir}/*.so.*

%files tools
%defattr (-,root,root,-)
%{_bindir}/*

%files devel
%defattr (-,root,root,-)
%{_includedir}/amrnb
%{_libdir}/*.so


%changelog
* Fri Jul 25 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 7.0.0.2-3
- Release bump for rpmfusion

* Thu Jun 12 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 7.0.0.2-2
- Fix rpath on x86_64
- Put tools in a seperate -tools package

* Thu Jun 12 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 7.0.0.2-1
- Initial rpmfusion package based on upstream specfile
