#include "absl/flags/flag.h"
#include "absl/flags/parse.h"
#include <grpcpp/grpcpp.h>
#include "service.grpc.pb.h"
#include "service.pb.h"
#include <rcsc/player/player_agent.h>
#include "player/sample_communication.h"


using grpc::Channel;
using grpc::ClientContext;
using grpc::Status;
using protos::Game;
using protos::State;
using protos::Action;

class GrpcAgent {
public:
    std::shared_ptr<Channel> channel;
    std::unique_ptr<Game::Stub> stub_;
    bool param_sent = false;
    Communication::Ptr sample_communication;
    

    GrpcAgent() {}

    void init(rcsc::PlayerAgent * agent,
              std::string target="localhost",
              int port=50051,
              bool use_same_grpc_port=true,
              bool add_20_to_grpc_port_if_right_side=false){
        if (add_20_to_grpc_port_if_right_side)
            if (agent->world().ourSide() == rcsc::SideID::RIGHT)
                port += 20;

        if (!use_same_grpc_port){
            port += agent->world().self().unum();
        }

        target += ":" + std::to_string(port);

        channel = grpc::CreateChannel(target, grpc::InsecureChannelCredentials());
        stub_ = Game::NewStub(channel);
        sample_communication = Communication::Ptr( new SampleCommunication() );
    }

    void sendParams(rcsc::PlayerAgent *agent){
        if (!param_sent){
            sendServerParam();
            sendPlayerParams();
            sendPlayerType();
            sendInitMessage(agent);
            param_sent = true;
        }
    }
    ~GrpcAgent() {}
    void getAction(rcsc::PlayerAgent *agent) const;
    void addSayMessage(rcsc::PlayerAgent *agent, protos::Say sayMessage) const;
    void addDlog(protos::Log log) const;
    void sendServerParam() const;
    void sendPlayerParams() const;
    void sendPlayerType() const;
    void sendInitMessage(rcsc::PlayerAgent * agent) const;

private:
    static rcsc::ViewWidth convertViewWidth(protos::ViewWidth view_width);
    static rcsc::SideID convertSideID(protos::Side side_id);
    static rcsc::Vector2D convertVector2D(protos::Vector2D vector2d);
};