import json

class ResponseHelper(object):

    @classmethod
    def formatJSON(cls, holder):

        result = {
            "status" : holder.getStatus(),
            "statusCode" : holder.getStatusCode(),
            "data" : holder.getData()
        }

        return json.loads(json.dumps(result, sort_keys=True, indent=4, separators=(',', ': ')))

    @classmethod
    def generateResponseSuccess(cls):
        return ""

    @classmethod
    def generateResponseFailed(cls):
        return ""