Summary:	Program to map and configure your Easy Access Keys
Summary(pl.UTF-8):	Program do mapowania i konfiguracji klawiszy LinEAK
Name:		klineakconfig
%define		beta	beta2
Version:	0.9
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/lineak/%{name}-%{version}.tar.gz
# Source0-md5:	b673575854f8d31443e05614ebb3e238
Patch0:		%{name}-desktop.patch
URL:		http://lineak.sourceforge.net/
BuildRequires:	automake
BuildRequires:	kdelibs-devel
BuildRequires:	lineakd-defs
BuildRequires:	lineakd-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	sed >= 4.0
Requires:	lineakd >= 0.4pre2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KlineakConfig is a configuration and control program for the lineakd
daemon that provides access to your keyboards easy access keys.

%description -l pl.UTF-8
KlineakConfig to program do konfiguracji i sterowania demonem lineakd
pozwalającym na korzystanie z "klawiszy łatwego dostępu".

%prep
%setup -q
%patch0 -p1

# kill stupid plugin dir existence test
sed -i -e 's/test ! -d \$pdir/false/' configure

%build
cp -f /usr/share/automake/config.* admin
kde_appsdir="%{_desktopdir}"; export kde_appsdir
kde_htmldir="%{_kdedocdir}"; export kde_htmldir

%configure \
	--disable-rpath \
	--with-lineak-plugindir=%{_libdir}/lineakd/plugins \
	--with-qt-libraries=%{_libdir}
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
%{_iconsdir}/*/*/apps/*.png
