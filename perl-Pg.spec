#
# Conditional build:
%bcond_with	tests	# perform "make test" - working database connection required
#
%define		pnam	Pg
%define		module	pgperl
Summary:	Perl interface to PostgreSQL database
Summary(es.UTF-8):	Módulo Perl para acceder un servidor PostgreSQL
Summary(pl.UTF-8):	Interfejs dla Perla umożliwiający dostęp do baz PostgreSQL
Summary(pt_BR.UTF-8):	Módulo Perl para acesso ao servidor PostgreSQL
Summary(ru.UTF-8):	Библиотеки и модули для доступа к PostgreSQL из perl
Summary(uk.UTF-8):	Бібліотеки та модулі для доступу до PostgreSQL з Perl
Summary(zh_CN.UTF-8):	PostgreSQL 的 PL/Perl 程序语言
Name:		perl-Pg
Version:	2.0.2
Release:	21
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	ftp://gborg.postgresql.org/pub/pgperl/stable/%{module}-%{version}.tar.gz
# Source0-md5:	0813c5ab151dd37ad8938634550e6c1a
URL:		http://gborg.postgresql.org/project/pgperl/projdisplay.php
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	postgresql-devel
Obsoletes:	postgresql-perl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is an interface between Perl and PostgreSQL. This uses the
Perl5 API for C extensions to call the PostgreSQL libpq interface.
Unlike DBD:pg, pgperl tries to implement the libpq interface as
closely as possible.

%description -l pl.UTF-8
Ten moduł jest interfejsem między Perlem a PostgreSQL-em. Używa API
Perla 5 dla rozszerzeń C, aby odwoływać się do interfejsu libpq
PostgreSQL-a. W przeciwieństwie do DBD::pg, pgperl jest próbą
implementacji interfejsu libpq tak bliską, jak to tylko możliwe.

%prep
%setup -q -n %{pnam}-%{version}

%build
POSTGRES_HOME=%{_prefix}
export POSTGRES_HOME
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
%dir %{perl_vendorarch}/auto/Pg
%attr(755,root,root) %{perl_vendorarch}/auto/Pg/*.so
%{perl_vendorarch}/*.pm
%{_mandir}/man[13]/*
