import mysql.connector
from flask import request
from flask import Flask

#importing Flask (class that holds the entire app)



app = Flask(__name__)
from app import views


connection = mysql.connector.connect(user='kc650', password='rucharity',
                              host='rutgerscharity.cjsliricy0ds.us-east-1.rds.amazonaws.com',
                              database='MainCharityDB')

cursor = connection.cursor()

operation = 'SELECT count(name) from Givers'
for result in cursor.execute(operation, multi=True):
  if result.with_rows:
    print("Rows produced by statement")
    print(result.fetchall())
  else:
    print("Number of rows affected by statement '{}': {}".format(
      result.statement, result.rowcount))


cursor.execute(operation)
print ("Command executed!");



connection.close()
