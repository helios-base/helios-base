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
    std::string M_target;
    std::shared_ptr<Channel> M_channel;
    std::unique_ptr<Game::Stub> M_stub_;
    bool M_is_connected = false;
    bool M_param_sent = false;
    protos::AgentType M_agent_type;
    int M_unum;
    std::string M_team_name;
    protos::RegisterResponse * M_register_response = new protos::RegisterResponse();

    ~GrpcAgent() {}
    
    void sendParams(bool offline_logging) override;
    void addDlog(protos::Log log) const;
    void sendServerParam() const;
    void sendPlayerParams() const;
    void sendPlayerType() const;
    void sendInitMessage(bool offline_logging) const;
    bool Register() const;
    void sendByeCommand() const override;
    bool connectToGrpcServer() override;
    bool isConnected() const override{
        return M_is_connected;
    }

    static rcsc::ViewWidth convertViewWidth(protos::ViewWidth view_width);
    static rcsc::SideID convertSideID(protos::Side side_id);
    static rcsc::Vector2D convertVector2D(protos::RpcVector2D vector2d);
};

#endif