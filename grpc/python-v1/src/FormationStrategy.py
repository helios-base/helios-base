import service_pb2 as pb2
from src.IPositionStrategy import IPositionStrategy
from src.delaunay_triangulation import *
from enum import Enum
from pyrusgeom.soccer_math import *

class Situation(Enum):
    OurSetPlay_Situation = 0,
    OppSetPlay_Situation = 1,
    Defense_Situation = 2,
    Offense_Situation = 3,
    PenaltyKick_Situation = 4

class FormationStrategy(IPositionStrategy):
    def __init__(self):
        self.before_kick_off_formation: Formation = Formation(f'src/formation_dt/before_kick_off.conf')
        self.defense_formation: Formation = Formation(f'src/formation_dt/defense_formation.conf')
        self.offense_formation: Formation = Formation(f'src/formation_dt/offense_formation.conf')
        self.goalie_kick_opp_formation: Formation = Formation(f'src/formation_dt/goalie_kick_opp_formation.conf')
        self.goalie_kick_our_formation: Formation = Formation(f'src/formation_dt/goalie_kick_our_formation.conf')
        self.kickin_our_formation: Formation = Formation(f'src/formation_dt/kickin_our_formation.conf')
        self.setplay_opp_formation: Formation = Formation(f'src/formation_dt/setplay_opp_formation.conf')
        self.setplay_our_formation: Formation = Formation(f'src/formation_dt/setplay_our_formation.conf')
        self._poses = [Vector2D(0, 0) for i in range(11)]
        self.current_situation = Situation.Offense_Situation
        self.current_formation = self.offense_formation

    def update(self, wm: pb2.WorldModel):
        tm_min = wm.intercept_table.first_teammate_reach_steps
        opp_min = wm.intercept_table.first_opponent_reach_steps
        self_min = wm.intercept_table.self_reach_steps
        all_min = min(tm_min, opp_min, self_min)
        current_ball_pos = Vector2D(wm.ball.position.x, wm.ball.position.y)
        current_ball_vel = Vector2D(wm.ball.velocity.x, wm.ball.velocity.y)
        ball_pos = inertia_n_step_point(current_ball_pos, current_ball_vel, all_min, 0.96) #todo use server param ball decay
        

        if True: #todo wm.game_mode().type() is GameModeType.PlayOn:
            thr = 0
            if ball_pos.x() > 0:
                thr += 1
            if wm.self.uniform_number > 6:
                thr += 1
            if min(tm_min, self_min) < opp_min + thr:
                self.current_situation = Situation.Offense_Situation
            else:
                self.current_situation = Situation.Defense_Situation
        else:
            pass
            # if wm.game_mode().is_penalty_kick_mode():
            #     self.current_situation = Situation.PenaltyKick_Situation
            # elif wm.game_mode().is_our_set_play(wm.our_side()):
            #     self.current_situation = Situation.OurSetPlay_Situation
            # else:
            #     self.current_situation = Situation.OppSetPlay_Situation

        if True: #ToDo wm.game_mode().type() is GameModeType.PlayOn:
            if self.current_situation is Situation.Offense_Situation:
                self.current_formation = self.offense_formation
            else:
                self.current_formation = self.defense_formation

        # elif wm.game_mode().type() in [GameModeType.BeforeKickOff, GameModeType.AfterGoal_Left,
        #                                GameModeType.AfterGoal_Right]:
        #     self.current_formation = self.before_kick_off_formation

        # elif wm.game_mode().type() in [GameModeType.GoalKick_Left, GameModeType.GoalKick_Right, GameModeType.GoalieCatchBall_Left, GameModeType.GoalieCatchBall_Right]: # Todo add Goal Catch!!
        #     if wm.game_mode().is_our_set_play(wm.our_side()):
        #         self.current_formation = self.goalie_kick_our_formation
        #     else:
        #         self.current_formation = self.goalie_kick_opp_formation

        # else:
        #     if wm.game_mode().is_our_set_play(wm.our_side()):
        #         if wm.game_mode().type() in [GameModeType.KickIn_Right, GameModeType.KickIn_Left,
        #                                      GameModeType.CornerKick_Right, GameModeType.CornerKick_Left]:
        #             self.current_formation = self.kickin_our_formation
        #         else:
        #             self.current_formation = self.setplay_our_formation
        #     else:
        #         self.current_formation = self.setplay_opp_formation

        self.current_formation.update(ball_pos)
        self._poses = self.current_formation.get_poses()

        # if self.current_formation is self.before_kick_off_formation or wm.game_mode().type() in \
        #         [GameModeType.KickOff_Left, GameModeType.KickOff_Right]:
        #     for pos in self._poses:
        #         pos._x = min(pos.x(), -0.5)
        # else:
        #     pass # Todo add offside line
        #     # for pos in self._poses:
        #     #     pos._x = math.min(pos.x(), )
    
    def getPosition(self, uniform_number):
        return self._poses[uniform_number - 1]