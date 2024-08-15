#!/bin/bash
set -e

wget -c "https://github.com/linuxdeploy/linuxdeploy/releases/download/continuous/linuxdeploy-x86_64.AppImage" -O linuxdeploy-x86_64.AppImage
chmod 777 linuxdeploy-x86_64.AppImage
PLAYER_APP_IMAGE_DIR_NAME="sample-player-x86_64"
mkdir -p $PLAYER_APP_IMAGE_DIR_NAME
COACH_APP_IMAGE_DIR_NAME="sample-coach-x86_64"
mkdir -p $COACH_APP_IMAGE_DIR_NAME
TRAINER_APP_IMAGE_DIR_NAME="sample-trainer-x86_64"
mkdir -p $TRAINER_APP_IMAGE_DIR_NAME

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
echo "SCRIPT_DIR=" $SCRIPT_DIR

BUILD_PWD="${SCRIPT_DIR}/../../build/bin/"
APP_IMAGE_DIR="${SCRIPT_DIR}"
echo "BUILD_PWD=" $BUILD_PWD
echo "APP_IMAGE_DIR=" $APP_IMAGE_DIR

# find libc and libstdc++ libz dependencies
LIBRCSC_PATH=$(ldd $BUILD_PWD/sample_player | grep librcsc.so.18 | awk '{ print $3 }')
LIBZ_PATH=$(ldd $BUILD_PWD/sample_player | grep libz.so | awk '{ print $3 }')
LIBSTDCPP_PATH=$(ldd $BUILD_PWD/sample_player | grep libstdc++ | awk '{ print $3 }')
LIBM_PATH=$(ldd $BUILD_PWD/sample_player | grep libm.so | awk '{ print $3 }')
LIBGCC_PATH=$(ldd $BUILD_PWD/sample_player | grep libgcc_s.so | awk '{ print $3 }')
LIBC_PATH=$(ldd $BUILD_PWD/sample_player | grep libc.so | awk '{ print $3 }')
LIB_THRIFT_PATH=$(ldd $BUILD_PWD/sample_player | grep libthrift-0.16.0.so | awk '{ print $3 }')
LIB_SSL_PATH=$(ldd $BUILD_PWD/sample_player | grep libssl.so | awk '{ print $3 }')
LIB_CRYPTO_PATH=$(ldd $BUILD_PWD/sample_player | grep libcrypto.so | awk '{ print $3 }')

echo "LIBRCSC_PATH=" $LIBRCSC_PATH
echo "LIBZ_PATH=" $LIBZ_PATH
echo "LIBSTDCPP_PATH=" $LIBSTDCPP_PATH
echo "LIBM_PATH=" $LIBM_PATH
echo "LIBGCC_PATH=" $LIBGCC_PATH
echo "LIBC_PATH=" $LIBC_PATH
echo "LIB_THRIFT_PATH=" $LIB_THRIFT_PATH
echo "LIB_SSL_PATH=" $LIB_SSL_PATH
echo "LIB_CRYPTO_PATH=" $LIB_CRYPTO_PATH

echo "Start to create app image for player"
./linuxdeploy-x86_64.AppImage --appdir ./$PLAYER_APP_IMAGE_DIR_NAME \
                                -e $BUILD_PWD/sample_player \
                                -l $LIBRCSC_PATH \
                                -l $LIBZ_PATH \
                                -l $LIBSTDCPP_PATH \
                                -l $LIBM_PATH \
                                -l $LIBGCC_PATH \
                                -l $LIBC_PATH \
                                -l $LIB_THRIFT_PATH \
                                -l $LIB_SSL_PATH \
                                -l $LIB_CRYPTO_PATH \
                                -d $APP_IMAGE_DIR/sample_player.desktop \
                                -i $APP_IMAGE_DIR/sample_player.png \
                                --output appimage 

echo "Start to create app image for coach"
./linuxdeploy-x86_64.AppImage --appdir ./$COACH_APP_IMAGE_DIR_NAME \
                                -e $BUILD_PWD/sample_coach \
                                -l $LIBRCSC_PATH \
                                -l $LIBZ_PATH \
                                -l $LIBSTDCPP_PATH \
                                -l $LIBM_PATH \
                                -l $LIBGCC_PATH \
                                -l $LIBC_PATH \
                                -l $LIB_THRIFT_PATH \
                                -l $LIB_SSL_PATH \
                                -l $LIB_CRYPTO_PATH \
                                -d $APP_IMAGE_DIR/sample_coach.desktop \
                                -i $APP_IMAGE_DIR/sample_coach.png \
                                --output appimage 

echo "Start to create app image for trainer"
./linuxdeploy-x86_64.AppImage --appdir ./$TRAINER_APP_IMAGE_DIR_NAME \
                                -e $BUILD_PWD/sample_trainer \
                                -l $LIBRCSC_PATH \
                                -l $LIBZ_PATH \
                                -l $LIBSTDCPP_PATH \
                                -l $LIBM_PATH \
                                -l $LIBGCC_PATH \
                                -l $LIBC_PATH \
                                -l $LIB_THRIFT_PATH \
                                -l $LIB_SSL_PATH \
                                -l $LIB_CRYPTO_PATH \
                                -d $APP_IMAGE_DIR/sample_trainer.desktop \
                                -i $APP_IMAGE_DIR/sample_trainer.png \
                                --output appimage 
echo "App Image Created."

echo "Start to create all in one."
mkdir -p soccer-simulation-proxy
mv samplecoach-x86_64.AppImage soccer-simulation-proxy/sample_coach
mv sampleplayer-x86_64.AppImage soccer-simulation-proxy/sample_player
mv sampletrainer-x86_64.AppImage soccer-simulation-proxy/sample_trainer

cp ${BUILD_PWD}formations-dt soccer-simulation-proxy/ -r
cp ${BUILD_PWD}formations-keeper soccer-simulation-proxy/ -r
cp ${BUILD_PWD}formations-taker soccer-simulation-proxy/ -r
cp ${BUILD_PWD}*.conf soccer-simulation-proxy/
cp ${BUILD_PWD}*.sh soccer-simulation-proxy/
chmod 777 soccer-simulation-proxy/*

# if [ -x "$(command -v 7z)" ]; then
#     7z a bin.7z bin/*
# fi

#tar -czvf soccer-simulation-proxy.tar.gz soccer-simulation-proxy/*
#tar -czvf sample_player.tar.gz sample_player
#tar -czvf sample_coach.tar.gz sample_coach
#tar -czvf sample_trainer.tar.gz sample_trainer
#echo "All in one created."
#
rm -rf $PLAYER_APP_IMAGE_DIR_NAME
rm -rf $COACH_APP_IMAGE_DIR_NAME
rm -rf $TRAINER_APP_IMAGE_DIR_NAME
#rm -rf soccer-simulation-proxy
