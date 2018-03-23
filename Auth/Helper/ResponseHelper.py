import json

class ResponseHelper(object):

    @classmethod
    def formatJSON(cls, holder):

        result = {
            "status" : holder.getStatus(),
            "statusCode" : holder.getStatusCode(),
            "data" : holder.getData()
        }

        return json
