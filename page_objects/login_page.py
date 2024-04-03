from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from page_objects.locators.login_page import Locators
from page_objects.base_page import BasePage
import allure


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
        wait = WebDriverWait(self.driver, 5)
        wait.until(ec.visibility_of_element_located((By.ID, self.locators.username_input_id_locator)))

        login_input = self.driver.find_element(by=By.ID, value=self.locators.username_input_id_locator)
        login_input.send_keys(username)

    @allure.step("Step 3")
    def set_password(self, password):
        pwd_input = self.driver.find_element(by=By.ID, value=self.locators.password_input_id_locator)
        pwd_input.send_keys(password)

    @allure.step("Step 4")
    def click_login(self):
        submit_button = self.driver.find_element(by=By.XPATH, value=self.locators.sign_in_btn_xpath_locator)
        submit_button.click()
