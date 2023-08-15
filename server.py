from concurrent import futures
from protobuff import product_pb2_grpc
from service.product_service import ProductService
from configs.database import Database
import grpc


def serve():
    db = Database('python_grpc', 'localhost', 'postgres', 'postgres', '5432')
    db.connect()
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    product_pb2_grpc.add_ProductServiceServicer_to_server(ProductService(db), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started listen on " + port)
    server.wait_for_termination()
    db.disconnect()


if __name__ == '__main__':
    serve()
