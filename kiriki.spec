#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
Name:		kiriki
Version:	25.04.3
Release:	%{?git:0.%{git}.}1
Summary:	Yahtzee-like dice game
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		https://games.kde.org/game.php?game=kiriki
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

%rename plasma6-kiriki

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
Kiriki is an addictive and fun dice game, designed to be played by as
many as six players.

Participants have to collect points by rolling five dice for up to
three times per single turn.

%files -f %{name}.lang
%{_bindir}/kiriki
%{_datadir}/applications/org.kde.kiriki.desktop
%{_iconsdir}/hicolor/*/apps/kiriki.png
%_datadir/metainfo/org.kde.kiriki.appdata.xml
%_datadir/kiriki/images/dice-[1-6].png
%_datadir/kiriki/images/dice-none.png
