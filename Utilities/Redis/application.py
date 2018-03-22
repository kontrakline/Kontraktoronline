import logging
import json
from Route import RRedis
# from Holder.RedisHolder import RedisHolder
# from Helper import ResponseHelper

def lambda_handler(pParam):

    function = pParam["function"]
    param    = pParam["data"]
    response = False

    try :
        command = getattr(RRedis(param), function)
        response = command()
    except Exception as e :
        print(e)

    return response
    # return ResponseHelper.formatJSON(response)


if __name__ == "__main__" :
    # param = {"function": "encodeToken", "data": {"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2NvdW50X2lkIjoxfQ.IpRROKVMnIOoJOGLJH3I6-OBTkqreWGQlxfPoJVKeas"}}
    param = {"function": "getKey", "data": {"key" : "192.168.0.3", "data" : "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2NvdW50X2lkIjoxfQ.IpRROKVMnIOoJOGLJH3I6-OBTkqreWGQlxfPoJVKeas"}}
    print(lambda_handler(param))