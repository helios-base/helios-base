#include "grpc_agent.h"
#include "state_generator.h"
#include "action_convertor.h"

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
        // todo log debugClient
        
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