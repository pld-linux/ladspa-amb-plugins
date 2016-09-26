Summary:	AMB (Ambisonics decoder and panner) LADSPA plugins
Summary(pl.UTF-8):	Wtyczki LADSPA AMB (dekodery i pannery Ambisonics)
Name:		ladspa-amb-plugins
Version:	0.1.0
Release:	1
License:	GPL v2+
Group:		Applications/Sound
#Source0Download: http://users.skynet.be/solaris/linuxaudio/getit.html
Source0:	http://users.skynet.be/solaris/linuxaudio/downloads/AMB-plugins-%{version}.tar.bz2
# Source0-md5:	88db5ecbe29e0fd75145e7e3beac69d1
Patch0:		%{name}-make.patch
URL:		http://users.skynet.be/solaris/linuxaudio/
BuildRequires:	ladspa-devel
BuildRequires:	libstdc++-devel
Requires:	ladspa-common
Obsoletes:	ladspa-mcp-plugins-alsa-modular-synth-examples
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AMB (Ambisonics surround sound decoder and panner) LADSPA plugins.

%description -l pl.UTF-8
Wtyczki LADSPA AMB (dekodery i pannery dźwięku przestrzennego
Ambisonics).

%prep
%setup -q -n AMB-plugins-%{version}
%patch0 -p1

%build
%{__make} \
	CXX="%{__cxx}" \
	CPPFLAGS="-I. -fPIC -D_REENTRANT -Wall %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/ladspa

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALL_PLUGINS_DIR=%{_libdir}/ladspa

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/ladspa/ambis1.so
%attr(755,root,root) %{_libdir}/ladspa/ambis2.so
