%include	/usr/lib/rpm/macros.perl
Summary:	Proc-SyncExec perl module
Summary(pl):	Modu³ perla Proc-SyncExec
Name:		perl-Proc-SyncExec
Version:	0.01
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Proc/Proc-SyncExec-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Proc-SyncExec module contains functions for synchronized process
spawning with full error return.

%description -l pl
Modu³ Proc-SyncExec zawiera funkcje do synchonicznego mno¿enia
procesów z pe³nym raportowaniem o b³êdach.

%prep
%setup -q -n Proc-SyncExec-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

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
