import json
import logging
import time

class AccountController(object):
    _requestParam = {}

    @classmethod
    def prepare(cls, requestParam):
        cls._requestParam = requestParam

    @classmethod
    def getAccount(cls):
        logging.info("@----Controller : getAccount ----")

        return "GetAccount"

    @classmethod
    def insertAccount(cls):
        logging.info("@----Controller : insertAccount ----")

        return "insertAccount"

    @classmethod
    def updateAccount(cls):
        logging.info("@----Controller : updateAccount ----")

        return "updateAccount"

    @classmethod
    def deleteAccount(cls):
        logging.info("@----Controller : deleteAccount ----")

        return "deleteAccount"