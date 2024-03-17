cmake_minimum_required(VERSION 2.8.13)
project(PowerSupplyControler)

# needed for python wrapper
find_package( Python3 COMPONENTS Development REQUIRED )
find_package( Boost COMPONENTS python REQUIRED )

include_directories(${CMAKE_CURRENT_SOURCE_DIR} ${OpenCV_INCLUDE_DIRS})

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_BUILD_TYPE Release)
set(CMAKE_CXX_FLAGS "-Wall -O3")

file(GLOB SOURCES "src/*.cxx")

add_library(PowerSupplyControler SHARED ${SOURCES})
add_executable(main "utils/main.cxx")
target_link_libraries(main PowerSupplyControler Python3::Python ${Boost_LIBRARIES})

# Silence boost warnings
add_definitions(-DBOOST_BIND_GLOBAL_PLACEHOLDERS)
add_definitions(-DBOOST_ALLOW_DEPRECATED_HEADERS)


# Build the Python module
add_library( PowerSupplyModule SHARED python_wrapper/utils/PowerSupplyModule.cxx ${LIB_HEADERS} )
set_target_properties(PowerSupplyModule PROPERTIES SUFFIX ".so")
target_link_libraries( PowerSupplyModule PRIVATE Python3::Python ${Boost_LIBRARIES} PowerSupplyControler)
set_target_properties( PowerSupplyModule PROPERTIES
   PREFIX ""
   OUTPUT_NAME "PowerSupplyModule" )