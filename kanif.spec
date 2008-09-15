Name:		kanif
Summary:	TakTuk wrapper for cluster management and administration
Version:	1.2.1
Release:	%mkrel 2
Requires:	taktuk
Group:		System/Cluster
License:	GPLv2+
URL:		http://taktuk.gforge.inria.fr/kanif/
Source:		http://gforge.inria.fr/frs/download.php/3984/kanif-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-buildroot
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

%prep
%setup -q

%build
%configure
%__make

%install
%{__rm} -Rf %{buildroot}
%makeinstall

%{__mkdir} tmp_doc
%{__mv} %{buildroot}%{_datadir}/doc/%{name} install_doc/

%clean
%{__rm} -Rf %{buildroot}

%files
%defattr(-,root,root)
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
