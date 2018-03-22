import jwt
import json
from Holder.HResponse import HResponse

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
        try :
            token = jwt.encode(cls._request, "123456789987654321", algorithm="HS256")

            if token :
                return cls._generateResponseSuccess(token)
            else :
                return cls._generateResponseFail()
        except Exception as e :
            print(e)
            return cls._generateResponseFail()

    @classmethod
    def _decode(cls, paramToken):

        try :
            data = jwt.decode(paramToken, "123456789987654321", algorithm="HS256")

            if data:
                return cls._generateResponseSuccess(data)
            else:
                return cls._generateResponseFail()
        except Exception as e :
            print(e)
            return cls._generateResponseFail()


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
    def _generateResponseFail(cls):
        response = HResponse()

        response.StatusCode = 500
        response.Status = False
        response.Data = {"data": ""}
        return response