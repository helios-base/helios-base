import service_pb2 as pb2
from src.IDecisionMaker import IDecisionMaker
from src.IAgent import IAgent
from pyrusgeom.soccer_math import *
from pyrusgeom.geom_2d import *


class NoBallDecisionMaker(IDecisionMaker):
    def __init__(self):
        pass
    
    def make_decision(self, agent: IAgent):
        teammate_reach_steps = agent.wm.intercept_table.first_teammate_reach_steps
        self_reach_steps = agent.wm.intercept_table.self_reach_steps
        our_reach_steps = min(teammate_reach_steps, self_reach_steps)
        opponent_reach_steps = agent.wm.intercept_table.first_opponent_reach_steps
        
        if our_reach_steps < opponent_reach_steps and self_reach_steps < teammate_reach_steps:
            agent.add_action(pb2.Action(body_intercept=pb2.Body_Intercept(save_recovery=False,
                                                                          face_point=pb2.Vector2D( x=agent.wm.ball.position.x,
                                                                       y=agent.wm.ball.position.y))))
            agent.add_action(pb2.Action(neck_turn_to_ball=pb2.Neck_TurnToBall()))
            return
        
        pos = agent.get_strategy().getPosition(agent.wm.self.uniform_number)
        agent.add_action(pb2.Action(body_go_to_point=pb2.Body_GoToPoint(target_point=pb2.Vector2D(x=pos.x(), y=pos.y()),
                                                                        distance_threshold=1,
                                                                        max_dash_power=100)))
        agent.add_action(pb2.Action(neck_turn_to_ball=pb2.Neck_TurnToBall()))
        if our_reach_steps < opponent_reach_steps:
            pass
        else:
            pass