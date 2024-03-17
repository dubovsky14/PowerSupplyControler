cmake_minimum_required(VERSION 2.8.13)
project(PowerSupplyControler)

# needed for python wrapper
find_package( Python3 COMPONENTS Development REQUIRED )

include_directories(${CMAKE_CURRENT_SOURCE_DIR} ${OpenCV_INCLUDE_DIRS})

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_BUILD_TYPE Release)
set(CMAKE_CXX_FLAGS "-Wall -O3")

file(GLOB SOURCES "src/*.cxx")

add_library(PowerSupplyControler SHARED ${SOURCES})
add_executable(main "utils/main.cxx")
target_link_libraries(main PowerSupplyControler)
