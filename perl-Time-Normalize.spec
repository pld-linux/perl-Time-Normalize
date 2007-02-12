#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Time
%define		pnam	Normalize
Summary:	Time::Normalize - convert time and date values into standardized components
Summary(pl.UTF-8):   Time::Normalize - konwersja wartości czasu i dany na ustandaryzowane składniki
Name:		perl-Time-Normalize
Version:	0.03
Release:	1
# "same as perl"
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8b2e0846694b4d1e31be77099ebb5cd3
URL:		http://search.cpan.org/dist/Time-Normalize/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module performs simple but tedious (and error-prone) checks on
its inputs, and returns the time and/or date components in a
sanitized, standardized manner, suitable for use in the remainder of
your program.

%description -l pl.UTF-8
Ten moduł wykonuje proste ale nudne sprawdzenia na danych wejsciowych
i zwraca czas i/lub składniki daty w standardowej postaci,
używalnej w pozostałej części programu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Time/Normalize.pm
%{_mandir}/man3/*
