%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	TakTuk wrapper for cluster management and administration
Name:		kanif
Version:	1.2.2
Release:	2
License:	GPLv2+
Group:		System/Cluster
Url:		http://taktuk.gforge.inria.fr/kanif/
Source0:	http://gforge.inria.fr/frs/download.php/3984/kanif-%{version}.tar.gz
Source10:	%{name}.rpmlintrc
Requires:	taktuk

%description
kanif is a tool for cluster management and administration. It combines
main features of well known cluster management tools such as c3, pdsh
and dsh and mimics their syntax. For the effective cluster management
it relies on TakTuk, a tool for large scale remote execution deployment.

For simple parallel tasks that have to be executed on regular machines
such as clusters, TakTuk syntax is too complicated. The goal of kanif
is to provide an easier and familiar syntax to cluster administrators
while still taking advantage of TakTuk characteristics and features
(adaptivity, scalability, portability, autopropagation and informations
redirection).

%files
%doc install_doc/*
%{_bindir}/kaget
%{_bindir}/kanif
%{_bindir}/kaput
%{_bindir}/kash
%{_libdir}/pkgconfig/kanif.pc
%{_mandir}/man1/kaget.1.*
%{_mandir}/man1/kanif.1.*
%{_mandir}/man1/kaput.1.*
%{_mandir}/man1/kash.1.*
%{_mandir}/man5/kanif.conf.5.*

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%configure2_5x
make

%install
%makeinstall_std

mkdir tmp_doc
mv %{buildroot}%{_datadir}/doc/%{name} install_doc/

