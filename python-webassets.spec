%global mod_name webassets

Name:           python-webassets
Version:        0.7.1
Release:        2
Summary:        Media asset management for python
Group:          Development/Python
License:        BSD
URL:            http://github.com/miracle2k/%{mod_name}
# Because jsmin.py is non-free, we have to make a "clean" source tarball.
# First, get the original source:
# Source0:      http://pypi.python.org/packages/source/w/%{mod_name}/%{mod_name}-%{version}.tar.gz
# Then, unpack it, and delete src/webassets/filter/jsmin/jsmin.py
# tar xf %{mod_name}-%{version}.tar.gz
# rm -rf %{mod_name}-%{version}/src/webassets/filter/jsmin/jsmin.py
# tar cfz %{mod_name}-%{version}-clean.tar.gz %{mod_name}-%{version}
Source0:        %{mod_name}-%{version}-clean.tar.gz
BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-setuptools

%description
Merges, minifies and compresses Javascript and CSS files, 
supporting a variety of different filters, including YUI, 
jsmin, jspacker or CSS tidy. Also supports URL rewriting in CSS files.

%prep
%setup -q -n %{mod_name}-%{version}
sed -i "s|\r||g" README.rst
sed -i "s|\r||g" docs/index.rst
sed -i "s|\r||g" docs/conf.py
sed -i "s|\r||g" docs/builtin_filters.rst
sed -i "s|\r||g" docs/Makefile
sed -i "s|\r||g" docs/make.bat
sed -i "s|\r||g" docs/django/jinja2.rst
sed -i "s|\r||g" docs/faq.rst
# sed -i -e '/^#!\//, 1d' src/webassets/filter/jsmin/jsmin.py

rm -f src/django_assets/models.py

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
sed -i -e '/^#!\//, 1d' $RPM_BUILD_ROOT%{python_sitelib}/%{mod_name}/filter/rjsmin/rjsmin.py
 
%files
%doc docs/ README.rst CHANGES LICENSE PKG-INFO
%{_bindir}/%{mod_name}
%{python_sitelib}/django_assets/
%{python_sitelib}/*.egg-info/
%{python_sitelib}/%{mod_name}/

%changelog
* Mon Dec 17 2012 Paulo Andrade <pcpa@mandriva.com.br> - 0.7.1-1
- Import python-webassets.

* Wed Aug  8 2012 Tom Callaway <spot@fedoraproject.org> - 0.7.1-1
- 0.7.1 (cleaned out jsmin.py)

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat May 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-1
- New release

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 21 2011 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> - 0.5-1
- Initial RPM release
