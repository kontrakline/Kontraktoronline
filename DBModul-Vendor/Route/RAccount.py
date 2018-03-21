from Controller import VendorController

class RAccount(object) :

    def __init__(self, requestParam):
        VendorController.prepare(requestParam)

    def getVendor(self):
        VendorController.getVendor()
        return ""

    def insertVendor(self):
        VendorController.insertVendor()
        return ""

    def deleteVendor(self):
        VendorController.deleteVendor()
        return ""

    def updateVendor(self):
        VendorController.updateVendor()
        return ""
