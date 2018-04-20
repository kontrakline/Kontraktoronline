import logging
import json


from Holder import HResponse
from Helper import ResponseHelper
from Holder import HVendorRecom
from Holder import HVendorList
from Holder import HVendorDetails
from Service import Microservice


class VendorController(object):
    _requestParam = {}

    @classmethod
    def prepare(cls, requestParam):
        cls._requestParam = requestParam


    @classmethod
    def getVendorRecomendation(cls):

        logging.info ("@ ---- Controller: getVendorRecomendation ----")
        print ("ABC")
        requestVendorParam = HVendorRecom

        # Step 1
        # get Param here
        requestVendorParam.Email    = cls._requestParam.get("email")
        requestVendorParam.Latitude = cls._requestParam.get("latitude")
        requestVendorParam.Longitude= cls._requestParam.get("longitude")

        if requestVendorParam.Email is None : return ResponseHelper.generateResponseFail()
        if requestVendorParam.Longitude or requestVendorParam.Longitude is None : return ResponseHelper.generateResponseFail()

        # connect to DB module
        Microservice.prepare(requestVendorParam.toJSON())

        # Response from Db
        dbmodulResponse = Microservice.getVendorRecom()


        # Response to Mobile


        # End


        return ResponseHelper.generateResponseSuccess({"data":"getVendorRecomendation"})

    @classmethod
    def getVendorList(cls):
        logging.info("@ ---- Controller: getVendorList ----")
        print("BCA")
        requestVendorParam = HVendorList()

        requestVendorParam.Email = cls._requestParam.get("email")

        if requestVendorParam.Email is None : return ResponseHelper.generateResponseFail()

        Microservice.prepare(requestVendorParam.toJSON())
        # dbmoduleResponse = Microservice.getVendorList()
        # dbmoduleResponse = json.loads(json.dumps(dbmoduleResponse))

        return ResponseHelper.generateResponseSuccess({"data": "getVendorList"})


    @classmethod
    def getVendorDetails(cls):
        logging.info("@ ---- Controller: getVendorDetails")
        print ("ACB")

        requestVendorParam = HVendorList()

        requestVendorParam.Email = cls._requestParam.get("email")

        if requestVendorParam.Email is None: return ResponseHelper.generateResponseFail()

        Microservice.prepare(requestVendorParam.toJSON())
        # dbmoduleResponse = Microservice.getVendorDetails()
        # dbmoduleResponse = json.loads(json.dumps(dbmoduleResponse))

        return ResponseHelper.generateResponseSuccess({"data": "getVendorDetails"})