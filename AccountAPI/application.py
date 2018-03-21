import logging
import json
from Route import RAccount
from Holder import HResponse

def lambda_handler(pParam):

    function = pParam["function"]
    param = pParam["data"]
    response = HResponse()

    try:
        command = getattr(RAccount(param), function)
        response = command()
    except Exception as e:
        print(e)

    return json.dumps(response.getData())

if __name__ == "__main__" :
    param = {"function": "getAccount", "data": {"account_id":  ""}}
    # param_insert = {
    #     "function": "insertAccount",
    #     "data": {
    #         }
    # }
    # param_delete = {"function": "deleteAccount", "data": {"account_id": 3}}
    print(lambda_handler(param))