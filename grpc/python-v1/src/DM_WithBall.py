# from pyparsing import col
import service_pb2 as pb2
from src.IDecisionMaker import IDecisionMaker
from src.IAgent import IAgent
from pyrusgeom.soccer_math import *
from pyrusgeom.geom_2d import *
from src.GEN_Pass import GeneratorPass

class WithBallDecisionMaker(IDecisionMaker):
    def __init__(self):
        self.pass_generator = GeneratorPass()
        pass
    
    def makeDecision(self, agent: IAgent):
        candidateActions = self.pass_generator.generate(agent, 0)
        
        if len(candidateActions) == 0:
            return
        
        agent.addLogText(pb2.LoggerLevel.PASS, f"candidateActions: {candidateActions}")
        candidateActions.sort(key=lambda x: x.score, reverse=True)
        bestAction = candidateActions[0]
        
        agent.addAction(pb2.Action(body_smart_kick=pb2.Body_SmartKick(
            target_point=pb2.Vector2D(x=bestAction.targetBallPos.x(), y=bestAction.targetBallPos.y()),
            first_speed=bestAction.firstVelocity.r(),
            first_speed_threshold=0.0,
            max_steps=bestAction.targetCycle)))         
           