from abc import ABC, abstractmethod
import service_pb2 as pb2
from src.IPositionStrategy import IPositionStrategy

class IAgent(ABC):
    @abstractmethod
    def getActions(self, wm:pb2.WorldModel) -> pb2.Actions:
        pass
    
    @abstractmethod
    def addAction(self, actions:pb2.Action):
        pass

    @abstractmethod
    def getStrategy(self) -> IPositionStrategy:
        pass