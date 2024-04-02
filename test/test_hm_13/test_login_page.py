from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from page_objects.locators.login_page import Locators
from utils.config_manager import ConfigManager
from page_objects.login_page import LoginPage
from page_objects.scanners_page import ScannersPage
from selenium.webdriver.common.by import By


def test_login_page_loads(get_driver):
    driver = get_driver
    driver.get(ConfigManager.url)
    assert "Cloud Portal" in driver.title, "Page title does not contain 'Cloud Portal'"


def test_login_with_valid_credentials(get_driver):
    driver = get_driver
    driver.get(ConfigManager.url)
    driver.maximize_window()
    login_page = LoginPage(driver)
    login_page.set_user_name(ConfigManager.user_name)
    login_page.set_password(ConfigManager.user_pass)
    login_page.click_login()
    scanners_page = ScannersPage(driver)
    scanners_page.find_scanners_header_btn()


def test_login_with_invalid_user_name(get_driver):
    driver = get_driver
    driver.get(ConfigManager.url)
    login_page = LoginPage(driver)
    login_page.set_user_name(ConfigManager.invalid_name)
    login_page.set_password(ConfigManager.user_pass)
    login_page.click_login()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locators.error_message_xpath_locator)))
    error_message = driver.find_element(By.XPATH, Locators.error_message_xpath_locator).text
    assert "Incorrect username or password." in error_message


def test_login_with_invalid_password(get_driver):
    driver = get_driver
    driver.get(ConfigManager.url)
    login_page = LoginPage(driver)
    login_page.set_user_name(ConfigManager.user_name)
    login_page.set_password(ConfigManager.invalid_pass)
    login_page.click_login()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, Locators.error_message_xpath_locator)))
    error_message = driver.find_element(By.XPATH, Locators.error_message_xpath_locator).text
    assert "Incorrect username or password." in error_message


def test_forgot_password_link(get_driver):
    driver = get_driver
    driver.get(ConfigManager.url)
    forgot_password_btn = driver.find_element(By.XPATH, Locators.forgot_password_btn_xpath_locator)
    forgot_password_btn.click()
    reset_password_header = driver.find_element(By.XPATH, Locators.reset_password_xpath_locator).text
    assert "Reset password" in reset_password_header
