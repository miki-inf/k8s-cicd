#!/bin/python

# Dependencies:
# pip install flask
# pip install redis
import hotqueue
import flask
import redis
import time
import json
from flask import Response, stream_with_context
from flask import Flask, render_template,request,json
from hotqueue import HotQueue

redis_host="localhost"
app = Flask(__name__)
app.debug = True
queue = HotQueue("myqueue", host=redis_host, port=6379, db=0)

@app.route('/post',methods=['POST','GET'])
def post():
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    if _name and _email:
        queue.put('{"username" : "'+ _name + '","mail" : "'+ _email +'"}')
        return json.dumps({'html':'<span>All fields good !!</span>'})
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'})


@app.route("/")
def main():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0" ,port=9000)
