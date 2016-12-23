import urllib
from flask import Flask, request

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello World Gae!'

@app.route('/')
def gae_transmitted():
    url = request.values["url"]
    url_open = urllib.urlopen(url)
    return url_open.read()


if __name__ == '__main__':
    app.run(port=80, debug=True)