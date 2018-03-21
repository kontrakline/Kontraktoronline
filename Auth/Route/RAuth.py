import logging
from Controller import AuthController
from Helper import RequestHelper

class RAuth(object):

    def __init__(self, requestParam):
        logging.info("@--Router--")
        AuthController.prepare(RequestHelper.parseRequest(requestParam))

    def getAutoLogin(self):
        logging.info("@ - - getAutoLogin")
        ## cheking redis
        return AuthController.getAutoLogin()

    def getSignin(self):
        logging.info("@ - - getSiginin")
        ## cheking redis
        return AuthController.getSignin()

    def getSignout(self):
        logging.info("@ - - getSignout")
        ## clear redis
        return AuthController.getSignout()
