%define	pdir	B
%define	pnam	Graph
%include	/usr/lib/rpm/macros.perl
Summary:	B-Graph perl module
Summary(pl):	Modu³ perla B-Graph
Name:		perl-B-Graph
Version:	0.51
Release:	4

License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
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
