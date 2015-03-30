Name:           ros-indigo-turtlebot-description
Version:        2.3.9
Release:        0%{?dist}
Summary:        ROS turtlebot_description package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/turtlebot_description
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-create-description
Requires:       ros-indigo-kobuki-description
Requires:       ros-indigo-urdf
Requires:       ros-indigo-xacro
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-urdf
BuildRequires:  ros-indigo-xacro

%description
turtlebot_description provides a complete 3D model of the TurtleBot for
simulation and visualization. The files in this package are parsed and used by a
variety of other components. Most users will not interact directly with this
package.

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
* Mon Mar 30 2015 Daniel Stonier <stonier@yujinrobot.com> - 2.3.9-0
- Autogenerated by Bloom

* Mon Mar 23 2015 Daniel Stonier <stonier@yujinrobot.com> - 2.3.8-0
- Autogenerated by Bloom

* Mon Mar 02 2015 Daniel Stonier <stonier@yujinrobot.com> - 2.3.7-0
- Autogenerated by Bloom

* Fri Feb 27 2015 Daniel Stonier <stonier@yujinrobot.com> - 2.3.6-0
- Autogenerated by Bloom

* Mon Jan 12 2015 Daniel Stonier <stonier@yujinrobot.com> - 2.3.5-0
- Autogenerated by Bloom

* Wed Jan 07 2015 Daniel Stonier <stonier@yujinrobot.com> - 2.3.4-0
- Autogenerated by Bloom

* Mon Jan 05 2015 Daniel Stonier <stonier@yujinrobot.com> - 2.3.3-0
- Autogenerated by Bloom

* Tue Dec 30 2014 Daniel Stonier <stonier@yujinrobot.com> - 2.3.2-0
- Autogenerated by Bloom

