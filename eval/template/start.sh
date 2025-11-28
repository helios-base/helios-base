#!/bin/bash
HOST=127.0.0.1

HOMEDIR=`dirname $0`
${HOMEDIR}/start ${HOST} ${HOMEDIR} 1 &
sleep 0.5
${HOMEDIR}/start ${HOST} ${HOMEDIR} 2 &
sleep 0.1
${HOMEDIR}/start ${HOST} ${HOMEDIR} 3 &
sleep 0.1
${HOMEDIR}/start ${HOST} ${HOMEDIR} 4 &
sleep 0.1
${HOMEDIR}/start ${HOST} ${HOMEDIR} 5 &
sleep 0.1
${HOMEDIR}/start ${HOST} ${HOMEDIR} 6 &
sleep 0.1
${HOMEDIR}/start ${HOST} ${HOMEDIR} 7 &
sleep 0.1
${HOMEDIR}/start ${HOST} ${HOMEDIR} 8 &
sleep 0.1
${HOMEDIR}/start ${HOST} ${HOMEDIR} 9 &
sleep 0.1
${HOMEDIR}/start ${HOST} ${HOMEDIR} 10 &
sleep 0.1
${HOMEDIR}/start ${HOST} ${HOMEDIR} 11 &
sleep 0.5
${HOMEDIR}/start ${HOST} ${HOMEDIR} 12 &

