import logging
from Controller import AccountController
from Helper import RequestHelper

class RAccount(object):

    def __init__(self, requestParam):
        logging.info("@--Router--")
        AccountController.prepare(RequestHelper.parseRequest(requestParam))


    def getAccount(self):
        logging.info("@--getAccount--")
        return AccountController.getAccount()

    def updateAccount(self):
        logging.info("@--updateAccount--")
        return AccountController.updateAccount()

    def insertAccount(self):
        logging.info("@--insertAccount--")
        return AccountController.insertAccount()

    def deleteAccount(self):
        logging.info("@--deketeAccount--")
        return AccountController.deleteAccount()