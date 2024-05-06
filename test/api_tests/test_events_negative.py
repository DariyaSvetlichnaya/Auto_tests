import test.api_tests.conftest


def test_create_event_without_scanners(get_event_body_without_scanners):

    response = test.api_tests.conftest.events_api.create_events(body=get_event_body_without_scanners)

    assert response.status_code == 422
    assert 'ensure this value has at least 1 items' in response.json()['detail'][0]['msg']


def test_create_event_end_before_start(get_event_body_end_before_start):

    response = test.api_tests.conftest.events_api.create_events(body=get_event_body_end_before_start)

    assert response.status_code == 422
    assert 'Reporting End is before the Reporting Start' in response.json()['detail'][0]['msg']


def test_create_event_start_after_end(get_event_body_start_after_end):

    response = test.api_tests.conftest.events_api.create_events(body=get_event_body_start_after_end)

    assert response.status_code == 422
    assert 'Reporting End is before the Event Date' in response.json()['detail'][0]['msg']


def test_delete_event_with_incorrect_id():
    response = test.api_tests.conftest.events_api.delete_wrong_event()
    assert response.status_code == 404
