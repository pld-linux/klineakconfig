Summary:	Program to map and configure your Easy Access Keys
Summary(pl):	Program do mapowania i konfiguracji klawiszy LinEAK
Name:		klineakconfig
%define		beta	beta2
Version:	0.8
Release:	%{beta}.0.1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/lineak/%{name}-%{version}-%{beta}.tar.gz
# Source0-md5:	c6401c480d32112bbbd82972c41c4d7e
Patch0:		%{name}-desktop.patch
URL:		http://lineak.sourceforge.net/
BuildRequires:	kdelibs-devel
BuildRequires:	lineakd-defs
BuildRequires:	lineakd-devel
BuildRequires:	rpmbuild(macros) >= 1.129
Requires:	lineakd >= 0.4pre2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KlineakConfig is a configuration and control program for the lineakd
daemon that provides access to your keyboards easy access keys.

%description -l pl
KlineakConfig to program do konfiguracji i sterowania demonem lineakd
pozwalaj±cym na korzystanie z "klawiszy ³atwego dostêpu".

%prep
%setup -q -n %{name}-%{version}-%{beta}
%patch0 -p1

%build
kde_appsdir="%{_desktopdir}"; export kde_appsdir
kde_htmldir="%{_kdedocdir}"; export kde_htmldir
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
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*/*/apps/*.png
