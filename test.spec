Name: test
Version: 1
Release: 1%{?dist}
Summary: Test
# Public Domain
# https://spdx.org/licenses/
License: CC-PDDC
URL: https://github.com/junaruga/
# This value is replaced with the tar.gz file created from `git archive` by CI.
Source0: dummy

# List up the RPM package names needed to test here.
# gcc
BuildRequires: gcc
# g++
BuildRequires: gcc-c++
# clang, clang++
BuildRequires: clang
# make
BuildRequires: make

%description

%prep
# Print Source0.
echo "Source0: %{SOURCE0}"
# Create a dummy file for the valid RPM spec file.
touch dummy.txt

%check
echo "== Check section =="
tar xzvf %{SOURCE0}

pushd test-*
make test
popd

%files
%doc dummy.txt

%changelog
* Fri Jun 02 2023 Jun Aruga <jaruga@redhat.com> - 1-1
- Dummy.
