import logging
import json
from Route import RAccount
from Holder import HResponse

def lambda_handler(pParam):

    function = pParam["function"]
    param    = pParam["data"]
    response = HResponse()

    try :
        command = getattr(RAccount(), function)
        response = command()
    except Exception as e :
        print(e)

    return json.dumps(response.getData())


if __name__ == "__main__" :
    print(lambda_handler({"function" : "insertAccount", "data" : []}))