#include "grpc_agent_trainer.h"
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

GrpcAgentTrainer::GrpcAgentTrainer()
{
    M_agent_type = protos::AgentType::TrainerT;
}

void GrpcAgentTrainer::init(rcsc::TrainerAgent *agent,
                            std::string target,
                            int port,
                            bool use_same_grpc_port,
                            bool add_20_to_grpc_port_if_right_side)
{
    M_agent = agent;
    M_unum = 13;
    M_team_name = agent->world().ourTeamName();
    if (add_20_to_grpc_port_if_right_side)
        if (M_agent->world().ourSide() == rcsc::SideID::RIGHT)
            port += 20;

    if (!use_same_grpc_port)
    {
        port += 13;
    }

    this->M_target = target + ":" + std::to_string(port);
}

void GrpcAgentTrainer::getActions()
{
    auto agent = M_agent;
    State state = generateState();
    state.set_agent_type(protos::AgentType::TrainerT);
    state.set_allocated_register_response(M_register_response);
    protos::TrainerActions actions;
    ClientContext context;
    Status status = M_stub_->GetTrainerActions(&context, state, &actions);
    if (!status.ok())
    {
        std::cout << status.error_code() << ": " << status.error_message()
                  << std::endl;
        return;
    }

    for (int i = 0; i < actions.actions_size(); i++)
    {
        auto action = actions.actions(i);
        switch (action.action_case())
        {
        case TrainerAction::kDoKickOff:
        {
            agent->doKickOff();
            break;
        }
        case TrainerAction::kDoMoveBall:
        {
            const auto &doMoveBall = action.do_move_ball();
            const auto &ballPosition = GrpcAgent::convertVector2D(doMoveBall.position());
            const auto &ballVelocity = doMoveBall.has_velocity() ? GrpcAgent::convertVector2D(doMoveBall.velocity()) : rcsc::Vector2D(0, 0);
            agent->doMoveBall(ballPosition, ballVelocity);
            break;
        }
        case TrainerAction::kDoMovePlayer:
        {
            const auto &doMovePlayer = action.do_move_player();
            const auto &unum = doMovePlayer.uniform_number();
            const auto &position = GrpcAgent::convertVector2D(doMovePlayer.position());
            const auto &body = rcsc::AngleDeg(doMovePlayer.body_direction());
            std::string team_name = "";
            if (doMovePlayer.our_side())
            {
                team_name = agent->world().ourTeamName();
            }
            else
            {
                team_name = agent->world().theirTeamName();
            }
            agent->doMovePlayer(team_name, unum, position, body);
            break;
        }
        case TrainerAction::kDoRecover:
        {
            agent->doRecover();
            break;
        }
        case TrainerAction::kDoChangeMode:
        {
            const auto &mode = action.do_change_mode().game_mode_type();
            const auto &side = action.do_change_mode().side();

            rcsc::PlayMode play_mode;
            switch (mode)
            {
            case protos::GameModeType::BeforeKickOff:
            {
                play_mode = rcsc::PlayMode::PM_BeforeKickOff;
                break;
            }
            case protos::GameModeType::TimeOver:
            {
                play_mode = rcsc::PlayMode::PM_TimeOver;
                break;
            }
            case protos::GameModeType::PlayOn:
            {
                play_mode = rcsc::PlayMode::PM_PlayOn;
                break;
            }
            case protos::GameModeType::KickOff_:
            {
                play_mode = side == protos::Side::LEFT ? rcsc::PlayMode::PM_KickOff_Left : rcsc::PlayMode::PM_KickOff_Right;
                break;
            }
            case protos::GameModeType::KickIn_:
            {
                play_mode = side == protos::Side::LEFT ? rcsc::PlayMode::PM_KickIn_Left : rcsc::PlayMode::PM_KickIn_Right;
                break;
            }
            case protos::GameModeType::FreeKick_:
            {
                play_mode = side == protos::Side::LEFT ? rcsc::PlayMode::PM_FreeKick_Left : rcsc::PlayMode::PM_FreeKick_Right;
                break;
            }
            case protos::GameModeType::CornerKick_:
            {
                play_mode = side == protos::Side::LEFT ? rcsc::PlayMode::PM_CornerKick_Left : rcsc::PlayMode::PM_CornerKick_Right;
                break;
            }
            case protos::GameModeType::GoalKick_:
            {
                play_mode = side == protos::Side::LEFT ? rcsc::PlayMode::PM_GoalKick_Left : rcsc::PlayMode::PM_GoalKick_Right;
                break;
            }
            case protos::GameModeType::AfterGoal_:
            {
                play_mode = side == protos::Side::LEFT ? rcsc::PlayMode::PM_AfterGoal_Left : rcsc::PlayMode::PM_AfterGoal_Right;
                break;
            }
            case protos::GameModeType::OffSide_:
            {
                play_mode = side == protos::Side::LEFT ? rcsc::PlayMode::PM_OffSide_Left : rcsc::PlayMode::PM_OffSide_Right;
                break;
            }
            case protos::GameModeType::FirstHalfOver:
            {
                play_mode = rcsc::PlayMode::PM_FirstHalfOver;
                break;
            }
            case protos::GameModeType::Pause:
            {
                play_mode = rcsc::PlayMode::PM_Pause;
                break;
            }
            case protos::GameModeType::Human:
            {
                play_mode = rcsc::PlayMode::PM_Human;
                break;
            }
            case protos::GameModeType::FoulCharge_:
            {
                play_mode = side == protos::Side::LEFT ? rcsc::PlayMode::PM_Foul_Charge_Left : rcsc::PlayMode::PM_Foul_Charge_Right;
                break;
            }
            case protos::GameModeType::FoulPush_:
            {
                play_mode = side == protos::Side::LEFT ? rcsc::PlayMode::PM_Foul_Push_Left : rcsc::PlayMode::PM_Foul_Push_Right;
                break;
            }
            case protos::GameModeType::FoulMultipleAttacker_:
            {
                play_mode = side == protos::Side::LEFT ? rcsc::PlayMode::PM_Foul_MultipleAttacker_Left : rcsc::PlayMode::PM_Foul_MultipleAttacker_Right;
                break;
            }
            case protos::GameModeType::FoulBallOut_:
            {
                play_mode = side == protos::Side::LEFT ? rcsc::PlayMode::PM_Foul_BallOut_Left : rcsc::PlayMode::PM_Foul_BallOut_Right;
                break;
            }
            case protos::GameModeType::BackPass_:
            {
                play_mode = side == protos::Side::LEFT ? rcsc::PlayMode::PM_Back_Pass_Left : rcsc::PlayMode::PM_Back_Pass_Right;
                break;
            }
            case protos::GameModeType::FreeKickFault_:
            {
                play_mode = side == protos::Side::LEFT ? rcsc::PlayMode::PM_Free_Kick_Fault_Left : rcsc::PlayMode::PM_Free_Kick_Fault_Right;
                break;
            }
            case protos::GameModeType::CatchFault_:
            {
                play_mode = side == protos::Side::LEFT ? rcsc::PlayMode::PM_CatchFault_Left : rcsc::PlayMode::PM_CatchFault_Right;
                break;
            }
            case protos::GameModeType::IndFreeKick_:
            {
                play_mode = side == protos::Side::LEFT ? rcsc::PlayMode::PM_IndFreeKick_Left : rcsc::PlayMode::PM_IndFreeKick_Right;
                break;
            }
            case protos::GameModeType::PenaltySetup_:
            {
                play_mode = side == protos::Side::LEFT ? rcsc::PlayMode::PM_PenaltySetup_Left : rcsc::PlayMode::PM_PenaltySetup_Right;
                break;
            }
            case protos::GameModeType::PenaltyReady_:
            {
                play_mode = side == protos::Side::LEFT ? rcsc::PlayMode::PM_PenaltyReady_Left : rcsc::PlayMode::PM_PenaltyReady_Right;
                break;
            }
            case protos::GameModeType::PenaltyTaken_:
            {
                play_mode = side == protos::Side::LEFT ? rcsc::PlayMode::PM_PenaltyTaken_Left : rcsc::PlayMode::PM_PenaltyTaken_Right;
                break;
            }
            case protos::GameModeType::PenaltyMiss_:
            {
                play_mode = side == protos::Side::LEFT ? rcsc::PlayMode::PM_PenaltyMiss_Left : rcsc::PlayMode::PM_PenaltyMiss_Right;
                break;
            }
            case protos::GameModeType::PenaltyScore_:
            {
                play_mode = side == protos::Side::LEFT ? rcsc::PlayMode::PM_PenaltyScore_Left : rcsc::PlayMode::PM_PenaltyScore_Right;
                break;
            }
            case protos::GameModeType::IllegalDefense_:
            {
                play_mode = side == protos::Side::LEFT ? rcsc::PlayMode::PM_Illegal_Defense_Left : rcsc::PlayMode::PM_Illegal_Defense_Right;
                break;
            }
            default:
            {
                LOG("unknown action");
                break;
            }
            }
            agent->doChangeMode(play_mode);
            break;
        }
        case TrainerAction::kDoChangePlayerType:
        {
            const auto &doChangePlayerType = action.do_change_player_type();
            const auto &playerType = doChangePlayerType.type();
            const auto &unum = doChangePlayerType.uniform_number();
            std::string team_name = doChangePlayerType.our_side() ? agent->world().ourTeamName() : agent->world().theirTeamName();
            agent->doChangePlayerType(team_name, unum, playerType);
            break;
        }
        default:
        {
            LOG("unknown action");
            break;
        }
        }
    }
}

State GrpcAgentTrainer::generateState() const
{
    auto &wm = M_agent->world();
    // WorldModel * worldModel = StateGenerator::convertCoachWorldModel(wm);
    State state;
    // state.set_allocated_world_model(worldModel);
    return state;
}