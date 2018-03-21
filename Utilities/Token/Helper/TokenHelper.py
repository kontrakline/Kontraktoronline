import jwt

class TokenHelper(object):
    _request = None

    @classmethod
    def prepare(cls, paramRequest):
        cls._request = paramRequest

    @classmethod
    def encode(cls):
        return cls._encode()

    @classmethod
    def decode(cls, paramToken):
        return cls._decode(paramToken)

    @classmethod
    def _encode(cls):
        return jwt.encode({"id" : "1", "username" : "Admin"}, "123456789987654321", algorithm="HS256")

    @classmethod
    def _decode(cls, paramToken):
        return jwt.decode(paramToken, "123456789987654321", algorithm="HS256")

