Summary:	Program to map and configure your Easy Access Keys
Summary(pl):	Program do mapowania i konfiguracji klawiszy LinEAK
Name:		klineakconfig
Version:	0.5.1
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/lineak/%{name}-%{version}.tar.gz
URL:		http://lineak.sourceforge.net/
BuildRequires:	kdelibs-devel
BuildRequires:	lineakd
Requires:	lineakd >= 0.4pre2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_htmldir	/usr/share/doc/kde/HTML

%description
KlineakConfig is a configuration and control program for the lineakd
daemon that provides access to your keyboards easy access keys.

%description -l pl
KlineakConfig to program do konfiguracji i sterowania demonem lineakd
pozwalaj±cym na korzystanie z "klawiszy ³atwego dostêpu".

%prep
%setup -q

%build
kde_appsdir="%{_applnkdir}"; export kde_appsdir
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

%configure2_13

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	 DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/klineakconfig
%{_datadir}/apps/klineakconfig
%{_applnkdir}/Applications/*.desktop
%{_pixmapsdir}/*/*/apps/*.png
