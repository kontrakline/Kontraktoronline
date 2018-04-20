from Helper import envHelper
from Constant import config_default


import requests
import logging
import json


class Microservice(object):

    _env                = None
    _url_redis          = None
    _url_token          = None
    _url_login        = None
    _url_register       = None
    _url_changePassword = None
    _request            = None



    @classmethod
    def prepare(cls, paramRequest):
        logging.info("@---- Initialize Microservice ----")

        cls._env                = envHelper.getEnv()
        cls._url_token          = cls._env.TOKEN
        cls._url_login          = cls._env.DB_MODULE_ACCOUNT_NEW
        cls._url_register       = cls._env.DB_MODULE_ACCOUNT_NEW
        cls._url_changePassword = cls._env.DB_MODULE_ACCOUNT_NEW
        cls._request            = paramRequest

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
    def login(cls):
        logging.info("@---- Microservice: getAccount ----")

        headers = {"Content-type": "application/json"}
        request = {
            "function": "login",
            "data": cls._request
        }

        # print(json.dumps(request))

        logging.info("@ ---- Microservice: Send data ---- ")
        response = requests.post(url=cls._url_login, headers=headers, json=request)
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
        response = requests.post(url=cls._url_register, headers= headers, json=request)
        response = response.json()

        return  response

    @classmethod
    def changePassword(cls):
        logging.info("@ ---- Microservice : changePassword ----")

        headers = {"Content-type" : "application/json"}
        request = {
            "function": "changePassword",
            "data": cls._request
        }

        # print (json.dumps(request))

        logging.info("@ ---- Microservice: Send data ----")
        response = requests.post(url=cls._url_changePassword, headers = headers, json=request)
        response = response.json()

        return response