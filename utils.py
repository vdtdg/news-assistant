import json


def get_key_from_config(key):
    config_path = "config.json"  # Note the hardcoded path of the config here. There are better ways to do this than that.
    with open(config_path) as config_file:
        config = json.load(config_file)

    return config[key]  # If the key doesn't exist, this will fire an exception.
