%define		kdeappsver	18.12.1
%define		qtver		5.9.0
%define		kaname		ksirk
Summary:	ksirk
Name:		ka5-%{kaname}
Version:	18.12.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	b0f9e1c8832f063c700182848a32fd2a
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Qml-devel >= 5.11.1
BuildRequires:	Qt5Quick-devel >= 5.11.1
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	gettext-devel
BuildRequires:	ka5-libkdegames-devel >= %{kdeappsver}
BuildRequires:	kf5-kcompletion-devel >= 5.30.0
BuildRequires:	kf5-kconfig-devel >= 5.30.0
BuildRequires:	kf5-kconfigwidgets-devel >= 5.30.0
BuildRequires:	kf5-kcoreaddons-devel >= 5.30.0
BuildRequires:	kf5-kcrash-devel >= 5.30.0
BuildRequires:	kf5-kdoctools-devel >= 5.30.0
BuildRequires:	kf5-ki18n-devel >= 5.30.0
BuildRequires:	kf5-kiconthemes-devel >= 5.30.0
BuildRequires:	kf5-kio-devel >= 5.30.0
BuildRequires:	kf5-knewstuff-devel >= 5.30.0
BuildRequires:	kf5-kwallet-devel >= 5.30.0
BuildRequires:	kf5-kwidgetsaddons-devel >= 5.30.0
BuildRequires:	kf5-kxmlgui-devel >= 5.30.0
BuildRequires:	ninja
BuildRequires:	phonon-qt5-devel
BuildRequires:	qca-qt5-devel >= 2.1.0
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KsirK is a computerized version of the well known strategic board game
Risk. The goal of the game is simply to conquer the world by attacking
your neighbors with your armies. Features. Support for 1-6 human or
computer (AI) players.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/ksirk.categories
/etc/xdg/ksirk.knsrc
%attr(755,root,root) %{_bindir}/ksirk
%attr(755,root,root) %{_bindir}/ksirkskineditor
%attr(755,root,root) %{_libdir}/libiris_ksirk.so
%attr(755,root,root) %ghost %{_libdir}/libiris_ksirk.so.2
%attr(755,root,root) %{_libdir}/libiris_ksirk.so.2.*.*
%{_desktopdir}/org.kde.ksirk.desktop
%{_desktopdir}/org.kde.ksirkskineditor.desktop
%{_datadir}/config.kcfg/ksirksettings.kcfg
%{_datadir}/config.kcfg/ksirkskineditorsettings.kcfg
%{_iconsdir}/hicolor/128x128/apps/ksirk.png
%{_iconsdir}/hicolor/16x16/apps/ksirk.png
%{_iconsdir}/hicolor/22x22/apps/ksirk.png
%{_iconsdir}/hicolor/32x32/apps/ksirk.png
%{_iconsdir}/hicolor/48x48/apps/ksirk.png
%{_iconsdir}/hicolor/64x64/apps/ksirk.png
%{_iconsdir}/hicolor/scalable/apps/ksirk.svgz
%{_datadir}/ksirk
%{_datadir}/ksirkskineditor
%dir %{_datadir}/kxmlgui5/ksirk
%{_datadir}/kxmlgui5/ksirk/ksirkui.rc
%dir %{_datadir}/kxmlgui5/ksirkskineditor
%{_datadir}/kxmlgui5/ksirkskineditor/ksirkskineditorui.rc
%{_datadir}/metainfo/org.kde.ksirk.appdata.xml
