import test.api_tests.conftest


def test_get_all_events():
    response = test.api_tests.conftest.events_api.get_all_events()
    assert response.status_code == 200


def test_create_event(get_new_event_body):

    response = test.api_tests.conftest.events_api.create_events(body=get_new_event_body)

    assert response.status_code == 200
    assert any(item.get('id') is not None for item in response.json())


def test_get_event_by_id():
    response = test.api_tests.conftest.events_api.get_event_by_id()
    assert response.status_code == 200


def test_delete_event():
    response = test.api_tests.conftest.events_api.delete_event()
    assert response.status_code == 200


def test_get_events_sample_file():
    response = test.api_tests.conftest.events_api.get_events_sample_file()
    assert response.status_code == 200

    headers = response.headers
    assert 'sample_events.xlsx' in headers.get('content-disposition')
