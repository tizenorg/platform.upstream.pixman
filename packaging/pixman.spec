#sbs-git:slp/pkgs/p/pixman pixman 0.26.0 67eba3516f06fef40915917d7396b68108ee6316

Name:           pixman
Version:        0.26.0
Release:        3
License:        MIT
Summary:        Pixel manipulation library
Url:            http://www.x.org/
Group:          System/Libraries
Source:         %{name}-%{version}.tar.bz2
BuildRequires:  pkgconfig(libpng12)
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
Pixel manipulation library

%package devel
Summary:        Development components for the pixman library
Group:          Development/Libraries
Requires:       %{name} = %{version}

%description devel
Pixel manipulation library

%prep
%setup -q

%build

%reconfigure --disable-arm-iwmmxt
make %{?_smp_mflags}

%install
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/libpixman-1*.so.*

%files devel
%defattr(-,root,root,-)
%dir %{_includedir}/pixman-1
%{_includedir}/pixman-1/pixman.h
%{_includedir}/pixman-1/pixman-version.h
%{_libdir}/libpixman-1*.so
%{_libdir}/pkgconfig/pixman-1.pc

