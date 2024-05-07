import configparser
from os import path

ROOT_PATH = path.dirname(path.dirname(path.abspath(__file__)))

_config_path = path.join(ROOT_PATH, 'config_api_test.ini')

_config = configparser.RawConfigParser()
_config.read(_config_path)


class ConfigManager:

    all_events_url = _config.get('events_url', 'ALL_EVENTS_URL')
    create_events_url = _config.get('events_url', 'CREATE_EVENTS_URL')
    delete_event_url = _config.get('events_url', 'DELETE_EVENTS_URL')
    delete_wrong_event_url = _config.get('events_url', 'DELETE_WRONG_EVENT_URL')
    event_by_id_url = _config.get('events_url', 'GET_EVENT_BY_ID_URL')
    events_sample_file_url = _config.get('events_url', 'GET_EVENTS_SAMPLE_FILE_URL')
