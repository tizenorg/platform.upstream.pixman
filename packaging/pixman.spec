Name:           pixman
Version:        0.28.2
Release:        0
License:        MIT
Summary:        Pixel manipulation library
Url:            http://www.x.org/
Group:          System/Libraries
Source:         %{name}-%{version}.tar.gz
BuildRequires:  pkgconfig(libpng12)

%description
The pixel-manipulation library for X and cairo.

%package devel
Summary:        Development components for the pixman library
Group:          Development/Libraries
Requires:       %{name} = %{version}

%description devel
The pixel-manipulation library for X and cairo.

Development components for the pixman library.

%prep
%setup -q

%build

%configure --disable-arm-iwmmxt
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

