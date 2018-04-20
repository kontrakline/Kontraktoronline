import json

class HVendorRecom(object):

    def __init__(self):
        self._latitude = ""
        self._longitude = ""
        self._email = ""


    #-------------------------------------------
    def getLatitude(self):
        return  self.Latitude

    @property
    def Latitude(self):
        return self._latitude

    @Latitude.setter
    def Latitude(self, value):
        self._latitude = value

    #--------------------------------------------

    def getLongitude(self):
        return self.Longitude

    @property
    def Longitude(self):
        return self._longitude

    @Longitude.setter
    def Longitude(self, value):
        self._longitude = value

    #---------------------------------------------

    def getEmail(self):
        return  self.Email

    @property
    def Email(self):
        return  self._email

    @Email.setter
    def Email(self, value):
        self._email = value

    #----------------------------------------------

    def toJSON(self):
        result = {
            "longitude": self.Longitude,
            "latitude": self.Latitude,
            "id": self.Email
        }

        return json.loads(json.dumps(result, sort_keys=True, indent=4, separators=(',', ': ')))


