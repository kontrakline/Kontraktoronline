from Util import UDb

class VendorController(object):
    _requestParam = {}

    @classmethod
    def prepare(cls, requestParam):
        cls._requestParam = requestParam
        return ""

    @classmethod
    def findNearestVendor(cls):
        lat = cls._requestParam.get("lat")
        lng = cls._requestParam.get("lng")
        dist = 10

        sql = "select" \
              " vendor_id," \
              " vendor_name," \
              " round( 6371 * acos( cos( radians("+lat+") ) * cos( radians( vendor_latitude ) ) * cos( radians( vendor_longitude ) - radians("+lng+") ) + sin( radians("+lat+") ) * sin(radians(vendor_latitude)) ), 1) AS distance" \
              " from tbl_vendor" \
              " having distance <= 5.0" \
              " ORDER BY distance "

        return UDb.executeSelect(sql)

    @classmethod
    def highestScoreVendor(cls):
        return ""