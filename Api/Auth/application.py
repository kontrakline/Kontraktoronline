import logging
import json
from Route import RAuth
from Holder import HResponse
from Helper import ResponseHelper

def lambda_handler(event, contex):

    function = event["function"]
    param = event["data"]
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
    param = {"function": "getLogin", "data": { "email" : "rocket@yahoo.com", "password" : "1234567898", "ipAddress":"192301238", "imei":""}}

    print(lambda_handler(param, ""))