import pytest

from dbs.sqlite_products_table import SqliteProductsTable


@pytest.fixture(scope="module")
def products_table():
    return SqliteProductsTable()
