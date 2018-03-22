from Helper import TokenHelper
from Holder import HResponse

class TokenController(object) :

    _request = None

    @classmethod
    def prepare(cls, paramRequest):
        cls._request = paramRequest

    @classmethod
    def extractToken(cls):
        return TokenHelper.decode(cls._request.get("token"))

    @classmethod
    def generateToken(cls):
        response = HResponse()

        TokenHelper.prepare(cls._request)

        response = TokenHelper.encode()

        token = response.getData().get("data")

        #Step caching to Redis



        return response

    @classmethod
    def validateToken(cls):
        validToken = URedis.checkToken(cls._request.get("ipAddress"))

        if not validToken : return False

        return True

