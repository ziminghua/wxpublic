# -*- coding: utf-8 -*-
from flask import Flask, request
from wxapp.wxapp import WxApp

app = Flask(__name__)

from werkzeug._internal import _log


@app.route('/hello')
def hello_world():
    return 'Hello World!'


@app.route('/', methods=['GET', 'POST'])
def wx_main():
    _log("info", "收到请求")
    if "echostr" in request.values:
        return WxApp.is_valid(request)
    else:
        _log("info", "被动回复")
        return WxApp.reply(request)


if __name__ == '__main__':
    app.run(port=80)
