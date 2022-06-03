#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Data-Float
Version  : 0.013
Release  : 22
URL      : https://cpan.metacpan.org/authors/id/Z/ZE/ZEFRAM/Data-Float-0.013.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/Z/ZE/ZEFRAM/Data-Float-0.013.tar.gz
Summary  : 'details of the floating point data type'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Data-Float-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Module::Build)

%description
NAME
Data::Float - details of the floating point data type
DESCRIPTION
This module is about the native floating point numerical data type.
A floating point number is one of the types of datum that can appear
in the numeric part of a Perl scalar.  This module supplies constants
describing the native floating point type, classification functions,
and functions to manipulate floating point values at a low level.

%package dev
Summary: dev components for the perl-Data-Float package.
Group: Development
Provides: perl-Data-Float-devel = %{version}-%{release}
Requires: perl-Data-Float = %{version}-%{release}

%description dev
dev components for the perl-Data-Float package.


%package perl
Summary: perl components for the perl-Data-Float package.
Group: Default
Requires: perl-Data-Float = %{version}-%{release}

%description perl
perl components for the perl-Data-Float package.


%prep
%setup -q -n Data-Float-0.013
cd %{_builddir}/Data-Float-0.013

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Data::Float.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
