message(STATUS "=================Start Thrift CMAKE=======================")

# Find the Thrift include directory
find_path(THRIFT_INCLUDE_DIR thrift
        PATHS /usr/include /usr/local/include
        PATH_SUFFIXES thrift
)

if (NOT THRIFT_INCLUDE_DIR)
    message(FATAL_ERROR "Thrift include directory not found. Please install Thrift or specify the correct path.")
endif()

set(THRIFT_INCLUDE_DIR /usr/include/thrift)

# Find the Thrift library
find_library(THRIFT_LIBRARY thrift
        PATHS /usr/lib /usr/local/lib /usr/lib/x86_64-linux-gnu
)

if (NOT THRIFT_LIBRARY)
    message(FATAL_ERROR "Thrift library not found. Please install Thrift or specify the correct path.")
endif()

# Ensure that the Thrift compiler is found
find_program(THRIFT_COMPILER thrift
        PATHS /usr/bin /usr/local/bin
)

if (NOT THRIFT_COMPILER)
    message(FATAL_ERROR "Thrift compiler not found. Please install Thrift or specify the correct path.")
endif()

# Source and include directories
include_directories(${THRIFT_INCLUDE_DIR} include src/thrift-generated)

# Ensure the output directory exists
file(MAKE_DIRECTORY ${CMAKE_SOURCE_DIR}/src/thrift-generated)

# Custom command to generate Thrift files during configuration
execute_process(
        COMMAND ${THRIFT_COMPILER} --gen cpp -out ${CMAKE_SOURCE_DIR}/src/thrift-generated ${CMAKE_SOURCE_DIR}/idl/thrift/soccer_service.thrift
        WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
        RESULT_VARIABLE THRIFT_GEN_RESULT
)

# Check if the Thrift generation command was successful
if (THRIFT_GEN_RESULT)
    message(FATAL_ERROR "Failed to generate Thrift files. Ensure that the Thrift compiler is correctly installed and the IDL file exists.")
endif()

message(STATUS "=================End Thrift CMAKE=======================")