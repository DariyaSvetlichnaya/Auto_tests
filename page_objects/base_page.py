from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

        # Loader spinner
        self.loader_spinner = BaseElement(
            self.driver, (By.CSS_SELECTOR, "[class*='animate-spin']")
        )