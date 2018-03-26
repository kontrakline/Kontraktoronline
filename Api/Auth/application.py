import logging
import json
from Route import RAuth
from Holder import HResponse
from Helper import ResponseHelper

def lambda_handler(pParam):

    function = pParam["function"]
    param = pParam["data"]
    response = HResponse()

    try:
        command = getattr(RAuth(param), function)
        response = command()
    except Exception as e:
        print(e)

    print (response)
    print ("##########################")
    return ResponseHelper.formatJSON(response)

if __name__ == "__main__" :
    param = {"function": "getSignin", "data": {"ipAddress" : "192.168.0.1", "imei" : "", "email" : "admin@admin.com", "username" : "kaes", "password" : "123456"}}

    print(lambda_handler(param))