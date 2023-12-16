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

class Say(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

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
    __slots__ = ("unum",)
    UNUM_FIELD_NUMBER: _ClassVar[int]
    unum: int
    def __init__(self, unum: _Optional[int] = ...) -> None: ...

class AttentionToOf(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Log(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class DebugClient(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class Action(_message.Message):
    __slots__ = ("dash", "turn", "kick", "tackle", "catch", "move", "turn_neck", "change_view", "say", "point_to", "point_to_of", "attention_to", "attention_to_of", "log", "debug_client")
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
    def __init__(self, dash: _Optional[_Union[Dash, _Mapping]] = ..., turn: _Optional[_Union[Turn, _Mapping]] = ..., kick: _Optional[_Union[Kick, _Mapping]] = ..., tackle: _Optional[_Union[Tackle, _Mapping]] = ..., catch: _Optional[_Union[Catch, _Mapping]] = ..., move: _Optional[_Union[Move, _Mapping]] = ..., turn_neck: _Optional[_Union[TurnNeck, _Mapping]] = ..., change_view: _Optional[_Union[ChangeView, _Mapping]] = ..., say: _Optional[_Union[Say, _Mapping]] = ..., point_to: _Optional[_Union[PointTo, _Mapping]] = ..., point_to_of: _Optional[_Union[PointToOf, _Mapping]] = ..., attention_to: _Optional[_Union[AttentionTo, _Mapping]] = ..., attention_to_of: _Optional[_Union[AttentionToOf, _Mapping]] = ..., log: _Optional[_Union[Log, _Mapping]] = ..., debug_client: _Optional[_Union[DebugClient, _Mapping]] = ...) -> None: ...

class Actions(_message.Message):
    __slots__ = ("actions",)
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    actions: _containers.RepeatedCompositeFieldContainer[Action]
    def __init__(self, actions: _Optional[_Iterable[_Union[Action, _Mapping]]] = ...) -> None: ...
