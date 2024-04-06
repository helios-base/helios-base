# SS2D-gRPC-Base

![image](https://github.com/Cyrus2D/grpc-2d-base/assets/25696836/ed629150-5285-4512-b6d1-68d07464991a)
![image](https://github.com/Cyrus2D/SS2D-gRPC-Base/assets/25696836/804791be-e945-46ae-943b-0cf236c92602)
![image](https://github.com/Cyrus2D/SS2D-gRPC-Base/assets/25696836/4f0f4bfa-eb61-402b-bc64-bb8b9c0b4980)

[![GitHub license](https://img.shields.io/github/license/helios-base/helios-base)](https://github.com/helios-base/helios-base/blob/master/LISENCE)

SS2D-gRPC-Base is a new framework for the RoboCup Soccer Simulation 2D.
This new base code is powered by Helios-Base code and gRPC to help researcher developing a soccer simulation 2D team or researching in this area by using any languages supported by gRPC: 
 - [C#](https://grpc.io/docs/languages/csharp/) 
   - [Sample SS2D-gRPC-Server-CSharp](https://github.com/Cyrus2D/SS2D-gRPC-Server-CSharp)
 - [C++](https://grpc.io/docs/languages/cpp/)
 - [Dart](https://grpc.io/docs/languages/dart/)
 - [Go](https://grpc.io/docs/languages/go/)
 - [Java](https://grpc.io/docs/languages/java/)
 - [Kotlin](https://grpc.io/docs/languages/kotlin/)
 - [Node](https://grpc.io/docs/languages/node/)
   - [Sample SS2D-gRPC-Server-NodeJs](https://github.com/Cyrus2D/SS2D-gRPC-Server-NodeJs)
 - [Objective-C](https://grpc.io/docs/languages/objective-c/)
 - [PHP](https://grpc.io/docs/languages/php/)
 - [Python](https://grpc.io/docs/languages/python/)
   - [Sample SS2D-gRPC-Server-Python](https://github.com/Cyrus2D/SS2D-gRPC-Server-Python)
 - [Ruby](https://grpc.io/docs/languages/ruby/)
## Informations
### [RoboCup](https://www.robocup.org/)
RoboCup is an international robotics competition that focuses on promoting research and development in the field of autonomous robots. The competition aims to advance the state of the art in robotics and artificial intelligence by challenging teams to develop robots capable of playing soccer, rescue, and other tasks against other teams in a real-world or simulated environments.
### [Soccer Simulation 2D](https://ssim.robocup.org/)
The RoboCup Soccer Simulation 2D (SS2D) is one of the leagues within the RoboCup competition. It involves simulating a soccer game using virtual robots controlled by autonomous software agents. The objective is to develop intelligent strategies and algorithms that enable the virtual robots to play soccer effectively.
### [RCSSServer](https://github.com/rcsoccersim/rcssserver)
The RCSSServer is a soccer server for the RoboCup Soccer Simulation 2D. It is a program that simulates a soccer game between two teams of eleven players and one coach each. The server provides a complete simulation of the game, including the physics of the ball, the field, and the players, as well as the dynamics of the game, such as the rules, the referee, and the game clock.
### [Helios Base Code](https://github.com/helios-base/helios-base)
The Helios Base Code is a framework for the RoboCup Soccer Simulation 2D. It is a collection of software components that provide a common infrastructure for developing soccer simulation 2D teams. The base code is designed to be easy to use and extend, and it provides a number of features that make it easier to develop teams.
### [gRPC](https://grpc.io/docs/what-is-grpc/)
gRPC is a high performance, open source, general-purpose RPC framework that puts mobile and HTTP/2 first. gRPC is based on the HTTP/2 standard, which is the next generation of HTTP. HTTP/2 is a binary protocol that is more efficient than HTTP/1.1, which is the current version of HTTP. HTTP/2 is also more secure than HTTP/1.1, because it uses TLS encryption by default.
### [SS2D-gRPC-Base](https://github.com/Cyrus2D/SS2D-gRPC-Base)
SS2D-gRPC-Base is a new framework for the RoboCup Soccer Simulation 2D. This new base code is powered by Helios-Base code and gRPC to help researcher developing a soccer simulation 2D team or researching in this area by using any languages supported by gRPC such as C#, C++, Dart, Go, Java, Kotlin, Node, Objective-C, PHP, Python, Ruby.
In a normal game, each agents (player, coach, trainer) will connect to the server and send/receive messages to/from the server. By using this new framework, each agent sends infromation that received from RCSSServer after processing to a gRPC Server and receive actions from gRPC Server and send them to RCSSServer.
### [Protocol Buffers](https://github.com/Cyrus2D/SS2D-gRPC-Base/blob/master/grpc/protos/service.proto)
#### Messages from Base Code to gRPC Server
- State
- Server Param
- Player Param
- Player Type
### Actions from gRPC Server to Base Code
### SS2D-gRPC-Server
SS2D-gRPC-Server is a gRPC Server that receives information from SS2D-gRPC-Base and send actions to SS2D-gRPC-Base.
### Sample SS2D-gRPC-Server
### Why not develop a base code for each language?
Developing a base code for each language is a time-consuming task. It requires a lot of effort to develop a base code for each language. The RCSSServer send noisy observation to players and receives low level actions from player such as Dash, Turn, Kick. So, a sample base code should process the received information, denoise information, create a model, make decision, convert high level decision like BodySmartKick, BodyGoToPoint and ... to low level actions and send them to RCSSServer. Therefor, developing a base code for each language is a time-consuming task, also some of the languages are not high performance same as C++ and can not do all of the tasks in a cycle (0.1 second). By using this framework, the SS2D-gRPC-Base denoise information, creates models, sends them to SS2D-gRPC-Server and receives actions from SS2D-gRPC-Server and send them to RCSSServer. So, the SS2D-gRPC-Server can be developed in any language supported by gRPC and its reponsibility is just making decision and sending actions to SS2D-gRPC-Base.
## How To Use it?
### Build From Source
#### Requirements
- Ubuntu 22.04
```bash
sudo apt update
sudo apt install build-essential automake autoconf libtool flex bison libboost-all-dev cmake 
```
- RCSSServer - follow [this](https://github.com/rcsoccersim/rcssserver)
```bash
git clone git@github.com:rcsoccersim/rcssserver.git
cd rcssserver
mkdir build
cd build
cmake ..
make
sudo make install
```
- LibRCSC - follow [this](https://github.com/helios-base/librcsc)
```bash
git clone git@github.com:helios-base/librcsc.git
cd librcsc
git checkout 19175f339dcb5c3f61b56a8c1bff5345109f22ef
mkdir build
cd build
cmake ..
make
make install
```
- gRPC - follow [this](https://grpc.io/docs/languages/cpp/quickstart/)
```bash
export MY_INSTALL_DIR=$HOME/.local
mkdir -p $MY_INSTALL_DIR
export PATH="$MY_INSTALL_DIR/bin:$PATH"
sudo apt install -y build-essential autoconf libtool pkg-config
git clone --recurse-submodules -b v1.62.0 --depth 1 --shallow-submodules https://github.com/grpc/grpc
cd grpc/
mkdir -p cmake/build
pushd cmake/build
cmake -DgRPC_INSTALL=ON       -DgRPC_BUILD_TESTS=OFF       -DCMAKE_INSTALL_PREFIX=$MY_INSTALL_DIR       ../..
make -j 4
make install
```
- - Add the following lines at the end of $HOME/.bashrc
```bash
export MY_INSTALL_DIR=$HOME/.local
export PATH="$MY_INSTALL_DIR/bin:$PATH"
```
- - Use the new version of bashrc
```bash
source $HOME/.bashrc
```
- - to test grpc, go to grpc directory (in this example it is in $HOME/grpc)
```bash
cd examples/cpp/helloworld
mkdir -p cmake/build
cd cmake/build/
cmake -DCMAKE_PREFIX_PATH=$MY_INSTALL_DIR ../..
make
run ./greeter_server in one tab
run ./greeter_client in another tab
```
- SoccerSimulationProxy
```bash
git clone --recurse-submodules git@github.com:Cyrus2D/SoccerSimulationProxy.git
cd SoccerSimulationProxy
mkdir build
cd build
cmake ..
make
```
- - Troubleshooting
    - If you saw an error about the different version of GRpc
    - You should delete src/grpc/service.pb.cc and src/grpc/service.pb.h
    - Then, generate them again by going to the base root directory and
    ```bash
    cd grpc/CrossLangSoccerFramework/proto
    protoc --proto_path=. --cpp_out=../../../src/grpc/ --grpc_out=../../../src/grpc/ --plugin=protoc-gen-grpc=$HOME/.local/bin/grpc_cpp_plugin service.proto
    ```
- Monitor - follow [this](https://github.com/rcsoccersim/rcssmonitor)
Moniter is a GUI for RCSSServer. It is not necessary to run a team. It is just for watching the game and controlling the game.

- Soccer Window2 - follow [this](git@github.com:helios-base/soccerwindow2.git)
Soccer Window2 is a GUI for RCSSServer. It is not necessary to run a team. It is just for watching the game and controlling the game and debugging.
#### Run
You need to run the RCSSServer first to host a soccer simulation 2D game.
Then you should run the SS2D-gRPC-Base to run 12 agents (11 players and 1 coach) and connect them to the RCSSServer.
Before starting the game (kick off), you should run the SS2D-gRPC-Server to receive information from SS2D-gRPC-Base, make decision and send actions to SS2D-gRPC-Base.
All of the agents can connect to the SS2D-gRPC-Server, send information to it, and receive action from it. Also, each agent can connect to a unique SS2D-gRPC-Server. To connect to a unique SS2D-gRPC-Server, you should run 12 different instant of SS2D-gRPC-Server.
To watch a game you need to run RCSSMonitor or SoccerWindow2.

- RCSSServer: run the RCSSServer in a directory that you want to save the game log.
To change server configurations, you can pass the configuration file to the server, or set each config as an argument, or update default values in the $HOME/.rcssserver/server.conf file.
```bash
rcssserver
```

- SS2D-gRPC-Base
```bash
cd build/bin
./start.sh
```
You can change the configuration of the base code by passing arguments to the start.sh script. The arguments are as follows:
- -t: team name
- -h: rcssserver host name
- -p: rcssserver players port
- -P: rcssserver coach port
- -n: number of players
- --g-ip: grpc server ip
- --g-port: grpc server port
- --diff-g-port: specifies different grpc port for each player (from g-port to g-port + n)
- --gp20: add 20 to GRPC Port if team run on right side
### Use Docker
### Use Binary
## Useful Links
## References

The paper about HELIOS Base:
- Hidehisa Akiyama, Tomoharu Nakashima, HELIOS Base: An Open Source
Package for the RoboCup Soccer 2D Simulation, In Sven Behnke, Manuela
Veloso, Arnoud Visser, and Rong Xiong editors, RoboCup2013: Robot
World XVII, Lecture Notes in Artificial Intelligence, Springer Verlag,
Berlin, 2014. http://dx.doi.org/10.1007/978-3-662-44468-9_46
