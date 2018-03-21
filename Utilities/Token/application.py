import logging
import json
from Route import RToken
from Holder.HResponse import HResponse
from Controller import TokenController

def lambda_handler(pParam):

    function = pParam["function"]
    param    = pParam["data"]
    response = HResponse()

    try :
        command = getattr(RToken(param), function)
        response = command()
        print(response)
    except Exception as e :
        print(e)
        print("ASDASD")

    return "asdasd"


if __name__ == "__main__" :
    param = {"function": "requestToken", "data": {"account_id": 1}}
    lambda_handler(param)