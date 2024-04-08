from dbs.sqlite_products_table import SqliteProductsTable
from assertpy import assert_that


def test_get_all_products():

    products = SqliteProductsTable().get_all_products()
    assert_that(len(products), 'Products > 0').is_not_zero()
    assert products

def test_get_product_with_id_1():
    id = 1
    product = SqliteProductsTable().get_product_by_id(id)

    assert_that(product).is_length(id)
    product = product[0]

    assert_that(product[0]).is_equal_to(id)

