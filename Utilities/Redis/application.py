from Route import RRedis
from Holder import HResponse

def lambda_handler(event, context):

    function = event["function"]
    param    = event["data"]
    response = HResponse()

    try :
        command = getattr(RRedis(param), function)
        response = command()
    except Exception as e :
        print(e)

    return response
    # return ResponseHelper.formatJSON(response)


# if __name__ == "__main__" :
#     # param = {"function": "encodeToken", "data": {"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2NvdW50X2lkIjoxfQ.IpRROKVMnIOoJOGLJH3I6-OBTkqreWGQlxfPoJVKeas"}}
#     param = {"function": "addKey", "data": {"key" : "192.168.0.3", "data" : "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2NvdW50X2lkIjoxfQ.IpRROKVMnIOoJOGLJH3I6-OBTkqreWGQlxfPoJVKeas"}}
#     print(lambda_handler(param))