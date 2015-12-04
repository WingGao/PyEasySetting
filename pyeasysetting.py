__author__ = 'wing'
import json
import os

SETTING_METHOD_JSON = 'json'


class PyEasySetting(object):
    _method = None

    def __init__(self, method=SETTING_METHOD_JSON):
        self._method = method


class PyEasySettingJSON(PyEasySetting):
    def __init__(self, path):
        super(PyEasySettingJSON, self).__init__(method=SETTING_METHOD_JSON)
        self.path = path
        if os.path.isfile(path):
            with open(path) as f:
                self._json = json.load(f)
        else:
            self._json = json.loads('{}')

    def get(self, key, default=None):
        return self._json.get(key, default)

    def set(self, key_or_object, value=None, save=True):
        if isinstance(key_or_object, str):
            self._json[key_or_object] = value
        elif isinstance(key_or_object, dict):
            self._json.update(key_or_object)

        if save:
            self._save()

    def _save(self):
        with open(self.path, 'w') as f:
            json.dump(self._json, f)
