%include	/usr/lib/rpm/macros.perl
Summary:	Proc-SyncExec perl module
Summary(pl):	Modu� perla Proc-SyncExec
Name:		perl-Proc-SyncExec
Version:	1.00
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Proc/Proc-SyncExec-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Proc-SyncExec module contains functions for synchronized process
spawning with full error return.

%description -l pl
Modu� Proc-SyncExec zawiera funkcje do synchonicznego mno�enia
proces�w z pe�nym raportowaniem o b��dach.

%prep
%setup -q -n Proc-SyncExec-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Proc/SyncExec.pm
%{_mandir}/man3/*
