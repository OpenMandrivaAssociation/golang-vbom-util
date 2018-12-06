# Run tests in check section
%bcond_without check

%global goipath         vbom.ml/util
%global forgeurl        https://github.com/fvbommel/util
%global commit          256737ac55c46798123f754ab7d2c784e2c71783
%global common_description %{expand:
Sort orders, comparison functions, and "heavy-weight string" utilities in Go
(Golang).}

Version:        0

%gometa

Name:           %{goname}
Release:        0.1%{?dist}
Summary:        Sort orders, comparison functions, and "heavy-weight string" utilities
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/bruth/assert)
BuildRequires:  golang(github.com/xlab/handysort)

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%forgesetup

%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md

%changelog
* Mon Aug 13 2018 Gabe <redhatrises@gmail.com> - 0-0.1.20180813git256737a
- First package for Fedora
