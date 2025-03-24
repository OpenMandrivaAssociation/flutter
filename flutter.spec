Name:		flutter
Version:	3.29.0
Release:	7
Summary:	SDK for crafting beautiful, fast user experiences from a single codebase
License:	BSD-3-Clause
URL:		https://flutter.dev
Group:		Development/Other
Source0:	https://storage.googleapis.com/flutter_infra_release/releases/stable/linux/flutter_linux_%{version}-stable.tar.xz
Source100:	flutter.rpmlintrc
Requires:	bash
Requires:	cmake
Requires:	clang
Requires:	ninja
Requires:	pkgconfig(gtk+-3.0)
Requires:	pkgconfig(liblzma)
Requires:	pkgconfig(glu)
Requires:	libstdc++-devel
Requires:	curl
Requires:	git
Requires:	file
Requires:	which
Requires:	zip
Requires:	xz
ExclusiveArch:	%{x86_64}

%description
Flutter transforms the app development process. Build, test, and deploy
beautiful mobile, web, desktop, and embedded apps from a single codebase.

%prep
tar xf %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{_datadir} %{buildroot}%{_bindir}
mv %{name} %{buildroot}%{_datadir}/

# wrapper script
cat << EOF > %{buildroot}%{_bindir}/%{name}
#!/bin/sh
export PATH="$PATH:%{_datadir}/%{name}/bin"
exec %{_datadir}/%{name}/bin/flutter "$@"
EOF

%files
%attr(0755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
