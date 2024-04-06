set(GRPC_OUTPUT_DIR "${CMAKE_CURRENT_SOURCE_DIR}/../src/grpc")
set(PROTO_FILE "service.proto")
set(PROTO_PATH "${CMAKE_CURRENT_SOURCE_DIR}/protos")

find_program(PROTOBUF_PROTOC_EXECUTABLE protoc)
if(NOT PROTOBUF_PROTOC_EXECUTABLE)
    message(FATAL_ERROR "Protoc not found. Please make sure it is installed and in the system PATH.")
endif()

find_program(GRPC_CPP_PLUGIN grpc_cpp_plugin $ENV{HOME}/.local/bin)
if (NOT GRPC_CPP_PLUGIN)
    message(FATAL_ERROR "grpc_cpp_plugin not found. Please make sure it is installed and in the system PATH.")
endif()

message(STATUS "GRPC_OUTPUT_DIR: ${GRPC_OUTPUT_DIR}")
message(STATUS "PROTO_FILE: ${PROTO_FILE}")
message(STATUS "PROTO_PATH: ${PROTO_PATH}")
message(STATUS "Protoc executable used by CMake: ${PROTOBUF_PROTOC_EXECUTABLE}")
message(STATUS "GRPC_CPP_PLUGIN: ${GRPC_CPP_PLUGIN}")

message("Command: ${PROTOBUF_PROTOC_EXECUTABLE} 
        --grpc_out=${GRPC_OUTPUT_DIR} 
        --cpp_out=${GRPC_OUTPUT_DIR} 
        --plugin=protoc-gen-grpc=${GRPC_CPP_PLUGIN} 
        --proto_path=${PROTO_PATH}")

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

if(NOT PROTOC_RESULT EQUAL "0")
    message(FATAL_ERROR "Failed to generate protobuf files: ${PROTOC_ERROR}")
endif()

