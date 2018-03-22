from Util import URedis
from Holder import RedisHolder

class RedisController(object):
    _request = None

    @classmethod
    def prepare(cls, paramRequest):
        cls._request = paramRequest

    def checkToken(cls):
        token = cls.getKey(cls._request.get("key"))
        if not token :
            return False

        return True

    @classmethod
    def addKey(cls):
        redisHolder = RedisHolder()
        redisHolder.Key  = cls._request.get("key")
        redisHolder.Data = cls._request.get("data")
        return URedis.addKey(redisHolder)

    @classmethod
    def getKey(cls):
        redisHolder = RedisHolder()
        redisHolder.Key = cls._request.get("key")
        return URedis.getKey(redisHolder)

    @classmethod
    def deleteKey(cls):
        URedis.prepare()
        redisHolder = RedisHolder()
        redisHolder.Key(cls._request.get("key"))
        return URedis.deleteKey(redisHolder)

    @classmethod
    def updateKey(cls):
        URedis.prepare()
        redisHolder = RedisHolder()
        redisHolder.Key(cls._request.get("key"))
        return URedis.updateKey(redisHolder)