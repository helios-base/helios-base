import service_pb2 as pb2
from src.IDecisionMaker import IDecisionMaker
from src.IAgent import IAgent


class SetPlayDecisionMaker(IDecisionMaker):
    def __init__(self):
        pass
    
    def makeDecision(self, agent: IAgent, wm: pb2.WorldModel):
        agent.addAction(pb2.Action(turn=pb2.Turn(relative_direction=30.0)))