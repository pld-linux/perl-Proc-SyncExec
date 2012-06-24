%define		perl_sitelib	%(eval "`perl -V:installsitelib`"; echo $installsitelib)
Summary:	Proc-SyncExec perl module
Summary(pl):	Modu� perla Proc-SyncExec
Name:		perl-Proc-SyncExec
Version:	0.01
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Proc/Proc-SyncExec-%{version}.tar.gz
BuildRequires:	perl >= 5.005_03-10
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Proc-SyncExec module contains functions for synchronized process spawning with
full error return. 

%description -l pl
Modu� Proc-SyncExec zawiera funkcje do synchonicznego mno�enia proces�w
z pe�nym raportowaniem o b��dach.

%prep
%setup -q -n Proc-SyncExec-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Proc/SyncExec
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz

%{perl_sitelib}/Proc/SyncExec.pm
%{perl_sitearch}/auto/Proc/SyncExec

%{_mandir}/man3/*
