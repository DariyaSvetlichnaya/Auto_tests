from random import choice
from dbs.db_base.base_sqlite_table import execute_sql_query


class SqliteProductsTable:

    def __init__(self):
        self.db_name = 'products_db.db'
        self.table_name = 'Products'

    @execute_sql_query
    def get_all_products(self):
        return f'select * from {self.table_name}'

    @execute_sql_query
    def get_product_by_id(self, id):
        return f'select product_id from {self.table_name} where product_id = {id}'

    @execute_sql_query
    def create_product(self):
        return f'insert into {self.table_name} values ({choice(range(2, 10000))}, "Chang", 1, 1, 25)'

    @execute_sql_query
    def delete_product_by_id(self, id):
        return f'delete from {self.table_name} where product_id = {id}'


# print(SqliteProducts().get_all_products())
