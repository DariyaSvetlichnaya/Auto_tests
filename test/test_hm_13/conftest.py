from selenium import webdriver
from pytest import fixture

from utils.config_manager import ConfigManager
from utils.driver_factory import DriverFactory


@fixture
def get_driver():
    driver = DriverFactory(ConfigManager.browser).get_driver()
    yield driver
    driver.quit()
