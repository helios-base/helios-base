#include "absl/flags/flag.h"
#include "absl/flags/parse.h"
#include <grpcpp/grpcpp.h>
#include "service.grpc.pb.h"
#include "service.pb.h"
#include <rcsc/player/player_agent.h>


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
    GrpcAgent() {}

    void init(std::string target="localhost:50051"){
        channel = grpc::CreateChannel(target, grpc::InsecureChannelCredentials());
        stub_ = Game::NewStub(channel);
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