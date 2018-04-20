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
    param = {"function": "getVendorList", "data": {"email" : "admin@admin.com", "longitude" : "-6.0123874", "latitude" : "104.072364"}}

    print (lambda_handler(param,""))