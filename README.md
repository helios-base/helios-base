# SS2D-gRPC-Base

![image](https://github.com/Cyrus2D/grpc-2d-base/assets/25696836/ed629150-5285-4512-b6d1-68d07464991a)

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
#### Messages from Base Code to gRPC Server
#### State
#### Server Param
#### Player Param
#### Player Type
### Actions from gRPC Server to Base Code
### SS2D-gRPC-Server
SS2D-gRPC-Server is a gRPC Server that receives information from SS2D-gRPC-Base and send actions to SS2D-gRPC-Base.
### Sample SS2D-gRPC-Server
### Why not develop a base code for each language?
Developing a base code for each language is a time-consuming task. It requires a lot of effort to develop a base code for each language. The RCSSServer send noisy observation to players and receives low level actions from player such as Dash, Turn, Kick. So, a sample base code should process the received information, denoise information, create a model, make decision, convert high level decision like BodySmartKick, BodyGoToPoint and ... to low level actions and send them to RCSSServer. Therefor, developing a base code for each language is a time-consuming task, also some of the languages are not high performance same as C++ and can not do all of the tasks in a cycle (0.1 second). By using this framework, the SS2D-gRPC-Base denoise information, creates models, sends them to SS2D-gRPC-Server and receives actions from SS2D-gRPC-Server and send them to RCSSServer. So, the SS2D-gRPC-Server can be developed in any language supported by gRPC and its reponsibility is just making decision and sending actions to SS2D-gRPC-Base.
## How To Use it?
### Build From Source
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
