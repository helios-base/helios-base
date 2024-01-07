
add_executable(sample_trainer
  ../grpc/state_generator.cpp
  ../grpc/service.pb.cc
  ../grpc/service.grpc.pb.cc
  ../grpc/grpc_agent.cpp
  ../grpc/grpc_agent_trainer.cpp
  sample_trainer.cpp
  main_trainer.cpp
  )

target_include_directories(sample_trainer
  PRIVATE
    ${PROJECT_SOURCE_DIR}/../grpc/
    ${PROJECT_SOURCE_DIR}/src
    ${PROJECT_SOURCE_DIR}/trainer
    ${PROJECT_BINARY_DIR}
  PUBLIC
    ${Boost_INCLUDE_DIRS}
    ${LIBRCSC_INCLUDE_DIR}
  )

target_link_libraries(sample_trainer
  PRIVATE
    service_grpc_proto
    absl::flags
    absl::flags_parse
    ${_REFLECTION}
    ${_GRPC_GRPCPP}
    ${_PROTOBUF_LIBPROTOBUF}
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
