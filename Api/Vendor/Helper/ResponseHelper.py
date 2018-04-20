import json
from Holder import HResponse

class ResponseHelper(object):

    @classmethod
    def formatJSON(cls, holder):

        result = {
            "status" : holder.getStatus(),
            "message" : holder.getMessage(),
            "data" : holder.getData()
        }

        return json.loads(json.dumps(result, sort_keys=True, indent=4, separators=(',', ': ')))

    @classmethod
    def generateResponseSuccess(cls, paramdata):

        response = HResponse()

        response.Message = ("")
        response.Status = True
        response.Data = paramdata

        return response

    @classmethod
    def generateResponseFail(cls):

        response = HResponse()

        response.Message = ("Fail")
        response.Status = False
        response.Data = {}

        return response


