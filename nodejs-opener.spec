%define		pkg	opener
Summary:	Opens stuff, like webpages and files and executables, cross-platform
Name:		nodejs-%{pkg}
Version:	1.3.0
Release:	1
License:	WTFPL
Group:		Development/Libraries
URL:		https://github.com/domenic/opener
Source0:	http://registry.npmjs.org/%{pkg}/-/%{pkg}-%{version}.tgz
# Source0-md5:	9d2c2881d7da026c91829fe8072791a1
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Opens stuff, like webpages and files and executables, cross-platform.

%prep
%setup -qc
mv package/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{nodejs_libdir}/%{pkg}}
cp -a package.json opener.js $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE.txt
%{nodejs_libdir}/%{pkg}
