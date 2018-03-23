class HResponse(object):

    def __init__(self):
        self._statusCode = ""
        self._data=""
        self._status = False

    #---------------------------------
    def getStatusCode(self):
        return self.StatusCode

    @property
    def StatusCode(self):
        return self._statusCode

    @StatusCode.setter
    def StatusCode(self, value):
        self._statusCode = value
    #---------------------------------

    #---------------------------------
    def getStatus(self):
        return self.Status

    @property
    def Status(self):
        return self._status

    @Status.setter
    def Status(self, value):
        self._status = value
    #---------------------------------

    # ---------------------------------
    def getData(self):
        return self.Data

    @property
    def Data(self):
        return self._data

    @Data.setter
    def Data(self, value):
        self._data = value
    # ---------------------------------