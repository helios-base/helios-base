#include "grpc_client.h"

class GrpcClientTrainer : public GrpcClient {
    rcsc::TrainerAgent * M_agent;
    
    public:
    GrpcClientTrainer() ;

    void init(rcsc::TrainerAgent * agent,
              std::string target="localhost",
              int port=50051,
              bool use_same_grpc_port=true,
              bool add_20_to_grpc_port_if_right_side=false);

    void getActions();
    State generateState() const;
};