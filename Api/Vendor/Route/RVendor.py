import logging
from Controller import VendorController
from Helper import  RequestHelper



class Rvendor(object):

    def __init__(self, requestParam):
        logging.info("@----Router---")
        VendorController.prepare(RequestHelper.parseRequest(requestParam))

    def getVendorRecom(self):
        logging.info("@ - - getVendorRecom")
        ###checking redis
        return VendorController.getVendorById()