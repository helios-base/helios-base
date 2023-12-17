import service_pb2 as pb2
from src.IDecisionMaker import IDecisionMaker
from src.IAgent import IAgent
from pyrusgeom.soccer_math import *
from pyrusgeom.geom_2d import *

class NoBallDecisionMaker(IDecisionMaker):
    def __init__(self):
        pass
    
    def bodyGoToPoint(self, agent: IAgent, wm: pb2.WorldModel, pos: Vector2D):
        selfPos = Vector2D(wm.self.position.x, wm.self.position.y)
        body = AngleDeg(wm.self.body_direction)
        bodyDiff = ((pos - selfPos).th() - body).degree()
        if abs(bodyDiff) < 10:
            agent.addAction(pb2.Action(dash=pb2.Dash(power=100)))
        else:
            agent.addAction(pb2.Action(turn=pb2.Turn(relative_direction=bodyDiff)))
            
    def makeDecision(self, agent: IAgent, wm: pb2.WorldModel):
        teammate_reach_steps = wm.intercept_table.first_teammate_reach_steps
        self_reach_steps = wm.intercept_table.self_reach_steps
        our_reach_steps = min(teammate_reach_steps, self_reach_steps)
        opponent_reach_steps = wm.intercept_table.first_opponent_reach_steps
        if our_reach_steps < opponent_reach_steps and self_reach_steps < teammate_reach_steps:
            # Todo: call intercept
            intercept_info = wm.intercept_table.self_intercept_info
            pos = wm.ball.position
            if len(intercept_info) > 0:
                pos = intercept_info[0].final_self_position
            posVec = Vector2D(pos.x, pos.y)
            self.bodyGoToPoint(agent, wm, posVec)
        else:
            pos = agent.getStrategy().getPosition(wm.self.uniform_number)
            self.bodyGoToPoint(agent, wm, pos)
            if our_reach_steps < opponent_reach_steps:
                pass
            else:
                pass
                