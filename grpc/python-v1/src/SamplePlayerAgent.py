import service_pb2 as pb2
from src.DecisionMaker import DecisionMaker
from src.IAgent import IAgent
from src.FormationStrategy import FormationStrategy


class SamplePlayerAgent(IAgent):
    def __init__(self):
        self.actions: list[pb2.Action] = []
        self.decisionMaker = DecisionMaker()
        self.strategy = FormationStrategy()
    
    def getActions(self, wm:pb2.WorldModel) -> pb2.Actions:
        self.actions.clear()
        self.strategy.update(wm)
        self.decisionMaker.makeDecision(self, wm)
        actions = pb2.Actions()
        actions.actions.extend(self.actions)
        return actions
    
    def addAction(self, actions: pb2.Action):
        self.actions.append(actions)
        
    def getStrategy(self):
        return self.strategy
        
    
        
        