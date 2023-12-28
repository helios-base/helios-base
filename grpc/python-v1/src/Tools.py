import service_pb2 as pb2
import pyrusgeom.soccer_math as smath
from pyrusgeom.soccer_math import *
from pyrusgeom.geom_2d import *
from src.IAgent import IAgent
import math

class Tools:
    @staticmethod
    def inertia_final_point(playerType: pb2.PlayerType, position: Vector2D, velocity: Vector2D) -> Vector2D:
        return smath.inertia_final_point(position, velocity, playerType.player_decay)
        
    @staticmethod
    def ball_move_step(first_ball_speed, ball_move_dist, ball_decay):
        return int(math.ceil(calc_length_geom_series(first_ball_speed, ball_move_dist, ball_decay)) + 1.0e-10)
    
    @staticmethod
    def first_ball_speed(ball_move_dist: float, total_step: int, ball_decay: float):
        return calc_first_term_geom_series(ball_move_dist, ball_decay, total_step)
        
    @staticmethod
    def predict_kick_count(agent: IAgent, kicker_uniform_number, first_ball_speed, ball_move_angle: AngleDeg):
        if agent.wm.game_mode_type not in [pb2.GameModeType.PlayOn, pb2.GameModeType.PenaltyKick_Left, pb2.GameModeType.PenaltyKick_Right]:
            return 1

        if kicker_uniform_number == agent.wm.self.uniform_number and agent.wm.self.is_kickable:
            max_vel = Tools.calc_max_velocity(ball_move_angle, agent.wm.self.kick_rate, Tools.vector2d_message_to_vector2d(agent.wm.ball.velocity), agent.serverParams)
            if max_vel.r() >= first_ball_speed:
                return 1
        if first_ball_speed > 2.5:
            return 3
        elif first_ball_speed > 1.5:
            return 2
        return 1
    
    @staticmethod
    def calc_max_velocity(target_angle: AngleDeg,
                      krate,
                      ball_vel: Vector2D,
                      sp: pb2.ServerParam):
        ball_speed_max2 = sp.ball_speed_max ** 2
        max_accel = min(sp.max_power * krate,
                        sp.ball_accel_max)

        desired_ray = Ray2D(Vector2D(0.0, 0.0), target_angle)
        next_reachable_circle = Circle2D(ball_vel, max_accel)

        num = next_reachable_circle.intersection(desired_ray)
        if len(num) == 0:
            return Vector2D(0.0, 0.0)
        
        vel1 = num[0]
        
        if len(num) == 1:
            if vel1.r2() > ball_speed_max2:
                # next inertia ball point is within reachable circle.
                if next_reachable_circle.contains(Vector2D(0.0, 0.0)):
                    # can adjust angle at least
                    vel1.set_length(sp.ball_speed_max)

                else:
                    # failed
                    vel1.assign(0.0, 0.0)

            return vel1

        vel2 = num[1]
        #
        # num == 2
        #   ball reachable circle does not contain the current ball pos.

        length1 = vel1.r2()
        length2 = vel2.r2()

        if length1 < length2:
            vel1, vel2 = vel2, vel1
            length1, length2 = length2, length1

        if length1 > ball_speed_max2:
            if length2 > ball_speed_max2:
                # failed
                vel1.assign(0.0, 0.0)

            else:
                vel1.set_length(sp.ball_speed_max)

        return vel1
    
    @staticmethod
    def estimate_min_reach_cycle(player_pos: Vector2D, player_speed_max, target_first_point: Vector2D, target_move_angle: AngleDeg):
        target_to_player: Vector2D = (player_pos - target_first_point).rotated_vector(-target_move_angle)
        if target_to_player.x() < -1.0:
            return -1
        else:
            return max( 1, int(target_to_player.abs_y() / player_speed_max))
    
    @staticmethod    
    def inertia_point(initial_pos: Vector2D, initial_vel: Vector2D, n_step: int, player_decay: float):
        return smath.inertia_n_step_point(initial_pos, initial_vel, n_step, player_decay)
    
    @staticmethod
    def vector2d_message_to_vector2d(v: pb2.Vector2D):
        return Vector2D(v.x, v.y)
    
    @staticmethod
    def estimate_virtual_dash_distance(player: pb2.Player, real_speed_max: float):
        pos_count = min(10, player.pos_count, player.seen_pos_count)
        max_speed = real_speed_max * 0.8

        d = 0.
        for i in range(pos_count):
            d += max_speed * math.exp(-(i**2)/15)

        return d
    
    @staticmethod
    def cycles_to_reach_distance(dash_dist, real_speed_max):
        if dash_dist <= 0.001:
            return 0
        return int(math.ceil(dash_dist / real_speed_max))
        # todo: implement this
        # ddc = 0
        # for dd in self._dash_distance_table:
        #     if dash_dist <= dd:
        #         return ddc
        #     ddc += 1

        # cycle = len(self._dash_distance_table)
        # rest_dist = dash_dist - self._dash_distance_table[cycle - 1]
        # cycle += int(math.ceil(rest_dist / self.real_speed_max()))
        # return cycle
        
    @staticmethod
    def predict_player_turn_cycle(sp: pb2.ServerParam, ptype: pb2.PlayerType, player_body: AngleDeg, player_speed, target_dist,
                                  target_angle: AngleDeg, dist_thr, use_back_dash):
        n_turn = 0
        angle_diff = (target_angle - player_body).abs()

        if use_back_dash and target_dist < 5.0 and angle_diff > 90.0 and sp.min_dash_power < -sp.max_dash_power + 1.0:
            angle_diff = abs( angle_diff - 180.0 )

        turn_margin = 180.0
        if dist_thr < target_dist:
            turn_margin = max( 15.0, AngleDeg.asin_deg( dist_thr / target_dist ) )

        speed = float(player_speed)
        while angle_diff > turn_margin:
            angle_diff -= Tools.effective_turn( sp.max_moment, speed, ptype.inertia_moment )
            speed *= ptype.player_decay
            n_turn += 1

        return n_turn
    
    @staticmethod
    def effective_turn(command_moment, speed, inertia_moment):
        return command_moment / (1.0 + inertia_moment * speed)
    
    @staticmethod
    def get_nearest_teammate(agent: IAgent, position: Vector2D):
        players = agent.wm.teammates
        best_player = None
        min_dist2 = 1000
        for player in players:
            player_position = Tools.vector2d_message_to_vector2d(player.position)
            d2 = player_position.dist2( position )
            if d2 < min_dist2:
                min_dist2 = d2
                best_player = player

        return best_player
    
    @staticmethod
    def predict_opponent_reach_step(agent: IAgent, opponent: pb2.Player, first_ball_pos: Vector2D, first_ball_vel: Vector2D,
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

