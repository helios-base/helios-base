#include "rpc_agent.h"

#ifndef GrpcAgentCoach_H
#define GrpcAgentCoach_H

class RpcAgentCoach : public RpcAgent {
    rcsc::CoachAgent * M_agent;
    public:
    RpcAgentCoach() ;

    void init(rcsc::CoachAgent * agent,
              std::string target="localhost",
              int port=50051,
              bool use_same_grpc_port=true,
              bool add_20_to_grpc_port_if_right_side=false);

    void getActions() const;
    soccer::State generateState() const;
};
#endif