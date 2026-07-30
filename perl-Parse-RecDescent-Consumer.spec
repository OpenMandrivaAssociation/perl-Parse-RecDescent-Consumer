%define upstream_name    Parse-RecDescent-Consumer
%define upstream_version 1.03
Name:		perl-%{upstream_name}
Version:	1.03
Release:	1

Summary:	Parse::RecDescent::Consumer - reveal text matched through n token transitions
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Parse-RecDescent-Consumer
Source0:	https://cpan.metacpan.org/authors/id/T/TB/TBONE/Parse-RecDescent-Consumer-1.03.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildArch:	noarch

%description
A common need when writing grammars is to know how much text was
consumed at different points in a parse. Usually, this involves a lot
of brain-twisting unwinding of of highly nested list-of-lists (of
lists...). Instead this module allows you to take the low-road
approach. You simply create a Consumer which records the current
text about to be parsed. 

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes
%{perl_vendorlib}/Parse/RecDescent/Consumer.pm
%{_mandir}/*/*

