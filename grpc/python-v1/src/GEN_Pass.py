from src.IBallActionGenerator import BallActionGenerator
from src.IAgent import IAgent
import service_pb2 as pb2
import pyrusgeom.soccer_math as smath
from pyrusgeom.soccer_math import *
from pyrusgeom.geom_2d import *
from src.Tools import Tools
from src.IBallAction import IBallAction, ActionType


class GeneratorPass(BallActionGenerator):
    def __init__(self):
        super().__init__()
        self.receivers: pb2.TeammateMessage = []
        self.index = 0
        
    def generate(self, agent: IAgent, init_index: int = 0):
        self.candidateActions = []
        self.receivers = []
        self.debug_list = []
        self.index = init_index
        self.update_receiver(agent)
        self.generate_pass(agent)
        self.log_debug(agent, pb2.LoggerLevel.PASS)
        return self.candidateActions
    
    def update_receiver(self, agent: IAgent):
        agent.add_log_text(pb2.LoggerLevel.PASS, "update_receiver")
        for tm in agent.wm.teammates:
            if tm.uniform_number == agent.wm.self.uniform_number:
                agent.add_log_text(pb2.LoggerLevel.PASS, "-- {tm.uniform_number} is me")
                continue
            if tm.uniform_number < 0:
                agent.add_log_text(pb2.LoggerLevel.PASS, "-- {tm.uniform_number} unum is less than 0")
                continue
            
            if tm.pos_count > 10:
                agent.add_log_text(pb2.LoggerLevel.PASS, "-- {tm.uniform_number} pos_count is more than 10")
                continue
            
            if tm.is_tackling:
                agent.add_log_text(pb2.LoggerLevel.PASS, "-- {tm.uniform_number} is tackling")
                continue
            
            if tm.position.x > agent.wm.offside_line_x:
                agent.add_log_text(pb2.LoggerLevel.PASS, "-- {tm.uniform_number} is offside")
                continue
            
            if tm.is_goalie and tm.position.x < -30: # todo server param ourPenaltyAreaLineX
                agent.add_log_text(pb2.LoggerLevel.PASS, "-- {tm.uniform_number} is goalie and in danger area")
                continue
            
            agent.add_log_text(pb2.LoggerLevel.PASS, "-- {tm.uniform_number} is ok")
            self.receivers.append(tm)
        
    def generate_pass(self, agent: IAgent):
        agent.add_log_text(pb2.LoggerLevel.PASS, "generate_pass")
        for tm in self.receivers:
            self.generate_direct_pass(agent, tm)
            
    def generate_direct_pass(self, agent: IAgent, tm: pb2.Player):
        agent.add_log_text(pb2.LoggerLevel.PASS, f"generate_direct_pass to {tm.uniform_number}")
        sp = agent.serverParams
        player_type: pb2.PlayerType = agent.playerTypes[tm.type_id]
        min_receive_step = 3
        max_direct_pass_dist = 0.8 * smath.inertia_final_distance(sp.ball_speed_max, sp.ball_decay)
        max_receive_ball_speed = sp.ball_speed_max * pow(sp.ball_decay, min_receive_step)
        min_direct_pass_dist = player_type.kickable_area * 2.2
        tm_pos = Vector2D(tm.position.x, tm.position.y)
        tm_vel = Vector2D(tm.velocity.x, tm.velocity.y)
        ball_pos = Vector2D(agent.wm.ball.position.x, agent.wm.ball.position.y)
        if tm_pos.x() > sp.pitch_half_length - 1.5 \
                or tm_pos.x() < -sp.pitch_half_length + 5.0 \
                or tm_pos.abs_y() > sp.pitch_half_width - 1.5:
            agent.add_log_text(pb2.LoggerLevel.PASS, f"tm_pos is out of field")
            return
        # TODO sp.ourTeamGoalPos()
        if tm_pos.x() < agent.wm.ball.position.x + 1.0 \
                and tm_pos.dist(Vector2D(-52.5, 0)) < 18.0:
            agent.add_log_text(pb2.LoggerLevel.PASS, f"tm_pos is near our goal")
            return

        max_ball_speed = agent.wm.self.kick_rate * sp.max_power
        if agent.wm.game_mode_type == pb2.GameModeType.PlayOn:
            max_ball_speed = sp.ball_speed_max

        # TODO SP.defaultRealSpeedMax()
        min_ball_speed = 1.0

        receive_point = Tools.inertia_final_point(player_type, tm_pos, tm_vel)
        ball_move_dist = ball_pos.dist(receive_point)

        if ball_move_dist < min_direct_pass_dist or max_direct_pass_dist < ball_move_dist:
            agent.add_log_text(pb2.LoggerLevel.PASS, f"ball_move_dist is out of range")
            return

        if agent.wm.game_mode_type in [pb2.GameModeType.GoalKick_Left, pb2.GameModeType.GoalKick_Right] \
                and receive_point.x() < sp.our_penalty_area_line_x + 1.0 \
                and receive_point.abs_y() < sp.penalty_area_half_width + 1.0:
            agent.add_log_text(pb2.LoggerLevel.PASS, f"receive_point is in penalty area in goal kick mode")
            return

        max_receive_ball_speed = min(max_receive_ball_speed, player_type.kickable_area + (
                    sp.max_dash_power * player_type.dash_power_rate * player_type.effort_max) * 1.8)
        min_receive_ball_speed = player_type.real_speed_max

        ball_move_angle = (receive_point - ball_pos).th()

        min_ball_step = Tools.ball_move_step(sp.ball_speed_max, ball_move_dist, sp.ball_decay)
        # TODO Penalty step
        start_step = max(max(min_receive_step, min_ball_step), 0)
        max_step = start_step + 2
        agent.add_log_text(pb2.LoggerLevel.PASS, f"#DPass to {tm.uniform_number} {tm_pos}->{receive_point} start_step: {start_step}, max_step: {max_step}")

        self.create_pass(agent, tm, receive_point,
                    start_step, max_step, min_ball_speed,
                    max_ball_speed, min_receive_ball_speed,
                    max_receive_ball_speed, ball_move_dist,
                    ball_move_angle, "D")
    
    def create_pass(self, agent: IAgent, receiver: pb2.Player, receive_point: Vector2D,
                    min_step, max_step, min_first_ball_speed, max_first_ball_speed,
                    min_receive_ball_speed, max_receive_ball_speed,
                    ball_move_dist, ball_move_angle: AngleDeg, description):
        sp = agent.serverParams
        ball_pos = Tools.vector2d_message_to_vector2d(agent.wm.ball.position)
        for step in range(min_step, max_step + 1):
            self.index += 1
            first_ball_speed = smath.calc_first_term_geom_series(ball_move_dist, sp.ball_decay, step)

            if first_ball_speed < min_first_ball_speed:
                agent.add_log_text(pb2.LoggerLevel.PASS, f"##Pass {self.index},to {receiver.uniform_number} {receive_point}, step:{step}, ball_speed:{first_ball_speed}, first ball speed is low")
                self.debug_list.append((self.index, receive_point, False))
                break

            if max_first_ball_speed < first_ball_speed:
                agent.add_log_text(pb2.LoggerLevel.PASS, f"##Pass {self.index},to {receiver.uniform_number} {receive_point}, step:{step}, ball_speed:{first_ball_speed}, first ball speed is high")
                self.debug_list.append((self.index, receive_point, False))
                continue

            receive_ball_speed = first_ball_speed * pow(sp.ball_decay, step)

            if receive_ball_speed < min_receive_ball_speed:
                agent.add_log_text(pb2.LoggerLevel.PASS, f"##Pass {self.index},to {receiver.uniform_number} {receive_point}, step:{step}, ball_speed:{first_ball_speed}, rball_speed:{receive_ball_speed}, receive ball speed is low")
                self.debug_list.append((self.index, receive_point, False))
                break

            if max_receive_ball_speed < receive_ball_speed:
                agent.add_log_text(pb2.LoggerLevel.PASS, f"##Pass {self.index},to {receiver.uniform_number} {receive_point}, step:{step}, ball_speed:{first_ball_speed}, rball_speed:{receive_ball_speed}, receive ball speed is high")
                self.debug_list.append((self.index, receive_point, False))
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
                agent.add_log_text(pb2.LoggerLevel.PASS, f"## Failed Pass {self.index},to {receiver.uniform_number} {receive_point}, step:{step}, ball_speed:{first_ball_speed}, rball_speed:{receive_ball_speed}, opp {o_unum} step {o_step}, max_step {max_step}")
                self.debug_list.append((self.index, receive_point, False))
                break
            agent.add_log_text(pb2.LoggerLevel.PASS, f"## OK Pass {self.index},to {receiver.uniform_number} {receive_point}, step:{step}, ball_speed:{first_ball_speed}, rball_speed:{receive_ball_speed}, opp {o_unum} step {o_step}, max_step {max_step}")
            self.debug_list.append((self.index, receive_point, True))
            
            candidate = IBallAction()
            candidate.actionType = ActionType.DIRECT_PASS
            candidate.initBallPos = ball_pos
            candidate.targetBallPos = receive_point
            candidate.targetUnum = receiver.uniform_number
            candidate.firstVelocity = Vector2D.polar2vector(first_ball_speed, ball_move_angle)
            candidate.evaluate()
            self.candidateActions.append(candidate)

            find_another_pass = False
            if not find_another_pass:
                break

            if o_step <= step + 3:
                break

            if min_step + 3 <= step:
                break

    def predict_opponents_reach_step(self, agent: IAgent, first_ball_pos: Vector2D, first_ball_speed,
                                     ball_move_angle: AngleDeg, receive_point: Vector2D, max_cycle, description):
        first_ball_vel = Vector2D.polar2vector(first_ball_speed, ball_move_angle)
        min_step = 1000
        min_opp = 0
        intercepted_pos = None
        for opp in agent.wm.opponents:
            if opp is None or opp.uniform_number == 0:
                continue
            step, intercepted_pos = self.predict_opponent_reach_step(agent, opp, first_ball_pos, first_ball_vel, ball_move_angle,
                                                                     receive_point, max_cycle, description)
            if step < min_step:
                min_step = step
                min_opp = opp.uniform_number
        return min_step, min_opp, intercepted_pos

    def predict_opponent_reach_step(self, agent: IAgent, opponent: pb2.Player, first_ball_pos: Vector2D, first_ball_vel: Vector2D,
                                    ball_move_angle: AngleDeg, receive_point: Vector2D, max_cycle, description):
        sp = agent.serverParams

        penalty_area = Rect2D(Vector2D(sp.their_penalty_area_line_x, -sp.penalty_area_half_width ),
                                Size2D(sp.penalty_area_length, sp.penalty_area_half_width * 2.0))
        CONTROL_AREA_BUF = 0.15

        opp_pos = Vector2D(opponent.position.x, opponent.position.y)
        opp_vel = Vector2D(opponent.velocity.x, opponent.velocity.y)
        ptype:pb2.PlayerType = agent.get_type(opponent.type_id)
        min_cycle = Tools.estimate_min_reach_cycle(opp_pos, ptype.real_speed_max, first_ball_pos,
                                                   ball_move_angle)

        if min_cycle < 0:
            return 1000, None

        for cycle in range(max(1, min_cycle), max_cycle + 1):
            ball_pos = smath.inertia_n_step_point(first_ball_pos, first_ball_vel, cycle, sp.ball_decay)
            control_area = sp.catchable_area if opponent.is_goalie and penalty_area.contains(ball_pos) else ptype.kickable_area

            inertia_pos = Tools.inertia_point(opp_pos, opp_vel, cycle, ptype.player_decay)
            target_dist = inertia_pos.dist(ball_pos)

            dash_dist = target_dist
            if description == 'T' \
                and first_ball_vel.x() > 2.\
                and ( receive_point.x() > agent.wm.offside_line_x or receive_point.x() > 30.):
                pass
            else:
                dash_dist -= Tools.estimate_virtual_dash_distance(opponent, ptype.real_speed_max)
            if dash_dist - control_area - CONTROL_AREA_BUF < 0.001:
                return cycle, ball_pos

            if description == 'T' \
                and first_ball_vel.x() > 2.\
                and ( receive_point.x() > agent.wm.offside_line_x or receive_point.x() > 30.):

                dash_dist -= control_area
            else:
                if receive_point.x() < 25.:
                    dash_dist -= control_area + 0.5
                else:
                    dash_dist -= control_area + 0.2

            if dash_dist > ptype.real_speed_max * (cycle + min(opponent.pos_count, 5)):
                continue

            n_dash = Tools.cycles_to_reach_distance(dash_dist, ptype.real_speed_max)
            if n_dash > cycle + opponent.pos_count:
                continue

            n_turn = 0
            if opponent.body_direction_count > 1:
                n_turn = Tools.predict_player_turn_cycle(sp, ptype, AngleDeg(opponent.body_direction), opp_vel.r(),
                                                         target_dist,
                                                         (ball_pos - inertia_pos).th(), control_area, True)

            n_step = n_turn + n_dash if n_turn == 0 else n_turn + n_dash + 1

            bonus_step = 0
            if opponent.is_tackling:
                bonus_step = -5
            if n_step - bonus_step <= cycle:
                return cycle, ball_pos
        return 1000, None

