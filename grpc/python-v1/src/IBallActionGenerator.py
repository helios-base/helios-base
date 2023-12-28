from src.IBallAction import IBallAction
from src.IAgent import IAgent
import service_pb2 as pb2


class BallActionGenerator:
    def __init__(self):
        self.candidateActions: list[IBallAction] = []
        self.debug_list = []
        
    def log_debug(self, agent: IAgent, log_level:pb2.LoggerLevel):
        # (self.index, receive_point, False)
        for item in self.debug_list:
            agent.addLogCircle(log_level, item[1].x(), item[1].y(), 0.1, "blue" if item[2] else "red", False)
            agent.addLogMessage(log_level, f"{item[0]}", item[1].x() - 0.1, item[1].y() - 0.1, "blue" if item[2] else "red")
        