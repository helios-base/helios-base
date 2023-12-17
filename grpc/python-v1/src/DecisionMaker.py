import service_pb2 as pb2
from src.IDecisionMaker import IDecisionMaker
from src.DM_PlayOn import PlayOnDecisionMaker
from src.DM_SetPlay import SetPlayDecisionMaker
from src.IAgent import IAgent


class DecisionMaker(IDecisionMaker):
    def __init__(self):
        self.playOnDecisionMaker = PlayOnDecisionMaker()
        self.setPlayDecisionMaker = SetPlayDecisionMaker()
    
    def makeDecision(self, agent: IAgent, wm: pb2.WorldModel):
        # if wm.game_mode_type == pb2.GameModeType.PlayOn:
        self.playOnDecisionMaker.makeDecision(agent, wm)
        # elif wm.is_our_set_play or wm.is_their_set_play:
        #     self.setPlayDecisionMaker.makeDecision(agent, wm)