from Util import UDb

class VendorController(object):
    _requestParam = {}

    @classmethod
    def prepare(cls, requestParam):
        cls._requestParam = requestParam
        return ""

    @classmethod
    def getVendorById(cls):

        sql = "select " \
              "tv.vendor_name, " \
              "tv.vendor_phone, " \
              "tv.vendor_fax, " \
              "tv.vendor_email, " \
              "tv.vendor_description " \
              "from tbl_vendor tv where tv.vendor_id = " + str(cls._requestParam.get("vendor_id"))

        UDb.executeSelect(sql)
        return ""

    @classmethod
    def getVendorList(cls):

        sql = "select tv.vendor_id, " \
              "tv.vendor_name, " \
              "tv.vendor_phone, " \
              "tv.vendor_fax, " \
              "tv.vendor_email, " \
              "tv.vendor_description " \
              "from tbl_vendor tv "

        UDb.executeSelect(sql)
        return ""

    @classmethod
    def getVendorDetail(cls):

        sql = "select tvc.vendor_category_id, " \
                "tvc.vendor_category_name, " \
                "tsw.scale_of_work_id, " \
                "tsw.scale_of_work_name, " \
                "tfc.financial_category_id, " \
                "tfc.financial_category_name, " \
                "tec.experience_category_id, " \
                "tec.experience_category_name, " \
                "tsc.sdm_category_id, " \
                "tsc.sdm_category_name, " \
                "tkc.kalibrasi_category_id, " \
                "tkc.kalibrasi_category_name " \
            "from tbl_vendor_detail tvd,  " \
                "tbl_vendor_category tvc,  " \
                "tbl_scale_of_work tsw,  " \
                "tbl_financial_category tfc, " \ 
                "tbl_experience_category tec,  " \
                "tbl_sdm_category tsc,  " \
                "tbl_administration ta,  " \
                "tbl_kalibrasi_category tkc " \
            "where " \
                "tvd.vendor_detail_vendor_category_id = tvc.vendor_category_id " \
                "and tvc.vendor_detail_scale_of_work_id = tsw.scale_of_work_id " \
                "and tvc.vendor_detail_financial_category_id = tfc.financial_category_id " \
                "and tvc.vendor_detail_experience_category_id = tec.experience_category_id " \
                "and tvc.vendor_detail_sdm_category_id = tsc.sdm_category_id " \
                "and tvc.vendor_detail_administration_id = ta.administration_id " \
                "and tvc.vendor_detail_kalibrasi_category_id = tkc.kalibrasi_category_id " \
                "and tvc.vendor_detail_vendor_id = " + str(cls._requestParam.get("vendor_id"))

        UDb.executeSelect(sql)
        return ""

    @classmethod
    def insertVendor(cls):
        UDb.executeInsert()
        return ""

    @classmethod
    def deleteVendor(cls):
        UDb.executeDelete()
        return ""

    @classmethod
    def updateVendor(cls):
        UDb.executeUpdate()
        return ""