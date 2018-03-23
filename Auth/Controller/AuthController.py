import json
import logging
import time
from Holder import HTokenRequest
from Holder import HSignin
from Holder import HResponse
from Helper import ResponseHelper
from Service import SCurl

class AuthController(object):
    _requestParam = {}

    @classmethod
    def prepare(cls, requestParam):
        cls._requestParam = requestParam

    @classmethod
    def getAutoLogin(cls):
        logging.info("@----Controller : getAutoLogin ----")

        return "Auto Login Success"

    @classmethod
    def getSignin(cls):
        logging.info("@----Controller : getSignin ----")
        requestTokenParam   = HTokenRequest()
        reqeustSignInParam  = HSignin()


        # Start
        # Step 1
        # Build DB Modul param request

        reqeustSignInParam.Username = cls._requestParam.get("username")
        reqeustSignInParam.Password = cls._requestParam.get("password")
        reqeustSignInParam.Email = cls._requestParam.get("email")

        # dbmodulResponse = SCurl.sendRequest(reqeustSignInParam.toJson())
        # dbmodulResponse = json.loads(dbmodulResponse)
        #
        # if not dbmodulResponse.get("Status") : return ResponseHelper.generateResponseFail()

        # End
        #
        # Step 1



        # Start
        # Step 2
        # Build Token param request
        requestTokenParam.IpAddress = cls._requestParam.get("ipAddress")
        requestTokenParam.Imei = cls._requestParam.get("imei")
        requestTokenParam.Email = cls._requestParam.get("email")

        # tokenResponse = SCurl.sendRequest(requestTokenParam.toJson())
        # tokenResponse = json.loads(tokenResponse)
        #
        # if not dbmodulResponse.get("Status"): return  ResponseHelper.generateResponseFail()

        # End
        #
        # Step 2

        dbmodulResponse= {
            "StatusCode": 200 ,
            "Status": True,
            "Data": {
                "data": []
            }
        }


        #Success
        return  ResponseHelper.generateResponseSuccess(dbmodulResponse.get("data"))

    @classmethod
    def getSignout(cls):
        logging.info("@----Controller : getSignout ----")

        return "You Already Sign out From this Site"