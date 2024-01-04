#include "service.pb.h"
#include <rcsc/player/player_agent.h>
#include <rcsc/player/world_model.h>
#include "../player/strategy.h"


using protos::State;
using protos::WorldModel;
class StateGenerator {
public:
    static State generateState(rcsc::PlayerAgent *agent) {
        const rcsc::WorldModel &wm = agent->world();
        WorldModel * worldModel = convertWorldModel(wm);
        State state;
        state.set_allocated_world_model(worldModel);
        return state;
    }

    static protos::Side convertSide(rcsc::SideID sideId){
        if (sideId == rcsc::LEFT) {
            return protos::Side::LEFT;
        }
        else if (sideId == rcsc::RIGHT)
        {
            return protos::Side::RIGHT;
        }
        return protos::Side::UNKNOWN;
    }

    static protos::ViewWidth convertViewWidth(rcsc::ViewWidth::Type viewWidth){
        if (viewWidth == rcsc::ViewWidth::Type::NARROW)
        {
            return protos::ViewWidth::NARROW;
        }
        else if (viewWidth == rcsc::ViewWidth::Type::NORMAL)
        {
            return protos::ViewWidth::NORMAL;
        }
        else if (viewWidth == rcsc::ViewWidth::Type::WIDE)
        {
            return protos::ViewWidth::WIDE;
        }
        return protos::ViewWidth::NARROW;
    }

    static protos::Vector2D * convertVector2D(rcsc::Vector2D vector2D){
        auto res = new protos::Vector2D();
        res->set_x(static_cast<float>(vector2D.x));
        res->set_y(static_cast<float>(vector2D.y));
        res->set_dist(static_cast<float>(vector2D.r()));
        res->set_angle(static_cast<float>(vector2D.dir().degree()));
        return res;
    }

    static protos::Ball * convertBall(const rcsc::BallObject & ball){
        auto res = new protos::Ball();
        res->set_allocated_position(convertVector2D(ball.pos()));
        res->set_allocated_relative_position(convertVector2D(ball.rpos()));
        res->set_allocated_seen_position(convertVector2D(ball.seenPos()));
        res->set_allocated_heard_position(convertVector2D(ball.heardPos()));
        res->set_allocated_velocity(convertVector2D(ball.vel()));
        res->set_allocated_seen_velocity(convertVector2D(ball.seenVel()));
        res->set_allocated_heard_velocity(convertVector2D(ball.heardVel()));
        res->set_pos_count(ball.posCount());
        res->set_seen_pos_count(ball.seenPosCount());
        res->set_heard_pos_count(ball.heardPosCount());
        res->set_vel_count(ball.velCount());
        res->set_seen_vel_count(ball.seenVelCount());
        res->set_heard_vel_count(ball.heardVelCount());
        res->set_lost_count(ball.lostCount());
        res->set_ghost_count(ball.ghostCount());
        res->set_dist_from_self(static_cast<float>(ball.distFromSelf()));
        res->set_angle_from_self(static_cast<float>(ball.angleFromSelf().degree()));
        return res;
    }

    static protos::Self * convertSelf(const rcsc::SelfObject & self){
        auto res = new protos::Self();
        res->set_allocated_position(convertVector2D(self.pos()));
        res->set_allocated_seen_position(convertVector2D(self.seenPos()));
        res->set_allocated_heard_position(convertVector2D(self.heardPos()));
        res->set_allocated_velocity(convertVector2D(self.vel()));
        res->set_allocated_seen_velocity(convertVector2D(self.seenVel()));
        res->set_pos_count(self.posCount());
        res->set_seen_pos_count(self.seenPosCount());
        res->set_heard_pos_count(self.heardPosCount());
        res->set_vel_count(self.velCount());
        res->set_seen_vel_count(self.seenVelCount());
        res->set_ghost_count(self.ghostCount());
        res->set_id(self.id());
        res->set_side(convertSide(self.side()));
        res->set_uniform_number(self.unum());
        res->set_uniform_number_count(self.unumCount());
        res->set_is_goalie(self.goalie());
        res->set_body_direction(static_cast<float>(self.body().degree()));
        res->set_body_direction_count(self.bodyCount());
        res->set_face_direction(static_cast<float>(self.face().degree()));
        res->set_face_direction_count(self.faceCount());
        res->set_point_to_direction(static_cast<float>(self.pointtoAngle().degree()));
        res->set_point_to_direction_count(self.pointtoCount());
        res->set_is_kicking(self.isKicking());
        res->set_dist_from_ball(static_cast<float>(self.distFromBall()));
        res->set_angle_from_ball(static_cast<float>(self.angleFromBall().degree()));
        res->set_ball_reach_steps(self.ballReachStep());
        res->set_is_tackling(self.isTackling());
        res->set_relative_neck_direction(static_cast<float>(self.neck().degree()));
        res->set_stamina(static_cast<float>(self.stamina()));
        res->set_is_kickable(self.isKickable());
        res->set_catch_probability(static_cast<float>(self.catchProbability()));
        res->set_tackle_probability(static_cast<float>(self.tackleProbability()));
        res->set_foul_probability(static_cast<float>(self.foulProbability()));
        res->set_view_width(convertViewWidth(self.viewWidth().type()));
        res->set_type_id(self.playerTypePtr()->id());
        res->set_kick_rate(self.kickRate());
        return res;
    }

    static protos::InterceptActionType convertInterceptActionType(rcsc::Intercept::ActionType actionType){
        switch (actionType) {
            case rcsc::Intercept::ActionType::OMNI_DASH:
                return protos::InterceptActionType::OMNI_DASH;
            case rcsc::Intercept::ActionType::TURN_BACK_DASH:
                return protos::InterceptActionType::TURN_BACKWARD_DASH;
            case rcsc::Intercept::ActionType::TURN_FORWARD_DASH:
                return protos::InterceptActionType::TURN_FORWARD_DASH;
            default:
                return protos::InterceptActionType::UNKNOWN_Intercept_Action_Type;
        }
    }
    static protos::InterceptTable * convertInterceptTable(const rcsc::InterceptTable & interceptTable){
        auto res = new protos::InterceptTable();
        res->set_self_reach_steps(interceptTable.selfStep());
        res->set_first_teammate_reach_steps(interceptTable.teammateStep());
        res->set_second_teammate_reach_steps(interceptTable.secondTeammateStep());
        res->set_first_opponent_reach_steps(interceptTable.opponentStep());
        res->set_second_opponent_reach_steps(interceptTable.secondOpponentStep());
        if (interceptTable.firstTeammate())
            res->set_first_teammate_id(interceptTable.firstTeammate()->id());
        if (interceptTable.secondTeammate())
            res->set_second_teammate_id(interceptTable.secondTeammate()->id());
        if (interceptTable.firstOpponent())
            res->set_first_opponent_id(interceptTable.firstOpponent()->id());
        if (interceptTable.secondOpponent())
            res->set_second_opponent_id(interceptTable.secondOpponent()->id());
        for (auto intercept : interceptTable.selfResults())
        {
            protos::InterceptInfo * info = res->add_self_intercept_info();
            info->set_action_type(convertInterceptActionType(intercept.actionType()));
            info->set_turn_steps(intercept.turnStep());
            info->set_turn_angle(static_cast<float>(intercept.turnAngle()));
            info->set_dash_steps(intercept.dashStep());
            info->set_dash_power(static_cast<float>(intercept.dashPower()));
            info->set_dash_dir(static_cast<float>(intercept.dashDir()));
            info->set_allocated_final_self_position(convertVector2D(intercept.selfPos()));
            info->set_final_ball_dist(intercept.ballDist());
            info->set_final_stamina(static_cast<float>(intercept.stamina()));
            info->set_value(static_cast<float>(intercept.value()));
        }
        return res;
    }

    static void updatePlayerObject(protos::Player * p, const rcsc::PlayerObject * player){
        p->set_allocated_position(convertVector2D(player->pos()));
        p->set_allocated_seen_position(convertVector2D(player->seenPos()));
        p->set_allocated_heard_position(convertVector2D(player->heardPos()));
        p->set_allocated_velocity(convertVector2D(player->vel()));
        p->set_allocated_seen_velocity(convertVector2D(player->seenVel()));
        p->set_pos_count(player->posCount());
        p->set_seen_pos_count(player->seenPosCount());
        p->set_heard_pos_count(player->heardPosCount());
        p->set_vel_count(player->velCount());
        p->set_seen_vel_count(player->seenVelCount());
        p->set_ghost_count(player->ghostCount());
        p->set_dist_from_self(static_cast<float>(player->distFromSelf()));
        p->set_angle_from_self(static_cast<float>(player->angleFromSelf().degree()));
        p->set_id(player->id());
        p->set_side(convertSide(player->side()));
        p->set_uniform_number(player->unum());
        p->set_uniform_number_count(player->unumCount());
        p->set_is_goalie(player->goalie());
        p->set_body_direction(static_cast<float>(player->body().degree()));
        p->set_body_direction_count(player->bodyCount());
        p->set_face_direction(static_cast<float>(player->face().degree()));
        p->set_face_direction_count(player->faceCount());
        p->set_point_to_direction(static_cast<float>(player->pointtoAngle().degree()));
        p->set_point_to_direction_count(player->pointtoCount());
        p->set_is_kicking(player->isKicking());
        p->set_dist_from_ball(static_cast<float>(player->distFromBall()));
        p->set_angle_from_ball(static_cast<float>(player->angleFromBall().degree()));
        p->set_ball_reach_steps(player->ballReachStep());
        p->set_is_tackling(player->isTackling());
        p->set_type_id(player->playerTypePtr()->id());
    }

    static void updateAbstractPlayerObject(protos::Player * p, const rcsc::AbstractPlayerObject * player){
        p->set_allocated_position(convertVector2D(player->pos()));
        p->set_allocated_seen_position(convertVector2D(player->seenPos()));
        p->set_allocated_heard_position(convertVector2D(player->heardPos()));
        p->set_allocated_velocity(convertVector2D(player->vel()));
        p->set_allocated_seen_velocity(convertVector2D(player->seenVel()));
        p->set_pos_count(player->posCount());
        p->set_seen_pos_count(player->seenPosCount());
        p->set_heard_pos_count(player->heardPosCount());
        p->set_vel_count(player->velCount());
        p->set_seen_vel_count(player->seenVelCount());
        p->set_ghost_count(player->ghostCount());
        p->set_dist_from_self(static_cast<float>(player->distFromSelf()));
        p->set_angle_from_self(static_cast<float>(player->angleFromSelf().degree()));
        p->set_id(player->id());
        p->set_side(convertSide(player->side()));
        p->set_uniform_number(player->unum());
        p->set_uniform_number_count(player->unumCount());
        p->set_is_goalie(player->goalie());
        p->set_body_direction(static_cast<float>(player->body().degree()));
        p->set_body_direction_count(player->bodyCount());
        p->set_face_direction(static_cast<float>(player->face().degree()));
        p->set_face_direction_count(player->faceCount());
        p->set_point_to_direction(static_cast<float>(player->pointtoAngle().degree()));
        p->set_point_to_direction_count(player->pointtoCount());
        p->set_is_kicking(player->isKicking());
        p->set_dist_from_ball(static_cast<float>(player->distFromBall()));
        p->set_angle_from_ball(static_cast<float>(player->angleFromBall().degree()));
        p->set_ball_reach_steps(player->ballReachStep());
        p->set_is_tackling(player->isTackling());
        p->set_type_id(player->playerTypePtr()->id());
    }

    static protos::GameModeType converGameMode(const rcsc::WorldModel & wm){
        switch (wm.gameMode().type()){
            case rcsc::GameMode::BeforeKickOff:
                return protos::GameModeType::BeforeKickOff;
            case rcsc::GameMode::TimeOver:
                return protos::GameModeType::TimeOver;
            case rcsc::GameMode::PlayOn:
                return protos::GameModeType::PlayOn;
            case rcsc::GameMode::KickOff_:
                return protos::GameModeType::KickOff_;
            case rcsc::GameMode::KickIn_:
                return protos::GameModeType::KickIn_;
            case rcsc::GameMode::FreeKick_:
                return protos::GameModeType::FreeKick_;
            case rcsc::GameMode::CornerKick_:
                return protos::GameModeType::CornerKick_;
            case rcsc::GameMode::GoalKick_:
                return protos::GameModeType::GoalKick_;
            case rcsc::GameMode::AfterGoal_:
                return protos::GameModeType::AfterGoal_;
            case rcsc::GameMode::OffSide_:
                return protos::GameModeType::OffSide_;
            case rcsc::GameMode::PenaltyKick_:
                return protos::GameModeType::PenaltyKick_;
            case rcsc::GameMode::FirstHalfOver:
                return protos::GameModeType::FirstHalfOver;
            case rcsc::GameMode::Pause:
                return protos::GameModeType::Pause;
            case rcsc::GameMode::Human:
                return protos::GameModeType::Human;
            case rcsc::GameMode::FoulCharge_:
                return protos::GameModeType::FoulCharge_;
            case rcsc::GameMode::FoulPush_:
                return protos::GameModeType::FoulPush_;
            case rcsc::GameMode::FoulMultipleAttacker_:
                return protos::GameModeType::FoulMultipleAttacker_;
            case rcsc::GameMode::FoulBallOut_:
                return protos::GameModeType::FoulBallOut_;
            case rcsc::GameMode::BackPass_:
                return protos::GameModeType::BackPass_;
            case rcsc::GameMode::FreeKickFault_:
                return protos::GameModeType::FreeKickFault_;
            case rcsc::GameMode::CatchFault_:
                return protos::GameModeType::CatchFault_;
            case rcsc::GameMode::IndFreeKick_:
                return protos::GameModeType::IndFreeKick_;
            case rcsc::GameMode::PenaltySetup_:
                return protos::GameModeType::PenaltySetup_;
            case rcsc::GameMode::PenaltyReady_:
                return protos::GameModeType::PenaltyReady_;
            case rcsc::GameMode::PenaltyTaken_:
                return protos::GameModeType::PenaltyTaken_;
            case rcsc::GameMode::PenaltyMiss_:
                return protos::GameModeType::PenaltyMiss_;
            case rcsc::GameMode::PenaltyScore_:
                return protos::GameModeType::PenaltyScore_;
            case rcsc::GameMode::IllegalDefense_:
                return protos::GameModeType::IllegalDefense_;
            case rcsc::GameMode::PenaltyOnfield_:
                return protos::GameModeType::PenaltyOnfield_;
            case rcsc::GameMode::PenaltyFoul_:
                return protos::GameModeType::PenaltyFoul_;
            case rcsc::GameMode::GoalieCatch_:
                return protos::GameModeType::GoalieCatch_;
            case rcsc::GameMode::ExtendHalf:
                return protos::GameModeType::ExtendHalf;
            case rcsc::GameMode::MODE_MAX:
                return protos::GameModeType::MODE_MAX;
        }
        return protos::GameModeType::MODE_MAX;
    }
    static protos::WorldModel * convertWorldModel(const rcsc::WorldModel & wm){

        auto * res = new WorldModel();
        res->set_allocated_intercept_table(convertInterceptTable(wm.interceptTable()));
        res->set_allocated_our_team_name(new std::string (wm.ourTeamName()));
        res->set_allocated_their_team_name(new std::string (wm.theirTeamName()));
        res->set_our_side(convertSide(wm.ourSide()));
        res->set_last_set_play_start_time(wm.lastSetPlayStartTime().cycle());
        res->set_allocated_self(convertSelf(wm.self()));
        res->set_allocated_ball(convertBall(wm.ball()));
        for(auto player : wm.teammates()){
            auto p = res->add_teammates();
            updatePlayerObject(p, player);
        }
        for(auto player : wm.opponents()){
            auto p = res->add_opponents();
            updatePlayerObject(p, player);
        }
        //unknowns
        int counter = -1;
        for(auto player : wm.ourPlayers()){
            auto map = res->mutable_our_players_dict();
            auto p = protos::Player();
            updateAbstractPlayerObject(&p, player);
            if (player->unum() > 0)
                (*map)[player->unum()] = p;
            else
                (*map)[counter--] = p;
        }
        counter = -1;
        for(auto player : wm.theirPlayers()){
            auto map = res->mutable_their_players_dict();
            auto p = protos::Player();
            updateAbstractPlayerObject(&p, player);
            if (player->unum() > 0)
                (*map)[player->unum()] = p;
            else
                (*map)[counter--] = p;
        }
        res->set_our_goalie_uniform_number(wm.ourGoalieUnum());
        res->set_their_goalie_uniform_number(wm.theirGoalieUnum());
        res->set_offside_line_x(wm.offsideLineX());
        res->set_ofside_line_x_count(wm.offsideLineCount());
        if (wm.kickableTeammate())
            res->set_kickable_teammate_id(wm.kickableTeammate()->id());
        if (wm.kickableOpponent())
            res->set_kickable_opponent_id(wm.kickableOpponent()->id());
        res->set_last_kick_side(convertSide(wm.lastKickerSide()));
        res->set_last_kicker_uniform_number(wm.lastKickerUnum());
        res->set_cycle(wm.time().cycle());
        res->set_game_mode_type(converGameMode(wm));
        res->set_left_team_score(wm.gameMode().scoreLeft());
        res->set_right_team_score(wm.gameMode().scoreRight());
        res->set_is_our_set_play(wm.gameMode().isOurSetPlay(wm.ourSide()));
        res->set_is_their_set_play(wm.gameMode().isTheirSetPlay(wm.ourSide()));
        res->set_stoped_cycle(wm.gameMode().time().stopped());
        res->set_our_team_score(wm.ourSide() == rcsc::SideID::LEFT ? wm.gameMode().scoreLeft() : wm.gameMode().scoreRight());
        res->set_their_team_score(wm.ourSide() == rcsc::SideID::LEFT ? wm.gameMode().scoreRight() : wm.gameMode().scoreLeft());
        res->set_is_penalty_kick_mode(wm.gameMode().isPenaltyKickMode());
        for (int i = 1; i < 12; i++){
            auto map = res->mutable_helios_home_positions();
            auto home_pos = Strategy::i().getPosition(i);
            auto vec_msg = protos::Vector2D();
            vec_msg.set_x(home_pos.x);
            vec_msg.set_y(home_pos.y);
            (*map)[i] = vec_msg;
        }
        return res;
    }

};