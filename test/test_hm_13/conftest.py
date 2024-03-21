from selenium import webdriver
from pytest import fixture

from utils.driver_factory import DriverFactory


@fixture
def get_driver():
    driver = DriverFactory('chrome').get_driver()
    yield driver
    driver.quit()
