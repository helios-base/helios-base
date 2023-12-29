import service_pb2_grpc as pb2_grpc
import service_pb2 as pb2
import google.protobuf
from concurrent import futures
import grpc
from src.SamplePlayerAgent import SamplePlayerAgent
from threading import RLock

lock = RLock()


class Game(pb2_grpc.GameServicer):
    def __init__(self):
        self.agent = SamplePlayerAgent()
    
    def GetActions(self, request:pb2.State, context):
        # with lock:
        actions = self.agent.get_actions(request.world_model)
        return actions
    
    def SendServerParams(self, request: pb2.ServerParam, context):
        self.agent.set_params(request)
        return pb2.Empty()
    
    def SendPlayerParams(self, request:pb2.PlayerParam, context):
        self.agent.set_params(request)
        return pb2.Empty()
    
    def SendPlayerType(self, request: pb2.PlayerType, context):
        self.agent.set_params(request)
        return pb2.Empty()
    
    def SendInitMessage(self, request, context):
        self.agent.set_debug_mode(request.debug_mode)
        print("Debug mode: ", request.debug_mode)
        return pb2.Empty()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=22))
    pb2_grpc.add_GameServicer_to_server(Game(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started at port 50051")
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
