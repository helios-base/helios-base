from abc import ABC, abstractmethod
import service_pb2 as pb2
from pyrusgeom.soccer_math import *
from pyrusgeom.geom_2d import *


class IPositionStrategy(ABC):
    @abstractmethod
    def getPosition(self, uniform_number) -> Vector2D:
        pass
    
    @abstractmethod
    def update(self, wm: pb2.WorldModel):
        pass
    