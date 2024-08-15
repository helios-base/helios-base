# List of Thrift source files
set(THRIFT_SOURCES
        ../thrift-generated/Game.cpp
        ../thrift-generated/soccer_service_types.cpp
        ../thrift-client/thrift_state_generator.cpp
        ../thrift-client/thrift_agent.cpp
        ../thrift-client/thrift_agent_coach.cpp
)

# List of gRPC source files
set(GRPC_SOURCES
        ../grpc-generated/service.pb.cc
        ../grpc-generated/service.grpc.pb.cc
        ../grpc-client/state_generator.cpp
        ../grpc-client/grpc_agent.cpp
        ../grpc-client/grpc_agent_coach.cpp
)

set (COMMON_SOURCES
  sample_freeform_message.cpp
  sample_coach.cpp
  main_coach.cpp
  )

if (USE_THRIFT AND USE_GRPC)
  add_executable(sample_coach
          ${GRPC_SOURCES}
          ${THRIFT_SOURCES}
          ${COMMON_SOURCES}
  )
elseif (USE_THRIFT)
  add_executable(sample_coach
          ${THRIFT_SOURCES}
          ${COMMON_SOURCES}
  )
elseif (USE_GRPC)
  add_executable(sample_coach
          ${GRPC_SOURCES}
          ${COMMON_SOURCES}
  )
else()
  message(FATAL_ERROR "Neither USE_GRPC nor USE_THRIFT is defined. One must be enabled.")
endif()
# add_dependencies(sample_coach generate_proto)

target_include_directories(sample_coach
  PRIVATE
        # Include gRPC directories only if gRPC is enabled
        $<$<BOOL:${USE_GRPC}>:${PROJECT_SOURCE_DIR}/../idl/grpc/>

    ${PROJECT_SOURCE_DIR}/src/
    ${PROJECT_SOURCE_DIR}/src/coach
    ${PROJECT_BINARY_DIR}
  PUBLIC
    ${Boost_INCLUDE_DIRS}
    ${LIBRCSC_INCLUDE_DIR}
  )

target_link_libraries(sample_coach
  PRIVATE
        # Link Thrift library only if Thrift is enabled
        $<$<BOOL:${USE_THRIFT}>:${THRIFT_LIBRARY}>

        # Link gRPC++ library only if gRPC is enabled
        $<$<BOOL:${USE_GRPC}>:${_GRPC_GRPCPP}>
        pthread
  PUBLIC
    ${LIBRCSC_LIB}
    Boost::system
    ZLIB::ZLIB
    Threads::Threads
  )

  set_target_properties(sample_coach
  PROPERTIES
  RUNTIME_OUTPUT_DIRECTORY ${PROJECT_BINARY_DIR}/bin
  )
