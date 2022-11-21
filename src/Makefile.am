## Process this file with automake to produce Makefile.in

AUTOMAKE_OPTIONS = subdir-objects

noinst_PROGRAMS = sample_player sample_coach sample_trainer

sample_player_CPPFLAGS = -I$(top_srcdir)/src/planner -I$(top_srcdir)/src/setplay
sample_player_CXXFLAGS = -W -Wall
sample_player_LDFLAGS =
sample_player_LDADD =

sample_player_SOURCES = \
	basic_actions/basic_actions.cpp \
	basic_actions/bhv_before_kick_off.cpp \
	basic_actions/bhv_emergency.cpp \
	basic_actions/bhv_go_to_point_look_ball.cpp \
	basic_actions/bhv_scan_field.cpp \
	basic_actions/body_advance_ball2009.cpp \
	basic_actions/body_clear_ball2009.cpp \
	basic_actions/body_dribble2008.cpp \
	basic_actions/body_go_to_point.cpp \
	basic_actions/body_go_to_point_dodge.cpp \
	basic_actions/body_hold_ball2008.cpp \
	basic_actions/body_intercept2009.cpp \
	basic_actions/body_kick_one_step.cpp \
	basic_actions/body_kick_to_relative.cpp \
	basic_actions/body_pass.cpp \
	basic_actions/body_smart_kick.cpp \
	basic_actions/body_stop_ball.cpp \
	basic_actions/body_stop_dash.cpp \
	basic_actions/intention_dribble2008.cpp \
	basic_actions/intention_time_limit_action.cpp \
	basic_actions/kick_table.cpp \
	basic_actions/neck_scan_field.cpp \
	basic_actions/neck_scan_players.cpp \
	basic_actions/neck_turn_to_ball_and_player.cpp \
	basic_actions/neck_turn_to_ball_or_scan.cpp \
	basic_actions/neck_turn_to_goalie_or_scan.cpp \
	basic_actions/neck_turn_to_player_or_scan.cpp \
	basic_actions/neck_turn_to_low_conf_teammate.cpp \
	basic_actions/view_synch.cpp \
	planner/actgen_cross.cpp \
	planner/actgen_direct_pass.cpp \
	planner/actgen_self_pass.cpp \
	planner/actgen_shoot.cpp \
	planner/actgen_short_dribble.cpp \
	planner/actgen_simple_dribble.cpp \
	planner/actgen_strict_check_pass.cpp \
	planner/action_chain_graph.cpp \
	planner/action_chain_holder.cpp \
	planner/bhv_planned_action.cpp \
	planner/bhv_normal_dribble.cpp \
	planner/bhv_pass_kick_find_receiver.cpp \
	planner/bhv_strict_check_shoot.cpp \
	planner/body_force_shoot.cpp \
	planner/clear_ball.cpp \
	planner/clear_generator.cpp \
	planner/cooperative_action.cpp \
	planner/cross_generator.cpp \
	planner/dribble.cpp \
	planner/field_analyzer.cpp \
	planner/hold_ball.cpp \
	planner/neck_turn_to_receiver.cpp \
	planner/pass.cpp \
	planner/predict_state.cpp \
	planner/self_pass_generator.cpp \
	planner/shoot.cpp \
	planner/shoot_generator.cpp \
	planner/short_dribble_generator.cpp \
	planner/simple_pass_checker.cpp \
	planner/strict_check_pass_generator.cpp \
	planner/tackle_generator.cpp \
	setplay/bhv_go_to_placed_ball.cpp \
	setplay/bhv_prepare_set_play_kick.cpp \
	setplay/bhv_set_play.cpp \
	setplay/bhv_set_play_free_kick.cpp \
	setplay/bhv_set_play_goal_kick.cpp \
	setplay/bhv_set_play_indirect_free_kick.cpp \
	setplay/bhv_set_play_kick_in.cpp \
	setplay/bhv_set_play_kick_off.cpp \
	setplay/bhv_their_goal_kick_move.cpp \
	setplay/intention_wait_after_set_play_kick.cpp \
	bhv_basic_move.cpp \
	bhv_basic_tackle.cpp \
	bhv_custom_before_kick_off.cpp \
	bhv_goalie_basic_move.cpp \
	bhv_goalie_chase_ball.cpp \
	bhv_goalie_free_kick.cpp \
	bhv_penalty_kick.cpp \
	neck_default_intercept_neck.cpp \
	neck_goalie_turn_neck.cpp \
	neck_offensive_intercept_neck.cpp \
	view_tactical.cpp \
	intention_receive.cpp \
	soccer_role.cpp \
	role_center_back.cpp \
	role_center_forward.cpp \
	role_defensive_half.cpp \
	role_goalie.cpp \
	role_offensive_half.cpp \
	role_sample.cpp \
	role_side_back.cpp \
	role_side_forward.cpp \
	role_side_half.cpp \
	role_keepaway_keeper.cpp \
	role_keepaway_taker.cpp \
	keepaway_communication.cpp \
	sample_communication.cpp \
	sample_field_evaluator.cpp \
	sample_freeform_message_parser.cpp \
	sample_player.cpp \
	strategy.cpp \
	main_player.cpp

PLAYERHEADERS = \
	bhv_basic_move.h \
	bhv_basic_tackle.h \
	bhv_custom_before_kick_off.h \
	bhv_goalie_basic_move.h \
	bhv_goalie_chase_ball.h \
	bhv_goalie_free_kick.h \
	setplay/bhv_go_to_placed_ball.h \
	setplay/bhv_prepare_set_play_kick.h \
	setplay/bhv_set_play.h \
	setplay/bhv_set_play_free_kick.h \
	setplay/bhv_set_play_goal_kick.h \
	setplay/bhv_set_play_indirect_free_kick.h \
	setplay/bhv_set_play_kick_in.h \
	setplay/bhv_set_play_kick_off.h \
	setplay/bhv_their_goal_kick_move.h \
	setplay/intention_wait_after_set_play_kick.h \
	bhv_penalty_kick.h \
	neck_default_intercept_neck.h \
	neck_goalie_turn_neck.h \
	neck_offensive_intercept_neck.h \
	view_tactical.h \
	intention_receive.h \
	soccer_role.h \
	role_center_back.h \
	role_center_forward.h \
	role_defensive_half.h \
	role_goalie.h \
	role_offensive_half.h \
	role_sample.h \
	role_side_back.h \
	role_side_forward.h \
	role_side_half.h \
	role_keepaway_keeper.h \
	role_keepaway_taker.h \
	communication.h \
	keepaway_communication.h \
	sample_communication.h \
	sample_field_evaluator.h \
	sample_freeform_message_parser.h \
	sample_player.h \
	strategy.h

BASICACTIONHEADERS = \
	basic_actions/basic_actions.h \
	basic_actions/arm_off.h \
	basic_actions/arm_point_to_point.h \
	basic_actions/bhv_before_kick_off.h \
	basic_actions/bhv_body_neck_to_ball.h \
	basic_actions/bhv_body_neck_to_point.h \
	basic_actions/bhv_emergency.h \
	basic_actions/bhv_go_to_point_look_ball.h \
	basic_actions/bhv_neck_body_to_ball.h \
	basic_actions/bhv_neck_body_to_point.h \
	basic_actions/bhv_scan_field.h \
	basic_actions/body_advance_ball.h \
	basic_actions/body_advance_ball2009.h \
	basic_actions/body_clear_ball.h \
	basic_actions/body_clear_ball2009.h \
	basic_actions/body_dribble.h \
	basic_actions/body_dribble2008.h \
	basic_actions/body_go_to_point.h \
	basic_actions/body_go_to_point_dodge.h \
	basic_actions/body_hold_ball.h \
	basic_actions/body_hold_ball2008.h \
	basic_actions/body_intercept.h \
	basic_actions/body_intercept2009.h \
	basic_actions/body_kick_one_step.h \
	basic_actions/body_kick_to_relative.h \
	basic_actions/body_pass.h \
	basic_actions/body_smart_kick.h \
	basic_actions/body_stop_ball.h \
	basic_actions/body_stop_dash.h \
	basic_actions/body_tackle_to_point.h \
	basic_actions/body_turn_to_angle.h \
	basic_actions/body_turn_to_ball.h \
	basic_actions/body_turn_to_point.h \
	basic_actions/intention_dribble2008.h \
	basic_actions/intention_time_limit_action.h \
	basic_actions/kick_table.h \
	basic_actions/neck_scan_field.h \
	basic_actions/neck_scan_players.h \
	basic_actions/neck_turn_to_ball.h \
	basic_actions/neck_turn_to_ball_and_player.h \
	basic_actions/neck_turn_to_ball_or_scan.h \
	basic_actions/neck_turn_to_goalie_or_scan.h \
	basic_actions/neck_turn_to_player_or_scan.h \
	basic_actions/neck_turn_to_low_conf_teammate.h \
	basic_actions/neck_turn_to_point.h \
	basic_actions/neck_turn_to_relative.h \
	basic_actions/view_change_width.h \
	basic_actions/view_normal.h \
	basic_actions/view_synch.h \
	basic_actions/view_wide.h

CHAINACTIONHEADERS = \
	planner/actgen_action_chain_length_filter.h \
	planner/actgen_cross.h \
	planner/actgen_direct_pass.h \
	planner/actgen_self_pass.h \
	planner/actgen_shoot.h \
	planner/actgen_short_dribble.h \
	planner/actgen_simple_dribble.h \
	planner/actgen_strict_check_pass.h \
	planner/action_chain_graph.h \
	planner/action_chain_holder.h \
	planner/action_generator.h \
	planner/action_state_pair.h \
	planner/bhv_planned_action.h \
	planner/bhv_normal_dribble.h \
	planner/bhv_pass_kick_find_receiver.h \
	planner/bhv_strict_check_shoot.h \
	planner/body_force_shoot.h \
	planner/clear_ball.h \
	planner/clear_generator.h \
	planner/cooperative_action.h \
	planner/cross_generator.h \
	planner/dribble.h \
	planner/field_analyzer.h \
	planner/field_evaluator.h \
	planner/hold_ball.h \
	planner/neck_turn_to_receiver.h \
	planner/pass.h \
	planner/pass_checker.h \
	planner/predict_ball_object.h \
	planner/predict_player_object.h \
	planner/predict_state.h \
	planner/self_pass_generator.h \
	planner/shoot.h \
	planner/shoot_generator.h \
	planner/short_dribble_generator.h \
	planner/simple_pass_checker.h \
	planner/strict_check_pass_generator.h \
	planner/tackle_generator.h

COACHSOURCES = \
	sample_freeform_message.cpp \
	sample_coach.cpp \
	main_coach.cpp

COACHHEADERS = \
	sample_freeform_message.h \
	sample_coach.h

TRAINERSOURCES = \
	sample_trainer.cpp \
	main_trainer.cpp

TRAINERHEADERS = \
	sample_trainer.h


noinst_DATA = \
	start.sh.in \
	keepaway.sh.in \
	train.sh.in \
	coach.conf \
	player.conf \
	team_logo.xpm \
	formations-dt/before-kick-off.conf \
	formations-dt/goal-kick-opp.conf \
	formations-dt/goal-kick-our.conf \
	formations-dt/goalie-catch-opp.conf \
	formations-dt/goalie-catch-our.conf \
	formations-dt/goalie-formation.conf \
	formations-dt/indirect-freekick-opp-formation.conf \
	formations-dt/indirect-freekick-our-formation.conf \
	formations-dt/kickin-our-formation.conf \
	formations-dt/normal-formation.conf \
	formations-dt/defense-formation.conf \
	formations-dt/offense-formation.conf \
	formations-dt/setplay-opp-formation.conf \
	formations-dt/setplay-our-formation.conf \
	formations-keeper/before-kick-off.conf \
	formations-keeper/goal-kick-opp.conf \
	formations-keeper/goal-kick-our.conf \
	formations-keeper/goalie-catch-opp.conf \
	formations-keeper/goalie-catch-our.conf \
	formations-keeper/goalie-formation.conf \
	formations-keeper/indirect-freekick-opp-formation.conf \
	formations-keeper/indirect-freekick-our-formation.conf \
	formations-keeper/kickin-our-formation.conf \
	formations-keeper/normal-formation.conf \
	formations-keeper/defense-formation.conf \
	formations-keeper/offense-formation.conf \
	formations-keeper/setplay-opp-formation.conf \
	formations-keeper/setplay-our-formation.conf \
	formations-taker/before-kick-off.conf \
	formations-taker/goal-kick-opp.conf \
	formations-taker/goal-kick-our.conf \
	formations-taker/goalie-catch-opp.conf \
	formations-taker/goalie-catch-our.conf \
	formations-taker/goalie-formation.conf \
	formations-taker/indirect-freekick-opp-formation.conf \
	formations-taker/indirect-freekick-our-formation.conf \
	formations-taker/kickin-our-formation.conf \
	formations-taker/normal-formation.conf \
	formations-taker/defense-formation.conf \
	formations-taker/offense-formation.conf \
	formations-taker/setplay-opp-formation.conf \
	formations-taker/setplay-our-formation.conf

sample_coach_SOURCES = \
	$(COACHSOURCES)
sample_coach_CXXFLAGS = -W -Wall
sample_coach_LDFLAGS =
sample_coach_LDADD =

sample_trainer_SOURCES = \
	$(TRAINERSOURCES)
sample_trainer_CXXFLAGS = -W -Wall
sample_trainer_LDFLAGS =
sample_trainer_LDADD =

noinst_HEADERS = \
	$(BASICACTIONHEADERS) \
	$(CHAINACTIONHEADERS) \
	$(PLAYERHEADERS) \
	$(COACHHEADERS) \
	$(TRAINERHEADERS)

AM_CPPFLAGS = -I$(top_srcdir)/src
AM_CFLAGS = -W -Wall
AM_CXXFLAGS = -W -Wall
AM_LDLAGS =

CLEANFILES = core *~

DISTCLEANFILES = start.sh train.sh

EXTRA_DIST = $(noinst_DATA) \
	start-debug.sh \
	start-offline.sh
