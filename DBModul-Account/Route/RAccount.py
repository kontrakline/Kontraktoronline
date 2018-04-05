import logging
from Controller import AccountController
from Helper import RequestHelper

class RAccount(object):

    def __init__(self, requestParam):
        logging.info("@--Router--")
        AccountController.prepare(RequestHelper.parseRequest(requestParam))


    def login(self):
        logging.info("@--login--")
        return AccountController.loginByEmail()

    def changePassword(self):
        logging.info("@--changePassword--")
        return AccountController.changePassword()

    def register(self):
        logging.info("@--register--")
        return AccountController.registerAccount()

