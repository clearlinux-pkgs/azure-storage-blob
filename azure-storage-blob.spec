#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : azure-storage-blob
Version  : 12.6.0
Release  : 9
URL      : https://files.pythonhosted.org/packages/36/21/17828253012587b3396917349380f68591a760214d2ce1b30ae3933d448e/azure-storage-blob-12.6.0.zip
Source0  : https://files.pythonhosted.org/packages/36/21/17828253012587b3396917349380f68591a760214d2ce1b30ae3933d448e/azure-storage-blob-12.6.0.zip
Summary  : Microsoft Azure Blob Storage Client Library for Python
Group    : Development/Tools
License  : MIT
Requires: azure-storage-blob-license = %{version}-%{release}
Requires: azure-storage-blob-python = %{version}-%{release}
Requires: azure-storage-blob-python3 = %{version}-%{release}
Requires: azure-core
Requires: cryptography
Requires: msrest
BuildRequires : azure-core
BuildRequires : buildreq-distutils3
BuildRequires : cryptography
BuildRequires : msrest

%description
Azure Blob storage is Microsoft's object storage solution for the cloud. Blob storage is optimized for storing massive amounts of unstructured data, such as text or binary data.

%package license
Summary: license components for the azure-storage-blob package.
Group: Default

%description license
license components for the azure-storage-blob package.


%package python
Summary: python components for the azure-storage-blob package.
Group: Default
Requires: azure-storage-blob-python3 = %{version}-%{release}

%description python
python components for the azure-storage-blob package.


%package python3
Summary: python3 components for the azure-storage-blob package.
Group: Default
Requires: python3-core
Provides: pypi(azure_storage_blob)
Requires: pypi(azure_core)
Requires: pypi(cryptography)
Requires: pypi(msrest)

%description python3
python3 components for the azure-storage-blob package.


%prep
%setup -q -n azure-storage-blob-12.6.0
cd %{_builddir}/azure-storage-blob-12.6.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1608048262
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/azure-storage-blob
cp %{_builddir}/azure-storage-blob-12.6.0/LICENSE.txt %{buildroot}/usr/share/package-licenses/azure-storage-blob/db7376318a1c27e5890f668a05d8ac5f68048007
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/azure-storage-blob/db7376318a1c27e5890f668a05d8ac5f68048007

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
