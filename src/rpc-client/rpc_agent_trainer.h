#include "rpc_agent.h"

class RpcAgentTrainer : public RpcAgent {
    rcsc::TrainerAgent * M_agent;
    
    public:
    RpcAgentTrainer() ;

    void init(rcsc::TrainerAgent * agent,
              std::string target="localhost",
              int port=50051,
              bool use_same_grpc_port=true,
              bool add_20_to_grpc_port_if_right_side=false);

    void getActions() const;
    soccer::State generateState() const;
};