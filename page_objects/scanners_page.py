from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from page_objects.locators.scanners_page import Locators
from page_objects.base_page import BasePage


class ScannersPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locators = Locators()

    def find_scanners_header_btn(self):
        self._element_is_visible((By.XPATH, Locators.scanners_header_btn_xpath_locator))
        return self
