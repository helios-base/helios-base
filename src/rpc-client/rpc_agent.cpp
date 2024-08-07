#include "rpc_agent.h"
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

void RpcAgent::sendParams(bool offline_logging)
{
    if (!param_sent)
    {
        LOG("sendParams Started");
        sendServerParam();
        sendPlayerParams();
        sendPlayerType();
        sendInitMessage(offline_logging);
        param_sent = true;
        LOG("sendParams Done");
    }
}
void RpcAgent::sendServerParam() const
{
    LOG("sendServerParam Started");

    soccer::ServerParam serverParam;
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

    serverParam.goal_width = SP.goalWidth();
    serverParam.inertia_moment = SP.defaultInertiaMoment();
    serverParam.player_size = SP.defaultPlayerSize();
    serverParam.player_decay = SP.defaultPlayerDecay();
    serverParam.player_rand = SP.playerRand();
    serverParam.player_weight = SP.playerWeight();
    serverParam.player_speed_max = SP.defaultPlayerSpeedMax();
    serverParam.player_accel_max = SP.playerAccelMax();
    serverParam.stamina_max = SP.staminaMax();
    serverParam.stamina_inc_max = SP.defaultStaminaIncMax();
    serverParam.recover_init = SP.recoverInit();
    serverParam.recover_dec_thr = SP.recoverDecThr();
    serverParam.recover_min = SP.recoverMin();
    serverParam.recover_dec = SP.recoverDec();
    serverParam.effort_init = SP.effortInit();
    serverParam.effort_dec_thr = SP.effortDecThr();
    serverParam.effort_min = SP.defaultEffortMin();
    serverParam.effort_dec = SP.effortDec();
    serverParam.effort_inc_thr = SP.effortIncThr();
    serverParam.effort_inc = SP.effortInc();
    serverParam.kick_rand = SP.defaultKickRand();
    serverParam.team_actuator_noise = SP.teamActuatorNoise();
    serverParam.player_rand_factor_l = SP.playerRandFactorLeft();
    serverParam.player_rand_factor_r = SP.playerRandFactorRight();
    serverParam.kick_rand_factor_l = SP.kickRandFactorLeft();
    serverParam.kick_rand_factor_r = SP.kickRandFactorRight();
    serverParam.ball_size = SP.ballSize();
    serverParam.ball_decay = SP.ballDecay();
    serverParam.ball_rand = SP.ballRand();
    serverParam.ball_weight = SP.ballWeight();
    serverParam.ball_speed_max = SP.ballSpeedMax();
    serverParam.ball_accel_max = SP.ballAccelMax();
    serverParam.dash_power_rate = SP.defaultDashPowerRate();
    serverParam.kick_power_rate = SP.kickPowerRate();
    serverParam.kickable_margin = SP.defaultKickableMargin();
    serverParam.control_radius = SP.controlRadius();
    serverParam.control_radius_width = SP.controlRadiusWidth();
    serverParam.max_power = SP.maxPower();
    serverParam.min_power = SP.minPower();
    serverParam.max_moment = SP.maxMoment();
    serverParam.min_moment = SP.minMoment();
    serverParam.max_neck_moment = SP.maxNeckMoment();
    serverParam.min_neck_moment = SP.minNeckMoment();
    serverParam.max_neck_angle = SP.maxNeckAngle();
    serverParam.min_neck_angle = SP.minNeckAngle();
    serverParam.visible_angle = SP.visibleAngle();
    serverParam.visible_distance = SP.visibleDistance();
    serverParam.wind_dir = SP.windDir();
    serverParam.wind_force = SP.windForce();
    serverParam.wind_angle = SP.windAngle();
    serverParam.wind_rand = SP.windRand();
    serverParam.kickable_area = SP.defaultKickableArea();
    serverParam.catch_area_l = SP.catchAreaLength();
    serverParam.catch_area_w = SP.catchAreaWidth();
    serverParam.catch_probability = SP.catchProbability();
    serverParam.goalie_max_moves = SP.goalieMaxMoves();
    serverParam.corner_kick_margin = SP.cornerKickMargin();
    serverParam.offside_active_area_size = SP.offsideActiveAreaSize();
    serverParam.wind_none = SP.windNone();
    serverParam.use_wind_random = SP.useWindRandom();
    serverParam.coach_say_count_max = SP.coachSayCountMax();
    serverParam.coach_say_msg_size = SP.coachSayMsgSize();
    serverParam.clang_win_size = SP.clangWinSize();
    serverParam.clang_define_win = SP.clangDefineWin();
    serverParam.clang_meta_win = SP.clangMetaWin();
    serverParam.clang_advice_win = SP.clangAdviceWin();
    serverParam.clang_info_win = SP.clangInfoWin();
    serverParam.clang_mess_delay = SP.clangMessDelay();
    serverParam.clang_mess_per_cycle = SP.clangMessPerCycle();
    serverParam.half_time = SP.halfTime();
    serverParam.simulator_step = SP.simulatorStep();
    serverParam.send_step = SP.sendStep();
    serverParam.recv_step = SP.recvStep();
    serverParam.sense_body_step = SP.senseBodyStep();
    serverParam.lcm_step = SP.lcmStep();
    serverParam.player_say_msg_size = SP.playerSayMsgSize();
    serverParam.player_hear_max = SP.playerHearMax();
    serverParam.player_hear_inc = SP.playerHearInc();
    serverParam.player_hear_decay = SP.playerHearDecay();
    serverParam.catch_ban_cycle = SP.catchBanCycle();
    serverParam.slow_down_factor = SP.slowDownFactor();
    serverParam.use_offside = SP.useOffside();
    serverParam.kickoff_offside = SP.kickoffOffside();
    serverParam.offside_kick_margin = SP.offsideKickMargin();
    serverParam.audio_cut_dist = SP.audioCutDist();
    serverParam.dist_quantize_step = SP.distQuantizeStep();
    serverParam.landmark_dist_quantize_step = SP.landmarkDistQuantizeStep();
    serverParam.dir_quantize_step = SP.dirQuantizeStep();
    serverParam.dist_quantize_step_l = SP.landmarkDistQuantizeStepLeft();
    serverParam.dist_quantize_step_r = SP.distQuantizeStepRight();
    serverParam.landmark_dist_quantize_step_l = SP.landmarkDistQuantizeStepLeft();
    serverParam.landmark_dist_quantize_step_r = SP.landmarkDistQuantizeStepRight();
    serverParam.dir_quantize_step_l = SP.dirQuantizeStepLeft();
    serverParam.dir_quantize_step_r = SP.dirQuantizeStepRight();
    serverParam.coach_mode = SP.coachMode();
    serverParam.coach_with_referee_mode = SP.coachWithRefereeMode();
    serverParam.use_old_coach_hear = SP.useOldCoachHear();
    serverParam.slowness_on_top_for_left_team = SP.slownessOnTopForLeft();
    serverParam.slowness_on_top_for_right_team = SP.slownessOnTopForRight();
    serverParam.start_goal_l = SP.startGoalLeft();
    serverParam.start_goal_r = SP.stargGoalRight();
    serverParam.fullstate_l = SP.fullstateLeft();
    serverParam.fullstate_r = SP.fullstateRight();
    serverParam.drop_ball_time = SP.dropBallTime();
    serverParam.synch_mode = SP.synchMode();
    serverParam.synch_offset = SP.synchOffset();
    serverParam.synch_micro_sleep = SP.synchMicroSleep();
    serverParam.point_to_ban = SP.pointToBan();
    serverParam.point_to_duration = SP.pointToDuration();
    serverParam.player_port = SP.playerPort();
    serverParam.trainer_port = SP.trainerPort();
    serverParam.online_coach_port = SP.onlineCoachPort();
    serverParam.verbose_mode = SP.verboseMode();
    serverParam.coach_send_vi_step = SP.coachSendVIStep();
    serverParam.send_comms = SP.sendComms();
    serverParam.text_logging = SP.textLogging();
    serverParam.game_logging = SP.gameLogging();
    serverParam.game_log_version = SP.gameLogVersion();
    serverParam.use_text_log_fixed = SP.textLogFixed();
    serverParam.use_game_log_fixed = SP.gameLogFixed();
    serverParam.use_text_log_dated = SP.textLogDated();
    serverParam.use_game_log_dated = SP.gameLogDated();
    serverParam.log_times = SP.logTimes();
    serverParam.record_message = SP.recordMessage();
    serverParam.text_log_compression = SP.textLogCompression();
    serverParam.game_log_compression = SP.gameLogCompression();
    serverParam.use_profile = SP.useProfile();
    serverParam.tackle_dist = SP.tackleDist();
    serverParam.tackle_back_dist = SP.tackleBackDist();
    serverParam.tackle_width = SP.tackleWidth();
    serverParam.tackle_exponent = SP.tackleExponent();
    serverParam.tackle_cycles = SP.tackleCycles();
    serverParam.tackle_power_rate = SP.tacklePowerRate();
    serverParam.freeform_wait_period = SP.freeformWaitPeriod();
    serverParam.freeform_send_period = SP.freeformSendPeriod();
    serverParam.free_kick_faults = SP.freeKickFaults();
    serverParam.back_passes = SP.backPasses();
    serverParam.proper_goal_kicks = SP.properGoalKicks();
    serverParam.stopped_ball_vel = SP.stoppedBallVel();
    serverParam.max_goal_kicks = SP.maxGoalKicks();
    serverParam.clang_del_win = SP.clangDelWin();
    serverParam.clang_rule_win = SP.clangRuleWin();
    serverParam.auto_mode = SP.autoMode();
    serverParam.kick_off_wait = SP.kickOffWait();
    serverParam.connect_wait = SP.connectWait();
    serverParam.game_over_wait = SP.gameOverWait();
    serverParam.keepaway_mode = SP.keepawayMode();
    serverParam.keepaway_length = SP.keepawayLength();
    serverParam.keepaway_width = SP.keepawayWidth();
    serverParam.keepaway_logging = SP.keepawayLogging();
    serverParam.keepaway_log_fixed = SP.keepawayLogFixed();
    serverParam.keepaway_log_dated = SP.keepawayLogDated();
    serverParam.keepaway_start = SP.keepawayStart();
    serverParam.nr_normal_halfs = SP.nrNormalHalfs();
    serverParam.nr_extra_halfs = SP.nrExtraHalfs();
    serverParam.penalty_shoot_outs = SP.penaltyShootOuts();
    serverParam.pen_before_setup_wait = SP.penBeforeSetupWait();
    serverParam.pen_setup_wait = SP.penSetupWait();
    serverParam.pen_ready_wait = SP.penReadyWait();
    serverParam.pen_taken_wait = SP.penTakenWait();
    serverParam.pen_nr_kicks = SP.penNrKicks();
    serverParam.pen_max_extra_kicks = SP.penMaxExtraKicks();
    serverParam.pen_dist_x = SP.penDistX();
    serverParam.pen_random_winner = SP.penRandomWinner();
    serverParam.pen_allow_mult_kicks = SP.penAllowMultKicks();
    serverParam.pen_max_goalie_dist_x = SP.penMaxGoalieDistX();
    serverParam.pen_coach_moves_players = SP.penCoachMovesPlayers();
    serverParam.ball_stuck_area = SP.ballStuckArea();
    serverParam.max_tackle_power = SP.maxTacklePower();
    serverParam.max_back_tackle_power = SP.maxBackTacklePower();
    serverParam.player_speed_max_min = SP.playerSpeedMaxMin();
    serverParam.extra_stamina = SP.defaultExtraStamina();
    serverParam.synch_see_offset = SP.synchSeeOffset();
    serverParam.extra_half_time = SP.extraHalfTime();
    serverParam.stamina_capacity = SP.staminaCapacity();
    serverParam.max_dash_angle = SP.maxDashAngle();
    serverParam.min_dash_angle = SP.minDashAngle();
    serverParam.dash_angle_step = SP.dashAngleStep();
    serverParam.side_dash_rate = SP.sideDashRate();
    serverParam.back_dash_rate = SP.backDashRate();
    serverParam.max_dash_power = SP.maxDashPower();
    serverParam.min_dash_power = SP.minDashPower();
    serverParam.tackle_rand_factor = SP.tackleRandFactor();
    serverParam.foul_detect_probability = SP.foulDetectProbability();
    serverParam.foul_exponent = SP.foulExponent();
    serverParam.foul_cycles = SP.foulCycles();
    serverParam.golden_goal = SP.goldenGoal();
    serverParam.red_card_probability = SP.redCardProbability();
    serverParam.illegal_defense_duration = SP.illegalDefenseDuration();
    serverParam.illegal_defense_number = SP.illegalDefenseNumber();
    serverParam.illegal_defense_dist_x = SP.illegalDefenseDistX();
    serverParam.illegal_defense_width = SP.illegalDefenseWidth();
    serverParam.max_catch_angle = SP.maxCatchAngle();
    serverParam.min_catch_angle = SP.minCatchAngle();
    serverParam.random_seed = SP.randomSeed();
    serverParam.long_kick_power_factor = SP.longKickPowerFactor();
    serverParam.long_kick_delay = SP.longKickDelay();
    serverParam.max_monitors = SP.maxMonitors();
    serverParam.catchable_area = SP.catchableArea();
    serverParam.real_speed_max = SP.defaultRealSpeedMax();
    serverParam.pitch_half_length = SP.pitchHalfLength();
    serverParam.pitch_half_width = SP.pitchHalfWidth();
    serverParam.our_penalty_area_line_x = SP.ourPenaltyAreaLineX();
    serverParam.their_penalty_area_line_x = SP.theirPenaltyAreaLineX();
    serverParam.penalty_area_half_width = SP.penaltyAreaHalfWidth();
    serverParam.penalty_area_length = SP.penaltyAreaLength();

    try{
        soccer::Empty empty;
        client->SendServerParams(empty, register_response, serverParam);
    }
    catch(const std::exception& e){
        std::cout << "SendServerParams rpc failed." << std::endl
                  << e.what()
                  << std::endl;
    }
}

void RpcAgent::sendPlayerParams() const
{
    LOG("sendPlayerParams Started");
    soccer::PlayerParam playerParam;
    const rcsc::PlayerParam &PP = rcsc::PlayerParam::i();
    playerParam.agent_type = this->agent_type;
    playerParam.player_types = PP.playerTypes();
    playerParam.subs_max = PP.subsMax();
    playerParam.pt_max = PP.ptMax();
    playerParam.allow_mult_default_type = PP.allowMultDefaultType();
    playerParam.player_speed_max_delta_min = PP.playerSpeedMaxDeltaMin();
    playerParam.player_speed_max_delta_max = PP.playerSpeedMaxDeltaMax();
    playerParam.stamina_inc_max_delta_factor = PP.staminaIncMaxDeltaFactor();
    playerParam.player_decay_delta_min = PP.playerDecayDeltaMin();
    playerParam.player_decay_delta_max = PP.playerDecayDeltaMax();
    playerParam.inertia_moment_delta_factor = PP.inertiaMomentDeltaFactor();
    playerParam.dash_power_rate_delta_min = PP.dashPowerRateDeltaMin();
    playerParam.dash_power_rate_delta_max = PP.dashPowerRateDeltaMax();
    playerParam.player_size_delta_factor = PP.playerSizeDeltaFactor();
    playerParam.kickable_margin_delta_min = PP.kickableMarginDeltaMin();
    playerParam.kickable_margin_delta_max = PP.kickableMarginDeltaMax();
    playerParam.kick_rand_delta_factor = PP.kickRandDeltaFactor();
    playerParam.extra_stamina_delta_min = PP.extraStaminaDeltaMin();
    playerParam.extra_stamina_delta_max = PP.extraStaminaDeltaMax();
    playerParam.effort_max_delta_factor = PP.effortMaxDeltaFactor();
    playerParam.effort_min_delta_factor = PP.effortMinDeltaFactor();
    playerParam.random_seed = PP.randomSeed();
    playerParam.new_dash_power_rate_delta_min = PP.newDashPowerRateDeltaMin();
    playerParam.new_dash_power_rate_delta_max = PP.newDashPowerRateDeltaMax();
    playerParam.new_stamina_inc_max_delta_factor = PP.newStaminaIncMaxDeltaFactor();
    playerParam.kick_power_rate_delta_min = PP.kickPowerRateDeltaMin();
    playerParam.kick_power_rate_delta_max = PP.kickPowerRateDeltaMax();
    playerParam.foul_detect_probability_delta_factor = PP.foulDetectProbabilityDeltaFactor();
    playerParam.catchable_area_l_stretch_min = PP.catchAreaLengthStretchMin();
    playerParam.catchable_area_l_stretch_max = PP.catchAreaLengthStretchMax();

    try
    {
        soccer::Empty empty;
        client->SendPlayerParams(empty, register_response, playerParam);
    }
    catch(const std::exception& e){
        std::cout << "SendPlayerParams rpc failed." << std::endl
                  << e.what()
                  << std::endl;
    }
}

void RpcAgent::sendPlayerType() const
{
    LOG("sendPlayerType Started");
    const rcsc::PlayerParam &PP = rcsc::PlayerParam::i();
    const rcsc::PlayerTypeSet &PT = rcsc::PlayerTypeSet::i();
    for (int i = 0; i < PT.playerTypeMap().size(); i++)
    {
        LOG(i);
        soccer::PlayerType playerTypeGrpc;
        const rcsc::PlayerType *playerType = PT.get(i);

        playerTypeGrpc.id = playerType->id();
        playerTypeGrpc.player_speed_max = playerType->playerSpeedMax();
        playerTypeGrpc.stamina_inc_max = playerType->staminaIncMax();
        playerTypeGrpc.player_decay = playerType->playerDecay();
        playerTypeGrpc.inertia_moment = playerType->inertiaMoment();
        playerTypeGrpc.dash_power_rate = playerType->dashPowerRate();
        playerTypeGrpc.player_size = playerType->playerSize();
        playerTypeGrpc.kickable_margin = playerType->kickableMargin();
        playerTypeGrpc.kick_rand = playerType->kickRand();
        playerTypeGrpc.extra_stamina = playerType->extraStamina();
        playerTypeGrpc.effort_max = playerType->effortMax();
        playerTypeGrpc.effort_min = playerType->effortMin();
        playerTypeGrpc.kick_power_rate = playerType->kickPowerRate();
        playerTypeGrpc.foul_detect_probability = playerType->foulDetectProbability();
        playerTypeGrpc.catchable_area_l_stretch = playerType->catchAreaLengthStretch();
        playerTypeGrpc.unum_far_length = playerType->unumFarLength();
        playerTypeGrpc.unum_too_far_length = playerType->unumTooFarLength();
        playerTypeGrpc.team_far_length = playerType->teamFarLength();
        playerTypeGrpc.team_too_far_length = playerType->teamTooFarLength();
        playerTypeGrpc.player_max_observation_length = playerType->playerMaxObservationLength();
        playerTypeGrpc.ball_vel_far_length = playerType->ballVelFarLength();
        playerTypeGrpc.ball_vel_too_far_length = playerType->ballVelTooFarLength();
        playerTypeGrpc.ball_max_observation_length = playerType->ballMaxObservationLength();
        playerTypeGrpc.flag_chg_far_length = playerType->flagChgFarLength();
        playerTypeGrpc.flag_chg_too_far_length = playerType->flagChgTooFarLength();
        playerTypeGrpc.flag_max_observation_length = playerType->flagMaxObservationLength();
        playerTypeGrpc.kickable_area = playerType->kickableArea();
        playerTypeGrpc.reliable_catchable_dist = playerType->reliableCatchableDist();
        playerTypeGrpc.max_catchable_dist = playerType->maxCatchableDist();
        playerTypeGrpc.real_speed_max = playerType->realSpeedMax();
        playerTypeGrpc.player_speed_max2 = playerType->playerSpeedMax2();
        playerTypeGrpc.real_speed_max2 = playerType->realSpeedMax2();
        playerTypeGrpc.cycles_to_reach_max_speed = playerType->cyclesToReachMaxSpeed();
        try{
            soccer::Empty empty;
            playerTypeGrpc.agent_type = this->agent_type;
            client->SendPlayerType(empty, register_response, playerTypeGrpc);
        }
        catch(const std::exception& e){
            std::cout << "SendPlayerType rpc failed. id=" << i << std::endl
                      << e.what()
                      << std::endl;
        }
    }
}

void RpcAgent::sendInitMessage(bool offline_logging) const
{
    soccer::Empty empty;
    soccer::InitMessage initMessage;
    initMessage.debug_mode = offline_logging;
    initMessage.agent_type = this->agent_type;
    try{
        client->SendInitMessage(empty, register_response, initMessage);
    }
    catch(const std::exception& e){
        std::cout << "sendInitMessage rpc failed." << std::endl
                  << e.what()
                  << std::endl;
    }
}

bool RpcAgent::Register()
{
    std::cout<<"Getting InitMessage..."<<std::endl;
    soccer::Empty empty;
    soccer::RegisterRequest registerRequest;
    registerRequest.agent_type = agent_type;
    registerRequest.uniform_number = unum;
    registerRequest.team_name = team_name;
    try{
        client->Register(register_response, registerRequest);
        LOG("InitMessage received");
        return true;
    }
    catch(const std::exception& e){
        std::cout << "GetInitMessage rpc failed." << std::endl
                  << e.what()
                  << std::endl;
        return false;
    }
}

void RpcAgent::sendByeCommand() const
{
    try{
        soccer::Empty empty;
        soccer::Empty empty2;
        client->SendByeCommand(empty, register_response);
    }
    catch(const std::exception& e){
        std::cout << "SendByeCommand rpc failed." << std::endl
                  << e.what()
                  << std::endl;
    }
}

bool RpcAgent::connectToGrpcServer()
{
    std::cout<<"Connecting to server..."<<std::endl;
    socket = std::make_shared<TSocket>(server_host, server_port);

    // Wrap the socket in a buffered transport
    transport = std::make_shared<TBufferedTransport>(socket);

    // Create a binary protocol to use for the transport
    protocol = std::make_shared<TBinaryProtocol>(transport);

    // Open the transport
//    transport->open();

    // Create a client to use the protocol encoder
    client = std::make_shared<soccer::GameClient>(protocol);
    transport->open();
    if (Register())
    {
        is_connected = true;
        std::cout<<"Connected to server."<<std::endl;
        return true;
    }
    else
    {
        std::cout<<"Failed to connect to server."<<std::endl;
        return false;
    }
}

void RpcAgent::addDlog(soccer::Log log) const
{
    if (log.__isset.add_text){
        const auto &addText = log.add_text;
        rcsc::dlog.addText(addText.level, addText.message.c_str());
    }

    if (log.__isset.add_point){
        const auto &addPoint = log.add_point;
        const auto &point = RpcAgent::convertVector2D(addPoint.point);
        rcsc::dlog.addPoint(addPoint.level, point, addPoint.color.c_str());
    }

    if (log.__isset.add_line){
        const auto &addLine = log.add_line;
        const auto &point1 = RpcAgent::convertVector2D(addLine.start_point);
        const auto &point2 = RpcAgent::convertVector2D(addLine.end_point);
        rcsc::dlog.addLine(addLine.level, point1, point2, addLine.color.c_str());
    }

    if (log.__isset.add_arc){
        const auto &addArc = log.add_arc;
        const auto &center = RpcAgent::convertVector2D(addArc.center);
        rcsc::dlog.addArc(addArc.level, center, addArc.radius, addArc.start_angle, addArc.span_angel, addArc.color.c_str());
    }

    if (log.__isset.add_circle){
        const auto &addCircle = log.add_circle;
        const auto &center = RpcAgent::convertVector2D(addCircle.center);
        rcsc::dlog.addCircle(addCircle.level, center, addCircle.radius, addCircle.color.c_str(), addCircle.fill);
    }

    if (log.__isset.add_triangle){
        const auto &addTriangle = log.add_triangle;
        const auto &point1 = RpcAgent::convertVector2D(addTriangle.point1);
        const auto &point2 = RpcAgent::convertVector2D(addTriangle.point2);
        const auto &point3 = RpcAgent::convertVector2D(addTriangle.point3);
        rcsc::dlog.addTriangle(addTriangle.level, point1, point2, point3, addTriangle.color.c_str(), addTriangle.fill);
    }

    if (log.__isset.add_rectangle){
        const auto &addRectangle = log.add_rectangle;
        rcsc::dlog.addRect(addRectangle.level, addRectangle.left, addRectangle.top, addRectangle.length, addRectangle.width, addRectangle.color.c_str(), addRectangle.fill);
    }

    if (log.__isset.add_sector){
        const auto &addSector = log.add_sector;
        const auto &center = RpcAgent::convertVector2D(addSector.center);
        rcsc::dlog.addSector(addSector.level, center, addSector.min_radius, addSector.max_radius, addSector.start_angle, addSector.span_angel, addSector.color.c_str(), addSector.fill);
    }

    if (log.__isset.add_message){
        const auto &addMessage = log.add_message;
        const auto &position = RpcAgent::convertVector2D(addMessage.position);
        rcsc::dlog.addMessage(addMessage.level, position, addMessage.message.c_str(), addMessage.color.c_str());
    }
}

rcsc::ViewWidth RpcAgent::convertViewWidth(soccer::ViewWidth::type view_width)
{
    switch (view_width)
    {
    case soccer::ViewWidth::NARROW:
        return rcsc::ViewWidth::NARROW;
    case soccer::ViewWidth::NORMAL:
        return rcsc::ViewWidth::NORMAL;
    case soccer::ViewWidth::WIDE:
        return rcsc::ViewWidth::WIDE;
    default:
        return rcsc::ViewWidth::NORMAL;
    }
}

rcsc::SideID RpcAgent::convertSideID(soccer::Side::type side)
{
    switch (side)
    {
    case soccer::Side::LEFT:
        return rcsc::SideID::LEFT;
    case soccer::Side::RIGHT:
        return rcsc::SideID::RIGHT;
    default:
        return rcsc::SideID::LEFT;
    }
}

rcsc::Vector2D RpcAgent::convertVector2D(soccer::ThriftVector2D vector2d)
{
    return rcsc::Vector2D(vector2d.x, vector2d.y);
}