#ifndef GRPC_AGENT_H
#define GRPC_AGENT_H

#include "absl/flags/flag.h"
#include "absl/flags/parse.h"
#include <grpcpp/grpcpp.h>
#include "service.grpc.pb.h"
#include "service.pb.h"
#include <rcsc/player/player_agent.h>
#include <rcsc/coach/coach_agent.h>
#include <rcsc/trainer/trainer_agent.h>



using grpc::Channel;
using grpc::ClientContext;
using grpc::Status;
using protos::Game;
using protos::State;
using protos::PlayerAction;
using protos::CoachAction;
using protos::TrainerAction;

class GrpcAgent {
public:
    std::shared_ptr<Channel> channel;
    std::unique_ptr<Game::Stub> stub_;
    bool param_sent = false;
    protos::AgentType agent_type;

    ~GrpcAgent() {}
    
    void sendParams(bool offline_logging);
    void addDlog(protos::Log log) const;
    void sendServerParam() const;
    void sendPlayerParams() const;
    void sendPlayerType() const;
    void sendInitMessage(bool offline_logging) const;

    static rcsc::ViewWidth convertViewWidth(protos::ViewWidth view_width);
    static rcsc::SideID convertSideID(protos::Side side_id);
    static rcsc::Vector2D convertVector2D(protos::Vector2D vector2d);
};

#endif