#include "thrift_agent_trainer.h"
#include "thrift_state_generator.h"
// #include "state_generator.h"

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

ThriftAgentTrainer::ThriftAgentTrainer()
{
    M_agent_type = soccer::AgentType::TrainerT;
}

void ThriftAgentTrainer::init(rcsc::TrainerAgent *agent,
                              std::string target,
                              int port,
                              bool use_same_grpc_port,
                              bool add_20_to_grpc_port_if_right_side)
{
    M_agent = agent;
    M_team_name = agent->world().ourTeamName();
    M_unum = 13;
    if (add_20_to_grpc_port_if_right_side)
        if (M_agent->world().ourSide() == rcsc::SideID::RIGHT)
            port += 20;

    if (!use_same_grpc_port)
    {
        port += 13;
    }

    this->M_server_host = target;
    this->M_server_port = port;
}

void ThriftAgentTrainer::getActions()
{
    auto agent = M_agent;
    std::cout<<"generating state for cycle:"<<agent->world().time().cycle()<<std::endl;
    soccer::State state = generateState();
    std::cout<<"generated state for cycle:"<<agent->world().time().cycle()<<std::endl;
    state.agent_type = soccer::AgentType::TrainerT;
    state.register_response = M_register_response;
    soccer::TrainerActions actions;

    try{
        M_client->GetTrainerActions(actions, state);
    }
    catch(const std::exception& e){
        std::cerr << e.what() << '\n';
        M_is_connected = false;
        return;
    }
    std::cout<<"actions:"<<actions.actions.size()<<std::endl;
    for (int i = 0; i < actions.actions.size(); i++)
    {
        auto action = actions.actions[i];
        if (action.__isset.do_kick_off)
        {
            agent->doKickOff();
            continue;
        }
        if (action.__isset.do_move_ball)
        {
            const auto &doMoveBall = action.do_move_ball;
            const auto &ballPosition = ThriftAgent::convertVector2D(doMoveBall.position);
            const auto &ballVelocity = doMoveBall.__isset.velocity ? ThriftAgent::convertVector2D(doMoveBall.velocity) : rcsc::Vector2D(0, 0);
            agent->doMoveBall(ballPosition, ballVelocity);
            continue;
        }
        if (action.__isset.do_move_player)
        {
            const auto &doMovePlayer = action.do_move_player;
            const auto &unum = doMovePlayer.uniform_number;
            const auto &position = ThriftAgent::convertVector2D(doMovePlayer.position);
            const auto &body = rcsc::AngleDeg(doMovePlayer.body_direction);
            std::string team_name = "";
            if (doMovePlayer.our_side)
            {
                team_name = agent->world().ourTeamName();
            }
            else
            {
                team_name = agent->world().theirTeamName();
            }
            agent->doMovePlayer(team_name, unum, position, body);
            continue;
        }
        if (action.__isset.do_recover)
        {
            agent->doRecover();
            continue;
        }
        if (action.__isset.do_change_mode)
        {
            const auto &mode = action.do_change_mode.game_mode_type;
            const auto &side = action.do_change_mode.side;

            rcsc::PlayMode play_mode;
            switch (mode)
            {
            case soccer::GameModeType::BeforeKickOff:
            {
                play_mode = rcsc::PlayMode::PM_BeforeKickOff;
                break;
            }
            case soccer::GameModeType::TimeOver:
            {
                play_mode = rcsc::PlayMode::PM_TimeOver;
                break;
            }
            case soccer::GameModeType::PlayOn:
            {
                play_mode = rcsc::PlayMode::PM_PlayOn;
                break;
            }
            case soccer::GameModeType::KickOff_:
            {
                play_mode = side == soccer::Side::LEFT ? rcsc::PlayMode::PM_KickOff_Left : rcsc::PlayMode::PM_KickOff_Right;
                break;
            }
            case soccer::GameModeType::KickIn_:
            {
                play_mode = side == soccer::Side::LEFT ? rcsc::PlayMode::PM_KickIn_Left : rcsc::PlayMode::PM_KickIn_Right;
                break;
            }
            case soccer::GameModeType::FreeKick_:
            {
                play_mode = side == soccer::Side::LEFT ? rcsc::PlayMode::PM_FreeKick_Left : rcsc::PlayMode::PM_FreeKick_Right;
                break;
            }
            case soccer::GameModeType::CornerKick_:
            {
                play_mode = side == soccer::Side::LEFT ? rcsc::PlayMode::PM_CornerKick_Left : rcsc::PlayMode::PM_CornerKick_Right;
                break;
            }
            case soccer::GameModeType::GoalKick_:
            {
                play_mode = side == soccer::Side::LEFT ? rcsc::PlayMode::PM_GoalKick_Left : rcsc::PlayMode::PM_GoalKick_Right;
                break;
            }
            case soccer::GameModeType::AfterGoal_:
            {
                play_mode = side == soccer::Side::LEFT ? rcsc::PlayMode::PM_AfterGoal_Left : rcsc::PlayMode::PM_AfterGoal_Right;
                break;
            }
            case soccer::GameModeType::OffSide_:
            {
                play_mode = side == soccer::Side::LEFT ? rcsc::PlayMode::PM_OffSide_Left : rcsc::PlayMode::PM_OffSide_Right;
                break;
            }
            case soccer::GameModeType::FirstHalfOver:
            {
                play_mode = rcsc::PlayMode::PM_FirstHalfOver;
                break;
            }
            case soccer::GameModeType::Pause:
            {
                play_mode = rcsc::PlayMode::PM_Pause;
                break;
            }
            case soccer::GameModeType::Human:
            {
                play_mode = rcsc::PlayMode::PM_Human;
                break;
            }
            case soccer::GameModeType::FoulCharge_:
            {
                play_mode = side == soccer::Side::LEFT ? rcsc::PlayMode::PM_Foul_Charge_Left : rcsc::PlayMode::PM_Foul_Charge_Right;
                break;
            }
            case soccer::GameModeType::FoulPush_:
            {
                play_mode = side == soccer::Side::LEFT ? rcsc::PlayMode::PM_Foul_Push_Left : rcsc::PlayMode::PM_Foul_Push_Right;
                break;
            }
            case soccer::GameModeType::FoulMultipleAttacker_:
            {
                play_mode = side == soccer::Side::LEFT ? rcsc::PlayMode::PM_Foul_MultipleAttacker_Left : rcsc::PlayMode::PM_Foul_MultipleAttacker_Right;
                break;
            }
            case soccer::GameModeType::FoulBallOut_:
            {
                play_mode = side == soccer::Side::LEFT ? rcsc::PlayMode::PM_Foul_BallOut_Left : rcsc::PlayMode::PM_Foul_BallOut_Right;
                break;
            }
            case soccer::GameModeType::BackPass_:
            {
                play_mode = side == soccer::Side::LEFT ? rcsc::PlayMode::PM_Back_Pass_Left : rcsc::PlayMode::PM_Back_Pass_Right;
                break;
            }
            case soccer::GameModeType::FreeKickFault_:
            {
                play_mode = side == soccer::Side::LEFT ? rcsc::PlayMode::PM_Free_Kick_Fault_Left : rcsc::PlayMode::PM_Free_Kick_Fault_Right;
                break;
            }
            case soccer::GameModeType::CatchFault_:
            {
                play_mode = side == soccer::Side::LEFT ? rcsc::PlayMode::PM_CatchFault_Left : rcsc::PlayMode::PM_CatchFault_Right;
                break;
            }
            case soccer::GameModeType::IndFreeKick_:
            {
                play_mode = side == soccer::Side::LEFT ? rcsc::PlayMode::PM_IndFreeKick_Left : rcsc::PlayMode::PM_IndFreeKick_Right;
                break;
            }
            case soccer::GameModeType::PenaltySetup_:
            {
                play_mode = side == soccer::Side::LEFT ? rcsc::PlayMode::PM_PenaltySetup_Left : rcsc::PlayMode::PM_PenaltySetup_Right;
                break;
            }
            case soccer::GameModeType::PenaltyReady_:
            {
                play_mode = side == soccer::Side::LEFT ? rcsc::PlayMode::PM_PenaltyReady_Left : rcsc::PlayMode::PM_PenaltyReady_Right;
                break;
            }
            case soccer::GameModeType::PenaltyTaken_:
            {
                play_mode = side == soccer::Side::LEFT ? rcsc::PlayMode::PM_PenaltyTaken_Left : rcsc::PlayMode::PM_PenaltyTaken_Right;
                break;
            }
            case soccer::GameModeType::PenaltyMiss_:
            {
                play_mode = side == soccer::Side::LEFT ? rcsc::PlayMode::PM_PenaltyMiss_Left : rcsc::PlayMode::PM_PenaltyMiss_Right;
                break;
            }
            case soccer::GameModeType::PenaltyScore_:
            {
                play_mode = side == soccer::Side::LEFT ? rcsc::PlayMode::PM_PenaltyScore_Left : rcsc::PlayMode::PM_PenaltyScore_Right;
                break;
            }
            case soccer::GameModeType::IllegalDefense_:
            {
                play_mode = side == soccer::Side::LEFT ? rcsc::PlayMode::PM_Illegal_Defense_Left : rcsc::PlayMode::PM_Illegal_Defense_Right;
                break;
            }
            default:
            {
                LOG("unknown action");
                break;
            }
            }
            agent->doChangeMode(play_mode);
            continue;
        }
        if (action.__isset.do_change_player_type)
        {
            const auto &doChangePlayerType = action.do_change_player_type;
            const auto &playerType = doChangePlayerType.type;
            const auto &unum = doChangePlayerType.uniform_number;
            std::string team_name = doChangePlayerType.our_side ? agent->world().ourTeamName() : agent->world().theirTeamName();
            agent->doChangePlayerType(team_name, unum, playerType);
        }
    }
}

soccer::State ThriftAgentTrainer::generateState() const
{
    auto &wm = M_agent->world();
     soccer::WorldModel worldModel = ThriftStateGenerator::convertCoachWorldModel(wm);
    soccer::State state;
    state.world_model = worldModel;
    return state;
}