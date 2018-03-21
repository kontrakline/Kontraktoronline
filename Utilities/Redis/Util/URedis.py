class URedis(object):

    _connection = None

    @classmethod
    def prepare(cls):
        return False

    @classmethod
    def _openConnection(cls):
        return False

    @classmethod
    def _closeConnection(cls):
        return False

    @classmethod
    def getKey(cls):
        return False

    @classmethod
    def addKey(cls, redisHolder):

        return False

    @classmethod
    def updateKey(cls):
        return False

    @classmethod
    def deleteKey(cls):
        return False