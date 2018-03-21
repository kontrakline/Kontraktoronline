from Helper import TokenHelper

class TokenController(object) :

    _request = None

    @classmethod
    def prepare(cls, paramRequest):
        cls._request = paramRequest

    @classmethod
    def extractToken(cls, paramToken):
        return TokenHelper.decode(paramToken)

    @classmethod
    def generateToken(cls):
        return TokenHelper.encode()

    @classmethod
    def validateToken(cls):
        validToken = URedis.checkToken(cls._request.get("ipAddress"))

        if not validToken : return False

        return True

