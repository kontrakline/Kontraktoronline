from Controller import RedisController

class RRedis(object):

    def __init__(self, paramRequest):
        self._request = paramRequest

    def addKey(self):
        RedisController.prepare(self._request)
        return RedisController.addKey()

    def getKey(self):
        RedisController.prepare(self._request)
        return RedisController.getKey()