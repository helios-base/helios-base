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
    KickOff_Left: _ClassVar[GameModeType]
    KickOff_Right: _ClassVar[GameModeType]
    KickIn_Left: _ClassVar[GameModeType]
    KickIn_Right: _ClassVar[GameModeType]
    FreeKick_Left: _ClassVar[GameModeType]
    FreeKick_Right: _ClassVar[GameModeType]
    CornerKick_Left: _ClassVar[GameModeType]
    CornerKick_Right: _ClassVar[GameModeType]
    GoalKick_Left: _ClassVar[GameModeType]
    GoalKick_Right: _ClassVar[GameModeType]
    AfterGoal_Left: _ClassVar[GameModeType]
    AfterGoal_Right: _ClassVar[GameModeType]
    OffSide_Left: _ClassVar[GameModeType]
    OffSide_Right: _ClassVar[GameModeType]
    PenaltyKick_Left: _ClassVar[GameModeType]
    PenaltyKick_Right: _ClassVar[GameModeType]
    FirstHalfOver: _ClassVar[GameModeType]
    Pause: _ClassVar[GameModeType]
    Human: _ClassVar[GameModeType]
    FoulCharge_Left: _ClassVar[GameModeType]
    FoulCharge_Right: _ClassVar[GameModeType]
    FoulPush_Left: _ClassVar[GameModeType]
    FoulPush_Right: _ClassVar[GameModeType]
    FoulMultipleAttacker_Left: _ClassVar[GameModeType]
    FoulMultipleAttacker_Right: _ClassVar[GameModeType]
    FoulBallOut_Left: _ClassVar[GameModeType]
    FoulBallOut_Right: _ClassVar[GameModeType]
    BackPass_Left: _ClassVar[GameModeType]
    BackPass_Right: _ClassVar[GameModeType]
    FreeKickFault_Left: _ClassVar[GameModeType]
    FreeKickFault_Right: _ClassVar[GameModeType]
    CatchFault_Left: _ClassVar[GameModeType]
    CatchFault_Right: _ClassVar[GameModeType]
    IndFreeKick_Left: _ClassVar[GameModeType]
    IndFreeKick_Right: _ClassVar[GameModeType]
    PenaltySetup_Left: _ClassVar[GameModeType]
    PenaltySetup_Right: _ClassVar[GameModeType]
    PenaltyReady_Left: _ClassVar[GameModeType]
    PenaltyReady_Right: _ClassVar[GameModeType]
    PenaltyTaken_Left: _ClassVar[GameModeType]
    PenaltyTaken_Right: _ClassVar[GameModeType]
    PenaltyMiss_Left: _ClassVar[GameModeType]
    PenaltyMiss_Right: _ClassVar[GameModeType]
    PenaltyScore_Left: _ClassVar[GameModeType]
    PenaltyScore_Right: _ClassVar[GameModeType]
    IllegalDefense_Left: _ClassVar[GameModeType]
    IllegalDefense_Right: _ClassVar[GameModeType]
    PenaltyOnfield: _ClassVar[GameModeType]
    PenaltyFoul: _ClassVar[GameModeType]
    GoalieCatch_Left: _ClassVar[GameModeType]
    GoalieCatch_Right: _ClassVar[GameModeType]
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
KickOff_Left: GameModeType
KickOff_Right: GameModeType
KickIn_Left: GameModeType
KickIn_Right: GameModeType
FreeKick_Left: GameModeType
FreeKick_Right: GameModeType
CornerKick_Left: GameModeType
CornerKick_Right: GameModeType
GoalKick_Left: GameModeType
GoalKick_Right: GameModeType
AfterGoal_Left: GameModeType
AfterGoal_Right: GameModeType
OffSide_Left: GameModeType
OffSide_Right: GameModeType
PenaltyKick_Left: GameModeType
PenaltyKick_Right: GameModeType
FirstHalfOver: GameModeType
Pause: GameModeType
Human: GameModeType
FoulCharge_Left: GameModeType
FoulCharge_Right: GameModeType
FoulPush_Left: GameModeType
FoulPush_Right: GameModeType
FoulMultipleAttacker_Left: GameModeType
FoulMultipleAttacker_Right: GameModeType
FoulBallOut_Left: GameModeType
FoulBallOut_Right: GameModeType
BackPass_Left: GameModeType
BackPass_Right: GameModeType
FreeKickFault_Left: GameModeType
FreeKickFault_Right: GameModeType
CatchFault_Left: GameModeType
CatchFault_Right: GameModeType
IndFreeKick_Left: GameModeType
IndFreeKick_Right: GameModeType
PenaltySetup_Left: GameModeType
PenaltySetup_Right: GameModeType
PenaltyReady_Left: GameModeType
PenaltyReady_Right: GameModeType
PenaltyTaken_Left: GameModeType
PenaltyTaken_Right: GameModeType
PenaltyMiss_Left: GameModeType
PenaltyMiss_Right: GameModeType
PenaltyScore_Left: GameModeType
PenaltyScore_Right: GameModeType
IllegalDefense_Left: GameModeType
IllegalDefense_Right: GameModeType
PenaltyOnfield: GameModeType
PenaltyFoul: GameModeType
GoalieCatch_Left: GameModeType
GoalieCatch_Right: GameModeType
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
    __slots__ = ("position", "seen_position", "heard_position", "velocity", "seen_velocity", "pos_count", "seen_pos_count", "heard_pos_count", "vel_count", "seen_vel_count", "ghost_count", "dist_from_self", "angle_from_self", "id", "side", "uniform_number", "uniform_number_count", "is_goalie", "body_direction", "body_direction_count", "face_direction", "face_direction_count", "point_to_direction", "point_to_direction_count", "is_kicking", "dist_from_ball", "angle_from_ball", "ball_reach_steps", "is_tackling")
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
    def __init__(self, position: _Optional[_Union[Vector2D, _Mapping]] = ..., seen_position: _Optional[_Union[Vector2D, _Mapping]] = ..., heard_position: _Optional[_Union[Vector2D, _Mapping]] = ..., velocity: _Optional[_Union[Vector2D, _Mapping]] = ..., seen_velocity: _Optional[_Union[Vector2D, _Mapping]] = ..., pos_count: _Optional[int] = ..., seen_pos_count: _Optional[int] = ..., heard_pos_count: _Optional[int] = ..., vel_count: _Optional[int] = ..., seen_vel_count: _Optional[int] = ..., ghost_count: _Optional[int] = ..., dist_from_self: _Optional[float] = ..., angle_from_self: _Optional[float] = ..., id: _Optional[int] = ..., side: _Optional[_Union[Side, str]] = ..., uniform_number: _Optional[int] = ..., uniform_number_count: _Optional[int] = ..., is_goalie: bool = ..., body_direction: _Optional[float] = ..., body_direction_count: _Optional[int] = ..., face_direction: _Optional[float] = ..., face_direction_count: _Optional[int] = ..., point_to_direction: _Optional[float] = ..., point_to_direction_count: _Optional[int] = ..., is_kicking: bool = ..., dist_from_ball: _Optional[float] = ..., angle_from_ball: _Optional[float] = ..., ball_reach_steps: _Optional[int] = ..., is_tackling: bool = ...) -> None: ...

class Self(_message.Message):
    __slots__ = ("position", "seen_position", "heard_position", "velocity", "seen_velocity", "pos_count", "seen_pos_count", "heard_pos_count", "vel_count", "seen_vel_count", "ghost_count", "id", "side", "uniform_number", "uniform_number_count", "is_goalie", "body_direction", "body_direction_count", "face_direction", "face_direction_count", "point_to_direction", "point_to_direction_count", "is_kicking", "dist_from_ball", "angle_from_ball", "ball_reach_steps", "is_tackling", "relative_neck_direction", "stamina", "is_kickable", "catch_probability", "tackle_probability", "foul_probability", "view_width")
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
    def __init__(self, position: _Optional[_Union[Vector2D, _Mapping]] = ..., seen_position: _Optional[_Union[Vector2D, _Mapping]] = ..., heard_position: _Optional[_Union[Vector2D, _Mapping]] = ..., velocity: _Optional[_Union[Vector2D, _Mapping]] = ..., seen_velocity: _Optional[_Union[Vector2D, _Mapping]] = ..., pos_count: _Optional[int] = ..., seen_pos_count: _Optional[int] = ..., heard_pos_count: _Optional[int] = ..., vel_count: _Optional[int] = ..., seen_vel_count: _Optional[int] = ..., ghost_count: _Optional[int] = ..., id: _Optional[int] = ..., side: _Optional[_Union[Side, str]] = ..., uniform_number: _Optional[int] = ..., uniform_number_count: _Optional[int] = ..., is_goalie: bool = ..., body_direction: _Optional[float] = ..., body_direction_count: _Optional[int] = ..., face_direction: _Optional[float] = ..., face_direction_count: _Optional[int] = ..., point_to_direction: _Optional[float] = ..., point_to_direction_count: _Optional[int] = ..., is_kicking: bool = ..., dist_from_ball: _Optional[float] = ..., angle_from_ball: _Optional[float] = ..., ball_reach_steps: _Optional[int] = ..., is_tackling: bool = ..., relative_neck_direction: _Optional[float] = ..., stamina: _Optional[float] = ..., is_kickable: bool = ..., catch_probability: _Optional[float] = ..., tackle_probability: _Optional[float] = ..., foul_probability: _Optional[float] = ..., view_width: _Optional[_Union[ViewWidth, str]] = ...) -> None: ...

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
