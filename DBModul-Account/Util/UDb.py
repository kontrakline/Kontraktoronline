import logging

from Constant import Config
from Holder import HResponse

import pymysql.cursors

class UDb(object):
    _connection = None
    _config = Config.config_prod
    _databaseType = ""
    _sql = ""
    _result = ""
    _response = None

    @classmethod
    def _openConnection(cls):
        response = 0
        if cls._databaseType == "slave" :
            try:
                cls._connection = pymysql.connect(host          =cls._config.DATABASE_HOST,
                                                  user          =cls._config.DATABASE_USER,
                                                  password      =cls._config.DATABASE_PASSWORD,
                                                  db            = cls._config.DATABASE_NAME,
                                                  port          = cls._config.DATABASE_PORT,
                                                  charset      = 'utf8mb4',
                                                  cursorclass    = pymysql.cursors.DictCursor)
                response = 1
            except Exception as e:
                logging.error("@--UDb openConnection Slave -- : " + str(e))
        else :
            try:
                cls._connection = pymysql.connect(host          =cls._config.DATABASE_HOST,
                                                  user          =cls._config.DATABASE_USER,
                                                  password      =cls._config.DATABASE_PASSWORD,
                                                  db            =cls._config.DATABASE_NAME,
                                                  port          =cls._config.DATABASE_PORT,
                                                  charset      ='utf8mb4',
                                                  cursorclass    =pymysql.cursors.DictCursor)

                response = 1
            except Exception as e:
                logging.error("@--UDb openConnection Master --")

    @classmethod
    def _commit(cls):
        cls._connection.commit()

    @classmethod
    def _closeConnection(cls):
        cls._connection.close()

    @classmethod
    def _execute(cls):
        response = 0
        try:
            cursor = cls._connection.cursor()
            cursor.execute(cls._sql)
            cls._result = cursor.fetchall()
            response = 1
        except Exception as e:
            logging.error("@--Execution Query --")

        return response


    @classmethod
    def executeSelect(cls, sql):
        cls._databaseType = "slave"
        cls._sql = sql
        cls._response = cls._generateResponseFail()

        if cls._openConnection() == 0: return cls.response
        if cls._execute() == 0: return cls._response
        if len(cls._result) == 0 : return cls._response

        cls._closeConnection()
        return cls._generateResponseSuccess("select")

    @classmethod
    def executeUpdate(cls, sql):
        cls._databaseType = "master"
        cls._sql = sql
        cls._response = cls._generateResponseFail()

        if cls._openConnection() == 0 : return cls.response
        if cls._execute() == 0 : return cls._response
        if cls._result == 0 : return cls._response

        cls._commit()
        cls._closeConnection()
        return cls._generateResponseSuccess("update")

    @classmethod
    def executeInsert(cls, sql):
        cls._databaseType = "master"
        cls._sql = sql
        cls._response = cls._generateResponseFail()

        if cls._openConnection() == 0: return cls.response
        if cls._execute() == 0: return cls._response

        cls._commit()
        cls._closeConnection()
        return cls._generateResponseSuccess("insert")

    @classmethod
    def executeDelete(cls, sql):
        cls._databaseType = "master"
        cls._sql = sql
        cls._response = cls._generateResponseFail()

        if cls._openConnection() == 0 : return cls.response
        if cls._execute() == 0 : return cls._response
        if len(cls._result) == 0 : return cls._response

        cls._commit()
        cls._closeConnection()
        return cls._generateResponseSuccess("delete")

    @classmethod
    def _generateResponseFail(cls):
        result = HResponse()
        result.StatusCode = 500
        result.Status = False
        result.Data = {}

        return result

    @classmethod
    def _generateResponseSuccess(cls, queryType):
        result = HResponse()
        if queryType == "select":

            datas = []

            for data in cls._result:
                datas.append(data)

            result.StatusCode = 200
            result.Status = True
            result.Data = datas

            return result

        elif queryType == "insert":

            data = {}

            result.StatusCode = 200
            result.Status = True
            result.Data = data

            return result

        elif queryType == "update" or queryType == "delete":
            ids = {}

            result.StatusCode = 200
            result.Status = True
            result.Data = ids

            return result

