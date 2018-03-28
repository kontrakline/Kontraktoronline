from Controller import S3Controller

class Route(object):

    def __init__(self, requestParam):
        self._requestParam = requestParam


    def uploadImage(self):
        S3Controller.prepare(self._requestParam)
        return S3Controller.uploadImage()

    def uploadFile(self):
        return ""