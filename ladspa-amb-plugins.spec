Summary:	AMB (Ambisonics decoder and panner) LADSPA plugins
Summary(pl.UTF-8):	Wtyczki LADSPA AMB (dekodery i pannery Ambisonics)
Name:		ladspa-amb-plugins
Version:	0.8.1
Release:	2
License:	GPL v2+
Group:		Applications/Sound
Source0:	http://kokkinizita.linuxaudio.org/linuxaudio/downloads/AMB-plugins-%{version}.tar.bz2
# Source0-md5:	496d8d2bf6036611b6b4aa7f56325a52
Patch0:		%{name}-make.patch
URL:		http://kokkinizita.linuxaudio.org/linuxaudio/ladspa/index.html
BuildRequires:	ladspa-devel
BuildRequires:	libstdc++-devel
Requires:	ladspa-common
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoprovfiles	%{_libdir}/ladspa

%description
AMB (Ambisonics surround sound decoder and panner) LADSPA plugins.

%description -l pl.UTF-8
Wtyczki LADSPA AMB (dekodery i pannery dźwięku przestrzennego
Ambisonics).

%prep
%setup -q -n AMB-plugins-%{version}
%patch -P0 -p1

%build
%{__make} \
	CXX="%{__cxx}" \
	LDFLAGS="%{rpmldflags}" \
	CPPFLAGS="-I. -fPIC -D_REENTRANT -Wall %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/ladspa

cp -p *.so $RPM_BUILD_ROOT%{_libdir}/ladspa

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/ladspa/ambisonic0.so
%attr(755,root,root) %{_libdir}/ladspa/ambisonic1.so
%attr(755,root,root) %{_libdir}/ladspa/ambisonic2.so
%attr(755,root,root) %{_libdir}/ladspa/ambisonic3.so
