#!/bin/python

# Dependencies:
# pip install flask
# pip install redis
import flask
import time
import json
from flask import Response, stream_with_context
from flask import Flask, render_template,request,json
import MySQLdb


dbuser="root"
dbpass=""
dbhost="localhost"
database_name="users"
db1 = MySQLdb.connect(host=dbhost,user=dbuser,passwd=dbpass,db=database_name)
cursor = db1.cursor()
sql = 'SELECT * FROM  USERS'
cursor.execute(sql)
data = cursor.fetchall()
db1.close()


app = Flask(__name__)
app.debug = True



@app.route("/")
def main():
    return render_template('index.html',data=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0" ,port=9001)
