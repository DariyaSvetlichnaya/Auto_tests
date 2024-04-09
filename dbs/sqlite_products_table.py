from dbs.db_base.base_sqlite_table import execute_sql_query


class SqliteProductsTable:

    def __init__(self):
        self.db_name = 'products_db.db'
        self.table_name = 'Products'

    @execute_sql_query
    def get_all_products(self):
        return f'select * from {self.table_name}'

    @execute_sql_query
    def get_product_by_name(self, name):
        return f'select product_name from {self.table_name} where product_name = "{name}"'

    @execute_sql_query
    def get_product_by_product_id(self, product_id):
        return f'select * from {self.table_name} where product_id = {product_id}'

    def create_product(self, product_id=1, product_name='Tea', supplier_id=2, category_id=1, price=25):
        if not product_name or any(char in "!@#$%" for char in product_name):
            return "Invalid product name"
        sql_query = f'insert into {self.table_name} values ({product_id}, "{product_name}", {supplier_id}, {category_id}, {price})'
        return sql_query

    @execute_sql_query
    def delete_product_by_id(self, product_id):
        return f'delete from {self.table_name} where product_id = {product_id}'

    @execute_sql_query
    def update_product_category_id(self, category_id, product_id):
        return f'update {category_id} set {category_id} = 2 where product_id = {product_id}'
