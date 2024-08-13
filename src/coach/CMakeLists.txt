
add_executable(sample_coach
        ../thrift-generated/Game.cpp
        ../thrift-generated/soccer_service_types.cpp
        ../thrift-client/thrift_state_generator.cpp
        ../thrift-client/thrift_agent.cpp
        ../thrift-client/thrift_agent_coach.cpp
        ../grpc-generated/service.pb.cc
        ../grpc-generated/service.grpc.pb.cc
        ../grpc-client/state_generator.cpp
        ../grpc-client/grpc_agent.cpp
        ../grpc-client/grpc_agent_coach.cpp

  sample_freeform_message.cpp
  sample_coach.cpp
  main_coach.cpp
  )

# add_dependencies(sample_coach generate_proto)

target_include_directories(sample_coach
  PRIVATE
#    ${PROJECT_SOURCE_DIR}/../idl/grpc-client
        ${PROJECT_SOURCE_DIR}/../idl/grpc/

    ${PROJECT_SOURCE_DIR}/src/
    ${PROJECT_SOURCE_DIR}/src/coach
    ${PROJECT_BINARY_DIR}
  PUBLIC
    ${Boost_INCLUDE_DIRS}
    ${LIBRCSC_INCLUDE_DIR}
  )

target_link_libraries(sample_coach
  PRIVATE
        ${_GRPC_GRPCPP}
        ${THRIFT_LIBRARY}
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
