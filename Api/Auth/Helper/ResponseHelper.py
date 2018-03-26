import json
from Holder import HResponse

class ResponseHelper(object):

    @classmethod
    def formatJSON(cls, holder):

        result = {
            "status" : holder.getStatus(),
            "statusCode" : holder.getStatusCode(),
            "data" : holder.getData()
        }

        return json.dumps(result)

    @classmethod
    def generateResponseSuccess(cls, paramdata):

        response = HResponse()

        response.StatusCode = 200
        response.Status = True
        response.Data = {"data":paramdata}

        return response

    @classmethod
    def generateResponseFail(cls):

        response = HResponse()

        response.StatusCode = 500
        response.Status = False
        response.Data = {}

        return response


