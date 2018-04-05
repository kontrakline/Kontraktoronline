import json

class HPassword(object):

    def __init__(self):
        self._password=""
        self._email = ""


    #---------------------------------
    def getPassword(self):
        return self.Password

    @property
    def Password(self):
        return self._password

    @Password.setter
    def Password(self, value):
        self._password = value
    #---------------------------------

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
            "account_email" : self.Email,
            "account_password" : self.Password
        }

        return json.dumps(result)