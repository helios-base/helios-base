import service_pb2 as pb2
from src.DecisionMaker import DecisionMaker
from src.IAgent import IAgent
from src.FormationStrategy import FormationStrategy


class SamplePlayerAgent(IAgent):
    def __init__(self):
        super().__init__()
        self.decisionMaker = DecisionMaker()
        self.strategy = FormationStrategy()
        self.serverParams: pb2.ServerParam = None
        self.playerParams: pb2.PlayerParam = None
        self.playerTypes: dict[pb2.PlayerType] = {}
        self.wm: pb2.WorldModel = None
    
    def getActions(self, wm:pb2.WorldModel) -> pb2.Actions:
        self.wm = wm
        self.actions.clear()
        self.strategy.update(wm)
        self.decisionMaker.makeDecision(self)
        actions = pb2.Actions()
        actions.actions.extend(self.actions)
        return actions
    
    def getStrategy(self):
        return self.strategy
        
    def setParams(self, params):
        if isinstance(params, pb2.ServerParam):
            self.serverParams = params
        elif isinstance(params, pb2.PlayerParam):
            self.playerParams = params
        elif isinstance(params, pb2.PlayerType):
            self.playerTypes[params.id] = params
        else:
            raise Exception("Unknown params type")