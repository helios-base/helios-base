from abc import ABC, abstractmethod
import service_pb2 as pb2
from src.IAgent import IAgent

class IDecisionMaker(ABC):
    @abstractmethod
    def makeDecision(self, agent: IAgent):
        pass
