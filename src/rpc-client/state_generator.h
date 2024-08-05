//#include "service.pb.h"

#include <rcsc/player/player_agent.h>
#include <rcsc/coach/coach_agent.h>
#include <rcsc/trainer/trainer_agent.h>
#include <rcsc/player/world_model.h>
#include <thrift/transport/TSocket.h>
#include <thrift/transport/TBufferTransports.h>
#include <thrift/protocol/TBinaryProtocol.h>
#include "../thrift-generated/Game.h"
#include "../thrift-generated/soccer_service_types.h"
using namespace apache::thrift;
using namespace apache::thrift::protocol;
using namespace apache::thrift::transport;
//using namespace soccer;
//using protos::State;
//using protos::WorldModel;
/**
 * @class StateGenerator
 * @brief This class provides static methods to convert various objects from the rcsc namespace to their corresponding protobuf representations.
 */
class StateGenerator
{
public:
    static soccer::Side::type convertSide(rcsc::SideID sideId);
    static soccer::ViewWidth::type convertViewWidth(rcsc::ViewWidth::Type viewWidth);
    static soccer::ThriftVector2D convertVector2D(rcsc::Vector2D vector2D);
    static soccer::Ball convertBall(const rcsc::BallObject &ball);
    static soccer::Ball convertBall(const rcsc::CoachBallObject &ball);
    static soccer::Self convertSelf(const rcsc::SelfObject &self, const rcsc::WorldModel &wm);
    static soccer::InterceptActionType::type convertInterceptActionType(rcsc::Intercept::ActionType actionType);
    static soccer::InterceptTable convertInterceptTable(const rcsc::InterceptTable &interceptTable);
    static void updatePlayerObject(soccer::Player &p, const rcsc::PlayerObject *player);
    static void updatePlayerObject(soccer::Player &p, const rcsc::CoachPlayerObject *player);
    static void updateAbstractPlayerObject(soccer::Player &p, const rcsc::AbstractPlayerObject *player);
    static soccer::GameModeType::type converGameMode(const rcsc::GameMode::Type game_mode);
    static soccer::WorldModel convertWorldModel(const rcsc::WorldModel &wm);
    static soccer::WorldModel convertCoachWorldModel(const rcsc::CoachWorldModel &wm);
};