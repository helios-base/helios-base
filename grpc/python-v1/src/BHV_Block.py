import service_pb2 as pb2
from src.IDecisionMaker import IDecisionMaker
from src.IAgent import IAgent
from pyrusgeom.soccer_math import *
from pyrusgeom.geom_2d import *
from src.Tools import Tools
import pyrusgeom.soccer_math as smath


class BHV_Block:
    def __init__(self):
        pass
    
    def execute(self, agent: IAgent):
        if agent.wm.game_mode_type != pb2.GameModeType.PlayOn:
            return False
        teammate_reach_steps = agent.wm.intercept_table.first_teammate_reach_steps
        self_reach_steps = agent.wm.intercept_table.self_reach_steps
        our_reach_steps = min(teammate_reach_steps, self_reach_steps)
        opponent_reach_steps = agent.wm.intercept_table.first_opponent_reach_steps
        
        ball_pos = Vector2D(agent.wm.ball.position.x, agent.wm.ball.position.y)
        ball_vel = Vector2D(agent.wm.ball.velocity.x, agent.wm.ball.velocity.y)
        ball_pos = smath.inertia_n_step_point(ball_pos, ball_vel, opponent_reach_steps, agent.serverParams.ball_decay)
        
        dribble_speed_etimate = 0.7
        dribble_angle_estimate = (Vector2D(-52.0, 0) - ball_pos).th()
        blocker = 0
        block_cycle = 1000
        block_pos = Vector2D(0, 0)
        for unum in range(1, 12):
            if unum not in agent.wm.our_players_dict.keys():
                continue
            tm = agent.wm.our_players_dict[unum]
            tm_pos = Vector2D(tm.position.x, tm.position.y)
            tm_vel = Vector2D(tm.velocity.x, tm.velocity.y)
            tm_inertia_pos = smath.inertia_n_step_point(tm_pos, tm_vel, opponent_reach_steps, agent.serverParams.player_decay)
            if tm.uniform_number < 1:
                continue
            for c in range(1, 40):
                dribble_pos = ball_pos + Vector2D.polar2vector(c * dribble_speed_etimate, dribble_angle_estimate)
                turn_cycle = Tools.predict_player_turn_cycle(agent.serverParams, agent.get_type(tm.type_id), AngleDeg(tm.body_direction), tm_vel.r(), tm_pos.dist(dribble_pos), (dribble_pos - tm_pos).th(), 0.2, False)
                
                tm_cycle = Tools.cycles_to_reach_distance(tm_inertia_pos.dist(dribble_pos), agent.get_type(tm.type_id)) + turn_cycle
                if tm_cycle <= opponent_reach_steps + c:
                    if tm_cycle < block_cycle:
                        block_cycle = tm_cycle
                        blocker = unum
                        block_pos = dribble_pos
                        break
        if blocker == agent.wm.self.uniform_number:
            agent.add_action(pb2.Action(body_go_to_point=pb2.Body_GoToPoint(target_point=pb2.Vector2D(x=block_pos.x(), y=block_pos.y()), distance_threshold=0.5, max_dash_power=100)))
            agent.add_action(pb2.Action(neck_turn_to_ball=pb2.Neck_TurnToBall()))
            agent.add_action(pb2.Action(debug_client=pb2.DebugClient(message=f"blocker: {blocker}")))
            return True
        return False
