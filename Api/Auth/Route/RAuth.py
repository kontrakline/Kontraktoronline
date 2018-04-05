import logging
from Controller import AuthController
from Helper import RequestHelper

class RAuth(object):

    def __init__(self, requestParam):
        logging.info("@--Router--")
        AuthController.prepare(RequestHelper.parseRequest(requestParam))



    def getLogin(self):
        logging.info("@ - - getLogin")

        return AuthController.getLogin()

    def getSignout(self):
        logging.info("@ - - getSignout")
        ## clear redis
        return AuthController.getSignout()

    def getRegister(self):
        logging.info("@ - - getRegister")

        return AuthController.getRegister()

    def changePassword(self):
        logging.info("@ - - changePassword")

        return  AuthController.changePassword()
