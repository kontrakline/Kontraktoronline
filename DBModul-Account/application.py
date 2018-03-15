import logging
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

    return response


if __name__ == "__main__" :
    print(lambda_handler({"function" : "insertAccount", "data" : []}))