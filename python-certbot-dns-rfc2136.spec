%global pyname certbot-dns-rfc2136

# On fedora use python3 for certbot
%if 0%{?fedora}
%bcond_without python3
%else
%bcond_with python3
%endif

Name:       python-%{pyname}
Version:    0.18.1
Release:    1%{?dist}
Summary:    The DNS plugin for certbot using RFC2136 dynamic updates

License:    ASL 2.0
URL:        https://pypi.python.org/pypi/certbot-dns-rfc2136
Source0:    https://files.pythonhosted.org/packages/source/c/%{pyname}/%{pyname}-%{version}.tar.gz

Patch0:         allow-old-setuptools.patch

BuildArch:      noarch

BuildRequires: python2-devel

%if %{with python3}
BuildRequires:  python3-devel
%endif

#For running tests
BuildRequires: python2-certbot = %{version}
BuildRequires: python-dns

%if %{with python3}
BuildRequires: python3-certbot = %{version}
BuildRequires: python3-dns
%endif

%description
Plugin for certbot that uses DNS via RFC2136 dynamic updates for verification

%package -n python2-%{pyname}
# Provide the name users expect as a certbot plugin
Provides:      %{pyname} = %{version}-%{release}
# Although a plugin for the certbot command it's technically
# an extension to the certbot python libraries
Requires:      python2-certbot = %{version}
Requires:      python-dns
%if 0%{?fedora}
#Recommend the CLI as that will be the interface most use
Recommends:    certbot = %{version}
%else
Requires:      certbot = %{version}
%endif
Summary:     The DNS plugin for certbot using RFC2136 dynamic updates
%{?python_provide:%python_provide python2-%{pyname}}

%description -n python2-%{pyname}
Plugin for certbot that uses DNS via RFC2136 dynamic updates for verification

%if %{with python3}
%package -n python3-%{pyname}
# Provide the name users expect as a certbot plugin
Provides:      %{pyname} = %{version}-%{release}
# Although a plugin for the certbot command it's technically
# an extension to the certbot python libraries
Requires:      python3-certbot = %{version}
Requires:      python3-dns
%if 0%{?fedora}
#Recommend the CLI as that will be the interface most use
Recommends:    certbot = %{version}
%else
Requires:      certbot = %{version}
%endif
Summary:     The DNS plugin for certbot using RFC2136 dynamic updates
%{?python_provide:%python_provide python3-%{pyname}}

%description -n python3-%{pyname}
Plugin for certbot that uses DNS via RFC2136 dynamic updates for verification
%endif

%prep
%setup -n %{pyname}-%{version}
%if 0%{?rhel}
%patch0 -p1
%endif

%build
%{py2_build}
%if %{with python3}
%py3_build
%endif

%check
%{__python2} setup.py test
%if %{with python3}
%{__python3} setup.py test
%endif


%install
%{py2_install}
%if %{with python3}
%py3_install
%endif

%files -n python2-%{pyname}
%license LICENSE.txt
%doc README.rst
%{python2_sitelib}/certbot_dns_rfc2136
%{python2_sitelib}/certbot_dns_rfc2136-%{version}*.egg-info

%if %{with python3}
%files -n python3-%{pyname}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/certbot_dns_rfc2136
%{python3_sitelib}/certbot_dns_rfc2136-%{version}*.egg-info
%endif

%changelog
* Mon Sep 18 2017 Matt Dainty <matt@bodgit-n-scarper.com> - 0.18.1-1
- Initial package
