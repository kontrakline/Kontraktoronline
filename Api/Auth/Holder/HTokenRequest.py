class HTokenRequest(object):

    def __init__(self):
        self._ipAddress = ""
        self._imei=""
        self._email = ""

    #---------------------------------
    def getipAddress(self):
        return self.IpAddress

    @property
    def IpAddress(self):
        return self._ipAddress

    @IpAddress.setter
    def IpAddress(self, value):
        self._ipAddress = value
    #---------------------------------

    #---------------------------------
    def getImei(self):
        return self.Imei

    @property
    def Imei(self):
        return self._imei

    @Imei.setter
    def Imei(self, value):
        self._imei = value
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