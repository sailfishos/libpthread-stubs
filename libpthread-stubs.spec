# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.22
# 
# >> macros
# << macros

Name:       libpthread-stubs
Summary:    PThread Stubs for XCB
Version:    0.3
Release:    1
Group:      System/X11
License:    MIT
URL:        http://xcb.freedesktop.org
Source0:    http://xcb.freedesktop.org/dist/libpthread-stubs-%{version}.tar.bz2
Source1:    libpthread-stubs-rpmlintrc
Source100:  libpthread-stubs.yaml


%description
This library provides weak aliases for pthread functions not provided in libc
or otherwise available by default




%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%configure --disable-static
make %{?jobs:-j%jobs}

# >> build post
# << build post
%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post


# << install post






%files
%defattr(-,root,root,-)
# >> files
%{_libdir}/pkgconfig/pthread-stubs.pc
# << files

