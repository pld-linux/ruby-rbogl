Summary:	OpenGL module for Ruby
Summary(pl.UTF-8):	Moduł OpenGL dla Ruby
Name:		ruby-rbogl
Version:	0.32b
Release:	6
License:	GPL
Group:		Development/Languages
Source0:	http://www2.giganet.net/~yoshi/rbogl-%{version}.tgz
# Source0-md5:	94a689666a118b2ef10990183d5a308c
Patch0:		%{name}-extconf.patch
Patch1:		%{name}-cpp.patch
URL:		http://www2.giganet.net/~yoshi/
BuildRequires:	OpenGL-devel
BuildRequires:	glut-devel
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel >= 1:1.8.4-5
BuildRequires:	sed >= 4.0
Requires:	OpenGL
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1

%description
OpenGL module for Ruby.

%description -l pl.UTF-8
Moduł OpenGL dla Ruby.

%prep
%setup -q -n opengl
%patch0 -p1
%patch1 -p1
# TODO: see r1.6
sed -i -e 's#@LIBPATH@#/''usr/X11R6/%{_lib}#g#' extconf.rb

%build
ruby extconf.rb
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fPIC"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_sitearchdir},%{_examplesdir}/%{name}-%{version}}

install opengl.so $RPM_BUILD_ROOT%{ruby_sitearchdir}
install glut.so $RPM_BUILD_ROOT%{ruby_sitearchdir}
install sample/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.EUC ChangeLog
%attr(755,root,root) %{ruby_sitearchdir}/*.so
%{_examplesdir}/%{name}-%{version}
