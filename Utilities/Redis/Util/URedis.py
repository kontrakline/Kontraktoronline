import redis
from Holder import HResponse

class URedis(object):

    _client = None

    @classmethod
    def prepare(cls):
        return False

    @classmethod
    def _openConnection(cls):
        cls._client = redis.StrictRedis(host='redis-kontraktor.kegxid.ng.0001.apse1.cache.amazonaws.com', port=6379, db=0)

    @classmethod
    def getKey(cls, redisHolder):
        cls._openConnection()
        response = HResponse()

        try :
            result = cls._client.get(redisHolder.Key)

            if not result :
                response = cls._generateResponseFailed()
            else :
                response = cls._generateResponseSuccess(result)
        except Exception as e :
            response = cls._generateResponseFailed()
        return response

    @classmethod
    def addKey(cls, redisHolder):
        cls._openConnection()

        response = HResponse()
        try :
            result = cls._client.set(redisHolder.Key, redisHolder.Data)
            response = cls._generateResponseSuccess(result)
        except Exception as e :
            response = cls._generateResponseFailed()
        return response

    @classmethod
    def updateKey(cls):
        return False

    @classmethod
    def deleteKey(cls, redisHolder):
        response = HResponse()

        try:
            result = cls._client.delete(redisHolder.Key)
            response = cls._generateResponseSuccess(result)
        except Exception as e :
            response = cls._generateResponseFailed()
        return response

    @classmethod
    def _generateResponseSuccess(cls, data):
        response = HResponse()

        try :
            responseData = data
            if type(data) is not dict:
                responseData = data.decode()

            response.StatusCode = 200
            response.Status = True
            response.Data = {"data": responseData}
            return response
        except Exception as e :
            print(e)
            return cls._generateResponseFail()

    @classmethod
    def _generateResponseFailed(cls):
        response = HResponse()

        response.StatusCode = 500
        response.Status = False
        response.Data = {"data": ""}
        return response