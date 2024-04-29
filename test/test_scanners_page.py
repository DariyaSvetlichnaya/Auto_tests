from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import page_objects.scanners_page
from page_objects.locators.scanners_page import Locators
from utils.config_manager import ConfigManager
from page_objects.login_page import LoginPage
from page_objects.login_page import BasePage
from page_objects.scanners_page import ScannersPage
from selenium.webdriver.common.by import By
import os


def test_export_scanners_page(get_driver):
    driver = get_driver
    driver.get(ConfigManager.url)

    # Login
    login_page = LoginPage(driver)
    driver.maximize_window()
    login_page.set_user_name(ConfigManager.user_name)
    login_page.set_password(ConfigManager.user_pass)
    login_page.click_login()

    export_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, Locators.export_scanners_page_xpath_locator)))
    export_button.click()

    file_path = os.path.join(os.path.expanduser('~'), 'Downloads', 'scanners_table_export_data.csv')
    WebDriverWait(driver, 30).until(lambda x: os.path.exists(file_path))
    assert os.path.exists(file_path)


def test_scanner_search(get_driver):
    driver = get_driver
    driver.get(ConfigManager.url)

    # Login
    login_page = LoginPage(driver)
    driver.maximize_window()
    login_page.set_user_name(ConfigManager.user_name)
    login_page.set_password(ConfigManager.user_pass)
    login_page.click_login()

    search_input = page_objects.scanners_page.ScannersPage.find_scanner_search_fld()
    scanner_name = '50007'
    search_input.send_keys(scanner_name)
    search_input.send_keys(Keys.ENTER)

    # # Find the search input field
    # search_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Search']")
    #
    # # Enter the scanner name to search for
    # scanner_name = "Your Scanner Name"
    # search_input.send_keys(scanner_name)
    #
    # # Click on the search button
    # search_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Search')]")
    # search_button.click()
    #
    # # Wait for the search results to appear
    # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
    #     (By.XPATH, "//div[@class='ag-cell ag-cell-not-inline-editing ag-cell-with-height']"))
    #
    # # Assert that the search result contains the expected scanner name
    # search_results = self.driver.find_elements(By.XPATH,
    #  "//div[@class='ag-cell ag-cell-not-inline-editing ag-cell-with-height']")
    # for result in search_results:
    #     self.assertIn(scanner_name, result.text)
