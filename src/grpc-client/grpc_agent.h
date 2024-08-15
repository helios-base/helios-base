#ifndef GRPC_AGENT_H
#define GRPC_AGENT_H

#include "absl/flags/flag.h"
#include "absl/flags/parse.h"
#include <grpcpp/grpcpp.h>
#include "../grpc-generated/service.pb.h"
#include "../grpc-generated/service.grpc.pb.h"
#include <rcsc/player/player_agent.h>
#include <rcsc/coach/coach_agent.h>
#include <rcsc/trainer/trainer_agent.h>
#include "rpc-client/rpc-agent.h"



using grpc::Channel;
using grpc::ClientContext;
using grpc::Status;
using protos::Game;
using protos::State;
using protos::PlayerAction;
using protos::CoachAction;
using protos::TrainerAction;

class GrpcAgent : public IRpcAgent{
public:
    std::string target;
    std::shared_ptr<Channel> channel;
    std::unique_ptr<Game::Stub> stub_;
    bool is_connected = false;
    bool param_sent = false;
    protos::AgentType agent_type;
    int unum;
    std::string team_name;
    protos::RegisterResponse * register_response = new protos::RegisterResponse();

    ~GrpcAgent() {}
    
    void sendParams(bool offline_logging);
    void addDlog(protos::Log log) const;
    void sendServerParam() const;
    void sendPlayerParams() const;
    void sendPlayerType() const;
    void sendInitMessage(bool offline_logging) const;
    bool Register() const;
    void sendByeCommand() const;
    bool connectToGrpcServer();
    bool isConnected() const {
        return is_connected;
    }

    static rcsc::ViewWidth convertViewWidth(protos::ViewWidth view_width);
    static rcsc::SideID convertSideID(protos::Side side_id);
    static rcsc::Vector2D convertVector2D(protos::RpcVector2D vector2d);
};

#endif