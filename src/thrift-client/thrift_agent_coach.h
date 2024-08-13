#include "thrift_agent.h"

#ifndef THRIFTAgentCoach_H
#define THRIFTAgentCoach_H

class ThriftAgentCoach : public ThriftAgent {
    rcsc::CoachAgent * M_agent;
    public:
    ThriftAgentCoach() ;

    void init(rcsc::CoachAgent * agent,
              std::string target="localhost",
              int port=50051,
              bool use_same_grpc_port=true,
              bool add_20_to_grpc_port_if_right_side=false);

    void getActions() const;
    soccer::State generateState() const;
};
#endif