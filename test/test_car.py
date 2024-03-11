
def test_start_engine(car_instance):
    assert car_instance.start_engine() == "Engine started."


def test_stop_engine(car_instance):
    car_instance.start_engine()
    assert car_instance.stop_engine() == "Engine stopped."


def test_drive_successful(car_instance):
    car_instance.start_engine()
    assert car_instance.drive(50) == "Driving 50 miles."


def test_drive_exceeds_limit(car_instance):
    car_instance.start_engine()
    assert car_instance.drive(150) == "The miles limit has been exceeded"


def test_drive_engine_off(car_instance):
    assert car_instance.drive(50) == "Cannot drive. Engine is off."


def test_start_engine_twice(car_instance):
    car_instance.start_engine()
    assert car_instance.start_engine() == "Engine is already running."


def test_stop_engine_twice(car_instance):
    car_instance.start_engine()
    car_instance.stop_engine()
    assert car_instance.stop_engine() == "Engine is already off."


def test_drive_engine_off_limit_not_exceeded(car_instance):
    assert car_instance.drive(50) == "Cannot drive. Engine is off."
    assert car_instance.drive(20) == "Cannot drive. Engine is off."


def test_drive_engine_off_limit_exceeded(car_instance):
    assert car_instance.drive(150) == "Cannot drive. Engine is off."
    assert car_instance.drive(20) == "Cannot drive. Engine is off."


def test_drive_car(car_instance, teardown_car_instance):
    assert car_instance.start_engine() == "Engine started."
    assert car_instance.drive(50) == "Driving 50 miles."
    assert car_instance.stop_engine() == "Engine stopped."
