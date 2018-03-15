import logging
from Util import UDb

class AccountController(object):
    _requestParam = {}

    @classmethod
    def prepare(cls, requestParam):
        cls._requestParam = requestParam

    @classmethod
    def getAccount(cls):
        logging.info("@----Controller : getAccount ----")

        sql = "select " \
              "ta.account_id, " \
              "ta.account_username, " \
              "ta.account_email, " \
              "ta.account_phone, " \
              "tl.level_id, " \
              "tl.level_name " \
              "from tbl_account ta, tbl_level tl " \
              "where ta.account_level_id = tl.level_id"

        if cls._requestParam.get("account_id") is not None :
            sql = sql + " and ta.account_id = " + str(cls._requestParam.get("account_id"))

        return UDb.executeSelect(sql)

    @classmethod
    def updateAccount(cls):
        logging.info("@----Controller : updateAccount ----")

        sql = "update tbl_account set "

        for field in cls._requestParam:
            if field == "account_id":
                continue

            sql = sql + field + " = '" + cls._requestParam.get(field)+ "' "

        sql = sql+" where account_id = " + str(cls._requestParam.get("account_id"))

        return UDb.executeUpdate(sql)

    @classmethod
    def insertAccount(cls):
        logging.info("@----Controller : insertAccount ----")
        sql = "insert into " \
              "tbl_account(account_level_id, account_username, account_password, account_email, account_phone, account_address_id) " \
              "values" \
              "('"+str(cls._requestParam.get("account_level_id"))+"', '"\
              +str(cls._requestParam.get("account_username"))+"', '"\
              +str(cls._requestParam.get("account_password"))+"', '"\
              +str(cls._requestParam.get("account_email"))+"', '"\
              +str(cls._requestParam.get("account_phone"))+"', "\
              +str(cls._requestParam.get("account_address_id"))+")"
        return UDb.executeInsert(sql)

    @classmethod
    def deleteAccount(cls):
        logging.info("@----Controller : deleteAccount ----")
        return UDb.executeDelete("delete from tbl_account where account_id = "+str(cls._requestParam.get("account_id")))