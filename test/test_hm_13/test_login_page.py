import pytest
from utils.config_manager import ConfigManager
from page_objects.login_page import LoginPage


def test_login_load(get_driver):
    driver = get_driver
    driver.get(ConfigManager.url)
    signin_page = LoginPage(driver)
    assert signin_page.is_loaded(), "Login page did not load successfully"

# def test_sign_in(get_driver):
#
#     driver = get_driver
#
#     driver.get(ConfigManager.url)
#     login_page = LoginPage(driver)
#
#     login_page.set_user_name(ConfigManager.user_name)
#     login_page.set_password(ConfigManager.user_pass)
#     login_page.click_login()
