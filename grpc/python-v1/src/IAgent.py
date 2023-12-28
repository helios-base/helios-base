from abc import ABC, abstractmethod
import service_pb2 as pb2
from src.IPositionStrategy import IPositionStrategy

class IAgent(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.wm: pb2.WorldModel = None
        self.actions: list[pb2.Action] = []
        self.serverParams: pb2.ServerParam = None
        self.playerParams: pb2.PlayerParam = None
        self.playerTypes: dict[pb2.PlayerType] = {}
        
    @abstractmethod
    def getActions(self, wm:pb2.WorldModel) -> pb2.Actions:
        pass
    
    @abstractmethod
    def addAction(self, actions:pb2.Action):
        pass

    @abstractmethod
    def getStrategy(self) -> IPositionStrategy:
        pass
    
#     message Log {
#   oneof log {
#     AddText add_text = 1;
#     AddPoint add_point = 2;
#     AddLine add_line = 3;
#     AddArc add_arc = 4;
#     AddCircle add_circle = 5;
#     AddTriangle add_triangle = 6;
#     AddRectangle add_rectangle = 7;
#     AddSector add_sector = 8;
#     AddMessage add_message = 9;
#   }
# }

    def addLogText(self, level:pb2.LoggerLevel, message:str):
        self.addAction(pb2.Action(
            log=pb2.Log(
                add_text=pb2.AddText(
                    level=level,
                    message=message
                )
            )
        ))
    
    def addLogMessage(self, level:pb2.LoggerLevel, message:str, x, y, color):
        self.addAction(pb2.Action(
            log=pb2.Log(
                add_message=pb2.AddMessage(
                    level=level,
                    message=message,
                    position=pb2.Vector2D(x=x, y=y),
                    color=color,
                )
            )
        ))
        
    def addLogCircle(self, level:pb2.LoggerLevel, center_x:float, center_y:float, radius:float, color:str, fill:bool):
        self.addAction(pb2.Action(
            log=pb2.Log(
                add_circle=pb2.AddCircle(
                    level=level,
                    center=pb2.Vector2D(x=center_x, y=center_y),
                    radius=radius,
                    color=color,
                    fill=fill
                )
            )
        ))
        
    def addAction(self, actions: pb2.Action):
        self.actions.append(actions)