import json

class HSignin(object):

    def __init__(self):
        self._username = ""
        self._password=""
        self._email = ""

    #---------------------------------
    def getUsername(self):
        return self.Username

    @property
    def Username(self):
        return self._username

    @Username.setter
    def Username(self, value):
        self._username = value
    #---------------------------------

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
            "account_username" : self.Username,
            "account_email" : self.Email,
            "account_password" : self.Password
        }

        return json.dumps(result)