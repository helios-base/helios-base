#include "grpc_agent.h"
#include "player/sample_communication.h"

class GrpcAgentPlayer : public GrpcAgent {
    rcsc::PlayerAgent * M_agent;
    Communication::Ptr sample_communication;
    public:
    GrpcAgentPlayer();

    void init(rcsc::PlayerAgent * agent,
              std::string target="localhost",
              int port=50051,
              bool use_same_grpc_port=true,
              bool add_20_to_grpc_port_if_right_side=false);

    void getActions() const;
    void addSayMessage(soccer::Say sayMessage) const;
    soccer::State generateState() const;
    void addHomePosition(soccer::WorldModel * world_model) const;
};