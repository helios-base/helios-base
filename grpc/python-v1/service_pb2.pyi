from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ViewWidth(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NARROW: _ClassVar[ViewWidth]
    NORMAL: _ClassVar[ViewWidth]
    WIDE: _ClassVar[ViewWidth]

class Side(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN: _ClassVar[Side]
    LEFT: _ClassVar[Side]
    RIGHT: _ClassVar[Side]

class LoggerLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    None: _ClassVar[LoggerLevel]
    SYSTEM: _ClassVar[LoggerLevel]
    SENSOR: _ClassVar[LoggerLevel]
    WORLD: _ClassVar[LoggerLevel]
    ACTION: _ClassVar[LoggerLevel]
    INTERCEPT: _ClassVar[LoggerLevel]
    KICK: _ClassVar[LoggerLevel]
    HOLD: _ClassVar[LoggerLevel]
    DRIBBLE: _ClassVar[LoggerLevel]
    PASS: _ClassVar[LoggerLevel]
    CROSS: _ClassVar[LoggerLevel]
    SHOOT: _ClassVar[LoggerLevel]
    CLEAR: _ClassVar[LoggerLevel]
    BLOCK: _ClassVar[LoggerLevel]
    MARK: _ClassVar[LoggerLevel]
    POSITIONING: _ClassVar[LoggerLevel]
    ROLE: _ClassVar[LoggerLevel]
    TEAM: _ClassVar[LoggerLevel]
    COMMUNICATION: _ClassVar[LoggerLevel]
    ANALYZER: _ClassVar[LoggerLevel]
    ACTION_CHAIN: _ClassVar[LoggerLevel]
    PLAN: _ClassVar[LoggerLevel]

class InterceptActionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN_Intercept_Action_Type: _ClassVar[InterceptActionType]
    OMNI_DASH: _ClassVar[InterceptActionType]
    TURN_FORWARD_DASH: _ClassVar[InterceptActionType]
    TURN_BACKWARD_DASH: _ClassVar[InterceptActionType]

class GameModeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BeforeKickOff: _ClassVar[GameModeType]
    TimeOver: _ClassVar[GameModeType]
    PlayOn: _ClassVar[GameModeType]
    KickOff_: _ClassVar[GameModeType]
    KickIn_: _ClassVar[GameModeType]
    FreeKick_: _ClassVar[GameModeType]
    CornerKick_: _ClassVar[GameModeType]
    GoalKick_: _ClassVar[GameModeType]
    AfterGoal_: _ClassVar[GameModeType]
    OffSide_: _ClassVar[GameModeType]
    PenaltyKick_: _ClassVar[GameModeType]
    FirstHalfOver: _ClassVar[GameModeType]
    Pause: _ClassVar[GameModeType]
    Human: _ClassVar[GameModeType]
    FoulCharge_: _ClassVar[GameModeType]
    FoulPush_: _ClassVar[GameModeType]
    FoulMultipleAttacker_: _ClassVar[GameModeType]
    FoulBallOut_: _ClassVar[GameModeType]
    BackPass_: _ClassVar[GameModeType]
    FreeKickFault_: _ClassVar[GameModeType]
    CatchFault_: _ClassVar[GameModeType]
    IndFreeKick_: _ClassVar[GameModeType]
    PenaltySetup_: _ClassVar[GameModeType]
    PenaltyReady_: _ClassVar[GameModeType]
    PenaltyTaken_: _ClassVar[GameModeType]
    PenaltyMiss_: _ClassVar[GameModeType]
    PenaltyScore_: _ClassVar[GameModeType]
    IllegalDefense_: _ClassVar[GameModeType]
    PenaltyOnfield_: _ClassVar[GameModeType]
    PenaltyFoul_: _ClassVar[GameModeType]
    GoalieCatch_: _ClassVar[GameModeType]
    ExtendHalf: _ClassVar[GameModeType]
    MODE_MAX: _ClassVar[GameModeType]
NARROW: ViewWidth
NORMAL: ViewWidth
WIDE: ViewWidth
UNKNOWN: Side
LEFT: Side
RIGHT: Side
None: LoggerLevel
SYSTEM: LoggerLevel
SENSOR: LoggerLevel
WORLD: LoggerLevel
ACTION: LoggerLevel
INTERCEPT: LoggerLevel
KICK: LoggerLevel
HOLD: LoggerLevel
DRIBBLE: LoggerLevel
PASS: LoggerLevel
CROSS: LoggerLevel
SHOOT: LoggerLevel
CLEAR: LoggerLevel
BLOCK: LoggerLevel
MARK: LoggerLevel
POSITIONING: LoggerLevel
ROLE: LoggerLevel
TEAM: LoggerLevel
COMMUNICATION: LoggerLevel
ANALYZER: LoggerLevel
ACTION_CHAIN: LoggerLevel
PLAN: LoggerLevel
UNKNOWN_Intercept_Action_Type: InterceptActionType
OMNI_DASH: InterceptActionType
TURN_FORWARD_DASH: InterceptActionType
TURN_BACKWARD_DASH: InterceptActionType
BeforeKickOff: GameModeType
TimeOver: GameModeType
PlayOn: GameModeType
KickOff_: GameModeType
KickIn_: GameModeType
FreeKick_: GameModeType
CornerKick_: GameModeType
GoalKick_: GameModeType
AfterGoal_: GameModeType
OffSide_: GameModeType
PenaltyKick_: GameModeType
FirstHalfOver: GameModeType
Pause: GameModeType
Human: GameModeType
FoulCharge_: GameModeType
FoulPush_: GameModeType
FoulMultipleAttacker_: GameModeType
FoulBallOut_: GameModeType
BackPass_: GameModeType
FreeKickFault_: GameModeType
CatchFault_: GameModeType
IndFreeKick_: GameModeType
PenaltySetup_: GameModeType
PenaltyReady_: GameModeType
PenaltyTaken_: GameModeType
PenaltyMiss_: GameModeType
PenaltyScore_: GameModeType
IllegalDefense_: GameModeType
PenaltyOnfield_: GameModeType
PenaltyFoul_: GameModeType
GoalieCatch_: GameModeType
ExtendHalf: GameModeType
MODE_MAX: GameModeType

class Vector2D(_message.Message):
    __slots__ = ("x", "y", "dist", "angle")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    DIST_FIELD_NUMBER: _ClassVar[int]
    ANGLE_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    dist: float
    angle: float
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ..., dist: _Optional[float] = ..., angle: _Optional[float] = ...) -> None: ...

class Ball(_message.Message):
    __slots__ = ("position", "relative_position", "seen_position", "heard_position", "velocity", "seen_velocity", "heard_velocity", "pos_count", "seen_pos_count", "heard_pos_count", "vel_count", "seen_vel_count", "heard_vel_count", "lost_count", "ghost_count", "dist_from_self", "angle_from_self")
    POSITION_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_POSITION_FIELD_NUMBER: _ClassVar[int]
    SEEN_POSITION_FIELD_NUMBER: _ClassVar[int]
    HEARD_POSITION_FIELD_NUMBER: _ClassVar[int]
    VELOCITY_FIELD_NUMBER: _ClassVar[int]
    SEEN_VELOCITY_FIELD_NUMBER: _ClassVar[int]
    HEARD_VELOCITY_FIELD_NUMBER: _ClassVar[int]
    POS_COUNT_FIELD_NUMBER: _ClassVar[int]
    SEEN_POS_COUNT_FIELD_NUMBER: _ClassVar[int]
    HEARD_POS_COUNT_FIELD_NUMBER: _ClassVar[int]
    VEL_COUNT_FIELD_NUMBER: _ClassVar[int]
    SEEN_VEL_COUNT_FIELD_NUMBER: _ClassVar[int]
    HEARD_VEL_COUNT_FIELD_NUMBER: _ClassVar[int]
    LOST_COUNT_FIELD_NUMBER: _ClassVar[int]
    GHOST_COUNT_FIELD_NUMBER: _ClassVar[int]
    DIST_FROM_SELF_FIELD_NUMBER: _ClassVar[int]
    ANGLE_FROM_SELF_FIELD_NUMBER: _ClassVar[int]
    position: Vector2D
    relative_position: Vector2D
    seen_position: Vector2D
    heard_position: Vector2D
    velocity: Vector2D
    seen_velocity: Vector2D
    heard_velocity: Vector2D
    pos_count: int
    seen_pos_count: int
    heard_pos_count: int
    vel_count: int
    seen_vel_count: int
    heard_vel_count: int
    lost_count: int
    ghost_count: int
    dist_from_self: float
    angle_from_self: float
    def __init__(self, position: _Optional[_Union[Vector2D, _Mapping]] = ..., relative_position: _Optional[_Union[Vector2D, _Mapping]] = ..., seen_position: _Optional[_Union[Vector2D, _Mapping]] = ..., heard_position: _Optional[_Union[Vector2D, _Mapping]] = ..., velocity: _Optional[_Union[Vector2D, _Mapping]] = ..., seen_velocity: _Optional[_Union[Vector2D, _Mapping]] = ..., heard_velocity: _Optional[_Union[Vector2D, _Mapping]] = ..., pos_count: _Optional[int] = ..., seen_pos_count: _Optional[int] = ..., heard_pos_count: _Optional[int] = ..., vel_count: _Optional[int] = ..., seen_vel_count: _Optional[int] = ..., heard_vel_count: _Optional[int] = ..., lost_count: _Optional[int] = ..., ghost_count: _Optional[int] = ..., dist_from_self: _Optional[float] = ..., angle_from_self: _Optional[float] = ...) -> None: ...

class Player(_message.Message):
    __slots__ = ("position", "seen_position", "heard_position", "velocity", "seen_velocity", "pos_count", "seen_pos_count", "heard_pos_count", "vel_count", "seen_vel_count", "ghost_count", "dist_from_self", "angle_from_self", "id", "side", "uniform_number", "uniform_number_count", "is_goalie", "body_direction", "body_direction_count", "face_direction", "face_direction_count", "point_to_direction", "point_to_direction_count", "is_kicking", "dist_from_ball", "angle_from_ball", "ball_reach_steps", "is_tackling", "type_id")
    POSITION_FIELD_NUMBER: _ClassVar[int]
    SEEN_POSITION_FIELD_NUMBER: _ClassVar[int]
    HEARD_POSITION_FIELD_NUMBER: _ClassVar[int]
    VELOCITY_FIELD_NUMBER: _ClassVar[int]
    SEEN_VELOCITY_FIELD_NUMBER: _ClassVar[int]
    POS_COUNT_FIELD_NUMBER: _ClassVar[int]
    SEEN_POS_COUNT_FIELD_NUMBER: _ClassVar[int]
    HEARD_POS_COUNT_FIELD_NUMBER: _ClassVar[int]
    VEL_COUNT_FIELD_NUMBER: _ClassVar[int]
    SEEN_VEL_COUNT_FIELD_NUMBER: _ClassVar[int]
    GHOST_COUNT_FIELD_NUMBER: _ClassVar[int]
    DIST_FROM_SELF_FIELD_NUMBER: _ClassVar[int]
    ANGLE_FROM_SELF_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    SIDE_FIELD_NUMBER: _ClassVar[int]
    UNIFORM_NUMBER_FIELD_NUMBER: _ClassVar[int]
    UNIFORM_NUMBER_COUNT_FIELD_NUMBER: _ClassVar[int]
    IS_GOALIE_FIELD_NUMBER: _ClassVar[int]
    BODY_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    BODY_DIRECTION_COUNT_FIELD_NUMBER: _ClassVar[int]
    FACE_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    FACE_DIRECTION_COUNT_FIELD_NUMBER: _ClassVar[int]
    POINT_TO_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    POINT_TO_DIRECTION_COUNT_FIELD_NUMBER: _ClassVar[int]
    IS_KICKING_FIELD_NUMBER: _ClassVar[int]
    DIST_FROM_BALL_FIELD_NUMBER: _ClassVar[int]
    ANGLE_FROM_BALL_FIELD_NUMBER: _ClassVar[int]
    BALL_REACH_STEPS_FIELD_NUMBER: _ClassVar[int]
    IS_TACKLING_FIELD_NUMBER: _ClassVar[int]
    TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    position: Vector2D
    seen_position: Vector2D
    heard_position: Vector2D
    velocity: Vector2D
    seen_velocity: Vector2D
    pos_count: int
    seen_pos_count: int
    heard_pos_count: int
    vel_count: int
    seen_vel_count: int
    ghost_count: int
    dist_from_self: float
    angle_from_self: float
    id: int
    side: Side
    uniform_number: int
    uniform_number_count: int
    is_goalie: bool
    body_direction: float
    body_direction_count: int
    face_direction: float
    face_direction_count: int
    point_to_direction: float
    point_to_direction_count: int
    is_kicking: bool
    dist_from_ball: float
    angle_from_ball: float
    ball_reach_steps: int
    is_tackling: bool
    type_id: int
    def __init__(self, position: _Optional[_Union[Vector2D, _Mapping]] = ..., seen_position: _Optional[_Union[Vector2D, _Mapping]] = ..., heard_position: _Optional[_Union[Vector2D, _Mapping]] = ..., velocity: _Optional[_Union[Vector2D, _Mapping]] = ..., seen_velocity: _Optional[_Union[Vector2D, _Mapping]] = ..., pos_count: _Optional[int] = ..., seen_pos_count: _Optional[int] = ..., heard_pos_count: _Optional[int] = ..., vel_count: _Optional[int] = ..., seen_vel_count: _Optional[int] = ..., ghost_count: _Optional[int] = ..., dist_from_self: _Optional[float] = ..., angle_from_self: _Optional[float] = ..., id: _Optional[int] = ..., side: _Optional[_Union[Side, str]] = ..., uniform_number: _Optional[int] = ..., uniform_number_count: _Optional[int] = ..., is_goalie: bool = ..., body_direction: _Optional[float] = ..., body_direction_count: _Optional[int] = ..., face_direction: _Optional[float] = ..., face_direction_count: _Optional[int] = ..., point_to_direction: _Optional[float] = ..., point_to_direction_count: _Optional[int] = ..., is_kicking: bool = ..., dist_from_ball: _Optional[float] = ..., angle_from_ball: _Optional[float] = ..., ball_reach_steps: _Optional[int] = ..., is_tackling: bool = ..., type_id: _Optional[int] = ...) -> None: ...

class Self(_message.Message):
    __slots__ = ("position", "seen_position", "heard_position", "velocity", "seen_velocity", "pos_count", "seen_pos_count", "heard_pos_count", "vel_count", "seen_vel_count", "ghost_count", "id", "side", "uniform_number", "uniform_number_count", "is_goalie", "body_direction", "body_direction_count", "face_direction", "face_direction_count", "point_to_direction", "point_to_direction_count", "is_kicking", "dist_from_ball", "angle_from_ball", "ball_reach_steps", "is_tackling", "relative_neck_direction", "stamina", "is_kickable", "catch_probability", "tackle_probability", "foul_probability", "view_width", "type_id", "kick_rate")
    POSITION_FIELD_NUMBER: _ClassVar[int]
    SEEN_POSITION_FIELD_NUMBER: _ClassVar[int]
    HEARD_POSITION_FIELD_NUMBER: _ClassVar[int]
    VELOCITY_FIELD_NUMBER: _ClassVar[int]
    SEEN_VELOCITY_FIELD_NUMBER: _ClassVar[int]
    POS_COUNT_FIELD_NUMBER: _ClassVar[int]
    SEEN_POS_COUNT_FIELD_NUMBER: _ClassVar[int]
    HEARD_POS_COUNT_FIELD_NUMBER: _ClassVar[int]
    VEL_COUNT_FIELD_NUMBER: _ClassVar[int]
    SEEN_VEL_COUNT_FIELD_NUMBER: _ClassVar[int]
    GHOST_COUNT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    SIDE_FIELD_NUMBER: _ClassVar[int]
    UNIFORM_NUMBER_FIELD_NUMBER: _ClassVar[int]
    UNIFORM_NUMBER_COUNT_FIELD_NUMBER: _ClassVar[int]
    IS_GOALIE_FIELD_NUMBER: _ClassVar[int]
    BODY_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    BODY_DIRECTION_COUNT_FIELD_NUMBER: _ClassVar[int]
    FACE_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    FACE_DIRECTION_COUNT_FIELD_NUMBER: _ClassVar[int]
    POINT_TO_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    POINT_TO_DIRECTION_COUNT_FIELD_NUMBER: _ClassVar[int]
    IS_KICKING_FIELD_NUMBER: _ClassVar[int]
    DIST_FROM_BALL_FIELD_NUMBER: _ClassVar[int]
    ANGLE_FROM_BALL_FIELD_NUMBER: _ClassVar[int]
    BALL_REACH_STEPS_FIELD_NUMBER: _ClassVar[int]
    IS_TACKLING_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_NECK_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    STAMINA_FIELD_NUMBER: _ClassVar[int]
    IS_KICKABLE_FIELD_NUMBER: _ClassVar[int]
    CATCH_PROBABILITY_FIELD_NUMBER: _ClassVar[int]
    TACKLE_PROBABILITY_FIELD_NUMBER: _ClassVar[int]
    FOUL_PROBABILITY_FIELD_NUMBER: _ClassVar[int]
    VIEW_WIDTH_FIELD_NUMBER: _ClassVar[int]
    TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    KICK_RATE_FIELD_NUMBER: _ClassVar[int]
    position: Vector2D
    seen_position: Vector2D
    heard_position: Vector2D
    velocity: Vector2D
    seen_velocity: Vector2D
    pos_count: int
    seen_pos_count: int
    heard_pos_count: int
    vel_count: int
    seen_vel_count: int
    ghost_count: int
    id: int
    side: Side
    uniform_number: int
    uniform_number_count: int
    is_goalie: bool
    body_direction: float
    body_direction_count: int
    face_direction: float
    face_direction_count: int
    point_to_direction: float
    point_to_direction_count: int
    is_kicking: bool
    dist_from_ball: float
    angle_from_ball: float
    ball_reach_steps: int
    is_tackling: bool
    relative_neck_direction: float
    stamina: float
    is_kickable: bool
    catch_probability: float
    tackle_probability: float
    foul_probability: float
    view_width: ViewWidth
    type_id: int
    kick_rate: float
    def __init__(self, position: _Optional[_Union[Vector2D, _Mapping]] = ..., seen_position: _Optional[_Union[Vector2D, _Mapping]] = ..., heard_position: _Optional[_Union[Vector2D, _Mapping]] = ..., velocity: _Optional[_Union[Vector2D, _Mapping]] = ..., seen_velocity: _Optional[_Union[Vector2D, _Mapping]] = ..., pos_count: _Optional[int] = ..., seen_pos_count: _Optional[int] = ..., heard_pos_count: _Optional[int] = ..., vel_count: _Optional[int] = ..., seen_vel_count: _Optional[int] = ..., ghost_count: _Optional[int] = ..., id: _Optional[int] = ..., side: _Optional[_Union[Side, str]] = ..., uniform_number: _Optional[int] = ..., uniform_number_count: _Optional[int] = ..., is_goalie: bool = ..., body_direction: _Optional[float] = ..., body_direction_count: _Optional[int] = ..., face_direction: _Optional[float] = ..., face_direction_count: _Optional[int] = ..., point_to_direction: _Optional[float] = ..., point_to_direction_count: _Optional[int] = ..., is_kicking: bool = ..., dist_from_ball: _Optional[float] = ..., angle_from_ball: _Optional[float] = ..., ball_reach_steps: _Optional[int] = ..., is_tackling: bool = ..., relative_neck_direction: _Optional[float] = ..., stamina: _Optional[float] = ..., is_kickable: bool = ..., catch_probability: _Optional[float] = ..., tackle_probability: _Optional[float] = ..., foul_probability: _Optional[float] = ..., view_width: _Optional[_Union[ViewWidth, str]] = ..., type_id: _Optional[int] = ..., kick_rate: _Optional[float] = ...) -> None: ...

class InterceptInfo(_message.Message):
    __slots__ = ("action_type", "turn_steps", "turn_angle", "dash_steps", "dash_power", "dash_dir", "final_self_position", "final_ball_dist", "final_stamina", "value")
    ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    TURN_STEPS_FIELD_NUMBER: _ClassVar[int]
    TURN_ANGLE_FIELD_NUMBER: _ClassVar[int]
    DASH_STEPS_FIELD_NUMBER: _ClassVar[int]
    DASH_POWER_FIELD_NUMBER: _ClassVar[int]
    DASH_DIR_FIELD_NUMBER: _ClassVar[int]
    FINAL_SELF_POSITION_FIELD_NUMBER: _ClassVar[int]
    FINAL_BALL_DIST_FIELD_NUMBER: _ClassVar[int]
    FINAL_STAMINA_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    action_type: InterceptActionType
    turn_steps: int
    turn_angle: float
    dash_steps: int
    dash_power: float
    dash_dir: float
    final_self_position: Vector2D
    final_ball_dist: float
    final_stamina: float
    value: float
    def __init__(self, action_type: _Optional[_Union[InterceptActionType, str]] = ..., turn_steps: _Optional[int] = ..., turn_angle: _Optional[float] = ..., dash_steps: _Optional[int] = ..., dash_power: _Optional[float] = ..., dash_dir: _Optional[float] = ..., final_self_position: _Optional[_Union[Vector2D, _Mapping]] = ..., final_ball_dist: _Optional[float] = ..., final_stamina: _Optional[float] = ..., value: _Optional[float] = ...) -> None: ...

class InterceptTable(_message.Message):
    __slots__ = ("self_reach_steps", "first_teammate_reach_steps", "second_teammate_reach_steps", "first_opponent_reach_steps", "second_opponent_reach_steps", "first_teammate_id", "second_teammate_id", "first_opponent_id", "second_opponent_id", "self_intercept_info")
    SELF_REACH_STEPS_FIELD_NUMBER: _ClassVar[int]
    FIRST_TEAMMATE_REACH_STEPS_FIELD_NUMBER: _ClassVar[int]
    SECOND_TEAMMATE_REACH_STEPS_FIELD_NUMBER: _ClassVar[int]
    FIRST_OPPONENT_REACH_STEPS_FIELD_NUMBER: _ClassVar[int]
    SECOND_OPPONENT_REACH_STEPS_FIELD_NUMBER: _ClassVar[int]
    FIRST_TEAMMATE_ID_FIELD_NUMBER: _ClassVar[int]
    SECOND_TEAMMATE_ID_FIELD_NUMBER: _ClassVar[int]
    FIRST_OPPONENT_ID_FIELD_NUMBER: _ClassVar[int]
    SECOND_OPPONENT_ID_FIELD_NUMBER: _ClassVar[int]
    SELF_INTERCEPT_INFO_FIELD_NUMBER: _ClassVar[int]
    self_reach_steps: int
    first_teammate_reach_steps: int
    second_teammate_reach_steps: int
    first_opponent_reach_steps: int
    second_opponent_reach_steps: int
    first_teammate_id: int
    second_teammate_id: int
    first_opponent_id: int
    second_opponent_id: int
    self_intercept_info: _containers.RepeatedCompositeFieldContainer[InterceptInfo]
    def __init__(self, self_reach_steps: _Optional[int] = ..., first_teammate_reach_steps: _Optional[int] = ..., second_teammate_reach_steps: _Optional[int] = ..., first_opponent_reach_steps: _Optional[int] = ..., second_opponent_reach_steps: _Optional[int] = ..., first_teammate_id: _Optional[int] = ..., second_teammate_id: _Optional[int] = ..., first_opponent_id: _Optional[int] = ..., second_opponent_id: _Optional[int] = ..., self_intercept_info: _Optional[_Iterable[_Union[InterceptInfo, _Mapping]]] = ...) -> None: ...

class WorldModel(_message.Message):
    __slots__ = ("intercept_table", "our_team_name", "their_team_name", "our_side", "last_set_play_start_time", "self", "ball", "teammates", "opponents", "unknowns", "our_players_dict", "their_players_dict", "our_goalie_uniform_number", "their_goalie_uniform_number", "offside_line_x", "ofside_line_x_count", "kickable_teammate_id", "kickable_opponent_id", "last_kick_side", "last_kicker_uniform_number", "cycle", "game_mode_type", "left_team_score", "right_team_score", "is_our_set_play", "is_their_set_play", "stoped_cycle", "our_team_score", "their_team_score")
    class OurPlayersDictEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: Player
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[Player, _Mapping]] = ...) -> None: ...
    class TheirPlayersDictEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: Player
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[Player, _Mapping]] = ...) -> None: ...
    INTERCEPT_TABLE_FIELD_NUMBER: _ClassVar[int]
    OUR_TEAM_NAME_FIELD_NUMBER: _ClassVar[int]
    THEIR_TEAM_NAME_FIELD_NUMBER: _ClassVar[int]
    OUR_SIDE_FIELD_NUMBER: _ClassVar[int]
    LAST_SET_PLAY_START_TIME_FIELD_NUMBER: _ClassVar[int]
    SELF_FIELD_NUMBER: _ClassVar[int]
    BALL_FIELD_NUMBER: _ClassVar[int]
    TEAMMATES_FIELD_NUMBER: _ClassVar[int]
    OPPONENTS_FIELD_NUMBER: _ClassVar[int]
    UNKNOWNS_FIELD_NUMBER: _ClassVar[int]
    OUR_PLAYERS_DICT_FIELD_NUMBER: _ClassVar[int]
    THEIR_PLAYERS_DICT_FIELD_NUMBER: _ClassVar[int]
    OUR_GOALIE_UNIFORM_NUMBER_FIELD_NUMBER: _ClassVar[int]
    THEIR_GOALIE_UNIFORM_NUMBER_FIELD_NUMBER: _ClassVar[int]
    OFFSIDE_LINE_X_FIELD_NUMBER: _ClassVar[int]
    OFSIDE_LINE_X_COUNT_FIELD_NUMBER: _ClassVar[int]
    KICKABLE_TEAMMATE_ID_FIELD_NUMBER: _ClassVar[int]
    KICKABLE_OPPONENT_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_KICK_SIDE_FIELD_NUMBER: _ClassVar[int]
    LAST_KICKER_UNIFORM_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CYCLE_FIELD_NUMBER: _ClassVar[int]
    GAME_MODE_TYPE_FIELD_NUMBER: _ClassVar[int]
    LEFT_TEAM_SCORE_FIELD_NUMBER: _ClassVar[int]
    RIGHT_TEAM_SCORE_FIELD_NUMBER: _ClassVar[int]
    IS_OUR_SET_PLAY_FIELD_NUMBER: _ClassVar[int]
    IS_THEIR_SET_PLAY_FIELD_NUMBER: _ClassVar[int]
    STOPED_CYCLE_FIELD_NUMBER: _ClassVar[int]
    OUR_TEAM_SCORE_FIELD_NUMBER: _ClassVar[int]
    THEIR_TEAM_SCORE_FIELD_NUMBER: _ClassVar[int]
    intercept_table: InterceptTable
    our_team_name: str
    their_team_name: str
    our_side: Side
    last_set_play_start_time: int
    self: Self
    ball: Ball
    teammates: _containers.RepeatedCompositeFieldContainer[Player]
    opponents: _containers.RepeatedCompositeFieldContainer[Player]
    unknowns: _containers.RepeatedCompositeFieldContainer[Player]
    our_players_dict: _containers.MessageMap[int, Player]
    their_players_dict: _containers.MessageMap[int, Player]
    our_goalie_uniform_number: int
    their_goalie_uniform_number: int
    offside_line_x: float
    ofside_line_x_count: int
    kickable_teammate_id: int
    kickable_opponent_id: int
    last_kick_side: Side
    last_kicker_uniform_number: int
    cycle: int
    game_mode_type: GameModeType
    left_team_score: int
    right_team_score: int
    is_our_set_play: bool
    is_their_set_play: bool
    stoped_cycle: int
    our_team_score: int
    their_team_score: int
    def __init__(self, intercept_table: _Optional[_Union[InterceptTable, _Mapping]] = ..., our_team_name: _Optional[str] = ..., their_team_name: _Optional[str] = ..., our_side: _Optional[_Union[Side, str]] = ..., last_set_play_start_time: _Optional[int] = ..., self: _Optional[_Union[Self, _Mapping]] = ..., ball: _Optional[_Union[Ball, _Mapping]] = ..., teammates: _Optional[_Iterable[_Union[Player, _Mapping]]] = ..., opponents: _Optional[_Iterable[_Union[Player, _Mapping]]] = ..., unknowns: _Optional[_Iterable[_Union[Player, _Mapping]]] = ..., our_players_dict: _Optional[_Mapping[int, Player]] = ..., their_players_dict: _Optional[_Mapping[int, Player]] = ..., our_goalie_uniform_number: _Optional[int] = ..., their_goalie_uniform_number: _Optional[int] = ..., offside_line_x: _Optional[float] = ..., ofside_line_x_count: _Optional[int] = ..., kickable_teammate_id: _Optional[int] = ..., kickable_opponent_id: _Optional[int] = ..., last_kick_side: _Optional[_Union[Side, str]] = ..., last_kicker_uniform_number: _Optional[int] = ..., cycle: _Optional[int] = ..., game_mode_type: _Optional[_Union[GameModeType, str]] = ..., left_team_score: _Optional[int] = ..., right_team_score: _Optional[int] = ..., is_our_set_play: bool = ..., is_their_set_play: bool = ..., stoped_cycle: _Optional[int] = ..., our_team_score: _Optional[int] = ..., their_team_score: _Optional[int] = ...) -> None: ...

class State(_message.Message):
    __slots__ = ("world_model", "full_world_model")
    WORLD_MODEL_FIELD_NUMBER: _ClassVar[int]
    FULL_WORLD_MODEL_FIELD_NUMBER: _ClassVar[int]
    world_model: WorldModel
    full_world_model: WorldModel
    def __init__(self, world_model: _Optional[_Union[WorldModel, _Mapping]] = ..., full_world_model: _Optional[_Union[WorldModel, _Mapping]] = ...) -> None: ...

class InitMessage(_message.Message):
    __slots__ = ("debug_mode",)
    DEBUG_MODE_FIELD_NUMBER: _ClassVar[int]
    debug_mode: bool
    def __init__(self, debug_mode: bool = ...) -> None: ...

class Dash(_message.Message):
    __slots__ = ("power", "relative_direction")
    POWER_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    power: float
    relative_direction: float
    def __init__(self, power: _Optional[float] = ..., relative_direction: _Optional[float] = ...) -> None: ...

class Turn(_message.Message):
    __slots__ = ("relative_direction",)
    RELATIVE_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    relative_direction: float
    def __init__(self, relative_direction: _Optional[float] = ...) -> None: ...

class Kick(_message.Message):
    __slots__ = ("power", "relative_direction")
    POWER_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    power: float
    relative_direction: float
    def __init__(self, power: _Optional[float] = ..., relative_direction: _Optional[float] = ...) -> None: ...

class Tackle(_message.Message):
    __slots__ = ("power_or_dir", "foul")
    POWER_OR_DIR_FIELD_NUMBER: _ClassVar[int]
    FOUL_FIELD_NUMBER: _ClassVar[int]
    power_or_dir: float
    foul: bool
    def __init__(self, power_or_dir: _Optional[float] = ..., foul: bool = ...) -> None: ...

class Catch(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Move(_message.Message):
    __slots__ = ("x", "y")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ...) -> None: ...

class TurnNeck(_message.Message):
    __slots__ = ("moment",)
    MOMENT_FIELD_NUMBER: _ClassVar[int]
    moment: float
    def __init__(self, moment: _Optional[float] = ...) -> None: ...

class ChangeView(_message.Message):
    __slots__ = ("view_width",)
    VIEW_WIDTH_FIELD_NUMBER: _ClassVar[int]
    view_width: ViewWidth
    def __init__(self, view_width: _Optional[_Union[ViewWidth, str]] = ...) -> None: ...

class BallMessage(_message.Message):
    __slots__ = ("ball_position", "ball_velocity")
    BALL_POSITION_FIELD_NUMBER: _ClassVar[int]
    BALL_VELOCITY_FIELD_NUMBER: _ClassVar[int]
    ball_position: Vector2D
    ball_velocity: Vector2D
    def __init__(self, ball_position: _Optional[_Union[Vector2D, _Mapping]] = ..., ball_velocity: _Optional[_Union[Vector2D, _Mapping]] = ...) -> None: ...

class PassMessage(_message.Message):
    __slots__ = ("receiver_uniform_number", "receiver_point", "ball_position", "ball_velocity")
    RECEIVER_UNIFORM_NUMBER_FIELD_NUMBER: _ClassVar[int]
    RECEIVER_POINT_FIELD_NUMBER: _ClassVar[int]
    BALL_POSITION_FIELD_NUMBER: _ClassVar[int]
    BALL_VELOCITY_FIELD_NUMBER: _ClassVar[int]
    receiver_uniform_number: int
    receiver_point: Vector2D
    ball_position: Vector2D
    ball_velocity: Vector2D
    def __init__(self, receiver_uniform_number: _Optional[int] = ..., receiver_point: _Optional[_Union[Vector2D, _Mapping]] = ..., ball_position: _Optional[_Union[Vector2D, _Mapping]] = ..., ball_velocity: _Optional[_Union[Vector2D, _Mapping]] = ...) -> None: ...

class InterceptMessage(_message.Message):
    __slots__ = ("our", "uniform_number", "cycle")
    OUR_FIELD_NUMBER: _ClassVar[int]
    UNIFORM_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CYCLE_FIELD_NUMBER: _ClassVar[int]
    our: bool
    uniform_number: int
    cycle: int
    def __init__(self, our: bool = ..., uniform_number: _Optional[int] = ..., cycle: _Optional[int] = ...) -> None: ...

class GoalieMessage(_message.Message):
    __slots__ = ("goalie_uniform_number", "goalie_position", "goalie_body_direction")
    GOALIE_UNIFORM_NUMBER_FIELD_NUMBER: _ClassVar[int]
    GOALIE_POSITION_FIELD_NUMBER: _ClassVar[int]
    GOALIE_BODY_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    goalie_uniform_number: int
    goalie_position: Vector2D
    goalie_body_direction: float
    def __init__(self, goalie_uniform_number: _Optional[int] = ..., goalie_position: _Optional[_Union[Vector2D, _Mapping]] = ..., goalie_body_direction: _Optional[float] = ...) -> None: ...

class GoalieAndPlayerMessage(_message.Message):
    __slots__ = ("goalie_uniform_number", "goalie_position", "goalie_body_direction", "player_uniform_number", "player_position")
    GOALIE_UNIFORM_NUMBER_FIELD_NUMBER: _ClassVar[int]
    GOALIE_POSITION_FIELD_NUMBER: _ClassVar[int]
    GOALIE_BODY_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    PLAYER_UNIFORM_NUMBER_FIELD_NUMBER: _ClassVar[int]
    PLAYER_POSITION_FIELD_NUMBER: _ClassVar[int]
    goalie_uniform_number: int
    goalie_position: Vector2D
    goalie_body_direction: float
    player_uniform_number: int
    player_position: Vector2D
    def __init__(self, goalie_uniform_number: _Optional[int] = ..., goalie_position: _Optional[_Union[Vector2D, _Mapping]] = ..., goalie_body_direction: _Optional[float] = ..., player_uniform_number: _Optional[int] = ..., player_position: _Optional[_Union[Vector2D, _Mapping]] = ...) -> None: ...

class OffsideLineMessage(_message.Message):
    __slots__ = ("offside_line_x",)
    OFFSIDE_LINE_X_FIELD_NUMBER: _ClassVar[int]
    offside_line_x: float
    def __init__(self, offside_line_x: _Optional[float] = ...) -> None: ...

class DefenseLineMessage(_message.Message):
    __slots__ = ("defense_line_x",)
    DEFENSE_LINE_X_FIELD_NUMBER: _ClassVar[int]
    defense_line_x: float
    def __init__(self, defense_line_x: _Optional[float] = ...) -> None: ...

class WaitRequestMessage(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetplayMessage(_message.Message):
    __slots__ = ("wait_step",)
    WAIT_STEP_FIELD_NUMBER: _ClassVar[int]
    wait_step: int
    def __init__(self, wait_step: _Optional[int] = ...) -> None: ...

class PassRequestMessage(_message.Message):
    __slots__ = ("target_point",)
    TARGET_POINT_FIELD_NUMBER: _ClassVar[int]
    target_point: Vector2D
    def __init__(self, target_point: _Optional[_Union[Vector2D, _Mapping]] = ...) -> None: ...

class StaminaMessage(_message.Message):
    __slots__ = ("stamina",)
    STAMINA_FIELD_NUMBER: _ClassVar[int]
    stamina: float
    def __init__(self, stamina: _Optional[float] = ...) -> None: ...

class RecoveryMessage(_message.Message):
    __slots__ = ("recovery",)
    RECOVERY_FIELD_NUMBER: _ClassVar[int]
    recovery: float
    def __init__(self, recovery: _Optional[float] = ...) -> None: ...

class StaminaCapacityMessage(_message.Message):
    __slots__ = ("stamina_capacity",)
    STAMINA_CAPACITY_FIELD_NUMBER: _ClassVar[int]
    stamina_capacity: float
    def __init__(self, stamina_capacity: _Optional[float] = ...) -> None: ...

class DribbleMessage(_message.Message):
    __slots__ = ("target_point", "queue_count")
    TARGET_POINT_FIELD_NUMBER: _ClassVar[int]
    QUEUE_COUNT_FIELD_NUMBER: _ClassVar[int]
    target_point: Vector2D
    queue_count: int
    def __init__(self, target_point: _Optional[_Union[Vector2D, _Mapping]] = ..., queue_count: _Optional[int] = ...) -> None: ...

class BallGoalieMessage(_message.Message):
    __slots__ = ("ball_position", "ball_velocity", "goalie_position", "goalie_body_direction")
    BALL_POSITION_FIELD_NUMBER: _ClassVar[int]
    BALL_VELOCITY_FIELD_NUMBER: _ClassVar[int]
    GOALIE_POSITION_FIELD_NUMBER: _ClassVar[int]
    GOALIE_BODY_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    ball_position: Vector2D
    ball_velocity: Vector2D
    goalie_position: Vector2D
    goalie_body_direction: float
    def __init__(self, ball_position: _Optional[_Union[Vector2D, _Mapping]] = ..., ball_velocity: _Optional[_Union[Vector2D, _Mapping]] = ..., goalie_position: _Optional[_Union[Vector2D, _Mapping]] = ..., goalie_body_direction: _Optional[float] = ...) -> None: ...

class OnePlayerMessage(_message.Message):
    __slots__ = ("uniform_number", "position")
    UNIFORM_NUMBER_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    uniform_number: int
    position: Vector2D
    def __init__(self, uniform_number: _Optional[int] = ..., position: _Optional[_Union[Vector2D, _Mapping]] = ...) -> None: ...

class TwoPlayerMessage(_message.Message):
    __slots__ = ("first_uniform_number", "first_position", "second_uniform_number", "second_position")
    FIRST_UNIFORM_NUMBER_FIELD_NUMBER: _ClassVar[int]
    FIRST_POSITION_FIELD_NUMBER: _ClassVar[int]
    SECOND_UNIFORM_NUMBER_FIELD_NUMBER: _ClassVar[int]
    SECOND_POSITION_FIELD_NUMBER: _ClassVar[int]
    first_uniform_number: int
    first_position: Vector2D
    second_uniform_number: int
    second_position: Vector2D
    def __init__(self, first_uniform_number: _Optional[int] = ..., first_position: _Optional[_Union[Vector2D, _Mapping]] = ..., second_uniform_number: _Optional[int] = ..., second_position: _Optional[_Union[Vector2D, _Mapping]] = ...) -> None: ...

class ThreePlayerMessage(_message.Message):
    __slots__ = ("first_uniform_number", "first_position", "second_uniform_number", "second_position", "third_uniform_number", "third_position")
    FIRST_UNIFORM_NUMBER_FIELD_NUMBER: _ClassVar[int]
    FIRST_POSITION_FIELD_NUMBER: _ClassVar[int]
    SECOND_UNIFORM_NUMBER_FIELD_NUMBER: _ClassVar[int]
    SECOND_POSITION_FIELD_NUMBER: _ClassVar[int]
    THIRD_UNIFORM_NUMBER_FIELD_NUMBER: _ClassVar[int]
    THIRD_POSITION_FIELD_NUMBER: _ClassVar[int]
    first_uniform_number: int
    first_position: Vector2D
    second_uniform_number: int
    second_position: Vector2D
    third_uniform_number: int
    third_position: Vector2D
    def __init__(self, first_uniform_number: _Optional[int] = ..., first_position: _Optional[_Union[Vector2D, _Mapping]] = ..., second_uniform_number: _Optional[int] = ..., second_position: _Optional[_Union[Vector2D, _Mapping]] = ..., third_uniform_number: _Optional[int] = ..., third_position: _Optional[_Union[Vector2D, _Mapping]] = ...) -> None: ...

class SelfMessage(_message.Message):
    __slots__ = ("self_position", "self_body_direction", "self_stamina")
    SELF_POSITION_FIELD_NUMBER: _ClassVar[int]
    SELF_BODY_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    SELF_STAMINA_FIELD_NUMBER: _ClassVar[int]
    self_position: Vector2D
    self_body_direction: float
    self_stamina: float
    def __init__(self, self_position: _Optional[_Union[Vector2D, _Mapping]] = ..., self_body_direction: _Optional[float] = ..., self_stamina: _Optional[float] = ...) -> None: ...

class TeammateMessage(_message.Message):
    __slots__ = ("uniform_number", "position", "body_direction")
    UNIFORM_NUMBER_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    BODY_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    uniform_number: int
    position: Vector2D
    body_direction: float
    def __init__(self, uniform_number: _Optional[int] = ..., position: _Optional[_Union[Vector2D, _Mapping]] = ..., body_direction: _Optional[float] = ...) -> None: ...

class OpponentMessage(_message.Message):
    __slots__ = ("uniform_number", "position", "body_direction")
    UNIFORM_NUMBER_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    BODY_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    uniform_number: int
    position: Vector2D
    body_direction: float
    def __init__(self, uniform_number: _Optional[int] = ..., position: _Optional[_Union[Vector2D, _Mapping]] = ..., body_direction: _Optional[float] = ...) -> None: ...

class BallPlayerMessage(_message.Message):
    __slots__ = ("ball_position", "ball_velocity", "uniform_number", "player_position", "body_direction")
    BALL_POSITION_FIELD_NUMBER: _ClassVar[int]
    BALL_VELOCITY_FIELD_NUMBER: _ClassVar[int]
    UNIFORM_NUMBER_FIELD_NUMBER: _ClassVar[int]
    PLAYER_POSITION_FIELD_NUMBER: _ClassVar[int]
    BODY_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    ball_position: Vector2D
    ball_velocity: Vector2D
    uniform_number: int
    player_position: Vector2D
    body_direction: float
    def __init__(self, ball_position: _Optional[_Union[Vector2D, _Mapping]] = ..., ball_velocity: _Optional[_Union[Vector2D, _Mapping]] = ..., uniform_number: _Optional[int] = ..., player_position: _Optional[_Union[Vector2D, _Mapping]] = ..., body_direction: _Optional[float] = ...) -> None: ...

class Say(_message.Message):
    __slots__ = ("ball_message", "pass_message", "intercept_message", "goalie_message", "goalie_and_player_message", "offside_line_message", "defense_line_message", "wait_request_message", "setplay_message", "pass_request_message", "stamina_message", "recovery_message", "stamina_capacity_message", "dribble_message", "ball_goalie_message", "one_player_message", "two_player_message", "three_player_message", "self_message", "teammate_message", "opponent_message", "ball_player_message")
    BALL_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PASS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    INTERCEPT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    GOALIE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    GOALIE_AND_PLAYER_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    OFFSIDE_LINE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DEFENSE_LINE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    WAIT_REQUEST_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SETPLAY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PASS_REQUEST_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STAMINA_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RECOVERY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STAMINA_CAPACITY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DRIBBLE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    BALL_GOALIE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ONE_PLAYER_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TWO_PLAYER_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    THREE_PLAYER_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SELF_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TEAMMATE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    OPPONENT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    BALL_PLAYER_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ball_message: BallMessage
    pass_message: PassMessage
    intercept_message: InterceptMessage
    goalie_message: GoalieMessage
    goalie_and_player_message: GoalieAndPlayerMessage
    offside_line_message: OffsideLineMessage
    defense_line_message: DefenseLineMessage
    wait_request_message: WaitRequestMessage
    setplay_message: SetplayMessage
    pass_request_message: PassRequestMessage
    stamina_message: StaminaMessage
    recovery_message: RecoveryMessage
    stamina_capacity_message: StaminaCapacityMessage
    dribble_message: DribbleMessage
    ball_goalie_message: BallGoalieMessage
    one_player_message: OnePlayerMessage
    two_player_message: TwoPlayerMessage
    three_player_message: ThreePlayerMessage
    self_message: SelfMessage
    teammate_message: TeammateMessage
    opponent_message: OpponentMessage
    ball_player_message: BallPlayerMessage
    def __init__(self, ball_message: _Optional[_Union[BallMessage, _Mapping]] = ..., pass_message: _Optional[_Union[PassMessage, _Mapping]] = ..., intercept_message: _Optional[_Union[InterceptMessage, _Mapping]] = ..., goalie_message: _Optional[_Union[GoalieMessage, _Mapping]] = ..., goalie_and_player_message: _Optional[_Union[GoalieAndPlayerMessage, _Mapping]] = ..., offside_line_message: _Optional[_Union[OffsideLineMessage, _Mapping]] = ..., defense_line_message: _Optional[_Union[DefenseLineMessage, _Mapping]] = ..., wait_request_message: _Optional[_Union[WaitRequestMessage, _Mapping]] = ..., setplay_message: _Optional[_Union[SetplayMessage, _Mapping]] = ..., pass_request_message: _Optional[_Union[PassRequestMessage, _Mapping]] = ..., stamina_message: _Optional[_Union[StaminaMessage, _Mapping]] = ..., recovery_message: _Optional[_Union[RecoveryMessage, _Mapping]] = ..., stamina_capacity_message: _Optional[_Union[StaminaCapacityMessage, _Mapping]] = ..., dribble_message: _Optional[_Union[DribbleMessage, _Mapping]] = ..., ball_goalie_message: _Optional[_Union[BallGoalieMessage, _Mapping]] = ..., one_player_message: _Optional[_Union[OnePlayerMessage, _Mapping]] = ..., two_player_message: _Optional[_Union[TwoPlayerMessage, _Mapping]] = ..., three_player_message: _Optional[_Union[ThreePlayerMessage, _Mapping]] = ..., self_message: _Optional[_Union[SelfMessage, _Mapping]] = ..., teammate_message: _Optional[_Union[TeammateMessage, _Mapping]] = ..., opponent_message: _Optional[_Union[OpponentMessage, _Mapping]] = ..., ball_player_message: _Optional[_Union[BallPlayerMessage, _Mapping]] = ...) -> None: ...

class PointTo(_message.Message):
    __slots__ = ("x", "y")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ...) -> None: ...

class PointToOf(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AttentionTo(_message.Message):
    __slots__ = ("side", "unum")
    SIDE_FIELD_NUMBER: _ClassVar[int]
    UNUM_FIELD_NUMBER: _ClassVar[int]
    side: Side
    unum: int
    def __init__(self, side: _Optional[_Union[Side, str]] = ..., unum: _Optional[int] = ...) -> None: ...

class AttentionToOf(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AddText(_message.Message):
    __slots__ = ("level", "message")
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    level: LoggerLevel
    message: str
    def __init__(self, level: _Optional[_Union[LoggerLevel, str]] = ..., message: _Optional[str] = ...) -> None: ...

class AddPoint(_message.Message):
    __slots__ = ("level", "point", "color")
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    POINT_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    level: LoggerLevel
    point: Vector2D
    color: str
    def __init__(self, level: _Optional[_Union[LoggerLevel, str]] = ..., point: _Optional[_Union[Vector2D, _Mapping]] = ..., color: _Optional[str] = ...) -> None: ...

class AddLine(_message.Message):
    __slots__ = ("level", "start", "end", "color")
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    level: LoggerLevel
    start: Vector2D
    end: Vector2D
    color: str
    def __init__(self, level: _Optional[_Union[LoggerLevel, str]] = ..., start: _Optional[_Union[Vector2D, _Mapping]] = ..., end: _Optional[_Union[Vector2D, _Mapping]] = ..., color: _Optional[str] = ...) -> None: ...

class AddArc(_message.Message):
    __slots__ = ("level", "center", "radius", "start_angle", "span_angel", "color")
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    CENTER_FIELD_NUMBER: _ClassVar[int]
    RADIUS_FIELD_NUMBER: _ClassVar[int]
    START_ANGLE_FIELD_NUMBER: _ClassVar[int]
    SPAN_ANGEL_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    level: LoggerLevel
    center: Vector2D
    radius: float
    start_angle: float
    span_angel: float
    color: str
    def __init__(self, level: _Optional[_Union[LoggerLevel, str]] = ..., center: _Optional[_Union[Vector2D, _Mapping]] = ..., radius: _Optional[float] = ..., start_angle: _Optional[float] = ..., span_angel: _Optional[float] = ..., color: _Optional[str] = ...) -> None: ...

class AddCircle(_message.Message):
    __slots__ = ("level", "center", "radius", "color", "fill")
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    CENTER_FIELD_NUMBER: _ClassVar[int]
    RADIUS_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    FILL_FIELD_NUMBER: _ClassVar[int]
    level: LoggerLevel
    center: Vector2D
    radius: float
    color: str
    fill: bool
    def __init__(self, level: _Optional[_Union[LoggerLevel, str]] = ..., center: _Optional[_Union[Vector2D, _Mapping]] = ..., radius: _Optional[float] = ..., color: _Optional[str] = ..., fill: bool = ...) -> None: ...

class AddTriangle(_message.Message):
    __slots__ = ("level", "point1", "point2", "point3", "color", "fill")
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    POINT1_FIELD_NUMBER: _ClassVar[int]
    POINT2_FIELD_NUMBER: _ClassVar[int]
    POINT3_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    FILL_FIELD_NUMBER: _ClassVar[int]
    level: LoggerLevel
    point1: Vector2D
    point2: Vector2D
    point3: Vector2D
    color: str
    fill: bool
    def __init__(self, level: _Optional[_Union[LoggerLevel, str]] = ..., point1: _Optional[_Union[Vector2D, _Mapping]] = ..., point2: _Optional[_Union[Vector2D, _Mapping]] = ..., point3: _Optional[_Union[Vector2D, _Mapping]] = ..., color: _Optional[str] = ..., fill: bool = ...) -> None: ...

class AddRectangle(_message.Message):
    __slots__ = ("level", "left", "top", "length", "width", "color", "fill")
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    LEFT_FIELD_NUMBER: _ClassVar[int]
    TOP_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    FILL_FIELD_NUMBER: _ClassVar[int]
    level: LoggerLevel
    left: float
    top: float
    length: float
    width: float
    color: str
    fill: bool
    def __init__(self, level: _Optional[_Union[LoggerLevel, str]] = ..., left: _Optional[float] = ..., top: _Optional[float] = ..., length: _Optional[float] = ..., width: _Optional[float] = ..., color: _Optional[str] = ..., fill: bool = ...) -> None: ...

class AddSector(_message.Message):
    __slots__ = ("level", "center", "min_radius", "max_radius", "start_angle", "span_angel", "color", "fill")
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    CENTER_FIELD_NUMBER: _ClassVar[int]
    MIN_RADIUS_FIELD_NUMBER: _ClassVar[int]
    MAX_RADIUS_FIELD_NUMBER: _ClassVar[int]
    START_ANGLE_FIELD_NUMBER: _ClassVar[int]
    SPAN_ANGEL_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    FILL_FIELD_NUMBER: _ClassVar[int]
    level: LoggerLevel
    center: Vector2D
    min_radius: float
    max_radius: float
    start_angle: float
    span_angel: float
    color: str
    fill: bool
    def __init__(self, level: _Optional[_Union[LoggerLevel, str]] = ..., center: _Optional[_Union[Vector2D, _Mapping]] = ..., min_radius: _Optional[float] = ..., max_radius: _Optional[float] = ..., start_angle: _Optional[float] = ..., span_angel: _Optional[float] = ..., color: _Optional[str] = ..., fill: bool = ...) -> None: ...

class AddMessage(_message.Message):
    __slots__ = ("level", "position", "message", "color")
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    level: LoggerLevel
    position: Vector2D
    message: str
    color: str
    def __init__(self, level: _Optional[_Union[LoggerLevel, str]] = ..., position: _Optional[_Union[Vector2D, _Mapping]] = ..., message: _Optional[str] = ..., color: _Optional[str] = ...) -> None: ...

class Log(_message.Message):
    __slots__ = ("add_text", "add_point", "add_line", "add_arc", "add_circle", "add_triangle", "add_rectangle", "add_sector", "add_message")
    ADD_TEXT_FIELD_NUMBER: _ClassVar[int]
    ADD_POINT_FIELD_NUMBER: _ClassVar[int]
    ADD_LINE_FIELD_NUMBER: _ClassVar[int]
    ADD_ARC_FIELD_NUMBER: _ClassVar[int]
    ADD_CIRCLE_FIELD_NUMBER: _ClassVar[int]
    ADD_TRIANGLE_FIELD_NUMBER: _ClassVar[int]
    ADD_RECTANGLE_FIELD_NUMBER: _ClassVar[int]
    ADD_SECTOR_FIELD_NUMBER: _ClassVar[int]
    ADD_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    add_text: AddText
    add_point: AddPoint
    add_line: AddLine
    add_arc: AddArc
    add_circle: AddCircle
    add_triangle: AddTriangle
    add_rectangle: AddRectangle
    add_sector: AddSector
    add_message: AddMessage
    def __init__(self, add_text: _Optional[_Union[AddText, _Mapping]] = ..., add_point: _Optional[_Union[AddPoint, _Mapping]] = ..., add_line: _Optional[_Union[AddLine, _Mapping]] = ..., add_arc: _Optional[_Union[AddArc, _Mapping]] = ..., add_circle: _Optional[_Union[AddCircle, _Mapping]] = ..., add_triangle: _Optional[_Union[AddTriangle, _Mapping]] = ..., add_rectangle: _Optional[_Union[AddRectangle, _Mapping]] = ..., add_sector: _Optional[_Union[AddSector, _Mapping]] = ..., add_message: _Optional[_Union[AddMessage, _Mapping]] = ...) -> None: ...

class DebugClient(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class Body_GoToPoint(_message.Message):
    __slots__ = ("target_point", "distance_threshold", "max_dash_power")
    TARGET_POINT_FIELD_NUMBER: _ClassVar[int]
    DISTANCE_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    MAX_DASH_POWER_FIELD_NUMBER: _ClassVar[int]
    target_point: Vector2D
    distance_threshold: float
    max_dash_power: float
    def __init__(self, target_point: _Optional[_Union[Vector2D, _Mapping]] = ..., distance_threshold: _Optional[float] = ..., max_dash_power: _Optional[float] = ...) -> None: ...

class Body_SmartKick(_message.Message):
    __slots__ = ("target_point", "first_speed", "first_speed_threshold", "max_steps")
    TARGET_POINT_FIELD_NUMBER: _ClassVar[int]
    FIRST_SPEED_FIELD_NUMBER: _ClassVar[int]
    FIRST_SPEED_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    MAX_STEPS_FIELD_NUMBER: _ClassVar[int]
    target_point: Vector2D
    first_speed: float
    first_speed_threshold: float
    max_steps: int
    def __init__(self, target_point: _Optional[_Union[Vector2D, _Mapping]] = ..., first_speed: _Optional[float] = ..., first_speed_threshold: _Optional[float] = ..., max_steps: _Optional[int] = ...) -> None: ...

class Bhv_BeforeKickOff(_message.Message):
    __slots__ = ("point",)
    POINT_FIELD_NUMBER: _ClassVar[int]
    point: Vector2D
    def __init__(self, point: _Optional[_Union[Vector2D, _Mapping]] = ...) -> None: ...

class Bhv_BodyNeckToBall(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Bhv_BodyNeckToPoint(_message.Message):
    __slots__ = ("point",)
    POINT_FIELD_NUMBER: _ClassVar[int]
    point: Vector2D
    def __init__(self, point: _Optional[_Union[Vector2D, _Mapping]] = ...) -> None: ...

class Bhv_Emergency(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Bhv_GoToPointLookBall(_message.Message):
    __slots__ = ("target_point", "distance_threshold", "max_dash_power")
    TARGET_POINT_FIELD_NUMBER: _ClassVar[int]
    DISTANCE_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    MAX_DASH_POWER_FIELD_NUMBER: _ClassVar[int]
    target_point: Vector2D
    distance_threshold: float
    max_dash_power: float
    def __init__(self, target_point: _Optional[_Union[Vector2D, _Mapping]] = ..., distance_threshold: _Optional[float] = ..., max_dash_power: _Optional[float] = ...) -> None: ...

class Bhv_NeckBodyToBall(_message.Message):
    __slots__ = ("angle_buf",)
    ANGLE_BUF_FIELD_NUMBER: _ClassVar[int]
    angle_buf: float
    def __init__(self, angle_buf: _Optional[float] = ...) -> None: ...

class Bhv_NeckBodyToPoint(_message.Message):
    __slots__ = ("point", "angle_buf")
    POINT_FIELD_NUMBER: _ClassVar[int]
    ANGLE_BUF_FIELD_NUMBER: _ClassVar[int]
    point: Vector2D
    angle_buf: float
    def __init__(self, point: _Optional[_Union[Vector2D, _Mapping]] = ..., angle_buf: _Optional[float] = ...) -> None: ...

class Bhv_ScanField(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Body_AdvanceBall(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Body_ClearBall(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Body_Dribble(_message.Message):
    __slots__ = ("target_point", "distance_threshold", "dash_power", "dash_count", "dodge")
    TARGET_POINT_FIELD_NUMBER: _ClassVar[int]
    DISTANCE_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    DASH_POWER_FIELD_NUMBER: _ClassVar[int]
    DASH_COUNT_FIELD_NUMBER: _ClassVar[int]
    DODGE_FIELD_NUMBER: _ClassVar[int]
    target_point: Vector2D
    distance_threshold: float
    dash_power: float
    dash_count: int
    dodge: bool
    def __init__(self, target_point: _Optional[_Union[Vector2D, _Mapping]] = ..., distance_threshold: _Optional[float] = ..., dash_power: _Optional[float] = ..., dash_count: _Optional[int] = ..., dodge: bool = ...) -> None: ...

class Body_GoToPointDodge(_message.Message):
    __slots__ = ("target_point", "dash_power")
    TARGET_POINT_FIELD_NUMBER: _ClassVar[int]
    DASH_POWER_FIELD_NUMBER: _ClassVar[int]
    target_point: Vector2D
    dash_power: float
    def __init__(self, target_point: _Optional[_Union[Vector2D, _Mapping]] = ..., dash_power: _Optional[float] = ...) -> None: ...

class Body_HoldBall(_message.Message):
    __slots__ = ("do_turn", "turn_target_point", "kick_target_point")
    DO_TURN_FIELD_NUMBER: _ClassVar[int]
    TURN_TARGET_POINT_FIELD_NUMBER: _ClassVar[int]
    KICK_TARGET_POINT_FIELD_NUMBER: _ClassVar[int]
    do_turn: bool
    turn_target_point: Vector2D
    kick_target_point: Vector2D
    def __init__(self, do_turn: bool = ..., turn_target_point: _Optional[_Union[Vector2D, _Mapping]] = ..., kick_target_point: _Optional[_Union[Vector2D, _Mapping]] = ...) -> None: ...

class Body_Intercept(_message.Message):
    __slots__ = ("save_recovery", "face_point")
    SAVE_RECOVERY_FIELD_NUMBER: _ClassVar[int]
    FACE_POINT_FIELD_NUMBER: _ClassVar[int]
    save_recovery: bool
    face_point: Vector2D
    def __init__(self, save_recovery: bool = ..., face_point: _Optional[_Union[Vector2D, _Mapping]] = ...) -> None: ...

class Body_KickOneStep(_message.Message):
    __slots__ = ("target_point", "first_speed", "force_mode")
    TARGET_POINT_FIELD_NUMBER: _ClassVar[int]
    FIRST_SPEED_FIELD_NUMBER: _ClassVar[int]
    FORCE_MODE_FIELD_NUMBER: _ClassVar[int]
    target_point: Vector2D
    first_speed: float
    force_mode: bool
    def __init__(self, target_point: _Optional[_Union[Vector2D, _Mapping]] = ..., first_speed: _Optional[float] = ..., force_mode: bool = ...) -> None: ...

class Body_StopBall(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Body_StopDash(_message.Message):
    __slots__ = ("save_recovery",)
    SAVE_RECOVERY_FIELD_NUMBER: _ClassVar[int]
    save_recovery: bool
    def __init__(self, save_recovery: bool = ...) -> None: ...

class Body_TackleToPoint(_message.Message):
    __slots__ = ("target_point", "min_probability", "min_speed")
    TARGET_POINT_FIELD_NUMBER: _ClassVar[int]
    MIN_PROBABILITY_FIELD_NUMBER: _ClassVar[int]
    MIN_SPEED_FIELD_NUMBER: _ClassVar[int]
    target_point: Vector2D
    min_probability: float
    min_speed: float
    def __init__(self, target_point: _Optional[_Union[Vector2D, _Mapping]] = ..., min_probability: _Optional[float] = ..., min_speed: _Optional[float] = ...) -> None: ...

class Body_TurnToAngle(_message.Message):
    __slots__ = ("angle",)
    ANGLE_FIELD_NUMBER: _ClassVar[int]
    angle: float
    def __init__(self, angle: _Optional[float] = ...) -> None: ...

class Body_TurnToBall(_message.Message):
    __slots__ = ("cycle",)
    CYCLE_FIELD_NUMBER: _ClassVar[int]
    cycle: int
    def __init__(self, cycle: _Optional[int] = ...) -> None: ...

class Body_TurnToPoint(_message.Message):
    __slots__ = ("target_point", "cycle")
    TARGET_POINT_FIELD_NUMBER: _ClassVar[int]
    CYCLE_FIELD_NUMBER: _ClassVar[int]
    target_point: Vector2D
    cycle: int
    def __init__(self, target_point: _Optional[_Union[Vector2D, _Mapping]] = ..., cycle: _Optional[int] = ...) -> None: ...

class Focus_MoveToPoint(_message.Message):
    __slots__ = ("target_point",)
    TARGET_POINT_FIELD_NUMBER: _ClassVar[int]
    target_point: Vector2D
    def __init__(self, target_point: _Optional[_Union[Vector2D, _Mapping]] = ...) -> None: ...

class Focus_Reset(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Neck_ScanField(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Neck_ScanPlayers(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Neck_TurnToBallAndPlayer(_message.Message):
    __slots__ = ("side", "uniform_number", "count_threshold")
    SIDE_FIELD_NUMBER: _ClassVar[int]
    UNIFORM_NUMBER_FIELD_NUMBER: _ClassVar[int]
    COUNT_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    side: Side
    uniform_number: int
    count_threshold: int
    def __init__(self, side: _Optional[_Union[Side, str]] = ..., uniform_number: _Optional[int] = ..., count_threshold: _Optional[int] = ...) -> None: ...

class Neck_TurnToBallOrScan(_message.Message):
    __slots__ = ("count_threshold",)
    COUNT_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    count_threshold: int
    def __init__(self, count_threshold: _Optional[int] = ...) -> None: ...

class Neck_TurnToBall(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Neck_TurnToGoalieOrScan(_message.Message):
    __slots__ = ("count_threshold",)
    COUNT_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    count_threshold: int
    def __init__(self, count_threshold: _Optional[int] = ...) -> None: ...

class Neck_TurnToLowConfTeammate(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Neck_TurnToPlayerOrScan(_message.Message):
    __slots__ = ("side", "uniform_number", "count_threshold")
    SIDE_FIELD_NUMBER: _ClassVar[int]
    UNIFORM_NUMBER_FIELD_NUMBER: _ClassVar[int]
    COUNT_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    side: Side
    uniform_number: int
    count_threshold: int
    def __init__(self, side: _Optional[_Union[Side, str]] = ..., uniform_number: _Optional[int] = ..., count_threshold: _Optional[int] = ...) -> None: ...

class Neck_TurnToPoint(_message.Message):
    __slots__ = ("target_point",)
    TARGET_POINT_FIELD_NUMBER: _ClassVar[int]
    target_point: Vector2D
    def __init__(self, target_point: _Optional[_Union[Vector2D, _Mapping]] = ...) -> None: ...

class Neck_TurnToRelative(_message.Message):
    __slots__ = ("angle",)
    ANGLE_FIELD_NUMBER: _ClassVar[int]
    angle: float
    def __init__(self, angle: _Optional[float] = ...) -> None: ...

class View_ChangeWidth(_message.Message):
    __slots__ = ("view_width",)
    VIEW_WIDTH_FIELD_NUMBER: _ClassVar[int]
    view_width: ViewWidth
    def __init__(self, view_width: _Optional[_Union[ViewWidth, str]] = ...) -> None: ...

class View_Normal(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class View_Synch(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class View_Wide(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Action(_message.Message):
    __slots__ = ("dash", "turn", "kick", "tackle", "catch", "move", "turn_neck", "change_view", "say", "point_to", "point_to_of", "attention_to", "attention_to_of", "log", "debug_client", "body_go_to_point", "body_smart_kick", "bhv_before_kick_off", "bhv_body_neck_to_ball", "bhv_body_neck_to_point", "bhv_emergency", "bhv_go_to_point_look_ball", "bhv_neck_body_to_ball", "bhv_neck_body_to_point", "bhv_scan_field", "body_advance_ball", "body_clear_ball", "body_dribble", "body_go_to_point_dodge", "body_hold_ball", "body_intercept", "body_kick_one_step", "body_stop_ball", "body_stop_dash", "body_tackle_to_point", "body_turn_to_angle", "body_turn_to_ball", "body_turn_to_point", "focus_move_to_point", "focus_reset", "neck_scan_field", "neck_scan_players", "neck_turn_to_ball_and_player", "neck_turn_to_ball_or_scan", "neck_turn_to_ball", "neck_turn_to_goalie_or_scan", "neck_turn_to_low_conf_teammate", "neck_turn_to_player_or_scan", "neck_turn_to_point", "neck_turn_to_relative", "view_change_width", "view_normal", "view_synch", "view_wide")
    DASH_FIELD_NUMBER: _ClassVar[int]
    TURN_FIELD_NUMBER: _ClassVar[int]
    KICK_FIELD_NUMBER: _ClassVar[int]
    TACKLE_FIELD_NUMBER: _ClassVar[int]
    CATCH_FIELD_NUMBER: _ClassVar[int]
    MOVE_FIELD_NUMBER: _ClassVar[int]
    TURN_NECK_FIELD_NUMBER: _ClassVar[int]
    CHANGE_VIEW_FIELD_NUMBER: _ClassVar[int]
    SAY_FIELD_NUMBER: _ClassVar[int]
    POINT_TO_FIELD_NUMBER: _ClassVar[int]
    POINT_TO_OF_FIELD_NUMBER: _ClassVar[int]
    ATTENTION_TO_FIELD_NUMBER: _ClassVar[int]
    ATTENTION_TO_OF_FIELD_NUMBER: _ClassVar[int]
    LOG_FIELD_NUMBER: _ClassVar[int]
    DEBUG_CLIENT_FIELD_NUMBER: _ClassVar[int]
    BODY_GO_TO_POINT_FIELD_NUMBER: _ClassVar[int]
    BODY_SMART_KICK_FIELD_NUMBER: _ClassVar[int]
    BHV_BEFORE_KICK_OFF_FIELD_NUMBER: _ClassVar[int]
    BHV_BODY_NECK_TO_BALL_FIELD_NUMBER: _ClassVar[int]
    BHV_BODY_NECK_TO_POINT_FIELD_NUMBER: _ClassVar[int]
    BHV_EMERGENCY_FIELD_NUMBER: _ClassVar[int]
    BHV_GO_TO_POINT_LOOK_BALL_FIELD_NUMBER: _ClassVar[int]
    BHV_NECK_BODY_TO_BALL_FIELD_NUMBER: _ClassVar[int]
    BHV_NECK_BODY_TO_POINT_FIELD_NUMBER: _ClassVar[int]
    BHV_SCAN_FIELD_FIELD_NUMBER: _ClassVar[int]
    BODY_ADVANCE_BALL_FIELD_NUMBER: _ClassVar[int]
    BODY_CLEAR_BALL_FIELD_NUMBER: _ClassVar[int]
    BODY_DRIBBLE_FIELD_NUMBER: _ClassVar[int]
    BODY_GO_TO_POINT_DODGE_FIELD_NUMBER: _ClassVar[int]
    BODY_HOLD_BALL_FIELD_NUMBER: _ClassVar[int]
    BODY_INTERCEPT_FIELD_NUMBER: _ClassVar[int]
    BODY_KICK_ONE_STEP_FIELD_NUMBER: _ClassVar[int]
    BODY_STOP_BALL_FIELD_NUMBER: _ClassVar[int]
    BODY_STOP_DASH_FIELD_NUMBER: _ClassVar[int]
    BODY_TACKLE_TO_POINT_FIELD_NUMBER: _ClassVar[int]
    BODY_TURN_TO_ANGLE_FIELD_NUMBER: _ClassVar[int]
    BODY_TURN_TO_BALL_FIELD_NUMBER: _ClassVar[int]
    BODY_TURN_TO_POINT_FIELD_NUMBER: _ClassVar[int]
    FOCUS_MOVE_TO_POINT_FIELD_NUMBER: _ClassVar[int]
    FOCUS_RESET_FIELD_NUMBER: _ClassVar[int]
    NECK_SCAN_FIELD_FIELD_NUMBER: _ClassVar[int]
    NECK_SCAN_PLAYERS_FIELD_NUMBER: _ClassVar[int]
    NECK_TURN_TO_BALL_AND_PLAYER_FIELD_NUMBER: _ClassVar[int]
    NECK_TURN_TO_BALL_OR_SCAN_FIELD_NUMBER: _ClassVar[int]
    NECK_TURN_TO_BALL_FIELD_NUMBER: _ClassVar[int]
    NECK_TURN_TO_GOALIE_OR_SCAN_FIELD_NUMBER: _ClassVar[int]
    NECK_TURN_TO_LOW_CONF_TEAMMATE_FIELD_NUMBER: _ClassVar[int]
    NECK_TURN_TO_PLAYER_OR_SCAN_FIELD_NUMBER: _ClassVar[int]
    NECK_TURN_TO_POINT_FIELD_NUMBER: _ClassVar[int]
    NECK_TURN_TO_RELATIVE_FIELD_NUMBER: _ClassVar[int]
    VIEW_CHANGE_WIDTH_FIELD_NUMBER: _ClassVar[int]
    VIEW_NORMAL_FIELD_NUMBER: _ClassVar[int]
    VIEW_SYNCH_FIELD_NUMBER: _ClassVar[int]
    VIEW_WIDE_FIELD_NUMBER: _ClassVar[int]
    dash: Dash
    turn: Turn
    kick: Kick
    tackle: Tackle
    catch: Catch
    move: Move
    turn_neck: TurnNeck
    change_view: ChangeView
    say: Say
    point_to: PointTo
    point_to_of: PointToOf
    attention_to: AttentionTo
    attention_to_of: AttentionToOf
    log: Log
    debug_client: DebugClient
    body_go_to_point: Body_GoToPoint
    body_smart_kick: Body_SmartKick
    bhv_before_kick_off: Bhv_BeforeKickOff
    bhv_body_neck_to_ball: Bhv_BodyNeckToBall
    bhv_body_neck_to_point: Bhv_BodyNeckToPoint
    bhv_emergency: Bhv_Emergency
    bhv_go_to_point_look_ball: Bhv_GoToPointLookBall
    bhv_neck_body_to_ball: Bhv_NeckBodyToBall
    bhv_neck_body_to_point: Bhv_NeckBodyToPoint
    bhv_scan_field: Bhv_ScanField
    body_advance_ball: Body_AdvanceBall
    body_clear_ball: Body_ClearBall
    body_dribble: Body_Dribble
    body_go_to_point_dodge: Body_GoToPointDodge
    body_hold_ball: Body_HoldBall
    body_intercept: Body_Intercept
    body_kick_one_step: Body_KickOneStep
    body_stop_ball: Body_StopBall
    body_stop_dash: Body_StopDash
    body_tackle_to_point: Body_TackleToPoint
    body_turn_to_angle: Body_TurnToAngle
    body_turn_to_ball: Body_TurnToBall
    body_turn_to_point: Body_TurnToPoint
    focus_move_to_point: Focus_MoveToPoint
    focus_reset: Focus_Reset
    neck_scan_field: Neck_ScanField
    neck_scan_players: Neck_ScanPlayers
    neck_turn_to_ball_and_player: Neck_TurnToBallAndPlayer
    neck_turn_to_ball_or_scan: Neck_TurnToBallOrScan
    neck_turn_to_ball: Neck_TurnToBall
    neck_turn_to_goalie_or_scan: Neck_TurnToGoalieOrScan
    neck_turn_to_low_conf_teammate: Neck_TurnToLowConfTeammate
    neck_turn_to_player_or_scan: Neck_TurnToPlayerOrScan
    neck_turn_to_point: Neck_TurnToPoint
    neck_turn_to_relative: Neck_TurnToRelative
    view_change_width: View_ChangeWidth
    view_normal: View_Normal
    view_synch: View_Synch
    view_wide: View_Wide
    def __init__(self, dash: _Optional[_Union[Dash, _Mapping]] = ..., turn: _Optional[_Union[Turn, _Mapping]] = ..., kick: _Optional[_Union[Kick, _Mapping]] = ..., tackle: _Optional[_Union[Tackle, _Mapping]] = ..., catch: _Optional[_Union[Catch, _Mapping]] = ..., move: _Optional[_Union[Move, _Mapping]] = ..., turn_neck: _Optional[_Union[TurnNeck, _Mapping]] = ..., change_view: _Optional[_Union[ChangeView, _Mapping]] = ..., say: _Optional[_Union[Say, _Mapping]] = ..., point_to: _Optional[_Union[PointTo, _Mapping]] = ..., point_to_of: _Optional[_Union[PointToOf, _Mapping]] = ..., attention_to: _Optional[_Union[AttentionTo, _Mapping]] = ..., attention_to_of: _Optional[_Union[AttentionToOf, _Mapping]] = ..., log: _Optional[_Union[Log, _Mapping]] = ..., debug_client: _Optional[_Union[DebugClient, _Mapping]] = ..., body_go_to_point: _Optional[_Union[Body_GoToPoint, _Mapping]] = ..., body_smart_kick: _Optional[_Union[Body_SmartKick, _Mapping]] = ..., bhv_before_kick_off: _Optional[_Union[Bhv_BeforeKickOff, _Mapping]] = ..., bhv_body_neck_to_ball: _Optional[_Union[Bhv_BodyNeckToBall, _Mapping]] = ..., bhv_body_neck_to_point: _Optional[_Union[Bhv_BodyNeckToPoint, _Mapping]] = ..., bhv_emergency: _Optional[_Union[Bhv_Emergency, _Mapping]] = ..., bhv_go_to_point_look_ball: _Optional[_Union[Bhv_GoToPointLookBall, _Mapping]] = ..., bhv_neck_body_to_ball: _Optional[_Union[Bhv_NeckBodyToBall, _Mapping]] = ..., bhv_neck_body_to_point: _Optional[_Union[Bhv_NeckBodyToPoint, _Mapping]] = ..., bhv_scan_field: _Optional[_Union[Bhv_ScanField, _Mapping]] = ..., body_advance_ball: _Optional[_Union[Body_AdvanceBall, _Mapping]] = ..., body_clear_ball: _Optional[_Union[Body_ClearBall, _Mapping]] = ..., body_dribble: _Optional[_Union[Body_Dribble, _Mapping]] = ..., body_go_to_point_dodge: _Optional[_Union[Body_GoToPointDodge, _Mapping]] = ..., body_hold_ball: _Optional[_Union[Body_HoldBall, _Mapping]] = ..., body_intercept: _Optional[_Union[Body_Intercept, _Mapping]] = ..., body_kick_one_step: _Optional[_Union[Body_KickOneStep, _Mapping]] = ..., body_stop_ball: _Optional[_Union[Body_StopBall, _Mapping]] = ..., body_stop_dash: _Optional[_Union[Body_StopDash, _Mapping]] = ..., body_tackle_to_point: _Optional[_Union[Body_TackleToPoint, _Mapping]] = ..., body_turn_to_angle: _Optional[_Union[Body_TurnToAngle, _Mapping]] = ..., body_turn_to_ball: _Optional[_Union[Body_TurnToBall, _Mapping]] = ..., body_turn_to_point: _Optional[_Union[Body_TurnToPoint, _Mapping]] = ..., focus_move_to_point: _Optional[_Union[Focus_MoveToPoint, _Mapping]] = ..., focus_reset: _Optional[_Union[Focus_Reset, _Mapping]] = ..., neck_scan_field: _Optional[_Union[Neck_ScanField, _Mapping]] = ..., neck_scan_players: _Optional[_Union[Neck_ScanPlayers, _Mapping]] = ..., neck_turn_to_ball_and_player: _Optional[_Union[Neck_TurnToBallAndPlayer, _Mapping]] = ..., neck_turn_to_ball_or_scan: _Optional[_Union[Neck_TurnToBallOrScan, _Mapping]] = ..., neck_turn_to_ball: _Optional[_Union[Neck_TurnToBall, _Mapping]] = ..., neck_turn_to_goalie_or_scan: _Optional[_Union[Neck_TurnToGoalieOrScan, _Mapping]] = ..., neck_turn_to_low_conf_teammate: _Optional[_Union[Neck_TurnToLowConfTeammate, _Mapping]] = ..., neck_turn_to_player_or_scan: _Optional[_Union[Neck_TurnToPlayerOrScan, _Mapping]] = ..., neck_turn_to_point: _Optional[_Union[Neck_TurnToPoint, _Mapping]] = ..., neck_turn_to_relative: _Optional[_Union[Neck_TurnToRelative, _Mapping]] = ..., view_change_width: _Optional[_Union[View_ChangeWidth, _Mapping]] = ..., view_normal: _Optional[_Union[View_Normal, _Mapping]] = ..., view_synch: _Optional[_Union[View_Synch, _Mapping]] = ..., view_wide: _Optional[_Union[View_Wide, _Mapping]] = ...) -> None: ...

class Actions(_message.Message):
    __slots__ = ("actions",)
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    actions: _containers.RepeatedCompositeFieldContainer[Action]
    def __init__(self, actions: _Optional[_Iterable[_Union[Action, _Mapping]]] = ...) -> None: ...

class ServerParam(_message.Message):
    __slots__ = ("goal_width", "inertia_moment", "player_size", "player_decay", "player_rand", "player_weight", "player_speed_max", "player_accel_max", "stamina_max", "stamina_inc_max", "recover_init", "recover_dec_thr", "recover_min", "recover_dec", "effort_init", "effort_dec_thr", "effort_min", "effort_dec", "effort_inc_thr", "effort_inc", "kick_rand", "team_actuator_noise", "player_rand_factor_l", "player_rand_factor_r", "kick_rand_factor_l", "kick_rand_factor_r", "ball_size", "ball_decay", "ball_rand", "ball_weight", "ball_speed_max", "ball_accel_max", "dash_power_rate", "kick_power_rate", "kickable_margin", "control_radius", "control_radius_width", "max_power", "min_power", "max_moment", "min_moment", "max_neck_moment", "min_neck_moment", "max_neck_angle", "min_neck_angle", "visible_angle", "visible_distance", "wind_dir", "wind_force", "wind_angle", "wind_rand", "kickable_area", "catch_area_l", "catch_area_w", "catch_probability", "goalie_max_moves", "corner_kick_margin", "offside_active_area_size", "wind_none", "use_wind_random", "coach_say_count_max", "coach_say_msg_size", "clang_win_size", "clang_define_win", "clang_meta_win", "clang_advice_win", "clang_info_win", "clang_mess_delay", "clang_mess_per_cycle", "half_time", "simulator_step", "send_step", "recv_step", "sense_body_step", "lcm_step", "player_say_msg_size", "player_hear_max", "player_hear_inc", "player_hear_decay", "catch_ban_cycle", "slow_down_factor", "use_offside", "kickoff_offside", "offside_kick_margin", "audio_cut_dist", "dist_quantize_step", "landmark_dist_quantize_step", "dir_quantize_step", "dist_quantize_step_l", "dist_quantize_step_r", "landmark_dist_quantize_step_l", "landmark_dist_quantize_step_r", "dir_quantize_step_l", "dir_quantize_step_r", "coach_mode", "coach_with_referee_mode", "use_old_coach_hear", "slowness_on_top_for_left_team", "slowness_on_top_for_right_team", "start_goal_l", "start_goal_r", "fullstate_l", "fullstate_r", "drop_ball_time", "synch_mode", "synch_offset", "synch_micro_sleep", "point_to_ban", "point_to_duration", "player_port", "trainer_port", "online_coach_port", "verbose_mode", "coach_send_vi_step", "replay_file", "landmark_file", "send_comms", "text_logging", "game_logging", "game_log_version", "text_log_dir", "game_log_dir", "text_log_fixed_name", "game_log_fixed_name", "use_text_log_fixed", "use_game_log_fixed", "use_text_log_dated", "use_game_log_dated", "log_date_format", "log_times", "record_message", "text_log_compression", "game_log_compression", "use_profile", "tackle_dist", "tackle_back_dist", "tackle_width", "tackle_exponent", "tackle_cycles", "tackle_power_rate", "freeform_wait_period", "freeform_send_period", "free_kick_faults", "back_passes", "proper_goal_kicks", "stopped_ball_vel", "max_goal_kicks", "clang_del_win", "clang_rule_win", "auto_mode", "kick_off_wait", "connect_wait", "game_over_wait", "team_l_start", "team_r_start", "keepaway_mode", "keepaway_length", "keepaway_width", "keepaway_logging", "keepaway_log_dir", "keepaway_log_fixed_name", "keepaway_log_fixed", "keepaway_log_dated", "keepaway_start", "nr_normal_halfs", "nr_extra_halfs", "penalty_shoot_outs", "pen_before_setup_wait", "pen_setup_wait", "pen_ready_wait", "pen_taken_wait", "pen_nr_kicks", "pen_max_extra_kicks", "pen_dist_x", "pen_random_winner", "pen_allow_mult_kicks", "pen_max_goalie_dist_x", "pen_coach_moves_players", "module_dir", "ball_stuck_area", "coach_msg_file", "max_tackle_power", "max_back_tackle_power", "player_speed_max_min", "extra_stamina", "synch_see_offset", "extra_half_time", "stamina_capacity", "max_dash_angle", "min_dash_angle", "dash_angle_step", "side_dash_rate", "back_dash_rate", "max_dash_power", "min_dash_power", "tackle_rand_factor", "foul_detect_probability", "foul_exponent", "foul_cycles", "golden_goal", "red_card_probability", "illegal_defense_duration", "illegal_defense_number", "illegal_defense_dist_x", "illegal_defense_width", "fixed_teamname_l", "fixed_teamname_r", "max_catch_angle", "min_catch_angle", "random_seed", "long_kick_power_factor", "long_kick_delay", "max_monitors", "catchable_area", "real_speed_max", "pitch_half_length", "pitch_half_width", "our_penalty_area_line_x", "their_penalty_area_line_x", "penalty_area_half_width", "penalty_area_length")
    GOAL_WIDTH_FIELD_NUMBER: _ClassVar[int]
    INERTIA_MOMENT_FIELD_NUMBER: _ClassVar[int]
    PLAYER_SIZE_FIELD_NUMBER: _ClassVar[int]
    PLAYER_DECAY_FIELD_NUMBER: _ClassVar[int]
    PLAYER_RAND_FIELD_NUMBER: _ClassVar[int]
    PLAYER_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    PLAYER_SPEED_MAX_FIELD_NUMBER: _ClassVar[int]
    PLAYER_ACCEL_MAX_FIELD_NUMBER: _ClassVar[int]
    STAMINA_MAX_FIELD_NUMBER: _ClassVar[int]
    STAMINA_INC_MAX_FIELD_NUMBER: _ClassVar[int]
    RECOVER_INIT_FIELD_NUMBER: _ClassVar[int]
    RECOVER_DEC_THR_FIELD_NUMBER: _ClassVar[int]
    RECOVER_MIN_FIELD_NUMBER: _ClassVar[int]
    RECOVER_DEC_FIELD_NUMBER: _ClassVar[int]
    EFFORT_INIT_FIELD_NUMBER: _ClassVar[int]
    EFFORT_DEC_THR_FIELD_NUMBER: _ClassVar[int]
    EFFORT_MIN_FIELD_NUMBER: _ClassVar[int]
    EFFORT_DEC_FIELD_NUMBER: _ClassVar[int]
    EFFORT_INC_THR_FIELD_NUMBER: _ClassVar[int]
    EFFORT_INC_FIELD_NUMBER: _ClassVar[int]
    KICK_RAND_FIELD_NUMBER: _ClassVar[int]
    TEAM_ACTUATOR_NOISE_FIELD_NUMBER: _ClassVar[int]
    PLAYER_RAND_FACTOR_L_FIELD_NUMBER: _ClassVar[int]
    PLAYER_RAND_FACTOR_R_FIELD_NUMBER: _ClassVar[int]
    KICK_RAND_FACTOR_L_FIELD_NUMBER: _ClassVar[int]
    KICK_RAND_FACTOR_R_FIELD_NUMBER: _ClassVar[int]
    BALL_SIZE_FIELD_NUMBER: _ClassVar[int]
    BALL_DECAY_FIELD_NUMBER: _ClassVar[int]
    BALL_RAND_FIELD_NUMBER: _ClassVar[int]
    BALL_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    BALL_SPEED_MAX_FIELD_NUMBER: _ClassVar[int]
    BALL_ACCEL_MAX_FIELD_NUMBER: _ClassVar[int]
    DASH_POWER_RATE_FIELD_NUMBER: _ClassVar[int]
    KICK_POWER_RATE_FIELD_NUMBER: _ClassVar[int]
    KICKABLE_MARGIN_FIELD_NUMBER: _ClassVar[int]
    CONTROL_RADIUS_FIELD_NUMBER: _ClassVar[int]
    CONTROL_RADIUS_WIDTH_FIELD_NUMBER: _ClassVar[int]
    MAX_POWER_FIELD_NUMBER: _ClassVar[int]
    MIN_POWER_FIELD_NUMBER: _ClassVar[int]
    MAX_MOMENT_FIELD_NUMBER: _ClassVar[int]
    MIN_MOMENT_FIELD_NUMBER: _ClassVar[int]
    MAX_NECK_MOMENT_FIELD_NUMBER: _ClassVar[int]
    MIN_NECK_MOMENT_FIELD_NUMBER: _ClassVar[int]
    MAX_NECK_ANGLE_FIELD_NUMBER: _ClassVar[int]
    MIN_NECK_ANGLE_FIELD_NUMBER: _ClassVar[int]
    VISIBLE_ANGLE_FIELD_NUMBER: _ClassVar[int]
    VISIBLE_DISTANCE_FIELD_NUMBER: _ClassVar[int]
    WIND_DIR_FIELD_NUMBER: _ClassVar[int]
    WIND_FORCE_FIELD_NUMBER: _ClassVar[int]
    WIND_ANGLE_FIELD_NUMBER: _ClassVar[int]
    WIND_RAND_FIELD_NUMBER: _ClassVar[int]
    KICKABLE_AREA_FIELD_NUMBER: _ClassVar[int]
    CATCH_AREA_L_FIELD_NUMBER: _ClassVar[int]
    CATCH_AREA_W_FIELD_NUMBER: _ClassVar[int]
    CATCH_PROBABILITY_FIELD_NUMBER: _ClassVar[int]
    GOALIE_MAX_MOVES_FIELD_NUMBER: _ClassVar[int]
    CORNER_KICK_MARGIN_FIELD_NUMBER: _ClassVar[int]
    OFFSIDE_ACTIVE_AREA_SIZE_FIELD_NUMBER: _ClassVar[int]
    WIND_NONE_FIELD_NUMBER: _ClassVar[int]
    USE_WIND_RANDOM_FIELD_NUMBER: _ClassVar[int]
    COACH_SAY_COUNT_MAX_FIELD_NUMBER: _ClassVar[int]
    COACH_SAY_MSG_SIZE_FIELD_NUMBER: _ClassVar[int]
    CLANG_WIN_SIZE_FIELD_NUMBER: _ClassVar[int]
    CLANG_DEFINE_WIN_FIELD_NUMBER: _ClassVar[int]
    CLANG_META_WIN_FIELD_NUMBER: _ClassVar[int]
    CLANG_ADVICE_WIN_FIELD_NUMBER: _ClassVar[int]
    CLANG_INFO_WIN_FIELD_NUMBER: _ClassVar[int]
    CLANG_MESS_DELAY_FIELD_NUMBER: _ClassVar[int]
    CLANG_MESS_PER_CYCLE_FIELD_NUMBER: _ClassVar[int]
    HALF_TIME_FIELD_NUMBER: _ClassVar[int]
    SIMULATOR_STEP_FIELD_NUMBER: _ClassVar[int]
    SEND_STEP_FIELD_NUMBER: _ClassVar[int]
    RECV_STEP_FIELD_NUMBER: _ClassVar[int]
    SENSE_BODY_STEP_FIELD_NUMBER: _ClassVar[int]
    LCM_STEP_FIELD_NUMBER: _ClassVar[int]
    PLAYER_SAY_MSG_SIZE_FIELD_NUMBER: _ClassVar[int]
    PLAYER_HEAR_MAX_FIELD_NUMBER: _ClassVar[int]
    PLAYER_HEAR_INC_FIELD_NUMBER: _ClassVar[int]
    PLAYER_HEAR_DECAY_FIELD_NUMBER: _ClassVar[int]
    CATCH_BAN_CYCLE_FIELD_NUMBER: _ClassVar[int]
    SLOW_DOWN_FACTOR_FIELD_NUMBER: _ClassVar[int]
    USE_OFFSIDE_FIELD_NUMBER: _ClassVar[int]
    KICKOFF_OFFSIDE_FIELD_NUMBER: _ClassVar[int]
    OFFSIDE_KICK_MARGIN_FIELD_NUMBER: _ClassVar[int]
    AUDIO_CUT_DIST_FIELD_NUMBER: _ClassVar[int]
    DIST_QUANTIZE_STEP_FIELD_NUMBER: _ClassVar[int]
    LANDMARK_DIST_QUANTIZE_STEP_FIELD_NUMBER: _ClassVar[int]
    DIR_QUANTIZE_STEP_FIELD_NUMBER: _ClassVar[int]
    DIST_QUANTIZE_STEP_L_FIELD_NUMBER: _ClassVar[int]
    DIST_QUANTIZE_STEP_R_FIELD_NUMBER: _ClassVar[int]
    LANDMARK_DIST_QUANTIZE_STEP_L_FIELD_NUMBER: _ClassVar[int]
    LANDMARK_DIST_QUANTIZE_STEP_R_FIELD_NUMBER: _ClassVar[int]
    DIR_QUANTIZE_STEP_L_FIELD_NUMBER: _ClassVar[int]
    DIR_QUANTIZE_STEP_R_FIELD_NUMBER: _ClassVar[int]
    COACH_MODE_FIELD_NUMBER: _ClassVar[int]
    COACH_WITH_REFEREE_MODE_FIELD_NUMBER: _ClassVar[int]
    USE_OLD_COACH_HEAR_FIELD_NUMBER: _ClassVar[int]
    SLOWNESS_ON_TOP_FOR_LEFT_TEAM_FIELD_NUMBER: _ClassVar[int]
    SLOWNESS_ON_TOP_FOR_RIGHT_TEAM_FIELD_NUMBER: _ClassVar[int]
    START_GOAL_L_FIELD_NUMBER: _ClassVar[int]
    START_GOAL_R_FIELD_NUMBER: _ClassVar[int]
    FULLSTATE_L_FIELD_NUMBER: _ClassVar[int]
    FULLSTATE_R_FIELD_NUMBER: _ClassVar[int]
    DROP_BALL_TIME_FIELD_NUMBER: _ClassVar[int]
    SYNCH_MODE_FIELD_NUMBER: _ClassVar[int]
    SYNCH_OFFSET_FIELD_NUMBER: _ClassVar[int]
    SYNCH_MICRO_SLEEP_FIELD_NUMBER: _ClassVar[int]
    POINT_TO_BAN_FIELD_NUMBER: _ClassVar[int]
    POINT_TO_DURATION_FIELD_NUMBER: _ClassVar[int]
    PLAYER_PORT_FIELD_NUMBER: _ClassVar[int]
    TRAINER_PORT_FIELD_NUMBER: _ClassVar[int]
    ONLINE_COACH_PORT_FIELD_NUMBER: _ClassVar[int]
    VERBOSE_MODE_FIELD_NUMBER: _ClassVar[int]
    COACH_SEND_VI_STEP_FIELD_NUMBER: _ClassVar[int]
    REPLAY_FILE_FIELD_NUMBER: _ClassVar[int]
    LANDMARK_FILE_FIELD_NUMBER: _ClassVar[int]
    SEND_COMMS_FIELD_NUMBER: _ClassVar[int]
    TEXT_LOGGING_FIELD_NUMBER: _ClassVar[int]
    GAME_LOGGING_FIELD_NUMBER: _ClassVar[int]
    GAME_LOG_VERSION_FIELD_NUMBER: _ClassVar[int]
    TEXT_LOG_DIR_FIELD_NUMBER: _ClassVar[int]
    GAME_LOG_DIR_FIELD_NUMBER: _ClassVar[int]
    TEXT_LOG_FIXED_NAME_FIELD_NUMBER: _ClassVar[int]
    GAME_LOG_FIXED_NAME_FIELD_NUMBER: _ClassVar[int]
    USE_TEXT_LOG_FIXED_FIELD_NUMBER: _ClassVar[int]
    USE_GAME_LOG_FIXED_FIELD_NUMBER: _ClassVar[int]
    USE_TEXT_LOG_DATED_FIELD_NUMBER: _ClassVar[int]
    USE_GAME_LOG_DATED_FIELD_NUMBER: _ClassVar[int]
    LOG_DATE_FORMAT_FIELD_NUMBER: _ClassVar[int]
    LOG_TIMES_FIELD_NUMBER: _ClassVar[int]
    RECORD_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TEXT_LOG_COMPRESSION_FIELD_NUMBER: _ClassVar[int]
    GAME_LOG_COMPRESSION_FIELD_NUMBER: _ClassVar[int]
    USE_PROFILE_FIELD_NUMBER: _ClassVar[int]
    TACKLE_DIST_FIELD_NUMBER: _ClassVar[int]
    TACKLE_BACK_DIST_FIELD_NUMBER: _ClassVar[int]
    TACKLE_WIDTH_FIELD_NUMBER: _ClassVar[int]
    TACKLE_EXPONENT_FIELD_NUMBER: _ClassVar[int]
    TACKLE_CYCLES_FIELD_NUMBER: _ClassVar[int]
    TACKLE_POWER_RATE_FIELD_NUMBER: _ClassVar[int]
    FREEFORM_WAIT_PERIOD_FIELD_NUMBER: _ClassVar[int]
    FREEFORM_SEND_PERIOD_FIELD_NUMBER: _ClassVar[int]
    FREE_KICK_FAULTS_FIELD_NUMBER: _ClassVar[int]
    BACK_PASSES_FIELD_NUMBER: _ClassVar[int]
    PROPER_GOAL_KICKS_FIELD_NUMBER: _ClassVar[int]
    STOPPED_BALL_VEL_FIELD_NUMBER: _ClassVar[int]
    MAX_GOAL_KICKS_FIELD_NUMBER: _ClassVar[int]
    CLANG_DEL_WIN_FIELD_NUMBER: _ClassVar[int]
    CLANG_RULE_WIN_FIELD_NUMBER: _ClassVar[int]
    AUTO_MODE_FIELD_NUMBER: _ClassVar[int]
    KICK_OFF_WAIT_FIELD_NUMBER: _ClassVar[int]
    CONNECT_WAIT_FIELD_NUMBER: _ClassVar[int]
    GAME_OVER_WAIT_FIELD_NUMBER: _ClassVar[int]
    TEAM_L_START_FIELD_NUMBER: _ClassVar[int]
    TEAM_R_START_FIELD_NUMBER: _ClassVar[int]
    KEEPAWAY_MODE_FIELD_NUMBER: _ClassVar[int]
    KEEPAWAY_LENGTH_FIELD_NUMBER: _ClassVar[int]
    KEEPAWAY_WIDTH_FIELD_NUMBER: _ClassVar[int]
    KEEPAWAY_LOGGING_FIELD_NUMBER: _ClassVar[int]
    KEEPAWAY_LOG_DIR_FIELD_NUMBER: _ClassVar[int]
    KEEPAWAY_LOG_FIXED_NAME_FIELD_NUMBER: _ClassVar[int]
    KEEPAWAY_LOG_FIXED_FIELD_NUMBER: _ClassVar[int]
    KEEPAWAY_LOG_DATED_FIELD_NUMBER: _ClassVar[int]
    KEEPAWAY_START_FIELD_NUMBER: _ClassVar[int]
    NR_NORMAL_HALFS_FIELD_NUMBER: _ClassVar[int]
    NR_EXTRA_HALFS_FIELD_NUMBER: _ClassVar[int]
    PENALTY_SHOOT_OUTS_FIELD_NUMBER: _ClassVar[int]
    PEN_BEFORE_SETUP_WAIT_FIELD_NUMBER: _ClassVar[int]
    PEN_SETUP_WAIT_FIELD_NUMBER: _ClassVar[int]
    PEN_READY_WAIT_FIELD_NUMBER: _ClassVar[int]
    PEN_TAKEN_WAIT_FIELD_NUMBER: _ClassVar[int]
    PEN_NR_KICKS_FIELD_NUMBER: _ClassVar[int]
    PEN_MAX_EXTRA_KICKS_FIELD_NUMBER: _ClassVar[int]
    PEN_DIST_X_FIELD_NUMBER: _ClassVar[int]
    PEN_RANDOM_WINNER_FIELD_NUMBER: _ClassVar[int]
    PEN_ALLOW_MULT_KICKS_FIELD_NUMBER: _ClassVar[int]
    PEN_MAX_GOALIE_DIST_X_FIELD_NUMBER: _ClassVar[int]
    PEN_COACH_MOVES_PLAYERS_FIELD_NUMBER: _ClassVar[int]
    MODULE_DIR_FIELD_NUMBER: _ClassVar[int]
    BALL_STUCK_AREA_FIELD_NUMBER: _ClassVar[int]
    COACH_MSG_FILE_FIELD_NUMBER: _ClassVar[int]
    MAX_TACKLE_POWER_FIELD_NUMBER: _ClassVar[int]
    MAX_BACK_TACKLE_POWER_FIELD_NUMBER: _ClassVar[int]
    PLAYER_SPEED_MAX_MIN_FIELD_NUMBER: _ClassVar[int]
    EXTRA_STAMINA_FIELD_NUMBER: _ClassVar[int]
    SYNCH_SEE_OFFSET_FIELD_NUMBER: _ClassVar[int]
    EXTRA_HALF_TIME_FIELD_NUMBER: _ClassVar[int]
    STAMINA_CAPACITY_FIELD_NUMBER: _ClassVar[int]
    MAX_DASH_ANGLE_FIELD_NUMBER: _ClassVar[int]
    MIN_DASH_ANGLE_FIELD_NUMBER: _ClassVar[int]
    DASH_ANGLE_STEP_FIELD_NUMBER: _ClassVar[int]
    SIDE_DASH_RATE_FIELD_NUMBER: _ClassVar[int]
    BACK_DASH_RATE_FIELD_NUMBER: _ClassVar[int]
    MAX_DASH_POWER_FIELD_NUMBER: _ClassVar[int]
    MIN_DASH_POWER_FIELD_NUMBER: _ClassVar[int]
    TACKLE_RAND_FACTOR_FIELD_NUMBER: _ClassVar[int]
    FOUL_DETECT_PROBABILITY_FIELD_NUMBER: _ClassVar[int]
    FOUL_EXPONENT_FIELD_NUMBER: _ClassVar[int]
    FOUL_CYCLES_FIELD_NUMBER: _ClassVar[int]
    GOLDEN_GOAL_FIELD_NUMBER: _ClassVar[int]
    RED_CARD_PROBABILITY_FIELD_NUMBER: _ClassVar[int]
    ILLEGAL_DEFENSE_DURATION_FIELD_NUMBER: _ClassVar[int]
    ILLEGAL_DEFENSE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ILLEGAL_DEFENSE_DIST_X_FIELD_NUMBER: _ClassVar[int]
    ILLEGAL_DEFENSE_WIDTH_FIELD_NUMBER: _ClassVar[int]
    FIXED_TEAMNAME_L_FIELD_NUMBER: _ClassVar[int]
    FIXED_TEAMNAME_R_FIELD_NUMBER: _ClassVar[int]
    MAX_CATCH_ANGLE_FIELD_NUMBER: _ClassVar[int]
    MIN_CATCH_ANGLE_FIELD_NUMBER: _ClassVar[int]
    RANDOM_SEED_FIELD_NUMBER: _ClassVar[int]
    LONG_KICK_POWER_FACTOR_FIELD_NUMBER: _ClassVar[int]
    LONG_KICK_DELAY_FIELD_NUMBER: _ClassVar[int]
    MAX_MONITORS_FIELD_NUMBER: _ClassVar[int]
    CATCHABLE_AREA_FIELD_NUMBER: _ClassVar[int]
    REAL_SPEED_MAX_FIELD_NUMBER: _ClassVar[int]
    PITCH_HALF_LENGTH_FIELD_NUMBER: _ClassVar[int]
    PITCH_HALF_WIDTH_FIELD_NUMBER: _ClassVar[int]
    OUR_PENALTY_AREA_LINE_X_FIELD_NUMBER: _ClassVar[int]
    THEIR_PENALTY_AREA_LINE_X_FIELD_NUMBER: _ClassVar[int]
    PENALTY_AREA_HALF_WIDTH_FIELD_NUMBER: _ClassVar[int]
    PENALTY_AREA_LENGTH_FIELD_NUMBER: _ClassVar[int]
    goal_width: float
    inertia_moment: float
    player_size: float
    player_decay: float
    player_rand: float
    player_weight: float
    player_speed_max: float
    player_accel_max: float
    stamina_max: float
    stamina_inc_max: float
    recover_init: float
    recover_dec_thr: float
    recover_min: float
    recover_dec: float
    effort_init: float
    effort_dec_thr: float
    effort_min: float
    effort_dec: float
    effort_inc_thr: float
    effort_inc: float
    kick_rand: float
    team_actuator_noise: bool
    player_rand_factor_l: float
    player_rand_factor_r: float
    kick_rand_factor_l: float
    kick_rand_factor_r: float
    ball_size: float
    ball_decay: float
    ball_rand: float
    ball_weight: float
    ball_speed_max: float
    ball_accel_max: float
    dash_power_rate: float
    kick_power_rate: float
    kickable_margin: float
    control_radius: float
    control_radius_width: float
    max_power: float
    min_power: float
    max_moment: float
    min_moment: float
    max_neck_moment: float
    min_neck_moment: float
    max_neck_angle: float
    min_neck_angle: float
    visible_angle: float
    visible_distance: float
    wind_dir: float
    wind_force: float
    wind_angle: float
    wind_rand: float
    kickable_area: float
    catch_area_l: float
    catch_area_w: float
    catch_probability: float
    goalie_max_moves: int
    corner_kick_margin: float
    offside_active_area_size: float
    wind_none: bool
    use_wind_random: bool
    coach_say_count_max: int
    coach_say_msg_size: int
    clang_win_size: int
    clang_define_win: int
    clang_meta_win: int
    clang_advice_win: int
    clang_info_win: int
    clang_mess_delay: int
    clang_mess_per_cycle: int
    half_time: int
    simulator_step: int
    send_step: int
    recv_step: int
    sense_body_step: int
    lcm_step: int
    player_say_msg_size: int
    player_hear_max: int
    player_hear_inc: int
    player_hear_decay: int
    catch_ban_cycle: int
    slow_down_factor: int
    use_offside: bool
    kickoff_offside: bool
    offside_kick_margin: float
    audio_cut_dist: float
    dist_quantize_step: float
    landmark_dist_quantize_step: float
    dir_quantize_step: float
    dist_quantize_step_l: float
    dist_quantize_step_r: float
    landmark_dist_quantize_step_l: float
    landmark_dist_quantize_step_r: float
    dir_quantize_step_l: float
    dir_quantize_step_r: float
    coach_mode: bool
    coach_with_referee_mode: bool
    use_old_coach_hear: bool
    slowness_on_top_for_left_team: float
    slowness_on_top_for_right_team: float
    start_goal_l: int
    start_goal_r: int
    fullstate_l: bool
    fullstate_r: bool
    drop_ball_time: int
    synch_mode: bool
    synch_offset: int
    synch_micro_sleep: int
    point_to_ban: int
    point_to_duration: int
    player_port: int
    trainer_port: int
    online_coach_port: int
    verbose_mode: bool
    coach_send_vi_step: int
    replay_file: str
    landmark_file: str
    send_comms: bool
    text_logging: bool
    game_logging: bool
    game_log_version: int
    text_log_dir: str
    game_log_dir: str
    text_log_fixed_name: str
    game_log_fixed_name: str
    use_text_log_fixed: bool
    use_game_log_fixed: bool
    use_text_log_dated: bool
    use_game_log_dated: bool
    log_date_format: str
    log_times: bool
    record_message: bool
    text_log_compression: int
    game_log_compression: int
    use_profile: bool
    tackle_dist: float
    tackle_back_dist: float
    tackle_width: float
    tackle_exponent: float
    tackle_cycles: int
    tackle_power_rate: float
    freeform_wait_period: int
    freeform_send_period: int
    free_kick_faults: bool
    back_passes: bool
    proper_goal_kicks: bool
    stopped_ball_vel: float
    max_goal_kicks: int
    clang_del_win: int
    clang_rule_win: int
    auto_mode: bool
    kick_off_wait: int
    connect_wait: int
    game_over_wait: int
    team_l_start: str
    team_r_start: str
    keepaway_mode: bool
    keepaway_length: float
    keepaway_width: float
    keepaway_logging: bool
    keepaway_log_dir: str
    keepaway_log_fixed_name: str
    keepaway_log_fixed: bool
    keepaway_log_dated: bool
    keepaway_start: int
    nr_normal_halfs: int
    nr_extra_halfs: int
    penalty_shoot_outs: bool
    pen_before_setup_wait: int
    pen_setup_wait: int
    pen_ready_wait: int
    pen_taken_wait: int
    pen_nr_kicks: int
    pen_max_extra_kicks: int
    pen_dist_x: float
    pen_random_winner: bool
    pen_allow_mult_kicks: bool
    pen_max_goalie_dist_x: float
    pen_coach_moves_players: bool
    module_dir: str
    ball_stuck_area: float
    coach_msg_file: str
    max_tackle_power: float
    max_back_tackle_power: float
    player_speed_max_min: float
    extra_stamina: float
    synch_see_offset: int
    extra_half_time: int
    stamina_capacity: float
    max_dash_angle: float
    min_dash_angle: float
    dash_angle_step: float
    side_dash_rate: float
    back_dash_rate: float
    max_dash_power: float
    min_dash_power: float
    tackle_rand_factor: float
    foul_detect_probability: float
    foul_exponent: float
    foul_cycles: int
    golden_goal: bool
    red_card_probability: float
    illegal_defense_duration: int
    illegal_defense_number: int
    illegal_defense_dist_x: float
    illegal_defense_width: float
    fixed_teamname_l: str
    fixed_teamname_r: str
    max_catch_angle: float
    min_catch_angle: float
    random_seed: int
    long_kick_power_factor: float
    long_kick_delay: int
    max_monitors: int
    catchable_area: float
    real_speed_max: float
    pitch_half_length: float
    pitch_half_width: float
    our_penalty_area_line_x: float
    their_penalty_area_line_x: float
    penalty_area_half_width: float
    penalty_area_length: float
    def __init__(self, goal_width: _Optional[float] = ..., inertia_moment: _Optional[float] = ..., player_size: _Optional[float] = ..., player_decay: _Optional[float] = ..., player_rand: _Optional[float] = ..., player_weight: _Optional[float] = ..., player_speed_max: _Optional[float] = ..., player_accel_max: _Optional[float] = ..., stamina_max: _Optional[float] = ..., stamina_inc_max: _Optional[float] = ..., recover_init: _Optional[float] = ..., recover_dec_thr: _Optional[float] = ..., recover_min: _Optional[float] = ..., recover_dec: _Optional[float] = ..., effort_init: _Optional[float] = ..., effort_dec_thr: _Optional[float] = ..., effort_min: _Optional[float] = ..., effort_dec: _Optional[float] = ..., effort_inc_thr: _Optional[float] = ..., effort_inc: _Optional[float] = ..., kick_rand: _Optional[float] = ..., team_actuator_noise: bool = ..., player_rand_factor_l: _Optional[float] = ..., player_rand_factor_r: _Optional[float] = ..., kick_rand_factor_l: _Optional[float] = ..., kick_rand_factor_r: _Optional[float] = ..., ball_size: _Optional[float] = ..., ball_decay: _Optional[float] = ..., ball_rand: _Optional[float] = ..., ball_weight: _Optional[float] = ..., ball_speed_max: _Optional[float] = ..., ball_accel_max: _Optional[float] = ..., dash_power_rate: _Optional[float] = ..., kick_power_rate: _Optional[float] = ..., kickable_margin: _Optional[float] = ..., control_radius: _Optional[float] = ..., control_radius_width: _Optional[float] = ..., max_power: _Optional[float] = ..., min_power: _Optional[float] = ..., max_moment: _Optional[float] = ..., min_moment: _Optional[float] = ..., max_neck_moment: _Optional[float] = ..., min_neck_moment: _Optional[float] = ..., max_neck_angle: _Optional[float] = ..., min_neck_angle: _Optional[float] = ..., visible_angle: _Optional[float] = ..., visible_distance: _Optional[float] = ..., wind_dir: _Optional[float] = ..., wind_force: _Optional[float] = ..., wind_angle: _Optional[float] = ..., wind_rand: _Optional[float] = ..., kickable_area: _Optional[float] = ..., catch_area_l: _Optional[float] = ..., catch_area_w: _Optional[float] = ..., catch_probability: _Optional[float] = ..., goalie_max_moves: _Optional[int] = ..., corner_kick_margin: _Optional[float] = ..., offside_active_area_size: _Optional[float] = ..., wind_none: bool = ..., use_wind_random: bool = ..., coach_say_count_max: _Optional[int] = ..., coach_say_msg_size: _Optional[int] = ..., clang_win_size: _Optional[int] = ..., clang_define_win: _Optional[int] = ..., clang_meta_win: _Optional[int] = ..., clang_advice_win: _Optional[int] = ..., clang_info_win: _Optional[int] = ..., clang_mess_delay: _Optional[int] = ..., clang_mess_per_cycle: _Optional[int] = ..., half_time: _Optional[int] = ..., simulator_step: _Optional[int] = ..., send_step: _Optional[int] = ..., recv_step: _Optional[int] = ..., sense_body_step: _Optional[int] = ..., lcm_step: _Optional[int] = ..., player_say_msg_size: _Optional[int] = ..., player_hear_max: _Optional[int] = ..., player_hear_inc: _Optional[int] = ..., player_hear_decay: _Optional[int] = ..., catch_ban_cycle: _Optional[int] = ..., slow_down_factor: _Optional[int] = ..., use_offside: bool = ..., kickoff_offside: bool = ..., offside_kick_margin: _Optional[float] = ..., audio_cut_dist: _Optional[float] = ..., dist_quantize_step: _Optional[float] = ..., landmark_dist_quantize_step: _Optional[float] = ..., dir_quantize_step: _Optional[float] = ..., dist_quantize_step_l: _Optional[float] = ..., dist_quantize_step_r: _Optional[float] = ..., landmark_dist_quantize_step_l: _Optional[float] = ..., landmark_dist_quantize_step_r: _Optional[float] = ..., dir_quantize_step_l: _Optional[float] = ..., dir_quantize_step_r: _Optional[float] = ..., coach_mode: bool = ..., coach_with_referee_mode: bool = ..., use_old_coach_hear: bool = ..., slowness_on_top_for_left_team: _Optional[float] = ..., slowness_on_top_for_right_team: _Optional[float] = ..., start_goal_l: _Optional[int] = ..., start_goal_r: _Optional[int] = ..., fullstate_l: bool = ..., fullstate_r: bool = ..., drop_ball_time: _Optional[int] = ..., synch_mode: bool = ..., synch_offset: _Optional[int] = ..., synch_micro_sleep: _Optional[int] = ..., point_to_ban: _Optional[int] = ..., point_to_duration: _Optional[int] = ..., player_port: _Optional[int] = ..., trainer_port: _Optional[int] = ..., online_coach_port: _Optional[int] = ..., verbose_mode: bool = ..., coach_send_vi_step: _Optional[int] = ..., replay_file: _Optional[str] = ..., landmark_file: _Optional[str] = ..., send_comms: bool = ..., text_logging: bool = ..., game_logging: bool = ..., game_log_version: _Optional[int] = ..., text_log_dir: _Optional[str] = ..., game_log_dir: _Optional[str] = ..., text_log_fixed_name: _Optional[str] = ..., game_log_fixed_name: _Optional[str] = ..., use_text_log_fixed: bool = ..., use_game_log_fixed: bool = ..., use_text_log_dated: bool = ..., use_game_log_dated: bool = ..., log_date_format: _Optional[str] = ..., log_times: bool = ..., record_message: bool = ..., text_log_compression: _Optional[int] = ..., game_log_compression: _Optional[int] = ..., use_profile: bool = ..., tackle_dist: _Optional[float] = ..., tackle_back_dist: _Optional[float] = ..., tackle_width: _Optional[float] = ..., tackle_exponent: _Optional[float] = ..., tackle_cycles: _Optional[int] = ..., tackle_power_rate: _Optional[float] = ..., freeform_wait_period: _Optional[int] = ..., freeform_send_period: _Optional[int] = ..., free_kick_faults: bool = ..., back_passes: bool = ..., proper_goal_kicks: bool = ..., stopped_ball_vel: _Optional[float] = ..., max_goal_kicks: _Optional[int] = ..., clang_del_win: _Optional[int] = ..., clang_rule_win: _Optional[int] = ..., auto_mode: bool = ..., kick_off_wait: _Optional[int] = ..., connect_wait: _Optional[int] = ..., game_over_wait: _Optional[int] = ..., team_l_start: _Optional[str] = ..., team_r_start: _Optional[str] = ..., keepaway_mode: bool = ..., keepaway_length: _Optional[float] = ..., keepaway_width: _Optional[float] = ..., keepaway_logging: bool = ..., keepaway_log_dir: _Optional[str] = ..., keepaway_log_fixed_name: _Optional[str] = ..., keepaway_log_fixed: bool = ..., keepaway_log_dated: bool = ..., keepaway_start: _Optional[int] = ..., nr_normal_halfs: _Optional[int] = ..., nr_extra_halfs: _Optional[int] = ..., penalty_shoot_outs: bool = ..., pen_before_setup_wait: _Optional[int] = ..., pen_setup_wait: _Optional[int] = ..., pen_ready_wait: _Optional[int] = ..., pen_taken_wait: _Optional[int] = ..., pen_nr_kicks: _Optional[int] = ..., pen_max_extra_kicks: _Optional[int] = ..., pen_dist_x: _Optional[float] = ..., pen_random_winner: bool = ..., pen_allow_mult_kicks: bool = ..., pen_max_goalie_dist_x: _Optional[float] = ..., pen_coach_moves_players: bool = ..., module_dir: _Optional[str] = ..., ball_stuck_area: _Optional[float] = ..., coach_msg_file: _Optional[str] = ..., max_tackle_power: _Optional[float] = ..., max_back_tackle_power: _Optional[float] = ..., player_speed_max_min: _Optional[float] = ..., extra_stamina: _Optional[float] = ..., synch_see_offset: _Optional[int] = ..., extra_half_time: _Optional[int] = ..., stamina_capacity: _Optional[float] = ..., max_dash_angle: _Optional[float] = ..., min_dash_angle: _Optional[float] = ..., dash_angle_step: _Optional[float] = ..., side_dash_rate: _Optional[float] = ..., back_dash_rate: _Optional[float] = ..., max_dash_power: _Optional[float] = ..., min_dash_power: _Optional[float] = ..., tackle_rand_factor: _Optional[float] = ..., foul_detect_probability: _Optional[float] = ..., foul_exponent: _Optional[float] = ..., foul_cycles: _Optional[int] = ..., golden_goal: bool = ..., red_card_probability: _Optional[float] = ..., illegal_defense_duration: _Optional[int] = ..., illegal_defense_number: _Optional[int] = ..., illegal_defense_dist_x: _Optional[float] = ..., illegal_defense_width: _Optional[float] = ..., fixed_teamname_l: _Optional[str] = ..., fixed_teamname_r: _Optional[str] = ..., max_catch_angle: _Optional[float] = ..., min_catch_angle: _Optional[float] = ..., random_seed: _Optional[int] = ..., long_kick_power_factor: _Optional[float] = ..., long_kick_delay: _Optional[int] = ..., max_monitors: _Optional[int] = ..., catchable_area: _Optional[float] = ..., real_speed_max: _Optional[float] = ..., pitch_half_length: _Optional[float] = ..., pitch_half_width: _Optional[float] = ..., our_penalty_area_line_x: _Optional[float] = ..., their_penalty_area_line_x: _Optional[float] = ..., penalty_area_half_width: _Optional[float] = ..., penalty_area_length: _Optional[float] = ...) -> None: ...

class PlayerParam(_message.Message):
    __slots__ = ("player_types", "subs_max", "pt_max", "allow_mult_default_type", "player_speed_max_delta_min", "player_speed_max_delta_max", "stamina_inc_max_delta_factor", "player_decay_delta_min", "player_decay_delta_max", "inertia_moment_delta_factor", "dash_power_rate_delta_min", "dash_power_rate_delta_max", "player_size_delta_factor", "kickable_margin_delta_min", "kickable_margin_delta_max", "kick_rand_delta_factor", "extra_stamina_delta_min", "extra_stamina_delta_max", "effort_max_delta_factor", "effort_min_delta_factor", "random_seed", "new_dash_power_rate_delta_min", "new_dash_power_rate_delta_max", "new_stamina_inc_max_delta_factor", "kick_power_rate_delta_min", "kick_power_rate_delta_max", "foul_detect_probability_delta_factor", "catchable_area_l_stretch_min", "catchable_area_l_stretch_max")
    PLAYER_TYPES_FIELD_NUMBER: _ClassVar[int]
    SUBS_MAX_FIELD_NUMBER: _ClassVar[int]
    PT_MAX_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MULT_DEFAULT_TYPE_FIELD_NUMBER: _ClassVar[int]
    PLAYER_SPEED_MAX_DELTA_MIN_FIELD_NUMBER: _ClassVar[int]
    PLAYER_SPEED_MAX_DELTA_MAX_FIELD_NUMBER: _ClassVar[int]
    STAMINA_INC_MAX_DELTA_FACTOR_FIELD_NUMBER: _ClassVar[int]
    PLAYER_DECAY_DELTA_MIN_FIELD_NUMBER: _ClassVar[int]
    PLAYER_DECAY_DELTA_MAX_FIELD_NUMBER: _ClassVar[int]
    INERTIA_MOMENT_DELTA_FACTOR_FIELD_NUMBER: _ClassVar[int]
    DASH_POWER_RATE_DELTA_MIN_FIELD_NUMBER: _ClassVar[int]
    DASH_POWER_RATE_DELTA_MAX_FIELD_NUMBER: _ClassVar[int]
    PLAYER_SIZE_DELTA_FACTOR_FIELD_NUMBER: _ClassVar[int]
    KICKABLE_MARGIN_DELTA_MIN_FIELD_NUMBER: _ClassVar[int]
    KICKABLE_MARGIN_DELTA_MAX_FIELD_NUMBER: _ClassVar[int]
    KICK_RAND_DELTA_FACTOR_FIELD_NUMBER: _ClassVar[int]
    EXTRA_STAMINA_DELTA_MIN_FIELD_NUMBER: _ClassVar[int]
    EXTRA_STAMINA_DELTA_MAX_FIELD_NUMBER: _ClassVar[int]
    EFFORT_MAX_DELTA_FACTOR_FIELD_NUMBER: _ClassVar[int]
    EFFORT_MIN_DELTA_FACTOR_FIELD_NUMBER: _ClassVar[int]
    RANDOM_SEED_FIELD_NUMBER: _ClassVar[int]
    NEW_DASH_POWER_RATE_DELTA_MIN_FIELD_NUMBER: _ClassVar[int]
    NEW_DASH_POWER_RATE_DELTA_MAX_FIELD_NUMBER: _ClassVar[int]
    NEW_STAMINA_INC_MAX_DELTA_FACTOR_FIELD_NUMBER: _ClassVar[int]
    KICK_POWER_RATE_DELTA_MIN_FIELD_NUMBER: _ClassVar[int]
    KICK_POWER_RATE_DELTA_MAX_FIELD_NUMBER: _ClassVar[int]
    FOUL_DETECT_PROBABILITY_DELTA_FACTOR_FIELD_NUMBER: _ClassVar[int]
    CATCHABLE_AREA_L_STRETCH_MIN_FIELD_NUMBER: _ClassVar[int]
    CATCHABLE_AREA_L_STRETCH_MAX_FIELD_NUMBER: _ClassVar[int]
    player_types: int
    subs_max: int
    pt_max: int
    allow_mult_default_type: bool
    player_speed_max_delta_min: float
    player_speed_max_delta_max: float
    stamina_inc_max_delta_factor: float
    player_decay_delta_min: float
    player_decay_delta_max: float
    inertia_moment_delta_factor: float
    dash_power_rate_delta_min: float
    dash_power_rate_delta_max: float
    player_size_delta_factor: float
    kickable_margin_delta_min: float
    kickable_margin_delta_max: float
    kick_rand_delta_factor: float
    extra_stamina_delta_min: float
    extra_stamina_delta_max: float
    effort_max_delta_factor: float
    effort_min_delta_factor: float
    random_seed: int
    new_dash_power_rate_delta_min: float
    new_dash_power_rate_delta_max: float
    new_stamina_inc_max_delta_factor: float
    kick_power_rate_delta_min: float
    kick_power_rate_delta_max: float
    foul_detect_probability_delta_factor: float
    catchable_area_l_stretch_min: float
    catchable_area_l_stretch_max: float
    def __init__(self, player_types: _Optional[int] = ..., subs_max: _Optional[int] = ..., pt_max: _Optional[int] = ..., allow_mult_default_type: bool = ..., player_speed_max_delta_min: _Optional[float] = ..., player_speed_max_delta_max: _Optional[float] = ..., stamina_inc_max_delta_factor: _Optional[float] = ..., player_decay_delta_min: _Optional[float] = ..., player_decay_delta_max: _Optional[float] = ..., inertia_moment_delta_factor: _Optional[float] = ..., dash_power_rate_delta_min: _Optional[float] = ..., dash_power_rate_delta_max: _Optional[float] = ..., player_size_delta_factor: _Optional[float] = ..., kickable_margin_delta_min: _Optional[float] = ..., kickable_margin_delta_max: _Optional[float] = ..., kick_rand_delta_factor: _Optional[float] = ..., extra_stamina_delta_min: _Optional[float] = ..., extra_stamina_delta_max: _Optional[float] = ..., effort_max_delta_factor: _Optional[float] = ..., effort_min_delta_factor: _Optional[float] = ..., random_seed: _Optional[int] = ..., new_dash_power_rate_delta_min: _Optional[float] = ..., new_dash_power_rate_delta_max: _Optional[float] = ..., new_stamina_inc_max_delta_factor: _Optional[float] = ..., kick_power_rate_delta_min: _Optional[float] = ..., kick_power_rate_delta_max: _Optional[float] = ..., foul_detect_probability_delta_factor: _Optional[float] = ..., catchable_area_l_stretch_min: _Optional[float] = ..., catchable_area_l_stretch_max: _Optional[float] = ...) -> None: ...

class PlayerType(_message.Message):
    __slots__ = ("id", "player_speed_max", "stamina_inc_max", "player_decay", "inertia_moment", "dash_power_rate", "player_size", "kickable_margin", "kick_rand", "extra_stamina", "effort_max", "effort_min", "kick_power_rate", "foul_detect_probability", "catchable_area_l_stretch", "unum_far_length", "unum_too_far_length", "team_far_length", "team_too_far_length", "player_max_observation_length", "ball_vel_far_length", "ball_vel_too_far_length", "ball_max_observation_length", "flag_chg_far_length", "flag_chg_too_far_length", "flag_max_observation_length", "kickable_area", "reliable_catchable_dist", "max_catchable_dist", "real_speed_max", "player_speed_max2", "real_speed_max2", "cycles_to_reach_max_speed")
    ID_FIELD_NUMBER: _ClassVar[int]
    PLAYER_SPEED_MAX_FIELD_NUMBER: _ClassVar[int]
    STAMINA_INC_MAX_FIELD_NUMBER: _ClassVar[int]
    PLAYER_DECAY_FIELD_NUMBER: _ClassVar[int]
    INERTIA_MOMENT_FIELD_NUMBER: _ClassVar[int]
    DASH_POWER_RATE_FIELD_NUMBER: _ClassVar[int]
    PLAYER_SIZE_FIELD_NUMBER: _ClassVar[int]
    KICKABLE_MARGIN_FIELD_NUMBER: _ClassVar[int]
    KICK_RAND_FIELD_NUMBER: _ClassVar[int]
    EXTRA_STAMINA_FIELD_NUMBER: _ClassVar[int]
    EFFORT_MAX_FIELD_NUMBER: _ClassVar[int]
    EFFORT_MIN_FIELD_NUMBER: _ClassVar[int]
    KICK_POWER_RATE_FIELD_NUMBER: _ClassVar[int]
    FOUL_DETECT_PROBABILITY_FIELD_NUMBER: _ClassVar[int]
    CATCHABLE_AREA_L_STRETCH_FIELD_NUMBER: _ClassVar[int]
    UNUM_FAR_LENGTH_FIELD_NUMBER: _ClassVar[int]
    UNUM_TOO_FAR_LENGTH_FIELD_NUMBER: _ClassVar[int]
    TEAM_FAR_LENGTH_FIELD_NUMBER: _ClassVar[int]
    TEAM_TOO_FAR_LENGTH_FIELD_NUMBER: _ClassVar[int]
    PLAYER_MAX_OBSERVATION_LENGTH_FIELD_NUMBER: _ClassVar[int]
    BALL_VEL_FAR_LENGTH_FIELD_NUMBER: _ClassVar[int]
    BALL_VEL_TOO_FAR_LENGTH_FIELD_NUMBER: _ClassVar[int]
    BALL_MAX_OBSERVATION_LENGTH_FIELD_NUMBER: _ClassVar[int]
    FLAG_CHG_FAR_LENGTH_FIELD_NUMBER: _ClassVar[int]
    FLAG_CHG_TOO_FAR_LENGTH_FIELD_NUMBER: _ClassVar[int]
    FLAG_MAX_OBSERVATION_LENGTH_FIELD_NUMBER: _ClassVar[int]
    KICKABLE_AREA_FIELD_NUMBER: _ClassVar[int]
    RELIABLE_CATCHABLE_DIST_FIELD_NUMBER: _ClassVar[int]
    MAX_CATCHABLE_DIST_FIELD_NUMBER: _ClassVar[int]
    REAL_SPEED_MAX_FIELD_NUMBER: _ClassVar[int]
    PLAYER_SPEED_MAX2_FIELD_NUMBER: _ClassVar[int]
    REAL_SPEED_MAX2_FIELD_NUMBER: _ClassVar[int]
    CYCLES_TO_REACH_MAX_SPEED_FIELD_NUMBER: _ClassVar[int]
    id: int
    player_speed_max: float
    stamina_inc_max: float
    player_decay: float
    inertia_moment: float
    dash_power_rate: float
    player_size: float
    kickable_margin: float
    kick_rand: float
    extra_stamina: float
    effort_max: float
    effort_min: float
    kick_power_rate: float
    foul_detect_probability: float
    catchable_area_l_stretch: float
    unum_far_length: float
    unum_too_far_length: float
    team_far_length: float
    team_too_far_length: float
    player_max_observation_length: float
    ball_vel_far_length: float
    ball_vel_too_far_length: float
    ball_max_observation_length: float
    flag_chg_far_length: float
    flag_chg_too_far_length: float
    flag_max_observation_length: float
    kickable_area: float
    reliable_catchable_dist: float
    max_catchable_dist: float
    real_speed_max: float
    player_speed_max2: float
    real_speed_max2: float
    cycles_to_reach_max_speed: int
    def __init__(self, id: _Optional[int] = ..., player_speed_max: _Optional[float] = ..., stamina_inc_max: _Optional[float] = ..., player_decay: _Optional[float] = ..., inertia_moment: _Optional[float] = ..., dash_power_rate: _Optional[float] = ..., player_size: _Optional[float] = ..., kickable_margin: _Optional[float] = ..., kick_rand: _Optional[float] = ..., extra_stamina: _Optional[float] = ..., effort_max: _Optional[float] = ..., effort_min: _Optional[float] = ..., kick_power_rate: _Optional[float] = ..., foul_detect_probability: _Optional[float] = ..., catchable_area_l_stretch: _Optional[float] = ..., unum_far_length: _Optional[float] = ..., unum_too_far_length: _Optional[float] = ..., team_far_length: _Optional[float] = ..., team_too_far_length: _Optional[float] = ..., player_max_observation_length: _Optional[float] = ..., ball_vel_far_length: _Optional[float] = ..., ball_vel_too_far_length: _Optional[float] = ..., ball_max_observation_length: _Optional[float] = ..., flag_chg_far_length: _Optional[float] = ..., flag_chg_too_far_length: _Optional[float] = ..., flag_max_observation_length: _Optional[float] = ..., kickable_area: _Optional[float] = ..., reliable_catchable_dist: _Optional[float] = ..., max_catchable_dist: _Optional[float] = ..., real_speed_max: _Optional[float] = ..., player_speed_max2: _Optional[float] = ..., real_speed_max2: _Optional[float] = ..., cycles_to_reach_max_speed: _Optional[int] = ...) -> None: ...

class Empty(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
