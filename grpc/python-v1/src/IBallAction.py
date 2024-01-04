from abc import ABC, abstractmethod
from typing import Any
from pyrusgeom.soccer_math import *
from pyrusgeom.geom_2d import *
from enum import Enum
from src.IAgent import IAgent
import service_pb2 as pb2
import pyrusgeom.soccer_math as smath
from src.Tools import Tools

    
class ActionType(Enum):
    DRIBBLE = "dribble"
    SHOOT = "shoot"
    DIRECT_PASS = "direct_pass"
    LEAD_PASS = "lead_pass"
    THROUGH_PASS = "through_pass"


class BallAction(ABC):
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
        self.success = False
    
    def evaluate(self) -> float:
        self.score = self.targetBallPos.x()
        goal_dist = math.sqrt(pow(abs(self.targetBallPos.x() - 52.5), 2) + pow(abs(self.targetBallPos.y()), 2))
        if goal_dist < 40.0:
            self.score += (40.0 - goal_dist)
    
    def check_possibility(self, agent: Any) -> None:
        pass
    
    def __str__(self) -> str:
        return f"ActionType: {self.actionType}, score: {self.score}, targetBallPos: {self.targetBallPos}, firstVelocity: {self.firstVelocity}, targetVelocity: {self.targetVelocity}, targetDirection: {self.targetDirection}, success: {self.success}"
    
    def __repr__(self) -> str:
        return f"ActionType: {self.actionType}, score: {self.score}, targetBallPos: {self.targetBallPos}, firstVelocity: {self.firstVelocity}, targetVelocity: {self.targetVelocity}, targetDirection: {self.targetDirection}, success: {self.success}"
    
    
class PassAction(BallAction):
    def __init__(self) -> None:
        super().__init__()
        
    def check_possibility(self, agent: IAgent) -> None:
        if self.actionType == ActionType.DIRECT_PASS:
            self.check_direct_pass(agent)
        else:
            self.check_lead_pass(agent)
            
    def check_direct_pass(self, agent: IAgent) -> None:
        tm = agent.wm.our_players_dict[self.targetUnum]
        sp = agent.serverParams
        player_type: pb2.PlayerType = agent.get_type(tm.type_id)
        min_receive_step = 3
        max_direct_pass_dist = 0.8 * smath.inertia_final_distance(sp.ball_speed_max, sp.ball_decay)
        max_receive_ball_speed = sp.ball_speed_max * pow(sp.ball_decay, min_receive_step)
        min_direct_pass_dist = player_type.kickable_area * 2.2
        tm_vel = Vector2D(tm.velocity.x, tm.velocity.y)
        ball_pos = Vector2D(agent.wm.ball.position.x, agent.wm.ball.position.y)
        if self.targetBallPos.x() > sp.pitch_half_length - 1.5 \
                or self.targetBallPos.x() < -sp.pitch_half_length + 5.0 \
                or self.targetBallPos.abs_y() > sp.pitch_half_width - 1.5:
            if agent.debug_mode:
                agent.add_log_text(pb2.LoggerLevel.PASS, f"## FAILED tm_pos is out of field")
            return
        # TODO sp.ourTeamGoalPos()
        if self.targetBallPos.x() < agent.wm.ball.position.x + 1.0 \
                and self.targetBallPos.dist(Vector2D(-52.5, 0)) < 18.0:
            if agent.debug_mode:
                agent.add_log_text(pb2.LoggerLevel.PASS, f"## FAILED tm_pos is near our goal")
            return

        max_ball_speed = agent.wm.self.kick_rate * sp.max_power
        if agent.wm.game_mode_type == pb2.GameModeType.PlayOn:
            max_ball_speed = sp.ball_speed_max

        # TODO SP.defaultRealSpeedMax()
        min_ball_speed = 1.0

        receive_point = Tools.inertia_final_point(player_type, self.targetBallPos, tm_vel)
        ball_move_dist = ball_pos.dist(receive_point)

        if ball_move_dist < min_direct_pass_dist or max_direct_pass_dist < ball_move_dist:
            if agent.debug_mode:
                agent.add_log_text(pb2.LoggerLevel.PASS, f"## FAILED ball_move_dist is out of range")
            return

        if agent.wm.game_mode_type == pb2.GameModeType.GoalKick_ \
                and receive_point.x() < sp.our_penalty_area_line_x + 1.0 \
                and receive_point.abs_y() < sp.penalty_area_half_width + 1.0:
            if agent.debug_mode:
                agent.add_log_text(pb2.LoggerLevel.PASS, f"## FAILED receive_point is in penalty area in goal kick mode")
            return

        max_receive_ball_speed = min(max_receive_ball_speed, player_type.kickable_area + (
                    sp.max_dash_power * player_type.dash_power_rate * player_type.effort_max) * 1.8)
        min_receive_ball_speed = player_type.real_speed_max

        ball_move_angle = (receive_point - ball_pos).th()

        min_ball_step = Tools.ball_move_step(sp.ball_speed_max, ball_move_dist, sp.ball_decay)
        # TODO Penalty step
        start_step = max(max(min_receive_step, min_ball_step), 0)
        max_step = start_step + 2
        if agent.debug_mode:
            agent.add_log_text(pb2.LoggerLevel.PASS, f">>>> DPass to {tm.uniform_number} ({round(tm_pos.x(), 2)}, {round(tm_pos.y(), 2)}) -> ({round(receive_point.x(), 2)}, {round(receive_point.y(), 2)}) start_step: {start_step}, max_step: {max_step}")

        self.create_pass(agent, tm, receive_point,
                    start_step, max_step, min_ball_speed,
                    max_ball_speed, min_receive_ball_speed,
                    max_receive_ball_speed, ball_move_dist,
                    ball_move_angle, "D")
    
    def check_lead_pass(self, agent: IAgent) -> None:
        tm = agent.wm.our_players_dict[self.targetUnum]
        sp = agent.serverParams
        our_goal_dist_thr2 = pow(16.0, 2)
        min_receive_step = 4
        max_receive_step = 20
        min_leading_pass_dist = 3.0
        max_leading_pass_dist = 0.8 * smath.inertia_final_distance(sp.ball_speed_max, sp.ball_decay)
        max_receive_ball_speed = sp.ball_speed_max * pow(sp.ball_decay, min_receive_step)

        max_player_distance = 35
        tm_pos = Vector2D(tm.position.x, tm.position.y)
        ball_pos = Vector2D(agent.wm.ball.position.x, agent.wm.ball.position.y)
        
        if tm_pos.dist(ball_pos) > max_player_distance:
            if agent.debug_mode:
                agent.add_log_text(pb2.LoggerLevel.PASS, f"## FAILED tm_pos is too far")
            return

        ptype = agent.get_type(tm.type_id)
        max_ball_speed = agent.wm.self.kick_rate * sp.max_power
        if agent.wm.game_mode_type == pb2.GameModeType.PlayOn:
            max_ball_speed = sp.ball_speed_max
        min_ball_speed = agent.get_type(0).real_speed_max

        max_receive_ball_speed = min(max_receive_ball_speed, ptype.kickable_area + (
                    sp.max_dash_power * ptype.dash_power_rate * ptype.effort_max) * 1.5)
        min_receive_ball_speed = 0.001

        our_goal = Vector2D(-52.5, 0)

        receive_point = self.targetBallPos

        move_dist_penalty_step = 0
        ball_move_line = Line2D(ball_pos, receive_point)
        player_line_dist = ball_move_line.dist(tm_pos)
        move_dist_penalty_step = int(player_line_dist * 0.3)
        if receive_point.x() > sp.pitch_half_length - 3.0 \
                or receive_point.x() < -sp.pitch_half_length + 5.0 \
                or receive_point.abs_y() > sp.pitch_half_width - 3.0:
            if agent.debug_mode:
                agent.add_log_text(pb2.LoggerLevel.PASS, f"## FAILED receive_point is out of field")
            return

        if receive_point.x() < ball_pos.x() \
                and receive_point.dist2(our_goal) < our_goal_dist_thr2:
            if agent.debug_mode:
                agent.add_log_text(pb2.LoggerLevel.PASS, f"## FAILED receive_point is near our goal")
            return

        if agent.wm.game_mode_type == pb2.GameModeType.GoalKick_ \
                and receive_point.x() < sp.our_penalty_area_line_x + 1.0 \
                and receive_point.abs_y() < sp.penalty_area_half_width + 1.0:
            if agent.debug_mode:
                agent.add_log_text(pb2.LoggerLevel.PASS, f"## FAILED receive_point is in penalty area in goal kick mode")
            return

        ball_move_dist = ball_pos.dist(receive_point)

        if ball_move_dist < min_leading_pass_dist or max_leading_pass_dist < ball_move_dist:
            if agent.debug_mode:
                agent.add_log_text(pb2.LoggerLevel.PASS, f"## FAILED ball_move_dist is out of range")
            return

        nearest_receiver = Tools.get_nearest_teammate(agent, receive_point)
        if nearest_receiver.uniform_number != tm.uniform_number:
            if agent.debug_mode:
                agent.add_log_text(pb2.LoggerLevel.PASS, f"## FAILED nearest_receiver is not tm")
            return

        receiver_step = self.predict_receiver_reach_step(agent, tm, receive_point, 'L') + move_dist_penalty_step
        ball_move_angle = (receive_point - ball_pos).th()

        min_ball_step = Tools.ball_move_step(sp.ball_speed_max, ball_move_dist, sp.ball_decay)

        start_step = max(max(min_receive_step, min_ball_step), receiver_step)
        # ifdef CREATE_SEVERAL_CANDIDATES_ON_SAME_POINT
        max_step = max(max_receive_step, start_step + 3)
        # else
        if agent.debug_mode:
            agent.add_log_text(pb2.LoggerLevel.PASS, f">>>> LPass to {tm.uniform_number} ({round(tm_pos.x(), 2)}, {round(tm_pos.y(), 2)}) -> ({round(receive_point.x(), 2)}, {round(receive_point.y(), 2)}) start_step: {start_step}, max_step: {max_step}")
        max_step = start_step + 3
        self.create_pass(agent, tm, receive_point,
                            start_step, max_step, min_ball_speed,
                            max_ball_speed, min_receive_ball_speed,
                            max_receive_ball_speed, ball_move_dist,
                            ball_move_angle, "L")
        
    def create_pass(self, agent: IAgent, receiver: pb2.Player, receive_point: Vector2D,
                    min_step, max_step, min_first_ball_speed, max_first_ball_speed,
                    min_receive_ball_speed, max_receive_ball_speed,
                    ball_move_dist, ball_move_angle: AngleDeg, description):
        sp = agent.serverParams
        ball_pos = Tools.vector2d_message_to_vector2d(agent.wm.ball.position)
        same_index = -1
        for step in range(min_step, max_step + 1):
            same_index += 1
            if agent.debug_mode:
                agent.add_log_text(pb2.LoggerLevel.PASS, f">>>>>> #{self.index} Pass to {receiver.uniform_number} ({round(receive_point.x(), 2)}, {round(receive_point.y(), 2)}), step:{step}")
            self.index += 1
            first_ball_speed = smath.calc_first_term_geom_series(ball_move_dist, sp.ball_decay, step)

            if first_ball_speed < min_first_ball_speed:
                if agent.debug_mode:
                    agent.add_log_text(pb2.LoggerLevel.PASS, f"###### FAILED to {receiver.uniform_number} step:{step} ball_speed:{first_ball_speed} ? first ball speed is low")
                # self.debug_list.append((self.index, receive_point, False, same_index))
                break

            if max_first_ball_speed < first_ball_speed:
                if agent.debug_mode:
                    agent.add_log_text(pb2.LoggerLevel.PASS, f"###### FAILED to {receiver.uniform_number} step:{step} ball_speed:{first_ball_speed} ? first ball speed is high")
                # self.debug_list.append((self.index, receive_point, False, same_index))
                continue

            receive_ball_speed = first_ball_speed * pow(sp.ball_decay, step)

            if receive_ball_speed < min_receive_ball_speed:
                if agent.debug_mode:
                    agent.add_log_text(pb2.LoggerLevel.PASS, f"###### FAILED to {receiver.uniform_number} step:{step} ball_speed:{first_ball_speed} rball_speed:{receive_ball_speed} ? receive ball speed is low")
                # self.debug_list.append((self.index, receive_point, False, same_index))
                break

            if max_receive_ball_speed < receive_ball_speed:
                if agent.debug_mode:
                    agent.add_log_text(pb2.LoggerLevel.PASS, f"###### FAILED to {receiver.uniform_number} step:{step} ball_speed:{first_ball_speed} rball_speed:{receive_ball_speed} ? receive ball speed is high")
                # self.debug_list.append((self.index, receive_point, False, same_index))
                continue

            kick_count = Tools.predict_kick_count(agent, agent.wm.self.uniform_number, first_ball_speed, ball_move_angle)

            o_step, o_unum, o_intercepted_pos = self.predict_opponents_reach_step(agent, ball_pos,
                                                                                  first_ball_speed, ball_move_angle,
                                                                                  receive_point, step + (kick_count - 1) + 5,
                                                                                  description)

            failed = False
            if description == 'T':
                if o_step <= step:
                    failed = True
            else:
                if o_step <= step + (kick_count - 1):
                    failed = True
            if failed:
                if agent.debug_mode:
                    agent.add_log_text(pb2.LoggerLevel.PASS, f"###### Failed to {receiver.uniform_number} step:{step} ball_speed:{first_ball_speed} rball_speed:{receive_ball_speed} opp {o_unum} step {o_step} max_step {max_step} ? opp reach step is low")
                # self.debug_list.append((self.index, receive_point, False, same_index))
                break
            if agent.debug_mode:
                agent.add_log_text(pb2.LoggerLevel.PASS, f"###### OK to {receiver.uniform_number} step:{step} ball_speed:{first_ball_speed} rball_speed:{receive_ball_speed} opp {o_unum} step {o_step}, max_step {max_step}")
            # self.debug_list.append((self.index, receive_point, True, same_index))
            
            self.initBallPos = ball_pos
            self.firstVelocity = Vector2D.polar2vector(first_ball_speed, ball_move_angle)
            self.success = True
            
            
            find_another_pass = False
            if not find_another_pass:
                break

            if o_step <= step + 3:
                break

            if min_step + 3 <= step:
                break

    def predict_receiver_reach_step(self, agent: IAgent, receiver: pb2.Player, pos: Vector2D, pass_type):
        ptype = agent.get_type(receiver.type_id)
        receiver_pos = Vector2D(receiver.position.x, receiver.position.y)
        receiver_vel = Vector2D(receiver.velocity.x, receiver.velocity.y)
        receiver_inertia_pos = receiver_pos + receiver_vel
        target_dist = receiver_inertia_pos.dist(pos)
        n_turn = 1 if receiver.body_direction_count > 0 else Tools.predict_player_turn_cycle(agent.serverParams, ptype, receiver.body_direction,
                                                                                             receiver_vel.r(), target_dist, 
                                                                                             (pos - receiver_inertia_pos).th(),
                                                                                             ptype.kickable_area, False)
        dash_dist = target_dist

        # if use_penalty:
        #     dash_dist += receiver.penalty_distance_;

        if pass_type == 'L':
            dash_dist *= 1.05

            dash_angle = (pos - receiver_pos).th()

            if dash_angle.abs() > 90.0 or receiver.body_direction_count > 1 or (dash_angle - AngleDeg(receiver.body_direction)).abs() > 30.0:
                n_turn += 1

        
        n_dash = Tools.cycles_to_reach_distance(dash_dist, ptype.real_speed_max)

        n_step = n_turn + n_dash if n_turn == 0 else n_turn + n_dash + 1
        return n_step
    
    def predict_opponents_reach_step(self, agent: IAgent, first_ball_pos: Vector2D, first_ball_speed,
                                     ball_move_angle: AngleDeg, receive_point: Vector2D, max_cycle, description):
        first_ball_vel = Vector2D.polar2vector(first_ball_speed, ball_move_angle)
        min_step = 1000
        min_opp = 0
        intercepted_pos = None
        for opp in agent.wm.opponents:
            if opp is None or opp.uniform_number == 0:
                continue
            step, intercepted_pos = Tools.predict_opponent_reach_step(agent, opp, first_ball_pos, first_ball_vel, ball_move_angle,
                                                                     receive_point, max_cycle, description)
            if agent.debug_mode:
                agent.add_log_text(pb2.LoggerLevel.PASS, f"------ Opp {opp.uniform_number} step {step} min_step {min_step} in {intercepted_pos}")
            if step < min_step:
                min_step = step
                min_opp = opp.uniform_number
        return min_step, min_opp, intercepted_pos