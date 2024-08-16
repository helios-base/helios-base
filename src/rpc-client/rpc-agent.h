//
// Created by nader on 8/15/24.
//

#ifndef HELIOS_BASE_RPC_AGENT_H
#define HELIOS_BASE_RPC_AGENT_H

#include <string>
#include "rpc-client.h"

class RpcAgent {

public:
    IRpcClient * M_rpc_client;
    int M_first_rpc_port;
    bool M_use_same_rpc_port;
    bool M_add_20_to_rpc_port_if_right_side;
    std::string M_rpc_server_address;
    bool M_use_thrift;

    void SetFirstRpcPort(int port) { M_first_rpc_port = port; }
    void SetUseSameRpcPort(bool use_same_grpc_port) { M_use_same_rpc_port = use_same_grpc_port; }
    void SetAdd20ToRpcPortIfRightSide(bool add_20_to_grpc_port_if_right_side) { M_add_20_to_rpc_port_if_right_side = add_20_to_grpc_port_if_right_side; }
    void SetRpcIp(std::string grpc_server_address) { M_rpc_server_address = grpc_server_address; }
};
#endif //HELIOS_BASE_RPC_AGENT_H
