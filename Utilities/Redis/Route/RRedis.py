from Controller import RedisController

class RRedis(object):

    def __init__(self, paramRequest):
        self._request = paramRequest
        RedisController.prepare(self._request)

    def createSession(self):
        return RedisController.createSession()