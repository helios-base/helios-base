import service_pb2_grpc as pb2_grpc
import service_pb2 as pb2
import google.protobuf
from concurrent import futures
import grpc

from threading import RLock

lock = RLock()


class Game(pb2_grpc.GameServicer):
    def __init__(self):
        pass
    
    def GetActions(self, request:pb2.State, context):
        with lock:
            actions = pb2.Actions()
            actions.actions.append(pb2.Action(dash=pb2.Dash(power=100, relative_direction=30)))
            return actions


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_GameServicer_to_server(Game(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started at port 50051")
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
