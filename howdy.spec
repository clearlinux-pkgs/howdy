#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: make
# autospec version: v4
# autospec commit: 1ab68caa3dd3
#
Name     : howdy
Version  : 2.6.1
Release  : 5
URL      : https://github.com/boltgolt/howdy/archive/v2.6.1/howdy-2.6.1.tar.gz
Source0  : https://github.com/boltgolt/howdy/archive/v2.6.1/howdy-2.6.1.tar.gz
Source1  : https://github.com/davisking/dlib-models/raw/master/dlib_face_recognition_resnet_model_v1.dat.bz2
Source2  : https://github.com/davisking/dlib-models/raw/master/mmod_human_face_detector.dat.bz2
Source3  : https://github.com/davisking/dlib-models/raw/master/shape_predictor_5_face_landmarks.dat.bz2
Summary  : Windows Hello™ style authentication for Linux
Group    : Development/Tools
License  : MIT
Requires: howdy-bin = %{version}-%{release}
Requires: howdy-data = %{version}-%{release}
Requires: howdy-license = %{version}-%{release}
Requires: dlib
Requires: pam-python
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: stateless.patch

%description
Windows Hello™ style authentication for Linux. Use your built-in IR emitters and camera in combination with face recognition to prove who you are.

%package bin
Summary: bin components for the howdy package.
Group: Binaries
Requires: howdy-data = %{version}-%{release}
Requires: howdy-license = %{version}-%{release}

%description bin
bin components for the howdy package.


%package data
Summary: data components for the howdy package.
Group: Data

%description data
data components for the howdy package.


%package license
Summary: license components for the howdy package.
Group: Default

%description license
license components for the howdy package.


%prep
%setup -q -n howdy-2.6.1
cd %{_builddir}
mkdir -p dlib_face_recognition_resnet_model_v1.dat
cd dlib_face_recognition_resnet_model_v1.dat
bzcat %{_sourcedir}/dlib_face_recognition_resnet_model_v1.dat.bz2 > $(basename "%{_sourcedir}/dlib_face_recognition_resnet_model_v1.dat.bz2" .bz2)
cd %{_builddir}
mkdir -p mmod_human_face_detector.dat
cd mmod_human_face_detector.dat
bzcat %{_sourcedir}/mmod_human_face_detector.dat.bz2 > $(basename "%{_sourcedir}/mmod_human_face_detector.dat.bz2" .bz2)
cd %{_builddir}
mkdir -p shape_predictor_5_face_landmarks.dat
cd shape_predictor_5_face_landmarks.dat
bzcat %{_sourcedir}/shape_predictor_5_face_landmarks.dat.bz2 > $(basename "%{_sourcedir}/shape_predictor_5_face_landmarks.dat.bz2" .bz2)
cd %{_builddir}/howdy-2.6.1
mkdir -p src/dlib-data
cp -r %{_builddir}/dlib_face_recognition_resnet_model_v1.dat/* %{_builddir}/howdy-2.6.1/src/dlib-data
mkdir -p src/dlib-data
cp -r %{_builddir}/mmod_human_face_detector.dat/* %{_builddir}/howdy-2.6.1/src/dlib-data
mkdir -p src/dlib-data
cp -r %{_builddir}/shape_predictor_5_face_landmarks.dat/* %{_builddir}/howdy-2.6.1/src/dlib-data
%patch -P 1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1709859329
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
make  %{?_smp_mflags}  ||:


%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1709859329
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/howdy
cp %{_builddir}/howdy-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/howdy/5acdde412debe91775066e8e79b5086b1c7d15d3 || :
cp %{_builddir}/howdy-%{version}/debian/copyright %{buildroot}/usr/share/package-licenses/howdy/5acdde412debe91775066e8e79b5086b1c7d15d3 || :
export GOAMD64=v2
GOAMD64=v2
%make_install ||:
## install_append content
mkdir -p %{buildroot}%{_libdir}/security/%{name}

# Remove backup file
rm -rf src/*~

# Move reference config
mkdir -p %{buildroot}/usr/share/howdy
mv src/config.ini %{buildroot}/usr/share/howdy/

# Install base files
cp -pr src/* %{buildroot}%{_libdir}/security/%{name}

# Install facial recognition
mkdir -p %{buildroot}%{_libdir}/security/%{name}/dlib-data
cp -p src/dlib-data/*.dat %{buildroot}%{_libdir}/security/%{name}/dlib-data
rm -fr %{buildroot}%{_libdir}/security/%{name}/dlib-data/{Readme.md,install.sh,.gitignore}

# Add polkit rules
mkdir -p %{buildroot}%{_datadir}/polkit-1/actions
install -Dm 0644 fedora/*.policy %{buildroot}%{_datadir}/polkit-1/actions/

# Add bash completion
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
install -Dm 644 autocomplete/%{name} %{buildroot}%{_datadir}/bash-completion/completions

# Create an executable
mkdir -p %{buildroot}%{_bindir}
chmod +x %{buildroot}%{_libdir}/security/%{name}/cli.py
ln -s %{_libdir}/security/%{name}/cli.py %{buildroot}%{_bindir}/%{name}
## install_append end

%files
%defattr(-,root,root,-)
/usr/lib64/security/howdy/cli.py
/usr/lib64/security/howdy/cli/__init__.py
/usr/lib64/security/howdy/cli/add.py
/usr/lib64/security/howdy/cli/clear.py
/usr/lib64/security/howdy/cli/config.py
/usr/lib64/security/howdy/cli/disable.py
/usr/lib64/security/howdy/cli/list.py
/usr/lib64/security/howdy/cli/remove.py
/usr/lib64/security/howdy/cli/snap.py
/usr/lib64/security/howdy/cli/test.py
/usr/lib64/security/howdy/compare.py
/usr/lib64/security/howdy/dlib-data/dlib_face_recognition_resnet_model_v1.dat
/usr/lib64/security/howdy/dlib-data/mmod_human_face_detector.dat
/usr/lib64/security/howdy/dlib-data/shape_predictor_5_face_landmarks.dat
/usr/lib64/security/howdy/logo.png
/usr/lib64/security/howdy/pam-config/howdy
/usr/lib64/security/howdy/pam.py
/usr/lib64/security/howdy/recorders/__init__.py
/usr/lib64/security/howdy/recorders/ffmpeg_reader.py
/usr/lib64/security/howdy/recorders/pyv4l2_reader.py
/usr/lib64/security/howdy/recorders/v4l2.py
/usr/lib64/security/howdy/recorders/video_capture.py
/usr/lib64/security/howdy/snapshot.py

%files bin
%defattr(-,root,root,-)
/usr/bin/howdy

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/howdy
/usr/share/howdy/config.ini
/usr/share/polkit-1/actions/com.github.boltgolt.howdy.policy

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/howdy/5acdde412debe91775066e8e79b5086b1c7d15d3
