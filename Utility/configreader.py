import configparser

from unicodedata import category


def read_config(category, key):
    config = configparser.ConfigParser()
    config.read('Configuration/config.ini')
    return config.get(category, key)
