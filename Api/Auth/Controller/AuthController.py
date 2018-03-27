import json
import logging
import time
import requests

from Holder import HTokenRequest
from Holder import HSignin
from Holder import HRegister
from Holder import HResponse
from Helper import ResponseHelper
from Service import SCurl
from Service import Microservice

class AuthController(object):
    _requestParam = {}

    @classmethod
    def prepare(cls, requestParam):
        cls._requestParam = requestParam

    @classmethod
    def getAutoLogin(cls):
        logging.info("@----Controller : getAutoLogin ----")
        requestTokenParam = HTokenRequest()

        # Start
        # Step 1
        # Cheking Token to Redis

        reqeustSignInParam.Username = cls._requestParam.get("username")
        reqeustSignInParam.Password = cls._requestParam.get("password")
        reqeustSignInParam.Email = cls._requestParam.get("email")

        sendToRedisResponse = SCurl.sendRequest(requestSignInParam.toJson())
        sendToRedisResponse = json.load(sendToRedisResponse)

        if not sendToRedisResponse.get("Status") : return ResponseHelper.generateResponseFail()

        # End
        #
        # Step 1

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

        Microservice.prepre(json.loads(reqeustSignInParam.toJSON()))
        dbmodulResponse = Microservice.getAccount()
        dbmodulResponse = json.loads(json.dumps(dbmodulResponse))
        print (dbmodulResponse)

        if not dbmodulResponse.get("status") : return ResponseHelper.generateResponseFail()

        # End
        #
        # Step 1

        # Start
        # Step 2
        # Build Token param request
        requestTokenParam.IpAddress = cls._requestParam.get("ipAddress")
        requestTokenParam.Imei = cls._requestParam.get("imei")
        requestTokenParam.Email = dbmodulResponse.get("email")

        Microservice.prepre(json.loads(requestTokenParam.toJSON()))
        tokenResponse = Microservice.getToken()
        tokenResponse = json.loads(json.dumps(tokenResponse))

        if not tokenResponse.get("status"): return  ResponseHelper.generateResponseFail()

        # End
        #
        # Step 2

        # dbmodulResponse= {
        #     "StatusCode": 200 ,
        #     "Status": True,
        #     "Data": {
        #         "data": []
        #     }
        # }


        #Success
        return  ResponseHelper.generateResponseSuccess(dbmodulResponse.get("data"))

    @classmethod
    def getSignout(cls):
        logging.info("@----Controller : getSignout ----")

        return "You Already Sign out From this Site"

    @classmethod
    def getRegister(cls):
        logging.info("@----Controller : Register ----")

        requestsRegister= HRegister()


        # Step1
        #
        #Request to DB

        reqeustSignInParam.Username = cls._requestParam.get("username")
        reqeustSignInParam.Password = cls._requestParam.get("password")
        reqeustSignInParam.Email = cls._requestParam.get("email")

        Microservice.prepre(json.loads(requestsRegister.toJSON()))
        registerResponse = Microservice.register()
        registerResponse = json.loads(json.dumps(registerResponse))

        if not registerResponse.get("status"): return ResponseHelper.generateResponseFail()

        # End
        #
        # Step 2

        return "Success to Register your account"