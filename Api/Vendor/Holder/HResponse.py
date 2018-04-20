class HResponse(object):

    def __init__(self):
        self._message = ""
        self._data = ""
        self._status = False

    # ---------------------------------

    def getMessage(self):
        return self.Message

    @property
    def Message(self):
        return self._message

    @Message.setter
    def Message(self, value):
        self._message = value

    # ---------------------------------

    # -----------------------------
    def getData(self):
        return self.Data

    @property
    def Data(self):
        return self._data

    @Data.setter
    def Data(self, value):
        self._data =  value

    # -----------------------------

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


