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

    void getActions();
    void addSayMessage(protos::Say sayMessage) const;
    State generateState() const;
    void addHomePosition(protos::WorldModel * world_model) const;
};