#include "grpc_agent.h"

#ifndef GrpcAgentCoach_H
#define GrpcAgentCoach_H

class GrpcAgentCoach : public GrpcAgent {
    rcsc::CoachAgent * M_agent;
    std::string target;
    public:
    GrpcAgentCoach() ;

    void init(rcsc::CoachAgent * agent,
              std::string target="localhost",
              int port=50051,
              bool use_same_grpc_port=true,
              bool add_20_to_grpc_port_if_right_side=false);

    bool connectToGrpcServer();
    void getActions() const;
    State generateState() const;
};
#endif