#ifndef GRPC_AGENT_H
#define GRPC_AGENT_H

//#include "absl/flags/flag.h"
//#include "absl/flags/parse.h"
//#include <grpcpp/grpcpp.h>

//#include "service.rpc-client.pb.h"
//#include "service.pb.h"

#include <rcsc/player/player_agent.h>
#include <rcsc/coach/coach_agent.h>
#include <rcsc/trainer/trainer_agent.h>

#include <thrift/transport/TSocket.h>
#include <thrift/transport/TBufferTransports.h>
#include <thrift/protocol/TBinaryProtocol.h>
#include "thrift-generated/Game.h"
#include "thrift-generated/soccer_service_types.h"
using namespace apache::thrift;
using namespace apache::thrift::protocol;
using namespace apache::thrift::transport;
//using namespace soccer;

class RpcAgent {
public:
    std::string server_host;
    int server_port;
    std::shared_ptr<TTransport> socket;
    std::shared_ptr<TTransport> transport;
    std::shared_ptr<TProtocol> protocol;
    std::shared_ptr<soccer::GameClient> client;
    bool is_connected = false;
    bool param_sent = false;
    soccer::AgentType::type agent_type;

    ~RpcAgent() {}
    
    void sendParams(bool offline_logging);
    void addDlog(soccer::Log log) const;
    void sendServerParam() const;
    void sendPlayerParams() const;
    void sendPlayerType() const;
    void sendInitMessage(bool offline_logging) const;
    bool getInitMessage() const;
    void sendByeCommand() const;
    bool connectToGrpcServer();

    static rcsc::ViewWidth convertViewWidth(soccer::ViewWidth::type view_width);
    static rcsc::SideID convertSideID(soccer::Side::type side_id);
    static rcsc::Vector2D convertVector2D(soccer::ThriftVector2D vector2d);
};

#endif