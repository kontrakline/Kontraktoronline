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
    def getVendorRecomendation(cls):

        logging.info ("@ ---- Controller: getVendorRecomendation ----")

        # Step 1

        # get Param here


        # connect to DB module


        # Response from Db


        # Response to Mobile


        # End





        return "getVendorRecomendation"