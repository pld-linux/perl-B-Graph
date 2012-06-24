#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	B
%define		pnam	Graph
Summary:	B::Graph - Perl compiler backend to produce graphs of OP trees
Summary(pl.UTF-8):	B::Graph - backend dla kompilatora Perla tworzący grafy drzew OP
Name:		perl-B-Graph
Version:	0.51
Release:	7
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	907943809a96d8ff9f0118a64e40e723
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
B::Graph module is a backend to the Perl compiler (B::*) which,
instead of outputting bytecode or C based on Perl's compiled version
of a program, writes descriptions in graph-description languages
specifying graphs that show the program's structure. It currently
generates descriptions for the VCG tool
("http://www.cs.uni-sb.de/RW/users/sander/html/gsvcg1.html") and Dot
(part of the graph visualization toolkit from AT&T:
"http://www.research.att.com/sw/tools/graphviz/"). It also can produce
plain text output (which is more useful for debugging the module
itself than anything else).

%description -l pl.UTF-8
Moduł B::Graph jest backendem dla kompilatora Perla (B::*), który
zamiast generować kod pośredni lub kod C w oparciu kompilowaną wersję
programu perlowego, wypisuje opisy w językach opisu grafów, tworząc
grafy ukazujące strukturę programu. Aktualnie generuje on opisy dla
narzędzi: VCG
("http://www.cs.uni-sb.de/RW/users/sander/html/gsvcg1.html") oraz Dot
(część zestawu narzędziowego AT&T do wizualizacji
grafów:"http://www.research.att.com/sw/tools/graphviz/"). Potrafi on
również generować czysto tekstowy wynik (który jest bardziej przydatny
do odpluskwiania samego modułu, niż do czegokolwiek innego).

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
%{perl_vendorlib}/B/Graph.pm
%{_mandir}/man3/*
