import json
import logging
import time

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

        return "Please Sign in First"

    @classmethod
    def getSignout(cls):
        logging.info("@----Controller : getSignout ----")

        return "You Already Sign out From this Site"