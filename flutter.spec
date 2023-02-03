%define _build_pkgcheck_set %{_bindir}/true

%global _channel stable
%global _version 2.10.4
%global _install_dir /opt/flutter

Name: flutter
Version: %{_version}
Release: 1%{?dist}
License: BSD-3-Clause
Url: http://flutter.dev
Summary: Flutter

Source0: https://storage.googleapis.com/flutter_infra_release/releases/%{_channel}/linux/flutter_linux_%{_version}-%{_channel}.tar.xz

BuildRequires: tar

Requires: bash coreutils curl file git libGLU1 unzip which xz zip

ExclusiveArch: %{ix86} x86_64

%description
Flutter is an open source UI toolkit for building beautiful, natively compiled applications for mobile, web, desktop, and embedded devices from a single codebase. 
Flutter is primarily funded by Google with contributors from all around the world.

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_install_dir}
tar -xf %{S:0} --strip-components=1 -C %{buildroot}%{_install_dir}
install -m 0755 -d %{buildroot}%{_install_dir}
ln -s %{_install_dir}/bin/dart %{buildroot}%{_bindir}
ln -s %{_install_dir}/bin/flutter %{buildroot}%{_bindir}

%post
chmod -R g+w,o+w %{_install_dir}


%files
%{_bindir}/dart
%{_bindir}/flutter
%{_install_dir}
