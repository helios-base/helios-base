namespace cpp soccer
namespace py soccer

enum ViewWidth {
  NARROW = 0,
  NORMAL = 1,
  WIDE = 2
}

enum AgentType {
  PlayerT = 0,
  CoachT = 1,
  TrainerT = 2
}

struct ThriftVector2D {
  1: double x,
  2: double y,
  3: double dist,
  4: double angle
}

struct Ball {
  1: ThriftVector2D position,
  2: ThriftVector2D relative_position,
  3: ThriftVector2D seen_position,
  4: ThriftVector2D heard_position,
  5: ThriftVector2D velocity,
  6: ThriftVector2D seen_velocity,
  7: ThriftVector2D heard_velocity,
  8: i32 pos_count,
  9: i32 seen_pos_count,
  10: i32 heard_pos_count,
  11: i32 vel_count,
  12: i32 seen_vel_count,
  13: i32 heard_vel_count,
  14: i32 lost_count,
  15: i32 ghost_count,
  16: double dist_from_self,
  17: double angle_from_self
}

enum Side {
  UNKNOWN = 0,
  LEFT = 1,
  RIGHT = 2
}

enum LoggerLevel {
  NoneLevel = 0,
  SYSTEM = 1,
  SENSOR = 2,
  WORLD = 4,
  ACTION = 8,
  INTERCEPT = 16,
  KICK = 32,
  HOLD = 64,
  DRIBBLE = 128,
  PASS = 256,
  CROSS = 512,
  SHOOT = 1024,
  CLEAR = 2048,
  BLOCK = 4096,
  MARK = 8192,
  POSITIONING = 16384,
  ROLE = 32768,
  TEAM = 65536,
  COMMUNICATION = 131072,
  ANALYZER = 262144,
  ACTION_CHAIN = 524288,
  PLAN = 1048576
}

struct Player {
  1: ThriftVector2D position,
  2: ThriftVector2D seen_position,
  3: ThriftVector2D heard_position,
  4: ThriftVector2D velocity,
  5: ThriftVector2D seen_velocity,
  6: i32 pos_count,
  7: i32 seen_pos_count,
  8: i32 heard_pos_count,
  9: i32 vel_count,
  10: i32 seen_vel_count,
  11: i32 ghost_count,
  12: double dist_from_self,
  13: double angle_from_self,
  14: i32 id,
  15: Side side,
  16: i32 uniform_number,
  17: i32 uniform_number_count,
  18: bool is_goalie,
  19: double body_direction,
  20: i32 body_direction_count,
  21: double face_direction,
  22: i32 face_direction_count,
  23: double point_to_direction,
  24: i32 point_to_direction_count,
  25: bool is_kicking,
  26: double dist_from_ball,
  27: double angle_from_ball,
  28: i32 ball_reach_steps,
  29: bool is_tackling,
  30: i32 type_id
}

struct Self {
  1: ThriftVector2D position,
  2: ThriftVector2D seen_position,
  3: ThriftVector2D heard_position,
  4: ThriftVector2D velocity,
  5: ThriftVector2D seen_velocity,
  6: i32 pos_count,
  7: i32 seen_pos_count,
  8: i32 heard_pos_count,
  9: i32 vel_count,
  10: i32 seen_vel_count,
  11: i32 ghost_count,
  12: i32 id,
  13: Side side,
  14: i32 uniform_number,
  15: i32 uniform_number_count,
  16: bool is_goalie,
  17: double body_direction,
  18: i32 body_direction_count,
  19: double face_direction,
  20: i32 face_direction_count,
  21: double point_to_direction,
  22: i32 point_to_direction_count,
  23: bool is_kicking,
  24: double dist_from_ball,
  25: double angle_from_ball,
  26: i32 ball_reach_steps,
  27: bool is_tackling,
  28: double relative_neck_direction,
  29: double stamina,
  30: bool is_kickable,
  31: double catch_probability,
  32: double tackle_probability,
  33: double foul_probability,
  34: ViewWidth view_width,
  35: i32 type_id,
  36: double kick_rate
}

enum InterceptActionType {
  UNKNOWN_Intercept_Action_Type = 0,
  OMNI_DASH = 1,
  TURN_FORWARD_DASH = 2,
  TURN_BACKWARD_DASH = 3
}

struct InterceptInfo {
  1: InterceptActionType action_type,
  2: i32 turn_steps,
  3: double turn_angle,
  4: i32 dash_steps,
  5: double dash_power,
  6: double dash_dir,
  7: ThriftVector2D final_self_position,
  8: double final_ball_dist,
  9: double final_stamina,
  10: double value
}

struct InterceptTable {
  1: i32 self_reach_steps,
  2: i32 first_teammate_reach_steps,
  3: i32 second_teammate_reach_steps,
  4: i32 first_opponent_reach_steps,
  5: i32 second_opponent_reach_steps,
  6: i32 first_teammate_id,
  7: i32 second_teammate_id,
  8: i32 first_opponent_id,
  9: i32 second_opponent_id,
  10: list<InterceptInfo> self_intercept_info
}

enum GameModeType {
  BeforeKickOff = 0,
  TimeOver = 1,
  PlayOn = 2,
  KickOff_ = 3,
  KickIn_ = 4,
  FreeKick_ = 5,
  CornerKick_ = 6,
  GoalKick_ = 7,
  AfterGoal_ = 8,
  OffSide_ = 9,
  PenaltyKick_ = 10,
  FirstHalfOver = 11,
  Pause = 12,
  Human = 13,
  FoulCharge_ = 14,
  FoulPush_ = 15,
  FoulMultipleAttacker_ = 16,
  FoulBallOut_ = 17,
  BackPass_ = 18,
  FreeKickFault_ = 19,
  CatchFault_ = 20,
  IndFreeKick_ = 21,
  PenaltySetup_ = 22,
  PenaltyReady_ = 23,
  PenaltyTaken_ = 24,
  PenaltyMiss_ = 25,
  PenaltyScore_ = 26,
  IllegalDefense_ = 27,
  PenaltyOnfield_ = 28,
  PenaltyFoul_ = 29,
  GoalieCatch_ = 30,
  ExtendHalf = 31,
  MODE_MAX = 32
}

struct WorldModel {
  1: InterceptTable intercept_table,
  2: string our_team_name,
  3: string their_team_name,
  4: Side our_side,
  5: i32 last_set_play_start_time,
  6: Self myself,
  7: Ball ball,
  8: list<Player> teammates,
  9: list<Player> opponents,
  10: list<Player> unknowns,
  11: map<i32, Player> our_players_dict,
  12: map<i32, Player> their_players_dict,
  13: i32 our_goalie_uniform_number,
  14: i32 their_goalie_uniform_number,
  15: double offside_line_x,
  16: i32 offside_line_x_count,
  17: i32 kickable_teammate_id,
  18: i32 kickable_opponent_id,
  19: Side last_kick_side,
  20: i32 last_kicker_uniform_number,
  21: i32 cycle,
  22: GameModeType game_mode_type,
  23: i32 left_team_score,
  24: i32 right_team_score,
  25: bool is_our_set_play,
  26: bool is_their_set_play,
  27: i32 stoped_cycle,
  28: i32 our_team_score,
  29: i32 their_team_score,
  30: bool is_penalty_kick_mode,
  31: map<i32, ThriftVector2D> helios_home_positions
}

struct State {
  1: AgentType agent_type,
  2: WorldModel world_model,
  3: WorldModel full_world_model
}

struct InitMessage {
  1: AgentType agent_type,
  2: bool debug_mode
}

struct Dash {
  1: double power,
  2: double relative_direction
}

struct Turn {
  1: double relative_direction
}

struct Kick {
  1: double power,
  2: double relative_direction
}

struct Tackle {
  1: double power_or_dir,
  2: bool foul
}

struct Catch {}

struct Move {
  1: double x,
  2: double y
}

struct TurnNeck {
  1: double moment
}

struct ChangeView {
  1: ViewWidth view_width
}

struct BallMessage {
  1: ThriftVector2D ball_position,
  2: ThriftVector2D ball_velocity
}

struct PassMessage {
  1: i32 receiver_uniform_number,
  2: ThriftVector2D receiver_point,
  3: ThriftVector2D ball_position,
  4: ThriftVector2D ball_velocity
}

struct InterceptMessage {
  1: bool our,
  2: i32 uniform_number,
  3: i32 cycle
}

struct GoalieMessage {
  1: i32 goalie_uniform_number,
  2: ThriftVector2D goalie_position,
  3: double goalie_body_direction
}

struct GoalieAndPlayerMessage {
  1: i32 goalie_uniform_number,
  2: ThriftVector2D goalie_position,
  3: double goalie_body_direction,
  4: i32 player_uniform_number,
  5: ThriftVector2D player_position
}

struct OffsideLineMessage {
  1: double offside_line_x
}

struct DefenseLineMessage {
  1: double defense_line_x
}

struct WaitRequestMessage {}

struct SetplayMessage {
  1: i32 wait_step
}

struct PassRequestMessage {
  1: ThriftVector2D target_point
}

struct StaminaMessage {
  1: double stamina
}

struct RecoveryMessage {
  1: double recovery
}

struct StaminaCapacityMessage {
  1: double stamina_capacity
}

struct DribbleMessage {
  1: ThriftVector2D target_point,
  2: i32 queue_count
}

struct BallGoalieMessage {
  1: ThriftVector2D ball_position,
  2: ThriftVector2D ball_velocity,
  3: ThriftVector2D goalie_position,
  4: double goalie_body_direction
}

struct OnePlayerMessage {
  1: i32 uniform_number,
  2: ThriftVector2D position
}

struct TwoPlayerMessage {
  1: i32 first_uniform_number,
  2: ThriftVector2D first_position,
  3: i32 second_uniform_number,
  4: ThriftVector2D second_position
}

struct ThreePlayerMessage {
  1: i32 first_uniform_number,
  2: ThriftVector2D first_position,
  3: i32 second_uniform_number,
  4: ThriftVector2D second_position,
  5: i32 third_uniform_number,
  6: ThriftVector2D third_position
}

struct SelfMessage {
  1: ThriftVector2D self_position,
  2: double self_body_direction,
  3: double self_stamina
}

struct TeammateMessage {
  1: i32 uniform_number,
  2: ThriftVector2D position,
  3: double body_direction
}

struct OpponentMessage {
  1: i32 uniform_number,
  2: ThriftVector2D position,
  3: double body_direction
}

struct BallPlayerMessage {
  1: ThriftVector2D ball_position,
  2: ThriftVector2D ball_velocity,
  3: i32 uniform_number,
  4: ThriftVector2D player_position,
  5: double body_direction
}

struct Say {
  1: optional BallMessage ball_message,
  2: optional PassMessage pass_message,
  3: optional InterceptMessage intercept_message,
  4: optional GoalieMessage goalie_message,
  5: optional GoalieAndPlayerMessage goalie_and_player_message,
  6: optional OffsideLineMessage offside_line_message,
  7: optional DefenseLineMessage defense_line_message,
  8: optional WaitRequestMessage wait_request_message,
  9: optional SetplayMessage setplay_message,
  10: optional PassRequestMessage pass_request_message,
  11: optional StaminaMessage stamina_message,
  12: optional RecoveryMessage recovery_message,
  13: optional StaminaCapacityMessage stamina_capacity_message,
  14: optional DribbleMessage dribble_message,
  15: optional BallGoalieMessage ball_goalie_message,
  16: optional OnePlayerMessage one_player_message,
  17: optional TwoPlayerMessage two_player_message,
  18: optional ThreePlayerMessage three_player_message,
  19: optional SelfMessage self_message,
  20: optional TeammateMessage teammate_message,
  21: optional OpponentMessage opponent_message,
  22: optional BallPlayerMessage ball_player_message
}

struct PointTo {
  1: double x,
  2: double y
}

struct PointToOf {}

struct AttentionTo {
  1: Side side,
  2: i32 unum
}

struct AttentionToOf {}

struct AddText {
  1: LoggerLevel level,
  2: string message
}

struct AddPoint {
  1: LoggerLevel level,
  2: ThriftVector2D point,
  3: string color
}

struct AddLine {
  1: LoggerLevel level,
  2: ThriftVector2D start_point,
  3: ThriftVector2D end_point,
  4: string color
}

struct AddArc {
  1: LoggerLevel level,
  2: ThriftVector2D center,
  3: double radius,
  4: double start_angle,
  5: double span_angel,
  6: string color
}

struct AddCircle {
  1: LoggerLevel level,
  2: ThriftVector2D center,
  3: double radius,
  4: string color,
  5: bool fill
}

struct AddTriangle {
  1: LoggerLevel level,
  2: ThriftVector2D point1,
  3: ThriftVector2D point2,
  4: ThriftVector2D point3,
  5: string color,
  6: bool fill
}

struct AddRectangle {
  1: LoggerLevel level,
  2: double left,
  3: double top,
  4: double length,
  5: double width,
  6: string color,
  7: bool fill
}

struct AddSector {
  1: LoggerLevel level,
  2: ThriftVector2D center,
  3: double min_radius,
  4: double max_radius,
  5: double start_angle,
  6: double span_angel,
  7: string color,
  8: bool fill
}

struct AddMessage {
  1: LoggerLevel level,
  2: ThriftVector2D position,
  3: string message,
  4: string color
}

struct Log {
  1: optional AddText add_text,
  2: optional AddPoint add_point,
  3: optional AddLine add_line,
  4: optional AddArc add_arc,
  5: optional AddCircle add_circle,
  6: optional AddTriangle add_triangle,
  7: optional AddRectangle add_rectangle,
  8: optional AddSector add_sector,
  9: optional AddMessage add_message
}

struct DebugClient {
  1: string message
}

struct Body_GoToPoint {
  1: ThriftVector2D target_point,
  2: double distance_threshold,
  3: double max_dash_power
}

struct Body_SmartKick {
  1: ThriftVector2D target_point,
  2: double first_speed,
  3: double first_speed_threshold,
  4: i32 max_steps
}

struct Bhv_BeforeKickOff {
  1: ThriftVector2D point
}

struct Bhv_BodyNeckToBall {}

struct Bhv_BodyNeckToPoint {
  1: ThriftVector2D point
}

struct Bhv_Emergency {}

struct Bhv_GoToPointLookBall {
  1: ThriftVector2D target_point,
  2: double distance_threshold,
  3: double max_dash_power
}

struct Bhv_NeckBodyToBall {
  1: double angle_buf
}

struct Bhv_NeckBodyToPoint {
  1: ThriftVector2D point,
  2: double angle_buf
}

struct Bhv_ScanField {}

struct Body_AdvanceBall {}

struct Body_ClearBall {}

struct Body_Dribble {
  1: ThriftVector2D target_point,
  2: double distance_threshold,
  3: double dash_power,
  4: i32 dash_count,
  5: bool dodge
}

struct Body_GoToPointDodge {
  1: ThriftVector2D target_point,
  2: double dash_power
}

struct Body_HoldBall {
  1: bool do_turn,
  2: ThriftVector2D turn_target_point,
  3: ThriftVector2D kick_target_point
}

struct Body_Intercept {
  1: bool save_recovery,
  2: ThriftVector2D face_point
}

struct Body_KickOneStep {
  1: ThriftVector2D target_point,
  2: double first_speed,
  3: bool force_mode
}

struct Body_StopBall {}

struct Body_StopDash {
  1: bool save_recovery
}

struct Body_TackleToPoint {
  1: ThriftVector2D target_point,
  2: double min_probability,
   3: double min_speed
}

struct Body_TurnToAngle {
  1: double angle
}

struct Body_TurnToBall {
  1: i32 cycle
}

struct Body_TurnToPoint {
  1: ThriftVector2D target_point,
  2: i32 cycle
}

struct Focus_MoveToPoint {
  1: ThriftVector2D target_point
}

struct Focus_Reset {}

struct Neck_ScanField {}

struct Neck_ScanPlayers {}

struct Neck_TurnToBallAndPlayer {
  1: Side side,
  2: i32 uniform_number,
  3: i32 count_threshold
}

struct Neck_TurnToBallOrScan {
  1: i32 count_threshold
}

struct Neck_TurnToBall {}

struct Neck_TurnToGoalieOrScan {
  1: i32 count_threshold
}

struct Neck_TurnToLowConfTeammate {}

struct Neck_TurnToPlayerOrScan {
  1: Side side,
  2: i32 uniform_number,
  3: i32 count_threshold
}

struct Neck_TurnToPoint {
  1: ThriftVector2D target_point
}

struct Neck_TurnToRelative {
  1: double angle
}

struct View_ChangeWidth {
  1: ViewWidth view_width
}

struct View_Normal {}

struct View_Synch {}

struct View_Wide {}

struct HeliosGoalie {}

struct HeliosGoalieMove {}

struct HeliosGoalieKick {}

struct HeliosShoot {}

struct HeliosChainAction {
  1: bool direct_pass,
  2: bool lead_pass,
  3: bool through_pass,
  4: bool short_dribble,
  5: bool long_dribble,
  6: bool cross,
  7: bool simple_pass,
  8: bool simple_dribble,
  9: bool simple_shoot
}

struct HeliosBasicOffensive {}

struct HeliosBasicMove {}

struct HeliosSetPlay {}

struct HeliosPenalty {}

struct HeliosCommunicaion {}

struct PlayerAction {
  1: optional Dash dash,
  2: optional Turn turn,
  3: optional Kick kick,
  4: optional Tackle tackle,
  5: optional Catch catch_action,
  6: optional Move move,
  7: optional TurnNeck turn_neck,
  8: optional ChangeView change_view,
  9: optional Say say,
  10: optional PointTo point_to,
  11: optional PointToOf point_to_of,
  12: optional AttentionTo attention_to,
  13: optional AttentionToOf attention_to_of,
  14: optional Log log,
  15: optional DebugClient debug_client,
  16: optional Body_GoToPoint body_go_to_point,
  17: optional Body_SmartKick body_smart_kick,
  18: optional Bhv_BeforeKickOff bhv_before_kick_off,
  19: optional Bhv_BodyNeckToBall bhv_body_neck_to_ball,
  20: optional Bhv_BodyNeckToPoint bhv_body_neck_to_point,
  21: optional Bhv_Emergency bhv_emergency,
  22: optional Bhv_GoToPointLookBall bhv_go_to_point_look_ball,
  23: optional Bhv_NeckBodyToBall bhv_neck_body_to_ball,
  24: optional Bhv_NeckBodyToPoint bhv_neck_body_to_point,
  25: optional Bhv_ScanField bhv_scan_field,
  26: optional Body_AdvanceBall body_advance_ball,
  27: optional Body_ClearBall body_clear_ball,
  28: optional Body_Dribble body_dribble,
  29: optional Body_GoToPointDodge body_go_to_point_dodge,
  30: optional Body_HoldBall body_hold_ball,
  31: optional Body_Intercept body_intercept,
  32: optional Body_KickOneStep body_kick_one_step,
  33: optional Body_StopBall body_stop_ball,
  34: optional Body_StopDash body_stop_dash,
  35: optional Body_TackleToPoint body_tackle_to_point,
  36: optional Body_TurnToAngle body_turn_to_angle,
  37: optional Body_TurnToBall body_turn_to_ball,
  38: optional Body_TurnToPoint body_turn_to_point,
  39: optional Focus_MoveToPoint focus_move_to_point,
  40: optional Focus_Reset focus_reset,
  41: optional Neck_ScanField neck_scan_field,
  42: optional Neck_ScanPlayers neck_scan_players,
  43: optional Neck_TurnToBallAndPlayer neck_turn_to_ball_and_player,
  44: optional Neck_TurnToBallOrScan neck_turn_to_ball_or_scan,
  45: optional Neck_TurnToBall neck_turn_to_ball,
  46: optional Neck_TurnToGoalieOrScan neck_turn_to_goalie_or_scan,
  47: optional Neck_TurnToLowConfTeammate neck_turn_to_low_conf_teammate,
  48: optional Neck_TurnToPlayerOrScan neck_turn_to_player_or_scan,
  49: optional Neck_TurnToPoint neck_turn_to_point,
  50: optional Neck_TurnToRelative neck_turn_to_relative,
  51: optional View_ChangeWidth view_change_width,
  52: optional View_Normal view_normal,
  53: optional View_Synch view_synch,
  54: optional View_Wide view_wide,
  55: optional HeliosGoalie helios_goalie,
  56: optional HeliosGoalieMove helios_goalie_move,
  57: optional HeliosGoalieKick helios_goalie_kick,
  58: optional HeliosShoot helios_shoot,
  59: optional HeliosChainAction helios_chain_action,
  60: optional HeliosBasicOffensive helios_basic_offensive,
  61: optional HeliosBasicMove helios_basic_move,
  62: optional HeliosSetPlay helios_set_play,
  63: optional HeliosPenalty helios_penalty,
  64: optional HeliosCommunicaion helios_communication
}

struct PlayerActions {
  1: list<PlayerAction> actions
}

struct ChangePlayerType {
  1: i32 uniform_number,
  2: i32 type
}

struct DoHeliosSubstitute {}

struct DoHeliosSayPlayerTypes {}

struct CoachAction {
  1: optional ChangePlayerType change_player_types,
  2: optional DoHeliosSubstitute do_helios_substitute,
  3: optional DoHeliosSayPlayerTypes do_helios_say_player_types
}

struct CoachActions {
  1: list<CoachAction> actions
}

struct DoKickOff {}

struct DoMoveBall {
  1: ThriftVector2D position,
  2: optional ThriftVector2D velocity
}

struct DoMovePlayer {
  1: bool our_side,
  2: i32 uniform_number,
  3: ThriftVector2D position,
  4: double body_direction
}

struct DoRecover {}

struct DoChangeMode {
  1: GameModeType game_mode_type,
  2: Side side
}

struct DoChangePlayerType {
  1: bool our_side,
  2: i32 uniform_number,
  3: i32 type
}

struct TrainerAction {
  1: optional DoKickOff do_kick_off,
  2: optional DoMoveBall do_move_ball,
  3: optional DoMovePlayer do_move_player,
  4: optional DoRecover do_recover,
  5: optional DoChangeMode do_change_mode,
  6: optional DoChangePlayerType do_change_player_type
}

struct TrainerActions {
  1: list<TrainerAction> actions
}

struct ServerParam {
  1: AgentType agent_type,
  2: double inertia_moment,
  3: double player_size,
  4: double player_decay,
  5: double player_rand,
  6: double player_weight,
  7: double player_speed_max,
  8: double player_accel_max,
  9: double stamina_max,
  10: double stamina_inc_max,
  11: double recover_init,
  12: double recover_dec_thr,
  13: double recover_min,
  14: double recover_dec,
  15: double effort_init,
  16: double effort_dec_thr,
  17: double effort_min,
  18: double effort_dec,
  19: double effort_inc_thr,
  20: double effort_inc,
  21: double kick_rand,
  22: bool team_actuator_noise,
  23: double player_rand_factor_l,
  24: double player_rand_factor_r,
  25: double kick_rand_factor_l,
  26: double kick_rand_factor_r,
  27: double ball_size,
  28: double ball_decay,
  29: double ball_rand,
  30: double ball_weight,
  31: double ball_speed_max,
  32: double ball_accel_max,
  33: double dash_power_rate,
  34: double kick_power_rate,
  35: double kickable_margin,
  36: double control_radius,
  37: double control_radius_width,
  38: double max_power,
  39: double min_power,
  40: double max_moment,
  41: double min_moment,
  42: double max_neck_moment,
  43: double min_neck_moment,
  44: double max_neck_angle,
  45: double min_neck_angle,
  46: double visible_angle,
  47: double visible_distance,
  48: double wind_dir,
  49: double wind_force,
  50: double wind_angle,
  51: double wind_rand,
  52: double kickable_area,
  53: double catch_area_l,
  54: double catch_area_w,
  55: double catch_probability,
  56: i32 goalie_max_moves,
  57: double corner_kick_margin,
  58: double offside_active_area_size,
  59: bool wind_none,
  60: bool use_wind_random,
  61: i32 coach_say_count_max,
  62: i32 coach_say_msg_size,
  63: i32 clang_win_size,
  64: i32 clang_define_win,
  65: i32 clang_meta_win,
  66: i32 clang_advice_win,
  67: i32 clang_info_win,
  68: i32 clang_mess_delay,
  69: i32 clang_mess_per_cycle,
  70: i32 half_time,
  71: i32 simulator_step,
  72: i32 send_step,
  73: i32 recv_step,
  74: i32 sense_body_step,
  75: i32 lcm_step,
  76: i32 player_say_msg_size,
  77: i32 player_hear_max,
  78: i32 player_hear_inc,
  79: i32 player_hear_decay,
  80: i32 catch_ban_cycle,
  81: i32 slow_down_factor,
  82: bool use_offside,
  83: bool kickoff_offside,
  84: double offside_kick_margin,
  85: double audio_cut_dist,
  86: double dist_quantize_step,
  87: double landmark_dist_quantize_step,
  88: double dir_quantize_step,
  89: double dist_quantize_step_l,
  90: double dist_quantize_step_r,
  91: double landmark_dist_quantize_step_l,
  92: double landmark_dist_quantize_step_r,
  93: double dir_quantize_step_l,
  94: double dir_quantize_step_r,
  95: bool coach_mode,
  96: bool coach_with_referee_mode,
  97: bool use_old_coach_hear,
  98: double slowness_on_top_for_left_team,
  99: double slowness_on_top_for_right_team,
  100: i32 start_goal_l,
  101: i32 start_goal_r,
  102: bool fullstate_l,
  103: bool fullstate_r,
  104: i32 drop_ball_time,
  105: bool synch_mode,
  106: i32 synch_offset,
  107: i32 synch_micro_sleep,
  108: i32 point_to_ban,
  109: i32 point_to_duration,
  110: i32 player_port,
  111: i32 trainer_port,
  112: i32 online_coach_port,
  113: bool verbose_mode,
  114: i32 coach_send_vi_step,
  115: string replay_file,
  116: string landmark_file,
  117: bool send_comms,
  118: bool text_logging,
  119: bool game_logging,
  120: i32 game_log_version,
  121: string text_log_dir,
  122: string game_log_dir,
  123: string text_log_fixed_name,
  124: string game_log_fixed_name,
  125: bool use_text_log_fixed,
  126: bool use_game_log_fixed,
  127: bool use_text_log_dated,
  128: bool use_game_log_dated,
  129: string log_date_format,
  130: bool log_times,
  131: bool record_message,
  132: i32 text_log_compression,
  133: i32 game_log_compression,
  134: bool use_profile,
  135: double tackle_dist,
  136: double tackle_back_dist,
  137: double tackle_width,
  138: double tackle_exponent,
  139: i32 tackle_cycles,
  140: double tackle_power_rate,
  141: i32 freeform_wait_period,
  142: i32 freeform_send_period,
  143: bool free_kick_faults,
  144: bool back_passes,
  145: bool proper_goal_kicks,
  146: double stopped_ball_vel,
  147: i32 max_goal_kicks,
  148: i32 clang_del_win,
  149: i32 clang_rule_win,
  150: bool auto_mode,
  151: i32 kick_off_wait,
  152: i32 connect_wait,
  153: i32 game_over_wait,
  154: string team_l_start,
  155: string team_r_start,
  156: bool keepaway_mode,
  157: double keepaway_length,
  158: double keepaway_width,
  159: bool keepaway_logging,
  160: string keepaway_log_dir,
  161: string keepaway_log_fixed_name,
  162: bool keepaway_log_fixed,
  163: bool keepaway_log_dated,
  164: i32 keepaway_start,
  165: i32 nr_normal_halfs,
  166: i32 nr_extra_halfs,
  167: bool penalty_shoot_outs,
  168: i32 pen_before_setup_wait,
  169: i32 pen_setup_wait,
  170: i32 pen_ready_wait,
  171: i32 pen_taken_wait,
  172: i32 pen_nr_kicks,
  173: i32 pen_max_extra_kicks,
  174: double pen_dist_x,
  175: bool pen_random_winner,
  176: bool pen_allow_mult_kicks,
  177: double pen_max_goalie_dist_x,
  178: bool pen_coach_moves_players,
  179: string module_dir,
  180: double ball_stuck_area,
  181: string coach_msg_file,
  182: double max_tackle_power,
  183: double max_back_tackle_power,
  184: double player_speed_max_min,
  185: double extra_stamina,
  186: i32 synch_see_offset,
  187: i32 extra_half_time,
  188: double stamina_capacity,
  189: double max_dash_angle,
  190: double min_dash_angle,
  191: double dash_angle_step,
  192: double side_dash_rate,
  193: double back_dash_rate,
  194: double max_dash_power,
  195: double min_dash_power,
  196: double tackle_rand_factor,
  197: double foul_detect_probability,
  198: double foul_exponent,
  199: i32 foul_cycles,
  200: bool golden_goal,
  201: double red_card_probability,
  202: i32 illegal_defense_duration,
  203: i32 illegal_defense_number,
  204: double illegal_defense_dist_x,
  205: double illegal_defense_width,
  206: string fixed_teamname_l,
  207: string fixed_teamname_r,
  208: double max_catch_angle,
  209: double min_catch_angle,
  210: i32 random_seed,
  211: double long_kick_power_factor,
  212: i32 long_kick_delay,
  213: i32 max_monitors,
  214: double catchable_area,
  215: double real_speed_max,
  216: double pitch_half_length,
  217: double pitch_half_width,
  218: double our_penalty_area_line_x,
  219: double their_penalty_area_line_x,
  220: double penalty_area_half_width,
  221: double penalty_area_length,
  222: double goal_width
}

struct PlayerParam {
  1: AgentType agent_type,
  2: i32 player_types,
  3: i32 subs_max,
  4: i32 pt_max,
  5: bool allow_mult_default_type,
  6: double player_speed_max_delta_min,
  7: double player_speed_max_delta_max,
  8: double stamina_inc_max_delta_factor,
  9: double player_decay_delta_min,
  10: double player_decay_delta_max,
  11: double inertia_moment_delta_factor,
  12: double dash_power_rate_delta_min,
  13: double dash_power_rate_delta_max,
  14: double player_size_delta_factor,
  15: double kickable_margin_delta_min,
  16: double kickable_margin_delta_max,
  17: double kick_rand_delta_factor,
  18: double extra_stamina_delta_min,
  19: double extra_stamina_delta_max,
  20: double effort_max_delta_factor,
  21: double effort_min_delta_factor,
  22: i32 random_seed,
  23: double new_dash_power_rate_delta_min,
  24: double new_dash_power_rate_delta_max,
  25: double new_stamina_inc_max_delta_factor,
  26: double kick_power_rate_delta_min,
   27: double kick_power_rate_delta_max,
  28: double foul_detect_probability_delta_factor,
  29: double catchable_area_l_stretch_min,
  30: double catchable_area_l_stretch_max
}

struct PlayerType {
  1: AgentType agent_type,
  2: i32 id,
  3: double stamina_inc_max,
  4: double player_decay,
  5: double inertia_moment,
  6: double dash_power_rate,
  7: double player_size,
  8: double kickable_margin,
  9: double kick_rand,
  10: double extra_stamina,
  11: double effort_max,
  12: double effort_min,
  13: double kick_power_rate,
  14: double foul_detect_probability,
  15: double catchable_area_l_stretch,
  16: double unum_far_length,
  17: double unum_too_far_length,
  18: double team_far_length,
  19: double team_too_far_length,
  20: double player_max_observation_length,
  21: double ball_vel_far_length,
  22: double ball_vel_too_far_length,
  23: double ball_max_observation_length,
  24: double flag_chg_far_length,
  25: double flag_chg_too_far_length,
  26: double flag_max_observation_length,
  27: double kickable_area,
  28: double reliable_catchable_dist,
  29: double max_catchable_dist,
  30: double real_speed_max,
  31: double player_speed_max2,
  32: double real_speed_max2,
  33: i32 cycles_to_reach_max_speed,
  34: double player_speed_max
}

struct Empty {}

struct InitMessageFromServer {}

service Game {
  PlayerActions GetPlayerActions(1: State state),
  CoachActions GetCoachActions(1: State state),
  TrainerActions GetTrainerActions(1: State state),
  void SendInitMessage(1: InitMessage init_message),
  void SendServerParams(1: ServerParam server_param),
  void SendPlayerParams(1: PlayerParam player_param),
  void SendPlayerType(1: PlayerType player_type),
  InitMessageFromServer GetInitMessage(1: Empty empty),
  void SendByeCommand(1: Empty empty)
}

