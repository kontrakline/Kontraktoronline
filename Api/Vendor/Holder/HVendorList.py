import json

class HVendorList(object):

    def __init__(self):
        self._email = ""

    # ---------------------------------

    def getEmail(self):
        return self.Email

    @property
    def Email(self):
        return self._email

    @Email.setter
    def Email(self, value):
        self._email = value
    # ---------------------------------

    def toJSON(self):
        result = {

            "account_email" : self.Email

        }

        return json.loads(json.dumps(result, sort_keys=True, indent=4, separators=(',', ': ')))