Name:		flutter
Version:	3.29.0
Release:	2
Summary:	SDK for crafting beautiful, fast user experiences from a single codebase
License:	BSD-3-Clause
URL:		https://flutter.dev
Group:		Development/Other
Source0:	https://github.com/flutter/flutter/archive/refs/tags/%{version}.tar.gz


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

%package    devel
Summary:    Development files for %{name}
Requires:   %{name} = %{version}-%{release}
%description devel
Development files for %{name}

%prep
tar xf %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{_datadir} %{buildroot}%{_bindir}
mv %{name}-%{version} %{buildroot}%{_datadir}/

# wrapper script
cat << EOF > %{buildroot}%{_bindir}/%{name}
#!/bin/sh
export PATH="$PATH:%{_datadir}/%{name}-%{version}/bin"
exec %{_datadir}/%{name}-%{version}/bin/flutter "$@"
EOF

%files
%attr(0755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}-%{version}/bin
%{_datadir}/%{name}-%{version}/.github
%{_datadir}/%{name}-%{version}/C*
%{_datadir}/%{name}-%{version}/AUTHORS
%{_datadir}/%{name}-%{version}/DEPS
%{_datadir}/%{name}-%{version}/LICENSE
%{_datadir}/%{name}-%{version}/PATENT_GRANT
%{_datadir}/%{name}-%{version}/README.md
%{_datadir}/%{name}-%{version}/TESTOWNERS
%{_datadir}/%{name}-%{version}/analysis_options.yaml
%{_datadir}/%{name}-%{version}/flutter_console.bat
%{_datadir}/%{name}-%{version}/dartdoc_options.yaml
%{_datadir}/%{name}-%{version}/.ci.yaml
%{_datadir}/%{name}-%{version}/.gitattributes
%{_datadir}/%{name}-%{version}/.vscode/settings.json
%{_datadir}/%{name}-%{version}/docs
%files devel
%{_datadir}/%{name}-%{version}/packages
%{_datadir}/%{name}-%{version}/dev
%{_datadir}/%{name}-%{version}/examples
%{_datadir}/%{name}-%{version}/engine
