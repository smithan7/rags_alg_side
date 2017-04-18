cmake_minimum_required(VERSION 2.8.3)
project(rags_alg_side)

catkin_package()

include_directories(
  ${catkin_INCLUDE_DIRS}
)

catkin_install_python(PROGRAMS script/rags_alg_side.py
					DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
## Mark cpp header files for installation

install(DIRECTORY launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/launch
)

