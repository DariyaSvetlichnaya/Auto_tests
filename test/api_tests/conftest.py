import pytest

from api_service.events_api import EventsApi

events_api = EventsApi()

@pytest.fixture
def get_new_event_body():
    return [
        {
            "name": "Event80",
            "customer_event_category_id": 331,
            "reporting_start_time": "2023-08-23T09:56:40.499Z",
            "reporting_end_time": "2023-09-23T09:56:40.499Z",
            "start_time": "2023-08-23T09:56:40.499Z",
            "scanner_names": [
                "EXPR50007"
            ]
        }
    ]

@pytest.fixture
def get_event_body_without_scanners():
    return [
        {
            "name": "Event80",
            "customer_event_category_id": 331,
            "reporting_start_time": "2023-08-23T09:56:40.499Z",
            "reporting_end_time": "2023-09-23T09:56:40.499Z",
            "start_time": "2023-08-23T09:56:40.499Z",
            "scanner_names": [
            ]
        }
    ]

@pytest.fixture
def get_event_body_end_before_start():
    return [
        {
            "name": "Event80",
            "customer_event_category_id": 331,
            "reporting_start_time": "2023-10-23T09:56:40.499Z",
            "reporting_end_time": "2023-09-23T09:56:40.499Z",
            "start_time": "2023-08-23T09:56:40.499Z",
            "scanner_names": [
                "EXPR50007"
            ]
        }
    ]

@pytest.fixture
def get_event_body_start_after_end():
    return [
        {
            "name": "Event80",
            "customer_event_category_id": 331,
            "reporting_start_time": "2023-08-25T09:50:10.292Z",
            "reporting_end_time": "2023-08-25T10:50:10.292Z",
            "start_time": "2023-09-23T10:00:10.292Z",
            "scanner_names": [
                "EXPR50007"
            ]
        }
    ]
