#!Users/wangwang/anaconda/envs/python36/bin/python
# -*- coding: UTF-8 -*-

from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'


@app.route('/bbscrawler', methods=['GET'])
def get_bbscrawler():
    return 'ok'


@app.route('/bbscrawler', methods=['POST'])
def post_bbscrawler():
    if request.form['status'] == '0':
        print(request.form['html'])
        return 'ok'
    return 'error'


if __name__ == '__main__':
    app.run()
