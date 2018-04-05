import logging
import json
from Route import RAccount
from Holder import HResponse
from Helper import ResponseHelper

def lambda_handler(event, context):

    function = event["function"]
    param    = event["data"]
    response = HResponse()

    try :
        command = getattr(RAccount(param), function)
        response = command()
    except Exception as e :
        print(e)

    return ResponseHelper.formatJSON(response)


if __name__ == "__main__" :
    param = {
        "function" : "changePassword",
        "data": {
          "account_email": "a@a.com",
          "account_password": "ooooo"
        }
    }
    # param_delete = {"function" : "deleteAccount", "data" : {"account_id" : 3}}
    print(lambda_handler(param, ""))

    # print(lambda_handler({"function" : "insertAccount", "data" : "[]"}))
    #
    # print(lambda_handler({"function" : "updateAccount", "data" : "[]"}))
    #
    # print(lambda_handler({"function" : "deleteAccount", "data" : "[]"}))