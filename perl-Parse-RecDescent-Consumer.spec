%define real_name Parse-RecDescent-Consumer

Summary:	Parse::RecDescent::Consumer - reveal text matched through n token transitions
Name:		perl-%{real_name}
Version:	1.03
Release:	%mkrel 2
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	%{real_name}-%{version}.tar.bz2
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
%setup -q -n %{real_name}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes
%{perl_vendorlib}/Parse/RecDescent/Consumer.pm
%{_mandir}/*/*

