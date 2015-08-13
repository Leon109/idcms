#coding=utf-8

import os
import sys

workdir = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, workdir + "/../../../")

from app.models import Site, Rack, IpSubnet

class CustomValidator():
    '''自定义检测
    如国检测正确返回 OK
    如国失败返回提示信息
    '''
    def __init__(self, item, item_id, value):
        self.item = item
        self.change_site = Site.query.filter_by(id=int(item_id)).first()
        self.value = value
        self.sm =  {
            "site":self.validate_site,
        }

    def validate_return(self):
        if self.sm.get(self.item, None):
            return self.sm[self.item](self.value)
        else:
            return "OK"

    def validate_site(self, value):
        if Site.query.filter_by(site=value).first():
            return u"更改失败 机房已经存在"
        if Rack.query.filter_by(site=self.change_site.site).first():
            return u"更改失败 这个机房有机架在使用"
        if IpSubnet.query.filter_by(site=self.change_site.site).first():
            return u"更改失败 这个机房有IP子网在使用"
        else:
            return "OK"
