import logging
import json
from Route  import Rvendor
from Holder import HResponse
from Helper import ResponseHelper

def lambda_handler(event, contex):

    function = event["function"]
    param = event["data"]
    response = HResponse()

    try:
        command = getattr(Rvendor(param), function)
        response = command()
    except Exception as e:
        print(e)

    print (response)
    print ("##########################")
    return ResponseHelper.formatJSON(response)

if __name__ == "__main__" :
    param = {"function": "getVendorRecomendation", "data": {"ipAddress" : "192.168.0.1", "imei" : "", "email" : "admin@admin.com", "username" : "admin2", "password" : "admin"}}

    print (lambda_handler(param,""))