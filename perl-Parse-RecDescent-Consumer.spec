%define upstream_name    Parse-RecDescent-Consumer
%define upstream_version 1.03

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Parse::RecDescent::Consumer - reveal text matched through n token transitions
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Parse/%{upstream_name}-%{upstream_version}.tar.bz2

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
A common need when writing grammars is to know how much text was
consumed at different points in a parse. Usually, this involves a lot
of brain-twisting unwinding of of highly nested list-of-lists (of
lists...). Instead this module allows you to take the low-road
approach. You simply create a Consumer which records the current
text about to be parsed. 

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
