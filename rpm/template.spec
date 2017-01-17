Name:           ros-indigo-pepper-robot
Version:        0.1.9
Release:        0%{?dist}
Summary:        ROS pepper_robot package

Group:          Development/Libraries
License:        Apache 2.0
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-pepper-bringup
Requires:       ros-indigo-pepper-description
Requires:       ros-indigo-pepper-sensors-py
BuildRequires:  ros-indigo-catkin

%description
The pepper_robot package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Tue Jan 17 2017 Karsten Knese <karsten.knese@gmail.com> - 0.1.9-0
- Autogenerated by Bloom

* Tue Aug 11 2015 Karsten Knese <karsten.knese@gmail.com> - 0.1.7-0
- Autogenerated by Bloom

* Fri Jul 31 2015 Karsten Knese <karsten.knese@gmail.com> - 0.1.6-0
- Autogenerated by Bloom

* Fri Jul 31 2015 Karsten Knese <karsten.knese@gmail.com> - 0.1.5-0
- Autogenerated by Bloom

* Thu Jul 30 2015 Karsten Knese <karsten.knese@gmail.com> - 0.1.4-0
- Autogenerated by Bloom

* Thu Jun 25 2015 Karsten Knese <kknese@aldebaran.com> - 0.1.3-0
- Autogenerated by Bloom

* Fri Apr 10 2015 Karsten Knese <kknese@aldebaran.com> - 0.1.2-0
- Autogenerated by Bloom

* Wed Apr 08 2015 Karsten Knese <kknese@aldebaran.com> - 0.1.1-0
- Autogenerated by Bloom

