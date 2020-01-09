Summary:   Compat package with colord 1.0 libraries
Name:      compat-colord10
Version:   1.0.4
Release:   1%{?dist}
License:   GPLv2+ and LGPLv2+
URL:       http://www.freedesktop.org/software/colord/
Source0:   http://www.freedesktop.org/software/colord/releases/colord-%{version}.tar.xz

BuildRequires: dbus-devel
BuildRequires: docbook-utils
BuildRequires: gettext
BuildRequires: glib2-devel
BuildRequires: intltool
BuildRequires: systemd-devel
BuildRequires: lcms2-devel >= 2.2
BuildRequires: libgudev1-devel
BuildRequires: polkit-devel >= 0.103
BuildRequires: sqlite-devel
BuildRequires: gobject-introspection-devel
BuildRequires: libgusb-devel
BuildRequires: color-filesystem

%description
Compatibility package with colord 1.0 libraries.

%package -n compat-libcolord1
Summary: Compat package with colord 1.0 libraries
Conflicts: colord < 1.2

%description -n compat-libcolord1
Compatibility package with colord 1.0 libraries.

%prep
%setup -q -n colord-%{version}

%build
%configure \
        --with-daemon-user=colord \
        --disable-gtk-doc \
        --disable-vala \
        --disable-print-profiles \
        --disable-bash-completion \
        --disable-static \
        --disable-rpath \
        --disable-examples \
        --disable-silent-rules \
        --disable-dependency-tracking

make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

# Remove static libs and libtool archives.
find %{buildroot} -name '*.la' -exec rm -f {} ';'
find %{buildroot} -name '*.a' -exec rm -f {} ';'

rm -rf $RPM_BUILD_ROOT%{_sysconfdir}
rm -rf $RPM_BUILD_ROOT%{_bindir}
rm -rf $RPM_BUILD_ROOT%{_includedir}
rm -rf $RPM_BUILD_ROOT%{_prefix}/lib/systemd
rm -rf $RPM_BUILD_ROOT%{_prefix}/lib/udev
rm -rf $RPM_BUILD_ROOT%{_libdir}/colord-plugins/
rm -rf $RPM_BUILD_ROOT%{_libdir}/colord-sensors/
rm -rf $RPM_BUILD_ROOT%{_libdir}/girepository-1.0/
rm -rf $RPM_BUILD_ROOT%{_libdir}/libcolord.la
rm -rf $RPM_BUILD_ROOT%{_libdir}/libcolord.so
rm -rf $RPM_BUILD_ROOT%{_libdir}/libcolordprivate.lo
rm -rf $RPM_BUILD_ROOT%{_libdir}/libcolordprivate.so
rm -rf $RPM_BUILD_ROOT%{_libdir}/libcolorhug*
rm -rf $RPM_BUILD_ROOT%{_libdir}/pkgconfig/
rm -rf $RPM_BUILD_ROOT%{_libexecdir}
rm -rf $RPM_BUILD_ROOT%{_datadir}

%post -n compat-libcolord1 -p /sbin/ldconfig

%postun -n compat-libcolord1 -p /sbin/ldconfig

%files -n compat-libcolord1
%doc COPYING
%{_libdir}/libcolord.so.*
%{_libdir}/libcolordprivate.so.*

%changelog
* Tue May 05 2015 Richard Hughes <rhughes@redhat.com> - 1.0.4-1
- New compat package for RHEL
- Resolves: #1184213
