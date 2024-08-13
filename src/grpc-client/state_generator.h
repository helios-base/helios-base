#include "../grpc-generated/service.pb.h"
#include <rcsc/player/player_agent.h>
#include <rcsc/coach/coach_agent.h>
#include <rcsc/trainer/trainer_agent.h>
#include <rcsc/player/world_model.h>

using protos::State;
using protos::WorldModel;
/**
 * @class StateGenerator
 * @brief This class provides static methods to convert various objects from the rcsc namespace to their corresponding protobuf representations.
 */
class StateGenerator
{
public:
    static protos::Side convertSide(rcsc::SideID sideId);
    static protos::ViewWidth convertViewWidth(rcsc::ViewWidth::Type viewWidth);
    static protos::RpcVector2D *convertVector2D(rcsc::Vector2D vector2D);
    static protos::Ball *convertBall(const rcsc::BallObject &ball);
    static protos::Ball *convertBall(const rcsc::CoachBallObject &ball);
    static protos::Self *convertSelf(const rcsc::SelfObject &self, const rcsc::WorldModel &wm);
    static protos::InterceptActionType convertInterceptActionType(rcsc::Intercept::ActionType actionType);
    static protos::InterceptTable *convertInterceptTable(const rcsc::InterceptTable &interceptTable);
    static void updatePlayerObject(protos::Player *p, const rcsc::PlayerObject *player);
    static void updatePlayerObject(protos::Player *p, const rcsc::CoachPlayerObject *player);
    static void updateAbstractPlayerObject(protos::Player *p, const rcsc::AbstractPlayerObject *player);
    static protos::GameModeType converGameMode(const rcsc::GameMode::Type game_mode);
    static protos::WorldModel *convertWorldModel(const rcsc::WorldModel &wm);
    static protos::WorldModel *convertCoachWorldModel(const rcsc::CoachWorldModel &wm);
};