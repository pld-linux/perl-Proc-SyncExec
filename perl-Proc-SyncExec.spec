%include	/usr/lib/rpm/macros.perl
%define	pdir	Proc
%define	pnam	SyncExec
Summary:	Proc::SyncExec perl module
Summary(pl):	Modu³ perla Proc::SyncExec
Name:		perl-Proc-SyncExec
Version:	1.00
Release:	6
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e888bfb8bab757c1444d3613bd910266
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Proc::SyncExec module contains functions for synchronized process
spawning with full error return.

%description -l pl
Modu³ Proc::SyncExec zawiera funkcje do synchonicznego mno¿enia
procesów z pe³nym raportowaniem o b³êdach.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Proc/SyncExec.pm
%{_mandir}/man3/*
