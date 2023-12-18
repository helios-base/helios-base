#include "grpc_agent.h"
#include "state_generator.h"
#include "action_convertor.h"
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

#include <rcsc/player/say_message_builder.h>

#include <chrono>
#include <rcsc/common/logger.h>
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
    if (!status.ok()) {
        std::cout << status.error_code() << ": " << status.error_message()
                  << std::endl;
        return;
    } 


    int body_action_done = 0;
    for(int i = 0; i < actions.actions_size(); i++){
        auto action = actions.actions(i);
        switch (action.action_case())
        {
        case Action::kDash:
        {
            agent->doDash(action.dash().power(), action.dash().relative_direction());
            body_action_done++;
            break;
        }
        case Action::kKick:
        {
            agent->doKick(action.kick().power(), action.kick().relative_direction());
            body_action_done++;
            break;
        }
        case Action::kTurn:
        {
            agent->doTurn(action.turn().relative_direction());
            body_action_done++;
            break;
        }
        case Action::kTackle:
        {
            agent->doTackle(action.tackle().power_or_dir(), action.tackle().foul());
            body_action_done++;
            break;
        }
        case Action::kCatch:
        {
            agent->doCatch();
            body_action_done++;
            break;
        }
        case Action::kMove:
        {
            agent->doMove(action.move().x(), action.move().y());
            body_action_done++;
            break;
        }
        case Action::kTurnNeck:{
            agent->doTurnNeck(action.turn_neck().moment());
            break;
        }
        case Action::kChangeView:
        {
            const rcsc::ViewWidth view_width = GrpcAgent::convertViewWidth(action.change_view().view_width());
            agent->doChangeView(view_width);
            break;
        }
        case Action::kSay:
        {
            addSayMessage(agent, action.say());
            break;
        }
        case Action::kPointTo:
        {
            agent->doPointto(action.point_to().x(), action.point_to().y());
            break;
        }
        case Action::kPointToOf:
        {
            agent->doPointtoOff();
            break;
        }
        case Action::kAttentionTo:
        {
            const rcsc::SideID side = GrpcAgent::convertSideID(action.attention_to().side());
            agent->doAttentionto(side, action.attention_to().unum());
            break;
        }
        case Action::kAttentionToOf:
        {
            agent->doAttentiontoOff();
            break;
        }
        case Action::kLog:
        {
            addDlog(action.log());
            break;
        }
        // todo debugClient
        case Action::kBodyGoToPoint:
        {
            const auto& bodyGoToPoint = action.body_go_to_point();
            const auto& targetPoint = GrpcAgent::convertVector2D(bodyGoToPoint.target_point());
            Body_GoToPoint(targetPoint, bodyGoToPoint.distance_threshold(), bodyGoToPoint.max_dash_power()).execute(agent);
            body_action_done++;
            break;
        }
        case Action::kBodySmartKick:
        {
            const auto& bodySmartKick = action.body_smart_kick();
            const auto& targetPoint = GrpcAgent::convertVector2D(bodySmartKick.target_point());
            Body_SmartKick(targetPoint, bodySmartKick.first_speed(), bodySmartKick.first_speed_threshold(), bodySmartKick.max_steps()).execute(agent);
            body_action_done++;
            break;
        }
        case Action::kBhvBeforeKickOff:
        {
            const auto& bhvBeforeKickOff = action.bhv_before_kick_off();
            const auto& point = GrpcAgent::convertVector2D(bhvBeforeKickOff.point());
            Bhv_BeforeKickOff(point).execute(agent);
            break;
        }
        case Action::kBhvBodyNeckToBall:
        {
            Bhv_BodyNeckToBall().execute(agent);
            body_action_done++;
            break;
        }
        case Action::kBhvBodyNeckToPoint:
        {
            const auto& bhvBodyNeckToPoint = action.bhv_body_neck_to_point();
            const auto& targetPoint = GrpcAgent::convertVector2D(bhvBodyNeckToPoint.point());
            Bhv_BodyNeckToPoint(targetPoint).execute(agent);
            body_action_done++;
            break;
        }
        case Action::kBhvEmergency:
        {
            Bhv_Emergency().execute(agent);
            break;
        }
        case Action::kBhvGoToPointLookBall:
        {
            const auto& bhvGoToPointLookBall = action.bhv_go_to_point_look_ball();
            const auto& targetPoint = GrpcAgent::convertVector2D(bhvGoToPointLookBall.target_point());
            Bhv_GoToPointLookBall(targetPoint, bhvGoToPointLookBall.distance_threshold(), bhvGoToPointLookBall.max_dash_power()).execute(agent);
            body_action_done++;
            break;
        }
        case Action::kBhvNeckBodyToBall:
        {
            const auto& bhvNeckBodyToBall = action.bhv_neck_body_to_ball();
            Bhv_NeckBodyToBall(bhvNeckBodyToBall.angle_buf()).execute(agent);
            break;
        }
        case Action::kBhvNeckBodyToPoint:
        {
            const auto& bhvNeckBodyToPoint = action.bhv_neck_body_to_point();
            const auto& targetPoint = GrpcAgent::convertVector2D(bhvNeckBodyToPoint.point());
            Bhv_NeckBodyToPoint(targetPoint, bhvNeckBodyToPoint.angle_buf()).execute(agent);
            break;
        }
        case Action::kBhvScanField:
        {
            Bhv_ScanField().execute(agent);
            break;
        }
        case Action::kBodyAdvanceBall:
        {
            Body_AdvanceBall().execute(agent);
            body_action_done++;
            break;
        }
        case Action::kBodyClearBall:
        {
            Body_ClearBall().execute(agent);
            body_action_done++;
            break;
        }
        case Action::kBodyDribble:
        {
            const auto& bodyDribble = action.body_dribble();
            const auto& targetPoint = GrpcAgent::convertVector2D(bodyDribble.target_point());
            Body_Dribble(
                targetPoint,
                bodyDribble.distance_threshold(),
                bodyDribble.dash_power(),
                bodyDribble.dash_count(),
                bodyDribble.dodge()
            ).execute(agent);
            body_action_done++;
            break;
        }
        case Action::kBodyGoToPointDodge:
        {
            const auto& bodyGoToPointDodge = action.body_go_to_point_dodge();
            const auto& targetPoint = GrpcAgent::convertVector2D(bodyGoToPointDodge.target_point());
            Body_GoToPointDodge(
                targetPoint,
                bodyGoToPointDodge.dash_power()
            ).execute(agent);
            body_action_done++;
            break;
        }
        case Action::kBodyHoldBall:
        {
            const auto& bodyHoldBall = action.body_hold_ball();
            const auto& turnTargetPoint = GrpcAgent::convertVector2D(bodyHoldBall.turn_target_point());
            const auto& kickTargetPoint = GrpcAgent::convertVector2D(bodyHoldBall.kick_target_point());
            Body_HoldBall(
                bodyHoldBall.do_turn(),
                turnTargetPoint,
                kickTargetPoint
            ).execute(agent);
            body_action_done++;
            break;
        }
        case Action::kBodyIntercept:
        {
            const auto& bodyIntercept = action.body_intercept();
            const auto& facePoint = GrpcAgent::convertVector2D(bodyIntercept.face_point());
            Body_Intercept(
                bodyIntercept.save_recovery(),
                facePoint
            ).execute(agent);
            body_action_done++;
            break;
        }
        case Action::kBodyKickOneStep:
        {
            const auto& bodyKickOneStep = action.body_kick_one_step();
            const auto& targetPoint = GrpcAgent::convertVector2D(bodyKickOneStep.target_point());
            Body_KickOneStep(
                targetPoint,
                bodyKickOneStep.first_speed(),
                bodyKickOneStep.force_mode()
            ).execute(agent);
            body_action_done++;
            break;
        }
        case Action::kBodyStopBall:
        {
            Body_StopBall().execute(agent);
            body_action_done++;
            break;
        }
        case Action::kBodyStopDash:
        {
            const auto& bodyStopDash = action.body_stop_dash();
            Body_StopDash(
                bodyStopDash.save_recovery()
            ).execute(agent);
            body_action_done++;
            break;
        }
        case Action::kBodyTackleToPoint:
        {
            const auto& bodyTackleToPoint = action.body_tackle_to_point();
            const auto& targetPoint = GrpcAgent::convertVector2D(bodyTackleToPoint.target_point());
            Body_TackleToPoint(
                targetPoint,
                bodyTackleToPoint.min_probability(),
                bodyTackleToPoint.min_speed()
            ).execute(agent);
            body_action_done++;
            break;
        }
        case Action::kBodyTurnToAngle:
        {
            const auto& bodyTurnToAngle = action.body_turn_to_angle();
            Body_TurnToAngle(
                bodyTurnToAngle.angle()
            ).execute(agent);
            body_action_done++;
            break;
        }
        case Action::kBodyTurnToBall:
        {
            const auto& bodyTurnToBall = action.body_turn_to_ball();
            Body_TurnToBall(
                bodyTurnToBall.cycle()
            ).execute(agent);
            body_action_done++;
            break;
        }
        case Action::kBodyTurnToPoint:
        {
            const auto& bodyTurnToPoint = action.body_turn_to_point();
            const auto& targetPoint = GrpcAgent::convertVector2D(bodyTurnToPoint.target_point());
            Body_TurnToPoint(
                targetPoint,
                bodyTurnToPoint.cycle()
            ).execute(agent);
            body_action_done++;
            break;
        }
        case Action::kFocusMoveToPoint:
        {
            const auto& focusMoveToPoint = action.focus_move_to_point();
            const auto& targetPoint = GrpcAgent::convertVector2D(focusMoveToPoint.target_point());
            rcsc::Focus_MoveToPoint(
                targetPoint
            ).execute(agent);
            break;
        }
        case Action::kFocusReset:
        {
            rcsc::Focus_Reset().execute(agent);
            break;
        }
        case Action::kNeckScanField:
        {
            Neck_ScanField().execute(agent);
            break;
        }
        case Action::kNeckScanPlayers:
        {
            Neck_ScanPlayers().execute(agent);
            break;
        }
        case Action::kNeckTurnToBallAndPlayer:
        {
            const auto& neckTurnToBallAndPlayer = action.neck_turn_to_ball_and_player();
            const rcsc::AbstractPlayerObject* player = nullptr;
            if (neckTurnToBallAndPlayer.side() == protos::Side::LEFT && agent->world().ourSide() == rcsc::SideID::LEFT){
                player = agent->world().ourPlayer(neckTurnToBallAndPlayer.uniform_number());
            } else {
                player = agent->world().theirPlayer(neckTurnToBallAndPlayer.uniform_number());
            }
            if (player != nullptr){
                Neck_TurnToBallAndPlayer(
                    player,
                    neckTurnToBallAndPlayer.count_threshold()
                ).execute(agent);
            }
            break;
        }
        case Action::kNeckTurnToBallOrScan:
        {
            const auto& neckTurnToBallOrScan = action.neck_turn_to_ball_or_scan();
            Neck_TurnToBallOrScan(
                neckTurnToBallOrScan.count_threshold()
            ).execute(agent);
            break;
        }
        case Action::kNeckTurnToBall:
        {
            Neck_TurnToBall().execute(agent);
            break;
        }
        case Action::kNeckTurnToGoalieOrScan:
        {
            const auto& neckTurnToGoalieOrScan = action.neck_turn_to_goalie_or_scan();
            Neck_TurnToGoalieOrScan(
                neckTurnToGoalieOrScan.count_threshold()
            ).execute(agent);
            break;
        }
        case Action::kNeckTurnToLowConfTeammate:
        {
            const auto& neckTurnToLowConfTeammate = action.neck_turn_to_low_conf_teammate();
            Neck_TurnToLowConfTeammate().execute(agent);
            break;
        }
        case Action::kNeckTurnToPlayerOrScan:
        {
            const auto& neckTurnToPlayerOrScan = action.neck_turn_to_player_or_scan();
            const rcsc::AbstractPlayerObject* player = nullptr;
            if (neckTurnToPlayerOrScan.side() == protos::Side::LEFT && agent->world().ourSide() == rcsc::SideID::LEFT){
                player = agent->world().ourPlayer(neckTurnToPlayerOrScan.uniform_number());
            } else {
                player = agent->world().theirPlayer(neckTurnToPlayerOrScan.uniform_number());
            }
            if (player != nullptr){
                Neck_TurnToPlayerOrScan(
                    player,
                    neckTurnToPlayerOrScan.count_threshold()
                ).execute(agent);
            }
            break;
        }
        case Action::kNeckTurnToPoint:
        {
            const auto& neckTurnToPoint = action.neck_turn_to_point();
            const auto& targetPoint = GrpcAgent::convertVector2D(neckTurnToPoint.target_point());
            Neck_TurnToPoint(
                targetPoint
            ).execute(agent);
            break;
        }
        case Action::kNeckTurnToRelative:
        {
            const auto& neckTurnToRelative = action.neck_turn_to_relative();
            Neck_TurnToRelative(
                neckTurnToRelative.angle()
            ).execute(agent);
            break;
        }
        case Action::kViewChangeWidth:
        {
            const auto& viewChangeWidth = action.view_change_width();
            const rcsc::ViewWidth view_width = GrpcAgent::convertViewWidth(viewChangeWidth.view_width());
            View_ChangeWidth(
                view_width
            ).execute(agent);
            break;
        }
        case Action::kViewNormal:
        {
            View_Normal().execute(agent);
            break;
        }
        case Action::kViewWide:
        {
            View_Wide().execute(agent);
            break;
        }
        case Action::kViewSynch:
        {
            View_Synch().execute(agent);
            break;
        }
        default:
        {
            break;
        }

        }
    }
}

void GrpcAgent::addDlog(protos::Log log) const{
    switch (log.log_case())
    {
        case protos::Log::kAddText:
        {
            const auto& addText = log.add_text();
            rcsc::dlog.addText(addText.level(), addText.message().c_str());
            break;
        }
        case protos::Log::kAddPoint:
        {
            const auto& addPoint = log.add_point();
            const auto& point = GrpcAgent::convertVector2D(addPoint.point());
            rcsc::dlog.addPoint(addPoint.level(), point, addPoint.color().c_str());
            break;
        }
        case protos::Log::kAddLine:
        {
            const auto& addLine = log.add_line();
            const auto& point1 = GrpcAgent::convertVector2D(addLine.start());
            const auto& point2 = GrpcAgent::convertVector2D(addLine.end());
            rcsc::dlog.addLine(addLine.level(), point1, point2, addLine.color().c_str());
            break;
        }
        case protos::Log::kAddArc:
        {
            const auto& addArc = log.add_arc();
            const auto& center = GrpcAgent::convertVector2D(addArc.center());
            rcsc::dlog.addArc(addArc.level(), center, addArc.radius(), addArc.start_angle(), addArc.span_angel(), addArc.color().c_str());
            break;
        }
        case protos::Log::kAddCircle:
        {
            const auto& addCircle = log.add_circle();
            const auto& center = GrpcAgent::convertVector2D(addCircle.center());
            rcsc::dlog.addCircle(addCircle.level(), center, addCircle.radius(), addCircle.color().c_str(), addCircle.fill());
            break;
        }
        case protos::Log::kAddTriangle:
        {
            const auto& addTriangle = log.add_triangle();
            const auto& point1 = GrpcAgent::convertVector2D(addTriangle.point1());
            const auto& point2 = GrpcAgent::convertVector2D(addTriangle.point2());
            const auto& point3 = GrpcAgent::convertVector2D(addTriangle.point3());
            rcsc::dlog.addTriangle(addTriangle.level(), point1, point2, point3, addTriangle.color().c_str(), addTriangle.fill());
            break;
        }
        case protos::Log::kAddRectangle:
        {
            const auto& addRectangle = log.add_rectangle();
            rcsc::dlog.addRect(addRectangle.level(), addRectangle.left(), addRectangle.top(),addRectangle.length(), addRectangle.width(), addRectangle.color().c_str(), addRectangle.fill());
            break;
        }
        case protos::Log::kAddSector:
        {
            const auto& addSector = log.add_sector();
            const auto& center = GrpcAgent::convertVector2D(addSector.center());
            rcsc::dlog.addSector(addSector.level(), center, addSector.min_radius(), addSector.max_radius(), addSector.start_angle(), addSector.span_angel(), addSector.color().c_str(), addSector.fill());
            break;
        }
        case protos::Log::kAddMessage:
        {
            const auto& addMessage = log.add_message();
            const auto& position = GrpcAgent::convertVector2D(addMessage.position());
            rcsc::dlog.addMessage(addMessage.level(), position, addMessage.message().c_str(), addMessage.color().c_str());
            break;
        }

    }
}

void GrpcAgent::addSayMessage(rcsc::PlayerAgent * agent, protos::Say sayMessage) const {
    switch (sayMessage.message_case())
    {
        case protos::Say::kBallMessage:
        {
            const auto& ballMessage = sayMessage.ball_message();
            const auto& ballPosition = GrpcAgent::convertVector2D(ballMessage.ball_position());
            const auto& ballVelocity = GrpcAgent::convertVector2D(ballMessage.ball_velocity());
            agent->addSayMessage(new rcsc::BallMessage(ballPosition, ballVelocity));
            break;
        }
        case protos::Say::kPassMessage:
        {
            const auto& passMessage = sayMessage.pass_message();
            const auto& receiverPoint = GrpcAgent::convertVector2D(passMessage.receiver_point());
            const auto& ballPosition = GrpcAgent::convertVector2D(passMessage.ball_position());
            const auto& ballVelocity = GrpcAgent::convertVector2D(passMessage.ball_velocity());
            agent->addSayMessage(new rcsc::PassMessage(passMessage.receiver_uniform_number(),
                                                        receiverPoint,
                                                        ballPosition,
                                                        ballVelocity));
            break;
        }
        case protos::Say::kInterceptMessage:
        {
            const auto& interceptMessage = sayMessage.intercept_message();
            agent->addSayMessage(new rcsc::InterceptMessage(interceptMessage.our(), 
                                                            interceptMessage.uniform_number(), 
                                                            interceptMessage.cycle()));
            break;
        
        }
        case protos::Say::kGoalieMessage:
        {
            const auto& goalieMessage = sayMessage.goalie_message();
            const auto& goaliePosition = GrpcAgent::convertVector2D(goalieMessage.goalie_position());
            agent->addSayMessage(new rcsc::GoalieMessage(goalieMessage.goalie_uniform_number(), 
                                                            goaliePosition,
                                                            goalieMessage.goalie_body_direction()));
            break;
        }
        case protos::Say::kGoalieAndPlayerMessage:
        {
            const auto& goalieAndPlayerMessage = sayMessage.goalie_and_player_message();
            const auto& goaliePosition = GrpcAgent::convertVector2D(goalieAndPlayerMessage.goalie_position());
            const auto& playerPosition = GrpcAgent::convertVector2D(goalieAndPlayerMessage.player_position());
            agent->addSayMessage(new rcsc::GoalieAndPlayerMessage(goalieAndPlayerMessage.goalie_uniform_number(), 
                                                            goaliePosition,
                                                            goalieAndPlayerMessage.goalie_body_direction(),
                                                            goalieAndPlayerMessage.player_uniform_number(),
                                                            playerPosition));
            break;
        }
        case protos::Say::kOffsideLineMessage:
        {
            const auto& offsideLineMessage = sayMessage.offside_line_message();
            agent->addSayMessage(new rcsc::OffsideLineMessage(offsideLineMessage.offside_line_x()));
            break;
        }
        case protos::Say::kDefenseLineMessage:
        {
            const auto& defenseLineMessage = sayMessage.defense_line_message();
            agent->addSayMessage(new rcsc::DefenseLineMessage(defenseLineMessage.defense_line_x()));
            break;
        }
        case protos::Say::kWaitRequestMessage:
        {
            const auto& waitRequestMessage = sayMessage.wait_request_message();
            agent->addSayMessage(new rcsc::WaitRequestMessage());
            break;
        }
        case protos::Say::kSetplayMessage:
        {
            const auto& setplayMessage = sayMessage.setplay_message();
            agent->addSayMessage(new rcsc::SetplayMessage(setplayMessage.wait_step()));
            break;
        }
        case protos::Say::kPassRequestMessage:
        {
            const auto& passRequestMessage = sayMessage.pass_request_message();
            const auto& targetPoint = GrpcAgent::convertVector2D(passRequestMessage.target_point());
            agent->addSayMessage(new rcsc::PassRequestMessage(targetPoint));
            break;
        }
        case protos::Say::kStaminaMessage:
        {
            const auto& staminaMessage = sayMessage.stamina_message();
            agent->addSayMessage(new rcsc::StaminaMessage(staminaMessage.stamina()));
            break;
        }
        case protos::Say::kRecoveryMessage:
        {
            const auto& recoveryMessage = sayMessage.recovery_message();
            agent->addSayMessage(new rcsc::RecoveryMessage(recoveryMessage.recovery()));
            break;
        }
        case protos::Say::kStaminaCapacityMessage:
        {
            const auto& staminaCapacityMessage = sayMessage.stamina_capacity_message();
            agent->addSayMessage(new rcsc::StaminaCapacityMessage(staminaCapacityMessage.stamina_capacity()));
            break;
        }
        case protos::Say::kDribbleMessage:
        {
            const auto& dribbleMessage = sayMessage.dribble_message();
            const auto& targetPoint = GrpcAgent::convertVector2D(dribbleMessage.target_point());
            agent->addSayMessage(new rcsc::DribbleMessage(targetPoint, dribbleMessage.queue_count()));
            break;
        }
        case protos::Say::kBallGoalieMessage:
        {
            const auto& ballGoalieMessage = sayMessage.ball_goalie_message();
            const auto& ballPosition = GrpcAgent::convertVector2D(ballGoalieMessage.ball_position());
            const auto& ballVelocity = GrpcAgent::convertVector2D(ballGoalieMessage.ball_velocity());
            const auto& goaliePosition = GrpcAgent::convertVector2D(ballGoalieMessage.goalie_position());
            agent->addSayMessage(new rcsc::BallGoalieMessage(ballPosition, ballVelocity, goaliePosition, ballGoalieMessage.goalie_body_direction()));
            break;
        }
        case protos::Say::kOnePlayerMessage:
        {
            const auto& onePlayerMessage = sayMessage.one_player_message();
            const auto& playerPosition = GrpcAgent::convertVector2D(onePlayerMessage.position());
            agent->addSayMessage(new rcsc::OnePlayerMessage(onePlayerMessage.uniform_number(), playerPosition));
            break;
        }
        case protos::Say::kTwoPlayerMessage:
        {
            const auto& twoPlayersMessage = sayMessage.two_player_message();
            const auto& player1Position = GrpcAgent::convertVector2D(twoPlayersMessage.first_position());
            const auto& player2Position = GrpcAgent::convertVector2D(twoPlayersMessage.second_position());
            agent->addSayMessage(new rcsc::TwoPlayerMessage(twoPlayersMessage.first_uniform_number(), 
                                                            player1Position, 
                                                            twoPlayersMessage.second_uniform_number(), 
                                                            player2Position));
            break;
        }
        case protos::Say::kThreePlayerMessage:
        {
            const auto& threePlayersMessage = sayMessage.three_player_message();
            const auto& player1Position = GrpcAgent::convertVector2D(threePlayersMessage.first_position());
            const auto& player2Position = GrpcAgent::convertVector2D(threePlayersMessage.second_position());
            const auto& player3Position = GrpcAgent::convertVector2D(threePlayersMessage.third_position());
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
            const auto& selfMessage = sayMessage.self_message();
            const auto& selfPosition = GrpcAgent::convertVector2D(selfMessage.self_position());
            agent->addSayMessage(new rcsc::SelfMessage(selfPosition, selfMessage.self_body_direction(), selfMessage.self_stamina()));
            break;
        }
        case protos::Say::kTeammateMessage:
        {
            const auto& teammateMessage = sayMessage.teammate_message();
            const auto& teammatePosition = GrpcAgent::convertVector2D(teammateMessage.position());
            agent->addSayMessage(new rcsc::TeammateMessage(teammateMessage.uniform_number(), teammatePosition, teammateMessage.body_direction()));
            break;
        }
        case protos::Say::kOpponentMessage:
        {
            const auto& opponentMessage = sayMessage.opponent_message();
            const auto& opponentPosition = GrpcAgent::convertVector2D(opponentMessage.position());
            agent->addSayMessage(new rcsc::OpponentMessage(opponentMessage.uniform_number(), opponentPosition, opponentMessage.body_direction()));
            break;
        }
        case protos::Say::kBallPlayerMessage:
        {
            const auto& ballPlayerMessage = sayMessage.ball_player_message();
            const auto& ballPosition = GrpcAgent::convertVector2D(ballPlayerMessage.ball_position());
            const auto& ballVelocity = GrpcAgent::convertVector2D(ballPlayerMessage.ball_velocity());
            const auto& playerPosition = GrpcAgent::convertVector2D(ballPlayerMessage.player_position());
            agent->addSayMessage(new rcsc::BallPlayerMessage(ballPosition, ballVelocity, ballPlayerMessage.uniform_number(), playerPosition, ballPlayerMessage.body_direction()));
            break;
        }
        default:
        {
            std::cout<<"GrpcAgent: unknown say message"<<std::endl;
            break;
        }
    }
}

rcsc::ViewWidth GrpcAgent::convertViewWidth(protos::ViewWidth view_width){
    switch (view_width)
    {
    case protos::ViewWidth::NARROW:
        return rcsc::ViewWidth::NARROW;
    case protos::ViewWidth::NORMAL:
        return rcsc::ViewWidth::NORMAL;
    case protos::ViewWidth::WIDE:
        return rcsc::ViewWidth::WIDE;
    default:
        return rcsc::ViewWidth::NORMAL;
    }
}

rcsc::SideID GrpcAgent::convertSideID(protos::Side side){
    switch (side)
    {
    case protos::Side::LEFT:
        return rcsc::SideID::LEFT;
    case protos::Side::RIGHT:
        return rcsc::SideID::RIGHT;
    default:
        return rcsc::SideID::LEFT;
    }
}

rcsc::Vector2D GrpcAgent::convertVector2D(protos::Vector2D vector2d){
    return rcsc::Vector2D(vector2d.x(), vector2d.y());
}