import logging
import json
from Route import RAuth
from Holder import HResponse

def lambda_handler(pParam):

    function = pParam["function"]
    param = pParam["data"]
    response = HResponse()

    try:
        command = getattr(RAuth(param), function)
        response = command()
    except Exception as e:
        print(e)

    return json.dumps(response)

if __name__ == "__main__" :
    param = {"function": "getSignin", "data": {"IP":  ""}}

    print(lambda_handler(param))