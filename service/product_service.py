from protobuff import product_pb2_grpc, product_pb2
from configs.database import Database


class ProductService(product_pb2_grpc.ProductServiceServicer):
    def __init__(self, db: Database):
        self.db = db

    def GetProducts(self, request, context) -> product_pb2.Products:
        per_page = int(request.per_page) if request.per_page else 5
        current_page = int(request.page) if request.page else 1
        offset = (current_page - 1) * per_page

        query = f'''
            SELECT p.id, p.name, p.price::text, p.stock, c.id, c.name
            FROM products p
            JOIN category c on c.id = p.category_id
            LIMIT {per_page} OFFSET {offset};
        '''
        count_query = '''
            SELECT COUNT(*)
            FROM products p
            JOIN category c on c.id = p.category_id
        '''

        # Jalankan query COUNT terlebih dahulu dan simpan hasilnya
        count_result = self.db.exec(count_query, True)
        total_data = count_result[0][0]
        # total_data = 1

        # Jalankan query utama dan simpan hasilnya
        data = self.db.exec(query, True)

        total_page = (total_data + per_page - 1) // per_page

        products_data = []
        pagination = product_pb2.Pagination(
            total=total_data,
            per_page=per_page,
            current_page=current_page,
            last_page=total_page
        )

        for item in data:
            product_data = product_pb2.Product(
                id=item[0],
                name=item[1],
                price=float(item[2]),
                stock=item[3],
                category=product_pb2.Category(
                    id=item[4],
                    name=item[5]
                )
            )
            products_data.append(product_data)

        products = product_pb2.Products(pagination=pagination, data=products_data)
        return products

    def GetProduct(self, request, context):
        data = self.db.exec(f'''
            SELECT p.id, p.name, p.price::text, p.stock, c.id, c.name
            FROM products p
            JOIN category c on c.id = p.category_id
            WHERE p.id = {request.id}
        ''', True)

        product = product_pb2.Product(
            id=data[0][0],
            name=data[0][1],
            price=float(data[0][2]),
            stock=data[0][3],
            category=product_pb2.Category(id=data[0][4], name=data[0][5])
        )
        return product

    def CreateProduct(self, request, context):
        category = self.db.exec(f'''
            SELECT id FROM category c WHERE c.name ilike(\'{request.category.name}\')
        ''', True)
        if not category:
            create_category = self.db.exec(f'''
                INSERT INTO category (name) VALUES ('T-Shirt') RETURNING id;
            ''', True)
            category_id = create_category[0][0]
        else:
            category_id = category[0][0]
        product = self.db.exec(f'''
            INSERT INTO products (name, price, stock, category_id) VALUES (\'{request.name}\', {request.price}, {request.stock}, {category_id}) RETURNING id;
        ''', True)
        
        id_response = product_pb2.Id(id=product[0][0])
        return id_response

    def UpdateProduct(self, request, context):
        category = self.db.exec(f'''
            SELECT id FROM category c WHERE c.name ilike(\'{request.category.name}\')
        ''', True)
        if not category:
            create_category = self.db.exec(f'''
                INSERT INTO category (name) VALUES ('T-Shirt') RETURNING id;
            ''', True)
            category_id = create_category[0][0]
        else:
            category_id = category[0][0]
        product = self.db.exec(f'''
            UPDATE products
            SET name        = COALESCE(\'{request.name}\', name),
                price       = COALESCE({request.price}, price),
                stock       = COALESCE({request.stock}, stock),
                category_id = COALESCE({category_id}, category_id)
            WHERE id = {request.id}
        ''', True)
        update_response = product_pb2.Status(status=200)
        return update_response

    def DeleteProduct(self, request, context):
        self.db.exec(f'''
            DELETE FROM products WHERE id = {request.id}
        ''');
        delete_response = product_pb2.Status(status=204)
        return delete_response
