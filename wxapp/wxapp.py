# -*- coding: utf-8 -*-
import hashlib
from authentication.WXBizMsgCrypt import WXBizMsgCrypt
import xml.etree.cElementTree as ET
import city_dic
import urllib
from werkzeug._internal import _log


appid = "c41c084feb0d18dd1937ba989f667b42"
token = "ICcxs5844qOY24rTc1c696X5btR551m2"
encodingAESKey = "rEotmyYHNsLLXM1olf3ntRx2PXCYXK6eQ3CxWCJegSV"
wxcpt = WXBizMsgCrypt(token, encodingAESKey, appid)


class WxApp(object):
    @staticmethod
    def is_valid(request):
        print "==========开始认证==============="
        print "==========URL参数==============="
        signature, timestamp, nonce = WxApp.get_query_param(request)
        verifyEchoStr = request.values["echostr"]
        param_list = [token, timestamp, nonce]
        param_list.sort()
        sha1 = hashlib.sha1()
        sha1.update("".join(param_list).encode("utf-8"))
        hashcode = sha1.hexdigest()
        if hashcode == signature:
            return verifyEchoStr
        else:
            return ""

    @staticmethod
    def weather_search(request):
        _log("info", "开始")
        signature, timestamp, nonce = WxApp.get_query_param(request)
        _log("info", "%s %s %s" % (signature, timestamp, nonce))
        content, to_user = WxApp.get_content(request)
        _log("info", "%s %s" % (content, to_user))
        ret, encrypt_xml = WxApp.send_data(content, to_user, nonce)
        _log("info", "%s %s" % (ret, encrypt_xml))
        #city_string = WxApp.get_content(request)
        #city_code = city_dic.city_dic[city_string]
        #url_open = urllib.urlopen("http://www.weather.com.cn/data/cityinfo/%s.html" % city_code)
        #s = url_open.read()
        #s = WxApp.get_content(request).encode("utf-8")
        if ret == 0:
            return encrypt_xml
        else:
            return ret

    @staticmethod
    def get_content(request):
        signature, timestamp, nonce = WxApp.get_query_param(request)
        post_content = request.data
        ret, xml_content = wxcpt.DecryptMsg(post_content, signature, timestamp, nonce)
        xml_tree = ET.fromstring(xml_content)
        return xml_tree.find("Content").text, xml_tree.find("ToUserName")


    @staticmethod
    def get_query_param(request):
        signature = request.values["msg_signature"]
        timestamp = request.values["timestamp"]
        nonce = request.values["nonce"]
        return signature, timestamp, nonce

    @staticmethod
    def send_data(content, to_user, nonce):
        template = "<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[ziminghua88]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[text]]></MsgType><Content><![CDATA[%s]]></Content></xml>"
        return wxcpt.EncryptMsg(template % to_user, content, nonce)


