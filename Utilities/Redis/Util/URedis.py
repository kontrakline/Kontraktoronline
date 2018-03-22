import redis

class URedis(object):

    _client = None

    @classmethod
    def prepare(cls):
        return False

    @classmethod
    def _openConnection(cls):
        cls._client = redis.StrictRedis(host='localhost', port=6379, db=0)

    @classmethod
    def getKey(cls, redisHolder):
        cls._openConnection()
        response = False

        try :
            response = cls._client.get(redisHolder.Key)

            if not response :
                response = False
        except Exception as e :
            print(e)
        return response

    @classmethod
    def addKey(cls, redisHolder):
        cls._openConnection()

        response = False
        try :
            response = cls._client.set(redisHolder.Key, redisHolder.Data)
        except Exception as e :
            print(e)
        return response

    @classmethod
    def updateKey(cls):
        return False

    @classmethod
    def deleteKey(cls, redisHolder):
        response = False

        try:
            response = cls._client.delete(redisHolder.Key)
        except Exception as e :
            print(e)
        return response