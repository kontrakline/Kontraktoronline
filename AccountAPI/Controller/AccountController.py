import json
import time

class AccountController(object):
    _requestParam = {}

    @classmethod
    def getAccount(cls):
        logging.info("@----Controller : getAccount ----")

        return "GetAccount"