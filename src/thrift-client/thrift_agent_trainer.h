#include "thrift_agent.h"

class ThriftAgentTrainer : public ThriftAgent {
    rcsc::TrainerAgent * M_agent;
    
    public:
    ThriftAgentTrainer() ;

    void init(rcsc::TrainerAgent * agent,
              std::string target="localhost",
              int port=50051,
              bool use_same_grpc_port=true,
              bool add_20_to_grpc_port_if_right_side=false);

    void getActions();
    soccer::State generateState() const;
};