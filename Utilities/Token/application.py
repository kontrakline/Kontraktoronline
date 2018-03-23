import logging
import json
from Route import RToken
from Holder.HResponse import HResponse
from Helper import ResponseHelper

def lambda_handler(event, context):

    function = event["function"]
    param    = event["data"]
    response = HResponse()

    try :
        command = getattr(RToken(param), function)
        response = command()
    except Exception as e :
        print(e)

    return ResponseHelper.formatJSON(response)


# if __name__ == "__main__" :
#     # param = {"function": "encodeToken", "data": {"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2NvdW50X2lkIjoxfQ.IpRROKVMnIOoJOGLJH3I6-OBTkqreWGQlxfPoJVKeas"}}
#     param = {"function": "requestToken", "data": {"ipAddress" : "192.168.0.1", "imei" : "", "email" : "admin@admin.com"}}
#     print(lambda_handler(param))