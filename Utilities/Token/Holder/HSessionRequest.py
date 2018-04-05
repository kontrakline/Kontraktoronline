import json

class HSessionRequest(object):

    def __init__(self):
        self._key = None
        self._data = None

    def getKey(self):
        return self.Key

    @property
    def Key(self):
        return self._key

    @Key.setter
    def Key(self, value):
        self._key = value


    def getData(self):
        return self.Data

    @property
    def Data(self):
        return self._data

    @Data.setter
    def Data(self, value):
        self._data = value

    def toJSON(self):
        result = {
            "key": self.getKey(),
            "data": self.getData()
        }

        return json.loads(json.dumps(result, sort_keys=True, indent=4, separators=(',', ': ')))