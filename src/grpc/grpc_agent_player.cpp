#include "grpc_agent_player.h"
#include "state_generator.h"
#include "player/basic_actions/body_go_to_point.h"
#include "player/basic_actions/body_smart_kick.h"
#include "player/basic_actions/bhv_before_kick_off.h"
#include "player/basic_actions/bhv_body_neck_to_ball.h"
#include "player/basic_actions/bhv_body_neck_to_point.h"
#include "player/basic_actions/bhv_emergency.h"
#include "player/basic_actions/bhv_go_to_point_look_ball.h"
#include "player/basic_actions/bhv_neck_body_to_ball.h"
#include "player/basic_actions/bhv_neck_body_to_point.h"
#include "player/basic_actions/bhv_scan_field.h"
#include "player/basic_actions/body_advance_ball.h"
#include "player/basic_actions/body_clear_ball.h"
#include "player/basic_actions/body_dribble.h"
#include "player/basic_actions/body_go_to_point_dodge.h"
#include "player/basic_actions/body_hold_ball.h"
#include "player/basic_actions/body_intercept.h"
#include "player/basic_actions/body_kick_one_step.h"
#include "player/basic_actions/body_stop_ball.h"
#include "player/basic_actions/body_stop_dash.h"
#include "player/basic_actions/body_tackle_to_point.h"
#include "player/basic_actions/body_turn_to_angle.h"
#include "player/basic_actions/body_turn_to_point.h"
#include "player/basic_actions/body_turn_to_ball.h"
#include "player/basic_actions/focus_move_to_point.h"
#include "player/basic_actions/focus_reset.h"
#include "player/basic_actions/neck_scan_field.h"
#include "player/basic_actions/neck_scan_players.h"
#include "player/basic_actions/neck_turn_to_ball_and_player.h"
#include "player/basic_actions/neck_turn_to_ball_or_scan.h"
#include "player/basic_actions/neck_turn_to_ball.h"
#include "player/basic_actions/neck_turn_to_goalie_or_scan.h"
#include "player/basic_actions/neck_turn_to_low_conf_teammate.h"
#include "player/basic_actions/neck_turn_to_player_or_scan.h"
#include "player/basic_actions/neck_turn_to_point.h"
#include "player/basic_actions/neck_turn_to_relative.h"
#include "player/basic_actions/view_change_width.h"
#include "player/basic_actions/view_normal.h"
#include "player/basic_actions/view_wide.h"
#include "player/basic_actions/view_synch.h"
#include "player/role_goalie.h"
#include "planner/bhv_strict_check_shoot.h"
#include "player/bhv_basic_move.h"
#include "player/setplay/bhv_set_play.h"
#include "player/bhv_penalty_kick.h"
#include "planner/action_generator.h"
#include "planner/field_evaluator.h"
#include "player/sample_field_evaluator.h"
#include "planner/actgen_cross.h"
#include "planner/actgen_direct_pass.h"
#include "planner/actgen_self_pass.h"
#include "planner/actgen_strict_check_pass.h"
#include "planner/actgen_short_dribble.h"
#include "planner/actgen_simple_dribble.h"
#include "planner/actgen_shoot.h"
#include "planner/actgen_action_chain_length_filter.h"
#include "planner/action_chain_holder.h"
#include "planner/bhv_planned_action.h"
#include "player/strategy.h"
#include <rcsc/player/say_message_builder.h>
#include <rcsc/common/player_param.h>

#include <chrono>
#include <rcsc/common/logger.h>
using std::chrono::duration;
using std::chrono::duration_cast;
using std::chrono::high_resolution_clock;
using std::chrono::milliseconds;

#define DEBUG

#ifdef DEBUG
#define LOG(x) std::cout << x << std::endl
#define LOGV(x) std::cout << #x << ": " << x << std::endl
#else
#define LOG(x)
#define LOGV(x)
#endif

GrpcAgentPlayer::GrpcAgentPlayer()
{
    agent_type = protos::AgentType::PlayerT;
}

void GrpcAgentPlayer::init(rcsc::PlayerAgent *agent,
                           std::string target,
                           int port,
                           bool use_same_grpc_port,
                           bool add_20_to_grpc_port_if_right_side)
{
    M_agent = agent;
    if (add_20_to_grpc_port_if_right_side)
        if (M_agent->world().ourSide() == rcsc::SideID::RIGHT)
            port += 20;

    if (!use_same_grpc_port)
    {
        port += M_agent->world().self().unum();
    }

    this->target = target + ":" + std::to_string(port);
    LOG("target: " + this->target);
    sample_communication = Communication::Ptr(new SampleCommunication());
}

void GrpcAgentPlayer::getActions() const
{
    // LOG("getAction Started");
    auto agent = M_agent;
    // LOGV(agent->world().time().cycle());
    State state = generateState();
    state.set_agent_type(protos::AgentType::PlayerT);
    protos::PlayerActions actions;
    ClientContext context;
    Status status = stub_->GetPlayerActions(&context, state, &actions);

    if (!status.ok())
    {
        std::cout << status.error_code() << ": " << status.error_message()
                  << std::endl;
        return;
    }

    LOG("getAction apply actions on agent");
    int body_action_done = 0;
    for (int i = 0; i < actions.actions_size(); i++)
    {
        auto action = actions.actions(i);
        switch (action.action_case())
        {
        case PlayerAction::kDash:
        {
            agent->doDash(action.dash().power(), action.dash().relative_direction());
            body_action_done++;
            break;
        }
        case PlayerAction::kKick:
        {
            agent->doKick(action.kick().power(), action.kick().relative_direction());
            body_action_done++;
            break;
        }
        case PlayerAction::kTurn:
        {
            agent->doTurn(action.turn().relative_direction());
            body_action_done++;
            break;
        }
        case PlayerAction::kTackle:
        {
            agent->doTackle(action.tackle().power_or_dir(), action.tackle().foul());
            body_action_done++;
            break;
        }
        case PlayerAction::kCatch:
        {
            agent->doCatch();
            body_action_done++;
            break;
        }
        case PlayerAction::kMove:
        {
            agent->doMove(action.move().x(), action.move().y());
            body_action_done++;
            break;
        }
        case PlayerAction::kTurnNeck:
        {
            agent->doTurnNeck(action.turn_neck().moment());
            break;
        }
        case PlayerAction::kChangeView:
        {
            const rcsc::ViewWidth view_width = GrpcAgent::convertViewWidth(action.change_view().view_width());
            agent->doChangeView(view_width);
            break;
        }
        case PlayerAction::kSay:
        {
            addSayMessage(action.say());
            break;
        }
        case PlayerAction::kPointTo:
        {
            agent->doPointto(action.point_to().x(), action.point_to().y());
            break;
        }
        case PlayerAction::kPointToOf:
        {
            agent->doPointtoOff();
            break;
        }
        case PlayerAction::kAttentionTo:
        {
            const rcsc::SideID side = GrpcAgent::convertSideID(action.attention_to().side());
            agent->doAttentionto(side, action.attention_to().unum());
            break;
        }
        case PlayerAction::kAttentionToOf:
        {
            agent->doAttentiontoOff();
            break;
        }
        case PlayerAction::kLog:
        {
            addDlog(action.log());
            break;
        }
        // todo debugClient
        case PlayerAction::kBodyGoToPoint:
        {
            LOG("body go to point");
            const auto &bodyGoToPoint = action.body_go_to_point();
            const auto &targetPoint = GrpcAgent::convertVector2D(bodyGoToPoint.target_point());
            LOGV(targetPoint);
            Body_GoToPoint(targetPoint, bodyGoToPoint.distance_threshold(), bodyGoToPoint.max_dash_power()).execute(agent);
            body_action_done++;
            break;
        }
        case PlayerAction::kBodySmartKick:
        {
            const auto &bodySmartKick = action.body_smart_kick();
            const auto &targetPoint = GrpcAgent::convertVector2D(bodySmartKick.target_point());
            Body_SmartKick(targetPoint, bodySmartKick.first_speed(), bodySmartKick.first_speed_threshold(), bodySmartKick.max_steps()).execute(agent);
            body_action_done++;
            break;
        }
        case PlayerAction::kBhvBeforeKickOff:
        {
            const auto &bhvBeforeKickOff = action.bhv_before_kick_off();
            const auto &point = GrpcAgent::convertVector2D(bhvBeforeKickOff.point());
            Bhv_BeforeKickOff(point).execute(agent);
            break;
        }
        case PlayerAction::kBhvBodyNeckToBall:
        {
            Bhv_BodyNeckToBall().execute(agent);
            body_action_done++;
            break;
        }
        case PlayerAction::kBhvBodyNeckToPoint:
        {
            const auto &bhvBodyNeckToPoint = action.bhv_body_neck_to_point();
            const auto &targetPoint = GrpcAgent::convertVector2D(bhvBodyNeckToPoint.point());
            Bhv_BodyNeckToPoint(targetPoint).execute(agent);
            body_action_done++;
            break;
        }
        case PlayerAction::kBhvEmergency:
        {
            Bhv_Emergency().execute(agent);
            break;
        }
        case PlayerAction::kBhvGoToPointLookBall:
        {
            const auto &bhvGoToPointLookBall = action.bhv_go_to_point_look_ball();
            const auto &targetPoint = GrpcAgent::convertVector2D(bhvGoToPointLookBall.target_point());
            Bhv_GoToPointLookBall(targetPoint, bhvGoToPointLookBall.distance_threshold(), bhvGoToPointLookBall.max_dash_power()).execute(agent);
            body_action_done++;
            break;
        }
        case PlayerAction::kBhvNeckBodyToBall:
        {
            const auto &bhvNeckBodyToBall = action.bhv_neck_body_to_ball();
            Bhv_NeckBodyToBall(bhvNeckBodyToBall.angle_buf()).execute(agent);
            break;
        }
        case PlayerAction::kBhvNeckBodyToPoint:
        {
            const auto &bhvNeckBodyToPoint = action.bhv_neck_body_to_point();
            const auto &targetPoint = GrpcAgent::convertVector2D(bhvNeckBodyToPoint.point());
            Bhv_NeckBodyToPoint(targetPoint, bhvNeckBodyToPoint.angle_buf()).execute(agent);
            break;
        }
        case PlayerAction::kBhvScanField:
        {
            Bhv_ScanField().execute(agent);
            break;
        }
        case PlayerAction::kBodyAdvanceBall:
        {
            Body_AdvanceBall().execute(agent);
            body_action_done++;
            break;
        }
        case PlayerAction::kBodyClearBall:
        {
            Body_ClearBall().execute(agent);
            body_action_done++;
            break;
        }
        case PlayerAction::kBodyDribble:
        {
            const auto &bodyDribble = action.body_dribble();
            const auto &targetPoint = GrpcAgent::convertVector2D(bodyDribble.target_point());
            Body_Dribble(
                targetPoint,
                bodyDribble.distance_threshold(),
                bodyDribble.dash_power(),
                bodyDribble.dash_count(),
                bodyDribble.dodge())
                .execute(agent);
            body_action_done++;
            break;
        }
        case PlayerAction::kBodyGoToPointDodge:
        {
            const auto &bodyGoToPointDodge = action.body_go_to_point_dodge();
            const auto &targetPoint = GrpcAgent::convertVector2D(bodyGoToPointDodge.target_point());
            Body_GoToPointDodge(
                targetPoint,
                bodyGoToPointDodge.dash_power())
                .execute(agent);
            body_action_done++;
            break;
        }
        case PlayerAction::kBodyHoldBall:
        {
            const auto &bodyHoldBall = action.body_hold_ball();
            const auto &turnTargetPoint = GrpcAgent::convertVector2D(bodyHoldBall.turn_target_point());
            const auto &kickTargetPoint = GrpcAgent::convertVector2D(bodyHoldBall.kick_target_point());
            Body_HoldBall(
                bodyHoldBall.do_turn(),
                turnTargetPoint,
                kickTargetPoint)
                .execute(agent);
            body_action_done++;
            break;
        }
        case PlayerAction::kBodyIntercept:
        {
            const auto &bodyIntercept = action.body_intercept();
            const auto &facePoint = GrpcAgent::convertVector2D(bodyIntercept.face_point());
            Body_Intercept(
                bodyIntercept.save_recovery(),
                facePoint)
                .execute(agent);
            body_action_done++;
            break;
        }
        case PlayerAction::kBodyKickOneStep:
        {
            const auto &bodyKickOneStep = action.body_kick_one_step();
            const auto &targetPoint = GrpcAgent::convertVector2D(bodyKickOneStep.target_point());
            Body_KickOneStep(
                targetPoint,
                bodyKickOneStep.first_speed(),
                bodyKickOneStep.force_mode())
                .execute(agent);
            body_action_done++;
            break;
        }
        case PlayerAction::kBodyStopBall:
        {
            Body_StopBall().execute(agent);
            body_action_done++;
            break;
        }
        case PlayerAction::kBodyStopDash:
        {
            const auto &bodyStopDash = action.body_stop_dash();
            Body_StopDash(
                bodyStopDash.save_recovery())
                .execute(agent);
            body_action_done++;
            break;
        }
        case PlayerAction::kBodyTackleToPoint:
        {
            const auto &bodyTackleToPoint = action.body_tackle_to_point();
            const auto &targetPoint = GrpcAgent::convertVector2D(bodyTackleToPoint.target_point());
            Body_TackleToPoint(
                targetPoint,
                bodyTackleToPoint.min_probability(),
                bodyTackleToPoint.min_speed())
                .execute(agent);
            body_action_done++;
            break;
        }
        case PlayerAction::kBodyTurnToAngle:
        {
            const auto &bodyTurnToAngle = action.body_turn_to_angle();
            Body_TurnToAngle(
                bodyTurnToAngle.angle())
                .execute(agent);
            body_action_done++;
            break;
        }
        case PlayerAction::kBodyTurnToBall:
        {
            const auto &bodyTurnToBall = action.body_turn_to_ball();
            Body_TurnToBall(
                bodyTurnToBall.cycle())
                .execute(agent);
            body_action_done++;
            break;
        }
        case PlayerAction::kBodyTurnToPoint:
        {
            const auto &bodyTurnToPoint = action.body_turn_to_point();
            const auto &targetPoint = GrpcAgent::convertVector2D(bodyTurnToPoint.target_point());
            Body_TurnToPoint(
                targetPoint,
                bodyTurnToPoint.cycle())
                .execute(agent);
            body_action_done++;
            break;
        }
        case PlayerAction::kFocusMoveToPoint:
        {
            const auto &focusMoveToPoint = action.focus_move_to_point();
            const auto &targetPoint = GrpcAgent::convertVector2D(focusMoveToPoint.target_point());
            rcsc::Focus_MoveToPoint(
                targetPoint)
                .execute(agent);
            break;
        }
        case PlayerAction::kFocusReset:
        {
            rcsc::Focus_Reset().execute(agent);
            break;
        }
        case PlayerAction::kNeckScanField:
        {
            Neck_ScanField().execute(agent);
            break;
        }
        case PlayerAction::kNeckScanPlayers:
        {
            Neck_ScanPlayers().execute(agent);
            break;
        }
        case PlayerAction::kNeckTurnToBallAndPlayer:
        {
            const auto &neckTurnToBallAndPlayer = action.neck_turn_to_ball_and_player();
            const rcsc::AbstractPlayerObject *player = nullptr;
            if (neckTurnToBallAndPlayer.side() == protos::Side::LEFT && agent->world().ourSide() == rcsc::SideID::LEFT)
            {
                player = agent->world().ourPlayer(neckTurnToBallAndPlayer.uniform_number());
            }
            else
            {
                player = agent->world().theirPlayer(neckTurnToBallAndPlayer.uniform_number());
            }
            if (player != nullptr)
            {
                Neck_TurnToBallAndPlayer(
                    player,
                    neckTurnToBallAndPlayer.count_threshold())
                    .execute(agent);
            }
            break;
        }
        case PlayerAction::kNeckTurnToBallOrScan:
        {
            const auto &neckTurnToBallOrScan = action.neck_turn_to_ball_or_scan();
            Neck_TurnToBallOrScan(
                neckTurnToBallOrScan.count_threshold())
                .execute(agent);
            break;
        }
        case PlayerAction::kNeckTurnToBall:
        {
            Neck_TurnToBall().execute(agent);
            break;
        }
        case PlayerAction::kNeckTurnToGoalieOrScan:
        {
            const auto &neckTurnToGoalieOrScan = action.neck_turn_to_goalie_or_scan();
            Neck_TurnToGoalieOrScan(
                neckTurnToGoalieOrScan.count_threshold())
                .execute(agent);
            break;
        }
        case PlayerAction::kNeckTurnToLowConfTeammate:
        {
            const auto &neckTurnToLowConfTeammate = action.neck_turn_to_low_conf_teammate();
            Neck_TurnToLowConfTeammate().execute(agent);
            break;
        }
        case PlayerAction::kNeckTurnToPlayerOrScan:
        {
            const auto &neckTurnToPlayerOrScan = action.neck_turn_to_player_or_scan();
            const rcsc::AbstractPlayerObject *player = nullptr;
            if (neckTurnToPlayerOrScan.side() == protos::Side::LEFT && agent->world().ourSide() == rcsc::SideID::LEFT)
            {
                player = agent->world().ourPlayer(neckTurnToPlayerOrScan.uniform_number());
            }
            else
            {
                player = agent->world().theirPlayer(neckTurnToPlayerOrScan.uniform_number());
            }
            if (player != nullptr)
            {
                Neck_TurnToPlayerOrScan(
                    player,
                    neckTurnToPlayerOrScan.count_threshold())
                    .execute(agent);
            }
            break;
        }
        case PlayerAction::kNeckTurnToPoint:
        {
            const auto &neckTurnToPoint = action.neck_turn_to_point();
            const auto &targetPoint = GrpcAgent::convertVector2D(neckTurnToPoint.target_point());
            Neck_TurnToPoint(
                targetPoint)
                .execute(agent);
            break;
        }
        case PlayerAction::kNeckTurnToRelative:
        {
            const auto &neckTurnToRelative = action.neck_turn_to_relative();
            Neck_TurnToRelative(
                neckTurnToRelative.angle())
                .execute(agent);
            break;
        }
        case PlayerAction::kViewChangeWidth:
        {
            const auto &viewChangeWidth = action.view_change_width();
            const rcsc::ViewWidth view_width = GrpcAgent::convertViewWidth(viewChangeWidth.view_width());
            View_ChangeWidth(
                view_width)
                .execute(agent);
            break;
        }
        case PlayerAction::kViewNormal:
        {
            View_Normal().execute(agent);
            break;
        }
        case PlayerAction::kViewWide:
        {
            View_Wide().execute(agent);
            break;
        }
        case PlayerAction::kViewSynch:
        {
            View_Synch().execute(agent);
            break;
        }
        case PlayerAction::kHeliosGoalie:
        {
            RoleGoalie roleGoalie = RoleGoalie();
            roleGoalie.execute(agent);
            break;
        }
        case PlayerAction::kHeliosGoalieMove:
        {
            RoleGoalie roleGoalie = RoleGoalie();
            roleGoalie.doMove(agent);
            break;
        }
        case PlayerAction::kHeliosGoalieKick:
        {
            RoleGoalie roleGoalie = RoleGoalie();
            roleGoalie.doKick(agent);
            break;
        }
        case PlayerAction::kHeliosShoot:
        {
            const rcsc::WorldModel &wm = agent->world();

            if (wm.gameMode().type() != rcsc::GameMode::IndFreeKick_ && wm.time().stopped() == 0 && wm.self().isKickable() && Bhv_StrictCheckShoot().execute(agent))
            {
            }
            break;
        }
        case PlayerAction::kHeliosBasicMove:
        {
            Bhv_BasicMove().execute(agent);
            break;
        }
        case PlayerAction::kHeliosSetPlay:
        {
            Bhv_SetPlay().execute(agent);
            break;
        }
        case PlayerAction::kHeliosPenalty:
        {
            Bhv_PenaltyKick().execute(agent);
            break;
        }
        case PlayerAction::kHeliosCommunication:
        {
            sample_communication->execute(agent);
            break;
        }
        case PlayerAction::kHeliosChainAction:
        {
            FieldEvaluator::ConstPtr field_evaluator = FieldEvaluator::ConstPtr(new SampleFieldEvaluator);
            CompositeActionGenerator *g = new CompositeActionGenerator();

            if (action.helios_chain_action().lead_pass() || action.helios_chain_action().direct_pass() || action.helios_chain_action().through_pass())
                g->addGenerator(new ActGen_MaxActionChainLengthFilter(new ActGen_StrictCheckPass(), 1));
            if (action.helios_chain_action().cross())
                g->addGenerator(new ActGen_MaxActionChainLengthFilter(new ActGen_Cross(), 1));
            if (action.helios_chain_action().simple_pass())
                g->addGenerator(new ActGen_RangeActionChainLengthFilter(new ActGen_DirectPass(),
                                                                        2, ActGen_RangeActionChainLengthFilter::MAX));
            if (action.helios_chain_action().short_dribble())
                g->addGenerator(new ActGen_MaxActionChainLengthFilter(new ActGen_ShortDribble(), 1));
            if (action.helios_chain_action().long_dribble())
                g->addGenerator(new ActGen_MaxActionChainLengthFilter(new ActGen_SelfPass(), 1));
            if (action.helios_chain_action().simple_dribble())
                g->addGenerator(new ActGen_RangeActionChainLengthFilter(new ActGen_SimpleDribble(),
                                                                        2, ActGen_RangeActionChainLengthFilter::MAX));
            if (action.helios_chain_action().simple_shoot())
                g->addGenerator(new ActGen_RangeActionChainLengthFilter(new ActGen_Shoot(),
                                                                        2, ActGen_RangeActionChainLengthFilter::MAX));
            if (g->M_generators.empty())
            {
                Body_HoldBall().execute(agent);
                agent->setNeckAction(new Neck_ScanField());
                break;
            }
            ActionGenerator::ConstPtr action_generator = ActionGenerator::ConstPtr(g);
            ActionChainHolder::instance().setFieldEvaluator(field_evaluator);
            ActionChainHolder::instance().setActionGenerator(action_generator);
            ActionChainHolder::instance().update(agent->world());
            if (Bhv_PlannedAction().execute(agent))
            {
                agent->debugClient().addMessage("PlannedAction");
                break;
            }

            Body_HoldBall().execute(agent);
            agent->setNeckAction(new Neck_ScanField());
            break;
        }

            //                HeliosChainAction helios_chain_action = 59;
        default:
        {
            LOG("unknown action");
            break;
        }
        }
        LOG("getAction done");
    }
}

void GrpcAgentPlayer::addSayMessage(protos::Say sayMessage) const
{
    auto agent = M_agent;
    switch (sayMessage.message_case())
    {
    case protos::Say::kBallMessage:
    {
        const auto &ballMessage = sayMessage.ball_message();
        const auto &ballPosition = GrpcAgent::convertVector2D(ballMessage.ball_position());
        const auto &ballVelocity = GrpcAgent::convertVector2D(ballMessage.ball_velocity());
        agent->addSayMessage(new rcsc::BallMessage(ballPosition, ballVelocity));
        break;
    }
    case protos::Say::kPassMessage:
    {
        const auto &passMessage = sayMessage.pass_message();
        const auto &receiverPoint = GrpcAgent::convertVector2D(passMessage.receiver_point());
        const auto &ballPosition = GrpcAgent::convertVector2D(passMessage.ball_position());
        const auto &ballVelocity = GrpcAgent::convertVector2D(passMessage.ball_velocity());
        agent->addSayMessage(new rcsc::PassMessage(passMessage.receiver_uniform_number(),
                                                   receiverPoint,
                                                   ballPosition,
                                                   ballVelocity));
        break;
    }
    case protos::Say::kInterceptMessage:
    {
        const auto &interceptMessage = sayMessage.intercept_message();
        agent->addSayMessage(new rcsc::InterceptMessage(interceptMessage.our(),
                                                        interceptMessage.uniform_number(),
                                                        interceptMessage.cycle()));
        break;
    }
    case protos::Say::kGoalieMessage:
    {
        const auto &goalieMessage = sayMessage.goalie_message();
        const auto &goaliePosition = GrpcAgent::convertVector2D(goalieMessage.goalie_position());
        agent->addSayMessage(new rcsc::GoalieMessage(goalieMessage.goalie_uniform_number(),
                                                     goaliePosition,
                                                     goalieMessage.goalie_body_direction()));
        break;
    }
    case protos::Say::kGoalieAndPlayerMessage:
    {
        const auto &goalieAndPlayerMessage = sayMessage.goalie_and_player_message();
        const auto &goaliePosition = GrpcAgent::convertVector2D(goalieAndPlayerMessage.goalie_position());
        const auto &playerPosition = GrpcAgent::convertVector2D(goalieAndPlayerMessage.player_position());
        agent->addSayMessage(new rcsc::GoalieAndPlayerMessage(goalieAndPlayerMessage.goalie_uniform_number(),
                                                              goaliePosition,
                                                              goalieAndPlayerMessage.goalie_body_direction(),
                                                              goalieAndPlayerMessage.player_uniform_number(),
                                                              playerPosition));
        break;
    }
    case protos::Say::kOffsideLineMessage:
    {
        const auto &offsideLineMessage = sayMessage.offside_line_message();
        agent->addSayMessage(new rcsc::OffsideLineMessage(offsideLineMessage.offside_line_x()));
        break;
    }
    case protos::Say::kDefenseLineMessage:
    {
        const auto &defenseLineMessage = sayMessage.defense_line_message();
        agent->addSayMessage(new rcsc::DefenseLineMessage(defenseLineMessage.defense_line_x()));
        break;
    }
    case protos::Say::kWaitRequestMessage:
    {
        const auto &waitRequestMessage = sayMessage.wait_request_message();
        agent->addSayMessage(new rcsc::WaitRequestMessage());
        break;
    }
    case protos::Say::kSetplayMessage:
    {
        const auto &setplayMessage = sayMessage.setplay_message();
        agent->addSayMessage(new rcsc::SetplayMessage(setplayMessage.wait_step()));
        break;
    }
    case protos::Say::kPassRequestMessage:
    {
        const auto &passRequestMessage = sayMessage.pass_request_message();
        const auto &targetPoint = GrpcAgent::convertVector2D(passRequestMessage.target_point());
        agent->addSayMessage(new rcsc::PassRequestMessage(targetPoint));
        break;
    }
    case protos::Say::kStaminaMessage:
    {
        const auto &staminaMessage = sayMessage.stamina_message();
        agent->addSayMessage(new rcsc::StaminaMessage(staminaMessage.stamina()));
        break;
    }
    case protos::Say::kRecoveryMessage:
    {
        const auto &recoveryMessage = sayMessage.recovery_message();
        agent->addSayMessage(new rcsc::RecoveryMessage(recoveryMessage.recovery()));
        break;
    }
    case protos::Say::kStaminaCapacityMessage:
    {
        const auto &staminaCapacityMessage = sayMessage.stamina_capacity_message();
        agent->addSayMessage(new rcsc::StaminaCapacityMessage(staminaCapacityMessage.stamina_capacity()));
        break;
    }
    case protos::Say::kDribbleMessage:
    {
        const auto &dribbleMessage = sayMessage.dribble_message();
        const auto &targetPoint = GrpcAgent::convertVector2D(dribbleMessage.target_point());
        agent->addSayMessage(new rcsc::DribbleMessage(targetPoint, dribbleMessage.queue_count()));
        break;
    }
    case protos::Say::kBallGoalieMessage:
    {
        const auto &ballGoalieMessage = sayMessage.ball_goalie_message();
        const auto &ballPosition = GrpcAgent::convertVector2D(ballGoalieMessage.ball_position());
        const auto &ballVelocity = GrpcAgent::convertVector2D(ballGoalieMessage.ball_velocity());
        const auto &goaliePosition = GrpcAgent::convertVector2D(ballGoalieMessage.goalie_position());
        agent->addSayMessage(new rcsc::BallGoalieMessage(ballPosition, ballVelocity, goaliePosition, ballGoalieMessage.goalie_body_direction()));
        break;
    }
    case protos::Say::kOnePlayerMessage:
    {
        const auto &onePlayerMessage = sayMessage.one_player_message();
        const auto &playerPosition = GrpcAgent::convertVector2D(onePlayerMessage.position());
        agent->addSayMessage(new rcsc::OnePlayerMessage(onePlayerMessage.uniform_number(), playerPosition));
        break;
    }
    case protos::Say::kTwoPlayerMessage:
    {
        const auto &twoPlayersMessage = sayMessage.two_player_message();
        const auto &player1Position = GrpcAgent::convertVector2D(twoPlayersMessage.first_position());
        const auto &player2Position = GrpcAgent::convertVector2D(twoPlayersMessage.second_position());
        agent->addSayMessage(new rcsc::TwoPlayerMessage(twoPlayersMessage.first_uniform_number(),
                                                        player1Position,
                                                        twoPlayersMessage.second_uniform_number(),
                                                        player2Position));
        break;
    }
    case protos::Say::kThreePlayerMessage:
    {
        const auto &threePlayersMessage = sayMessage.three_player_message();
        const auto &player1Position = GrpcAgent::convertVector2D(threePlayersMessage.first_position());
        const auto &player2Position = GrpcAgent::convertVector2D(threePlayersMessage.second_position());
        const auto &player3Position = GrpcAgent::convertVector2D(threePlayersMessage.third_position());
        agent->addSayMessage(new rcsc::ThreePlayerMessage(threePlayersMessage.first_uniform_number(),
                                                          player1Position,
                                                          threePlayersMessage.second_uniform_number(),
                                                          player2Position,
                                                          threePlayersMessage.third_uniform_number(),
                                                          player3Position));
        break;
    }
    case protos::Say::kSelfMessage:
    {
        const auto &selfMessage = sayMessage.self_message();
        const auto &selfPosition = GrpcAgent::convertVector2D(selfMessage.self_position());
        agent->addSayMessage(new rcsc::SelfMessage(selfPosition, selfMessage.self_body_direction(), selfMessage.self_stamina()));
        break;
    }
    case protos::Say::kTeammateMessage:
    {
        const auto &teammateMessage = sayMessage.teammate_message();
        const auto &teammatePosition = GrpcAgent::convertVector2D(teammateMessage.position());
        agent->addSayMessage(new rcsc::TeammateMessage(teammateMessage.uniform_number(), teammatePosition, teammateMessage.body_direction()));
        break;
    }
    case protos::Say::kOpponentMessage:
    {
        const auto &opponentMessage = sayMessage.opponent_message();
        const auto &opponentPosition = GrpcAgent::convertVector2D(opponentMessage.position());
        agent->addSayMessage(new rcsc::OpponentMessage(opponentMessage.uniform_number(), opponentPosition, opponentMessage.body_direction()));
        break;
    }
    case protos::Say::kBallPlayerMessage:
    {
        const auto &ballPlayerMessage = sayMessage.ball_player_message();
        const auto &ballPosition = GrpcAgent::convertVector2D(ballPlayerMessage.ball_position());
        const auto &ballVelocity = GrpcAgent::convertVector2D(ballPlayerMessage.ball_velocity());
        const auto &playerPosition = GrpcAgent::convertVector2D(ballPlayerMessage.player_position());
        agent->addSayMessage(new rcsc::BallPlayerMessage(ballPosition, ballVelocity, ballPlayerMessage.uniform_number(), playerPosition, ballPlayerMessage.body_direction()));
        break;
    }
    default:
    {
        std::cout << "GrpcAgent: unknown say message" << std::endl;
        break;
    }
    }
}

State GrpcAgentPlayer::generateState() const
{
    const rcsc::WorldModel &wm = M_agent->world();
    WorldModel *worldModel = StateGenerator::convertWorldModel(wm);
    addHomePosition(worldModel);
    State state;
    state.set_allocated_world_model(worldModel);
    return state;
}

void GrpcAgentPlayer::addHomePosition(protos::WorldModel *res) const
{
    for (int i = 1; i < 12; i++)
    {
        auto map = res->mutable_helios_home_positions();
        auto home_pos = Strategy::i().getPosition(i);
        auto vec_msg = protos::Vector2D();
        vec_msg.set_x(home_pos.x);
        vec_msg.set_y(home_pos.y);
        (*map)[i] = vec_msg;
    }
}
