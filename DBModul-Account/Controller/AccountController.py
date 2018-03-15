import logging
from Util import UDb

class AccountController(object):

    @classmethod
    def getAccount(cls):
        logging.info("@----Controller : getAccount ----")
        return UDb.executeSelect("select * from tbl_account")

    @classmethod
    def updateAccount(cls):
        logging.info("@----Controller : updateAccount ----")
        return UDb.executeUpdate("update tbl_account set account_username = 'admin2' where account_id = 7")

    @classmethod
    def insertAccount(cls):
        logging.info("@----Controller : insertAccount ----")
        return UDb.executeInsert("insert into tbl_account values(null, 1, 'admin', 'admin', 'admin@gmail.com', '081282123833', 1)")

    @classmethod
    def deleteAccount(cls):
        logging.info("@----Controller : deleteAccount ----")
        return UDb.executeDelete("delete from tbl_account where account_id = 7")