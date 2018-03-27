import json
import logging
import sys

from Constant import config_staging


class envHelper(object):

    _config = 'config_staging'


    @classmethod
    def getEnv(cls):
        config = cls._config
        indetifier = getattr(sys.modules[__name__], config)

        return indetifier

    @classmethod
    def checkEnv(cls):
        return cls.__config