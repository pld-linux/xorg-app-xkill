Summary:	xkill application to kill a client by its X resource
Summary(pl.UTF-8):	Aplikacja xkill do zabijania klientów poprzez ich zasoby X
Name:		xorg-app-xkill
Version:	1.0.6
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	https://xorg.freedesktop.org/releases/individual/app/xkill-%{version}.tar.xz
# Source0-md5:	f62b99839249ce9a7a8bb71a5bab6f9d
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
# just xmuu
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-proto-xproto-devel >= 7.0.22
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xkill is a utility for forcing the X server to close connections to
clients. This program is very dangerous, but is useful for aborting
programs that have displayed undesired windows on a user's screen.

%description -l pl.UTF-8
Aplikacja xkill to narzędzie zmuszające serwer X do zamknięcia
połączeń z klientami. Ten program jest bardzo niebezpieczny, ale
przydatny do przerywania programów, które wyświetliły niepożądane
okienka na ekranie użytkownika.

%prep
%setup -q -n xkill-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README.md
%attr(755,root,root) %{_bindir}/xkill
%{_mandir}/man1/xkill.1*
