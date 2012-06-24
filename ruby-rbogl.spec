%define	ruby_sitearchdir	%(ruby -r rbconfig -e 'print Config::CONFIG["sitearchdir"]')
Summary:	OpenGL module for Ruby
Summary(pl):	Modu� OpenGL dla Ruby
Name:		ruby-rbogl
Version:	0.32b
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://www2.giganet.net/~yoshi/rbogl-%{version}.tgz
# Source0-md5:	94a689666a118b2ef10990183d5a308c
Patch0:	%{name}-extconf.patch
Patch1:	%{name}-cpp.patch
URL:		http://www2.giganet.net/~yoshi/
BuildRequires:	XFree86-OpenGL-devel
BuildRequires:	XFree86-OpenGL-core
BuildRequires:	ruby
Requires:	ruby
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenGL module for Ruby.

%description -l pl
Modu� OpenGL dla Ruby

%prep
%setup -q -n opengl
%patch0 -p1
%patch1 -p1

%build
# not autoconf-generated
ruby extconf.rb
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fPIC"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_sitearchdir},%{_examplesdir}/%{name}}

install opengl.so $RPM_BUILD_ROOT%{ruby_sitearchdir}
install glut.so $RPM_BUILD_ROOT%{ruby_sitearchdir}
install sample/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.EUC ChangeLog
%attr(755,root,root) %{ruby_sitearchdir}/*.so
%{_examplesdir}/*
