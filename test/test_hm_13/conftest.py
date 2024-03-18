from selenium import webdriver
from pytest import fixture


@fixture
def get_driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
