%include	/usr/lib/rpm/macros.perl
%define		pdir	B
%define		pnam	Graph
Summary:	B::Graph perl module
Summary(pl):	Modu� perla B::Graph
Name:		perl-B-Graph
Version:	0.51
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
B::Graph - Perl Compiler backend to diagram OP trees.

%description -l pl
Modu� perla B::Graph.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/B/Graph.pm
%{_mandir}/man3/*
