import json
import logging
import time
import requests
import hashlib
import random

from Holder import HTokenRequest
from Holder import HLogin
from Holder import HRegisterReq
from Holder import HResponse
from Holder import HPassword
from Helper import ResponseHelper
from Service import SCurl
from Service import Microservice

class AuthController(object):
    _requestParam = {}

    @classmethod
    def prepare(cls, requestParam):
        cls._requestParam = requestParam


    @classmethod
    def getLogin(cls):

        logging.info("@----Controller : getSignin ----")
        requestTokenParam   = HTokenRequest()
        requestLoginParam  = HLogin()


        # Start
        # Step 1
        # Build DB Modul param request



        ### Cheking Param Exist
        requestLoginParam.Email     = cls._requestParam.get("email")
        requestLoginParam.Password  = hashlib.md5(cls._requestParam.get("password").encode("utf")).hexdigest()
        requestLoginParam.Imei      = cls._requestParam.get("imei")
        requestLoginParam.IpAddress = cls._requestParam.get("ipAddress")


        if requestLoginParam.Email or requestLoginParam.Password is None : return  ResponseHelper.generateResponseFail()

        ### End of cheking param process

        Microservice.prepre(requestLoginParam.toJSON())


        dbmodulResponse = Microservice.login()
        dbmodulResponse = json.loads(json.dumps(dbmodulResponse))




        if not dbmodulResponse.get("status") : return ResponseHelper.generateResponseFail()

        # compare the password
        password = json.loads(json.dumps(dbmodulResponse.get("data")))
        password = password[0].get("account_password")
        password = password[3::]



        if requestLoginParam.Password != password: return ResponseHelper.generateResponseFail()
        # End

        # Step 1

        # Start
        # Step 2
        # Build Token param request

        requestTokenParam.IpAddress = cls._requestParam.get("ipAddress")
        requestTokenParam.Imei      = cls._requestParam.get("imei")
        requestTokenParam.Email     = cls._requestParam.get("email")

        Microservice.prepre(requestTokenParam.toJSON())
        tokenResponse = Microservice.getToken()
        tokenResponse = json.loads(json.dumps(tokenResponse))

        if not tokenResponse.get("status"): return  ResponseHelper.generateResponseFail()

        # End
        #
        # Step 2

        userDetail = dbmodulResponse.get("data")[0]

        responseData = {}
        responseData["id"] = userDetail.get("account_id")
        responseData["nama"] = userDetail.get("account_username")
        responseData["email"] = userDetail.get("account_email")
        responseData["level_id"] = userDetail.get("level_id")
        responseData["level_name"] = userDetail.get("level_name")
        responseData["token"] = tokenResponse.get("data")



        #Success
        return  ResponseHelper.generateResponseSuccess(responseData)

    @classmethod
    def getSignout(cls):
        logging.info("@----Controller : getSignout ----")

        return "You Already Sign out From this Site"

    @classmethod
    def getRegister(cls):
        logging.info("@----Controller : Register ----")

        requestRegisterParam= HRegisterReq()
        response = HResponse()


        # Start
        # Step1
        # Request to DB

        ### Cheking Param Exist
        requestRegisterParam.Username = cls._requestParam.get("username")
        requestRegisterParam.Email = cls._requestParam.get("email")
        requestRegisterParam.Password = cls._requestParam.get("password")
        requestRegisterParam.Password = hashlib.md5(cls._requestParam.get("password").encode("utf")).hexdigest()
        requestRegisterParam.Password = str(random.randrange(100,999)) + str(requestRegisterParam.Password)


        if requestRegisterParam.Email or requestRegisterParam.Password is None : return ResponseHelper.generateResponseFail()

        ### End of cheking param process

        Microservice.prepre(requestRegisterParam.toJSON())
        registerResponse = Microservice.register()
        registerResponse = json.loads(json.dumps(registerResponse))
        print (registerResponse)
        print "----------"

        if not registerResponse.get("status"): return ResponseHelper.generateResponseFail()


        # Request to Method Login after succes
        # requestLoginParam = HLogin()
        # requestLoginParam.Email     = cls._requestParam.get("email")
        # requestLoginParam.Imei      = cls._requestParam.get("imei")
        # requestLoginParam.IpAddress = cls._requestParam.get("ipAddress")
        #
        # cls.prepare(requestLoginParam.toJSON())
        # cls.getLogin()


        # End
        #
        # Step 1

        return ResponseHelper.generateResponseSuccess({})



    @classmethod
    def changePassword(cls):
        logging.info ("@ ---- Controller : changePassword")

        requestPasswordParam =  HPassword()

        # Start
        # Step1
        # Request to DB

        ### Cheking Param Exist
        requestPasswordParam.Email = cls._requestParam.get("email")
        requestPasswordParam.Password  = cls._requestParam.get("password")
        requestPasswordParam.Password = hashlib.md5(cls._requestParam.get("password").encode("utf")).hexdigest()
        requestPasswordParam.Password = str(random.randrange(100,999)) + str(requestPasswordParam.Password)

        if not requestPasswordParam: return  ResponseHelper.generateResponseFail()

        ### End of cheking param process

        Microservice.prepre(requestPasswordParam.toJSON())
        changePasswordResponse = Microservice.changePassword()
        changePasswordResponse = json.loads(json.dumps(changePasswordResponse))
        print (changePasswordResponse)
        print "-------------"

        if not changePasswordResponse.get("status"): return ResponseHelper.generateResponseFail()

        # End
        #
        # Step 1

        return  ResponseHelper.generateResponseSuccess({})

