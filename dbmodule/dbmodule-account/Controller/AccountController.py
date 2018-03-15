

import logging
import time

class AccountController(object):

    _request   = None
    _result    = None
    _start     = None


    @classmethod
    def unset(cls):
        cls._request    = None
        cls._result     = None
        cls._start      = None


    @classmethod
    def handle(cls,request):
        