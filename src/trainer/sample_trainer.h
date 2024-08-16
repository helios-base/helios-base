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

#ifndef SAMPLE_TRAINER_H
#define SAMPLE_TRAINER_H

#include <rcsc/trainer/trainer_agent.h>
#ifdef USE_THRIFT
#include "thrift-client/thrift_client_trainer.h"
#endif
#ifdef USE_GRPC
#include "grpc-client/grpc_client_trainer.h"
#endif

#include "rpc-client/rpc-client.h"
#include "rpc-client/rpc-agent.h"


class SampleTrainer
    : public rcsc::TrainerAgent, public RpcAgent{

public:

    SampleTrainer();

    virtual
    ~SampleTrainer();

    void SetRpcType(bool use_thrift){
        M_use_thrift = use_thrift;
        if (use_thrift){
#ifdef USE_THRIFT
            M_rpc_client = new ThriftClientTrainer();
#endif
        }
        else
        {
#ifdef USE_GRPC
            M_rpc_client = new GrpcClientTrainer();
#endif
        }
    }

protected:

    /*!
      You can override this method.
      But you must call TrainerAgent::doInit() in this method.
    */
    virtual
    bool initImpl( rcsc::CmdLineParser & cmd_parser );
    void
    handleExit() override;

    //! main decision
    virtual
    void actionImpl();

    virtual
    void handleInitMessage();
    virtual
    void handleServerParam();
    virtual
    void handlePlayerParam();
    virtual
    void handlePlayerType();

private:

    void sampleAction();
    void recoverForever();
    void doSubstitute();
    void doKeepaway();

};

#endif
