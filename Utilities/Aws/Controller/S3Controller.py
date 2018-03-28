import base64
from Util import Boto3

class S3Controller(object) :

    @classmethod
    def prepare(cls, requestParam):
        cls._requestParam = requestParam

    @classmethod
    def uploadImage(cls):
        Boto3.prepare(cls._requestParam.get("image"))
        Boto3.uploadImage()
        return ""

    @classmethod
    def uploadFile(cls):
        return ""