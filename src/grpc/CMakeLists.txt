# cmake_minimum_required(VERSION 3.8)

# project(helios-base VERSION 2023.03)

# if(CMAKE_VERSION VERSION_LESS "3.7.0")
#     set(CMAKE_INCLUDE_CURRENT_DIR ON)
# endif()

# # compliler options
# set(CMAKE_CXX_STANDARD 17)
# set(CMAKE_CXX_STANDARD_REQUIRED True)

# include(../../grpc/common.cmake)
get_filename_component(service_proto "../../grpc/CrossLangSoccerFramework/protos/service.proto" ABSOLUTE)
get_filename_component(service_proto_path "${service_proto}" PATH)

set(service_proto_srcs "${CMAKE_CURRENT_SOURCE_DIR}/service.pb.cc")
set(service_proto_hdrs "${CMAKE_CURRENT_SOURCE_DIR}/service.pb.h")
set(service_grpc_srcs "${CMAKE_CURRENT_SOURCE_DIR}/service.grpc.pb.cc")
set(service_grpc_hdrs "${CMAKE_CURRENT_SOURCE_DIR}/service.grpc.pb.h")

add_custom_command(
      OUTPUT "${service_proto_srcs}" "${service_proto_hdrs}" "${service_grpc_srcs}" "${service_grpc_hdrs}"
      COMMAND ${_PROTOBUF_PROTOC}
      ARGS --grpc_out "${CMAKE_CURRENT_SOURCE_DIR}"
        --cpp_out "${CMAKE_CURRENT_SOURCE_DIR}"
        -I "${service_proto_path}"
        --plugin=protoc-gen-grpc="${_GRPC_CPP_PLUGIN_EXECUTABLE}"
        "${service_proto}"
      DEPENDS "${service_proto}")

add_library(service_grpc_proto
    ${service_grpc_srcs}
    ${service_grpc_hdrs}
    ${service_proto_srcs}
    ${service_proto_hdrs})

target_link_libraries(service_grpc_proto
    ${_REFLECTION}
    ${_GRPC_GRPCPP}
    ${_PROTOBUF_LIBPROTOBUF})

find_package(Threads REQUIRED)