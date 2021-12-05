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


## Reference

If you use helios-base in your scientific work, please cite as:

- Hidehisa Akiyama, Tomoharu Nakashima, HELIOS Base: An Open Source
Package for the RoboCup Soccer 2D Simulation, In Sven Behnke, Manuela
Veloso, Arnoud Visser, and Rong Xiong editors, RoboCup2013: Robot
World XVII, Lecture Notes in Artificial Intelligence, Springer Verlag,
Berlin, 2014.

```
@inbook{akiyama2014,
  author="Hidehisa AKIYAMA and Tomoharu NAKASHIMA",
  editor="Sven Behnke and Manuela Veloso and Arnoud Visser and Rong Xiong",
  title="HELIOS Base: An Open Source Package for the RoboCup Soccer 2D Simulation",
  booktitle="RoboCup 2013: Robot World Cup XVII",
  series="Lecture Notes in Artificial Intelligence",
  year="2014",
  publisher="Springer",
  address="Berlin",
  pages="528--535",
  isbn="978-3-662-44468-9",
  doi="10.1007/978-3-662-44468-9_46",
  url="http://dx.doi.org/10.1007/978-3-662-44468-9_46"
}
```

