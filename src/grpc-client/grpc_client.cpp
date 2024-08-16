#include "grpc_client.h"
#include "state_generator.h"

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

void GrpcClient::sendParams(bool offline_logging)
{
    if (!M_param_sent)
    {
        sendServerParam();
        sendPlayerParams();
        sendPlayerType();
        sendInitMessage(offline_logging);
        M_param_sent = true;
    }
}
void GrpcClient::sendServerParam() const
{
    LOG("sendServerParam Started");

    protos::ServerParam serverParam;
    const rcsc::ServerParam &SP = rcsc::ServerParam::i();

    //    std::string replayFile = SP.replayFile();
    //    serverParam.set_allocated_replay_file(&replayFile);
    //    std::string landmarkFile = SP.landmarkFile();
    //    serverParam.set_allocated_landmark_file(&landmarkFile);
    //    std::string textLogDir = SP.textLogDir();
    //    serverParam.set_allocated_text_log_dir(&textLogDir);
    //    std::string gameLogDir = SP.gameLogDir();
    //    serverParam.set_allocated_game_log_dir(&gameLogDir);
    //    std::string textLogFixedName = SP.textLogFixedName();
    //    serverParam.set_allocated_text_log_fixed_name(&textLogFixedName);
    //    std::string gameLogFixedName = SP.gameLogFixedName();
    //    serverParam.set_allocated_game_log_fixed_name(&gameLogFixedName);
    //    std::string logDateFormat = SP.logDateFormat();
    //    serverParam.set_allocated_log_date_format(&logDateFormat);
    //    std::string teamLeftStartCommand = SP.teamLeftStartCommand();
    //    serverParam.set_allocated_team_l_start(&teamLeftStartCommand);
    //    std::string teamRightStartCommand = SP.teamRightStartCommand();
    //    serverParam.set_allocated_team_r_start(&teamRightStartCommand);
    //    std::string keepawayLogDir = SP.keepawayLogDir();
    //    serverParam.set_allocated_keepaway_log_dir(&keepawayLogDir);
    //    std::string keepawayLogFixedName = SP.keepawayLogFixedName();
    //    serverParam.set_allocated_keepaway_log_fixed_name(&keepawayLogFixedName);
    //    std::string moduleDir = SP.moduleDir();
    //    serverParam.set_allocated_module_dir(&moduleDir);
    //    std::string coachMsgFile = SP.coachMsgFile();
    //    serverParam.set_allocated_coach_msg_file(&coachMsgFile);
    //    std::string fixedTeamNameLeft = SP.fixedTeamNameLeft();
    //    serverParam.set_allocated_fixed_teamname_l(&fixedTeamNameLeft);
    //    std::string fixedTeamNameRight = SP.fixedTeamNameRight();
    //    serverParam.set_allocated_fixed_teamname_r(&fixedTeamNameRight);

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

    serverParam.set_pitch_half_length(SP.pitchHalfLength());
    serverParam.set_pitch_half_width(SP.pitchHalfWidth());
    serverParam.set_our_penalty_area_line_x(SP.ourPenaltyAreaLineX());
    serverParam.set_their_penalty_area_line_x(SP.theirPenaltyAreaLineX());
    serverParam.set_penalty_area_half_width(SP.penaltyAreaHalfWidth());
    serverParam.set_penalty_area_length(SP.penaltyAreaLength());

    ClientContext context;
    protos::Empty empty;
    protos::RegisterResponse* response = new protos::RegisterResponse(*M_register_response);
    serverParam.set_allocated_register_response(response);
    Status status = M_stub_->SendServerParams(&context, serverParam, &empty);
    if (!status.ok())
    {
        std::cout << "SendServerParams rpc failed." << std::endl
                  << status.error_code() << ": " << status.error_message()
                  << std::endl;
    }
}

void GrpcClient::sendPlayerParams() const
{
    protos::PlayerParam playerParam;
    const rcsc::PlayerParam &PP = rcsc::PlayerParam::i();

    playerParam.set_player_types(PP.playerTypes());
    playerParam.set_subs_max(PP.subsMax());
    playerParam.set_pt_max(PP.ptMax());
    playerParam.set_allow_mult_default_type(PP.allowMultDefaultType());
    playerParam.set_player_speed_max_delta_min(PP.playerSpeedMaxDeltaMin());
    playerParam.set_player_speed_max_delta_max(PP.playerSpeedMaxDeltaMax());
    playerParam.set_stamina_inc_max_delta_factor(PP.staminaIncMaxDeltaFactor());
    playerParam.set_player_decay_delta_min(PP.playerDecayDeltaMin());
    playerParam.set_player_decay_delta_max(PP.playerDecayDeltaMax());
    playerParam.set_inertia_moment_delta_factor(PP.inertiaMomentDeltaFactor());
    playerParam.set_dash_power_rate_delta_min(PP.dashPowerRateDeltaMin());
    playerParam.set_dash_power_rate_delta_max(PP.dashPowerRateDeltaMax());
    playerParam.set_player_size_delta_factor(PP.playerSizeDeltaFactor());
    playerParam.set_kickable_margin_delta_min(PP.kickableMarginDeltaMin());
    playerParam.set_kickable_margin_delta_max(PP.kickableMarginDeltaMax());
    playerParam.set_kick_rand_delta_factor(PP.kickRandDeltaFactor());
    playerParam.set_extra_stamina_delta_min(PP.extraStaminaDeltaMin());
    playerParam.set_extra_stamina_delta_max(PP.extraStaminaDeltaMax());
    playerParam.set_effort_max_delta_factor(PP.effortMaxDeltaFactor());
    playerParam.set_effort_min_delta_factor(PP.effortMinDeltaFactor());
    playerParam.set_random_seed(PP.randomSeed());
    playerParam.set_new_dash_power_rate_delta_min(PP.newDashPowerRateDeltaMin());
    playerParam.set_new_dash_power_rate_delta_max(PP.newDashPowerRateDeltaMax());
    playerParam.set_new_stamina_inc_max_delta_factor(PP.newStaminaIncMaxDeltaFactor());
    playerParam.set_kick_power_rate_delta_min(PP.kickPowerRateDeltaMin());
    playerParam.set_kick_power_rate_delta_max(PP.kickPowerRateDeltaMax());
    playerParam.set_foul_detect_probability_delta_factor(PP.foulDetectProbabilityDeltaFactor());
    playerParam.set_catchable_area_l_stretch_min(PP.catchAreaLengthStretchMin());
    playerParam.set_catchable_area_l_stretch_max(PP.catchAreaLengthStretchMax());

    ClientContext context;
    protos::Empty empty;
    protos::RegisterResponse* response = new protos::RegisterResponse(*M_register_response);
    playerParam.set_allocated_register_response(response);
    Status status = M_stub_->SendPlayerParams(&context, playerParam, &empty);
    if (!status.ok())
    {
        std::cout << "SendPlayerParams rpc failed." << std::endl
                  << status.error_code() << ": " << status.error_message()
                  << std::endl;
    }
}

void GrpcClient::sendPlayerType() const
{
    const rcsc::PlayerParam &PP = rcsc::PlayerParam::i();
    const rcsc::PlayerTypeSet &PT = rcsc::PlayerTypeSet::i();
    LOG("pt");
    LOG(PT.playerTypeMap().size());
    for (int i = 0; i < PT.playerTypeMap().size(); i++)
    {
        LOG(i);
        protos::PlayerType playerTypeGrpc;
        const rcsc::PlayerType *playerType = PT.get(i);

        playerTypeGrpc.set_id(playerType->id());
        playerTypeGrpc.set_player_speed_max(playerType->playerSpeedMax());
        playerTypeGrpc.set_stamina_inc_max(playerType->staminaIncMax());
        playerTypeGrpc.set_player_decay(playerType->playerDecay());
        playerTypeGrpc.set_inertia_moment(playerType->inertiaMoment());
        playerTypeGrpc.set_dash_power_rate(playerType->dashPowerRate());
        playerTypeGrpc.set_player_size(playerType->playerSize());
        playerTypeGrpc.set_kickable_margin(playerType->kickableMargin());
        playerTypeGrpc.set_kick_rand(playerType->kickRand());
        playerTypeGrpc.set_extra_stamina(playerType->extraStamina());
        playerTypeGrpc.set_effort_max(playerType->effortMax());
        playerTypeGrpc.set_effort_min(playerType->effortMin());
        playerTypeGrpc.set_kick_power_rate(playerType->kickPowerRate());
        playerTypeGrpc.set_foul_detect_probability(playerType->foulDetectProbability());
        playerTypeGrpc.set_catchable_area_l_stretch(playerType->catchAreaLengthStretch());
        playerTypeGrpc.set_unum_far_length(playerType->unumFarLength());
        playerTypeGrpc.set_unum_too_far_length(playerType->unumTooFarLength());
        playerTypeGrpc.set_team_far_length(playerType->teamFarLength());
        playerTypeGrpc.set_team_too_far_length(playerType->teamTooFarLength());
        playerTypeGrpc.set_player_max_observation_length(playerType->playerMaxObservationLength());
        playerTypeGrpc.set_ball_vel_far_length(playerType->ballVelFarLength());
        playerTypeGrpc.set_ball_vel_too_far_length(playerType->ballVelTooFarLength());
        playerTypeGrpc.set_ball_max_observation_length(playerType->ballMaxObservationLength());
        playerTypeGrpc.set_flag_chg_far_length(playerType->flagChgFarLength());
        playerTypeGrpc.set_flag_chg_too_far_length(playerType->flagChgTooFarLength());
        playerTypeGrpc.set_flag_max_observation_length(playerType->flagMaxObservationLength());
        playerTypeGrpc.set_kickable_area(playerType->kickableArea());
        playerTypeGrpc.set_reliable_catchable_dist(playerType->reliableCatchableDist());
        playerTypeGrpc.set_max_catchable_dist(playerType->maxCatchableDist());
        playerTypeGrpc.set_real_speed_max(playerType->realSpeedMax());
        playerTypeGrpc.set_player_speed_max2(playerType->playerSpeedMax2());
        playerTypeGrpc.set_real_speed_max2(playerType->realSpeedMax2());
        playerTypeGrpc.set_cycles_to_reach_max_speed(playerType->cyclesToReachMaxSpeed());

        ClientContext context;
        protos::Empty empty;
        protos::RegisterResponse* response = new protos::RegisterResponse(*M_register_response);
        playerTypeGrpc.set_allocated_register_response(response);
        Status status = M_stub_->SendPlayerType(&context, playerTypeGrpc, &empty);
        if (!status.ok())
        {
            std::cout << "SendPlayerType rpc failed. id=" << i << std::endl
                      << status.error_code() << ": " << status.error_message()
                      << std::endl;
        }
    }
}

void GrpcClient::sendInitMessage(bool offline_logging) const
{

    ClientContext context;
    protos::Empty empty;
    protos::InitMessage initMessage;
    initMessage.set_debug_mode(offline_logging);
    protos::RegisterResponse* response = new protos::RegisterResponse(*M_register_response);
    initMessage.set_allocated_register_response(response);
    Status status = M_stub_->SendInitMessage(&context, initMessage, &empty);
    if (!status.ok())
    {
        std::cout << "sendInitMessage rpc failed." << std::endl
                  << status.error_code() << ": " << status.error_message()
                  << std::endl;
    }
}

bool GrpcClient::Register() const
{
    ClientContext context;
    protos::RegisterRequest request;
    request.set_agent_type(M_agent_type);
    request.set_team_name(M_team_name);
    request.set_uniform_number(M_unum);

    Status status = M_stub_->Register(&context, request, M_register_response);
    if (!status.ok())
    {
        std::cout << "GetInitMessage rpc failed." << std::endl
                  << status.error_code() << ": " << status.error_message()
                  << std::endl;
        return false;
    }
    else
    {
        LOG("InitMessage received");
        LOGV(M_register_response->DebugString());
        return true;
    }
}

void GrpcClient::sendByeCommand() const
{
    ClientContext context;
    protos::Empty empty;

    Status status = M_stub_->SendByeCommand(&context, *M_register_response, &empty);
    if (!status.ok())
    {
        std::cout << "SendByeCommand rpc failed." << std::endl
                  << status.error_code() << ": " << status.error_message()
                  << std::endl;
    }

}

bool GrpcClient::connectToGrpcServer()
{
    M_channel = grpc::CreateChannel(this->M_target, grpc::InsecureChannelCredentials());
    M_stub_ = Game::NewStub(M_channel);

    if (Register())
    {
        M_is_connected = true;
        return true;
    }
    else
    {
        return false;
    }
}

void GrpcClient::addDlog(protos::Log log) const
{
    switch (log.log_case())
    {
    case protos::Log::kAddText:
    {
        const auto &addText = log.add_text();
        rcsc::dlog.addText(addText.level(), addText.message().c_str());
        break;
    }
    case protos::Log::kAddPoint:
    {
        const auto &addPoint = log.add_point();
        const auto &point = GrpcClient::convertVector2D(addPoint.point());
        rcsc::dlog.addPoint(addPoint.level(), point, addPoint.color().c_str());
        break;
    }
    case protos::Log::kAddLine:
    {
        const auto &addLine = log.add_line();
        const auto &point1 = GrpcClient::convertVector2D(addLine.start());
        const auto &point2 = GrpcClient::convertVector2D(addLine.end());
        rcsc::dlog.addLine(addLine.level(), point1, point2, addLine.color().c_str());
        break;
    }
    case protos::Log::kAddArc:
    {
        const auto &addArc = log.add_arc();
        const auto &center = GrpcClient::convertVector2D(addArc.center());
        rcsc::dlog.addArc(addArc.level(), center, addArc.radius(), addArc.start_angle(), addArc.span_angel(), addArc.color().c_str());
        break;
    }
    case protos::Log::kAddCircle:
    {
        const auto &addCircle = log.add_circle();
        const auto &center = GrpcClient::convertVector2D(addCircle.center());
        rcsc::dlog.addCircle(addCircle.level(), center, addCircle.radius(), addCircle.color().c_str(), addCircle.fill());
        break;
    }
    case protos::Log::kAddTriangle:
    {
        const auto &addTriangle = log.add_triangle();
        const auto &point1 = GrpcClient::convertVector2D(addTriangle.point1());
        const auto &point2 = GrpcClient::convertVector2D(addTriangle.point2());
        const auto &point3 = GrpcClient::convertVector2D(addTriangle.point3());
        rcsc::dlog.addTriangle(addTriangle.level(), point1, point2, point3, addTriangle.color().c_str(), addTriangle.fill());
        break;
    }
    case protos::Log::kAddRectangle:
    {
        const auto &addRectangle = log.add_rectangle();
        rcsc::dlog.addRect(addRectangle.level(), addRectangle.left(), addRectangle.top(), addRectangle.length(), addRectangle.width(), addRectangle.color().c_str(), addRectangle.fill());
        break;
    }
    case protos::Log::kAddSector:
    {
        const auto &addSector = log.add_sector();
        const auto &center = GrpcClient::convertVector2D(addSector.center());
        rcsc::dlog.addSector(addSector.level(), center, addSector.min_radius(), addSector.max_radius(), addSector.start_angle(), addSector.span_angel(), addSector.color().c_str(), addSector.fill());
        break;
    }
    case protos::Log::kAddMessage:
    {
        const auto &addMessage = log.add_message();
        const auto &position = GrpcClient::convertVector2D(addMessage.position());
        rcsc::dlog.addMessage(addMessage.level(), position, addMessage.message().c_str(), addMessage.color().c_str());
        break;
    }
    }
}

rcsc::ViewWidth GrpcClient::convertViewWidth(protos::ViewWidth view_width)
{
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

rcsc::SideID GrpcClient::convertSideID(protos::Side side)
{
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

rcsc::Vector2D GrpcClient::convertVector2D(protos::RpcVector2D vector2d)
{
    return rcsc::Vector2D(vector2d.x(), vector2d.y());
}