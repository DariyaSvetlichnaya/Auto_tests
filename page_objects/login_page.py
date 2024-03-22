from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
# from page_objects.base_page import BasePage
# from page_objects.locators.login_page import Locators
# from page_objects.products_page import ProductsPage


class LoginPage:

    username_input_id_locator = 'user-name'  # id of element
    password_input_xpath_locator = '//input[@data-test="password"]'  # x-path locator
    login_btn_xpath_locator = '//*[@type="submit"]'  # x-path locator

    def __init__(self, driver):
        self.driver = driver

    def set_user_name(self, username):
        wait = WebDriverWait(self.driver, 5)
        wait.until(ec.visibility_of_element_located((By.ID, self.username_input_id_locator)))

        login_input = self.driver.find_element(by=By.ID, value=self.username_input_id_locator)
        login_input.send_keys(username)

    def set_password(self, password):
        pwd_input = self.driver.find_element(by=By.XPATH, value=self.login_btn_xpath_locator)
        pwd_input.send_keys(password)

    def click_login(self):
        submit_button = self.driver.find_element(by=By.XPATH, value=self.login_btn_xpath_locator)
        submit_button.click()
