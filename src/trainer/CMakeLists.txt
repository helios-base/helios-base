
add_executable(sample_trainer
        ../thrift-generated/Game.cpp
        ../thrift-generated/soccer_service_types.cpp
        ../rpc-client/state_generator.cpp
        ../rpc-client/grpc_agent.cpp
        ../rpc-client/grpc_agent_trainer.cpp
  sample_trainer.cpp
  main_trainer.cpp
  )

  
# add_dependencies(sample_trainer generate_proto)

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
        ${THRIFT_LIBRARY}
        pthread
#    ${_GRPC_GRPCPP}
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
