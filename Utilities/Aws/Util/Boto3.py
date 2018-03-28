from Constant import config_staging
import boto3
import base64

class Boto3(object) :

    @classmethod
    def prepare(cls, img_base64):
        cls._img_base64 = img_base64
        cls._bucketName = config_staging.AWS_BUCKET
        return ""

    @classmethod
    def _openConnection(cls):
        try :
            cls._client = boto3.client('s3', aws_access_key_id      =config_staging.AWS_ACCESS_KEY,
                                             aws_secret_access_key  =config_staging.AWS_SECRET_KEY,
                                             region_name            =config_staging.AWS_DEFAULT_REGION)
        except Exception as e:
            print(e)

    @classmethod
    def uploadImage(cls):

        try :
            cls._openConnection()

            img_base64 = base64.b64decode(cls._img_base64)

            cls._client.put_object(Body         =img_base64,
                                   Bucket       =cls._bucketName,
                                   Key          ="images/profile/(vendorid)",
                                   CacheControl ='no-store, no-cache, must-revalidate, post-check=0, pre-check=0',
                                   ContentType  ='image/jpg',
                                   ACL          ='public-read')
        except Exception as e :
            print(e)

        return ""

    @classmethod
    def uploadFile(cls):
        return ""