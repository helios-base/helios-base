
add_executable(sample_coach
        ../thrift-generated/Game.cpp
        ../thrift-generated/soccer_service_types.cpp
        ../rpc-client/state_generator.cpp
        ../rpc-client/grpc_agent.cpp
        ../rpc-client/grpc_agent_coach.cpp

  sample_freeform_message.cpp
  sample_coach.cpp
  main_coach.cpp
  )

# add_dependencies(sample_coach generate_proto)

target_include_directories(sample_coach
  PRIVATE
    ${PROJECT_SOURCE_DIR}/../grpc/
    ${PROJECT_SOURCE_DIR}/src/
    ${PROJECT_SOURCE_DIR}/src/coach
    ${PROJECT_BINARY_DIR}
  PUBLIC
    ${Boost_INCLUDE_DIRS}
    ${LIBRCSC_INCLUDE_DIR}
  )

target_link_libraries(sample_coach
  PRIVATE
        ${THRIFT_LIBRARY}
        pthread
#    ${_GRPC_GRPCPP}
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
