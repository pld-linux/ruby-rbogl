%define pkgname rbogl
Summary:	OpenGL module for Ruby
Summary(pl.UTF-8):	Moduł OpenGL dla Ruby
Name:		ruby-%{pkgname}
Version:	0.32g
Release:	7
License:	GPL
Group:		Development/Languages
Source0:	http://www2.giganet.net/~yoshi/%{pkgname}-%{version}.tar.gz
# Source0-md5:	0832d08a87ebb16f6d4e30459a5019f0
Patch0:		%{name}-ruby1.9.patch
URL:		http://www2.giganet.net/~yoshi/
BuildRequires:	OpenGL-devel
BuildRequires:	OpenGL-glut-devel
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
BuildRequires:	ruby-devel >= 1:1.8.6
BuildRequires:	ruby-modules
BuildRequires:	sed >= 4.0
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	xorg-lib-libXmu-devel
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1

%description
OpenGL module for Ruby.

%description -l pl.UTF-8
Moduł OpenGL dla Ruby.

%prep
%setup -q -n opengl-%{version}
%patch0 -p1

%build
%{__ruby} extconf.rb \
	--vendor

%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fPIC"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a sample/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.EUC ChangeLog
%attr(755,root,root) %{ruby_vendorarchdir}/glut.so
%attr(755,root,root) %{ruby_vendorarchdir}/opengl.so
%{_examplesdir}/%{name}-%{version}
