Name:       libpthread-stubs
Summary:    PThread Stubs for XCB
Version:    0.4
Release:    1
Group:      System/X11
License:    MIT
URL:        http://xcb.freedesktop.org
Source0:    http://xcb.freedesktop.org/dist/libpthread-stubs-%{version}.tar.bz2
Source1:    libpthread-stubs-rpmlintrc

%description
This library provides weak aliases for pthread functions not provided in libc
or otherwise available by default

%prep
%setup -q -n %{name}-%{version}

%build
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/pthread-stubs.pc
