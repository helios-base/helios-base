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

#define DEBUG

#ifdef DEBUG
#define LOG(x) std::cout << x << std::endl
#define LOGV(x) std::cout << #x << ": " << x << std::endl
#else
#define LOG(x)
#define LOGV(x)
#endif

void GrpcAgent::sendServerParam() const {
    LOG("sendServerParam Started");

    protos::ServerParam serverParam;
    const rcsc::ServerParam& SP = rcsc::ServerParam::i();
    
    std::string replayFile = SP.replayFile();
    serverParam.set_allocated_replay_file(&replayFile);
    std::string landmarkFile = SP.landmarkFile();
    serverParam.set_allocated_landmark_file(&landmarkFile);
    std::string textLogDir = SP.textLogDir();
    serverParam.set_allocated_text_log_dir(&textLogDir);
    std::string gameLogDir = SP.gameLogDir();
    serverParam.set_allocated_game_log_dir(&gameLogDir);
    std::string textLogFixedName = SP.textLogFixedName();
    serverParam.set_allocated_text_log_fixed_name(&textLogFixedName);
    std::string gameLogFixedName = SP.gameLogFixedName();
    serverParam.set_allocated_game_log_fixed_name(&gameLogFixedName);
    std::string logDateFormat = SP.logDateFormat();
    serverParam.set_allocated_log_date_format(&logDateFormat);
    std::string teamLeftStartCommand = SP.teamLeftStartCommand();
    serverParam.set_allocated_team_l_start(&teamLeftStartCommand);
    std::string teamRightStartCommand = SP.teamRightStartCommand();
    serverParam.set_allocated_team_r_start(&teamRightStartCommand);
    std::string keepawayLogDir = SP.keepawayLogDir();
    serverParam.set_allocated_keepaway_log_dir(&keepawayLogDir);
    std::string keepawayLogFixedName = SP.keepawayLogFixedName();
    serverParam.set_allocated_keepaway_log_fixed_name(&keepawayLogFixedName);
    std::string moduleDir = SP.moduleDir();
    serverParam.set_allocated_module_dir(&moduleDir);
    std::string coachMsgFile = SP.coachMsgFile();
    serverParam.set_allocated_coach_msg_file(&coachMsgFile);
    std::string fixedTeamNameLeft = SP.fixedTeamNameLeft();
    serverParam.set_allocated_fixed_teamname_l(&fixedTeamNameLeft);
    std::string fixedTeamNameRight = SP.fixedTeamNameRight();
    serverParam.set_allocated_fixed_teamname_r(&fixedTeamNameRight);

    serverParam.set_goal_width(SP.goalWidth());
    serverParam.set_inertia_moment(SP.defaultInertiaMoment());
    serverParam.set_player_size(SP.defaultPlayerSize());
    serverParam.set_player_decay(SP.defaultPlayerDecay());
    serverParam.set_player_rand(SP.playerRand());
    serverParam.set_player_weight(SP.playerWeight());
    serverParam.set_player_speed_max(SP.defaultPlayerSpeedMax());
    serverParam.set_player_accel_max(SP.playerAccelMax());
    serverParam.set_stamina_max(SP.staminaMax());
    serverParam.set_stamina_inc_max(SP.defaultStaminaIncMax());
    serverParam.set_recover_init(SP.recoverInit());
    serverParam.set_recover_dec_thr(SP.recoverDecThr());
    serverParam.set_recover_min(SP.recoverMin());
    serverParam.set_recover_dec(SP.recoverDec());
    serverParam.set_effort_init(SP.effortInit());
    serverParam.set_effort_dec_thr(SP.effortDecThr());
    serverParam.set_effort_min(SP.defaultEffortMin());
    serverParam.set_effort_dec(SP.effortDec());
    serverParam.set_effort_inc_thr(SP.effortIncThr());
    serverParam.set_effort_inc(SP.effortInc());
    serverParam.set_kick_rand(SP.defaultKickRand());
    serverParam.set_team_actuator_noise(SP.teamActuatorNoise());
    serverParam.set_player_rand_factor_l(SP.playerRandFactorLeft());
    serverParam.set_player_rand_factor_r(SP.playerRandFactorRight());
    serverParam.set_kick_rand_factor_l(SP.kickRandFactorLeft());
    serverParam.set_kick_rand_factor_r(SP.kickRandFactorRight());
    serverParam.set_ball_size(SP.ballSize());
    serverParam.set_ball_decay(SP.ballDecay());
    serverParam.set_ball_rand(SP.ballRand());
    serverParam.set_ball_weight(SP.ballWeight());
    serverParam.set_ball_speed_max(SP.ballSpeedMax());
    serverParam.set_ball_accel_max(SP.ballAccelMax());
    serverParam.set_dash_power_rate(SP.defaultDashPowerRate());
    serverParam.set_kick_power_rate(SP.kickPowerRate());
    serverParam.set_kickable_margin(SP.defaultKickableMargin());
    serverParam.set_control_radius(SP.controlRadius());
    serverParam.set_control_radius_width(SP.controlRadiusWidth());
    serverParam.set_max_power(SP.maxPower());
    serverParam.set_min_power(SP.minPower());
    serverParam.set_max_moment(SP.maxMoment());
    serverParam.set_min_moment(SP.minMoment());
    serverParam.set_max_neck_moment(SP.maxNeckMoment());
    serverParam.set_min_neck_moment(SP.minNeckMoment());
    serverParam.set_max_neck_angle(SP.maxNeckAngle());
    serverParam.set_min_neck_angle(SP.minNeckAngle());
    serverParam.set_visible_angle(SP.visibleAngle());
    serverParam.set_visible_distance(SP.visibleDistance());
    serverParam.set_wind_dir(SP.windDir());
    serverParam.set_wind_force(SP.windForce());
    serverParam.set_wind_angle(SP.windAngle());
    serverParam.set_wind_rand(SP.windRand());
    serverParam.set_kickable_area(SP.defaultKickableArea());
    serverParam.set_catch_area_l(SP.catchAreaLength());
    serverParam.set_catch_area_w(SP.catchAreaWidth());
    serverParam.set_catch_probability(SP.catchProbability());
    serverParam.set_goalie_max_moves(SP.goalieMaxMoves());
    serverParam.set_corner_kick_margin(SP.cornerKickMargin());
    serverParam.set_offside_active_area_size(SP.offsideActiveAreaSize());
    serverParam.set_wind_none(SP.windNone());
    serverParam.set_use_wind_random(SP.useWindRandom());
    serverParam.set_coach_say_count_max(SP.coachSayCountMax());
    serverParam.set_coach_say_msg_size(SP.coachSayMsgSize());
    serverParam.set_clang_win_size(SP.clangWinSize());
    serverParam.set_clang_define_win(SP.clangDefineWin());
    serverParam.set_clang_meta_win(SP.clangMetaWin());
    serverParam.set_clang_advice_win(SP.clangAdviceWin());
    serverParam.set_clang_info_win(SP.clangInfoWin());
    serverParam.set_clang_mess_delay(SP.clangMessDelay());
    serverParam.set_clang_mess_per_cycle(SP.clangMessPerCycle());
    serverParam.set_half_time(SP.halfTime());
    serverParam.set_simulator_step(SP.simulatorStep());
    serverParam.set_send_step(SP.sendStep());
    serverParam.set_recv_step(SP.recvStep());
    serverParam.set_sense_body_step(SP.senseBodyStep());
    serverParam.set_lcm_step(SP.lcmStep());
    serverParam.set_player_say_msg_size(SP.playerSayMsgSize());
    serverParam.set_player_hear_max(SP.playerHearMax());
    serverParam.set_player_hear_inc(SP.playerHearInc());
    serverParam.set_player_hear_decay(SP.playerHearDecay());
    serverParam.set_catch_ban_cycle(SP.catchBanCycle());
    serverParam.set_slow_down_factor(SP.slowDownFactor());
    serverParam.set_use_offside(SP.useOffside());
    serverParam.set_kickoff_offside(SP.kickoffOffside());
    serverParam.set_offside_kick_margin(SP.offsideKickMargin());
    serverParam.set_audio_cut_dist(SP.audioCutDist());
    serverParam.set_dist_quantize_step(SP.distQuantizeStep());
    serverParam.set_landmark_dist_quantize_step(SP.landmarkDistQuantizeStep());
    serverParam.set_dir_quantize_step(SP.dirQuantizeStep());
    serverParam.set_dist_quantize_step_l(SP.landmarkDistQuantizeStepLeft());
    serverParam.set_dist_quantize_step_r(SP.distQuantizeStepRight());
    serverParam.set_landmark_dist_quantize_step_l(SP.landmarkDistQuantizeStepLeft());
    serverParam.set_landmark_dist_quantize_step_r(SP.landmarkDistQuantizeStepRight());
    serverParam.set_dir_quantize_step_l(SP.dirQuantizeStepLeft());
    serverParam.set_dir_quantize_step_r(SP.dirQuantizeStepRight());
    serverParam.set_coach_mode(SP.coachMode());
    serverParam.set_coach_with_referee_mode(SP.coachWithRefereeMode());
    serverParam.set_use_old_coach_hear(SP.useOldCoachHear());
    serverParam.set_slowness_on_top_for_left_team(SP.slownessOnTopForLeft());
    serverParam.set_slowness_on_top_for_right_team(SP.slownessOnTopForRight());
    serverParam.set_start_goal_l(SP.startGoalLeft());
    serverParam.set_start_goal_r(SP.stargGoalRight());
    serverParam.set_fullstate_l(SP.fullstateLeft());
    serverParam.set_fullstate_r(SP.fullstateRight());
    serverParam.set_drop_ball_time(SP.dropBallTime());
    serverParam.set_synch_mode(SP.synchMode());
    serverParam.set_synch_offset(SP.synchOffset());
    serverParam.set_synch_micro_sleep(SP.synchMicroSleep());
    serverParam.set_point_to_ban(SP.pointToBan());
    serverParam.set_point_to_duration(SP.pointToDuration());
    serverParam.set_player_port(SP.playerPort());
    serverParam.set_trainer_port(SP.trainerPort());
    serverParam.set_online_coach_port(SP.onlineCoachPort());
    serverParam.set_verbose_mode(SP.verboseMode());
    serverParam.set_coach_send_vi_step(SP.coachSendVIStep());
    serverParam.set_send_comms(SP.sendComms());
    serverParam.set_text_logging(SP.textLogging());
    serverParam.set_game_logging(SP.gameLogging());
    serverParam.set_game_log_version(SP.gameLogVersion());
    serverParam.set_use_text_log_fixed(SP.textLogFixed());
    serverParam.set_use_game_log_fixed(SP.gameLogFixed());
    serverParam.set_use_text_log_dated(SP.textLogDated());
    serverParam.set_use_game_log_dated(SP.gameLogDated());
    serverParam.set_log_times(SP.logTimes());
    serverParam.set_record_message(SP.recordMessage());
    serverParam.set_text_log_compression(SP.textLogCompression());
    serverParam.set_game_log_compression(SP.gameLogCompression());
    serverParam.set_use_profile(SP.useProfile());
    serverParam.set_tackle_dist(SP.tackleDist());
    serverParam.set_tackle_back_dist(SP.tackleBackDist());
    serverParam.set_tackle_width(SP.tackleWidth());
    serverParam.set_tackle_exponent(SP.tackleExponent());
    serverParam.set_tackle_cycles(SP.tackleCycles());
    serverParam.set_tackle_power_rate(SP.tacklePowerRate());
    serverParam.set_freeform_wait_period(SP.freeformWaitPeriod());
    serverParam.set_freeform_send_period(SP.freeformSendPeriod());
    serverParam.set_free_kick_faults(SP.freeKickFaults());
    serverParam.set_back_passes(SP.backPasses());
    serverParam.set_proper_goal_kicks(SP.properGoalKicks());
    serverParam.set_stopped_ball_vel(SP.stoppedBallVel());
    serverParam.set_max_goal_kicks(SP.maxGoalKicks());
    serverParam.set_clang_del_win(SP.clangDelWin());
    serverParam.set_clang_rule_win(SP.clangRuleWin());
    serverParam.set_auto_mode(SP.autoMode());
    serverParam.set_kick_off_wait(SP.kickOffWait());
    serverParam.set_connect_wait(SP.connectWait());
    serverParam.set_game_over_wait(SP.gameOverWait());
    serverParam.set_keepaway_mode(SP.keepawayMode());
    serverParam.set_keepaway_length(SP.keepawayLength());
    serverParam.set_keepaway_width(SP.keepawayWidth());
    serverParam.set_keepaway_logging(SP.keepawayLogging());
    serverParam.set_keepaway_log_fixed(SP.keepawayLogFixed());
    serverParam.set_keepaway_log_dated(SP.keepawayLogDated());
    serverParam.set_keepaway_start(SP.keepawayStart());
    serverParam.set_nr_normal_halfs(SP.nrNormalHalfs());
    serverParam.set_nr_extra_halfs(SP.nrExtraHalfs());
    serverParam.set_penalty_shoot_outs(SP.penaltyShootOuts());
    serverParam.set_pen_before_setup_wait(SP.penBeforeSetupWait());
    serverParam.set_pen_setup_wait(SP.penSetupWait());
    serverParam.set_pen_ready_wait(SP.penReadyWait());
    serverParam.set_pen_taken_wait(SP.penTakenWait());
    serverParam.set_pen_nr_kicks(SP.penNrKicks());
    serverParam.set_pen_max_extra_kicks(SP.penMaxExtraKicks());
    serverParam.set_pen_dist_x(SP.penDistX());
    serverParam.set_pen_random_winner(SP.penRandomWinner());
    serverParam.set_pen_allow_mult_kicks(SP.penAllowMultKicks());
    serverParam.set_pen_max_goalie_dist_x(SP.penMaxGoalieDistX());
    serverParam.set_pen_coach_moves_players(SP.penCoachMovesPlayers());
    serverParam.set_ball_stuck_area(SP.ballStuckArea());
    serverParam.set_max_tackle_power(SP.maxTacklePower());
    serverParam.set_max_back_tackle_power(SP.maxBackTacklePower());
    serverParam.set_player_speed_max_min(SP.playerSpeedMaxMin());
    serverParam.set_extra_stamina(SP.defaultExtraStamina());
    serverParam.set_synch_see_offset(SP.synchSeeOffset());
    serverParam.set_extra_half_time(SP.extraHalfTime());
    serverParam.set_stamina_capacity(SP.staminaCapacity());
    serverParam.set_max_dash_angle(SP.maxDashAngle());
    serverParam.set_min_dash_angle(SP.minDashAngle());
    serverParam.set_dash_angle_step(SP.dashAngleStep());
    serverParam.set_side_dash_rate(SP.sideDashRate());
    serverParam.set_back_dash_rate(SP.backDashRate());
    serverParam.set_max_dash_power(SP.maxDashPower());
    serverParam.set_min_dash_power(SP.minDashPower());
    serverParam.set_tackle_rand_factor(SP.tackleRandFactor());
    serverParam.set_foul_detect_probability(SP.foulDetectProbability());
    serverParam.set_foul_exponent(SP.foulExponent());
    serverParam.set_foul_cycles(SP.foulCycles());
    serverParam.set_golden_goal(SP.goldenGoal());
    serverParam.set_red_card_probability(SP.redCardProbability());
    serverParam.set_illegal_defense_duration(SP.illegalDefenseDuration());
    serverParam.set_illegal_defense_number(SP.illegalDefenseNumber());
    serverParam.set_illegal_defense_dist_x(SP.illegalDefenseDistX());
    serverParam.set_illegal_defense_width(SP.illegalDefenseWidth());
    serverParam.set_max_catch_angle(SP.maxCatchAngle());
    serverParam.set_min_catch_angle(SP.minCatchAngle());
    serverParam.set_random_seed(SP.randomSeed());
    serverParam.set_long_kick_power_factor(SP.longKickPowerFactor());
    serverParam.set_long_kick_delay(SP.longKickDelay());
    serverParam.set_max_monitors(SP.maxMonitors());
    serverParam.set_catchable_area(SP.catchableArea());
    serverParam.set_real_speed_max(SP.defaultRealSpeedMax());
}

void GrpcAgent::getAction(rcsc::PlayerAgent * agent) const{
    LOG("getAction Started");
    LOGV(agent->world().time().cycle());
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

    LOG("getAction apply actions on agent");
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
            LOG("body go to point");
            const auto& bodyGoToPoint = action.body_go_to_point();
            const auto& targetPoint = GrpcAgent::convertVector2D(bodyGoToPoint.target_point());
            LOGV(targetPoint);
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
            LOG("unknown action");
            break;
        }
        }
        LOG("getAction done");
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