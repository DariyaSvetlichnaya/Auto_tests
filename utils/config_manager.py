import os
import configparser

from os import path

ROOT_PATH = path.dirname(path.dirname(path.abspath(__file__)))

_config_path = path.join(ROOT_PATH, 'config_ui_test.ini')

_config = configparser.RawConfigParser()
_config.read(_config_path)


class ConfigManager:

    url = _config.get(section: 'app_data', option: 'BASE_URL')



