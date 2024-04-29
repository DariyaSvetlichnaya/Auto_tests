from pytest import fixture

from utils.config_manager import ConfigManager
from utils.driver_factory import DriverFactory
from selenium.webdriver.remote.webdriver import WebDriver


@fixture
def get_driver():
    driver = DriverFactory(ConfigManager.browser).get_driver()
    yield driver
    driver.quit()


@fixture
def open_login_page(get_driver) -> WebDriver:
    get_driver.get(ConfigManager.url)
    get_driver.maximize_window()
    return get_driver


@fixture(scope='session')
def get_user_name() -> str:
    return ConfigManager.user_name


@fixture(scope='session')
def get_user_password() -> str:
    return ConfigManager.user_pass


@fixture(scope='session')
def get_invalid_user_name() -> str:
    return ConfigManager.invalid_name


@fixture(scope='session')
def get_invalid_user_password() -> str:
    return ConfigManager.invalid_pass
