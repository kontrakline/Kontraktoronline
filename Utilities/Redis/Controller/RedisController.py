from Util import URedis
from Holder import HRedis

class RedisController(object):
    _request = None

    @classmethod
    def prepare(cls, paramRequest):
        cls._request = paramRequest

    @classmethod
    def createSession(cls):
        redisHolder = HRedis()
        redisHolder.Key  = cls._request.get("key")
        redisHolder.Data = cls._request.get("data")
        return URedis.addKey(redisHolder)