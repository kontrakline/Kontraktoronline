import logging
import json


from Holder import HResponse
from Helper import ResponseHelper


class VendorController(object):
    _requestParam = {}

    @classmethod
    def prepare(cls, requestParam):
        cls._requestParam = requestParam

    @classmethod
    def getVendorById(cls):

        logging.info ("@ ---- Controller:getVendorById ----")

        return "getVendorById"
