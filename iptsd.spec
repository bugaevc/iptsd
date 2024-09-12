%global optflags -O3 -g

Name: iptsd
Version: 2
Release: 1.mine%{?dist}
Summary: Userspace daemon for Intel Precise Touch & Stylus
License: GPLv2+

URL: https://github.com/linux-surface/iptsd
Source: {{{ create_tarball }}}

BuildRequires: meson
BuildRequires: gcc-g++

# Some of our dependencies can only be resolved with cmake
BuildRequires: cmake

# Daemon
BuildRequires: cmake(CLI11)
BuildRequires: pkgconfig(eigen3)
BuildRequires: pkgconfig(fmt)
BuildRequires: pkgconfig(inih)
BuildRequires: cmake(Microsoft.GSL)
BuildRequires: pkgconfig(spdlog)

# Debug Tools
BuildRequires: pkgconfig(cairomm-1.0)
BuildRequires: pkgconfig(sdl2)

BuildRequires: pkgconfig(systemd)
BuildRequires: pkgconfig(udev)
BuildRequires: systemd-rpm-macros

%description
iptsd is a userspace daemon that processes touch events from the IPTS
kernel driver, and sends them back to the kernel using uinput devices.

%prep
%autosetup

%build

%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license LICENSE
%doc README.md
%config(noreplace) %{_sysconfdir}/iptsd.conf
%dir %{_datadir}/iptsd
%dir %{_sysconfdir}/iptsd.d
%{_bindir}/iptsd
%{_bindir}/iptsd-check-device
%{_bindir}/iptsd-calibrate
%{_bindir}/iptsd-dump
%{_bindir}/iptsd-find-hidraw
%{_bindir}/iptsd-find-service
%{_bindir}/iptsd-perf
%{_bindir}/iptsd-plot
%{_bindir}/iptsd-show
%{_unitdir}/iptsd@.service
%{_udevrulesdir}/50-iptsd.rules
%{_datadir}/iptsd/*
