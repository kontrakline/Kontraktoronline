from Helper import TokenHelper
from Holder import HResponse
from Holder import HSessionRequest
from Service import SRedis
from Helper import ResponseHelper
import json

class TokenController(object) :

    _request = None

    @classmethod
    def prepare(cls, paramRequest):
        cls._request = paramRequest

    @classmethod
    def generateToken(cls):
        response = HResponse()

        # Step 1
        #
        # Validasi parameter

        if cls._request.get("ipAddress") and cls._request.get("imei") is None : return ResponseHelper.generateResponseFail()
        if cls._request.get("email") is None : return ResponseHelper.generateResponseFail()

        # Step 2
        #
        # Generate Token
        response = TokenHelper.encode(cls._request)
        token = response.getData().get("data")

        # Step 3
        #
        # Caching to redis

        hsession = HSessionRequest()
        hsession.Data = token
        if cls._request.get("ipAddress") is not None :
            hsession.Key = cls._request.get("ipAddress")
        else :
            hsession.Key = cls._request.get("imei")


        sredis = SRedis()
        sredisResponse = json.loads(json.dumps(sredis.createSession(hsession)))
        print(sredisResponse)

        if not sredisResponse.get("status") :
            return ResponseHelper.generateResponseFail()


        return ResponseHelper.generateResponseSuccess(token)