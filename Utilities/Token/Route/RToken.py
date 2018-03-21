from Controller import TokenController

class RToken(object):

    def __init__(self, paramRequest):
        self._request = paramRequest

    def validateToken(self):
        TokenController.prepare(self._request)
        return TokenController.validateToken()

    def requestToken(self):
        TokenController.prepare(self._request)
        return TokenController.generateToken()

    def encodeToken(self):
        TokenController.prepare()
        return TokenController.extractToken()