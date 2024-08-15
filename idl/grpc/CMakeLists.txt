message(STATUS "=================Start gRPC CMAKE=======================")

# Set the output directory for generated files
set(GRPC_OUTPUT_DIR "${CMAKE_SOURCE_DIR}/src/grpc-generated")
file(MAKE_DIRECTORY ${GRPC_OUTPUT_DIR})

# Define the .proto file and its path
set(PROTO_FILE "service.proto")
set(PROTO_PATH "${CMAKE_CURRENT_SOURCE_DIR}")

# Locate the protoc executable
find_program(PROTOBUF_PROTOC_EXECUTABLE protoc)
if(NOT PROTOBUF_PROTOC_EXECUTABLE)
    message(FATAL_ERROR "Protoc not found. Please make sure it is installed and in the system PATH.")
endif()

# Locate the gRPC C++ plugin executable
find_program(GRPC_CPP_PLUGIN grpc_cpp_plugin $ENV{HOME}/.local/bin)
if (NOT GRPC_CPP_PLUGIN)
    message(FATAL_ERROR "grpc_cpp_plugin not found. Please make sure it is installed and in the system PATH.")
endif()

# Output the status of variables
message(STATUS "GRPC_OUTPUT_DIR: ${GRPC_OUTPUT_DIR}")
message(STATUS "PROTO_FILE: ${PROTO_FILE}")
message(STATUS "PROTO_PATH: ${PROTO_PATH}")
message(STATUS "Protoc executable used by CMake: ${PROTOBUF_PROTOC_EXECUTABLE}")
message(STATUS "gRPC C++ plugin: ${GRPC_CPP_PLUGIN}")

# Output the command that will be executed
message(STATUS "Command: ${PROTOBUF_PROTOC_EXECUTABLE} "
        "--grpc_out=${GRPC_OUTPUT_DIR} "
        "--cpp_out=${GRPC_OUTPUT_DIR} "
        "--plugin=protoc-gen-grpc=${GRPC_CPP_PLUGIN} "
        "--proto_path=${PROTO_PATH} "
        "${PROTO_FILE}")

# Run protoc during the CMake configuration phase
execute_process(
        COMMAND ${PROTOBUF_PROTOC_EXECUTABLE}
        --grpc_out=${GRPC_OUTPUT_DIR}
        --cpp_out=${GRPC_OUTPUT_DIR}
        --plugin=protoc-gen-grpc=${GRPC_CPP_PLUGIN}
        --proto_path=${PROTO_PATH}
        ${PROTO_FILE}
        RESULT_VARIABLE PROTOC_RESULT
        OUTPUT_VARIABLE PROTOC_OUTPUT
        ERROR_VARIABLE PROTOC_ERROR
)

# Check if protoc command was successful
if(NOT PROTOC_RESULT EQUAL "0")
    message(FATAL_ERROR "Failed to generate protobuf files: ${PROTOC_ERROR}\nOutput: ${PROTOC_OUTPUT}")
endif()

message(STATUS "=================End gRPC CMAKE=======================")
