# from pyparsing import col
import service_pb2 as pb2
from src.IDecisionMaker import IDecisionMaker
from src.IAgent import IAgent
from pyrusgeom.soccer_math import *
from pyrusgeom.geom_2d import *
from src.GEN_Pass import GeneratorPass
from src.IBallAction import BallAction
import time

class WithBallDecisionMaker(IDecisionMaker):
    def __init__(self):
        self.pass_generator = GeneratorPass()
        pass
    
    sum_time = 0
    count = 0
    def make_decision(self, agent: IAgent):
        start_time = time.time()
        candidate_actions: list[BallAction] = self.pass_generator.generate(agent, 0)

        if len(candidate_actions) == 0:
            agent.add_action(pb2.Action(body_hold_ball=pb2.Body_HoldBall()))
            return

        if agent.debug_mode:
            agent.add_log_text(pb2.LoggerLevel.PASS, f"candidate_actions: {candidate_actions}")
        candidate_actions.sort(key=lambda x: x.score, reverse=True)

        best_action = None
        i = 0
        best_score = -1000000
        for candidate in candidate_actions:
            candidate.check_possibility(agent)
            i += 1
            if candidate.success:
                if candidate.score > best_score:
                    best_score = candidate.score
                    best_action = candidate
                    break        
        end_time = time.time()
        WithBallDecisionMaker.sum_time += end_time - start_time
        WithBallDecisionMaker.count += 1
        print(f"{agent.wm.cycle} {i} {len(candidate_actions)} {float(i) / len(candidate_actions)} {candidate.score} {end_time - start_time} {WithBallDecisionMaker.sum_time / WithBallDecisionMaker.count}")
        if best_action is None:
            agent.add_action(pb2.Action(body_hold_ball=pb2.Body_HoldBall()))
            return
        
        agent.add_action(pb2.Action(body_smart_kick=pb2.Body_SmartKick(
            target_point=pb2.Vector2D(x=best_action.targetBallPos.x(), y=best_action.targetBallPos.y()),
            first_speed=best_action.firstVelocity.r(),
            first_speed_threshold=0.0,
            max_steps=3)))
