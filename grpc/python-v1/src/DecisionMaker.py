import service_pb2 as pb2
from src.IDecisionMaker import IDecisionMaker
from src.DM_PlayOn import PlayOnDecisionMaker
from src.DM_SetPlay import SetPlayDecisionMaker
from src.IAgent import IAgent


class DecisionMaker(IDecisionMaker):
    def __init__(self):
        self.playOnDecisionMaker = PlayOnDecisionMaker()
        self.setPlayDecisionMaker = SetPlayDecisionMaker()
    
    def make_decision(self, agent: IAgent):
        if agent.wm.self.is_goalie:
            agent.add_action(pb2.Action(helios_goalie=pb2.HeliosGoalie()))
        else:
            if agent.wm.game_mode_type == pb2.GameModeType.PlayOn:
                self.playOnDecisionMaker.make_decision(agent)
            elif agent.wm.is_penalty_kick_mode:
                agent.add_action(pb2.Action(helios_penalty=pb2.HeliosPenalty()))
            else:
                agent.add_action(pb2.Action(helios_set_play=pb2.HeliosSetPlay()))