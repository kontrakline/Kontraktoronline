import json
import logging
import time
from Holder import HTokenRequest
from Helper import ResponseHelper

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
        request = HTokenRequest()
        response = ResponseHelper()


        request.IpAddress = "192.168.0.1"
        request.Imei = ""
        request.Email = ""

        # hit Utilities Token
        # checkToken = getToken(request)
        # get True or False

        return response

    @classmethod
    def getSignout(cls):
        logging.info("@----Controller : getSignout ----")

        return "You Already Sign out From this Site"