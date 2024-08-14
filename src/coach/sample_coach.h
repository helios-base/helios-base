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

#ifndef SAMPLE_COACH_H
#define SAMPLE_COACH_H

#include <rcsc/coach/coach_agent.h>
#include <rcsc/types.h>
#include "thrift-client/thrift_agent_coach.h"
#include "grpc-client/grpc_agent_coach.h"
#include "rpc-client/rpc-agent.h"
#include <vector>


namespace rcsc {
class PlayerType;
}


class SampleCoach
    : public rcsc::CoachAgent {
private:
    typedef std::vector< const rcsc::PlayerType * > PlayerTypePtrCont;


    int M_opponent_player_types[11];

    rcsc::TeamGraphic M_team_graphic;

    IRpcAgent * M_grpc_agent;
    int M_first_grpc_port;
    bool M_use_same_grpc_port;
    bool M_add_20_to_grpc_port_if_right_side;
    std::string M_grpc_server_address;
    bool M_use_thrift;

public:

    SampleCoach();

    virtual
    ~SampleCoach();

    void SetFirstGrpcPort(int port) { M_first_grpc_port = port; }
    void SetUseSameGrpcPort(bool use_same_grpc_port) { M_use_same_grpc_port = use_same_grpc_port; }
    void SetAdd20ToGrpcPortIfRightSide(bool add_20_to_grpc_port_if_right_side) { M_add_20_to_grpc_port_if_right_side = add_20_to_grpc_port_if_right_side; }
    void SetGrpcIp(std::string grpc_server_address) { M_grpc_server_address = grpc_server_address; }
    void SetRpc(bool use_thrift){
        M_use_thrift = use_thrift;
        if (use_thrift){
            M_grpc_agent = new ThriftAgentCoach();
        }
        else
        {
            M_grpc_agent = new GrpcAgentCoach();
        }
    }
    
    void doSubstitute();
    void sayPlayerTypes();

protected:

    /*!
      You can override this method.
      But, CoachAgent::initImpl() must be called in this method.
    */
    virtual
    bool initImpl( rcsc::CmdLineParser & cmd_parser );

    //! main decision making
    virtual
    void actionImpl();
    void
    handleExit() override;


    virtual
    void handleInitMessage();
    virtual
    void handleServerParam();
    virtual
    void handlePlayerParam();
    virtual
    void handlePlayerType();

private:

    void doFirstSubstitute();
    void doSubstituteTiredPlayers();

    void substituteTo( const int unum,
                       const int type );

    int getFastestType( PlayerTypePtrCont & candidates );

    void sendTeamGraphic();
};

#endif
