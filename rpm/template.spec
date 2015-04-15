Name:           ros-indigo-turtlebot
Version:        2.3.11
Release:        0%{?dist}
Summary:        ROS turtlebot package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/turtlebot
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-turtlebot-bringup
Requires:       ros-indigo-turtlebot-capabilities
Requires:       ros-indigo-turtlebot-description
Requires:       ros-indigo-turtlebot-teleop
BuildRequires:  ros-indigo-catkin

%description
The turtlebot meta package provides all the basic drivers for running and using
a TurtleBot.

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
* Wed Apr 15 2015 Daniel Stonier <stonier@rnd.yujinrobot.com> - 2.3.11-0
- Autogenerated by Bloom

* Thu Apr 02 2015 Daniel Stonier <stonier@rnd.yujinrobot.com> - 2.3.10-0
- Autogenerated by Bloom

* Mon Mar 30 2015 Daniel Stonier <stonier@rnd.yujinrobot.com> - 2.3.9-0
- Autogenerated by Bloom

* Mon Mar 23 2015 Daniel Stonier <stonier@rnd.yujinrobot.com> - 2.3.8-0
- Autogenerated by Bloom

* Mon Mar 02 2015 Daniel Stonier <stonier@rnd.yujinrobot.com> - 2.3.7-0
- Autogenerated by Bloom

* Fri Feb 27 2015 Daniel Stonier <stonier@rnd.yujinrobot.com> - 2.3.6-0
- Autogenerated by Bloom

* Mon Jan 12 2015 Daniel Stonier <stonier@rnd.yujinrobot.com> - 2.3.5-0
- Autogenerated by Bloom

* Wed Jan 07 2015 Daniel Stonier <stonier@rnd.yujinrobot.com> - 2.3.4-0
- Autogenerated by Bloom

* Mon Jan 05 2015 Daniel Stonier <stonier@rnd.yujinrobot.com> - 2.3.3-0
- Autogenerated by Bloom

* Tue Dec 30 2014 Daniel Stonier <stonier@rnd.yujinrobot.com> - 2.3.2-0
- Autogenerated by Bloom

