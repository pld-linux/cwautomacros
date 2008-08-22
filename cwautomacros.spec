Summary:	A collection of autoconf macros
Name:		cwautomacros
Version:	20080318
Release:	1
License:	GPL
Group:		Development/Building
Source0:	http://download.berlios.de/cwautomacros/%{name}-%{version}.tar.bz2
# Source0-md5:	2991984bffd96222f2ae754872911022
URL:		http://cwautomacros.berlios.de/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cwautomacros is a collection of autoconf macros, plus an autogen.sh
script that can be used with them.

%prep
%setup -q

%build
for scripts in `ls scripts/*.sh`; do
	sed -i -e 's^@INSTALLPREFIX@^/usr^g' $scripts
done

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -a m4 scripts templates $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/index.php
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/m4
%{_datadir}/%{name}/m4/*.m4
%dir %{_datadir}/%{name}/scripts
%attr(755,root,root) %{_datadir}/%{name}/scripts/*.sh
%{_datadir}/%{name}/scripts/line2entity
%dir %{_datadir}/%{name}/templates
%attr(755,root,root) %{_datadir}/%{name}/templates/autogen.sh
%{_datadir}/%{name}/templates/doxygen
