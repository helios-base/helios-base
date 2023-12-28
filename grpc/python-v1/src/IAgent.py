from abc import ABC, abstractmethod
import service_pb2 as pb2
from src.IPositionStrategy import IPositionStrategy
from typing import Union


class IAgent(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.wm: Union[pb2.WorldModel, None] = None
        self.actions: list[pb2.Action] = []
        self.serverParams: Union[pb2.ServerParam, None] = None
        self.playerParams: Union[pb2.PlayerParam, None] = None
        self.playerTypes: Union[pb2.PlayerType, dict[pb2.PlayerType]] = {}

    def get_type(self, id: int) -> pb2.PlayerType:
        if id < 0:
            id = 0
        return self.playerTypes[id]
    
    @abstractmethod
    def get_actions(self, wm: pb2.WorldModel) -> pb2.Actions:
        pass

    @abstractmethod
    def get_strategy(self) -> IPositionStrategy:
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

    def add_log_text(self, level: pb2.LoggerLevel, message: str):
        self.add_action(pb2.Action(
            log=pb2.Log(
                add_text=pb2.AddText(
                    level=level,
                    message=message
                )
            )
        ))

    def add_log_message(self, level: pb2.LoggerLevel, message: str, x, y, color):
        self.add_action(pb2.Action(
            log=pb2.Log(
                add_message=pb2.AddMessage(
                    level=level,
                    message=message,
                    position=pb2.Vector2D(x=x, y=y),
                    color=color,
                )
            )
        ))

    def add_log_circle(self, level: pb2.LoggerLevel, center_x: float, center_y: float, radius: float, color: str,
                       fill: bool):
        self.add_action(pb2.Action(
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

    def add_action(self, actions: pb2.Action):
        self.actions.append(actions)
