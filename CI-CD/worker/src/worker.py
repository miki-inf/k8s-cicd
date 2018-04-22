import redis
import time
import json
from hotqueue import HotQueue
import MySQLdb


dbuser="root"
dbpass=""
dbhost="localhost"
database_name="users"
redis_host="localhost"
db1 = MySQLdb.connect(host=dbhost,user=dbuser,passwd=dbpass)
cursor = db1.cursor()
sql = 'CREATE DATABASE  IF NOT EXISTS ' +  database_name
print(sql)
cursor.execute(sql)
db1.commit()
db1.close()

db2 = MySQLdb.connect(host=dbhost,  # your host
                     user=dbuser,       # username
                     passwd=dbpass,     # password
                     db=database_name)   # name of the database
# Create a Cursor object to execute queries.
cur = db2.cursor()
sql = """CREATE TABLE IF NOT EXISTS  USERS (
         NAME  CHAR(20) NOT NULL,
         EMAIL  CHAR(50) )"""

# Select data from table using SQL query.
cur.execute(sql)





queue = HotQueue("myqueue", host=redis_host, port=6379, db=0)
for item in queue.consume():
    print(item)
    js=json.loads(item)
    sql = "INSERT INTO USERS(NAME,EMAIL) VALUES ('%s', '%s' )" % (js['username'],js['mail'] )
    cur.execute(sql)
db2.commit()
db2.close()
