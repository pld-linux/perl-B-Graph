%include	/usr/lib/rpm/macros.perl
Summary:	B-Graph perl module
Summary(pl):	Modu³ perla B-Graph
Name:		perl-B-Graph
Version:	0.51
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/B/B-Graph-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
B-Graph - Perl Compiler backend to diagram OP trees.

%description -l pl
Modu³ perla B-Graph.

%prep
%setup -q -n B-Graph-%{version}

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
%{perl_sitelib}/B/Graph.pm
%{_mandir}/man3/*
