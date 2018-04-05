import redis
from Holder import HResponse
from Helper import ResponseHelper

class URedis(object):

    _client = None

    @classmethod
    def prepare(cls):
        return False

    @classmethod
    def _openConnection(cls):
        cls._client = redis.Redis(host='redis-kontraktor.kegxid.ng.0001.apse1.cache.amazonaws.com', port=6379, db=0)

    @classmethod
    def getKey(cls, redisHolder):
        cls._openConnection()
        response = HResponse()

        try :
            result = cls._client.get(redisHolder.Key)

            if not result :
                response = ResponseHelper.generateResponseFail()
            else :
                response = ResponseHelper.generateResponseSuccess(result)
        except Exception as e :
            response = ResponseHelper.generateResponseFail()
        return response.toJSON()

    @classmethod
    def addKey(cls, redisHolder):
        cls._openConnection()

        response = HResponse()
        try :
            result = cls._client.set(redisHolder.Key, redisHolder.Data)
            response = ResponseHelper.generateResponseSuccess(result)
        except Exception as e :
            response = ResponseHelper.generateResponseFail()
        return response.toJSON()

    @classmethod
    def updateKey(cls):
        return False

    @classmethod
    def deleteKey(cls, redisHolder):
        response = HResponse()

        try:
            result = cls._client.delete(redisHolder.Key)
            response = ResponseHelper.generateResponseSuccess(result)
        except Exception as e :
            response = ResponseHelper.generateResponseFail()
        return response.toJSON()