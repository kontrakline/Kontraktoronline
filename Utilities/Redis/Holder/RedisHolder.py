class RedisHolder(object):

    def __init__(self):
        self._key = None
        self._data = None


    def getKey(self):
        return self._key

    @property
    def Key(self):
        return self._key

    @property.setter
    def Key(self, paramKey):
        self._key = paramKey

    #=================

    def getData(self):
        return self._data

    @property
    def Data(self):
        return self._data

    @property.setter
    def Data(self, paramData):
        self._data = paramData