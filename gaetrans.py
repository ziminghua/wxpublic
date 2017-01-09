#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
from flask import Flask, request

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello World Gae!'


@app.route('/', methods=["GET", "POST"])
def gae_transmitted():
    url = request.values["url"]
    method = request.values["method"].upper()
    url = urllib.unquote(url)
    if method == "GET":
        url = urllib.unquote(url)
        url_open = urllib.urlopen(url)
        return url_open.read()
    else:
        post_data = request.form
        resp = urllib.urlopen(url, urllib.urlencode(post_data))
        return resp.read()

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

if __name__ == '__main__':
    app.run(port=80)