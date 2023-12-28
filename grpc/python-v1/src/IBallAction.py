from abc import ABC, abstractmethod
from typing import Any
from pyrusgeom.soccer_math import *
from pyrusgeom.geom_2d import *
from enum import Enum

    
class ActionType(Enum):
    DRIBBLE = "dribble"
    SHOOT = "shoot"
    DIRECT_PASS = "direct_pass"
    LEAD_PASS = "lead_pass"
    THROUGH_PASS = "through_pass"


class IBallAction(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.index = 0
        self.actionType: ActionType = None
        self.initUnum = 0
        self.targetUnum = 0
        self.initBallPos: Vector2D = None
        self.targetBallPos: Vector2D = None
        self.firstVelocity: Vector2D = None
        self.targetVelocity: Vector2D = None
        self.targetDirection: AngleDeg = None
        self.score = 0.0
        self.initCycle = 0
        self.targetCycle = 0
        self.durations = 0
        self.success = False
        
    def evaluate(self) -> float:
        self.score = self.targetBallPos.x()
        goal_dist = self.targetBallPos.dist(Vector2D(52.5, 0.0))
        if goal_dist < 40.0:
            self.score += (40.0 - goal_dist)
            
    def __str__(self) -> str:
        return f"ActionType: {self.actionType}, score: {self.score}, targetBallPos: {self.targetBallPos}, firstVelocity: {self.firstVelocity}, targetVelocity: {self.targetVelocity}, targetDirection: {self.targetDirection}, initCycle: {self.initCycle}, targetCycle: {self.targetCycle}, durations: {self.durations}, success: {self.success}"
    
    def __repr__(self) -> str:
        return f"ActionType: {self.actionType}, score: {self.score}, targetBallPos: {self.targetBallPos}, firstVelocity: {self.firstVelocity}, targetVelocity: {self.targetVelocity}, targetDirection: {self.targetDirection}, initCycle: {self.initCycle}, targetCycle: {self.targetCycle}, durations: {self.durations}, success: {self.success}"