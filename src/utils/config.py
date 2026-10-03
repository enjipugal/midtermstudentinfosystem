import json
import os


class Config:
    def __init__(self, config_file='config/config.json'):
        self.config_file = config_file
        self.settings = self._load_config()

    def _load_config(self):
        try:
            with open(self.config_file, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def get(self, key, default=None):
        return self.settings.get(key, default)
    