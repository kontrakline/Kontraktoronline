from Helper import envHelper
from Constant import config_default


import requests
import logging
import json


class Microservice(object):

    _env        = None
    _url_redis  = None
    _url_token  = None
    _url_account= None
    _url_register= None
    _request    = None



    @classmethod
    def prepre(cls, paramRequest):
        logging.info("@---- Initialize Microservice ----")

        cls._env        = envHelper.getEnv()
        cls._url_token  = cls._env.TOKEN
        cls._url_account= cls._env.DB_MODULE_ACCOUNT
        cls._url_register = cls._env.DB_MODULE_ACCOUNT
        cls._request    = paramRequest

    @classmethod
    def getToken(cls):
        logging.info("@---- Microservice: getToken ----")

        headers = {"Content-type": "application/json"}
        request = {
            "function": "requestToken",
            "data": cls._request
        }

        logging.info("@ ---- Microservice: Send data ---- ")
        response = requests.post(url=cls._url_token, headers = headers, json= request  )
        response = response.json()

        return response

    @classmethod
    def getAccount(cls):
        logging.info("@---- Microservice: getAccount ----")

        headers = {"Content-type": "application/json"}
        request = {
            "function": "getAccountByUsernamePassword",
            "data": cls._request
        }

        # print(json.dumps(request))

        logging.info("@ ---- Microservice: Send data ---- ")
        response = requests.post(url=cls._url_account, headers=headers, json=request)
        response = response.json()

        return response

    @classmethod
    def register(cls):
        logging.info("@--- Microservice: register ----")

        headers = {"Content-type": "application/json"}
        request = {
            "function": "register",
            "data": cls._request
        }

        # print (json.dumps(request))

        logging.info("@ ---- Microservice: Send data ----")
        response = requests.post(url=cls._url_account, headers= headers, json=request)
        response = response.json()

        return  response