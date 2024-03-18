from test.test_hm_11.car import Car
import pytest


@pytest.fixture
def car_instance():
    car = Car("Toyota", "Camry", miles_limit=100)
    yield car


@pytest.fixture
def teardown_car_instance(car_instance):
    yield
