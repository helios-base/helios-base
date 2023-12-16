#include "grpc_agent.h"
#include "state_generator.h"
#include "action_convertor.h"

#include <chrono>
using std::chrono::high_resolution_clock;
using std::chrono::duration_cast;
using std::chrono::duration;
using std::chrono::milliseconds;
void GrpcAgent::getAction(rcsc::PlayerAgent * agent) const{
    State state = StateGenerator::generateState(agent);
    protos::Actions actions;
    ClientContext context;
    static int c = 0;
    static int t_1_2 = 0;
    c++;
    auto t1 = std::chrono::high_resolution_clock::now();
    Status status = stub_->GetActions(&context, state, &actions);
    auto t2 = std::chrono::high_resolution_clock::now();
    t_1_2 += (t2 - t1).count();
    if (c > 100){
        std::cout<<"grpc:"<<static_cast<float>(t_1_2) / float (c)<<std::endl;
    }
    if (status.ok()) {
//        std::cout << "Action: " << actions.DebugString() << std::endl;
        for(int i = 0; i < actions.actions_size(); i++){
            auto action = actions.actions(i);
            if (action.action_case()  == Action::kDash){
                agent->doDash(action.dash().power());
            }
        }
    } else {
        std::cout << status.error_code() << ": " << status.error_message()
                  << std::endl;
    }
}