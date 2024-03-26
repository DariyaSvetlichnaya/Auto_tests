from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from page_objects.locators.login_page import Locators


class LoginPage:

    def __init__(self, driver):
        #super().__init__(driver)
        self.driver = driver
        self.locators = Locators()
  
    def set_user_name(self, username):
        wait = WebDriverWait(self.driver, 5)
        wait.until(ec.visibility_of_element_located((By.ID, self.locators.username_input_id_locator)))

        login_input = self.driver.find_element(by=By.ID, value=self.locators.username_input_id_locator)
        login_input.send_keys(username)

    def set_password(self, password):
        pwd_input = self.driver.find_element(by=By.ID, value=self.locators.password_input_id_locator)
        pwd_input.send_keys(password)

    def click_login(self):
        submit_button = self.driver.find_element(by=By.XPATH, value=self.locators.sign_in_btn_xpath_locator)
        submit_button.click()
