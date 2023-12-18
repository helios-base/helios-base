import service_pb2 as pb2
from src.IDecisionMaker import IDecisionMaker
from src.IAgent import IAgent
from pyrusgeom.soccer_math import *
from pyrusgeom.geom_2d import *

class PassAction:
    def __init__(self) -> None:
        self.target: Vector2D = Vector2D(0, 0)
        self.first_speed = 0
        self.value = 0

class WithBallDecisionMaker(IDecisionMaker):
    def __init__(self):
        pass
    
    def generate_direct_pass_to_teammate(self, agent: IAgent, wm: pb2.WorldModel, teammate: pb2.Player):
        angle_step = 6
        dist_step = 3
        
        all_pass: list[PassAction] = []
        for angle_index in range(angle_step):
            angle = AngleDeg(angle_index * 360 / angle_step)
            
            for dist_index in range(dist_step):
                dist = dist_index * 3 / dist_step
                
                target = Vector2D(r=dist, th=angle)
                target += Vector2D(wm.self.position.x, wm.self.position.y)
                
                the_pass = PassAction()
                the_pass.target = target
                the_pass.first_speed = self.getSpeed(agent, wm, the_pass)
                if self.checkPass(agent, wm, the_pass, teammate):
                    all_pass.append(self.evaluatePass(agent, wm, target, teammate))
        
        return all_pass
    
    def getSpeed(self, agent: IAgent, wm: pb2.WorldModel, the_pass: PassAction):
        move_dist = (Vector2D(wm.ball.position.x, wm.ball.position.y) - the_pass.target).r()
        speed = 0.7
        while move_dist > 0.1:
            move_dist -= speed
            speed *= 0.94
        return speed
    
    def checkPass(self, agent: IAgent, wm: pb2.WorldModel, the_pass: PassAction, teammate: pb2.Player):
        if the_pass.target.x() < -52 or the_pass.target.x() > 52:
            return False
        
        if the_pass.target.y() < -34 or the_pass.target.y() > 34:
            return False
        
        for opp in wm.opponents:
            if self.canOppIntercept(agent, wm, the_pass, opp):
                return False
        
        return True
    
    def canOppIntercept(self, agent: IAgent, wm: pb2.WorldModel, the_pass: PassAction, opp: pb2.Player):
        pass
        
    
    def doPass(self, agent: IAgent, wm: pb2.WorldModel):
        all_pass: list[PassAction] = []
        for tm in wm.teammates:
            if tm.uniform_number == wm.self.uniform_number:
                continue
            
            new_pass = self.generate_direct_pass_to_teammate(agent, wm, tm)
            all_pass += new_pass
        
        if len(all_pass) == 0:
            return False

        all_pass.sort(key=lambda x: x.value, reverse=True)
        best_pass = all_pass[0]
        pb2.Body_SmartKick(pb2.Vector2D(best_pass.target.x(), best_pass.target.y()), best_pass.first_speed, 0.3, 3)
        
    
    def makeDecision(self, agent: IAgent, wm: pb2.WorldModel):
        if self.doPass(agent, wm):
            return
        agent.addAction(pb2.Action(kick=pb2.Kick(power=100, relative_direction=30)))
        