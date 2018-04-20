from Helper import envHelper
# from Constant import config_default


import requests
import logging
import json


class Microservice(object):

    _env                = None
    _url_redis          = None
    _url_token          = None
    _url_vendorrecom    = None
    _url_vendordetails  = None
    _url_vendorlist     = None
    _request            = None


    @classmethod
    def prepare(cls, paramRequest):
        logging.info("@---- Initialize Microservice ----")

        cls._env                = envHelper.getEnv()
        cls._url_token          = cls._env.TOKEN
        cls._url_login          = cls._env.DB_MODULE_VENDOR
        cls._url_vendorrecom    = cls._env.DB_MODULE_VENDOR
        cls._url_vendordetails  = cls._env.DB_MODULE_VENDOR

        cls._request            = paramRequest

    @classmethod
    def getVendorRecom(cls):
        logging.info("@---- Microservice: getVendorRecom ----")

        headers = {"Content-type": "application/json"}
        request = {
            "function": "vendorRecomendation",
            "data": cls._request
        }

        logging.info("@ ---- Microservice: Send data ---- ")
        response = requests.post(url=cls._url_vendorrecom, headers=headers, json=request)
        response = response.json()

        return response

    @classmethod
    def getVendorDetails(cls):
        logging.info("---- Microservice: getVendorDetails ----")

        headers = {"Content-type": "application/json"}
        request = {
            "function":"vendorDetails",
            "data": cls._request
        }

        logging.info("@ ---- Mircoservice: Send data ----")
        response = requests.post(url=cls._url_vendordetails, headers= headers, json= request)
        response = response.json()

        return response

    @classmethod
    def getVendorList(cls):
        logging.info("---- Microservice: getVendorList ----")
        print ("BBBBBB")

        headers = {"Content-type": "application/json"}
        request = {
            "function":"vendorList",
            "data": cls._request
        }
        logging.info("@ ---- Microservice: Send data ----")
        response = requests.post(url=cls._url_vendorlist, headers = headers, json = request)
        response = response.json()

