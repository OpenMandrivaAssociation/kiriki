#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
Name:		plasma6-kiriki
Version:	24.08.1
Release:	%{?git:0.%{git}.}1
Summary:	Yahtzee-like dice game
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://games.kde.org/game.php?game=kiriki
%if 0%{?git:1}
Source0:	https://invent.kde.org/games/kiriki/-/archive/%{gitbranch}/kiriki-%{gitbranchd}.tar.bz2#/kiriki-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kiriki-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KDEGames6)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6PrintSupport)

%description
Kiriki is an addictive and fun dice game, designed to be played by as
many as six players.

Participants have to collect points by rolling five dice for up to
three times per single turn.

%files -f kiriki.lang
%{_bindir}/kiriki
%{_datadir}/applications/org.kde.kiriki.desktop
%{_iconsdir}/hicolor/*/apps/kiriki.png
%_datadir/metainfo/org.kde.kiriki.appdata.xml
%_datadir/kiriki/images/dice-[1-6].png
%_datadir/kiriki/images/dice-none.png

#------------------------------------------------------------------------------

%prep
%autosetup -p1 -n kiriki-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang kiriki --with-html
