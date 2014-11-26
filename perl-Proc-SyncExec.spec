#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Proc
%define		pnam	SyncExec
%include	/usr/lib/rpm/macros.perl
Summary:	Proc::SyncExec perl module
Summary(pl.UTF-8):	Moduł perla Proc::SyncExec
Name:		perl-Proc-SyncExec
Version:	1.01
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	38dd51ed78504d73bf6520a044744cb8
URL:		http://search.cpan.org/dist/Proc-SyncExec/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Proc::SyncExec module contains functions for synchronized process
spawning with full error return.

%description -l pl.UTF-8
Moduł Proc::SyncExec zawiera funkcje do synchronicznego mnożenia
procesów z pełnym raportowaniem o błędach.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Proc/SyncExec.pm
%{_mandir}/man3/*
