__author__ = 'wing'
import json
import os

SETTING_METHOD_JSON = 'json'
SETTING_METHOD_MONGO = 'mongodb'
KEY_NAME = 'key'
VALUE_NAME = 'value'


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


class PyEasySettingMongo(PyEasySetting):
    def __init__(self, host='localhost', port=27017, db='Settings', collection='PyEasySetting',
                 user=None, password=None):
        import pymongo

        super(PyEasySettingMongo, self).__init__(method=SETTING_METHOD_MONGO)

        self.mongoCon = pymongo.MongoClient(host, port)
        mdb = self.mongoCon[db]
        if user is not None:
            mdb.authenticate(user, password)
        self.collection = mdb[collection]
        self._prepare()

    def _prepare(self):
        index_name = 'ezs_key'
        if index_name not in self.collection.index_information():
            self.collection.create_index(KEY_NAME, name=index_name, unique=True)

    def get(self, key, default=None):
        v = self.collection.find_one({KEY_NAME: key})
        if v is None:
            return default
        else:
            return v['value']

    def set(self, key_or_object, value=None, save=True):
        if isinstance(key_or_object, str):
            self.collection.update({KEY_NAME: key_or_object}, {KEY_NAME: key_or_object, VALUE_NAME: value}, upsert=True)
        elif isinstance(key_or_object, dict):
            for k, v in key_or_object.items():
                self.set(k, v, save=save)

    def all(self):
        v = {}
        for i in self.collection.find({}):
            v[i[KEY_NAME]] = i[VALUE_NAME]

        return v
