#
# Conditional build:
# _with_tests - perform "make test" - working database connection required
#
%include	/usr/lib/rpm/macros.perl
%define		pname	Pg
%define		module	pgperl
Summary:        Perl interface to PostgreSQL database
Summary(es):    M�dulo Perl para acceder un servidor PostgreSQL
Summary(pl):    Interfejs dla Perla umo�liwiaj�cy dost�p do baz PostgreSQL
Summary(pt_BR): M�dulo Perl para acesso ao servidor PostgreSQL
Summary(ru):    ���������� � ������ ��� ������� � postgresql �� perl
Summary(uk):    ��̦����� �� ����̦ ��� ������� �� postgresql � Perl
Summary(zh_CN): PostgreSQL �� PL/Perl ��������
Name:		perl-%{pname}
Version:	2.0.2
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://gborg.postgresql.org/pub/pgperl/stable/%{module}-%{version}.tar.gz
URL:		http://gborg.postgresql.org/project/pgperl/projdisplay.php
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	postgresql-devel
Requires:	perl >= 5.6
Obsoletes:	postgresql-perl
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is an interface between Perl and PostgreSQL. This uses the
Perl5 API for C extensions to call the PostgreSQL libpq interface.
Unlike DBD:pg, pgperl tries to implement the libpq interface as
closely as possible.

%description -l pl
Ten modu� jest interfejsem mi�dzy Perlem a PostgreSQL-em. U�ywa API
Perla 5 dla rozszerze� C, aby odwo�ywa� si� do interfejsu libpq
PostgreSQL-a. W przeciwie�stwie do DBD::pg, pgperl jest pr�b�
implementacji interfejsu libpq tak blisk�, jak to tylko mo�liwe.

%prep
%setup -q -n %{pname}-%{version}

%build
POSTGRES_HOME=%{_prefix}
export POSTGRES_HOME
%{__perl} Makefile.PL
%{__make}

%{?_with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_sitearch}/auto/Pg
%attr(755,root,root) %{perl_sitearch}/auto/Pg/*.so
%{perl_sitearch}/auto/Pg/*.bs
%{perl_sitearch}/*.pm
%{_mandir}/man[13]/*
