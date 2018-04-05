from Controller import TokenController

class RToken(object):

    def __init__(self, paramRequest):
        self._request = paramRequest
        TokenController.prepare(self._request)

    def requestToken(self):
        return TokenController.generateToken()