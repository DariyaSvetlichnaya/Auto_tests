from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from page_objects.locators.login_page import Locators
from page_objects.base_page import BasePage
import allure

from page_objects.scanners_page import ScannersPage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locators = Locators()

    @allure.step("Step 1")
    def is_loaded(self):
        wait = WebDriverWait(self.driver, 5)
        wait.until(ec.element_to_be_clickable((By.ID, self.locators.forgot_password_btn_xpath_locator)))

    @allure.step("Step 2")
    def set_user_name(self, username):
        self._fill_input(username, (By.ID, self.locators.username_input_id_locator))
        return self
        # wait = WebDriverWait(self.driver, 5)
        # wait.until(ec.visibility_of_element_located((By.ID, self.locators.username_input_id_locator)))
        #
        # login_input = self.driver.find_element(by=By.ID, value=self.locators.username_input_id_locator)
        # login_input.send_keys(username)

    @allure.step("Step 3")
    def set_password(self, password):
        self._fill_input(password, (By.ID, self.locators.password_input_id_locator))
        return self
        # pwd_input = self.driver.find_element(by=By.ID, value=self.locators.password_input_id_locator)
        # pwd_input.send_keys(password)

    @allure.step("Step 4")
    def click_login(self):
        self._click_button(By.XPATH, self.locators.sign_in_btn_xpath_locator)
        return ScannersPage(self.driver)
        # submit_button = self.driver.find_element(by=By.XPATH, value=self.locators.sign_in_btn_xpath_locator)
        # submit_button.click()

    def do_login(self, username, password):
        self.set_user_name(username)
        self.set_password(password)
        self.click_login()
        return self

    def get_invalid_name_error_message(self):
        self._element_is_visible(By.XPATH, self.locators.error_message_xpath_locator)
        return self.driver.find_element(By.XPATH, self.locators.error_message_xpath_locator).text
