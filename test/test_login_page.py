from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from page_objects.locators.login_page import Locators
from utils.config_manager import ConfigManager
from page_objects.login_page import LoginPage
from page_objects.scanners_page import ScannersPage
from selenium.webdriver.common.by import By
import allure
import pytest


@allure.title("Sign in page is displayed")
@allure.description("This test ensures that the Sign in page is loading")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.ui_tests
def test_login_page_loads(get_driver):
    driver = get_driver
    driver.get(ConfigManager.url)
    assert "Cloud Portal" in driver.title, "Page title does not contain 'Cloud Portal'"


def test_login_with_valid_creds(open_login_page, get_user_name, get_user_password):
    LoginPage(open_login_page).do_login(get_user_name, get_user_password)
    ScannersPage(open_login_page).find_scanners_header_btn()
# @allure.title("Sign in with valid credentials")
# @allure.description("This test is verifying whether a user can sign in to the Portal")
# @allure.severity(allure.severity_level.CRITICAL)
# @pytest.mark.ui_tests
# def test_login_with_valid_credentials(get_driver):
#     driver = get_driver
#     driver.get(ConfigManager.url)
#     driver.maximize_window()
#     login_page = LoginPage(driver)
#
#     login_page.set_user_name(ConfigManager.user_name)
#     login_page.set_password(ConfigManager.user_pass)
#
#     login_page.click_login()
#
#     scanners_page = ScannersPage(driver)
#     scanners_page.find_scanners_header_btn()


# def test_login_with_invalid_name(open_login_page, get_invalid_user_name, get_user_password):
#     login_page = LoginPage(open_login_page)
#     login_page.do_login(get_invalid_user_name, get_user_password)
#     error_message = login_page.get_invalid_name_error_message()
#     assert "Incorrect username or password." in error_message


    # LoginPage(open_login_page).do_login(get_invalid_user_name, get_user_password)
    # error_message = LoginPage.get_invalid_name_error_message()
    # assert "Incorrect username or password." in error_message

@allure.title("Sign in with invalid username")
@allure.description("This test is verifying whether a user can't sign in to the Portal with invalid username")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.ui_tests
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


@allure.title("Sign in with invalid password")
@allure.description("This test is verifying whether a user can't sign in to the Portal with invalid password")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.ui_tests
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


@allure.title("Forgot Password button check")
@allure.description("This test is checking that the Forgot Password button is not broken")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.ui_tests
def test_forgot_password_link(get_driver):
    driver = get_driver
    driver.get(ConfigManager.url)
    forgot_password_btn = driver.find_element(By.XPATH, Locators.forgot_password_btn_xpath_locator)
    forgot_password_btn.click()
    reset_password_header = driver.find_element(By.XPATH, Locators.reset_password_xpath_locator).text
    assert "Reset password" in reset_password_header
