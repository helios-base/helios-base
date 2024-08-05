cmake_minimum_required(VERSION 3.8)

project(helios-base VERSION 2023.03)

if(CMAKE_VERSION VERSION_LESS "3.7.0")
    set(CMAKE_INCLUDE_CURRENT_DIR ON)
endif()

# compliler options
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

if(NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE "Release" CACHE STRING "" FORCE)
endif()
set(CMAKE_CXX_FLAGS "-W -Wall")

# Thrift paths
set(THRIFT_INCLUDE_DIR /usr/include/thrift)
set(THRIFT_LIBRARY /usr/lib/x86_64-linux-gnu/libthrift.so)
set(THRIFT_COMPILER /usr/bin/thrift)

# GRPC
# list(APPEND CMAKE_PREFIX_PATH "${GRPC_LIB_PATH}")
# set(LIBRARY_PATH "${GRPC_LIB_PATH}/lib")
# link_directories(${LIBRARY_PATH})
#find_package(absl CONFIG REQUIRED)
#find_package(Protobuf CONFIG REQUIRED)
#find_package(gRPC CONFIG REQUIRED)
# set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -I${Protobuf_INCLUDE_DIRS}")
# set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -I${gRPC_INCLUDE_DIRS}")
# set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -I${absl_INCLUDE_DIRS}")
# set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -I${GRPC_LIB_PATH}/include")
# set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -L${GRPC_LIB_PATH}/lib")
#set(_GRPC_GRPCPP gRPC::grpc++)

# check librcsc
set(LIBRCSC_INSTALL_DIR "$ENV{HOME}/.local;$ENV{HOME}/local" CACHE PATH "The path where librcsc is installed.")

find_library(LIBRCSC_LIB NAMES rcsc
  PATHS ${LIBRCSC_INSTALL_DIR}
  PATH_SUFFIXES lib
  )
if(NOT LIBRCSC_LIB)
  message(FATAL_ERROR "librcsc library not found!")
endif()
get_filename_component(LIBRCSC_LIBDIR ${LIBRCSC_LIB} DIRECTORY)

find_path(LIBRCSC_INCLUDE_DIR
  NAME rcsc/types.h
  PATHS ${LIBRCSC_INSTALL_DIR}
  PATH_SUFFIXES include
  )
if(NOT LIBRCSC_INCLUDE_DIR)
  message(FATAL_ERROR "librcsc include dir not found!")
endif()

# remove variables from GUI
mark_as_advanced(
  LIBRCSC_LIB
  LIBRCSC_INCLUDE_DIR
  LIBRCSC_LIBDIR
  )

# boost
find_package(Boost 1.36.0 COMPONENTS system REQUIRED)
if(NOT Boost_FOUND)
  message(FATAL_ERROR "Boost not found!")
endif()

# zlib
find_package(ZLIB)
if(ZLIB_FOUND)
  set(HAVE_LIBZ TRUE)
endif()

# generate config.h
add_definitions(-DHAVE_CONFIG_H)
configure_file(
  ${PROJECT_SOURCE_DIR}/cmake-config.h.in
  ${PROJECT_BINARY_DIR}/config.h
  )

# thread
find_package(Threads REQUIRED)

# check the settings
message(STATUS "Found librcsc:")
message(STATUS "  LIBRCSC_LIBDIR=${LIBRCSC_LIBDIR}")
message(STATUS "  LIBRCSC_LIB=${LIBRCSC_LIB}")
message(STATUS "  LIBRCSC_INCLUDE_DIR=${LIBRCSC_INCLUDE_DIR}")
message(STATUS "Build settings:")
message(STATUS "  BUILD_TYPE=${CMAKE_BUILD_TYPE}")

# Source and include directories
include_directories(${THRIFT_INCLUDE_DIR} include src/thrift)

# Custom command to generate Thrift files during configuration
execute_process(
        COMMAND ${THRIFT_COMPILER} --gen cpp -out ${CMAKE_SOURCE_DIR}/src/thrift ${CMAKE_SOURCE_DIR}/idl/soccer_service.thrift
        WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
        RESULT_VARIABLE THRIFT_GEN_RESULT
)

# sub directories
#add_subdirectory(grpc)
add_subdirectory(src)

#include_directories("${GRPC_LIB_PATH}/include/google/protobuf")
#add_definitions("${GRPC_LIB_PATH}/include/google/protobuf")