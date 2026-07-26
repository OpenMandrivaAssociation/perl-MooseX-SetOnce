%define upstream_name    MooseX-SetOnce
Name:		perl-%{upstream_name}
Version:	0.203
Release:	2

Summary:	Write-once, read-many attributes for Moose
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/rjbs/MooseX-SetOnce
Source0:	https://cpan.metacpan.org/authors/id/R/RJ/RJBS/MooseX-SetOnce-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Moose::Role)
BuildRequires:	perl(Test::Fatal)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Try::Tiny)

BuildArch:	noarch

%description
The 'SetOnce' attribute lets your class have attributes that are not lazy
and not set, but that cannot be altered once set.

The logic is very simple: if you try to alter the value of an attribute
with the SetOnce trait, either by accessor or writer, and the attribute has
a value, it will throw an exception.

If the attribute has a clearer, you may clear the attribute and set it
again.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml LICENSE README META.json
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun Apr 17 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.200.0-1mdv2011.0
+ Revision: 654127
- update to new version 0.200000

* Thu Mar 10 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.100.473-1
+ Revision: 643411
- update to new version 0.100473

* Fri Nov 12 2010 Jérôme Quelin <jquelin@mandriva.org> 0.100.472-1mdv2011.0
+ Revision: 596628
- update to 0.100472

* Wed Jul 14 2010 Jérôme Quelin <jquelin@mandriva.org> 0.100.471-1mdv2011.0
+ Revision: 553057
- import perl-MooseX-SetOnce


* Wed Jul 14 2010 cpan2dist 0.100471-1mdv
- initial mdv release, generated with cpan2dist

