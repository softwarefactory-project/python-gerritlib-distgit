# Python2 macros for EPEL
%if 0%{?rhel} && 0%{?rhel} <= 6
%{!?__python2: %global __python2 /usr/bin/python2}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from %distutils.sysconfig import get_python_lib; print(get_python_lib())")}

%endif

%global pypi_name gerritlib
%global desc A Python library for interacting with Gerrit

Name:           python-%{pypi_name}
Version:        0.6.0
Release:        7%{?dist}
Summary:        Client library for accessing Gerrit
License:        ASL 2.0
URL:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        https://files.pythonhosted.org/packages/source/g/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:	python2-rpm-macros
BuildRequires:  python2-setuptools
BuildRequires:  python2-pbr
BuildRequires:  python2-hacking
BuildRequires:  python2-paramiko

%description
%{desc}

%package -n python2-%{pypi_name}
Summary:        %{summary}
Requires:       python2-pbr
Requires:       python2-paramiko
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
%{desc}

%prep
%autosetup -n %{pypi_name}-%{version}
sed -i 's/\r//' LICENSE

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# We handle requirements ourselves, remove requirements.txt
rm -rf requirements.txt test-requirements.txt

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}

%check
%{__python2} setup.py test

%files -n python2-%{pypi_name}
%doc README.rst AUTHORS ChangeLog
%license LICENSE
%{python2_sitelib}/*.egg-info
%{python2_sitelib}/%{pypi_name}

%changelog
* Mon Feb 28 2017 Matthieu Huin <mhuin@redhat.com> - 0.6.0-7
- Do not use EPEL macros

* Mon Feb 27 2017 Matthieu Huin <mhuin@redhat.com> - 0.6.0-6
- Add python rpm macros

* Mon Feb 27 2017 Matthieu Huin <mhuin@redhat.com> - 0.6.0-5
- Force rebuild

* Fri Feb 24 2017 Matthieu Huin <mhuin@redhat.com> - 0.6.0-4
- Lightweight packaging for Software Factory

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-2
- Rebuild for Python 3.6

* Fri Aug 26 2016 Lumir Balhar <lbalhar@redhat.com> - 0.6.0-1
- New upstream release
- Modernized specfile
- New subpackages for each Python version

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-7
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild


* Tue Feb 25 2014 Kashyap Chamarthy <kashyapc@fedoraproject.org> - 0.3.0-3
- Add Python2 macros for EPEL

* Tue Feb 25 2014 Kashyap Chamarthy <kashyapc@fedoraproject.org> - 0.3.0-2
- Use  %{__python2} macros instead of  %{__python} (this is deprecated)

* Mon Feb 24 2014 Kashyap Chamarthy <kashyapc@fedoraproject.org> - 0.3.0-1
- Initial package
