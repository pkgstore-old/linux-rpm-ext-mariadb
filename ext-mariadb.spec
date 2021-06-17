%global app                     mysql
%global user                    %{app}
%global group                   %{app}

%global d_home                  /home
%global d_storage               %{d_home}/storage.01
%global d_data                  %{d_storage}/data.02

%global d_cnf                   %{_sysconfdir}/my.cnf.d
%global d_service               %{_sysconfdir}/systemd/system/mariadb.service.d

%global release_prefix          100

Name:                           ext-mariadb
Version:                        1.0.3
Release:                        %{release_prefix}%{?dist}
Summary:                        META-package for install and configure MariaDB
License:                        MIT

Source10:                       my.cnf
Source20:                       service.homedir.conf
Source21:                       service.limits.conf

Requires:                       MariaDB-server MariaDB-client

%description
META-package for install and configure MariaDB.

# -------------------------------------------------------------------------------------------------------------------- #
# -----------------------------------------------------< SCRIPT >----------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

%prep


%install
%{__rm} -rf %{buildroot}

%{__install} -dp -m 0755 %{buildroot}%{d_data}/%{app}

%{__install} -Dp -m 0644 %{SOURCE10} \
  %{buildroot}%{d_cnf}/custom.my.cnf
%{__install} -Dp -m 0644 %{SOURCE20} \
  %{buildroot}%{d_service}/custom.homedir.conf
%{__install} -Dp -m 0644 %{SOURCE21} \
  %{buildroot}%{d_service}/custom.limits.conf


%files
%attr(0700,%{user},%{group}) %dir %{d_data}/%{app}
%config %{d_cnf}/custom.my.cnf
%config %{d_service}/custom.homedir.conf
%config %{d_service}/custom.limits.conf


%changelog
* Thu Jun 17 2021 Package Store <kitsune.solar@gmail.com> - 1.0.3-100
- UPD: Move to GitHub.
- UPD: License.

* Tue Nov 12 2019 Package Store <kitsune.solar@gmail.com> - 1.0.2-100
- UPD: Directory names.

* Sun Jul 28 2019 Package Store <kitsune.solar@gmail.com> - 1.0.1-101
- UPD: SPEC-file.

* Wed Jul 10 2019 Package Store <kitsune.solar@gmail.com> - 1.0.1-100
- UPD: MariaDB config.
- NEW: SystemD config.

* Wed Jul 10 2019 Package Store <kitsune.solar@gmail.com> - 1.0.0-114
- UPD: MariaDB config.

* Wed Jul 10 2019 Package Store <kitsune.solar@gmail.com> - 1.0.0-113
- UPD: MariaDB config.

* Wed Jul 10 2019 Package Store <kitsune.solar@gmail.com> - 1.0.0-112
- UPD: MariaDB config.

* Sat Jul 06 2019 Package Store <kitsune.solar@gmail.com> - 1.0.0-111
- UPD: MariaDB config.

* Fri Jul 05 2019 Package Store <kitsune.solar@gmail.com> - 1.0.0-110
- UPD: MariaDB config.

* Fri Jul 05 2019 Package Store <kitsune.solar@gmail.com> - 1.0.0-109
- UPD: SPEC-file.

* Tue Jul 02 2019 Package Store <kitsune.solar@gmail.com> - 1.0.0-108
- UPD: DB directory.

* Tue Jul 02 2019 Package Store <kitsune.solar@gmail.com> - 1.0.0-107
- UPD: SPEC-file.

* Mon Jul 01 2019 Package Store <kitsune.solar@gmail.com> - 1.0.0-106
- UPD: MariaDB config.

* Fri Apr 19 2019 Package Store <kitsune.solar@gmail.com> - 1.0.0-105
- UPD: Directory structure.

* Sun Apr 14 2019 Package Store <kitsune.solar@gmail.com> - 1.0.0-104
- UPD: Directory structure.

* Sat Apr 13 2019 Package Store <kitsune.solar@gmail.com> - 1.0.0-103
- NEW: 1.0.0-103.

* Wed Apr 10 2019 Package Store <kitsune.solar@gmail.com> - 1.0.0-102
- NEW: 1.0.0-102.

* Sat Mar 30 2019 Package Store <kitsune.solar@gmail.com> - 1.0.0-101
- NEW: 1.0.0-101.

* Wed Jan 02 2019 Package Store <kitsune.solar@gmail.com> - 1.0.0-100
- Initial build.
