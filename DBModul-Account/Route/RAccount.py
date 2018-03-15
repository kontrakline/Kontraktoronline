import logging
from Controller import AccountController

class RAccount(object):

    def __init__(self):
        logging.info("@--Router--")


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