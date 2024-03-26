from selenium.webdriver.common.by import By
from utils.config_manager import ConfigManager
from page_objects.login_page import LoginPage


def test_simple(get_driver):

    driver = get_driver

    driver.get(ConfigManager.url)
    login_page = LoginPage(driver)

    login_page.set_user_name(ConfigManager.user_name)
    login_page.set_password(ConfigManager.user_pass)
    login_page.click_login()


