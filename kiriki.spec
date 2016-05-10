Name:		kiriki
Version:	16.04.0
Release:	1
Epoch:		1
Summary:	Yahtzee-like dice game
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://games.kde.org/game.php?game=kiriki
Source:		http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
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
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5Crash)

%description
Kiriki is an addictive and fun dice game, designed to be played by as
many as six players.

Participants have to collect points by rolling five dice for up to
three times per single turn.

%files
%{_bindir}/kiriki
%{_datadir}/applications/org.kde.kiriki.desktop
%{_iconsdir}/hicolor/*/apps/kiriki.png
%_kde5_datadir/appdata/org.kde.kiriki.appdata.xml
%_kde5_xmlguidir/kiriki/kirikiui.rc
%_kde5_datadir/kiriki/images/dice-1.png
%_kde5_datadir/kiriki/images/dice-2.png
%_kde5_datadir/kiriki/images/dice-3.png
%_kde5_datadir/kiriki/images/dice-4.png
%_kde5_datadir/kiriki/images/dice-5.png
%_kde5_datadir/kiriki/images/dice-6.png
%_kde5_datadir/kiriki/images/dice-none.png
%doc %{_docdir}/*/*/kiriki

#------------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
