from selenium.webdriver.common.by import By


def test_simple(get_driver):

    username_input_id_locator = 'user-name'  # id of element
    password_input_xpath_locator = '//input[@data-test="password"]'  # x-path locator
    login_btn_xpath_locator = '//*[@type="submit"]'  # x-path locator
    shopping_cart_class_locator = 'shopping_cart_link'

    driver = get_driver

    driver.get(BASE_URL)
    login_input = driver.find_element(by=By.ID, value=username_input_id_locator)
    pwd_input = driver.find_element(by=By.XPATH, value=password_input_xpath_locator)
    submit_button = driver.find_element(by=By.XPATH, value=login_btn_xpath_locator)

    login_input.send_keys(BASE_USER)
    pwd_input.send_keys(BASE_PASSWORD)
    submit_button.click()

    driver.find_element(by=By.CLASS_NAME, value=shopping_cart_class_locator)
