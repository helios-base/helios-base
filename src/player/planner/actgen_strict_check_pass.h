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

#ifndef ACTGEN_STRICT_CHECK_PASS_H
#define ACTGEN_STRICT_CHECK_PASS_H

#include "action_generator.h"

class ActGen_StrictCheckPass
    : public ActionGenerator {

public:
    bool M_generate_direct_pass;
    bool M_generate_lead_pass;
    bool M_generate_through_pass;

    ActGen_StrictCheckPass(bool generete_direct_pass = true,
                           bool generete_lead_pass = true,
                           bool generete_through_pass = true)
        : M_generate_direct_pass(generete_direct_pass),
          M_generate_lead_pass(generete_lead_pass),
          M_generate_through_pass(generete_through_pass)
    { }
    
    virtual
    void generate( std::vector< ActionStatePair > * result,
                   const PredictState & state,
                   const rcsc::WorldModel & wm,
                   const std::vector< ActionStatePair > & path ) const;
};

#endif
