%define upstream_name    MooseX-SetOnce
%define upstream_version 0.100471

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Write-once, read-many attributes for Moose
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/MooseX/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Moose)
BuildRequires: perl(Moose::Role)
BuildRequires: perl(Test::More)
BuildRequires: perl(Try::Tiny)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
The 'SetOnce' attribute lets your class have attributes that are not lazy
and not set, but that cannot be altered once set.

The logic is very simple: if you try to alter the value of an attribute
with the SetOnce trait, either by accessor or writer, and the attribute has
a value, it will throw an exception.

If the attribute has a clearer, you may clear the attribute and set it
again.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml LICENSE README META.json
%{_mandir}/man3/*
%perl_vendorlib/*


