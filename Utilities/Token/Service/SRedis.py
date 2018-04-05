import requests
import logging
from Constant import config_prod

class SRedis(object):

    def __init__(self):
        self._env_url = config_prod.REDIS_URL
        self._env_header = {"Content-type": "application/json"}
        return

    def createSession(self, htokenRequest):
        logging.info("@---- SRedis: cacheToken ----")


        request = {
            "function": "createSession",
            "data": htokenRequest.toJSON()
        }

        logging.info("@ ---- Microservice: Send data ---- ")
        response = requests.post(url=self._env_url, headers=self._env_header, json=request)
        response = response.json()

        return response