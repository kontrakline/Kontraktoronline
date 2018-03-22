class RedisHolder(object):

    def __init__(self):
        self._key = None
        self._data = None


    def getKey(self):
        return self.Key

    @property
    def Key(self):
        return self._key

    @Key.setter
    def Key(self, paramKey):
        self._key = paramKey

    #=================

    def getData(self):
        return self.Data

    @property
    def Data(self):
        return self._data

    @Data.setter
    def Data(self, paramData):
        self._data = paramData