import json

class HLogin(object):

    def __init__(self):
        self._email = ""
        self._password = ""
        self._ipaddress = ""
        self._imei = ""


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

    # ----------------------------------
    def getPassword(self):
        return self.Password

    @property
    def Password(self):
        return  self._password

    @Password.setter
    def Password(self, value):
        self._password = value

    # ----------------------------------
    # ----------------------------------
    def getIpAddress(self):
        return self._ipaddress

    @property
    def IpAddress(self):
        return  self._ipaddress

    @IpAddress.setter
    def IpAddress(self, value):
        self._ipaddress = value

    # ----------------------------------
    # ----------------------------------
    def getImei(self):
        return self._imei

    @property
    def Imei(self):
        return self._imei

    @Imei.setter
    def Imei(self, value):
        self._imei = value

    # ----------------------------------

    def toJSON(self):
        result = {

            "account_email" : self.Email,
            "account_password" : self.Password,
            "account_ipaddress" : self.IpAddress,
            "account_imei" : self.Imei

        }

        return json.dumps(result)