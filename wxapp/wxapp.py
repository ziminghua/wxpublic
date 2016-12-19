# -*- coding: utf-8 -*-
import hashlib
from authentication.WXBizMsgCrypt import WXBizMsgCrypt

appid = 'c41c084feb0d18dd1937ba989f667b42'
token = 'ICcxs5844qOY24rTc1c696X5btR551m2'
encodingAESKey = 'rEotmyYHNsLLXM1olf3ntRx2PXCYXK6eQ3CxWCJegSV'
wxcpt = WXBizMsgCrypt(token, encodingAESKey, appid)


class WxApp(object):
    @staticmethod
    def is_valid(request):
        print '==========开始认证==============='
        print '==========URL参数==============='
        signature = request.values['signature']
        timestamp = request.values['timestamp']
        nonce = request.values['nonce']
        verifyEchoStr = request.values["echostr"]
        param_list = [token, timestamp, nonce]
        param_list.sort()
        sha1 = hashlib.sha1()
        sha1.update(''.join(param_list).encode('utf-8'))
        hashcode = sha1.hexdigest()
        if hashcode == signature:
            return verifyEchoStr
        else:
            return ''
