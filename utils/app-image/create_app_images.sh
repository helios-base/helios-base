#!/bin/bash
set -e

wget -c "https://github.com/linuxdeploy/linuxdeploy/releases/download/continuous/linuxdeploy-x86_64.AppImage" -O linuxdeploy-x86_64.AppImage
chmod +x linuxdeploy-x86_64.AppImage
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

echo "LIBRCSC_PATH=" $PLAYER_LIBRCSC_PATH
echo "LIBZ_PATH=" $PLAYER_LIBZ_PATH
echo "LIBSTDCPP_PATH=" $PLAYER_LIBSTDCPP_PATH
echo "LIBM_PATH=" $PLAYER_LIBM_PATH
echo "LIBGCC_PATH=" $PLAYER_LIBGCC_PATH
echo "LIBC_PATH=" $PLAYER_LIBC_PATH

./linuxdeploy-x86_64.AppImage --appdir ./$PLAYER_APP_IMAGE_DIR_NAME \
                                -e $BUILD_PWD/sample_player \
                                -l $LIBRCSC_PATH \
                                -l $LIBZ_PATH \
                                -l $LIBSTDCPP_PATH \
                                -l $LIBM_PATH \
                                -l $LIBGCC_PATH \
                                -l $LIBC_PATH \
                                -d $APP_IMAGE_DIR/sample_player.desktop \
                                -i $APP_IMAGE_DIR/sample_player.png \
                                --output appimage 

./linuxdeploy-x86_64.AppImage --appdir ./$COACH_APP_IMAGE_DIR_NAME \
                                -e $BUILD_PWD/sample_coach \
                                -l $LIBRCSC_PATH \
                                -l $LIBZ_PATH \
                                -l $LIBSTDCPP_PATH \
                                -l $LIBM_PATH \
                                -l $LIBGCC_PATH \
                                -l $LIBC_PATH \
                                -d $APP_IMAGE_DIR/sample_coach.desktop \
                                -i $APP_IMAGE_DIR/sample_coach.png \
                                --output appimage 

./linuxdeploy-x86_64.AppImage --appdir ./$TRAINER_APP_IMAGE_DIR_NAME \
                                -e $BUILD_PWD/sample_trainer \
                                -l $LIBRCSC_PATH \
                                -l $LIBZ_PATH \
                                -l $LIBSTDCPP_PATH \
                                -l $LIBM_PATH \
                                -l $LIBGCC_PATH \
                                -l $LIBC_PATH \
                                -d $APP_IMAGE_DIR/sample_trainer.desktop \
                                -i $APP_IMAGE_DIR/sample_trainer.png \
                                --output appimage 
echo "App Image Created."

echo "Start to create all in one."
mkdir -p bin
mv samplecoach-x86_64.AppImage bin/sample_coach
mv sampleplayer-x86_64.AppImage bin/sample_player
mv sampletrainer-x86_64.AppImage bin/sample_trainer

cp ${BUILD_PWD}formations-dt bin/ -r
cp ${BUILD_PWD}formations-keeper bin/ -r
cp ${BUILD_PWD}formations-taker bin/ -r
cp ${BUILD_PWD}*.conf bin/
cp ${BUILD_PWD}*.sh bin/
chmod 777 bin/*

if [ -x "$(command -v 7z)" ]; then
    7z a bin.7z bin/*
fi

tar -czvf bin.tar.gz bin/*

echo "All in one created."

rm -rf $PLAYER_APP_IMAGE_DIR_NAME
rm -rf $COACH_APP_IMAGE_DIR_NAME
rm -rf $TRAINER_APP_IMAGE_DIR_NAME
rm -rf bin
