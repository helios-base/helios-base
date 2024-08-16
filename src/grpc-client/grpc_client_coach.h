#include "grpc_client.h"

#ifndef GrpcAgentCoach_H
#define GrpcAgentCoach_H

class GrpcClientCoach : public GrpcClient {
    rcsc::CoachAgent * M_agent;
    public:
    GrpcClientCoach() ;

    void init(rcsc::CoachAgent * agent,
              std::string target="localhost",
              int port=50051,
              bool use_same_grpc_port=true,
              bool add_20_to_grpc_port_if_right_side=false);

    void getActions();
    State generateState() const;
};
#endif