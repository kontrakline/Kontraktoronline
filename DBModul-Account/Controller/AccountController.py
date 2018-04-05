import logging
from Util import UDb
from Helper import ResponseHelper

class AccountController(object):
    _requestParam = {}

    @classmethod
    def prepare(cls, requestParam):
        cls._requestParam = requestParam

    @classmethod
    def loginByEmail(cls):
        logging.info("@----Controller : loginByByEmail ----")

        sql = "select " \
              "ta.account_id, " \
              "ta.account_username, " \
              "ta.account_password, " \
              "ta.account_email, " \
              "ta.account_phone, " \
              "tl.level_id, " \
              "tl.level_name " \
              "from tbl_account ta, tbl_level tl " \
              "where ta.account_level_id = tl.level_id"

        # Step 1
        #
        # Validasi parameter
        if cls._requestParam.get("account_email") is None : return ResponseHelper.generateResponseFailed()

        # Step 2
        #
        # Concat query
        sql = sql + " and ta.account_email = '" + str(cls._requestParam.get("account_email")) + "'"

        return UDb.executeSelect(sql)

    @classmethod
    def changePassword(cls):
        logging.info("@----Controller : changePassword ----")

        #Step 1
        #
        #Validasi parameter

        if cls._requestParam.get("account_password") is None : return ResponseHelper.generateResponseFailed()
        if cls._requestParam.get("account_email") is None    : return ResponseHelper.generateResponseFailed()

        #Step 2
        #
        #Concate query

        sql = "update tbl_account set account_password = '" + cls._requestParam.get("account_password") + "' " \
              "where account_email = '" + str(cls._requestParam.get("account_email")) + "'"

        print(sql)

        return UDb.executeUpdate(sql)

    @classmethod
    def registerAccount(cls):
        logging.info("@----Controller : registerAccount ----")

        # Step 1
        #
        # Validasi parameter

        if cls._requestParam.get("account_email") is None      : return ResponseHelper.generateResponseFailed()
        if cls._requestParam.get("account_password") is None   : return ResponseHelper.generateResponseFailed()

        # Step 2
        # account_level_id = 0 // new user
        # Concate query

        sql = "insert into " \
              "tbl_account(account_level_id, account_username, account_password, account_email, account_address_id) " \
              "values" \
              "(4, '" \
              + str(cls._requestParam.get("account_username")) + "', '" \
              + str(cls._requestParam.get("account_password")) + "', '" \
              + str(cls._requestParam.get("account_email")) + "', 0)"

        print(sql)

        return UDb.executeInsert(sql)