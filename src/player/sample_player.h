// -*-c++-*-

/*
 *Copyright:

 Copyright (C) Hidehisa AKIYAMA

 This code is free software; you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation; either version 3, or (at your option)
 any later version.

 This code is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License
 along with this code; see the file COPYING.  If not, write to
 the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.

 *EndCopyright:
 */

/////////////////////////////////////////////////////////////////////

#ifndef SAMPLE_PLAYER_H
#define SAMPLE_PLAYER_H

#include "action_generator.h"
#include "field_evaluator.h"
#include "communication.h"
#include "grpc/grpc_agent_player.h"

#include <rcsc/player/player_agent.h>
#include <vector>

class SamplePlayer
    : public rcsc::PlayerAgent {
private:

    Communication::Ptr M_communication;

    FieldEvaluator::ConstPtr M_field_evaluator;
    ActionGenerator::ConstPtr M_action_generator;
    GrpcAgentPlayer M_grpc_agent = GrpcAgentPlayer();
    int M_first_grpc_port;
    bool M_use_same_grpc_port;
    bool M_add_20_to_grpc_port_if_right_side;

public:

    SamplePlayer();

    virtual
    ~SamplePlayer();

    void SetFirstGrpcPort(int port) { M_first_grpc_port = port; }
    void SetUseSameGrpcPort(bool use_same_grpc_port) { M_use_same_grpc_port = use_same_grpc_port; }
    void SetAdd20ToGrpcPortIfRightSide(bool add_20_to_grpc_port_if_right_side) { M_add_20_to_grpc_port_if_right_side = add_20_to_grpc_port_if_right_side; }

protected:

    /*!
      You can override this method.
      But you must call PlayerAgent::initImpl() in this method.
    */
    virtual
    bool initImpl( rcsc::CmdLineParser & cmd_parser );

    //! main decision
    virtual
    void actionImpl();

    //! communication decision
    virtual
    void communicationImpl();

    virtual
    void handleActionStart();
    virtual
    void handleActionEnd();

    virtual
    void handleInitMessage();
    virtual
    void handleServerParam();
    virtual
    void handlePlayerParam();
    virtual
    void handlePlayerType();

    virtual
    FieldEvaluator::ConstPtr createFieldEvaluator() const;

    virtual
    ActionGenerator::ConstPtr createActionGenerator() const;

private:

    bool doPreprocess();
    bool doShoot();
    bool doForceKick();
    bool doHeardPassReceive();

public:
    virtual
    FieldEvaluator::ConstPtr getFieldEvaluator() const;
};

#endif
