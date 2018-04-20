# Script generated with Bloom
pkgdesc="ROS - turtlebot_bringup provides roslaunch scripts for starting the TurtleBot base functionality."
url='http://ros.org/wiki/turtlebot_bringup'

pkgname='ros-kinetic-turtlebot-bringup'
pkgver='2.4.2_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
)

depends=('ros-kinetic-astra-launch'
'ros-kinetic-create-node'
'ros-kinetic-depthimage-to-laserscan'
'ros-kinetic-diagnostic-aggregator'
'ros-kinetic-freenect-launch'
'ros-kinetic-kobuki-bumper2pc'
'ros-kinetic-kobuki-capabilities'
'ros-kinetic-kobuki-node'
'ros-kinetic-kobuki-safety-controller'
'ros-kinetic-laptop-battery-monitor'
'ros-kinetic-openni2-launch'
'ros-kinetic-realsense-camera'
'ros-kinetic-robot-pose-ekf'
'ros-kinetic-robot-state-publisher'
'ros-kinetic-rocon-app-manager'
'ros-kinetic-rocon-bubble-icons'
'ros-kinetic-turtlebot-capabilities'
'ros-kinetic-turtlebot-description'
'ros-kinetic-yocs-cmd-vel-mux'
'ros-kinetic-zeroconf-avahi'
)

conflicts=()
replaces=()

_dir=turtlebot_bringup
source=()
md5sums=()

prepare() {
    cp -R $startdir/turtlebot_bringup $srcdir/turtlebot_bringup
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

