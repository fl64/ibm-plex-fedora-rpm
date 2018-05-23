Name: ibm-plex-font
Version: 0.1
Release: 1%{?dist}
Summary: RPM-package for IBM-plex fonts

License: SIL Open Font License 1.1
URL: https://github.com/IBM/plex
BuildArch:      noarch
Source: txt.tar.gz

BuildRequires: git


Prefix:/usr/share/fonts/IBMPlex

%define _topdir %(echo $PWD)/
%undefine _missing_build_ids_terminate_build

%description

%install
cd $RPM_BUILD_ROOT
git clone -b v1.0.2 https://github.com/IBM/plex.git
mkdir -p $RPM_BUILD_ROOT/%{prefix}
cd plex
find . -iname "*.ttf" -exec cp {} $RPM_BUILD_ROOT/%{prefix} \;
cd ..
rm -rf $RPM_BUILD_ROOT/plex

%files
%defattr(-,root,root,0755)
%{prefix}

%post
/usr/bin/fc-cache -r
