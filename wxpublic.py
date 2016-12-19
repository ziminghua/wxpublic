# -*- coding: utf-8 -*-
from flask import Flask, request
from wxapp.wxapp import WxApp

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello World!'

@app.route('/')
def wx_main():
    return WxApp.is_valid(request)

if __name__ == '__main__':
    app.run(port=80)
