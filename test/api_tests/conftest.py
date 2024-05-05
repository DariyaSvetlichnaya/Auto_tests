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
