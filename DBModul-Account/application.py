import logging
from Route import RAccount

def lambda_handler(pParam):

    function = pParam["function"]
    data     = pParam["data"]

    try :
        command = getattr(RAccount(), function)
        response = command()

        print(response.getData())
    except Exception as e :
        print(e)

    return True


if __name__ == "__main__" :
    print(lambda_handler({"function" : "deleteAccount", "data" : []}))