import logging
import json
from Route import RAccount
from Holder import HResponse

def lambda_handler(pParam):

    function = pParam["function"]
    param    = pParam["data"]
    response = HResponse()

    try :
        command = getattr(RAccount(param), function)
        response = command()
    except Exception as e :
        print(e)


    return json.dumps(response.getData())


if __name__ == "__main__" :
    param = {"function" : "getAccount", "data" : {"account_id" : 1}}
    param_insert = {
        "function" : "insertAccount",
        "data" : {
            "account_level_id" : 1,
            "account_username" : "admin",
            "account_password" : "admin",
            "account_email" : "admin2@gmail.com",
            "account_phone" : "0812382341234",
            "account_address_id" : 1}}
    param_delete = {"function" : "deleteAccount", "data" : {"account_id" : 3}}
    print(lambda_handler(param))

    # print(lambda_handler({"function" : "insertAccount", "data" : "[]"}))
    #
    # print(lambda_handler({"function" : "updateAccount", "data" : "[]"}))
    #
    # print(lambda_handler({"function" : "deleteAccount", "data" : "[]"}))