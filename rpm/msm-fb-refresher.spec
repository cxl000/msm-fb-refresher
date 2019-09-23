Name:		msm-fb-refresher
Version:	0.2
Release:	1%{?dist}
Summary:	Display refresher for Qualcom devices

Group:		System
License:	GPL2
URL:		https://github.com/AsteroidOS/msm-fb-refresher
Source0:	%{name}-%{version}.tar.bz2
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	kernel-headers
#Requires:	

%description


%prep
%setup -q


%build
gcc refresher.c -o refresher.o -c
gcc refresher.o -o msm-fb-refresher


%install
rm -rf $RPM_BUILD_ROOT
install -Dm755 msm-fb-refresher %{buildroot}/%{_sbindir}/msm-fb-refresher


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_sbindir}/msm-fb-refresher


%changelog

