# List of Thrift source files
set(THRIFT_SOURCES
        ../thrift-generated/Game.cpp
        ../thrift-generated/soccer_service_types.cpp
        ../thrift-client/thrift_state_generator.cpp
        ../thrift-client/thrift_client.cpp
        ../thrift-client/thrift_client_trainer.cpp
)

# List of gRPC source files
set(GRPC_SOURCES
        ../grpc-generated/service.pb.cc
        ../grpc-generated/service.grpc.pb.cc
        ../grpc-client/state_generator.cpp
        ../grpc-client/grpc_client.cpp
        ../grpc-client/grpc_client_trainer.cpp
)

# List of common source files
set(COMMON_SOURCES
        sample_trainer.cpp
        main_trainer.cpp
)

# Combine sources based on selected RPC framework
if (USE_THRIFT AND USE_GRPC)
  add_executable(sample_trainer
          ${GRPC_SOURCES}
          ${THRIFT_SOURCES}
          ${COMMON_SOURCES}
  )
elseif (USE_THRIFT)
  add_executable(sample_trainer
          ${THRIFT_SOURCES}
          ${COMMON_SOURCES}
  )
elseif (USE_GRPC)
  add_executable(sample_trainer
          ${GRPC_SOURCES}
          ${COMMON_SOURCES}
  )
else()
  message(FATAL_ERROR "Neither USE_GRPC nor USE_THRIFT is defined. One must be enabled.")
endif()

target_include_directories(sample_trainer
        PRIVATE
        ${PROJECT_SOURCE_DIR}/src
        ${PROJECT_SOURCE_DIR}/trainer
        ${PROJECT_BINARY_DIR}

        # Include gRPC directories only if gRPC is enabled
        $<$<BOOL:${USE_GRPC}>:${PROJECT_SOURCE_DIR}/../idl/grpc/>

        PUBLIC
        ${Boost_INCLUDE_DIRS}
        ${LIBRCSC_INCLUDE_DIR}
)

target_link_libraries(sample_trainer
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

set_target_properties(sample_trainer
  PROPERTIES
  RUNTIME_OUTPUT_DIRECTORY ${PROJECT_BINARY_DIR}/bin
  )
