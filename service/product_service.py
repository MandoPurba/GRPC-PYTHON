from protobuff import product_pb2_grpc, product_pb2
from configs.database import Database


class ProductService(product_pb2_grpc.ProductServiceServicer):
    def __init__(self, db: Database):
        self.db = db

    def GetProducts(self, request, context) -> product_pb2.Products:
        pagination = product_pb2.Pagination(
            total=10,
            per_page=5,
            current_page=1,
            last_page=2
        )
        products_data = [
            product_pb2.Product(
                id=1,
                name="Product 1",
                price=10.99,
                stock=100,
                category=product_pb2.Category(id=1, name='Category 1')
            ),
            product_pb2.Product(
                id=2,
                name="Product 2",
                price=9.10,
                stock=1000,
                category=product_pb2.Category(id=2, name='Category 2')
            )
        ]
        products = product_pb2.Products(pagination=pagination, data=products_data)
        return products

    def GetProduct(self, request, context):
        product = product_pb2.Product(
            id=1,
            name='Product 1',
            price=10.99,
            stock=100,
            category=product_pb2.Category(id=1, name="Product 1")
        )
        return product

    def CreateProduct(self, request, context):
        id_response = product_pb2.Id(id=123)
        return id_response

    def UpdateProduct(self, request, context):
        update_response = product_pb2.Status(status=200)
        return update_response

    def DeleteProduct(self, request, context):
        delete_response = product_pb2.Status(status=204)
        return delete_response
