from assertpy import assert_that


def test_create_product(products_table):
    # Positive test: Ensure product is created successfully
    products_table.create_product()
    products = products_table.get_all_products()

    assert_that(len(products) > 0, "No products found in the database")


def test_get_product_by_name(products_table):
    # Positive test: Ensure product can be retrieved by name
    name = "Syrup"
    product = products_table.get_product_by_name(name)
    product = product[0]

    assert_that(product[0]).is_equal_to(name)


def test_create_product_with_empty_name(products_table):
    # Negative test: Attempt to create a product with an empty name
    initial_product_count = len(products_table.get_all_products())
    products_table.create_product(product_name='')
    final_product_count = len(products_table.get_all_products())

    assert initial_product_count == final_product_count


def test_create_product_with_invalid_name(products_table):
    # Negative test: Attempt to create a product with characters in the name
    initial_product_count = len(products_table.get_all_products())
    products_table.create_product(product_name='%^&&')
    final_product_count = len(products_table.get_all_products())

    assert initial_product_count == final_product_count
