#!/bin/sh

dir=`dirname $0`
cd $dir

. "./config"

DIST_DATETIME=`date +"%Y%m%d-%H%M%S"`

echo "##### Create ${TEAM_NAME}S Binary Package #####"

if [ -d ${PACKAGEDIR} ]; then
   echo "The package directory ${PACKAGEDIR} already exists."
   echo "Remove or rename it first."
   exit 1
fi
echo "make directory [${PACKAGEDIR}]"
cp -r template ${PACKAGEDIR}

touch ${PACKAGEDIR}/${DIST_DATETIME}

echo "copy library"
mkdir ${PACKAGEDIR}/lib
cp -a ${LIBDIR}/librcsc.* ${PACKAGEDIR}/lib/

echo "copy team"
cp -rp ${TEAMDIR}/src/formations-dt ${PACKAGEDIR}
cp -a ${TEAMDIR}/src/player.conf ${PACKAGEDIR}
cp -a ${TEAMDIR}/src/coach.conf ${PACKAGEDIR}
cp -a ${TEAMDIR}/src/player/sample_player ${PACKAGEDIR}
cp -a ${TEAMDIR}/src/coach/sample_coach ${PACKAGEDIR}

rm -f ${PACKAGEDIR}/formations-dt/*.conf_*
rm -f ${PACKAGEDIR}/formations-dt/*.conf-*

strip ${PACKAGEDIR}/lib/librcsc.so.*.*.*
strip ${PACKAGEDIR}/sample_player
strip ${PACKAGEDIR}/sample_coach

# Replace @DIST_DATETIME
sed -i -e "s/@DIST_DATETIME@/${DIST_DATETIME}/g" ${PACKAGEDIR}/start

# Replace @TEAM_NAME@
sed -i -e "s/@TEAM_NAME@/${TEAM_NAME}/g" ${PACKAGEDIR}/start

tar czvfp ${PACKAGEDIR}-${DIST_DATETIME}.tar.gz ${PACKAGEDIR}
rm -rf ${PACKAGEDIR}
