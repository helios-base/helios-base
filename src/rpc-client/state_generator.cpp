#include "state_generator.h"
using namespace apache::thrift;
using namespace apache::thrift::protocol;
using namespace apache::thrift::transport;
//using namespace soccer;
/**
 * Converts a `rcsc::SideID` to a `protos::Side`.
 *
 * @param sideId The `rcsc::SideID` to convert.
 * @return The converted `protos::Side`.
 */
soccer::Side::type StateGenerator::convertSide(rcsc::SideID sideId)
{
    if (sideId == rcsc::LEFT)
    {
        return soccer::Side::LEFT;
    }
    else if (sideId == rcsc::RIGHT)
    {
        return soccer::Side::RIGHT;
    }
    return soccer::Side::UNKNOWN;
}

/**
 * Converts the given `rcsc::ViewWidth::Type` to `soccer::ViewWidth`.
 *
 * @param viewWidth The `rcsc::ViewWidth::Type` to be converted.
 * @return The converted `soccer::ViewWidth`.
 */
soccer::ViewWidth::type StateGenerator::convertViewWidth(rcsc::ViewWidth::Type viewWidth)
{
    if (viewWidth == rcsc::ViewWidth::Type::NARROW)
    {
        return soccer::ViewWidth::NARROW;
    }
    else if (viewWidth == rcsc::ViewWidth::Type::NORMAL)
    {
        return soccer::ViewWidth::NORMAL;
    }
    else if (viewWidth == rcsc::ViewWidth::Type::WIDE)
    {
        return soccer::ViewWidth::WIDE;
    }
    return soccer::ViewWidth::NARROW;
}

/**
 * Converts an rcsc::Vector2D object to a soccer::Vector2D object.
 *
 * @param vector2D The rcsc::Vector2D object to be converted.
 * @return The converted soccer::Vector2D object.
 */
soccer::ThriftVector2D StateGenerator::convertVector2D(rcsc::Vector2D vector2D)
{
    auto res = soccer::ThriftVector2D();
    res.x = static_cast<float>(vector2D.x);
    res.y = static_cast<float>(vector2D.y);
    res.dist = static_cast<float>(vector2D.r());
    res.angle = static_cast<float>(vector2D.dir().degree());
    return res;
}

/**
 * Converts a `rcsc::BallObject` to a `soccer::Ball` object.
 *
 * @param ball The `rcsc::BallObject` to be converted.
 * @return The converted `soccer::Ball` object.
 */
soccer::Ball StateGenerator::convertBall(const rcsc::BallObject &ball)
{
    auto res = soccer::Ball();
    res.position = convertVector2D(ball.pos());
    res.relative_position = convertVector2D(ball.rpos());
    res.seen_position = convertVector2D(ball.seenPos());
    res.heard_position = convertVector2D(ball.heardPos());
    res.velocity = convertVector2D(ball.vel());
    res.seen_velocity = convertVector2D(ball.seenVel());
    res.heard_velocity = convertVector2D(ball.heardVel());
    res.pos_count = ball.posCount();
    res.seen_pos_count = ball.seenPosCount();
    res.heard_pos_count = ball.heardPosCount();
    res.vel_count = ball.velCount();
    res.seen_vel_count = ball.seenVelCount();
    res.heard_vel_count = ball.heardVelCount();
    res.lost_count = ball.lostCount();
    res.ghost_count = ball.ghostCount();
    res.dist_from_self = static_cast<float>(ball.distFromSelf());
    res.angle_from_self = static_cast<float>(ball.angleFromSelf().degree());

    return res;
}

/**
 * Converts a CoachBallObject to a soccer::Ball object.
 *
 * @param ball The CoachBallObject to be converted.
 * @return The converted soccer::Ball object.
 */
soccer::Ball StateGenerator::convertBall(const rcsc::CoachBallObject &ball)
{
    auto res = soccer::Ball();
    res.position = convertVector2D(ball.pos());
    res.velocity = convertVector2D(ball.vel());
    return res;
}

/**
 * Converts a `rcsc::SelfObject` to a `soccer::Self` object.
 *
 * @param self The `rcsc::SelfObject` to be converted.
 * @param wm The `rcsc::WorldModel` object containing the world state.
 * @return The converted `soccer::Self` object.
 */
soccer::Self StateGenerator::convertSelf(const rcsc::SelfObject &self, const rcsc::WorldModel &wm)
{
    auto res = soccer::Self();
    res.position = convertVector2D(self.pos());
    res.seen_position = convertVector2D(self.seenPos());
    res.heard_position = convertVector2D(self.heardPos());
    res.velocity = convertVector2D(self.vel());
    res.seen_velocity = convertVector2D(self.seenVel());
    res.pos_count = self.posCount();
    res.seen_pos_count = self.seenPosCount();
    res.heard_pos_count = self.heardPosCount();
    res.vel_count = self.velCount();
    res.seen_vel_count = self.seenVelCount();
    res.ghost_count = self.ghostCount();
    res.id = self.id();
    res.side = convertSide(self.side());
    res.uniform_number = self.unum();
    res.uniform_number_count = self.unumCount();
    res.is_goalie = self.goalie();
    res.body_direction = static_cast<float>(self.body().degree());
    res.body_direction_count = self.bodyCount();
    res.face_direction = static_cast<float>(self.face().degree());
    res.face_direction_count = self.faceCount();
    res.point_to_direction = static_cast<float>(self.pointtoAngle().degree());
    res.point_to_direction_count = self.pointtoCount();
    res.is_kicking = self.isKicking();
    res.dist_from_ball = static_cast<float>(self.distFromBall());
    res.angle_from_ball = static_cast<float>(self.angleFromBall().degree());
    res.ball_reach_steps = self.ballReachStep();
    res.is_tackling = self.isTackling();
    res.relative_neck_direction = static_cast<float>(self.neck().degree());
    res.stamina = static_cast<float>(self.stamina());
    res.is_kickable = self.isKickable();
    res.catch_probability = static_cast<float>(self.catchProbability());
    res.tackle_probability = static_cast<float>(self.tackleProbability());
    res.foul_probability = static_cast<float>(self.foulProbability());
    res.view_width = convertViewWidth(self.viewWidth().type());
    res.type_id = self.playerTypePtr()->id();

    double kick_rate = self.playerType().kickRate(wm.ball().distFromSelf(),
                                                  (wm.ball().angleFromSelf() - self.body()).degree());
    kick_rate = std::max(kick_rate, 0.0001);
    res.kick_rate = static_cast<float>(kick_rate);

    return res;
}

/**
 * Converts the given `rcsc::Intercept::ActionType` to `soccer::InterceptActionType`.
 *
 * @param actionType The `rcsc::Intercept::ActionType` to be converted.
 * @return The converted `soccer::InterceptActionType`.
 */
soccer::InterceptActionType::type StateGenerator::convertInterceptActionType(rcsc::Intercept::ActionType actionType)
{
    switch (actionType)
    {
    case rcsc::Intercept::ActionType::OMNI_DASH:
        return soccer::InterceptActionType::OMNI_DASH;
    case rcsc::Intercept::ActionType::TURN_BACK_DASH:
        return soccer::InterceptActionType::TURN_BACKWARD_DASH;
    case rcsc::Intercept::ActionType::TURN_FORWARD_DASH:
        return soccer::InterceptActionType::TURN_FORWARD_DASH;
    default:
        return soccer::InterceptActionType::UNKNOWN_Intercept_Action_Type;
    }
}
/**
 * Converts a `rcsc::InterceptTable` object to a `soccer::InterceptTable` object.
 *
 * @param interceptTable The `rcsc::InterceptTable` object to be converted.
 * @return The converted `soccer::InterceptTable` object.
 */
soccer::InterceptTable StateGenerator::convertInterceptTable(const rcsc::InterceptTable &interceptTable)
{
    auto res = soccer::InterceptTable();
    res.self_reach_steps = interceptTable.selfStep();
    res.first_teammate_reach_steps = interceptTable.teammateStep();
    res.second_teammate_reach_steps = interceptTable.secondTeammateStep();
    res.first_opponent_reach_steps = interceptTable.opponentStep();
    res.second_opponent_reach_steps = interceptTable.secondOpponentStep();
    if (interceptTable.firstTeammate())
        res.first_teammate_id = interceptTable.firstTeammate()->id();
    if (interceptTable.secondTeammate())
        res.second_teammate_id = interceptTable.secondTeammate()->id();
    if (interceptTable.firstOpponent())
        res.first_opponent_id = interceptTable.firstOpponent()->id();
    if (interceptTable.secondOpponent())
        res.second_opponent_id = interceptTable.secondOpponent()->id();

    res.self_intercept_info = std::vector<soccer::InterceptInfo>();
    for (auto intercept : interceptTable.selfResults())
    {
        soccer::InterceptInfo info = soccer::InterceptInfo();
        info.action_type = convertInterceptActionType(intercept.actionType());
        info.turn_steps = intercept.turnStep();
        info.turn_angle = static_cast<float>(intercept.turnAngle());
        info.dash_steps = intercept.dashStep();
        info.dash_power = static_cast<float>(intercept.dashPower());
        info.dash_dir = static_cast<float>(intercept.dashDir());
        info.final_self_position = convertVector2D(intercept.selfPos());
        info.final_ball_dist = intercept.ballDist();
        info.final_stamina = static_cast<float>(intercept.stamina());
        info.value = static_cast<float>(intercept.value());
        res.self_intercept_info.push_back(info);
    }

    return res;
}

/**
 * Updates the player object with the given player information.
 *
 * @param p The protobuf Player object to update.
 * @param player The rcsc::PlayerObject containing the player information.
 */
void StateGenerator::updatePlayerObject(soccer::Player & p, const rcsc::PlayerObject *player)
{
    p.position = convertVector2D(player->pos());
    p.seen_position = convertVector2D(player->seenPos());
    p.heard_position = convertVector2D(player->heardPos());
    p.velocity = convertVector2D(player->vel());
    p.seen_velocity = convertVector2D(player->seenVel());
    p.pos_count = player->posCount();
    p.seen_pos_count = player->seenPosCount();
    p.heard_pos_count = player->heardPosCount();
    p.vel_count = player->velCount();
    p.seen_vel_count = player->seenVelCount();
    p.ghost_count = player->ghostCount();
    p.dist_from_self = static_cast<float>(player->distFromSelf());
    p.angle_from_self = static_cast<float>(player->angleFromSelf().degree());
    p.id = player->id();
    p.side = convertSide(player->side());
    p.uniform_number = player->unum();
    p.uniform_number_count = player->unumCount();
    p.is_goalie = player->goalie();
    p.body_direction = static_cast<float>(player->body().degree());
    p.body_direction_count = player->bodyCount();
    p.face_direction = static_cast<float>(player->face().degree());
    p.face_direction_count = player->faceCount();
    p.point_to_direction = static_cast<float>(player->pointtoAngle().degree());
    p.point_to_direction_count = player->pointtoCount();
    p.is_kicking = player->isKicking();
    p.dist_from_ball = static_cast<float>(player->distFromBall());
    p.angle_from_ball = static_cast<float>(player->angleFromBall().degree());
    p.ball_reach_steps = player->ballReachStep();
    p.is_tackling = player->isTackling();
    if (player->playerTypePtr() == nullptr)
    {
        p.type_id = 0;
    }
    else
    {
        p.type_id = player->playerTypePtr()->id();
    }
}

/**
 * Updates the player object with the given CoachPlayerObject.
 *
 * @param p The pointer to the soccer::Player object to be updated.
 * @param player The pointer to the rcsc::CoachPlayerObject containing the updated player information.
 */
void StateGenerator::updatePlayerObject(soccer::Player &p, const rcsc::CoachPlayerObject *player)
{
    p.position = convertVector2D(player->pos());
    p.velocity = convertVector2D(player->vel());
    p.side = convertSide(player->side());
    p.uniform_number = player->unum();
    p.is_goalie = player->goalie();
    p.body_direction = static_cast<float>(player->body().degree());
    p.face_direction = static_cast<float>(player->face().degree());
    p.point_to_direction = static_cast<float>(player->pointtoAngle().degree());
    p.is_kicking = player->isKicking();
    p.ball_reach_steps = player->ballReachStep();
    p.is_tackling = player->isTackling();
    if (player->playerTypePtr() == nullptr)
    {
        p.type_id = 0;
    }
    else
    {
        p.type_id = player->playerTypePtr()->id();
    }

}

/**
 * Updates the abstract player object with the given player information.
 *
 * @param p The protobuf Player object to update.
 * @param player The rcsc::AbstractPlayerObject containing the player information.
 */
void StateGenerator::updateAbstractPlayerObject(soccer::Player &p, const rcsc::AbstractPlayerObject *player)
{
    p.position = convertVector2D(player->pos());
    p.seen_position = convertVector2D(player->seenPos());
    p.heard_position = convertVector2D(player->heardPos());
    p.velocity = convertVector2D(player->vel());
    p.seen_velocity = convertVector2D(player->seenVel());
    p.pos_count = player->posCount();
    p.seen_pos_count = player->seenPosCount();
    p.heard_pos_count = player->heardPosCount();
    p.vel_count = player->velCount();
    p.seen_vel_count = player->seenVelCount();
    p.ghost_count = player->ghostCount();
    p.dist_from_self = static_cast<float>(player->distFromSelf());
    p.angle_from_self = static_cast<float>(player->angleFromSelf().degree());
    p.id = player->id();
    p.side = convertSide(player->side());
    p.uniform_number = player->unum();
    p.uniform_number_count = player->unumCount();
    p.is_goalie = player->goalie();
    p.body_direction = static_cast<float>(player->body().degree());
    p.body_direction_count = player->bodyCount();
    p.face_direction = static_cast<float>(player->face().degree());
    p.face_direction_count = player->faceCount();
    p.point_to_direction = static_cast<float>(player->pointtoAngle().degree());
    p.point_to_direction_count = player->pointtoCount();
    p.is_kicking = player->isKicking();
    p.dist_from_ball = static_cast<float>(player->distFromBall());
    p.angle_from_ball = static_cast<float>(player->angleFromBall().degree());
    p.ball_reach_steps = player->ballReachStep();
    p.is_tackling = player->isTackling();
    if (player->playerTypePtr() == nullptr)
    {
        p.type_id = 0;
    }
    else
    {
        p.type_id = player->playerTypePtr()->id();
    }
}

/**
 * Converts the given `game_mode` from the `rcsc::GameMode::Type` enum to the corresponding `soccer::GameModeType` enum.
 *
 * @param game_mode The game mode to convert.
 * @return The converted game mode.
 */
soccer::GameModeType::type StateGenerator::converGameMode(const rcsc::GameMode::Type game_mode)
{
    switch (game_mode)
    {
    case rcsc::GameMode::BeforeKickOff:
        return soccer::GameModeType::BeforeKickOff;
    case rcsc::GameMode::TimeOver:
        return soccer::GameModeType::TimeOver;
    case rcsc::GameMode::PlayOn:
        return soccer::GameModeType::PlayOn;
    case rcsc::GameMode::KickOff_:
        return soccer::GameModeType::KickOff_;
    case rcsc::GameMode::KickIn_:
        return soccer::GameModeType::KickIn_;
    case rcsc::GameMode::FreeKick_:
        return soccer::GameModeType::FreeKick_;
    case rcsc::GameMode::CornerKick_:
        return soccer::GameModeType::CornerKick_;
    case rcsc::GameMode::GoalKick_:
        return soccer::GameModeType::GoalKick_;
    case rcsc::GameMode::AfterGoal_:
        return soccer::GameModeType::AfterGoal_;
    case rcsc::GameMode::OffSide_:
        return soccer::GameModeType::OffSide_;
    case rcsc::GameMode::PenaltyKick_:
        return soccer::GameModeType::PenaltyKick_;
    case rcsc::GameMode::FirstHalfOver:
        return soccer::GameModeType::FirstHalfOver;
    case rcsc::GameMode::Pause:
        return soccer::GameModeType::Pause;
    case rcsc::GameMode::Human:
        return soccer::GameModeType::Human;
    case rcsc::GameMode::FoulCharge_:
        return soccer::GameModeType::FoulCharge_;
    case rcsc::GameMode::FoulPush_:
        return soccer::GameModeType::FoulPush_;
    case rcsc::GameMode::FoulMultipleAttacker_:
        return soccer::GameModeType::FoulMultipleAttacker_;
    case rcsc::GameMode::FoulBallOut_:
        return soccer::GameModeType::FoulBallOut_;
    case rcsc::GameMode::BackPass_:
        return soccer::GameModeType::BackPass_;
    case rcsc::GameMode::FreeKickFault_:
        return soccer::GameModeType::FreeKickFault_;
    case rcsc::GameMode::CatchFault_:
        return soccer::GameModeType::CatchFault_;
    case rcsc::GameMode::IndFreeKick_:
        return soccer::GameModeType::IndFreeKick_;
    case rcsc::GameMode::PenaltySetup_:
        return soccer::GameModeType::PenaltySetup_;
    case rcsc::GameMode::PenaltyReady_:
        return soccer::GameModeType::PenaltyReady_;
    case rcsc::GameMode::PenaltyTaken_:
        return soccer::GameModeType::PenaltyTaken_;
    case rcsc::GameMode::PenaltyMiss_:
        return soccer::GameModeType::PenaltyMiss_;
    case rcsc::GameMode::PenaltyScore_:
        return soccer::GameModeType::PenaltyScore_;
    case rcsc::GameMode::IllegalDefense_:
        return soccer::GameModeType::IllegalDefense_;
    case rcsc::GameMode::PenaltyOnfield_:
        return soccer::GameModeType::PenaltyOnfield_;
    case rcsc::GameMode::PenaltyFoul_:
        return soccer::GameModeType::PenaltyFoul_;
    case rcsc::GameMode::GoalieCatch_:
        return soccer::GameModeType::GoalieCatch_;
    case rcsc::GameMode::ExtendHalf:
        return soccer::GameModeType::ExtendHalf;
    case rcsc::GameMode::MODE_MAX:
        return soccer::GameModeType::MODE_MAX;
    }
    return soccer::GameModeType::MODE_MAX;
}

/**
 * Converts a rcsc::WorldModel object to a soccer::WorldModel object.
 *
 * @param wm The rcsc::WorldModel object to be converted.
 * @return A pointer to the converted soccer::WorldModel object.
 */
soccer::WorldModel StateGenerator::convertWorldModel(const rcsc::WorldModel &wm)
{
    auto res = soccer::WorldModel();
    res.intercept_table = convertInterceptTable(wm.interceptTable());
    res.our_team_name = wm.ourTeamName();
    res.their_team_name = wm.theirTeamName();
    res.our_side = convertSide(wm.ourSide());
    res.last_set_play_start_time = wm.lastSetPlayStartTime().cycle();
    res.myself = convertSelf(wm.self(), wm);
    res.ball = convertBall(wm.ball());
    for (auto player : wm.teammates())
    {
        auto p = soccer::Player();
        updatePlayerObject(p, player);
    }
    for (auto player : wm.opponents())
    {
        auto p = soccer::Player();
        updatePlayerObject(p, player);
    }
    // unknowns
    int counter = -1;
    for (auto player : wm.ourPlayers())
    {
        auto p = soccer::Player();
        updateAbstractPlayerObject(p, player);
        if (player->unum() > 0)
            res.our_players_dict[player->unum()] = p;
        else
            res.our_players_dict[counter--] = p;
    }
    counter = -1;
    for (auto player : wm.theirPlayers())
    {
        auto p = soccer::Player();
        updateAbstractPlayerObject(p, player);
        if (player->unum() > 0)
            res.our_players_dict[player->unum()] = p;
        else
            res.our_players_dict[counter--] = p;
    }
    res.our_goalie_uniform_number = wm.ourGoalieUnum();
    res.their_goalie_uniform_number = wm.theirGoalieUnum();
    res.offside_line_x = wm.offsideLineX();
    res.offside_line_x_count = wm.offsideLineCount();
    if (wm.kickableTeammate())
        res.kickable_teammate_id = wm.kickableTeammate()->id();
    if (wm.kickableOpponent())
        res.kickable_opponent_id = wm.kickableOpponent()->id();
    res.last_kick_side = convertSide(wm.lastKickerSide());
    res.last_kicker_uniform_number = wm.lastKickerUnum();
    res.cycle = wm.time().cycle();
    res.game_mode_type = converGameMode(wm.gameMode().type());
    res.left_team_score = wm.gameMode().scoreLeft();
    res.right_team_score = wm.gameMode().scoreRight();
    res.is_our_set_play = wm.gameMode().isOurSetPlay(wm.ourSide());
    res.is_their_set_play = wm.gameMode().isTheirSetPlay(wm.ourSide());
    res.stoped_cycle = wm.gameMode().time().stopped();
    res.our_team_score = wm.ourSide() == rcsc::SideID::LEFT ? wm.gameMode().scoreLeft() : wm.gameMode().scoreRight();
    res.their_team_score = wm.ourSide() == rcsc::SideID::LEFT ? wm.gameMode().scoreRight() : wm.gameMode().scoreLeft();
    res.is_penalty_kick_mode = wm.gameMode().isPenaltyKickMode();
    return res;
}

/**
 * Converts a CoachWorldModel object to a soccer::WorldModel object.
 *
 * @param wm The CoachWorldModel object to be converted.
 * @return A pointer to the converted soccer::WorldModel object.
 */
soccer::WorldModel StateGenerator::convertCoachWorldModel(const rcsc::CoachWorldModel &wm)
{
    auto res = soccer::WorldModel();
    res.our_team_name = wm.ourTeamName();
    res.their_team_name = wm.theirTeamName();
    res.our_side = convertSide(wm.ourSide());
    res.last_set_play_start_time = wm.lastSetPlayStartTime().cycle();
    res.ball = convertBall(wm.ball());
    for (auto player : wm.teammates())
    {
        if(player == nullptr || !player->isValid() || player->unum() < 1 || player->unum() > 11 ){
            continue;
        }
        std::cout<<">>added teammate"<<std::endl;
        auto p = soccer::Player();
        updatePlayerObject(p, player);
        res.teammates.push_back(p);
    }
    for (auto player : wm.opponents())
    {
        if(player == nullptr || !player->isValid() || player->unum() < 1 || player->unum() > 11 ){
            continue;
        }
        auto p = soccer::Player();
        updatePlayerObject(p, player);
        res.opponents.push_back(p);
    }
    res.offside_line_x = wm.ourOffsideLineX();
    res.last_kick_side = convertSide(wm.lastKickerSide());
    res.last_kicker_uniform_number = wm.lastKickerUnum();
    res.cycle = wm.time().cycle();
    res.game_mode_type = converGameMode(wm.gameMode().type());
    res.left_team_score = wm.gameMode().scoreLeft();
    res.right_team_score = wm.gameMode().scoreRight();
    res.is_our_set_play = wm.gameMode().isOurSetPlay(wm.ourSide());
    res.is_their_set_play = wm.gameMode().isTheirSetPlay(wm.ourSide());
    res.stoped_cycle = wm.gameMode().time().stopped();
    res.our_team_score = wm.ourSide() == rcsc::SideID::LEFT ? wm.gameMode().scoreLeft() : wm.gameMode().scoreRight();
    res.their_team_score = wm.ourSide() == rcsc::SideID::LEFT ? wm.gameMode().scoreRight() : wm.gameMode().scoreLeft();
    res.is_penalty_kick_mode = wm.gameMode().isPenaltyKickMode();
    return res;
}