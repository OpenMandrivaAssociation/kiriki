Name:		kiriki
Version:	15.08.3
Release:	1
Epoch:		1
Summary:	Yahtzee-like dice game
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://games.kde.org/game.php?game=kiriki
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5KDEGames)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(Qt5Widgets)

%description
Kiriki is an addictive and fun dice game, designed to be played by as
many as six players.

Participants have to collect points by rolling five dice for up to
three times per single turn.

%files
%{_bindir}/kiriki
%{_datadir}/applications/org.kde.kiriki.desktop
%{_iconsdir}/hicolor/*/apps/kiriki.png
%{_datadir}/kiriki
%{_datadir}/kxmlgui5/kiriki
%doc %{_docdir}/*/*/kiriki

#------------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
