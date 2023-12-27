from pyparsing import col
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
                
                target = Vector2D.polar2vector(dist, angle)
                target += Vector2D(teammate.position.x, teammate.position.y)
                
                the_pass = PassAction()
                the_pass.target = target
                the_pass.first_speed = self.getSpeed(agent, wm, the_pass)
                if self.checkPass(agent, wm, the_pass, teammate):
                    the_pass.value = self.evaluatePass(agent, wm, the_pass, teammate)
                    all_pass.append(the_pass)
                    self.debugPass(agent, the_pass, True)
                else:
                    self.debugPass(agent, the_pass, False)
        
        return all_pass
    
    def debugPass(self, agent: IAgent, the_pass: PassAction, is_valid: bool):
        agent.addAction(pb2.Action(
            log=pb2.Log(
                add_circle=pb2.AddCircle(
                    level=pb2.LoggerLevel.PASS,
                    center=pb2.Vector2D(x=the_pass.target.x(), y=the_pass.target.y()),
                    radius=0.2,
                    color="#00ff00" if is_valid else "#ff0000",
                    fill=False
                )
            )
        ))
    
    def evaluatePass(self, agent: IAgent, wm: pb2.WorldModel, the_pass: PassAction, teammate: pb2.Player):
        value = the_pass.target.x()
        return value
    
    def getSpeed(self, agent: IAgent, wm: pb2.WorldModel, the_pass: PassAction):
        move_dist = (Vector2D(wm.ball.position.x, wm.ball.position.y) - the_pass.target).r()
        speed = 0.7
        while move_dist > 0.1:
            move_dist -= speed
            speed /= 0.94
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
        ball_pos = Vector2D(wm.ball.position.x, wm.ball.position.y)
        ball_dir = (the_pass.target - ball_pos).th()
        ball_vel = Vector2D.polar2vector(the_pass.first_speed, ball_dir)
        opp_pos = Vector2D(opp.position.x, opp.position.y)
        
        ball_pos += ball_vel
        ball_vel *= 0.94
        
        cycle = 1
        while ball_pos.dist(the_pass.target) > 0.8 and cycle < 20:
            n_turn = 1
            n_dash = self.predictOppDash(ball_pos.dist(opp_pos))
            
            if n_dash + n_turn < cycle:
                return True
            
            cycle += 1
            ball_pos += ball_vel
            ball_vel *= 0.94
        return False

    def predictOppDash(self, dist: float):
        return dist / 0.7
    
    def doPass(self, agent: IAgent, wm: pb2.WorldModel):
        all_pass: list[PassAction] = []
        for tm in wm.teammates:
            if tm.uniform_number == wm.self.uniform_number:
                agent.addAction(pb2.Action(
                    log=pb2.Log(
                        add_text=pb2.AddText(
                            level=pb2.LoggerLevel.PASS,
                            message=f"Skip pass to myself, myUnum={wm.self.uniform_number}, tmUnum={tm.uniform_number}"
                        )
                    )
                ))
                continue
            
            new_pass = self.generate_direct_pass_to_teammate(agent, wm, tm)
            all_pass += new_pass
        
        if len(all_pass) == 0:
            return False

        all_pass.sort(key=lambda x: x.value, reverse=True)
        best_pass = all_pass[0]
        agent.addAction(pb2.Action(body_smart_kick=pb2.Body_SmartKick(target_point=pb2.Vector2D(x=best_pass.target.x(), y=best_pass.target.y()),
                                           first_speed=best_pass.first_speed,
                                           first_speed_threshold=0.3,
                                           max_steps=3)))
        
    
    def makeDecision(self, agent: IAgent, wm: pb2.WorldModel):
        if self.doPass(agent, wm):
            return
        # agent.addAction(pb2.Action(kick=pb2.Kick(power=100, relative_direction=30)))
        