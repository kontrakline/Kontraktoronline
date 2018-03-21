class HResponse(object):

    def __init__(self):
        self._errorCode = ""
        self._data=""

    #---------------------------------
    def getErrorCode(self):
        return self.ErrorCode

    @property
    def ErrorCode(self):
        return self._errorCode

    @ErrorCode.setter
    def ErrorCode(self, value):
        self._errorCode = value
    #---------------------------------

    #---------------------------------
    def getData(self):
        return self.Data

    @property
    def Data(self):
        return self._data

    @Data.setter
    def Data(self, value):
        self._data = value
    #---------------------------------