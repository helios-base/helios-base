# HELIOS Base
[![GitHub license](https://img.shields.io/github/license/helios-base/helios-base)](https://github.com/helios-base/helios-base/blob/master/LISENCE)

helios-base is a sample team for the RoboCup Soccer 2D Simulator.
All programs can work with rcssserver-16.

- The RoboCup Soccer Simulator: http://github.com/rcsoccersim/
- RoboCup Official Homepage: http://www.robocup.org/

## Quick Start

The latest helios-base depends on the following libraries:
 - Boost 1.38 or later https://www.boost.org/
 - The latest librcsc https://github.com/helios-base/librcsc

In the case of Ubuntu 16.04 or later, execute the following commands for installing a basic development environment:
```
sudo apt update
sudo apt install build-essential libboost-all-dev
```
And, install librcsc.

To build binaries, execute commands from the root of source directory:
```
./bootstrap
./configure
make
```

To start the agent2d team, invoke the start script in `src` directory.
```
./start.sh
```

## Configuring

You may need to configure the build settings if you installed librcsc to an unusual location. 
You can specify the installed location of librcsc by using `--with-librcsc` option as follows:
```
./configure --with-librcsc=/path/to/librcsc
```
Usually, this value is the same as `--prefix` option of configuring librcsc.
You may also need to set the environment variable `LD_LIBRARY_PATH`.

See `./configure --help` for others options.


## References

- Hidehisa Akiyama, Tomoharu Nakashima, HELIOS2012: RoboCup 2012 Soccer Simulation 2D League Champion, RoboCup 2012: Robot Soccer World Cup XVI Lecture Notes in Computer 
- Hidehisa Akiyama, Tomoharu Nakashima, HELIOS Base: An Open Source
Package for the RoboCup Soccer 2D Simulation, In Sven Behnke, Manuela
Veloso, Arnoud Visser, and Rong Xiong editors, RoboCup2013: Robot
World XVII, Lecture Notes in Artificial Intelligence, Springer Verlag,
Berlin, 2014. http://dx.doi.org/10.1007/978-3-662-44468-9_46
Science Volume 7500, pp.13-19, June 2013. http://dx.doi.org/10.1007/978-3-642-39250-4_2
- Takuya Fukushima, Tomoharu Nakashima, Hidehisa Akiyama, Mimicking an Expert Team through the Learning of Evaluation Functions from Action Sequences, RoboCup 2018: Robot World Cup XXII Lecture Notes in Computer Science, Vol. 11374, Springer, Cham, pp 170-180, 04 August 2019  https://doi.org/10.1007/978-3-030-27544-0_14
- Hidehisa Akiyama, Tomoharu Nakashima, Takuya Fukushima, Jiarun Zhong, Yudai Suzuki, An Ohori, HELIOS2018: RoboCup 2018 Soccer Simulation 2D League Champion, RoboCup 2018: Robot World Cup XXII, Lecture Notes in Computer Science, Vol.11374, Springer, Cham, pp.450-461, 04 August 2019. https://doi.org/10.1007/978-3-030-27544-0_37
- 福島卓弥, 中島智晴, 秋山英久, RoboCupサッカーにおけるニューラルネットワークを用いた評価関数モデリング, 電気学会論文誌Ｃ（電子・情報・システム部門誌）, 2019, 139 巻, 10 号, pp. 1128-1133, 2019-10-01 https://doi.org/10.1541/ieejeiss.139.1128
- 秋山 英久, 中島 智晴, 五十嵐 治一, RoboCup サッカーシミュレーションにおける局面評価の表現法と学習法, 知能と情報, 2020, 32 巻, 2 号, p. 691-703, 公開日 2020/04/15, Online ISSN 1881-7203, Print ISSN 1347-7986, https://doi.org/10.3156/jsoft.32.2_691
- Takuya Fukushima, Tomoharu Nakashima, Hidehisa Akiyama, Evaluation-function modeling with multi-layered perceptron for RoboCup soccer 2D simulation, Artificial Life and Robotics, Volume 25, issue 3, pp.440-445, 2020-04-30. https://doi.org/10.1007/s10015-020-00602-w

