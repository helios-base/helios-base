[![GitHub license](https://img.shields.io/github/license/helios-base/helios-base)](https://github.com/helios-base/helios-base/blob/master/LISENCE)

# About
RoboCup is an international competition aimed at advancing autonomous robotics and AI through tasks like soccer and rescue. The RoboCup Soccer Simulation 2D league focuses on developing intelligent agents that play soccer in a simulated 2D environment. This league is ideal for testing and developing AI and ML algorithms, including reinforcement learning and multi-agent systems. [more details](https://github.com/CLSFramework/cross-language-soccer-framework/wiki/Definitions)

![image](https://github.com/Cross-Language-Soccer-Framework/cross-language-soccer-framework/assets/25696836/7b0b1d49-7001-479c-889f-46a96a8802c4)


To run a game in the RoboCup Soccer Simulation 2D, you need to operate the rcssserver for hosting games, rcssmonitor to display them, and engage 12 agents (11 players and a coach) per team. Each cycle, agents receive data from the server and must execute actions such as dash and kick. Developing a team can be complex due to the environment's intricacy, typically necessitating C++ programming. However, our framework allows for other languages development, leveraging the helios-base features. By using SoccerSimulationProxy, you can develop a team in any language supported by gRPC, such as C#, C++, Dart, Go, Java, Kotlin, Node, Objective-C, PHP, Python, and Ruby. You just need to develop a gRPC server based on proto messages and gRPC services ([protofile](https://github.com/CLSFramework/soccer-simulation-proxy/blob/master/grpc/protos/service.proto), check [wiki](https://github.com/CLSFramework/cross-language-soccer-framework/wiki/Protobuf) to be more familier with messages and services) to receive data from the SoccerSimulationProxy and send actions back to it. This way, you can focus on developing your team's strategy and AI algorithms without worrying about the server's complexity. If you would like to develop a team or research in this area by using Python, C# or JavaScript you can check the following links:
- [Playmaker-Server-Python](https://github.com/CLSFramework/playmaker-server-python)
- [Playmaker-Server-CSharp](https://github.com/CLSFramework/playmaker-server-csharp)
- [Playmaker-Server-NodeJs](https://github.com/CLSFramework/playmaker-server-nodejs)

![image](https://github.com/Cross-Language-Soccer-Framework/cross-language-soccer-framework/assets/25696836/d152797b-53f0-490f-a8dd-b8c0ef667317)

To find more information about the framework, you can visit the [CLSFramework Wiki Pages](https://github.com/CLSFramework/cross-language-soccer-framework/wiki)


![Screenshot 2024-04-07 012226](https://github.com/Cyrus2D/SoccerSimulationProxy/assets/25696836/abb24e0c-61b9-497d-926f-941d1c90e2ee)

This new base code is powered by Helios-Base code and gRPC to help researcher developing a soccer simulation 2D team or researching in this area by using any languages supported by gRPC: 
 - [C#](https://grpc.io/docs/languages/csharp/) 
   - [Playmaker-Server-CSharp](https://github.com/CLSFramework/playmaker-server-csharp)
 - [C++](https://grpc.io/docs/languages/cpp/)
 - [Dart](https://grpc.io/docs/languages/dart/)
 - [Go](https://grpc.io/docs/languages/go/)
 - [Java](https://grpc.io/docs/languages/java/)
 - [Kotlin](https://grpc.io/docs/languages/kotlin/)
 - [Node](https://grpc.io/docs/languages/node/)
   - [Playmaker-Server-NodeJs](https://github.com/CLSFramework/playmaker-server-nodejs)
 - [Objective-C](https://grpc.io/docs/languages/objective-c/)
 - [PHP](https://grpc.io/docs/languages/php/)
 - [Python](https://grpc.io/docs/languages/python/)
   - [Playmaker-Server-Python](https://github.com/CLSFramework/playmaker-server-python)
 - [Ruby](https://grpc.io/docs/languages/ruby/)

## How To Use it?

To use this framework, you need to run rcssserver to host a game, run SoccerSimulationProxy (Agents) to connect to the rcssserver to receive information and send actions, and run Playmaker-Server (gRPC-Server) to receive information from agents and send appropriate actions back. To watch the game, you can run rcssmonitor or SoccerWindow2.

To run the rcssserver and rcssmonitor, you can follow the instructions in the [rcssserver](https://github.com/CLSFramework/cross-language-soccer-framework/wiki/RoboCup-Soccer-Simulation-Server) and [rcssmonitor](https://github.com/CLSFramework/cross-language-soccer-framework/wiki/Soccer-Simulation-Monitor).

To run the SoccerSimulationProxy, there are some different ways such as using Docker, building from source, or using AppImage.

In this page, we will explain how you can run the SoccerSimulationProxy by using AppImage. To find more information about building from source or using Docker, you can visit the [CLSFramework Wiki Pages](https://github.com/CLSFramework/cross-language-soccer-framework/wiki/Soccer-Simulation-Proxy).

## Use AppImage (Linux, WSL)

### Download
You can download the AppImage of the Soccer Simulation Proxy from the [release page](https://github.com/CLSFramework/soccer-simulation-proxy/releases).

Or download the latest version by using the following command:
```bash
wget $(curl -s "https://api.github.com/repos/clsframework/soccer-simulation-proxy/releases/latest" | grep -oP '"browser_download_url": "\K[^"]*' | grep "soccer-simulation-proxy.tar.gz")
```

### Extract
```bash
tar -xvf soccer-simulation-proxy.tar.gz
```

### Run
```bash
cd SoccerSimulationProxy
./start.sh
```

## References

The paper about HELIOS Base:
- Hidehisa Akiyama, Tomoharu Nakashima, HELIOS Base: An Open Source
Package for the RoboCup Soccer 2D Simulation, In Sven Behnke, Manuela
Veloso, Arnoud Visser, and Rong Xiong editors, RoboCup2013: Robot
World XVII, Lecture Notes in Artificial Intelligence, Springer Verlag,
Berlin, 2014. http://dx.doi.org/10.1007/978-3-662-44468-9_46
