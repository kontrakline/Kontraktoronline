import json

class RequestHelper(object) :

    @classmethod
    def parseRequest(cls, requestParam):
        return json.loads(json.dumps(requestParam))