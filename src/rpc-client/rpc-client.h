//
// Created by nader on 8/13/24.
//

#ifndef HELIOS_BASE_RPC_CLIENT_H
#define HELIOS_BASE_RPC_CLIENT_H

#include <rcsc/player/player_agent.h>

class IRpcClient {
public:
    virtual bool isConnected() const = 0;
    virtual bool connectToGrpcServer() = 0;
    virtual void sendParams(bool offline_logging) = 0;
    virtual void getActions() = 0;
    virtual void sendByeCommand() const = 0;
};
#endif //HELIOS_BASE_RPC_CLIENT_H
